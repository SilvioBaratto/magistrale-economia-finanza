# Finanza Strategica (EM5005) — tracce d'esame e appelli simulati

Le tracce degli appelli passati, riportate come le ha date il docente: **senza risposte, senza
svolgimenti, senza note a mano**. Un PDF per appello, con lo stesso template delle dispense.
I sorgenti stanno qui; i PDF escono in `esami/finanza-strategica/` alla radice del repository.

| Appello | Sorgente | Struttura |
|---|---|---|
| Primo appello, 23 dicembre 2022, versione B | `src/FSTR_Esame_2022-12-23_Primo-Appello-B.md` | 20 domande a risposta multipla · 2 esercizi · 2 domande di teoria (se ne svolge una) |

Qui c'è solo l'esame **completo**, con tutte e tre le parti (test, esercizi, teoria). L'appello del
13 dicembre 2021 (versioni A e B, solo esercizi e teoria) non è stato tenuto: il testo resta nella
trascrizione `Moodle/11-Finanza-Strategica/Esami/FSTR_Esame_Esercizi-Appelli-Passati-A-B.md`.

## Da dove viene il testo

Dalle trascrizioni in `Moodle/11-Finanza-Strategica/Esami/*.md` (a loro volta dai PDF `FSTR_Esame_*`).
Quelle trascrizioni restano fedeli al foglio, con crocette, note a mano e soluzioni; il sorgente
di qui è la **versione pulita** e si corregge qui, non lì. Non c'è un legame automatico: se si
cambia una cifra in una, va riportata nell'altra.

Regole usate per pulire:

- **Parola per parola.** I refusi del docente restano (`Tehcnostamp`, `del'80%`, `fin a 10 punti`,
  `ed :`). Cambiano solo i difetti di impaginazione dello scan: il punto doppio in `B. . una presenza`
  e l'etichetta ripetuta in `C. C. si sta utilizzando`.
- **Numeri come stampati** (`355.579`, `1.09` nella tabella di settore, `10,20%` nel testo).
- Le risposte segnate sul foglio non compaiono: il PDF non è una chiave.

## Cosa manca nell'originale

- La foto dell'esame è **tagliata**: la tabella dei multipli di settore (Esercizio 1) finisce alla
  riga *Education*; le righe successive non sono visibili. Il dato che serve all'esercizio
  (*Building Materials*, 1.09) c'è.
- I numeri delle domande 14 e 15 non si vedono nella foto: sono dedotti dalla sequenza.

## Compilare

```bash
python3 build_esami.py --corso finanza-strategica --all
python3 build_esami.py --corso finanza-strategica --exam 2022-12-23   # un solo appello
```

Non c'è volume unico (`volume=None` in `build_esami.py`): ogni appello è un PDF.

## Formato del sorgente

Front matter con `title`, `subtitle`, `stats`; un capitolo per parte (`# Test a risposta
multipla`, `# Esercizi`, `# Domande di teoria`). Ogni domanda o esercizio è un blocco
`::::: {.callout kind="question" heading="N"}` (testo d'esame, `cvtesto`). Le alternative sono
scritte `A.  testo` con **due spazi** dopo il punto: con uno solo pandoc non le legge come elenco.

## Teoria: le stesse domande tornano

Le trascrizioni `Moodle/11-Finanza-Strategica/Esami/FSTR_Esame_Teoria_*.md` riportano, con la risposta
scritta a mano, le Domande A e B del 2021. La Domanda B del 2022 è la stessa del 2021, parola per parola
(divisa in punti a), b), c)); la Domanda A del 2022 è nuova (tipologie di integrazione, formula del valore
di acquisizione, benefici privati). Nel PDF qui le risposte non ci sono.

## Dieci appelli simulati

Dieci appelli completi costruiti sul modello del 23/12/2022 (20 test A/B/C, 2 esercizi, 2 domande di teoria di cui se ne svolge una) e sulle note di `obsidian/11-Finanza-Strategica/`. Per ognuno due PDF in `esami/finanza-strategica/`: `FSTR_Esame_Simulato_NN.pdf` (la traccia, senza risposte) e `FSTR_Soluzioni_Simulato_NN.pdf` (chiave del test con la sezione della nota che giustifica ogni risposta, esercizi con tutti i passaggi, tracce di risposta per la teoria). **Non sono tracce ufficiali del docente.**

