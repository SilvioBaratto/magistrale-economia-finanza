# LaTeX — dispense e soluzioni d'esame

Un'unica soluzione LaTeX per tutti i PDF del repository, con un template e un
filtro condivisi:

| Script | Da | A |
|---|---|---|
| `build.py` | vault Obsidian (`../obsidian/`) | una dispensa per insegnamento in `../dispense/`, più un volume unico |
| `build_esami.py` | materiale d'esame (`esami/<corso>/src/`) | un PDF per sorgente in `../esami/<corso>/`, più il volume unico di ogni corso |

Nulla viene scritto dentro `../obsidian/`. Il materiale d'esame di ogni corso ha il suo README:

| Corso | Che cosa | README |
|---|---|---|
| `econometria` | soluzioni svolte dei temi d'esame, con figure | [`esami/econometria/README.md`](esami/econometria/README.md) |
| `legislazione-bancaria-1` | tracce per la prova orale, punti 1-7 | [`esami/legislazione-bancaria-1/README.md`](esami/legislazione-bancaria-1/README.md) |
| `legislazione-bancaria-2` | tracce per la prova orale, punti 8-11 | [`esami/legislazione-bancaria-2/README.md`](esami/legislazione-bancaria-2/README.md) |

`verifica_orale.py` controlla formato e completezza delle tracce d'orale prima di compilarle.

## Uso

```bash
python3 build.py --list                    # insegnamenti e numero di capitoli
python3 build.py --all                     # un PDF per insegnamento -> ../dispense/
python3 build.py --subject 01-Econometria  # solo un insegnamento
python3 build.py --all --combined          # aggiunge ../dispense/00-dispense-complete.pdf
python3 build.py --all --toc-depth 2       # indice con capitoli + sezioni
python3 build.py --all --keep              # conserva .md intermedi e file ausiliari LaTeX
```

Oppure `make`, `make list`, `make combined`, `make sections`, `make clean`.
Per il materiale d'esame `make esami` e `make esami-volume` (`make verifica` per le tracce d'orale); `make everything`
ricompila ogni PDF del repository, `make figure` e `make figure-esami`
rigenerano le figure.

## Requisiti

| Strumento | Versione testata | Note |
|-----------|------------------|------|
| pandoc    | 3.8.2            | `brew install pandoc` |
| XeLaTeX + latexmk | TeX Live 2025 | font Latin Modern (OpenType) + Latin Modern Math |
| Python    | 3.12             | build: libreria standard; figure: numpy, scipy, matplotlib, pandas, statsmodels |

## Pipeline

```
../obsidian/<Materia>/*.md
    └─ build.py      front-matter, ordine dei capitoli, callout, wikilink, glifi
        └─ build/<slug>.md            markdown normalizzato
            └─ pandoc + filters/callouts.lua + template/dispensa.latex
                └─ tex/<slug>.tex
                    └─ latexmk -xelatex
                        └─ ../dispense/<slug>.pdf
```

### Cosa fa la normalizzazione

- **Ordine dei capitoli**: letto dalla lista `## Lezioni` della nota indice
  (`tipo/indice`) di ogni cartella; le note non elencate finiscono in coda.
- **Front matter**: `title` diventa il titolo del capitolo, `source`/`pages`
  la riga "Fonte: ..." sotto il titolo (disattivabile con `--no-sources`).
- **Callout Obsidian** → blocchi con testa a capoverso, numerati per capitolo
  dove serve, senza riquadri né colori (stili `amsthm`):

  | Callout      | Ambiente LaTeX     | Resa |
  |--------------|--------------------|------|
  | `[!abstract]`| `cvdefinizione`    | **Definizione 3.2.** testa blu in neretto, corpo tondo |
  | `[!tip]`     | `cvteorema`        | **Teorema 3.1.** testa blu in neretto, corpo tondo |
  | `[!example]` | `cvesempio`        | **Esempio 3.4.** testa blu in neretto, corpo tondo |
  | `[!note]`    | `cvdimostrazione`  | *Dimostrazione.* testa in corsivo, quadratino finale |

- **Wikilink**: `[[Nota|etichetta]]` diventa un rimando interno se la nota è nello
  stesso PDF, altrimenti resta testo semplice.
- **Riferimenti alle slide**: le righe `*(slide 11–18)*` vanno in corsivo piccolo,
  a filo destro sull'ultima riga del capoverso che precede (su una riga propria
  solo se non c'è spazio o se prima c'è un blocco).
- **Glifi**: i simboli che Latin Modern non ha (→, ⇒, ✓, ✗, greche fuori dalla
  matematica, ...) sono riscritti con `\ensuremath`, mai con `$...$`, e **solo fuori
  dalle formule**.
- **Dollari**: `$` di valuta (`$29.68`, `($)`) vengono protetti, altrimenti pandoc
  li accoppia al dollaro successivo e apre una formula che si mangia il testo.
- **Virgola decimale**: con `decimalcomma` `1,5` è un decimale e `1, 5` un elenco;
  le virgole di tuple intere (`N(0,1)`, `(1,0)'`), di serie `1,2,3` e dei capoversi
  che scrivono i decimali come `0{,}30` ricevono lo spazio da separatore.
