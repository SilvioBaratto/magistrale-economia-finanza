"""Tests for the extensions of build_esami.py that carry the exercise volumes."""

import contextlib
import dataclasses
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from esercitazioni.lib import config

sys.path.insert(0, str(config.LATEX))
import build_esami  # noqa: E402

QUESTION = "> [!question] Esercizio\n> Testo.\n"


def _course(tmp: Path):
    """Return a course reading its sources from ``tmp`` and counting callout questions."""
    return dataclasses.replace(build_esami.COURSES["finanza-strategica"], src=tmp,
                               question_re=r"^> \[!question\]")


def _volume(**over):
    kw = dict(stem="ECON_Eserc_Completo", pattern="ECON_Eserc_*.md", title="T", subtitle="S",
              disclaimer="D", chapter_label="Modulo")
    kw.update(over)
    return build_esami.Volume(**kw)


class EditionTest(unittest.TestCase):
    """An edition names its chapters and counts its questions as the exercise volumes need."""

    def setUp(self):
        """Create a folder of rendered sources."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)

    def test_chapter_title_from_front_matter(self):
        """A source with a capitolo field is titled by it, one without by label and number."""
        (self.tmp / "ECON_Eserc_03.md").write_text(
            '---\ncapitolo: "Modulo 03 — Regressione multipla"\n---\n\n' + QUESTION)
        (self.tmp / "ECON_Eserc_04.md").write_text(QUESTION)
        body, _ = build_esami.edition_markdown(_course(self.tmp), _volume())
        self.assertIn("# Modulo 03 — Regressione multipla", body)
        self.assertIn("# Modulo 04\n", body)

    def test_edition_stats_use_unit(self):
        """With a unit the title page counts that unit and the question callouts."""
        (self.tmp / "ECON_Eserc_03.md").write_text(QUESTION * 2)
        (self.tmp / "ECON_Eserc_04.md").write_text(QUESTION)
        _, meta = build_esami.edition_markdown(_course(self.tmp), _volume(unit="parti"))
        self.assertEqual(meta["stats"], "2 parti · 3 domande")

    def test_edition_without_unit_keeps_the_old_statistics(self):
        """An edition without a unit counts multiple-choice tests as before."""
        (self.tmp / "ECON_Eserc_03.md").write_text('::: {heading="1"}\n:::\n')
        _, meta = build_esami.edition_markdown(_course(self.tmp), _volume())
        self.assertEqual(meta["stats"], "1 appelli · 1 domande a risposta multipla")


class MainTest(unittest.TestCase):
    """An edition with no rendered sources is skipped, never built empty."""

    def test_missing_sources_skipped(self):
        """No sources: a message on stderr, no call to the renderer, no exception."""
        with tempfile.TemporaryDirectory() as tmp:
            fake = _course(Path(tmp))
            err = io.StringIO()
            with mock.patch.dict(build_esami.COURSES, {"finanza-strategica": fake}, clear=True), \
                    mock.patch.object(build_esami, "render") as render, \
                    contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                status = build_esami.main(["--corso", "finanza-strategica", "--volume"])
        render.assert_not_called()
        self.assertEqual(status, 1)
        self.assertIn("nessun sorgente per FSTR_Esame_Simulato_Completo", err.getvalue())


class CoursesTest(unittest.TestCase):
    """The new course lands where the spec says and the old ones do not move."""

    EXPECTED = {
        "econometria": dict(pattern="ECON_Sol_*.md", volume="ECON_Soluzioni_Raccolta", parts=True,
                            question_re="^## ", unit="appelli", dated=True, volumes=()),
        "legislazione-bancaria-1": dict(pattern="LEGB1_Orale_*.md", volume="LEGB1_Orale_Completo",
                                        parts=False, question_re="^##\\s+D\\d+", unit="sezioni",
                                        dated=True, volumes=()),
        "legislazione-bancaria-2": dict(pattern="LEGB2_Orale_*.md", volume="LEGB2_Orale_Completo",
                                        parts=False, question_re="^##\\s+D\\d+", unit="sezioni",
                                        dated=True, volumes=()),
        "test-ingresso": dict(pattern="EMR20_Prereq_Test-Completo_*.md", volume=None, parts=False,
                              question_re='kind="question"', unit="file", dated=True, volumes=()),
        "finanza-strategica": dict(pattern="FSTR_*.md", volume=None, parts=False,
                                   question_re='kind="question"', unit="appelli", dated=False,
                                   volumes=("FSTR_Esame_Simulato_Completo",
                                            "FSTR_Soluzioni_Simulato_Completo")),
    }

    def test_existing_courses_unchanged(self):
        """The attributes of every pre-existing course are what they were before the change."""
        for slug, expected in self.EXPECTED.items():
            course = build_esami.COURSES[slug]
            with self.subTest(slug=slug):
                actual = {k: getattr(course, k) for k in expected if k != "volumes"}
                actual["volumes"] = tuple(v.stem for v in course.volumes)
                self.assertEqual(actual, expected)
                self.assertEqual(course.macros_file, course.sources_dir / "macros.tex")

    def test_new_course_paths(self):
        """The exercise course writes to esami/econometria/esercitazioni and reads the parent macros."""
        course = build_esami.COURSES["econometria/esercitazioni"]
        self.assertEqual(course.outdir, build_esami.REPO / "esami" / "econometria" / "esercitazioni")
        self.assertEqual(course.sources_dir, build_esami.LATEX / "esami" / "econometria" / "esercitazioni")
        self.assertEqual(course.src_dir, config.BUILD / "src")
        self.assertTrue(course.macros_file.is_file())
        self.assertEqual(course.macros_file.parent, build_esami.LATEX / "esami" / "econometria")

    def test_new_course_builds_one_pdf_per_source_and_no_volume(self):
        """Every rendered source (one per module and kind) is its own PDF; no single volume."""
        course = build_esami.COURSES["econometria/esercitazioni"]
        self.assertEqual(course.pattern, "ECON_*.md")
        self.assertEqual(course.volumes, ())
        self.assertIsNone(course.volume)

    def test_new_course_sources_are_listed_by_their_descriptive_names(self):
        """The sources esercitazioni.build writes are picked up by the course's pattern."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            for name in ("ECON_Esercizi_03_Regressione-multipla.md",
                         "ECON_Soluzioni_03_Regressione-multipla.md", "altro.md"):
                (tmp / name).write_text("x")
            course = dataclasses.replace(build_esami.COURSES["econometria/esercitazioni"], src=tmp)
            self.assertEqual([p.name for p in build_esami.sources(course)],
                             ["ECON_Esercizi_03_Regressione-multipla.md",
                              "ECON_Soluzioni_03_Regressione-multipla.md"])


if __name__ == "__main__":
    unittest.main()
