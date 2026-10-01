---
title: "Introduzione alla revisione di portafoglio"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-10-Introduzione-alla-revisione-di-portafoglio-lucidi.pdf"
pages: 47
text_layer: true
verified: true
generated: 2026-07-10
---

## Dati del corso

**Parte 5 — Metodi per la Gestione dei Portafogli Personali**

Marco Corazza — Department of Economics, University Ca' Foscari of Venice.

*(slide 1)*

## Tra gestione statica e gestione dinamica: la revisione di portafoglio

> «Un limite del modello di Markowitz [...] è che esso indica come selezionare un portafoglio solo in un singolo istante temporale.»
> — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 427)

In un'economia ideale mono-periodale (da $t$ a $t+\Delta t$), l'agente economico seleziona il proprio portafoglio ottimo in $t$ e lo "rilascia" (cioè lo liquida) in $t+\Delta t$.

Nella realtà, però, l'agente economico opera in un'economia (almeno) multi-periodale (da $t$ a $t+\Delta t$, da $t+\Delta t$ a $t+2\Delta t$, ..., da $t+i\Delta t$ a $t+(i+1)\Delta t$, ...). Pertanto:

- seleziona il proprio portafoglio ottimo in $t$;
- non può più "rilasciarlo" in $t+\Delta t$;
- deve gestirlo in $t+\Delta t$, $t+2\Delta t$, ..., $t+i\Delta t$, ....

**Domanda.** In un'economia multi-periodale, in cosa consiste la gestione del portafoglio in $t+\Delta t$, $t+2\Delta t$, ..., $t+i\Delta t$, ...?

**Risposta.** In un'economia multi-periodale ideale, le medie, le varianze e i coefficienti di correlazione lineare relativi alle diverse scelte di investimento restano sempre gli stessi in qualunque istante temporale considerato. Di conseguenza, il portafoglio ottimo selezionato in $t$ dall'agente economico è ottimo anche in $t+\Delta t$, in $t+2\Delta t$, ..., in $t+i\Delta t$, ....

**Risposta (continua).** Ma, in generale, nella realtà queste medie, varianze e coefficienti di correlazione lineare cambiano al variare dell'istante temporale considerato. Perciò, il portafoglio ottimo selezionato in $t$ potrebbe non essere più né ottimo né efficiente in $t+\Delta t$, e/o in $t+2\Delta t$, ..., e/o in $t+i\Delta t$, .... Questo limite viene illustrato dall'esempio che segue.

*(slide 2–5)*

## Esempio: instabilità temporale del portafoglio ottimo

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai seguenti titoli azionari del mercato borsistico italiano:
>
> - $X_1$ = Alleanza Assicurazioni;
> - $X_2$ = Fondiaria–Sai;
> - $X_3$ = Unicredito Italiano.
>
> Le medie, le varianze e i coefficienti di correlazione lineare relativi ai tassi di rendimento di $X_1$, $X_2$ e $X_3$, valutati:
>
> - su dati giornalieri dal 22 agosto 2006 al 20 settembre 2006 (colonna A),
> - e su dati giornalieri dal 23 agosto 2006 al 21 settembre 2006 (colonna B, finestra traslata di un giorno),
>
> sono rispettivamente:
>
> | Parametri | A | B |
> |---|---|---|
> | $r_1$ | 4.437E−04 | 4.037E−04 |
> | $r_2$ | 6.648E−04 | 9.901E−04 |
> | $r_3$ | 1.144E−03 | 1.213E−03 |
> | $\sigma_1^2$ | 1.231E−04 | 1.229E−04 |
> | $\sigma_2^2$ | 1.168E−04 | 1.514E−04 |
> | $\sigma_3^2$ | 7.802E−05 | 7.794E−05 |
> | $\rho_{1,2}$ | 1.591E−01 | 1.600E−01 |
> | $\rho_{1,3}$ | −7.665E−02 | −8.291E−02 |
> | $\rho_{2,3}$ | 4.074E−01 | 4.150E−01 |
>
> Imponendo $\pi = 0.00041$ nel problema base di portafoglio (di tipo Markowitz), le percentuali ottimali di investimento risultanti sono:
>
> | Percentuali | A | B |
> |---|---|---|
> | $x_1^*$ | 0.69193 | 0.96600 |
> | $x_2^*$ | 0.52029 | 0.09500 |
> | $x_3^*$ | −0.21223 | −0.06100 |
>
> **Figura** — Frontiera efficiente (contrassegnata con "+") e frontiera inefficiente (contrassegnata con "×") nel piano $\mathrm{Var}(X)$–$E(X)$, calcolate sui dati della colonna A. La frontiera efficiente è il ramo superiore dell'iperbole media-varianza; il grafico mostra come, fissato un livello di varianza, esistano combinazioni di portafoglio con rendimento atteso più basso (frontiera inefficiente) rispetto a quelle ottimali (frontiera efficiente).
>
> Se l'agente economico desidera che il portafoglio selezionato realizzi un tasso di rendimento atteso pari a $0.00041$ sia da $t$ (= 20 settembre 2006) a $t+\Delta t$ (= 21 settembre 2006), sia da $t+\Delta t$ a $t+2\Delta t$ (= 22 settembre 2006), allora in $t+\Delta t$ l'agente economico deve:
>
> - **comprare** $X_1$ (Alleanza Assicurazioni) per una percentuale del proprio capitale pari a $0.27407$ ($= 0.96600 - 0.69193$);
> - **vendere** $X_2$ (Fondiaria–Sai) per una percentuale del proprio capitale pari a $0.42529$ ($= 0.09500 - 0.52029$);
> - **comprare** $X_3$ (Unicredito Italiano) per una percentuale del proprio capitale pari a $0.15123$ ($= -0.06100 - (-0.21223)$).
>
> Questo esempio mostra concretamente come, cambiando anche di un solo giorno la finestra di stima dei parametri statistici, il portafoglio ottimo cambi in modo significativo, imponendo una revisione della composizione del portafoglio.