- **Tabelle**: larghezze delle colonne calcolate dal contenuto (algoritmo
  automatico delle tabelle CSS); se non entrano nella giustezza sconfinano
  centrate nei margini fino a 10 mm per lato, poi scendono a `\footnotesize` e
  `\scriptsize`.
- **Formule in display** più larghe della riga: stesso criterio, margini prima e
  riduzione di scala solo oltre.
- Blocchi di codice (output gretl/R) a capo automatico con segno di continuazione.
- **Figure**: le immagini incorporate nelle note (`![](assets/...)` o `![[file.png]]`)
  vengono copiate in `tex/img/` (il percorso del vault contiene spazi) e messe al
  centro nel flusso del testo, non come oggetti flottanti: il paragrafo
  "Figura N — ..." che segue le descrive. Il testo alternativo, se c'è, va sotto
  in corsivo piccolo.

Se accanto al PNG c'è un PDF con lo stesso nome, LaTeX usa il PDF (vettoriale).

### Figure di Econometria

Le 54 figure di `obsidian/01-Econometria` sono ridisegnate in matplotlib, una per
script, identiche agli originali delle slide del corso:

| Fonte dei dati | Figure |
|---|---|
| estratti dal grafico vettoriale della slide (`figure-src/01-econometria/data/*.csv`) | 28 |
| dataset reali del corso (copie in `figure-src/datasets/`) | 17 |
| diagrammi ridisegnati | 6 |
| curve analitiche | 2 |
| simulate (originale raster), con nota sotto la figura | 1 |

```bash
python3 figure-src/01-econometria/econ-06-fig04.py   # rigenera PNG + PDF di una figura
for f in figure-src/01-econometria/econ-*.py; do python3 "$f"; done
```

Ogni script scrive `obsidian/01-Econometria/assets/econ-0N/figNN.png` (per Obsidian)
e il `.pdf` accanto (per la dispensa). Stile condiviso in `figure-src/style.py`:
Latin Modern, blu Polimi, palette gretl `GP_RED`/`GP_GREEN`/`GP_BLUE` per i grafici
che nelle slide vengono da gretl.

## Impianto tipografico

Stile del template Overleaf *Polimi Thesis in Computer Science and Engineering*
(D. Baroffio, F. Reghenzani), derivato dalla classe `PoliMi3i_thesis` del
Politecnico di Milano (P. F. Antonietti, S. Bonetti, A. Gruttadauria,
G. Mescolini, A. Zingaro, 2021). Lo stile è **riprodotto** in
`template/dispensa.latex`; nessun file di quel template è copiato nel repository
(la classe riporta "All rights reserved").

Dallo stile originale: Latin Modern (lo stesso disegno del Computer Modern),
capitoli "**N |** Titolo" in blu Polimi, sezioni nere numerate "2.1.",
testatina "N| Capitolo" e numero di pagina, teste dei blocchi in blu neretto,
`parskip` con rientro di 10 pt.

Adattato da tesi a dispensa:

| Tesi (originale) | Dispensa |
|---|---|
| fronte-retro, pagina bianca prima di ogni capitolo | solo fronte, capitolo su pagina nuova senza bianche |
| margini 3,0 / 2,0 cm per la rilegatura | 2,5 cm simmetrici |
| 12 pt, interlinea 1,5 (regolamento tesi) | 11 pt, interlinea 1,15 |
| corpo dei teoremi in corsivo | corpo tondo: definizioni ed esempi lunghi |
| frontespizio con logo, matricola, relatore | Ateneo, corso di laurea, "Appunti di", contenuto, A.A. |
| "Contents" elencato nell'indice | l'indice non elenca sé stesso |
| — | segnalibri PDF fino alle sottosezioni |

Logo, raggiera e diciture del Politecnico sono esclusi: le dispense non sono
documenti del Politecnico.

Lo stesso template e lo stesso filtro generale compongono le soluzioni d'esame
(`build_esami.py`): una modifica qui cambia anche quei PDF, da ricompilare con
`make esami esami-volume`.

## Personalizzare

- **Aspetto** (font, colori, gabbia, frontespizio, testatine, blocchi):
  `template/dispensa.latex`.
- **Mappatura callout → ambiente, larghezze delle tabelle, formule larghe**:
  `filters/callouts.lua` (le costanti delle tabelle dipendono da corpo e
  `\tabcolsep` del template); blocchi del materiale d'esame (domanda, dati,
  richiamo, svolgimento, risposta) in `filters/esami.lua`.
- **Un nuovo corso d'esame**: una voce in `COURSES` di `build_esami.py` e i
  sorgenti in `esami/<corso>/src/`.
- **Autore, ateneo, anno accademico, disclaimer**: costanti in cima a `build.py`.

## Note

- `tex/` e `build/` sono intermedi (ignorati da git). I PDF non stanno qui: le
  dispense escono in `../dispense/`, il materiale d'esame in `../esami/<corso>/`.
- Un errore LaTeX interrompe il build e stampa le ultime righe del log; i file
  ausiliari restano in `tex/.aux-<slug>/` se si usa `--keep`.
