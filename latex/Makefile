PY ?= python3

.PHONY: all list sections appunti formulari esami esami-volume esercitazioni verifica verifica-simulati figure figure-esami everything clean distclean
all:            ## build one PDF per subject
	$(PY) build.py --all

list:           ## show subjects and chapter counts
	$(PY) build.py --list

sections:       ## build with a two-level table of contents
	$(PY) build.py --all --toc-depth 2

appunti:        ## merge each course's lecture notes (obsidian/<corso>/appunti/) into ../dispense/appunti/<corso>.pdf
	$(PY) build_appunti.py --all

formulari:      ## build the PDF of every formulary (../Formulari/Formulario_<corso>.md) next to its source
	$(PY) build_formulari.py --all

esami:          ## build the exam material of every course into ../esami/<corso>/
	$(PY) build_esami.py --all

verifica:       ## check format and completeness of the oral-exam tracks
	$(PY) verifica_orale.py --quiet

verifica-simulati: ## check the simulated Finanza Strategica exams (structure, answer key, duplicates)
	$(PY) verifica_simulati.py
	$(PY) verifica_calcoli_simulati.py

esami-volume:   ## build the single volume of every course
	$(PY) build_esami.py --volume

esercitazioni:  ## build the Econometria exercise sets: sources from the banks, then one exercises PDF and one solutions PDF per module and per appello in ../esami/econometria/esercitazioni/
	cd esami/econometria && $(PY) -m esercitazioni.build --all
	$(PY) build_esami.py --corso econometria/esercitazioni --all

figure:         ## regenerate the figures of the dispense
	for f in figure-src/01-econometria/econ-*.py; do $(PY) "$$f" || exit 1; done

figure-esami:   ## regenerate the figures of the exam solutions
	for f in esami/econometria/figure/*/plots.py; do $(PY) "$$f" || exit 1; done

everything: all esami esami-volume formulari   ## every PDF of the repository

clean:          ## remove LaTeX intermediates
	rm -rf tex/.aux-* build/*.md build/esami-* build/esercitazioni-*

distclean: clean
	rm -f tex/*.tex ../dispense/*.pdf ../esami/*/*.pdf ../Formulari/*.pdf
