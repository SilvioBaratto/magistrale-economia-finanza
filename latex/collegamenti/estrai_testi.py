#!/usr/bin/env python3
"""Extract the legal text of the hub articles of edges.yaml into testi.yaml.

The sources are the official texts that were once under Moodle/03-Legislazione-Bancaria-1/Normativa/
(they are in the git history; this script reads them from wherever they are restored):

    python3 estrai_testi.py --tub tub.pdf --reg reg.pdf --cost costituzione.md

* TUB: the consolidated text of 22 January 2026 (Wolters Kluwer export). Paragraphs repealed
  but still printed between square brackets are kept and marked ``abrogato``.
* Costituzione: the markdown extract in notebooklm/fonti-estratte/.
* Reg. UE 1024/2013: the original text of the Official Journal, read column by column.

Nothing is rewritten: only layout noise (headers, footnote markers, hyphenation) is removed.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEFAULT_EDGES = HERE / "edges.yaml"
DEFAULT_OUT = HERE / "testi.yaml"

TUB_SOURCE = "TUB (d.lgs. 385/1993), testo consolidato al 22 gennaio 2026"
COST_SOURCE = "Costituzione della Repubblica italiana"
REG_SOURCE = "Reg. (UE) n. 1024/2013, testo originale (GU L 287 del 29.10.2013, non consolidato)"

_NOISE = re.compile(r"^\s*(WOLTERS KLUWER|One\s*$|One\s+Legale)|Copyright Wolters Kluwer", re.I)
_STRUCTURE = re.compile(r"^\s*(TITOLO|Titolo|CAPO|Capo|SEZIONE|Sezione|PARTE|Parte)\s+[IVXLC\d]+\b")
_ARTICLE = re.compile(r"^Art\.\s+(\d+(?:-[a-z]+)*)\s+(.*)$")
_FOOTNOTE = re.compile(r"\s*\[\d+\]")
_COMMA = re.compile(r"^\[?\s*(\d+(?:\s*[-\u2013]\s*(?:[a-z]\s*){2,12})?)\s*\.\s+(.*)$")
_SUBITEM = re.compile(r"^\[?\s*((?:[a-z]{1,2}(?:-[a-z]+)?|\d+)\.\d+)\s*\)\s*(.*)$")
_LETTER = re.compile(r"^\[?\s*((?:[a-z]\s*)+(?:-\s*(?:[a-z]\s*)+)*)\)\s*(.*)$")
_NUMBERED = re.compile(r"^\[?\s*(\d+)\s*\)\s+(.*)$")
_BULLET = re.compile(r"^[-\u2013\u2022]\s+(.*)$")
_LETTER_LABEL = re.compile(r"^[a-z]{1,2}(?:-[a-z]{2,12})?$")
_LATIN_SUFFIX = re.compile(r"^([a-z])(bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)$")
_APOSTROPHE = re.compile(r"(?<=[A-Za-zÀ-ÿ])(['’])\s+(?=[A-Za-zÀ-ÿ0-9])")


def _clean(text: str) -> str:
    """Normalize ligatures and spacing in one paragraph of running text."""
    text = unicodedata.normalize("NFKC", text).replace("­", "")
    text = _APOSTROPHE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def _is_heading(line: str) -> bool:
    """Whether the line is a Titolo/Capo heading printed in capitals between two articles."""
    text = line.strip()
    return len(text) > 3 and text.upper() == text and any(c.isalpha() for c in text) and not re.search(r"[\d\[\]]", text)


def _split_label(line: str):
    """Return (level, label, rest) when the line opens a comma, a letter, a numbered item or a bullet, else None."""
    m = _COMMA.match(line)
    if m:
        return 0, re.sub(r"\s+", "", m.group(1)).replace("\u2013", "-") + ".", m.group(2)
    m = _SUBITEM.match(line)
    if m:
        return 2, m.group(1) + ")", m.group(2)
    m = _LETTER.match(line)
    if m:
        label = re.sub(r"\s+", "", m.group(1))
        label = _LATIN_SUFFIX.sub(r"\1-\2", label)
        if _LETTER_LABEL.match(label):
            return 1, label + ")", m.group(2)
    m = _NUMBERED.match(line)
    if m:
        return 2, m.group(1) + ")", m.group(2)
    m = _BULLET.match(line)
    if m:
        return 2, "\u2013", m.group(1)
    return None


def _paragraphs(lines: list[str], bracketed_repeal: bool) -> list[dict]:
    """Group wrapped lines into paragraphs: one per comma, letter, numbered item or bullet.

    Args:
        lines: Text lines of one article, without heading and footnotes.
        bracketed_repeal: Whether a paragraph wrapped in square brackets is a repealed one
            (true for the consolidated TUB, whose printed brackets mean "abrogato").
    """
    blocks: list[dict] = []
    after_blank = True
    for raw in lines:
        line = raw.strip()
        if not line:
            after_blank = True
            continue
        opened = _split_label(line)
        bracket = bracketed_repeal and line.startswith("[")
        if opened:
            level, label, rest = opened
            blocks.append({"level": level, "label": label, "parts": [rest], "bracket": bracket})
        elif blocks and (not after_blank or line[:1].islower()):
            # A lower-case start after a blank line is the rest of a paragraph split by a page break.
            blocks[-1]["parts"].append(line)
        else:
            blocks.append({"level": 0, "label": "", "parts": [line.lstrip("[ ") if bracket else line], "bracket": bracket})
        after_blank = False
    out, repealed = [], False
    for b in blocks:
        repealed = repealed or b["bracket"]
        text = _clean(_FOOTNOTE.sub("", " ".join(b["parts"])))
        closes = repealed and text.endswith("]")
        if closes:
            text = text[:-1].rstrip()
        if text:
            out.append({"label": b["label"], "text": text, "level": b["level"], "abrogato": repealed})
        if closes:
            repealed = False
    return out


def tub_article(lines: list[str], art: str) -> dict | None:
    """Return the text of ``art`` from the lines of the consolidated TUB, or None when it is absent."""
    starts = [(i, _ARTICLE.match(line)) for i, line in enumerate(lines)]
    starts = [(i, m) for i, m in starts if m]
    for k, (i, m) in enumerate(starts):
        if m.group(1) != art:
            continue
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        body = []
        for line in lines[i + 1:end]:
            if line.strip() == "Note:":
                break
            if _NOISE.search(line) or _STRUCTURE.match(line) or _is_heading(line):
                continue
            body.append(line)
        rubrica, vigore = m.group(2), ""
        for k2, line in enumerate(body[:3]):
            at = line.lower().find("in vigore dal")
            if at >= 0:
                vigore = _clean(line[at + len("in vigore dal"):])
                rubrica = " ".join([rubrica, *body[:k2], line[:at]])
                body = body[k2 + 1:]
                break
        return {"fonte": TUB_SOURCE, "rubrica": _clean(_FOOTNOTE.sub("", rubrica)), "vigore": vigore,
                "par": _paragraphs(body, bracketed_repeal=True)}
    return None


def cost_article(md: str, art: str) -> dict | None:
    """Return the text of an article of the Costituzione from the markdown extract; paragraphs become commi."""
    sections = re.split(r"\n(\d+)\.\s*\n", "\n" + md)
    # split() returns [preamble, num, body, num, body, ...]
    for num, body in zip(sections[1::2], sections[2::2]):
        if num != art:
            continue
        body = body.split("-----------------------")[0]
        par, comma = [], 0
        for chunk in (c.strip() for c in body.split("\n\n")):
            if not chunk or re.match(r"^\(\d+\)\s+(Vedi|Lettera|Comma|Articolo)", chunk):
                continue
            text = _clean(re.sub(r"\s*(\[\d+\]|\(\d+\))", "", chunk))
            lettera = re.match(r"^([a-z])\)\s+(.*)$", text)
            if lettera:
                par.append({"label": lettera.group(1) + ")", "text": lettera.group(2), "level": 1, "abrogato": False})
            else:
                comma += 1
                par.append({"label": f"{comma}.", "text": text, "level": 0, "abrogato": False})
        return {"fonte": COST_SOURCE, "rubrica": "", "vigore": "", "par": par}
    return None


def _pdftotext(pdf: Path, *args: str) -> str:
    done = subprocess.run(["pdftotext", *args, str(pdf), "-"], capture_output=True, text=True, check=True)
    return done.stdout


_REG_NOISE = re.compile(r"^(IT|L \d+/\d+|Gazzetta ufficiale.*|dell’Unione europea|\d\d\.\d\d\.\d{4})$")


def reg_article(pdf: Path, art: str) -> dict | None:
    """Return one article of a two-column Official Journal PDF, reading each column in order."""
    pages = _pdftotext(pdf).split("\f")
    first = next((i for i, p in enumerate(pages, 1) if re.search(rf"^Articolo {art}$", p, re.M)), None)
    if first is None:
        return None
    lines: list[str] = []
    for page in range(first, min(first + 3, len(pages)) + 1):
        for x in (0, 298):
            text = _pdftotext(pdf, "-f", str(page), "-l", str(page), "-x", str(x), "-y", "40", "-W", "298", "-H", "770")
            lines += text.split("\n")
    start = next(i for i, line in enumerate(lines) if line.strip() == f"Articolo {art}")
    stop = next((i for i, line in enumerate(lines[start + 1:], start + 1) if re.match(r"^Articolo \d+$", line.strip())), len(lines))
    body = [line for line in lines[start + 1:stop] if not _REG_NOISE.match(line.strip())]
    rubrica = _clean(body[0]) if body else ""
    merged, i = [], 1
    while i < len(body):
        cur = body[i].strip()
        if re.fullmatch(r"\d+\.", cur) and i + 1 < len(body):
            merged.append(f"{cur} {body[i + 1].strip()}")
            i += 2
            continue
        merged.append(body[i])
        i += 1
    joined = "\n".join(merged).replace("­\n", "")
    return {"fonte": REG_SOURCE, "rubrica": rubrica, "vigore": "", "par": _paragraphs(joined.split("\n"), bracketed_repeal=False)}


def main() -> int:
    """Write testi.yaml with the text of every hub article that a source is given for."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edges", type=Path, default=DEFAULT_EDGES)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--tub", type=Path, help="consolidated TUB, PDF with a text layer")
    ap.add_argument("--reg", type=Path, help="Reg. UE 1024/2013, PDF with a text layer")
    ap.add_argument("--cost", type=Path, help="markdown extract of Costituzione artt. 41, 47, 117")
    args = ap.parse_args()

    graph = yaml.safe_load(args.edges.read_text(encoding="utf-8"))
    hubs = [(nid, spec) for nid, spec in graph["nodes"].items() if spec.get("hub")]
    tub_lines = _pdftotext(args.tub, "-layout").split("\n") if args.tub else []
    cost_md = args.cost.read_text(encoding="utf-8") if args.cost else ""
    texts, missing = {}, []
    for nid, spec in hubs:
        art = str(spec.get("art") or "")
        found = None
        if spec["fonte"] == "TUB" and tub_lines and art:
            found = tub_article(tub_lines, art)
        elif spec["fonte"] == "COST" and cost_md and art:
            found = cost_article(cost_md, art)
        elif nid.startswith("UE:reg-ue-1024-2013:") and args.reg and art:
            found = reg_article(args.reg, art)
        if found:
            texts[nid] = found
        else:
            missing.append(nid)
    args.out.write_text("# Text of the hub articles, extracted by estrai_testi.py. Not to be edited by hand.\n"
                        + yaml.safe_dump(texts, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print(f"{len(texts)} articoli estratti; senza testo: {', '.join(missing) or 'nessuno'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
