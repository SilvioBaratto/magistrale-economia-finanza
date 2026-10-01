PY ?= python3

.PHONY: all list combined sections esami esami-volume figure figure-esami everything clean distclean
all:            ## build one PDF per subject
	$(PY) build.py --all

list:           ## show subjects and chapter counts
	$(PY) build.py --list

combined:       ## build every subject + the single-volume edition
	$(PY) build.py --all --combined

sections:       ## build with a two-level table of contents
	$(PY) build.py --all --toc-depth 2

esami:          ## build every Econometria exam solution into ../esami/econometria/
	$(PY) build_esami.py --all

esami-volume:   ## build all exam solutions as one PDF
	$(PY) build_esami.py --volume

figure:         ## regenerate the figures of the dispense
	for f in figure-src/01-econometria/econ-*.py; do $(PY) "$$f" || exit 1; done

figure-esami:   ## regenerate the figures of the exam solutions
	for f in esami/econometria/figure/*/plots.py; do $(PY) "$$f" || exit 1; done

everything: combined esami esami-volume   ## every PDF of the repository

clean:          ## remove LaTeX intermediates
	rm -rf tex/.aux-* build/*.md build/esami-*

distclean: clean
	rm -f tex/*.tex ../dispense/*.pdf ../esami/econometria/*.pdf
