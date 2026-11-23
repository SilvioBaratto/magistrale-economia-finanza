# Economia del Rischio e delle Assicurazioni (EM2080) — appelli simulati

Sei appelli scritti simulati, costruiti sul modello dell'unico appello vero disponibile e sulle note di
`obsidian/14-Economia-Rischio-Assicurazioni/`. Per ognuno due PDF in `esami/economia-rischio-assicurazioni/`:
`ERA_Esame_Simulato_NN.pdf` (la traccia, senza risposte) e `ERA_Soluzioni_Simulato_NN.pdf` (richiamo, svolgimento,
risposta da scrivere in esame e, dove c'è, l'errore tipico), più due volumi con tutti gli appelli:
`ERA_Esame_Simulato_Completo.pdf` e `ERA_Soluzioni_Simulato_Completo.pdf`. **Non sono tracce ufficiali del docente.**

| Appello | A (avversione al rischio) | B | C (confronto di opzioni) | D | E |
|---|---|---|---|---|---|
| 01 | $u=-1/W$: CE, prudenza e DARA, scala della lotteria | selezione avversa (ERA 07) | dominanza, struttura di Allais | azzardo morale, benchmark | portafoglio: $\partial\alpha^*/\partial w_0$, rischiosità del titolo |
| 02 | $\sqrt W$ e $\ln W$: trasformazione concava | prezzo dei titoli (ERA 06) con ln: kernel, titoli multipli, partecipazione limitata | dominanza sui rendimenti in eccesso | azzardo morale, impegno alto | portafoglio: $V'(0)$, l'agente più avverso investe meno |
| 03 | CARA: forma chiusa, DARA debole, verso $(3)\Rightarrow(2)$ | lotterie composte, triangolo di Machina, Ellsberg (max-min) | condivisione del rischio, $N=1$ contro $N=2$ | screening (ERA 07) | portafoglio con CRRA, $r=10\%$ |
| 04 | utilità quadratica: il premio cresce con la ricchezza | selezione avversa e screening con ln | nessun ordine; investitore con $\sqrt z$ | azzardo morale con numeri | prezzo dei titoli (ERA 06): segno della domanda, $n$ titoli |
| 05 | ln contro CARA: due agenti non confrontabili | puzzle dell'equity premium, due paesi, titolo correlato | distribuzioni continue (uniformi, normali) | azzardo morale: PC e IC dal testo | portafoglio con CARA, DARA e ricchezza |
| 06 | CRRA con $\gamma=3$: CE esatto e approssimazione | scommessa con $E[X]>0$ e ln, DARA | solo SOSD, medie diverse | azzardo morale con ln: polizza e franchigia | portafoglio con tassazione e sussidio |

## Da dove viene la struttura

Dal solo appello vero su Moodle, `Moodle/14-Economia-Rischio-Assicurazioni/Esami/ERA_Esame_2025-06-13_Mock-exam.pdf` (nome «Mock
exam», intestazione di un esame con data reale: non è chiaro se sia un vero appello): 5 domande A-E da 20 punti, 17 sotto-domande
(A 4, B 4, C 4, D 3, E 2), 90 minuti, 100 punti, a libro chiuso, con limiti di righe («max 2 righe», «max 3 righe») e «Consigli»
brevi. Ogni simulato ha la stessa forma: stesse sezioni, stessi punti, stessi limiti di righe, stesse istruzioni. Il Mock non
indica la soglia di sufficienza. L'altro documento del corso, `ERA_Esame_2024_Dimostrazioni-per-l-esame.pdf`, è un elenco di 18
titoli di dimostrazioni per lezione: dice che cosa il docente considera dimostrabile, e ha orientato le domande E e le
dimostrazioni guidate.

## Divergenze da sapere

- **I pesi non vengono da dati.** Un solo appello più un elenco di titoli: le unità del piano (20, una per tema delle note) hanno
  pesi stimati, non ricavati da più appelli. Il piano è in `piano/blueprint.json`.
