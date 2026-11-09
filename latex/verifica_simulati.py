#!/usr/bin/env python3
"""Check the simulated Finanza Strategica exams before and after any edit.

Run it with no arguments for every exam followed by the cross-exam checks, with exam numbers
(``python3 verifica_simulati.py 3 7``) for those exams only, and with ``--lettere`` to also list
every option letter quoted in the answer key next to the option it points to.

Per exam (``esami/finanza-strategica/src/FSTR_{Esame,Soluzioni}_Simulato_NN.md`` and the PDFs):
structure of the paper, 20 questions with options A/B/C, balance of the answer key, answer length
bias, periodic key patterns, forbidden wording, TeX left visible in the PDF. Across exams:
duplicate questions, repeated company names, repeated comparable rows and notes covered.
Exit status 1 when any problem is found.
"""
from __future__ import annotations

import argparse
import collections
import difflib
import itertools
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "latex" / "esami" / "finanza-strategica" / "src"
OUT = REPO / "esami" / "finanza-strategica"
NOTES = REPO / "obsidian" / "11-Finanza-Strategica"

QUESTION = re.compile(r'::::: \{\.callout kind="question" heading="(\d+)"\}\n(.*?)\n:::::', re.S)
KEY = re.compile(r"\*\*(\d+)\) ([ABC])\.")
LETTER_REF = re.compile(
    r"\(([ABC])\)|\b(?:[Ll]a|[Ll]e|alternativ[ae]|opzion[ei]|risposta)\s+([ABC])\b|\b([ABC]) e ([ABC])\b")
LENGTH_BIAS = (2, 8)  # correct option may be the longest in 2-8 questions out of 20
SKIP_HEADING = re.compile(
    r"^(Oggetto del capitolo|Inquadramento|Introduzione|Collocazione nel corso|Introduzione e riferimenti"
    r"|Introduzione e collocazione nel corso)", re.I)


def options(block: str) -> dict[str, str]:
    """Map the letters A, B, C of a question block to the text of each option.

    Args:
        block: Markdown of one question, options written ``A.  text`` with two spaces.

    Returns:
        The options found; fewer than three means the block is malformed.
    """
    return dict(re.findall(r"^([ABC])\.  (.+)$", block, re.M))


