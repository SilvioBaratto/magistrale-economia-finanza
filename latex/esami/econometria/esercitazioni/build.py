"""Driver of the exercise banks: run, verify, lint and render the volume sources.

Run from ``latex/esami/econometria/``::

    python3 -m esercitazioni.build --modulo 3 [--check] [--blind-pack DIR]
    python3 -m esercitazioni.build --appello 1
    python3 -m esercitazioni.build --all
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

from .lib import bank, config, coverage, lint, render

# Matplotlib writes the creation time into every PDF. The figures are tracked, so a fixed
# epoch keeps them byte-identical between builds instead of changing all of them each time.
os.environ.setdefault("SOURCE_DATE_EPOCH", "0")

# Appelli take the module numbers from 8 on (an appello N is 7 + N), so modules stop at 7.
MAX_MODULO = 7

_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


@dataclass(frozen=True)
class Unit:
    """A module (00-07) or a simulated exam (1-4).

    Attributes:
        kind: ``"modulo"`` or ``"appello"``.
        number: The module number, or the number of the appello.
    """

    kind: str
    number: int

    @property
    def modulo(self) -> int:
        """Module number the exercises register under; an appello ``N`` is ``7 + N``."""
        return self.number if self.kind == "modulo" else 7 + self.number

    @property
    def label(self) -> str:
        """Name of the answers file: ``03`` for a module, ``a01`` for an appello."""
        return f"{self.number:02d}" if self.kind == "modulo" else f"a{self.number:02d}"

    def folder(self, root: Path) -> Path:
        """Return the folder holding ``ex.py`` and the templates.

        Raises:
            FileNotFoundError: If the folder does not exist or a module number is ambiguous.
        """
        if self.kind == "appello":
            found = [root / "appelli" / f"{self.number:02d}"]
        else:
            found = sorted((root / "moduli").glob(f"{self.number:02d}-*"))
        if len(found) != 1 or not found[0].is_dir():
            raise FileNotFoundError(f"{self.kind} {self.label}: cartella non trovata o ambigua")
        return found[0]


@dataclass
class Built:
    """The result of building one unit.

    Attributes:
        unit: What was built.
        exercises: The verified exercises.
        esercizi_md: Rendered exercise source, with front matter.
        soluzioni_md: Rendered solution source, with front matter.
        problemi: Everything that failed; the sources are empty when it is not empty.
        folder: Folder of the unit, whose name gives the descriptive part of the file names.
    """

    unit: Unit
    exercises: list[bank.Exercise]
    folder: Path | None = None
    esercizi_md: str = ""
    soluzioni_md: str = ""
    problemi: list[str] = field(default_factory=list)


def discover(root: Path) -> list[Unit]:
    """Return every module and appello folder under ``root``, modules first."""
    modules = sorted(int(p.name[:2]) for p in (root / "moduli").glob("[0-9][0-9]-*") if p.is_dir())
    appelli = sorted(int(p.name) for p in (root / "appelli").glob("[0-9][0-9]") if p.is_dir())
    return [Unit("modulo", n) for n in modules] + [Unit("appello", n) for n in appelli]


def load_bank(folder: Path) -> str:
    """Import ``ex.py`` of a unit, registering its exercises, and return its ``TITOLO``.

    Raises:
        AttributeError: If the module defines no ``TITOLO``.
    """
    name = "_bank_" + re.sub(r"\W", "_", f"{folder.parent.name}_{folder.name}")
    spec = importlib.util.spec_from_file_location(name, folder / "ex.py")
    module = importlib.util.module_from_spec(spec)
    # dataclasses resolve string annotations through sys.modules.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module.TITOLO


def build_unit(unit: Unit, titolo: str, root: Path) -> Built:
    """Verify, lint and render one unit whose ``ex.py`` is already loaded."""
    folder = unit.folder(root)
    built = Built(unit, [], folder)
    try:
        built.exercises = bank.build_all(unit.modulo, folder / "figure")
    except bank.ExerciseError as exc:
        built.problemi += exc.problemi
        return built
    # Renumbering an exercise renames its figures; the old files would stay behind unreferenced.
    produced = {p for e in built.exercises for p in e.figure_path.values()}
    for stale in (folder / "figure").glob("*.pdf"):
        if stale not in produced:
            stale.unlink()
    templates = {name: (folder / f"{name}.tpl.md").read_text(encoding="utf-8")
                 for name in ("esercizi", "soluzioni")}
    for name, text in templates.items():
        built.problemi += [f"{name}.tpl.md:{i.line}: {i.reason}: {i.snippet}"
                           for i in lint.lint_template(text)]
    if built.problemi:
        return built
    chapter = (f"Modulo {unit.number:02d} — {titolo}" if unit.kind == "modulo"
               else f"Appello simulato {unit.number}")
    try:
        built.esercizi_md, built.soluzioni_md = render.render_module(
            templates["esercizi"], templates["soluzioni"], {e.id: e for e in built.exercises},
            titolo=chapter)
    except render.RenderError as exc:
        built.problemi.append(str(exc))
    return built


def source_stem(built: Built, kind: str) -> str:
    """Return the file stem, and so the PDF name, of one source of a unit.

    Args:
        built: The built unit.
        kind: ``Esercizi`` or ``Soluzioni``.

    Returns:
        ``ECON_<kind>_<NN>_<Description>``: the description is the folder name of a
        module after its number (``Regressione-multipla``) or ``Appello-simulato-N``.
    """
    unit = built.unit
    if unit.kind == "modulo":
        words = built.folder.name.split("-", 1)[1]
        description = words[:1].upper() + words[1:]
    else:
        description = f"Appello-simulato-{unit.number}"
    return f"ECON_{kind}_{unit.modulo:02d}_{description}"


def write_unit(built: Built, build_dir: Path) -> None:
    """Write the two sources and the answers of a unit that built without problems.

    Sources of the same unit written under another name (an earlier naming of the
    files) are removed first, so each rebuild leaves exactly one pair per unit.
    """
    src, answers = build_dir / "src", build_dir / "answers"
    src.mkdir(parents=True, exist_ok=True)
    answers.mkdir(parents=True, exist_ok=True)
    for old in src.glob(f"ECON_*_{built.unit.modulo:02d}*.md"):
        old.unlink()
    (src / f"{source_stem(built, 'Esercizi')}.md").write_text(built.esercizi_md, encoding="utf-8")
    (src / f"{source_stem(built, 'Soluzioni')}.md").write_text(built.soluzioni_md, encoding="utf-8")
    data = render.answers_json({e.id: e for e in built.exercises})
    (answers / f"{built.unit.label}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_blind_pack(built: Built, outdir: Path, root: Path) -> None:
    """Write what a blind solver may see: the rendered exercises and their data figures.

    Raises:
        FileExistsError: If ``outdir`` is not empty, since stale files could leak answers.
    """
    if outdir.exists() and any(outdir.iterdir()):
        raise FileExistsError(f"{outdir} non è vuota")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "esercizi.md").write_text(built.esercizi_md, encoding="utf-8")
    for ref in _IMG_RE.findall(built.esercizi_md):
        source = root / ref
        if not ref.startswith("http") and source.is_file():
            (outdir / ref).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, outdir / ref)


def main(argv: list[str] | None = None, *, root: Path = config.ROOT,
         build: Path = config.BUILD) -> int:
    """Run the driver.

    Args:
        argv: Command-line arguments; ``sys.argv[1:]`` when ``None``.
        root: Folder with ``moduli/``, ``appelli/`` and ``TASSONOMIA.md``.
        build: Folder receiving the rendered sources and the answers.

    Returns:
        0 when everything passed, 1 otherwise.
    """
    ap = argparse.ArgumentParser(prog="esercitazioni.build", description=__doc__.split("\n")[0])
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--modulo", type=int)
    group.add_argument("--appello", type=int)
    group.add_argument("--all", action="store_true")
    ap.add_argument("--check", action="store_true", help="verify without writing the sources")
    ap.add_argument("--blind-pack", type=Path, metavar="DIR")
    args = ap.parse_args(argv)

    if args.all:
        units = discover(root)
    elif args.modulo is not None:
        units = [Unit("modulo", args.modulo)]
    else:
        units = [Unit("appello", args.appello)]
    too_high = [u for u in units if u.kind == "modulo" and u.number > MAX_MODULO]
    if too_high:
        print(f"ERRORE i moduli arrivano a {MAX_MODULO:02d}: il numero {too_high[0].number:02d} "
              "è riservato agli appelli simulati", file=sys.stderr)
        return 1
    if args.blind_pack and len(units) != 1:
        ap.error("--blind-pack richiede un solo modulo o appello")

    bank.clear_registry()
    titles: dict[Unit, str] = {}
    problems: list[str] = []
    for unit in units:
        try:
            titles[unit] = load_bank(unit.folder(root))
        except (FileNotFoundError, AttributeError) as exc:
            problems.append(f"{unit.kind} {unit.label}: {exc}")
    results = [build_unit(u, titles[u], root) for u in units if u in titles]
    for b in results:
        print(f"{b.unit.kind} {b.unit.label}: {len(b.exercises)} esercizi, {len(b.problemi)} problemi")
        problems += [f"{b.unit.kind} {b.unit.label}: {p}" for p in b.problemi]

    if not problems:
        for b in results:
            if not args.check:
                write_unit(b, build)
            if args.blind_pack:
                write_blind_pack(b, args.blind_pack, root)
    if args.all and (root / "TASSONOMIA.md").exists():
        table, gaps = coverage.matrice(coverage.load_tassonomia(root / "TASSONOMIA.md"),
                                       [e for b in results for e in b.exercises])
        problems += [f"copertura: {g}" for g in gaps]
        if not args.check:
            body = "# Copertura\n\nGenerato da `esercitazioni.build --all`.\n\n" + table + "\n"
            (root / "COPERTURA.md").write_text(body, encoding="utf-8")
    elif args.all:
        print("TASSONOMIA.md assente: copertura non verificata")
    for p in problems:
        print(f"ERRORE {p}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