*(slide 6–11)*

## La revisione di portafoglio e la sua convenienza

**Osservazioni**

- L'insieme di questi aggiustamenti di portafoglio in $t+\Delta t$ è chiamato **revisione di portafoglio** (in un mercato privo di frizioni).
- Nella realtà questi aggiustamenti di portafoglio hanno un costo. In particolare, i costi di revisione a volte potrebbero essere maggiori dell'incremento del tasso di rendimento atteso del portafoglio rivisto. Perciò, la revisione di portafoglio non è sempre conveniente.

**Domanda.** Come effettuare una revisione di portafoglio (conveniente)?

**Risposta.**

1. Prima, identificare le principali tipologie di costi di revisione;
2. secondo, individuare il potenziale portafoglio rivisto;
3. terzo, verificare se la revisione di portafoglio è conveniente.

*(slide 12–13)*

## Le principali tipologie di costi di revisione

> [!abstract] Definizione
> Le principali tipologie di costi di revisione che l'agente economico deve eventualmente sostenere negli istanti temporali $t+\Delta t$, $t+2\Delta t$, ..., $t+i\Delta t$, ... sono le seguenti.
>
> **1. Costi per la raccolta ed elaborazione dei dati.** I costi per raccogliere i nuovi dati, per aggiornare il relativo data set, per trasformare opportunamente questi nuovi dati (ad esempio da prezzi a rendimenti percentuali/logaritmici), e per calcolare le grandezze di interesse (ad esempio medie, varianze, coefficienti di correlazione lineare, ...).
>
> *Osservazione.* Questa tipologia di costo è **fissa**. Pertanto, l'agente economico deve sostenerla in ogni istante temporale, sia che riveda il proprio portafoglio, sia che non lo riveda.
>
> **2. Costi di transazione.** I costi per negoziare le scelte di investimento considerate, cioè i costi da pagare a un intermediario professionale (ad esempio banca, broker, ...) per comprare e/o (short-)vendere le scelte di investimento.
>
> *Osservazione.* Questa tipologia di costo è **variabile**. Pertanto, l'agente economico deve sostenerla soltanto negli istanti temporali in cui rivede il proprio portafoglio.
>
> **3. Imposte sul capital gain.** Le imposizioni fiscali sul capital gain, cioè le tasse da pagare sull'eventuale incremento realizzato del valore, espresso in termini di numerario, del portafoglio. Tecnicamente, le imposizioni fiscali sul capital gain non sono costi, ma in questo contesto possono essere considerate come aventi lo stesso status di un costo. Questo status viene illustrato nella sezione seguente.

*(slide 14–17)*

## Formalizzazione e condizione di convenienza della revisione in presenza di imposta sul capital gain