def check_exam(n: int, show_letters: bool) -> tuple[list[str], str]:
    """Return the problems of exam ``n`` and the text of its answer key."""
    problems: list[str] = []
    paper_path = SRC / f"FSTR_Esame_Simulato_{n:02d}.md"
    key_path = SRC / f"FSTR_Soluzioni_Simulato_{n:02d}.md"
    if not paper_path.exists() or not key_path.exists():
        return [f"[{n:02d}] missing paper or solutions"], ""
    paper, solutions = paper_path.read_text(), key_path.read_text()

    blocks = QUESTION.findall(paper)
    if [int(h) for h, _ in blocks if h.isdigit()][:20] != list(range(1, 21)):
        problems.append(f"[{n:02d}] test numbering is not 1-20")
    for heading, body in blocks:
        if "\n\nA.  " not in body:
            continue
        if [k for k in options(body)] != ["A", "B", "C"]:
            problems.append(f"[{n:02d}] question {heading}: options are not A, B, C with two spaces")
        if re.search(r"tutte le precedenti|slide|lezione \d", body, re.I):
            problems.append(f"[{n:02d}] question {heading}: forbidden wording")
    for needle in ('# Test a risposta multipla', '# Esercizi', '# Domande di teoria',
                   'heading="Esercizio 1"', 'heading="Esercizio 2"', 'heading="Domanda A"',
                   'heading="Domanda B"', "Barrare una sola risposta. Una sola risposta è corretta."):
        if needle not in paper:
            problems.append(f"[{n:02d}] paper lacks {needle!r}")
    if re.search(r"Risposta segnata|\bSoluzione\b", paper):
        problems.append(f"[{n:02d}] paper contains solution wording")

    key = KEY.findall(solutions)
    letters = "".join(k[1] for k in key)
    if [int(k[0]) for k in key] != list(range(1, 21)):
        problems.append(f"[{n:02d}] key numbering is not 1-20")
    count = collections.Counter(letters)
    if any(not 6 <= count[x] <= 8 for x in "ABC"):
        problems.append(f"[{n:02d}] A/B/C balance {dict(count)}")
    if re.search(r"(.)\1\1", letters):
        problems.append(f"[{n:02d}] three equal answers in a row: {letters}")
    for i in range(len(letters) - 8):
        w = letters[i:i + 9]
        if w[:3] == w[3:6] == w[6:] and len(set(w[:3])) == 3:
            problems.append(f"[{n:02d}] answers repeat a 3-letter cycle at questions {i + 1}-{i + 9}: {w}")
            break

    longest = 0
    for (heading, body), (_, correct) in zip(blocks, key):
        opts = options(body)
        if len(opts) == 3:
            lens = {k: len(v) for k, v in opts.items()}
            top = max(lens.values())
            longest += lens[correct] == top and list(lens.values()).count(top) == 1
    if not LENGTH_BIAS[0] <= longest <= LENGTH_BIAS[1]:
        problems.append(f"[{n:02d}] correct option is the longest in {longest}/20 (allowed {LENGTH_BIAS})")
    print(f"[{n:02d}] key {letters}  A={count['A']} B={count['B']} C={count['C']}  longest-correct {longest}/20")

    for pdf_name in (f"FSTR_Esame_Simulato_{n:02d}.pdf", f"FSTR_Soluzioni_Simulato_{n:02d}.pdf"):
        pdf = OUT / pdf_name
        if not pdf.exists():
            problems.append(f"[{n:02d}] {pdf_name} not built")
            continue
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        for m in re.finditer(r"\$|\\[a-zA-Z]{2,}|\?\?|\{,\}", text):
            problems.append(f"[{n:02d}] {pdf_name}: stray TeX near {text[max(0, m.start() - 30):m.end() + 30]!r}")

    if show_letters:
        for (heading, body), (_, correct) in zip(blocks, key):
            opts = options(body)
            m = re.search(rf"\*\*{heading}\) [ABC]\.\*\*(.*?)(?=\n\n\*\*\d+\)|\n\n#)", solutions, re.S)
            for ref in LETTER_REF.finditer(m.group(1) if m else ""):
                for letter in (g for g in ref.groups() if g):
                    print(f"   Q{heading} key {correct}: {letter} = {opts.get(letter, '?')[:90]}")
    return problems, letters


def check_citations(solutions: dict[int, str]) -> list[str]:
    """Require every ``«title»`` quoted next to ``FSTR NN`` to exist in that note.

    Args:
        solutions: Markdown of the answer keys, by exam number.

    Returns:
        One message per quoted title that the cited note does not contain.
    """
    norm = lambda s: re.sub(r"\s+", " ", s.replace("*", "").replace("`", "")).strip().lower()
    bodies = {f.name.split()[1][:2]: norm(f.read_text()) for f in NOTES.glob("FSTR *.md")}
    problems = []
    total = 0
    for n, text in solutions.items():
        for note, segment in re.findall(r"FSTR (\d\d)(?:-full)?(.*?)(?=FSTR \d\d|\)\*|\)\s|$)", text, re.S):
            for title in re.findall(r"«([^»]+)»", segment):
                total += 1
                if note not in bodies or norm(title) not in bodies[note]:
                    problems.append(f"[{n:02d}] cites «{title}» in FSTR {note}, which does not contain it")
    print(f"citations checked against the notes: {total}")
    return problems


