# Economia e Finanza — appunti e dispense

Appunti di studio per la Laurea Magistrale in **Economia e Finanza**
dell'Università Ca' Foscari Venezia, A.A. 2026/2027: le note di ogni
insegnamento in formato Obsidian, le dispense PDF composte da quelle note e gli
esami di Econometria svolti passo per passo, con tutte le figure.

> Appunti personali, non ufficiali e non rivisti dai docenti. Possono contenere
> errori: verificare sempre sul materiale del corso.

## Dispense

Un PDF per insegnamento, generato dalle note Obsidian.

| Insegnamento | Codice | Dispensa | Pagine | Note Obsidian |
|---|---|---|---|---|
| Econometria | EM0004 | [PDF](dispense/01-econometria.pdf) | 115 | [note](obsidian/01-Econometria/) |
| Legislazione Bancaria — modulo 1 | EM2101 | [PDF](dispense/03-legislazione-bancaria-1.pdf) | 70 | [note](obsidian/03-Legislazione-Bancaria-1/) |
| Legislazione Bancaria — modulo 2 | EM2101 | [PDF](dispense/04-legislazione-bancaria-2.pdf) | 102 | [note](obsidian/04-Legislazione-Bancaria-2/) |
| Economia dei Mercati e degli Investimenti Finanziari — modulo 1 | EM5002 | [PDF](dispense/05-economia-mercati-investimenti-1.pdf) | 260 | [note](obsidian/05-Economia-Mercati-Investimenti-1/) |
| Gestione della Banca | EM2102 | [PDF](dispense/07-gestione-della-banca.pdf) | 86 | [note](obsidian/07-Gestione-della-Banca/) |
| Diritto del Mercato Finanziario | EM0001 | [PDF](dispense/08-diritto-mercato-finanziario.pdf) | 105 | [note](obsidian/08-Diritto-Mercato-Finanziario/) |
| Metodi per la Gestione dei Portafogli Personali | EM5011 | [PDF](dispense/09-metodi-portafogli.pdf) | 151 | [note](obsidian/09-Metodi-Portafogli/) |
| Misurazione del Rischio | EM5012 | [PDF](dispense/10-misurazione-rischio.pdf) | 7 | [note](obsidian/10-Misurazione-Rischio/) |
| Finanza Strategica | EM5005 | [PDF](dispense/11-finanza-strategica.pdf) | 159 | [note](obsidian/11-Finanza-Strategica/) |
| **Volume unico** (tutti gli insegnamenti) | | [PDF](dispense/00-dispense-complete.pdf) | 1052 | |

## Esami svolti — Econometria

Testo d'esame, richiami di teoria, svolgimento e risposta per ogni domanda, con
una figura per ogni passaggio inferenziale.

| Appello | Soluzione | Pagine | Sorgente |
|---|---|---|---|
| 22/12/2022 | [PDF](esami/econometria/ECON_Sol_2022-12-22.pdf) | 47 | [sorgente](latex/esami/econometria/src/ECON_Sol_2022-12-22.md) |
| 17/01/2023 | [PDF](esami/econometria/ECON_Sol_2023-01-17.pdf) | 49 | [sorgente](latex/esami/econometria/src/ECON_Sol_2023-01-17.md) |
| 15/06/2023 | [PDF](esami/econometria/ECON_Sol_2023-06-15.pdf) | 50 | [sorgente](latex/esami/econometria/src/ECON_Sol_2023-06-15.md) |
| 29/08/2023 | [PDF](esami/econometria/ECON_Sol_2023-08-29.pdf) | 48 | [sorgente](latex/esami/econometria/src/ECON_Sol_2023-08-29.md) |
| 21/12/2023 | [PDF](esami/econometria/ECON_Sol_2023-12-21.pdf) | 42 | [sorgente](latex/esami/econometria/src/ECON_Sol_2023-12-21.md) |
| 13/06/2024 | [PDF](esami/econometria/ECON_Sol_2024-06-13.pdf) | 47 | [sorgente](latex/esami/econometria/src/ECON_Sol_2024-06-13.md) |
| 21/01/2025 | [PDF](esami/econometria/ECON_Sol_2025-01-21.pdf) | 43 | [sorgente](latex/esami/econometria/src/ECON_Sol_2025-01-21.md) |
| **Tutti gli appelli** | [PDF](esami/econometria/ECON_Soluzioni_Raccolta.pdf) | 329 | |

## Contenuto

```
.
├── dispense/              le dispense (solo PDF)
├── esami/
│   └── econometria/       le soluzioni d'esame (solo PDF)
├── obsidian/              note Obsidian, una cartella per insegnamento (+ immagini in assets/)
└── latex/                 l'unica soluzione LaTeX: template, filtri, script, figure
    ├── build.py           dispense  (obsidian/ -> dispense/)
    ├── build_esami.py     esami     (latex/esami/ -> esami/)
    ├── esami/econometria/ sorgenti e figure delle soluzioni d'esame
    └── figure-src/        script e dati delle figure delle dispense
```

## Leggere le note in Obsidian

Aprire la cartella `obsidian/` come vault (*Open folder as vault*). Ogni
insegnamento ha una nota indice con l'ordine delle lezioni. Le note si leggono
anche direttamente su GitHub.

## Ricompilare

| Strumento | Versione usata |
|---|---|
| pandoc | 3.8 |
| TeX Live (XeLaTeX + latexmk) | 2025, con Latin Modern |
| Python | 3.12 con numpy, scipy, matplotlib, pandas, statsmodels |

```bash
cd latex
make everything        # tutte le dispense, le soluzioni d'esame e la raccolta
make combined          # solo le dispense (+ volume unico)
make esami             # solo le soluzioni d'esame
make figure            # rigenera le figure delle dispense
```

Dettagli in [`latex/README.md`](latex/README.md) e
[`latex/esami/econometria/README.md`](latex/esami/econometria/README.md).

## Crediti

- Contenuti tratti dal materiale didattico ufficiale degli insegnamenti
  (slide, dispense, temi d'esame), rielaborato a fini di studio.
- Impaginazione ispirata al template Overleaf *Polimi Thesis in Computer
  Science and Engineering* (D. Baroffio, F. Reghenzani), derivato dalla classe
  PoliMi3i del Politecnico di Milano; nessun file di quel template è incluso.
- Dataset delle figure: quelli distribuiti nel corso di Econometria.
