#!/usr/bin/env python3
"""Controlli strutturali sulle tracce d'orale, prima di compilarle.

    python3 verifica_orale.py                                   # tutti i corsi
    python3 verifica_orale.py --corso legislazione-bancaria-1   # un corso
    python3 verifica_orale.py --quiet                           # solo i problemi

Le tracce stanno in esami/<corso>/src/, le bozze in esami/<corso>/.bozze/.

Due famiglie di controlli:

* FORMATO — quello che romperebbe pandoc/XeLaTeX o il filtro dei callout:
  front matter, una sola intestazione di capitolo, domande «## D<n> — ...»
  numerate in sequenza, ognuna con Domanda, Risposta da dare e
  Spiegazione, callout con riga vuota prima e dopo, niente
  intestazioni di livello 3, wikilink, immagini o blocchi di codice.

* COMPLETEZZA — il confronto con la bozza in .bozze/. La revisione può solo
  aggiungere: se il file finale ha meno domande o meno righe della bozza,
  l'agente che l'ha riscritto si e' fermato a meta' ed e' stato troncato.
  E' il guasto piu' insidioso, perche' il file resta sintatticamente valido.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ESAMI = Path(__file__).resolve().parent / "esami"
CORSI = ("legislazione-bancaria-1", "legislazione-bancaria-2")
# Set per course by main(); controlla() reads the drafts from BOZZE.
SRC, BOZZE = Path(), Path()

Q_RE = re.compile(r"^##\s+D(\d+)\s+—\s+(.+)$")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\]")
KINDS = {"question", "success", "info", "tip", "warning", "note", "abstract", "example"}


def frontmatter(lines: list[str]) -> tuple[dict, int]:
    if not lines or lines[0].strip() != "---":
        return {}, 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta = {}
            for line in lines[1:i]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            return meta, i + 1
    return {}, 0


def controlla(path: Path) -> list[str]:
    testo = path.read_text(encoding="utf-8")
    lines = testo.splitlines()
    problemi: list[str] = []

    meta, start = frontmatter(lines)
    if not meta:
        problemi.append("front matter YAML assente")
    else:
        for chiave in ("title", "subtitle"):
            if not meta.get(chiave):
                problemi.append(f"front matter: manca «{chiave}»")

    capitoli = [i for i, l in enumerate(lines) if l.startswith("# ")]
    if len(capitoli) != 1:
        problemi.append(f"attese 1 intestazione di capitolo, trovate {len(capitoli)}")

    # domande numerate in sequenza
    domande = [(i, Q_RE.match(l)) for i, l in enumerate(lines) if l.startswith("## ")]
    malformate = [i + 1 for i, m in domande if not m]
    if malformate:
        problemi.append(f"intestazioni ## non nella forma «## D<n> — titolo» alle righe {malformate[:5]}")
    numeri = [int(m.group(1)) for _, m in domande if m]
    if numeri and numeri != list(range(1, len(numeri) + 1)):
        atteso = [n for n, k in zip(numeri, range(1, len(numeri) + 1)) if n != k]
        problemi.append(f"numerazione delle domande non progressiva (prime anomalie: {atteso[:5]})")

    # sintassi che rompe la compilazione
    for i, l in enumerate(lines):
        if l.startswith("### "):
            problemi.append(f"intestazione di livello 3 alla riga {i + 1}")
            break
    if "[[" in testo:
        problemi.append("wikilink [[...]] presenti")
    if re.search(r"^!\[", testo, re.MULTILINE):
        problemi.append("immagini markdown presenti")
    if "```" in testo:
        problemi.append("blocchi di codice presenti")

    # callout: tipo noto, riga vuota prima, corpo non vuoto
    for i, l in enumerate(lines):
        m = CALLOUT_RE.match(l)
        if not m:
            continue
        if m.group(1).lower() not in KINDS:
            problemi.append(f"callout di tipo sconosciuto «{m.group(1)}» alla riga {i + 1}")
        if i > 0 and lines[i - 1].strip() != "":
            problemi.append(f"callout senza riga vuota prima, riga {i + 1}")
        if i + 1 >= len(lines) or not lines[i + 1].startswith(">"):
            problemi.append(f"callout senza corpo, riga {i + 1}")

    # ogni domanda ha i suoi tre blocchi: domanda, risposta da dare, spiegazione
    confini = [i for i, _ in domande] + [len(lines)]
    for k in range(len(confini) - 1):
        blocco = lines[confini[k]:confini[k + 1]]
        tipi = {CALLOUT_RE.match(l).group(1).lower() for l in blocco if CALLOUT_RE.match(l)}
        etichetta = lines[confini[k]].strip()
        if "question" not in tipi:
            problemi.append(f"«{etichetta}» senza callout [!question]")
        if "success" not in tipi:
            problemi.append(f"«{etichetta}» senza callout [!success]")
        if "info" not in tipi:
            problemi.append(f"«{etichetta}» senza callout [!info] Spiegazione")

    # completezza rispetto alla bozza: la revisione puo' solo aggiungere
    bozza = BOZZE / path.name
    if bozza.exists():
        b_lines = bozza.read_text(encoding="utf-8").splitlines()
        b_dom = len([l for l in b_lines if Q_RE.match(l)])
        if len(numeri) < b_dom:
            problemi.append(f"TRONCATO: {len(numeri)} domande contro le {b_dom} della bozza")
        elif len(lines) < len(b_lines) * 0.9:
            problemi.append(f"TRONCATO: {len(lines)} righe contro le {len(b_lines)} della bozza")
    else:
        problemi.append("nessuna bozza di riferimento in .bozze/ (completezza non verificabile)")

    return problemi


def rinumera(path: Path) -> int:
    """Riporta le intestazioni «## D<n> — titolo» a una sequenza continua.

    Serve dopo che un agente ha aggiunto domande in coda: la numerazione e'
    l'unica cosa che un'aggiunta chirurgica non puo' sistemare da sola, e
    farla a mano e' il modo piu' rapido per introdurre un buco.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    n, cambi = 0, 0
    for i, l in enumerate(lines):
        m = Q_RE.match(l)
        if not m:
            continue
        n += 1
        if int(m.group(1)) != n:
            lines[i] = f"## D{n} — {m.group(2)}"
            cambi += 1
    if cambi:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return cambi


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corso", action="append", choices=CORSI,
                    help="limita a un corso (ripetibile); di default tutti")
    ap.add_argument("--quiet", action="store_true", help="stampa solo i file con problemi")
    ap.add_argument("--rinumera", action="store_true",
                    help="riporta le domande a una numerazione continua prima di controllare")
    args = ap.parse_args()

    global SRC, BOZZE
    guasti = 0
    for corso in args.corso or CORSI:
        SRC, BOZZE = ESAMI / corso / "src", ESAMI / corso / ".bozze"
        print(f"== {corso}")
        guasti += verifica_corso(args)
    return 1 if guasti else 0


def verifica_corso(args: argparse.Namespace) -> int:
    """Check one course's tracks; return how many files have problems."""
    if args.rinumera:
        for p in sorted(SRC.glob("*.md")):
            cambi = rinumera(p)
            if cambi:
                print(f"  rinumerate {cambi} domande in {p.name}")

    files = sorted(SRC.glob("*.md"))
    if not files:
        print("nessuna traccia in src/")
        return 0

    guasti = 0
    for p in files:
        problemi = controlla(p)
        if problemi:
            guasti += 1
            print(f"✗ {p.name}")
            for x in problemi:
                print(f"    {x}")
        elif not args.quiet:
            print(f"✓ {p.name}")
    print(f"\n{len(files) - guasti}/{len(files)} tracce integre")
    return guasti


if __name__ == "__main__":
    raise SystemExit(main())