- **Il tema di B, D ed E ruota.** Nel Mock D è sempre azzardo morale (ERA 08) ed E sempre portafoglio (ERA 05); ERA 06 e 07 non
  compaiono, ma l'elenco delle dimostrazioni ha sei voci su quelle due lezioni. Per coprirle B, D ed E cambiano argomento fra gli
  appelli (D è screening nel 03, E è prezzo dei titoli nel 04), mantenendo tipo di domanda, punti e limiti di righe.
- **Voci escluse.** Nell'elenco delle dimostrazioni due voci sono barrate in rosso (1(a) «Jensen» e 2(a) «Mean-preserving spread
  implica SOSD»): non sono state usate come domande di dimostrazione. Il prezzo di acquisto e di vendita di una lotteria (A.2-A.3
  del Mock) non ha appiglio nelle note e non è stato ripreso.
- **U15 compare in 2 appelli su 3.** «Agenti eterogenei (partecipazione limitata) e mercato internazionale» ha come minimo
  calcolato 3 appelli (peso 2 su 6); compare in 02 e 05, con quattro domande. Una terza comparsa avrebbe ripetuto 02 B.3-B.4 o
  05 B.2-B.4, o richiesto una dimostrazione che le note non fanno: il minimo di `blueprint.json` è stato abbassato a 2 e
  `controlla.py` lo segnala come avviso.
- **Scelte di piano da guardare.** 04 A usa l'utilità quadratica (definita in ERA 06, non fra le tre di riferimento di ERA 03);
  05 C usa distribuzioni continue invece di tre valori; Ellsberg compare solo nel 03.
- **Carico.** Il Mock richiede circa 60 minuti di scrittura. Le stime dei revisori e dei solutori ciechi per i simulati vanno da 70 a
  80 minuti (il solutore cieco di 03 ne ha stimati fino a 105 con tutte le derivazioni): sono fattibili in 90 ma senza margine, a
  mano, a libro chiuso. L'appello 01 ha voci più pesanti del Mock in A.3, D.1 ed E.1 (quattro compiti per 5 punti in A.3, una
  derivazione completa per 6 in D.1) e non ha limiti di righe in A.3 e B.1.

## Convenzioni

- **Premio per il rischio.** ERA 03 definisce $R=w-CE$ solo per lotterie a media nulla; con $E[X]\neq 0$ i testi dichiarano la
  definizione usata («ricchezza attesa meno CE», come in ERA 07). $CE$ è un livello di ricchezza, non un guadagno.
- **Stretto e debole.** «Più avverso» e DARA sono deboli ($A_2\ge A_1$, $A'\le 0$): la CARA è DARA solo in senso debole. Dove la
  risposta dipende dalla stretta concavità o dalla stretta preferenza, il testo lo dice («strettamente avverso»).
- **Rendimenti.** ERA 05 usa rendimenti netti ($x=x_0-r$, $w_0=W(1+r)$, $\alpha\in[0,W]$); ERA 06 usa rendimenti lordi.
- **Simboli.** $P$, $R$, $F$, $W$, $p$, $k$, $\alpha$ cambiano senso fra le note: ogni traccia dichiara ciò che usa nei Dati.
- **Azzardo morale.** La normalizzazione $B_0=0$ si impone dopo le condizioni del primo ordine in $B_l$ ($l=0,\dots,L$);
  «Pareto efficiente» dichiara sempre l'insieme di riferimento: «rispetto alle allocazioni fattibili quando l'impegno è
  osservabile» (ERA 08, «Efficienza del benchmark»); in 03, per lo screening, «con informazione perfetta».
- **Calcoli.** Tutti i numeri sono esatti o a forma chiusa, senza calcolatrice; dove serve un logaritmo il testo lo dà
  (05 E.1: $\ln(3/2)\approx 0{,}405$) o accetta la forma chiusa.

## Come è stato controllato

- **Un solutore cieco per appello** (e uno nuovo dopo ogni correzione importante) ha risolto la sola traccia con le note: ogni
  risposta numerica o categorica è stata confrontata con la chiave da `confronta.py`. Sulle risposte confrontabili non restano
  divergenze di sostanza; le segnalazioni residue sono di formato o di tempo.
- **Un revisore per appello** ha rifatto tutti i passaggi aperti e le dimostrazioni contro le note, e ha cercato risposte
  difendibili più di una, domande risolvibili dal testo di altre, aiuti eccessivi nei «Consigli», frasi copiate dal Mock e
  doppioni fra gli appelli. Gli appelli 03 e 04 hanno avuto un secondo passaggio sui soli punti cambiati. Ogni errore vincolante
  trovato è stato corretto nel testo, nelle soluzioni e nella chiave (per esempio: un controesempio non crescente in 05 C.4, la
  FOC in $p$ come opposto della somma in 01 D.1, «Pareto efficiente» senza insieme di riferimento in 01 e 02).
- **Ogni numero esce da uno script.** `calc/appello_NN.py` calcola i numeri della traccia e della soluzione e verifica le forme
  chiuse; le soluzioni copiano l'output. `calc/comune.py` contiene gli helper condivisi (utilità, probabilità, derivate numeriche,
  ottimo del portafoglio). Lo script di 01 (854 righe) ha una copia propria degli helper, con tolleranze diverse; quello di 02
  (1025 righe) importa da `comune.py`; gli altri sono di circa 400-470 righe.