| Appello | Esercizio 1 | Esercizio 2 (NPV per A) |
|---|---|---|
| 01 | multipli EV/Sales | sinergie, negativo |
| 02 | multipli EV/Sales | sinergie, positivo |
| 03 | multipli EV/Sales | sinergie con benefici privati, positivo |
| 04 | WACC: beta unlevered, CAPM, VAN | sinergie, negativo |
| 05 | multipli EV/Sales | sinergie, positivo |
| 06 | DCF: VAM sintetico e analitico, peso del TV | sinergie, negativo |
| 07 | multipli EV/Sales | sinergie con benefici privati, positivo |
| 08 | opzioni reali: VAN medio e opzione di abbandono | sinergie, negativo |
| 09 | multipli EV/Sales | sinergie, positivo |
| 10 | multipli EV/Sales | sinergie con benefici privati, negativo |

Il test segue il mix del 2022 (investimenti 3, costo del capitale 3, DCF 3, multipli 5, sinergie 4, due diligence 2): in totale 200 domande, che toccano tutte le sezioni di contenuto delle lezioni 01-12.

Oltre ai file singoli ci sono due volumi, un file per tutti gli appelli e uno per tutte le soluzioni, con un capitolo per appello (Test, Esercizi, Teoria): `FSTR_Esame_Simulato_Completo.pdf` (73 pp, 200 domande) e `FSTR_Soluzioni_Simulato_Completo.pdf` (86 pp). Si compilano con `python3 build_esami.py --corso finanza-strategica --volume`.

### Convenzioni da conoscere

- **Esercizio 2: metodo del docente, non la formula della nota.** Come nello svolgimento dell'appello 2022 e negli esercizi in aula, la quota acquistata α scala **solo** la sinergia di tasso; le sinergie di flusso, di debito e dell'investimento addizionale sono interamente di A e il valore stand alone della quota è (attivi − PFN)·α. La nota FSTR 12 scrive invece α(W_S + W_D). Nei dieci appelli il segno dell'NPV non dipende dalla scelta (le soluzioni, nel file di calcolo, tengono le due varianti a confronto), ma i valori sì. È una decisione aperta: da confermare col docente.
- **Benefici privati** (appelli 03, 07, 10): trattati come senza effetto sui flussi stand alone del target, quindi per intero ad A.
- **Teoria:** nessuna domanda propone la formula con α, per non contraddire l'esercizio.
- **Opzione di abbandono (08):** il flusso dell'anno 1 si attualizza una volta sola. Lo svolgimento dell'Esercizio 4 delle dispense (`Moodle/.../FSTR_Eserc_Extra-Dispense-sol_...`, p. 3) sconta due volte il flusso dell'anno 1 e non è stato replicato.
- Escluse dalle domande le convenzioni dove slide e note divergono (EV con PFN negativa, definizione di ROI, plusvalenza della lezione 08, numeri del razionamento di capitale, FCFE di DeLonghi, TV dello scudo fiscale con (1+g), tipo di fusione di Eni/Matrìca-Novamont).

### Come sono stati controllati

Ogni numero è calcolato da uno script (`calc.py`) e copiato dall'output. Ogni appello è passato da: un verificatore indipendente che ha risposto al test usando solo le note e ricalcolato gli esercizi da zero prima di vedere le soluzioni; le correzioni; un secondo passaggio cieco (risposta al test senza chiave, controllo di ogni citazione). I passaggi hanno trovato, fra gli altri, domande risolvibili dal testo di altre parti dell'appello, doppioni fra appelli, un residuo numerico dopo la scalatura dei dati e lettere sbagliate nelle motivazioni dopo uno scambio di alternative.

```bash
python3 build_esami.py --corso finanza-strategica --all      # un PDF per sorgente
python3 build_esami.py --corso finanza-strategica --volume   # i due volumi unici (appelli, soluzioni)
python3 verifica_simulati.py                              # struttura, bilanciamento delle risposte, doppioni, residui TeX, citazioni delle note
python3 verifica_calcoli_simulati.py                      # ricalcola gli esercizi dalle tracce e li confronta con le soluzioni
python3 verifica_simulati.py --lettere 7                  # le lettere citate nelle motivazioni, accanto all'alternativa
```

Dopo ogni modifica a un'alternativa o a una chiave rilancia `verifica_simulati.py --lettere NN`: le motivazioni citano le alternative per lettera e vanno aggiornate a mano.

## Prossimi appelli

Altre tracce vanno aggiunte come `src/FSTR_Esame_<AAAA-MM-GG>_<Appello>-<Versione>.md`, nello
stesso formato, partendo dal testo originale (non dalle trascrizioni con annotazioni).
