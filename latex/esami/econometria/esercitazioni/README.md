# Esercitazioni di Econometria

Esercizi di preparazione all'esame, dalle fondamenta di probabilità e statistica al livello delle domande d'appello. In `esami/econometria/esercitazioni/` ci sono **24 PDF**: per ognuno degli 8 moduli e dei 4 appelli simulati, un PDF di soli **esercizi** e uno di sole **soluzioni** (con richiamo, svolgimento, errore tipico, risposta da scrivere in esame e un grafico per ogni esercizio). Ogni numero che compare è prodotto da codice Python (dati sintetici, tabelle in stile gretl) e ricalcolato da un risolutore indipendente.

| Parte | Cartella | Esercizi | Nome dei PDF |
|---|---|---|---|
| 00 Fondamenta di probabilità e statistica | `moduli/00-*` | 14 | `ECON_Esercizi_00_Fondamenta-probabilita-statistica`, `ECON_Soluzioni_00_...` |
| 01 Introduzione e causalità | `moduli/01-*` | 6 | `..._01_Introduzione-causalita` |
| 02 Regressione semplice | `moduli/02-*` | 12 | `..._02_Regressione-semplice` |
| 03 Regressione multipla | `moduli/03-*` | 13 | `..._03_Regressione-multipla` |
| 04 Test F e restrizioni | `moduli/04-*` | 12 | `..._04_Test-f-restrizioni` |
| 05 Eteroschedasticità | `moduli/05-*` | 10 | `..._05_Eteroschedasticita` |
| 06 Modelli dinamici | `moduli/06-*` | 13 | `..._06_Modelli-dinamici` |
| 07 Cointegrazione e ECM | `moduli/07-*` | 13 | `..._07_Cointegrazione` |
| 08-11 Appelli simulati 1-4 | `appelli/01`…`04` | 2 ciascuno, 10 domande | `..._08_Appello-simulato-1` … `..._11_Appello-simulato-4` |

## Comandi

Da `latex/esami/econometria/`:

```bash
python3 -m esercitazioni.build --modulo 3 --check     # verifica un modulo, senza scrivere
python3 -m esercitazioni.build --modulo 3             # verifica e scrive i sorgenti renderizzati
python3 -m esercitazioni.build --appello 1            # un appello simulato
python3 -m esercitazioni.build --all                  # tutto, più COPERTURA.md
python3 -m esercitazioni.build --modulo 3 --blind-pack DIR   # pacchetto per il risolutore cieco
python3 -m esercitazioni.lib.compare_blind 03 cieco.json     # confronto col risolutore cieco (a01 per un appello)
python3 -m unittest discover -s esercitazioni/tests -t .     # test della libreria
```

Da `latex/`: `make esercitazioni` costruisce i sorgenti e i 24 PDF (circa venti minuti). Per un solo PDF: `python3 build_esami.py --corso econometria/esercitazioni --exam Esercizi_03`. I `.md` renderizzati stanno in `latex/build/esercitazioni-econometria/` (ignorato da git); ogni ricostruzione sostituisce quelli con un nome precedente.

## Come funziona

```
moduli/NN-nome/ex.py            banco: dati, stime, risposte, figure (una funzione per esercizio)
moduli/NN-nome/esercizi.tpl.md  testo, con segnaposto {{id.chiave}}
moduli/NN-nome/soluzioni.tpl.md soluzioni, con {{testo:id}} che ripete il testo dell'esercizio
appelli/NN/                     stessa forma, due esercizi per appello (id aNN_01, aNN_02)
TASSONOMIA.md                   tipi di domanda; COPERTURA.md li incrocia con gli esercizi
```

- Un esercizio è una funzione `f(rng) -> Draft` registrata con `@exercise(id, modulo=, livello=, tipo=)`. Il seed è `zlib.crc32(id)`: cambiare l'id cambia i dati. Un appello `N` usa `modulo=7+N`.
- `tipo` è un id della tassonomia o una tupla di id; l'esercizio conta per ciascuno. Origini dei tipi: `appello` (chiesti negli appelli veri: ≥2 esercizi di cui uno di livello 3), `ripasso` (i tre ripassi di statistica) e `corso` (insegnati dalle note ma mai chiesti): ≥1 esercizio.
- Le **risposte nelle soluzioni** sono ricalcolate dalla sola tabella stampata, con i numeri arrotondati come all'esame; la build rifiuta lo scarto oltre un'unità dell'ultima cifra.
- Ogni decisione di un test ha un `Margin`: la statistica sta a più del 15% dal valore critico.
- Le `attese` fissano la storia dell'esercizio e verificano numericamente le formule derivate (derivata numerica, identità esatte, simulazione).
- Le etichette dei `Quesito` ((a), (b)… negli esercizi dei moduli, `d1`…`d10c` negli appelli) devono puntare alla risposta giusta: verità e percorso studente usano le stesse chiavi, quindi un errore di mappatura lo vede solo il risolutore cieco.
- Il lint rifiuta decimali e interi di tre cifre scritti a mano nei template, salvo le costanti ammesse in `lib/config.py`.
- I titoli degli esercizi nei template sono a livello `#`: ogni PDF li usa come capitoli.

Una `t` con valore assoluto da 100 in su, stampata a 4 cifre significative, non regge due decimali: scegliere i `decimali` di conseguenza.

## Verifica

Per ogni modulo e appello: la build (`--check`), un risolutore cieco che riceve il solo testo (`--blind-pack`) e `compare_blind` che confronta le sue risposte con quelle del banco; infine una revisione concettuale delle soluzioni contro le note del corso. Convenzioni fissate (valori critici, segno dell'ECM, conteggio dei periodi di assorbimento, errori standard robusti HC1) in `TASSONOMIA.md`.

## Versioni

I risultati dipendono dalle librerie: numpy 1.26.4, scipy 1.13.1, statsmodels 0.14.5, matplotlib 3.9.4, pandas 2.3.3. Servono `pandoc`, `xelatex` e `latexmk`.

## Avvertenza

Esercizi sintetici costruiti a fini di studio sul modello dei veri appelli: non sono materiale ufficiale del docente.
