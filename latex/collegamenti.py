#!/usr/bin/env python3
"""Add a "Collegamenti" part to a subject's dispensa.

For every hub article of the graph in collegamenti/edges.yaml it draws one
page: the article at the centre, the provisions it exchanges with arranged in
bands by level of source (Costituzione, diritto UE, TUB, fonti secondarie) and
arrows that carry the relation word (fonda, impone, attribuisce, delega...).
In the running text every "art. N" of a hub becomes a tappable link to its page.

    python3 collegamenti.py --subject 03-Legislazione-Bancaria-1

The result is a separate PDF under ../dispense/prova-collegamenti/; the regular
dispensa and ../obsidian/ are left untouched.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

import build

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "collegamenti"
DEFAULT_EDGES = DATA / "edges.yaml"
DEFAULT_TESTI = DATA / "testi.yaml"
HEADER = DATA / "header.tex"
OUT_DIR = ROOT.parent / "dispense" / "prova-collegamenti"

BAND_ORDER = ("COST", "UE", "TUB", "SEC")
BAND_TITLE = {"COST": "Costituzione", "UE": "Diritto UE", "TUB": "TUB e leggi", "SEC": "Fonti secondarie"}
FONTE_BAND = {"COST": "COST", "UE": "UE", "TUB": "TUB", "CC": "TUB", "ALTRO": "TUB", "SEC": "SEC"}
FONTE_COLOR = {"COST": "fCost", "UE": "fUE", "TUB": "fTub", "SEC": "fSec", "CC": "fAlt", "ALTRO": "fAlt"}
BAND_COLOR = {band: FONTE_COLOR[band] for band in BAND_ORDER}
BAND_LEVEL = {band: i for i, band in enumerate(BAND_ORDER)}

# Relations between norms of the same rank are drawn dashed; the others link
# one level of the hierarchy to another.
HORIZONTAL_RELS = frozenset({"richiama", "condiziona", "integra", "deroga", "sanziona"})

# Raw LaTeX: the text font has no check glyph, and the intro goes through pandoc, not tex().
CHECK_MARK = "`\\textcolor{fSec}{\\ding{51}}`{=latex}"
AGENT_CHECKED = frozenset({"doppio controllo", "citazione + campione"})

REL_GLOSS = {
    "fonda": "una fonte superiore dà il fondamento a una norma inferiore",
    "impone": "obbliga a un risultato o a una condotta",
    "attribuisce": "assegna una competenza o un potere a un'autorità",
    "delega": "rinvia la disciplina di dettaglio a una fonte secondaria",
    "recepisce": "la norma nazionale traspone un atto dell'Unione",
    "attua": "una fonte specifica dà attuazione a una più generale",
    "richiama": "rinvio generico fra norme",
    "condiziona": "subordina l'efficacia di una norma a un requisito",
    "integra": "aggiunge un criterio o una disciplina a un procedimento",
    "deroga": "regime speciale rispetto alla regola generale",
    "sanziona": "collega una sanzione alla violazione",
    "altro": "altra relazione, descritta nel testo",
}

# Diagram geometry in cm; the band width equals the text width of the template.
BAND_W = 16.0
NODE_X0, NODE_W_AREA = -7.2, 15.0
NODE_W, NODE_H = 3.1, 1.4
ROW_GAP, BAND_PAD, BAND_GAP = 0.8, 0.4, 1.2
ROW_MAX = 3

# A hub page draws at most this many edges that touch the hub, plus a few among its
# neighbours; each level of the hierarchy keeps its best edges before the rest compete on weight.
MAX_INCIDENT = 8
MAX_BETWEEN_NEIGHBOURS = 2
PER_BAND_FLOOR = 2
MAX_REVIEW_LISTED = 12

FENCE = build.FENCE


# --------------------------------------------------------------------------- graph
@dataclass(frozen=True)
class Node:
    """A provision of some source: an article, or a whole instrument when ``art`` is empty.

    Attributes:
        id: Stable key such as ``TUB:14`` or ``UE:reg-ue-1024-2013:4``.
        fonte: Level of the source: COST, UE, TUB, SEC, CC or ALTRO.
        doc: Canonical name of the instrument, e.g. ``Reg. UE 1024/2013``.
        art: Article number, empty for a whole instrument.
        title: Short descriptive subtitle shown in the diagram, optional.
        hub: Whether the node gets a page of its own.
    """

    id: str
    fonte: str
    doc: str
    art: str
    title: str = ""
    hub: bool = False

    @property
    def band(self) -> str:
        return FONTE_BAND[self.fonte]

    @property
    def color(self) -> str:
        return FONTE_COLOR[self.fonte]

    @property
    def name(self) -> str:
        """Citation form used in running text, e.g. "art. 14 TUB"."""
        if self.fonte == "TUB":
            return f"art. {self.art} TUB" if self.art else "TUB (intero testo)"
        if self.fonte == "COST":
            return f"art. {self.art} Cost." if self.art else "Costituzione"
        return f"{self.doc} art. {self.art}" if self.art else self.doc

    @property
    def anchor(self) -> str:
        return "snodo-" + re.sub(r"[^a-z0-9]+", "-", self.id.lower()).strip("-")


@dataclass
class Edge:
    """A directed relation from the acting provision ``src`` to ``dst``.

    Attributes:
        rel: Relation word from REL_GLOSS; the arrow reads "src <rel> dst".
        label: Short Italian description of the concrete content of the link.
        why: One or two sentences on the logic of the link.
        src_loc: Comma/lettera of ``src`` involved, if narrower than the article.
        dst_loc: Same for ``dst``.
        status: ``accepted`` edges are drawn; any other value is listed for review.
        sources: Where the link comes from, shown as a tiny tag for checking.
        notes: Caveat or reviewer remark.
        weight: How well attested the link is (distinct sources, plus one across levels);
            decides which edges a hub page draws when it has more than fit.
        check: How the edge was verified; "doppio controllo" and "citazione + campione" mean an
            agent read the source for it, anything else only that the cited quote exists.
    """

    src: str
    dst: str
    rel: str
    label: str
    why: str
    src_loc: str = ""
    dst_loc: str = ""
    status: str = "accepted"
    sources: list = field(default_factory=list)
    notes: str = ""
    weight: int = 1
    check: str = ""

    @property
    def read_by_agent(self) -> bool:
        """Whether an agent, not just the quote lookup, confirmed the edge against the source."""
        return self.check in AGENT_CHECKED


@dataclass
class Graph:
    """Nodes, edges and the oral-exam questions indexed by node id."""

    nodes: dict[str, Node]
    edges: list[Edge]
    questions: dict[str, list[dict]]

    def hubs(self) -> list[Node]:
        """Return the nodes that get a page of their own."""
        return [n for n in self.nodes.values() if n.hub]

    def drawn(self) -> list[Edge]:
        """Return the edges that are accepted and therefore drawn."""
        return [e for e in self.edges if e.status == "accepted"]


def load_graph(path: Path) -> Graph:
    """Read the graph file.

    Args:
        path: YAML file with ``nodes``, ``edges`` and optionally ``questions``.

    Returns:
        The parsed graph.

    Raises:
        SystemExit: If a node has an unknown level, or an edge has an undeclared endpoint,
            points to itself or uses a relation word outside REL_GLOSS.
    """
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    nodes = {}
    for nid, spec in raw["nodes"].items():
        if spec.get("fonte") not in FONTE_BAND:
            raise SystemExit(f"node {nid!r}: unknown fonte {spec.get('fonte')!r}")
        nodes[nid] = Node(id=nid, fonte=spec["fonte"], doc=spec.get("doc") or "", art=str(spec.get("art") or ""),
                          title=spec.get("title") or "", hub=bool(spec.get("hub")))
    edges = []
    for i, spec in enumerate(raw["edges"]):
        src, dst, rel = spec.get("src"), spec.get("dst"), spec.get("rel")
        for end in (src, dst):
            if end not in nodes:
                raise SystemExit(f"edge #{i}: unknown node {end!r}")
        if src == dst:
            raise SystemExit(f"edge #{i}: {src!r} points to itself")
        if rel not in REL_GLOSS:
            raise SystemExit(f"edge #{i}: unknown relation {rel!r}")
        edges.append(Edge(src=src, dst=dst, rel=rel, label=spec.get("label") or "", why=spec.get("why") or "",
                          src_loc=spec.get("src_loc") or "", dst_loc=spec.get("dst_loc") or "",
                          status=spec.get("status") or "accepted", sources=list(spec.get("sources") or []),
                          notes=spec.get("notes") or "", weight=int(spec.get("weight") or 1),
                          check=spec.get("check") or ""))
    return Graph(nodes, edges, raw.get("questions") or {})


# --------------------------------------------------------------------------- tex helpers
_TEX_ESC = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
            "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def tex(text: str) -> str:
    """Escape text for LaTeX and rewrite glyphs the text font lacks."""
    return build.fix_glyphs("".join(_TEX_ESC.get(c, c) for c in text))


def tex_name(node: Node, loc: str = "") -> str:
    """Return the escaped citation of a node, with the narrower comma/lettera if given."""
    if not node.art and loc.lower().startswith("intero"):
        loc = ""
    suffix = f", {loc}" if loc else ""
    return tex(node.name + suffix)


# --------------------------------------------------------------------------- article mentions
_SUFFIXES = ("bis|ter|quater|quinquies|sexies|septies|octies|novies|decies|undecies|duodecies|"
             "terdecies|quaterdecies")
_SUFFIX = rf"(?:[- ](?i:{_SUFFIXES}))?"
_NUM = rf"\d+{_SUFFIX}"
# In "art. 19, 5° comma" or "art. 14, 5 lett. a)" the number after the comma is a paragraph
# or a letter of the same article, not another article.
_NOT_SUBDIVISION = r"(?!\d|\s*(?:\u00b0|\u00ba|\u00aa|comma\b|lett\b|co\.|par\b|punto\b))"
ART_RE = re.compile(
    rf"(?P<kw>\b[Aa]rtt?\.)[ \u00a0]*(?P<list>{_NUM}(?:\s*(?:,|e|ed|-|\u2013)\s*{_NUM}{_NOT_SUBDIVISION})*)")
NUM_RE = re.compile(_NUM)
RANGE_SEP_RE = re.compile(r"\s*[-\u2013]\s*")

_COST_RE = re.compile(r"\bCost\b|\bCostituzione\b")
_TUB_RE = re.compile(r"\bTUB\b|testo unico bancario", re.I)
_OTHER_RE = re.compile(
    r"\bReg\b|\bRegolamento\b|\bDir\b|\bDirettiva\b|\bCRD\b|\bCRR\b|\bd\.\s?m\b|\bd\.\s?lgs\b|\bd\.\s?l\b|"
    r"\bc\.\s?c\b|\bcod\. civ|\bcodice civile\b|\bc\.\s?p\b|\bTFUE\b|\bTUE\b|\bTrattato\b|\bCirc\b|"
    r"\bCircolare\b|\bTUF\b|\bl\.\s?\d|\blegge\b|\bStatuto\b|\bd\.p\.r\b|\bdpr\b|\bdecreto\b|"
    r"\bSEBC\b|\br\.\s?d\.\s?l\b", re.I)
# "Reg. UE 1024/2013, art. 14" and "TUF, art. 5": an instrument cited right before the number.
# The TUB itself is often cited as "d.lgs. 385/1993", which must not turn its articles into OTHER.
_DOC_NUMBER_RE = re.compile(r"\b(\d{1,4})\s*/\s*(\d{2,4})\b")
TUB_DECREE = ("385", "1993")
BEFORE_WINDOW = 45
# "nella legge bancaria (ex art. 5)": there "ex" means "former". A bare "autorizzazione ex art. 14,
# comma 1" is the ordinary "pursuant to" and stays a TUB citation.
_FORMER_RE = re.compile(r"\(\s*ex\s*$|legge bancaria|l\. bancaria|previgente", re.I)
# Articles 41, 47 and 117 of the TUB lie outside the programme, so in these notes a bare
# "art. 41" is the Costituzione.
COST_BARE = frozenset({"41", "47", "117"})
_NEXT_ART_RE = re.compile(r"\b[Aa]rtt?\.")
_SENTENCE_END_RE = re.compile(r"(?<=[A-Za-z\u00c0-\u00ff\)\d\u00bb\"*_])\.(?=\s+[A-Z\u00c0-\u00d9])")
_PREVIOUS_ART_RE = re.compile(r"\b[Aa]rtt?\.\s*[\w-]+|;")


@dataclass(frozen=True)
class Mention:
    """One article number cited in a line of text.

    Attributes:
        kind: TUB, COST, or OTHER for any other instrument.
        art: Article number, lower-case (``6-bis``).
        start: Offset where a link would begin; includes the "art." keyword for the first number of a list.
        end: Offset just past the number.
        in_range: Whether the number is an endpoint of a range such as "13-18", which cites
            articles that are not named one by one.
    """

    kind: str
    art: str
    start: int
    end: int
    in_range: bool


def _instrument_before(before: str) -> bool:
    """Return whether another instrument is cited in the clause right before an article number."""
    seg = before[-BEFORE_WINDOW:]
    boundary = 0
    for rx in (_PREVIOUS_ART_RE, _SENTENCE_END_RE):
        for m in rx.finditer(seg):
            boundary = max(boundary, m.end())
    seg = seg[boundary:]
    numbers = _DOC_NUMBER_RE.findall(seg)
    if numbers:
        return numbers[-1] != TUB_DECREE
    marks = list(_OTHER_RE.finditer(seg))
    return bool(marks) and not _TUB_RE.search(seg[marks[-1].end():])


def classify(text: str, start: int, end: int) -> tuple[str, bool]:
    """Decide which instrument the article number at text[start:end] belongs to.

    The TUB is the default: the course is about it and the notes cite it bare.
    A conservative "OTHER" is preferred to a wrong link, so any instrument
    marker between the number and the end of its sentence wins over the default,
    and so does an instrument cited in the clause just before the number.

    Returns:
        The kind (TUB, COST or OTHER) and whether the text named the instrument
        explicitly rather than leaving the default to decide.
    """
    # The window starts one character early so that a full stop right after the
    # number still has the letter before it that marks a sentence end.
    window = text[end - 1:end + 90]
    nxt = _NEXT_ART_RE.search(window, 1)
    if nxt:
        window = window[:nxt.start()]
    cut = _SENTENCE_END_RE.search(window)
    if cut:
        window = window[:cut.start()]
    tail = window[1:]
    hits = [(m.start(), kind) for kind, rx in (("COST", _COST_RE), ("TUB", _TUB_RE), ("OTHER", _OTHER_RE))
            if (m := rx.search(tail))]
    if hits:
        return min(hits)[1], True
    before = text[max(0, start - BEFORE_WINDOW - 15):start]
    if _instrument_before(before) or _FORMER_RE.search(before):
        return "OTHER", True
    return "TUB", False


def mentions(text: str) -> list[Mention]:
    """Return every article number cited in ``text``, in order of appearance."""
    found: list[Mention] = []
    for m in ART_RE.finditer(text):
        kind, explicit = classify(text, m.start(), m.end())
        listing = m.group("list")
        base = m.start("list")
        tokens = list(NUM_RE.finditer(listing))
        for i, tok in enumerate(tokens):
            before = listing[tokens[i - 1].end():tok.start()] if i else ""
            after = listing[tok.end():tokens[i + 1].start()] if i + 1 < len(tokens) else ""
            ranged = bool(RANGE_SEP_RE.fullmatch(before) or RANGE_SEP_RE.fullmatch(after))
            start = m.start("kw") if i == 0 else base + tok.start()
            art = re.sub(r"\s+", "-", tok.group(0).lower())
            of = "COST" if (kind == "TUB" and not explicit and art in COST_BARE) else kind
            found.append(Mention(of, art, start, base + tok.end(), ranged))
    return found


def natural_key(art: str) -> list:
    """Sort key that puts article numbers in numeric order: 5, 6-bis, 10."""
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", art)]


def node_id_of(m: Mention) -> str | None:
    """Return the graph node id of a mention, or None for instruments outside the graph."""
    return f"{m.kind}:{m.art}" if m.kind in ("TUB", "COST") else None


def _in_code_or_math(text: str, pos: int) -> bool:
    prefix = text[:pos]
    return prefix.count("`") % 2 == 1 or len(re.findall(r"(?<!\\)\$", prefix)) % 2 == 1


_GLYPH_BACK = {latex: char for char, latex in build.TEXT_GLYPHS.items()}


def _plain_heading(text: str) -> str:
    """Strip the markdown and the glyph macros build.py already put in a heading, leaving plain text for tex()."""
    for latex, char in _GLYPH_BACK.items():
        text = text.replace(latex, char)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_`$]", "", re.sub(r"\{#[^}]*\}", "", text)).strip()


@dataclass
class HeadingRef:
    """A lecture heading that treats an article, with the anchor given to it."""

    anchor: str
    text: str
    chapter: str


@dataclass
class Prepared:
    """Chapters after anchoring and linking, with what the hub pages need to know.

    Attributes:
        markdown: The chapters joined, ready for pandoc.
        counts: Chapter anchor -> node id -> number of mentions in that chapter.
        headings: Node id -> lecture headings that treat the article.
        links: Number of mentions turned into links.
    """

    markdown: str
    counts: dict[str, Counter]  # chapter anchor -> node id -> mentions
    headings: dict[str, list[HeadingRef]]  # node id -> headings that treat it
    links: int = 0


HEADING_RE = re.compile(r"^(#{2,6})\s+(.*?)\s*$")


def prepare_chapters(chapters: list[tuple[build.Note, str]], hubs: dict[str, Node]) -> Prepared:
    """Give article headings an anchor and turn hub mentions into links."""
    prepared = Prepared("", {}, defaultdict(list))
    used_ids: Counter = Counter()
    out_chapters = []
    for note, md in chapters:
        counts: Counter = Counter()
        lines, in_code = [], False
        for line in md.split("\n"):
            stripped = line.lstrip()
            if stripped.startswith("```"):
                in_code = not in_code
            if in_code or stripped.startswith("```") or line.startswith(FENCE):
                lines.append(line)
                continue
            heading = HEADING_RE.match(line)
            if heading:
                lines.append(_anchor_heading(line, heading, note, prepared, used_ids, hubs))
                continue
            if line.startswith("# "):
                lines.append(line)
                continue
            lines.append(_link_line(line, hubs, counts, prepared))
        prepared.counts[note.anchor] = counts
        out_chapters.append("\n".join(lines))
    prepared.markdown = "\n".join(out_chapters)
    return prepared


def _anchor_heading(line: str, heading: re.Match, note: build.Note, prepared: Prepared, used: Counter,
                    hubs: dict[str, Node]) -> str:
    text = heading.group(2)
    if text.endswith("}") or not re.match(r"[Aa]rtt?\.", text):
        return line
    first = mentions(text)
    if not first or first[0].start != 0 or first[0].kind == "OTHER" or first[0].in_range:
        return line
    colon = text.find(":")
    if len(first) > 1 and (colon == -1 or first[1].start < colon):
        return line
    nid = f"{first[0].kind}:{first[0].art}"
    base = f"art-{nid.lower().replace(':', '-')}"
    used[base] += 1
    anchor = base if used[base] == 1 else f"{base}-{used[base]}"
    prepared.headings[nid].append(HeadingRef(anchor, _plain_heading(text), note.anchor))
    anchored = f"{line} {{#{anchor}}}"
    hub = hubs.get(nid)
    if hub is None:
        return anchored
    return f"{anchored}\n\n`\\snodolink{{{hub.anchor}}}{{{hub.name}}}`{{=latex}}\n"


def _link_line(line: str, hubs: dict[str, Node], counts: Counter, prepared: Prepared) -> str:
    found = mentions(line)
    if not found:
        return line
    for m in reversed(found):
        nid = node_id_of(m)
        if nid is None or m.in_range or _in_code_or_math(line, m.start):
            continue
        counts[nid] += 1
        hub = hubs.get(nid)
        if hub is None:
            continue
        shown = line[m.start:m.end].replace(" ", "~").replace("\u00a0", "~")
        line = line[:m.start] + f"`\\artref{{{hub.anchor}}}{{{shown}}}`{{=latex}}" + line[m.end:]
        prepared.links += 1
    return line


# --------------------------------------------------------------------------- layout
def _order_bands(bands: dict[str, list[str]], center: str, adj: dict[str, set[str]]) -> dict[str, list[str]]:
    """Order nodes inside each band by the barycentre of their neighbours.

    Sweeping up and down a few times pulls connected nodes into the same
    columns, which is what keeps the arrows from crossing; the centre node
    stays in the middle of its band.
    """
    frac: dict[str, float] = {}
    for ids in bands.values():
        ids.sort()
        for i, nid in enumerate(ids):
            frac[nid] = (i + 0.5) / len(ids)
    for sweep in range(6):
        for band in (BAND_ORDER if sweep % 2 == 0 else tuple(reversed(BAND_ORDER))):
            ids = bands[band]
            if len(ids) < 2:
                continue

            def _barycentre(nid: str, here=tuple(ids)) -> float:
                ps = [frac[m] for m in adj[nid] if m in frac and m not in here]
                return sum(ps) / len(ps) if ps else frac[nid]

            ordered = sorted((i for i in ids if i != center), key=lambda i: (_barycentre(i), i))
            if center in ids:
                ordered.insert(len(ordered) // 2, center)
            bands[band] = ordered
            for i, nid in enumerate(ordered):
                frac[nid] = (i + 0.5) / len(ordered)
    return bands


def _split_rows(ids: list[str], rows: int, center: str, adj: dict[str, set[str]],
                band_of: dict[str, str], here: int) -> list[list[str]]:
    """Spread one band over ``rows`` rows, keeping the left-to-right order of ``ids``.

    The hub goes in the top row; the others are ranked by whether their links
    lead up or down the hierarchy, so that nodes tied to the bands above sit
    closer to them and arrows have less to cross.
    """
    if rows == 1:
        return [ids]

    def _lean(nid: str) -> int:
        levels = [BAND_LEVEL[band_of[m]] for m in adj[nid] if m in band_of]
        return sum(1 for lv in levels if lv > here) - sum(1 for lv in levels if lv < here)

    size = math.ceil(len(ids) / rows)
    ranked = sorted(ids, key=lambda i: (i != center, _lean(i)))
    order = {nid: k for k, nid in enumerate(ids)}
    return [sorted(ranked[r * size:(r + 1) * size], key=order.__getitem__) for r in range(rows)]


def place(nodes: list[Node], edges: list[Edge], center: str):
    """Assign coordinates (cm) to the nodes of one diagram.

    Args:
        nodes: Nodes to place.
        edges: Edges among them; only used to order nodes within a band.
        center: Id of the hub, kept in the middle of its band.

    Returns:
        A pair: node id -> (x, y) of the node centre, and the list of
        (band, top, bottom) rectangles to paint behind the nodes.
    """
    bands: dict[str, list[str]] = {b: [] for b in BAND_ORDER}
    for n in nodes:
        bands[n.band].append(n.id)
    adj: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        adj[e.src].add(e.dst)
        adj[e.dst].add(e.src)
    order = _order_bands(bands, center, adj)
    band_of = {n.id: n.band for n in nodes}
    coords: dict[str, tuple[float, float]] = {}
    boxes: list[tuple[str, float, float]] = []
    cursor = 0.0
    for band in BAND_ORDER:
        ids = order[band]
        if not ids:
            continue
        grid = _split_rows(ids, math.ceil(len(ids) / ROW_MAX), center, adj, band_of, BAND_LEVEL[band])
        width = max(len(row) for row in grid)
        height = 2 * BAND_PAD + len(grid) * NODE_H + (len(grid) - 1) * ROW_GAP
        for r, row in enumerate(grid):
            for s_, nid in enumerate(row):
                coords[nid] = (NODE_X0 + (s_ + 0.5 + (width - len(row)) / 2) * NODE_W_AREA / width,
                               cursor - BAND_PAD - NODE_H / 2 - r * (NODE_H + ROW_GAP))
        boxes.append((band, cursor, cursor - height))
        cursor -= height + BAND_GAP
    return coords, boxes


def _node_tikz(idx: int, node: Node, xy: tuple[float, float], is_center: bool, target: str | None) -> str:
    if node.fonte in ("TUB", "COST") and node.art:
        top, mid = f"art.~{tex(node.art)}", tex("TUB" if node.fonte == "TUB" else "Cost.")
    elif node.fonte in ("TUB", "COST"):
        top, mid = tex("TUB" if node.fonte == "TUB" else "Costituzione"), "intero testo"
    else:
        top, mid = tex(node.doc), (f"art.~{tex(node.art)}" if node.art else "")
    body = rf"\textbf{{\textcolor{{{node.color}}}{{{top}}}}}"
    if mid:
        body += rf"\\{{\scriptsize {mid}}}"
    if node.title:
        body += rf"\\{{\tiny\itshape {tex(node.title)}}}"
    if target:
        body = rf"\hyperref[{target}]{{{body}}}"
    weight = "line width=1.5pt" if is_center else "line width=0.6pt"
    tint = 28 if is_center else 8
    return (rf"\node[draw={node.color}, fill={node.color}!{tint}, rounded corners=2pt, {weight}, "
            rf"minimum width={NODE_W}cm, minimum height={NODE_H}cm, text width={NODE_W - 0.3}cm, "
            rf"align=center, inner sep=2pt, font=\footnotesize] (n{idx}) at ({xy[0]:.2f},{xy[1]:.2f}) {{{body}}};")


def diagram(center: Node, nodes: list[Node], edges: list[Edge], by_id: dict[str, Node]) -> str:
    """Return the TikZ picture of one hub: banded nodes joined by labelled arrows.

    Args:
        center: The hub, drawn with a heavier border and not linked.
        nodes: Every node to draw, the hub included.
        edges: Edges to draw; their position in the list is the number printed on the arrow.
        by_id: Lookup of all graph nodes by id.
    """
    coords, boxes = place(nodes, edges, center.id)
    index = {n.id: i for i, n in enumerate(nodes)}
    lines = [r"\begin{center}", r"\begin{tikzpicture}[>=Stealth]"]
    for band, top, bottom in boxes:
        color = BAND_COLOR[band]
        lines.append(rf"\fill[{color}!7, rounded corners=3pt] ({-BAND_W / 2},{top:.2f}) rectangle ({BAND_W / 2},{bottom:.2f});")
        lines.append(rf"\node[rotate=90, font=\tiny\scshape, text={color}] at ({-BAND_W / 2 + 0.28},{(top + bottom) / 2:.2f}) {{{tex(BAND_TITLE[band])}}};")
    for n in nodes:
        target = n.anchor if (n.hub and n.id != center.id) else None
        lines.append(_node_tikz(index[n.id], n, coords[n.id], n.id == center.id, target))
    pairs = {(e.src, e.dst) for e in edges}
    for k, e in enumerate(edges, start=1):
        a, b = f"n{index[e.src]}", f"n{index[e.dst]}"
        (sx, sy), (dx, dy) = coords[e.src], coords[e.dst]
        style = "dashed" if e.rel in HORIZONTAL_RELS else "solid"
        where = "midway"
        if abs(sy - dy) < 0.1:
            # Same row: an arc over the nodes keeps the label out of the narrow gap between boxes.
            path = f"to[bend {'left' if sx < dx else 'right'}=42]"
        elif (e.dst, e.src) in pairs:
            path = "to[bend left=20]"
            where = "pos=0.35" if e.src < e.dst else "pos=0.65"
        else:
            path = "--"
        if center.id in (e.src, e.dst) and path == "--":
            # Arrows converge on the hub, so their labels sit at the far end where they fan out.
            where = "pos=0.3" if e.dst == center.id else "pos=0.7"
        lines.append(
            rf"\draw[-{{Stealth[length=2mm,width=1.5mm]}}, {style}, line width=0.55pt, black!65] ({a}) {path} "
            rf"node[{where}, fill=white, inner sep=1.2pt, font=\scriptsize] {{\textbf{{{k}}}\,{tex(e.rel)}}} ({b});")
    lines += [r"\end{tikzpicture}", r"\end{center}"]
    return "\n".join(lines)


# --------------------------------------------------------------------------- pages
def _source_tag(sources: list) -> str:
    return ", ".join(str(s) for s in sources[:3])


def select_edges(center: Node, graph: Graph) -> tuple[list[Edge], list[Edge], int]:
    """Choose which edges the page of ``center`` draws.

    Returns:
        The edges that touch the hub, the edges among its neighbours, and how many
        edges of the hub were left out. The best edges of every level of the
        hierarchy come first, so a page about the TUB does not lose its link to the
        Costituzione to a crowd of TUB-to-TUB links.
    """
    def _other(e: Edge) -> str:
        return e.dst if e.src == center.id else e.src

    touching = sorted((e for e in graph.drawn() if center.id in (e.src, e.dst)),
                      key=lambda e: (-e.weight, e.src, e.dst))
    chosen: list[Edge] = []
    for band in BAND_ORDER:
        in_band = [e for e in touching if graph.nodes[_other(e)].band == band]
        chosen += in_band[:PER_BAND_FLOOR]
    for e in touching:
        if len(chosen) >= MAX_INCIDENT:
            break
        if e not in chosen:
            chosen.append(e)
    ids = {center.id} | {x for e in chosen for x in (e.src, e.dst)}
    between = sorted((e for e in graph.drawn() if e not in chosen and e.src in ids and e.dst in ids),
                     key=lambda e: (-e.weight, e.src, e.dst))[:MAX_BETWEEN_NEIGHBOURS]
    return chosen, between, len(touching) - len(chosen)


def page_edges(center: Node, graph: Graph) -> tuple[list[Edge], int]:
    """Return the edges of the page of ``center`` in the order the page numbers them.

    The position in the list is the number printed on the arrow and in "Come si collega",
    so anything that refers to "arrow 3" of a page must take it from here.

    Returns:
        The edges that touch the hub first, by level of the other provision, then the edges
        among its neighbours; and how many edges of the hub the page leaves out.
    """
    incident, between, omitted = select_edges(center, graph)

    def _rank(e: Edge):
        other = graph.nodes[e.dst if e.src == center.id else e.src] if e in incident else graph.nodes[e.src]
        return (0 if e in incident else 1, BAND_ORDER.index(other.band), e.rel, e.src, e.dst)

    return sorted(incident + between, key=_rank), omitted


def text_block(testo: dict | None) -> list[str]:
    """Return the raw LaTeX of the "Testo dell'articolo" section.

    Args:
        testo: Entry of testi.yaml for the hub (source, heading, paragraphs), or None when no text is
            available; a repealed paragraph is greyed and labelled.
    """
    head = r"\par\medskip\noindent\textbf{Testo dell'articolo}"
    if not testo:
        return [head + r"\par\smallskip", r"{\small\itshape Testo non incluso in questo file: si trova nella fonte ufficiale.}"]
    source = tex(testo["fonte"]) + (f", in vigore dal {tex(testo['vigore'])}" if testo.get("vigore") else "")
    parts = [head + rf"\ {{\footnotesize\itshape [{source}]}}\par\smallskip"]
    if testo.get("rubrica"):
        parts.append(rf"{{\small\bfseries {tex(testo['rubrica'])}}}\par\smallskip")
    for item in testo["par"]:
        body = tex(item["text"])
        if item["abrogato"]:
            body = rf"\textcolor{{black!50}}{{\textit{{[abrogato]}} {body}}}"
        parts.append(rf"\testoitem{{{('0em', '1.7em', '3.4em')[item['level']]}}}{{{tex(item['label'])}}}{{{body}}}")
    return parts


def hub_page(center: Node, graph: Graph, prepared: Prepared, chapters: list[build.Note],
             testi: dict | None = None, with_text: bool = False) -> str:
    """Return the pandoc markdown of the page of one hub article.

    The page holds the diagram, a numbered explanation of every arrow, the
    oral-exam questions that touch the article and where the lectures treat it.
    With ``with_text`` it also holds the legal text of the article, taken from ``testi``.
    """
    ordered, omitted = page_edges(center, graph)
    ids = {center.id} | {x for e in ordered for x in (e.src, e.dst)}
    nodes = [graph.nodes[i] for i in sorted(ids)]
    official = ((testi or {}).get(center.id) or {}).get("rubrica") if with_text else ""
    label = official or center.title
    heading = f"{center.name} \u2014 {label}" if label else center.name
    parts = [f"# {heading} {{#{center.anchor}}}", "",
             f"{FENCE} {{.chapsource}}", "Collegamenti con le altre fonti: tocca un riquadro per passare al suo snodo.", FENCE, "",
             "```{=latex}", diagram(center, nodes, ordered, graph.nodes)]
    parts.append(r"\par\medskip\noindent\textbf{Come si collega}\par\smallskip")
    if omitted:
        parts.append(rf"{{\small\itshape Dei collegamenti di questo articolo sono disegnati i meglio attestati: altri {omitted} stanno nel grafo.}}\par\smallskip")
    for k, e in enumerate(ordered, start=1):
        src, dst = graph.nodes[e.src], graph.nodes[e.dst]
        arrow = r"\ensuremath{\rightarrow}"
        text = (rf"\textbf{{{tex(e.rel)}}} \ \ {tex_name(src, e.src_loc)} {arrow} {tex_name(dst, e.dst_loc)}: "
                rf"{tex(e.label.rstrip('.'))}.")
        if e.why:
            text += rf" \emph{{Perché:}} {tex(e.why)}"
        if e.notes:
            text += rf" \emph{{Attenzione:}} {tex(e.notes)}"
        mark = r" \textcolor{fSec}{" + tex("\u2713") + "}" if e.read_by_agent else ""
        if e.sources:
            text += rf" {{\tiny\color{{black!55}}[{tex(_source_tag(e.sources))}]}}{mark}"
        parts.append(rf"\collitem{{{k}}}{{{text}}}")
    if with_text:
        parts += text_block((testi or {}).get(center.id))
    questions = graph.questions.get(center.id, [])
    if questions:
        parts.append(r"\par\medskip\noindent\textbf{Domande d'orale che toccano questo articolo}\par\smallskip")
        for q in questions:
            parts.append(rf"\collitem{{\ensuremath{{\bullet}}}}{{{tex(q['src'])} \textbf{{{tex(str(q['id']))}}}: {tex(q['title'])}}}")
    where = prepared.headings.get(center.id, [])
    titles = {n.anchor: n.title for n in chapters}
    seen = [(a, c) for a, c in prepared.counts.items() if c.get(center.id)]
    if where or seen:
        parts.append(r"\par\medskip\noindent\textbf{Nel testo}\par\smallskip")
        for h in where:
            parts.append(rf"\collitem{{\ensuremath{{\bullet}}}}{{\hyperref[{h.anchor}]{{\textcolor{{fUE}}{{{tex(h.text)}}}}} "
                         rf"(p.~\pageref{{{h.anchor}}})}}")
        for anchor, count in seen:
            times = count[center.id]
            cited = "citato 1 volta" if times == 1 else f"citato {times} volte"
            parts.append(rf"\collitem{{\ensuremath{{\bullet}}}}{{{cited} in "
                         rf"\hyperref[{anchor}]{{\textcolor{{fUE}}{{{tex(titles[anchor])}}}}} (p.~\pageref{{{anchor}}})}}")
    parts.append("```")
    return "\n".join(parts)


def intro_page(graph: Graph, solo: bool = False) -> str:
    """Return the reading guide: how to read a diagram, the relation words, and a tappable index of hubs."""
    drawn = graph.drawn()
    rels = sorted({e.rel for e in drawn}, key=list(REL_GLOSS).index)

    def _example(rel: str) -> str:
        best = max((e for e in drawn if e.rel == rel), key=lambda e: e.weight)
        return "" if rel == "altro" else f"{graph.nodes[best.src].name} \u2192 {graph.nodes[best.dst].name}"

    rows = "\n".join(f"| **{r}** | {REL_GLOSS[r]} | {_example(r)} |" for r in rels)
    hubs_by_band = {b: [n for n in graph.hubs() if n.band == b] for b in BAND_ORDER}
    index = []
    for band in BAND_ORDER:
        items = sorted(hubs_by_band[band], key=lambda n: (n.doc, natural_key(n.art)))
        if items:
            links = r" \quad ".join(rf"\artref{{{n.anchor}}}{{{tex(n.name)}}}" for n in items)
            index.append(rf"\collitem{{}}{{\textbf{{{tex(BAND_TITLE[band])}}}: {links}}}")
    return "\n".join([
        "# Come leggere i collegamenti", "",
        "Le pagine che seguono mostrano, articolo per articolo, **come si intrecciano Costituzione, diritto UE, TUB e fonti secondarie**. "
        "Ogni diagramma ha l'articolo al centro e raggruppa le norme collegate in fasce, una per livello di fonte, dall'alto verso il basso.",
        "", "- **Colore e fascia** dicono il livello: rosso Costituzione, blu diritto UE, grigio TUB e leggi, verde fonti secondarie.",
        "- **Freccia continua**: rapporto fra livelli diversi di fonte. **Freccia tratteggiata**: interazione fra norme dello stesso livello.",
        "- La **parola sulla freccia** dice che cosa fa l'una all'altra; il numero rimanda alla riga che la spiega sotto il diagramma.",
        "- **Quanto fidarsi.** Il grafo è stato ricavato in automatico dalle lezioni e dalle tracce d'orale. "
        "Dove accanto all'arco c'è il segno " + CHECK_MARK + " un agente ha riletto il testo e lo conferma; senza il segno è verificato soltanto che la citazione "
        "esista nel file e nomini i due articoli, quindi **comma e descrizione possono contenere errori**: nel dubbio fa fede il testo della norma.",
        ("- Sotto ogni diagramma c'è il **testo dell'articolo**: TUB nel testo consolidato al 22 gennaio 2026 (in grigio i commi abrogati, "
         "ancora stampati nel consolidato), Costituzione, Reg. UE 1024/2013 nel testo originale della Gazzetta ufficiale."
         if solo else
         "- Nelle lezioni, sotto il titolo di ogni articolo che ha uno snodo c'è il link \u00abCollegamenti di art. N\u00bb; anche gli \u00abart. N\u00bb colorati di blu nel testo sono link allo snodo."),
        "", "Le parole delle frecce:", "", "| Parola | Significato | Esempio |", "|---|---|---|", rows, "",
        "Snodi disponibili:", "", "```{=latex}", *index, "```",
    ])


def review_page(graph: Graph) -> str:
    """Return the list of edges that are not drawn because the checks disagreed, or "" if there are none."""
    hub_ids = {n.id for n in graph.hubs()}
    pending = sorted((e for e in graph.edges if e.status != "accepted" and (e.src in hub_ids or e.dst in hub_ids)),
                     key=lambda e: (-e.weight, e.src, e.dst))
    if not pending:
        return ""
    listed = pending[:MAX_REVIEW_LISTED]
    rest = len(pending) - len(listed)
    lines = ["# Collegamenti da verificare", "",
             "Archi degli snodi emersi dall'estrazione ma su cui i due controlli non concordano: non sono disegnati. "
             "Da riguardare sul testo della norma prima di fidarsene."
             + (f" Sono elencati i {len(listed)} meglio attestati; altri {rest} stanno nel grafo." if rest else ""),
             "", "```{=latex}"]
    for k, e in enumerate(listed, start=1):
        src, dst = graph.nodes[e.src], graph.nodes[e.dst]
        lines.append(rf"\collitem{{{k}}}{{\textbf{{{tex(e.rel)}}} \ \ {tex_name(src, e.src_loc)} \ensuremath{{\rightarrow}} "
                     rf"{tex_name(dst, e.dst_loc)}: {tex(e.label.rstrip('.'))}. \emph{{Dubbio:}} {tex(e.notes or 'nessuna nota')}}}")
    lines.append("```")
    return "\n".join(lines)


# --------------------------------------------------------------------------- cli
def main() -> int:
    """Build the dispensa of one subject with the Collegamenti part appended."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--subject", default="03-Legislazione-Bancaria-1", help="folder name under ../obsidian")
    ap.add_argument("--edges", type=Path, default=DEFAULT_EDGES, help="graph file (YAML)")
    ap.add_argument("--out", type=Path, default=OUT_DIR, help="output directory for the PDF")
    ap.add_argument("--keep", action="store_true", help="keep intermediate .md and LaTeX aux files")
    ap.add_argument("--solo", action="store_true",
                    help="only the Collegamenti part, without the lectures, with the legal text of every hub article")
    ap.add_argument("--testi", type=Path, default=DEFAULT_TESTI, help="texts of the hub articles (YAML), used with --solo")
    ap.add_argument("--review", action="store_true",
                    help="append the chapter listing edges on which the two checks disagreed (a QA aid, not for studying)")
    args = ap.parse_args()

    graph = load_graph(args.edges)
    subjects = build.discover(build.VAULT)
    subject = next((s for s in subjects if s.folder.name == args.subject or s.slug == args.subject), None)
    if subject is None:
        raise SystemExit(f"no subject {args.subject!r} in {build.VAULT}")

    for d in (build.BUILD, build.TEXDIR, args.out):
        d.mkdir(parents=True, exist_ok=True)
    hubs = {n.id: n for n in graph.hubs()}
    order = sorted(graph.hubs(), key=lambda n: (BAND_ORDER.index(n.band), n.doc, natural_key(n.art)))
    meta = build.subject_meta(subject)
    if args.solo:
        testi = yaml.safe_load(args.testi.read_text(encoding="utf-8")) if args.testi.exists() else {}
        prepared = Prepared("", {}, defaultdict(list))
        pages = [intro_page(graph, solo=True)] + [hub_page(n, graph, prepared, [], testi, with_text=True) for n in order]
        markdown = "\n\n".join(p for p in pages if p)
        meta["subtitle"] = "Solo collegamenti fra le fonti, con il testo degli articoli"
        slug = f"{subject.slug}-solo-collegamenti"
        meta["stats"] = f"{len(order)} articoli"
    else:
        anchors = build.build_anchor_map(subjects)
        chapters = [(note, build.chapter_markdown(note, anchors, True)) for note in subject.chapters]
        prepared = prepare_chapters(chapters, hubs)
        pages = [intro_page(graph)] + [hub_page(n, graph, prepared, subject.chapters) for n in order]
        markdown = "\n".join([prepared.markdown, "\\part{Collegamenti tra le fonti}\n", "\n\n".join(p for p in pages if p)])
        meta["subtitle"] = "Dispensa del corso, edizione con collegamenti"
        slug = f"{subject.slug}-collegamenti"
    if args.review:
        markdown += "\n\n" + review_page(graph)
    pdf = build.render(slug, markdown, meta, 1, args.keep, extra_pandoc=("-H", str(HEADER)), pdf_dir=args.out)
    print(f"==> {subject.title}: {len(graph.hubs())} snodi, {prepared.links} link nel testo")
    print(f"    {pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