> [!note] Dimostrazione
> **Notazione.** Si considerino:
>
> - $\mathbf{z}^*_\tau = (z^*_{\tau,1}, z^*_{\tau,2})$: un semplice portafoglio a due attività, espresso in termini di scelte di investimento, selezionato/rivisto in $\tau$ dall'agente economico (il pedice relativo all'istante temporale rende univoca la notazione);
> - $P_{\tau,i}$: il prezzo in $\tau$ della $i$-esima scelta di investimento;
> - $r_{\tau,i}$: il tasso di rendimento atteso in $\tau$ della $i$-esima scelta di investimento;
> - $\Delta_{\tau,i}$: il numero di titoli comprati o (short-)venduti in $\tau$ della $i$-esima scelta di investimento;
> - $t_{cg} \in [0,1)$: la percentuale del capital gain realizzato da pagare come imposta.
>
> **L'agire dell'agente economico.** In $t$ l'agente economico seleziona il proprio portafoglio ottimo, $\mathbf{z}^*_t$. In $t+\Delta t$ può mettere in pratica una delle due strategie seguenti.
>
> **Strategia 1 — Nessuna revisione.** Non effettuare alcuna revisione di portafoglio, da cui $\mathbf{z}^*_{t+\Delta t} = \mathbf{z}^*_t$. Il rendimento atteso, espresso in termini di numerario, del portafoglio non rivisto è:
>
> $$r_{NR,\,t+\Delta t} = z^*_{t,1}\,P_{t+\Delta t,1}\,r_{t+\Delta t,1} + z^*_{t,2}\,P_{t+\Delta t,2}\,r_{t+\Delta t,2}.$$
>
> **Strategia 2 — Revisione.** Effettuare una revisione di portafoglio che consiste:
>
> - nel disinvestire dalla prima scelta di investimento l'importo, in termini di numerario, $\Delta_{t+\Delta t,1}\,P_{t+\Delta t,1}$;
> - nel pagare l'imposta sull'eventuale capital gain realizzato, cioè nel pagare $t_{cg} \max\{\Delta_{t+\Delta t,1}(P_{t+\Delta t,1} - P_{t,1}), 0\}$;
> - e nell'investire l'importo di numerario rimanente, cioè $\Delta_{t+\Delta t,1}\,P_{t+\Delta t,1} - t_{cg}\max\{\Delta_{t+\Delta t,1}(P_{t+\Delta t,1} - P_{t,1}), 0\}$, nella seconda scelta di investimento.
>
> Il rendimento atteso, espresso in termini di numerario, del portafoglio rivisto è quindi:
>
> $$r_{R,\,t+\Delta t} = \left(z^*_{t,1} - \Delta_{t+\Delta t,1}\right) P_{t+\Delta t,1}\, r_{t+\Delta t,1} + \Big(z^*_{t,2}\,P_{t+\Delta t,2} + \Delta_{t+\Delta t,1}\,P_{t+\Delta t,1} - t_{cg}\max\{\Delta_{t+\Delta t,1}(P_{t+\Delta t,1}-P_{t,1}),0\}\Big)\, r_{t+\Delta t,2}.$$
>
> **Derivazione della condizione di convenienza.** La revisione di portafoglio è conveniente se il rendimento atteso del portafoglio rivisto è maggiore del rendimento atteso di quello non rivisto, cioè se
>
> $$r_{R,t+\Delta t} > r_{NR,t+\Delta t},$$
>
> ossia, dopo alcuni passaggi,
>
> $$\Delta_{t+\Delta t,1}\,P_{t+\Delta t,1}\,(r_{t+\Delta t,2} - r_{t+\Delta t,1}) > t_{cg}\max\{\Delta_{t+\Delta t,1}(P_{t+\Delta t,1}-P_{t,1}),0\}\, r_{t+\Delta t,2} \ge 0,$$
>
> ossia, dopo altri passaggi,
>
> $$r_{t+\Delta t,2} > r_{t+\Delta t,1} + \frac{t_{cg}\max\{\Delta_{t+\Delta t,1}(P_{t+\Delta t,1}-P_{t,1}),0\}}{\Delta_{t+\Delta t,1}\,P_{t+\Delta t,1}}.$$
>
> **Osservazione.** Questa tipologia di "costo" dipende dal verificarsi di un capital gain realizzato. Quando questo capital gain realizzato si verifica, la tipologia di "costo" considerata è **variabile**. Pertanto, l'agente economico non deve sostenerla in tutti gli istanti temporali in cui rivede il proprio portafoglio (solo quando si realizza un guadagno in conto capitale sulla posizione liquidata).

