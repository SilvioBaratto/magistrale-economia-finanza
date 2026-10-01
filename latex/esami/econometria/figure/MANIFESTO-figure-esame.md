---
title: "Figure originali dei temi d'esame"
tags: [corso/econometria, tipo/nota]
---

# Le figure del professore, ritagliate dai PDF d'esame

Tredici figure, estratte **vettoriali** dai temi originali: nessun ri-rendering,
nessuna ricostruzione. Il riquadro non e' stato scelto a occhio ma calcolato dai
tracciati della pagina con `pdfplumber`, ancorando il bordo inferiore alla riga
della didascalia e raggruppando i tracciati in blocchi verticali per escludere le
righe di «Nome:» e «Matricola:» (misurato: gli stacchi dentro una figura a due
pannelli arrivano a 37 pt, quello che la separa dal testo e' di 105 pt).
Il ritaglio e' fatto con `standalone` in modo `preview`.

Script: `../../../../private/tmp/.../estrai_figure.py` (copia in `_teoria/`).

| Appello | Fig. | File | Pagina d'esame | Didascalia originale |
|---|---|---|---|---|
| 2022-12-22 | 1 | `figure/2022-12-22/esame/esame-fig1.pdf` | p. 6 di `ECON_Esame_2022-12-22.pdf` | ACF e PACF dei residui della potenziale relazione di lungo periodo |
| 2022-12-22 | 2 | `figure/2022-12-22/esame/esame-fig2.pdf` | p. 8 di `ECON_Esame_2022-12-22.pdf` | ACF e PACF del modello ECM |
| 2023-01-17 | 1 | `figure/2023-01-17/esame/esame-fig1.pdf` | p. 1 di `ECON_Esame_2023-01-17.pdf` | Serie storiche del GDP di stati uniti ed Australia |
| 2023-01-17 | 2 | `figure/2023-01-17/esame/esame-fig2.pdf` | p. 3 di `ECON_Esame_2023-01-17.pdf` | ACF e PACF dei residui del modello ECM |
| 2023-01-17 | 3 | `figure/2023-01-17/esame/esame-fig3.pdf` | p. 4 di `ECON_Esame_2023-01-17.pdf` | ACF e PACF di ∆ log(usat ) |
| 2023-01-17 | 4 | `figure/2023-01-17/esame/esame-fig4.pdf` | p. 6 di `ECON_Esame_2023-01-17.pdf` | Valori predetti vs. residui |
| 2023-06-15 | 1 | `figure/2023-06-15/esame/esame-fig1.pdf` | p. 4 di `ECON_Esame_2023-06-15_Testo.pdf` | Tassi di interesse a 10 anni per Germania ed Irlanda (2001/3-2007/11). |
| 2023-12-21 | 1 | `figure/2023-12-21/esame/esame-fig1.pdf` | p. 3 di `ECON_Esame_2023-12-21.pdf` | Residui ˆ vs. valori predetti ŷ |
| 2023-12-21 | 2 | `figure/2023-12-21/esame/esame-fig2.pdf` | p. 5 di `ECON_Esame_2023-12-21.pdf` | Prezzi di oro e argento, osservati dall 1 Aprile 1968 al 7 Aprile 2021 |
| 2024-06-13 | 1 | `figure/2024-06-13/esame/esame-fig1.pdf` | p. 1 di `ECON_Esame_2024-06-13_Es2.pdf` | Grafico delle due serie storiche |
| 2024-06-13 | 2 | `figure/2024-06-13/esame/esame-fig2.pdf` | p. 3 di `ECON_Esame_2024-06-13_Es2.pdf` | ACF e PACF della serie Deltagf r |
| 2025-01-21 | 1 | `figure/2025-01-21/esame/esame-fig1.pdf` | p. 4 di `ECON_Esame_2025-01-21.pdf` | Residui vs. valori predetti |
| 2025-01-21 | 2 | `figure/2025-01-21/esame/esame-fig2.pdf` | p. 7 di `ECON_Esame_2025-01-21.pdf` | ACF e PACF della serie ∆price |

## Come si inseriscono

Vanno messe **dove la domanda le richiama**, prima della lettura del grafico, con una
didascalia che dica che sono il materiale originale della prova. La figura d'esame
precede quella costruita nello svolgimento: prima si mostra al lettore cio' che il
professore gli ha messo davanti, poi lo si rilegge con il grafico dell'inferenza.

`2023-08-29` non compare: quel tema non contiene figure.