def check_across(numbers: list[int]) -> list[str]:
    """Duplicate questions, names, comparable rows and notes coverage across the given exams."""
    problems: list[str] = []
    papers = {n: (SRC / f"FSTR_Esame_Simulato_{n:02d}.md").read_text() for n in numbers}
    solutions = {n: (SRC / f"FSTR_Soluzioni_Simulato_{n:02d}.md").read_text() for n in numbers}
    norm = lambda s: re.sub(r"\W+", " ", s.lower()).strip()

    questions = []
    for n, paper in papers.items():
        for heading, body in QUESTION.findall(paper):
            if "\n\nA.  " in body:
                stem, rest = body.split("\n\nA.  ", 1)
                questions.append((n, heading, norm(stem), norm(rest)))
    for (n1, h1, s1, r1), (n2, h2, s2, r2) in itertools.combinations(questions, 2):
        if n1 == n2:
            continue
        a = difflib.SequenceMatcher(None, s1, s2).ratio()
        b = difflib.SequenceMatcher(None, r1, r2).ratio()
        if a > 0.80 or b > 0.80:
            problems.append(f"similar questions {n1:02d} Q{h1} / {n2:02d} Q{h2} (stem {a:.2f}, options {b:.2f})")

    names: dict[str, list[int]] = collections.defaultdict(list)
    rows: dict[tuple, list[int]] = collections.defaultdict(list)
    for n, paper in papers.items():
        for m in re.finditer(r"^\| ([A-Z][\w' ]+?) \| [A-Z]{1,3} \| \d+% \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", paper, re.M):
            names[m.group(1).strip()].append(n)
            rows[m.groups()[1:]].append(n)
        for m in re.finditer(r"all'impresa ([A-Z][\w ]+?) S\.p\.A\.", paper):
            names[m.group(1).strip()].append(n)
    for name, where in names.items():
        if len(set(where)) > 1:
            problems.append(f"company name {name!r} used in exams {sorted(set(where))}")
    for row, where in rows.items():
        if len(set(where)) > 1:
            problems.append(f"comparable row {row} in exams {sorted(set(where))}")

    cited: set[tuple[str, str]] = set()
    for text in solutions.values():
        # One citation may name several notes: "(FSTR 11, «A»; FSTR 10, «B»)". A segment runs
        # from one "FSTR NN" to the next, so each title is attributed to the note before it.
        for note, segment in re.findall(r"FSTR (\d\d)(?:-full)?(.*?)(?=FSTR \d\d|\)\*|\)\s|$)", text, re.S):
            cited.update((note, t.strip()) for t in re.findall(r"«([^»]+)»", segment))
    total = hit = 0
    missing = []
    for note in sorted(NOTES.glob("FSTR *.md")):
        num = note.name.split()[1][:2]
        if num in ("00", "13", "14"):
            continue
        for line in note.read_text().splitlines():
            if line.startswith("## ") and not SKIP_HEADING.match(line[3:].strip()):
                title = line[3:].strip()
                total += 1
                if any(k[0] == num and (k[1] == title or k[1] in title or title in k[1]) for k in cited):
                    hit += 1
                else:
                    missing.append(f"FSTR {num} - {title}")
    problems += check_citations(solutions)
    print(f"notes covered: {hit}/{total} sections of lessons 01-12 (the rest are cases and worked examples)")
    for m in missing:
        print(f"   not cited: {m}")
    return problems


def check_volumes() -> list[str]:
    """Check the two single-file editions: they exist, hold ten appelli and show no stray TeX.

    Returns:
        One message per problem found.
    """
    problems = []
    for name, marker, expected in (("FSTR_Esame_Simulato_Completo.pdf", "Esercizio 1.", 10),
                                   ("FSTR_Soluzioni_Simulato_Completo.pdf", "Risultato.", 20)):
        pdf = OUT / name
        if not pdf.exists():
            problems.append(f"{name} not built (python3 build_esami.py --corso finanza-strategica --volume)")
            continue
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        chapters = len(re.findall(r"^\d{1,2} +Appello simulato", text, re.M))
        if chapters != 10 or text.count(marker) != expected:
            problems.append(f"{name}: {chapters} chapters and {text.count(marker)} x {marker!r}, expected 10 and {expected}")
        for m in re.finditer(r"\$|\\[a-zA-Z]{2,}|\?\?|\{,\}", text):
            problems.append(f"{name}: stray TeX near {text[max(0, m.start() - 30):m.end() + 30]!r}")
    return problems


def main() -> int:
    """Run the per-exam checks, then the cross-exam ones when several exams are selected.

    Returns:
        1 when any problem was found, 0 otherwise.
    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("exams", nargs="*", type=int, help="exam numbers (default: 1-10)")
    ap.add_argument("--lettere", action="store_true", help="list every letter quoted in the key")
    args = ap.parse_args()
    numbers = args.exams or list(range(1, 11))
    problems: list[str] = []
    for n in numbers:
        found, _ = check_exam(n, args.lettere)
        problems += found
    if len(numbers) > 1:
        problems += check_across(numbers)
        problems += check_volumes()
    print("\nPROBLEMS" if problems else "\nno problems")
    print("\n".join(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