*(slide 18–24)*

## Individuazione del portafoglio potenzialmente rivisto: il modello di Smith (1967)

> [!abstract] Definizione
> Per individuare in $t+\Delta t$ il potenziale portafoglio rivisto non esistono molti approcci. Di seguito vengono presentati sinteticamente alcuni di quelli classici.
>
> **Il modello di Smith (1967)**
>
> > «Lo scopo di questo lavoro è estendere una metodologia esistente per la selezione di portafoglio su base intertemporale. La tecnica proposta è un meccanismo di tipo adattivo che viene eseguito a intervalli finiti.»
> > — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 425)
>
> In questo lavoro l'Autore propone una strategia di revisione di portafoglio così articolata:
>
> - in $t$ l'agente economico seleziona il proprio portafoglio ottimo espresso in termini di scelte di investimento, cioè $\mathbf{z}^*_t$;
> - in $t+\Delta t$ si verifica una delle seguenti situazioni:
>  1. $\mathbf{z}^*_t$ è ancora il portafoglio ottimo per l'agente economico. Quindi non è necessaria alcuna revisione e $\mathbf{z}^*_{t+\Delta t} = \mathbf{z}^*_t$.
>  2. $\mathbf{z}^*_t$ non è più il portafoglio ottimo per l'agente economico, ma è di nuovo efficiente. La revisione di portafoglio potrebbe essere effettuata.
>  3. $\mathbf{z}^*_t$ non è più né ottimo né efficiente per l'agente economico. La revisione di portafoglio potrebbe essere effettuata.
>
> **Caso 2).** Rispetto al caso 2), $\mathbf{z}^*_t$
>
> > «si trova sulla nuova curva efficiente, quindi la transizione verso qualsiasi altro portafoglio efficiente comporterebbe un trade-off tra rendimento e rischio. A causa della difficoltà nello specificare le curve di indifferenza, si postula che se $[\mathbf{z}^*_t]$ è efficiente, l'investitore sarà soddisfatto di mantenerlo.»
> > — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 429)
>
> Quindi, in questo caso, non viene effettuata alcuna revisione di portafoglio e $\mathbf{z}^*_{t+\Delta t} = \mathbf{z}^*_t$.
>
> **Caso 3): analisi grafica.** Rispetto al caso 3), $\mathbf{z}^*_t$ potrebbe essere rivisto secondo una delle modalità rappresentate nella figura seguente.
>
> **Figura** — Diagramma nel piano $\mathrm{Var}(X)$–$E(X)$: la curva rappresenta la (nuova) frontiera efficiente; il punto $\mathbf{z}^*_t$ (il portafoglio ottimo precedente, ora non più efficiente) è indicato in basso a destra rispetto alla curva; sulla frontiera sono evidenziati tre punti candidati per la revisione — $A$ (alla stessa quota $r_t$ del rendimento atteso originario), $B$ (punto di tangenza), $C$ (alla stessa ascissa, cioè stessa varianza, di $\mathbf{z}^*_t$, a quota $r_{t+\Delta t}$); frecce collegano $\mathbf{z}^*_t$ ad $A$, $B$ e $C$. La figura illustra graficamente le tre alternative di transizione discusse nel seguito.
>
> Con riferimento al **punto A**:
>
> - $\mathbf{z}^*_{t+\Delta t}$ è efficiente, ha lo stesso rendimento atteso (e una varianza del rendimento inferiore) di $\mathbf{z}^*_t$, ma non è necessariamente ottimo per l'agente economico.
>
> > «poiché le transizioni verranno valutate in termini di [numerario] atteso e di costi, è difficile misurare un rendimento in [numerario] comparabile a fronte della riduzione del rischio di portafoglio ottenuta spostandosi verso il punto $[A]$.»
> > — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 429)
>
> Quindi, in questo sotto-caso, non viene effettuata alcuna revisione di portafoglio e $\mathbf{z}^*_{t+\Delta t} = \mathbf{z}^*_t$.
>
> Con riferimento al **punto B**:
>
> - $\mathbf{z}^*_{t+\Delta t}$ è ottimo per l'agente economico.
>
> > «se l'investitore potesse specificare la propria funzione di preferenza, la soluzione di tangenza nel punto $[B]$ sarebbe un logico obiettivo per una transizione. Ma poiché si evita di specificare tale funzione di preferenza, il portafoglio nel punto $[B]$ non viene considerato.»
> > — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 429)
>
> Quindi, in questo sotto-caso, non viene effettuata alcuna revisione di portafoglio e $\mathbf{z}^*_{t+\Delta t} = \mathbf{z}^*_t$.
>
> Con riferimento al **punto C**:
>
> - $\mathbf{z}^*_{t+\Delta t}$ è efficiente, ha la stessa varianza del rendimento (e un rendimento atteso maggiore) di $\mathbf{z}^*_t$, ma non è necessariamente ottimo per l'agente economico.
>
> > «in questa situazione, l'investitore accetta il rischio insito nel portafoglio esistente (secondo le aspettative riviste) e cerca di ottenere il massimo miglioramento nel rendimento atteso. Operativamente ciò è fattibile poiché il rendimento è misurato in [numerario ...]. Il portafoglio nel punto $[C ...]$ è il portafoglio obiettivo, o desiderato, alla luce delle aspettative riviste.»
> > — Smith K.V., *A transition model for portfolio revision*, The Journal of Finance, 1967 (pagina 429)
>
> Quindi, in questo sotto-caso, la revisione di portafoglio è effettuabile.
>
> **Condizione di convenienza.** Naturalmente, prima di effettuare la revisione di portafoglio considerata, l'Autore verifica se essa è conveniente, cioè verifica se l'incremento del rendimento atteso del portafoglio rivisto è maggiore dei relativi costi di revisione, cioè verifica se
>
> $$\sum_{i=1}^{N} \left(z^*_{t+\Delta t,i} - z^*_{t,i}\right) P_{t+\Delta t,i}\, r_{t+\Delta t,i} > prc_{t+\Delta t}.$$