- **`controlla.py scritto economia-rischio-assicurazioni`:** formato, punti, id, assenza di risposte nella traccia, citazioni delle
  note, doppioni, bilanciamento delle lettere e copertura delle unità. Esito: 0 errori e 1 avviso (il minimo di U15).
- **Revisione dello standard di codice.** `calc/comune.py` con `appello_02.py`, `appello_03.py` con `appello_04.py` e
  `appello_05.py` con `appello_06.py` hanno una revisione con esito PASS sul loro stato finale. Gli script 03-06 sono passati per
  più giri di correzione (funzioni che restituiscono le righe e solo `main()` che stampa, costanti con nome, funzioni sotto le 30
  righe, nomi di scopo). Restano rilievi preferenziali, non vincolanti: gli helper per c.d.f. e dominanza sono ripetuti fra gli
  script invece di stare in `comune.py`, non ci sono test automatici e manca un elenco delle dipendenze (numpy, scipy).
  `appello_01.py` non è stato toccato in questo giro e non ha una revisione di questa sessione.

## Limiti noti

- Il solutore cieco di 06 ha segnalato, e non è stato corretto, che alcune risposte aperte («perché lo scarto non è piccolo» in
  A.3) potrebbero avere nella chiave un solo motivo fra più difendibili.
- `confronta.py` non legge le frazioni `p/q` nelle risposte dei solutori (ammesse dalla guida): nelle verifiche i valori frazionari
  sono stati controllati a mano.
- Due citazioni di 01 hanno due note nella stessa parentesi, che `controlla.py` non verifica: sono state controllate a mano. Nei
  nuovi appelli ogni parentesi cita una sola nota.
- Nessun test automatico per gli script: la verifica è nei `check` che girano a ogni esecuzione.

## Comandi

```bash
python3 latex/build_esami.py --corso economia-rischio-assicurazioni --all          # tutti i PDF
python3 latex/build_esami.py --corso economia-rischio-assicurazioni --exam Simulato_03   # un appello (traccia e soluzioni)
python3 latex/build_esami.py --corso economia-rischio-assicurazioni --volume       # i due volumi «Completo»
python3 .claude/skills/genera-esami/scripts/controlla.py scritto economia-rischio-assicurazioni
python3 latex/esami/economia-rischio-assicurazioni/calc/appello_03.py              # i numeri dell'appello 03
```

Sorgenti: `src/ERA_Esame_Simulato_NN.md` e `src/ERA_Soluzioni_Simulato_NN.md`; piano e chiave: `piano/appello-NN.json` e
`piano/blueprint.json`. Formato: `.claude/skills/genera-esami/references/formato-scritto.md`.
