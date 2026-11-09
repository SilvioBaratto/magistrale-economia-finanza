# Esami di Econometria — soluzioni svolte

Soluzioni dei temi d'esame **in stile docente** (prof. Raggi): per ogni domanda il
testo integrale, una risposta breve di 3-8 righe e una figura. Un PDF per appello.

Il metodo è quello delle soluzioni ufficiali dei Problem Set e dei manoscritti del
15/06/2023 e del 29/08/2023: effetto marginale scritto come Δ, decisione con
l'intervallo di confidenza o con il test F su un vincolo lineare, conversioni in
percentuale con la sola approssimazione 100·β, soglia VIF 10, numerazione dei
coefficienti come nel testo dell'esame. Ogni numero è ricavabile dalle sole tabelle
del testo d'esame. Per le domande 1-6 di 15/06/2023 e 29/08/2023 le risposte seguono
il manoscritto; per gli altri cinque appelli non esiste una soluzione del prof e lo
stile è dedotto dai Problem Set.

Le versioni lunghe, con derivazioni e richiami di teoria (circa 45 pagine ad
appello), sono nella storia di git al commit `7059143`.

## Struttura

Questa cartella contiene i **sorgenti**; i PDF escono in `esami/econometria/`
alla radice del repository. La compilazione è quella delle dispense: stesso
template (`latex/template/dispensa.latex`), stesso filtro generale
(`latex/filters/callouts.lua`), più `latex/filters/esami.lua` per i blocchi
d'esame, che gira per primo perché qui i tipi di callout hanno un altro
significato (per esempio `abstract` sono i dati, non una definizione).

```
latex/
├── build_esami.py                <- Markdown -> PDF (pandoc + latexmk)
├── filters/esami.lua             <- blocchi d'esame (Testo, Dati, Richiamo, Svolgimento, Risposta)
└── esami/econometria/
    ├── src/ECON_Sol_<data>.md    <- sorgente Markdown di ogni soluzione
    ├── figure/<data>/plots.py    <- script che genera TUTTE le figure di quell'esame
    ├── figure/<data>/*.pdf       <- figure vettoriali, incluse nel PDF
    ├── figure/econstyle.py       <- stile e primitive grafiche condivise
    └── macros.tex                <- notazione del corso (\Var, \Cov, \Ex, \plim, \se, \betah)

esami/econometria/ECON_Sol_<data>.pdf   <- i PDF finali
```

## Il volume unico

Oltre ai sette PDF per appello c'è `ECON_Soluzioni_Raccolta.pdf`: gli stessi
svolgimenti in un solo documento, con un frontespizio e un indice soli,
numerazione di pagina continua e un appello per parte. Le etichette delle
equazioni e delle figure vengono **spaziate per appello** durante la
composizione (i sette sorgenti nascono indipendenti e riusano gli stessi nomi,
`eq:d01-derivata`, `fig:d03`): senza il prefisso i rimandi punterebbero
all'appello sbagliato.

```bash
python3 build_esami.py --corso econometria --volume   # ECON_Soluzioni_Raccolta.pdf
```

## Ricompilare

Dalla cartella `latex/`:

```bash
python3 build_esami.py --corso econometria --list               # cosa c'è e cosa è già compilato
python3 build_esami.py --corso econometria --all                # ricompila tutti gli appelli
python3 build_esami.py --corso econometria --exam 2025-01-21    # ricompila un PDF
python3 build_esami.py --corso econometria --volume             # il volume unico
python3 build_esami.py --corso econometria --exam 2025-01-21 --keep   # conserva il .tex
python3 esami/econometria/figure/2025-01-21/plots.py   # rigenera le figure di un appello
make esami esami-volume                           # tutti i corsi, via make
```

Requisiti: `pandoc`, `xelatex` + `latexmk` (TeX Live), Python con
`numpy`/`scipy`/`matplotlib` (`pandas`/`statsmodels` solo per l'appello 2023-12-21,
l'unico con i dati veri).

## Che cosa c'è

| PDF | Domande | Figure | Righe di sorgente |
|---|---|---|---|
| `ECON_Sol_2022-12-22.pdf` | 10 | 10 | 323 |
| `ECON_Sol_2023-01-17.pdf` | 10 | 10 | 302 |
| `ECON_Sol_2023-06-15.pdf` | 10 | 10 | 279 |
| `ECON_Sol_2023-08-29.pdf` | 10 | 10 | 271 |
| `ECON_Sol_2023-12-21.pdf` | 10 | 10 | 274 |
| `ECON_Sol_2024-06-13.pdf` | 10 | 10 | 261 |
| `ECON_Sol_2025-01-21.pdf` | 10 | 10 | 261 |

**70 domande, 70 figure.** Ogni domanda ha il testo integrale, la risposta breve e la figura.
Ciascun sorgente è stato ricontrollato da un revisore indipendente, che ha ricalcolato i
numeri dalle tabelle d'esame; le scelte dubbie (per esempio dove l'esame è incoerente con sé
stesso) sono state decise caso per caso seguendo il metodo dei Problem Set.

## Corrispondenza esame → soluzione

| Soluzione | Testo d'esame (Moodle del corso) | Domande |
|---|---|---|
| `ECON_Sol_2022-12-22` | `ECON_Esame_2022-12-22.md` | 1–10 |
| `ECON_Sol_2023-01-17` | `ECON_Esame_2023-01-17.md` | 1–10 |
| `ECON_Sol_2023-06-15` | `ECON_Esame_2023-06-15_Testo.md` (= `_Es1-v2` dom. 1–6 + `_Es1` dom. 7–10) | 1–10 |
| `ECON_Sol_2023-08-29` | `ECON_Esame_2023-08-29.md` | 1–10 |
| `ECON_Sol_2023-12-21` | `ECON_Esame_2023-12-21.md` | 1–10 |
| `ECON_Sol_2024-06-13` | `ECON_Esame_2024-06-13_Es1.md` + `_Es2.md` | 1–10 |
| `ECON_Sol_2025-01-21` | `ECON_Esame_2025-01-21.md` | 1–10 |

`ECON_Esame_2024-01-16_Soluzione.md` non compare: è già una soluzione (ufficiale,
solo Parte I) e il testo del relativo appello non è disponibile. Serve da metro di
paragone per lo stile atteso.

## Impianto di ogni risposta

Lo stesso delle dispense (vedi `latex/README.md`): stile del template
Polimi adattato ad appunti, Latin Modern, capitoli "**N |** Esercizio" in blu,
sezioni numerate per domanda, equazioni numerate **solo** dove il testo le cita.
Le figure usano lo stesso font (`figure/econstyle.py`).

Ogni domanda è scandita da blocchi con testa a capoverso:

1. **Testa blu in neretto, corpo tondo** — testo d'esame, dati e output,
   richiami teorici, svolgimento, risposta.
2. **Testa in corsivo** — osservazioni e note.
3. **Corpo del testo** — l'impostazione e il ragionamento.

### Autosufficienza

I documenti **non rimandano ad alcun file esterno**: la formula che serve a una risposta
(effetto marginale, varianza di β̂ⱼ con il VIF, assorbimento dell'ECM) è scritta nella
risposta stessa. Le derivazioni complete restano in `_teoria/`.

## Avvertenza

Svolgimento personale a fini di studio: non è una soluzione ufficiale e non è stato
corretto dal docente.