*(slide 25–35)*

## Individuazione del portafoglio potenzialmente rivisto: il modello di Stone e Hill (1979)

> [!abstract] Definizione
> **Il modello di Stone e Hill (1979)**
>
> > «La procedura di revisione [considerata] è una generalizzazione del classico algoritmo dello zaino (knapsack) lineare, che ne conserva la maggior parte delle caratteristiche, ossia una grande efficienza computazionale e la capacità di gestire problemi di grandi dimensioni.»
> > — Stone B.K. e Hill N.C., *Portfolio management and the shrinking knapsack problem*, Journal of Financial and Quantitative Analysis, 1979 (pagina 1071)
>
> In questo lavoro:
>
> - innanzitutto, gli Autori formulano un problema di selezione di portafoglio lineare (che approssima i classici problemi quadratico-lineari) da utilizzare in $t$;
> - poi, gli Autori formulano un problema di revisione di portafoglio lineare da utilizzare in $t+\Delta t$, $t+2\Delta t$, ..., $t+i\Delta t$, ...;
> - infine, gli Autori forniscono una procedura risolutiva per il problema di portafoglio rivisto e ne discutono l'efficienza computazionale.
>
> **Un po' di formalizzazione.** Si considerino:
>
> - $\mathbf{c}' = (r_1 - \beta_1\theta, \ldots, r_N - \beta_N\theta)$: l'$N$-vettore dei tassi di rendimento corretti per il rischio, dove $\beta_i$ è il cosiddetto "rischio sistematico" della $i$-esima scelta di investimento, e $\theta$ è una costante che pesa opportunamente il rischio sistematico;
> - $f_i \in [0,1]$: un limite superiore associato a $x_i$.
>
> Il problema di selezione di portafoglio lineare considerato è quindi:
>
> $$\max_{x_1,\ldots,x_N} \ \mathbf{x}'\mathbf{c} \qquad \text{s.t.} \quad \begin{cases} \mathbf{x}'\mathbf{e} = 1 \\ 0 \le x_i \le f_i, \quad i=1,\ldots,N \end{cases}$$
>
> **Ulteriore formalizzazione.** Si considerino inoltre:
>
> - $\mathbf{b}' = \mathbf{c}' - (bc_1,\ldots,bc_N)$: l'$N$-vettore dei tassi di rendimento netti corretti per il rischio "guadagnati" acquistando le scelte di investimento, dove $bc_i$ è il costo da sostenere per comprare 1 unità di numerario della $i$-esima scelta di investimento;
> - $\mathbf{s}' = \mathbf{c}' + (sc_1,\ldots,sc_N)$: l'$N$-vettore dei tassi di rendimento netti corretti per il rischio "persi" vendendo le scelte di investimento, dove $sc_i$ è il costo da sostenere per vendere 1 unità di numerario della $i$-esima scelta di investimento;
> - $\mathbf{q}' = (q_1,\ldots,q_N)$: l'$N$-vettore degli importi in numerario investiti nelle scelte di investimento prima che la revisione di portafoglio venga effettuata;
> - $\mathbf{z_b}' = (z_{b,1},\ldots,z_{b,N})$: l'$N$-vettore (incognito) degli importi in numerario da investire in ciascuna scelta di investimento;
> - $\mathbf{z_s}' = (z_{s,1},\ldots,z_{s,N})$: l'$N$-vettore (incognito) degli importi in numerario da disinvestire da ciascuna scelta di investimento.
>
> Il problema di revisione di portafoglio lineare considerato è quindi:
>
> $$\max_{z_{b,1},\ldots,z_{b,N},\,z_{s,1},\ldots,z_{s,N}} \ \mathbf{b}'\mathbf{z_b} - \mathbf{s}'\mathbf{z_s}$$
>
> $$\text{s.t.} \quad \begin{cases} \mathbf{z_b}'[\mathbf{e} + (bc_1,\ldots,bc_N)] - \mathbf{z_s}'[\mathbf{e} - (bs_1,\ldots,bs_N)] = 0 \\ z_{b,i} \ge 0, \quad i=1,\ldots,N \\ z_{b,i} \le f_i\,\mathbf{q}'\mathbf{e} - q_i, \quad i=1,\ldots,N \\ z_{s,i} \ge 0, \quad i=1,\ldots,N \\ z_{s,i} \le q_i, \quad i=1,\ldots,N \end{cases}$$
>
> **Osservazioni.**
>
> - Il primo vincolo garantisce che l'importo in numerario da investire (più i relativi costi di transazione) sia uguale all'importo in numerario da disinvestire (meno i relativi costi di transazione).
> - Il vincolo $z_{b,i} \le f_i\,\mathbf{q}'\mathbf{e} - q_i$ garantisce che la percentuale del valore del portafoglio prima della revisione ($= \mathbf{q}'\mathbf{e}$) da investire nella $i$-esima scelta di investimento sia inferiore o uguale a $f_i$.
> - Il valore della funzione obiettivo (da massimizzare) aumenta comprando quella generica $i$-esima scelta di investimento e vendendo quella generica $j$-esima scelta di investimento tali che
>
> $$c_i - bc_i > c_j + sc_j, \qquad i,j \in \{1,\ldots,N\} \wedge i \ne j,$$
>
> cioè tale valore aumenta se
>
> $$c_i - c_j > bc_i + sc_j, \qquad i,j \in \{1,\ldots,N\} \wedge i \ne j.$$
>
> > «Pertanto, per l'intero programma di scambio, la funzione obiettivo equivale a massimizzare l'incremento del [tasso di rendimento corretto per il rischio] degli acquisti rispetto alle vendite, al netto dei costi di transazione totali. ... L'espressione della funzione obiettivo [...] suggerisce un approccio risolutivo, ossia classificare i candidati all'acquisto sulla base di $[c_i - bc_i]$ e classificare le posizioni correnti di portafoglio sulla base di $[c_j + sc_j]$. Comprare il candidato all'acquisto con il rango più alto e vendere la posizione di portafoglio con il rango più basso produce il massimo miglioramento della funzione obiettivo. È sufficiente determinare l'importo dello scambio in modo che nessun vincolo venga violato.»
> > — Stone B.K. e Hill N.C., *Portfolio management and the shrinking knapsack problem*, Journal of Financial and Quantitative Analysis, 1979 (pagine 1074)

*(slide 36–46)*

## Caratteristiche di un "buon" modello di revisione di portafoglio

**Domanda.** Quali caratteristiche deve avere un "buon" modello di revisione di portafoglio?

**Risposta.** Deve possedere:

- **realismo**;
- **complessità (computazionale) ridotta**;
- **efficacia**.

*(slide 47)*
