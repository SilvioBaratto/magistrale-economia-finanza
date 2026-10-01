---
title: "Estensioni del modello classico di selezione di portafoglio"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-7-Estensioni-del-modello-classico.pdf"
pages: 33
text_layer: true
verified: true
generated: 2026-07-10
---

## Alcuni limiti del modello classico di selezione di portafoglio

Il modello classico di Markowitz presenta alcuni limiti che motivano le estensioni trattate nel seguito:

- **Distribuzione del rendimento del portafoglio**: in generale i rendimenti non seguono una distribuzione normale multivariata, ma una distribuzione asimmetrica a destra.
- **Diversificazione**: l'aumento del numero dei titoli riduce il rischio complessivo, ma l'effetto tende a decrescere al crescere del numero di titoli inclusi nel portafoglio.
- **Utilizzo della varianza come misura di rischio**: la varianza è un indice di variabilità e, per questo, è sensibile agli outliers. Inoltre può essere adottata come misura di rischio solo se la distribuzione dei rendimenti è simmetrica.
- **Limiti operativi**: le assunzioni di base del modello classico sono poco realistiche.

*(slide 1)*

## Misure alternative di rischio: la semi-varianza

> [!abstract] Definizione
> **Elementi di riflessione.** La semi-varianza è una misura del cosiddetto *downside risk*, cioè del rischio in corrispondenza di rendimenti inferiori a un prefissato benchmark, solitamente lo zero o il valor medio.
>
> Agli investitori che non praticano lo *short-selling* interessa minimizzare il rischio che i rendimenti di portafoglio siano sotto la media, in quanto i rendimenti che stanno sopra la media sono desiderabili. La semi-varianza è quindi un'appropriata misura di rischio quando gli investitori percepiscono il rischio come una possibilità di risultati avversi, piuttosto che come una dispersione del rendimento.
>
> **Definizione.** La semi-varianza del rendimento aleatorio di un'attività, $r$, è definita come:
>
> $$Semi\text{-}Var(r) = \sum_{t=1;\,r_t<\bar r}^{T} \left(r_t-\bar r\right)^2 \Big/ T .$$
>
> - La semi-varianza è equivalente alla varianza quando i rendimenti seguono una distribuzione simmetrica.
> - Questa misura **non** è agevolmente trattabile da un punto di vista analitico.

*(slide 2–3)*

## Misure alternative di rischio: la mean absolute deviation (MAD)

> [!abstract] Definizione
> La *mean absolute-deviation* del rendimento aleatorio di un'attività, $r$, è definita come:
>
> $$MAD(r) = \sum_{t=1}^{T} \left| r_t - \bar r \right| \Big/ T .$$
>
> - Si tratta di una misura sensibile agli outliers, anche se meno della varianza.
> - Anch'essa non è facile da trattare analiticamente, per la presenza dell'operatore valore assoluto.

*(slide 4)*

## L'asimmetria (skewness) dei rendimenti

L'asimmetria è il primo dei momenti successivi alla varianza (il momento terzo) e può contenere informazioni utili per la formulazione delle decisioni di investimento.

Per gli investitori è preferibile un'**asimmetria positiva**: essa indica che la distribuzione ha la coda destra più "grassa" (*fat*), cioè che il maggior numero di osservazioni è concentrato alla destra della media. Ciò significa che il rendimento di un titolo assume, con probabilità maggiore, valori superiori alla media.

Queste considerazioni (semi-varianza, MAD, asimmetria) motivano l'introduzione, nelle sezioni seguenti, di modelli di selezione di portafoglio basati su **vincoli misti interi**.

*(slide 5)*

## Modello di Markowitz con vincolo di cardinalità

> [!abstract] Definizione
> Una prima estensione del modello classico introduce un **vincolo di cardinalità**, che limita il numero di titoli effettivamente detenuti in portafoglio:
>
> $$\min_{x_1,\dots,x_N;\;z_1,\dots,z_N} \; Var(r)$$
> $$\text{s.t.} \quad \sum_{i=1}^{N} x_i z_i = \pi$$
> $$\sum_{i=1}^{N} x_i z_i = 1$$
> $$\sum_{i=1}^{N} z_i = K$$
> $$z_i \in \{0,1\}$$
>
> in cui:
>
> - $z_i = 0$ indica che l'$i$-esimo titolo **non** è stato selezionato, mentre $z_i = 1$ indica che l'$i$-esimo titolo **è stato** selezionato;
> - $K$ indica il numero di titoli selezionabili.
>
> Lo scopo dell'introduzione del vincolo di cardinalità è che esso permette un controllo, seppure indiretto, dei costi di transazione.
>
> Questo tipo di vincolo porta alla cosiddetta **cardinality constrained efficient frontier**, che in generale è discontinua.
>
> **Figura (pag. 8)** — Grafico Return (asse verticale) contro Risk-variance (asse orizzontale): a differenza della frontiera efficiente classica (continua), la cardinality constrained efficient frontier è composta da più archi separati e discontinui tra loro. Ciò mostra che imporre un numero fisso $K$ di titoli selezionabili spezza la frontiera efficiente in segmenti non collegati, invece di lasciarla come curva continua.

*(slide 6–8)*

## Modello Mean-Variance con vincoli misti-interi

> [!abstract] Definizione
> $$\min \; \lambda\left[\sum_{i=1}^{N}\sum_{j=1}^{N} x_i x_j \sigma_{ij}\right] - (1-\lambda)\left[\sum_{i=1}^{N} x_i \mu_i\right]$$
> $$x_1,\dots,x_N;\;z_1,\dots,z_N$$
> $$st. \quad \sum_{i=1}^{N} x_i = 1$$
> $$\sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le x_i \le \delta_i z_i \qquad i=1,\dots,N;$$
> $$z_i \in \{0,1\} \qquad i=1,\dots,N;$$
>
> in cui:
>
> - $\lambda \in [0,1]$;
> - $\varepsilon_i$ indica la percentuale minima del titolo $i$-esimo che può essere selezionata;
> - $\delta_i$ indica la percentuale massima del titolo $i$-esimo che può essere selezionata.
>
> Il caso $\lambda = 0$ corrisponde alla massimizzazione del rendimento atteso, mentre $\lambda = 1$ corrisponde alla minimizzazione del rischio. Un valore di $\lambda$ intermedio corrisponde a un trade-off tra rischio e rendimento.

*(slide 9–10)*

## Modello Semi-Variance con vincoli misti-interi

> [!abstract] Definizione
> $$\min \; \lambda\left[\sum_{t=1;\,r_t<\bar r}^{T} \left(r_t-\bar r\right)^2 \big/ T\right] - (1-\lambda)\bar r$$
> $$x_1,\dots,x_N;\;z_1,\dots,z_N$$
> $$st. \quad \sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le w_i \le \delta_i z_i \qquad i=1,\dots,N;$$
> $$\sum_{i=1}^{N} w_i = 1$$
> $$r_t = \log_e\!\left[\left(\sum_{i=1}^{N} w_i v_{it}/v_{iT}\right)\Big/\left(\sum_{i=1}^{N} w_i v_{i,t-1}/v_{iT}\right)\right] \qquad t=1,\dots,T;$$
> $$w_i \ge 0 \qquad i=1,\dots,N;$$
> $$z_i \in \{0,1\} \qquad i=1,\dots,N;$$
> $$\bar r = \frac{\sum_{t=1}^{T} r_t}{T}.$$

*(slide 11)*

## Approfondimento sul modello mean semi-variance: definizioni, variabili e formulazione equivalente

> [!abstract] Definizione
> **Definizioni preliminari**
>
> - $N$: numero totale di attività (titoli) distinte in cui è possibile investire;
> - $\lambda \in [0,1]$: parametro di avversione al rischio;
> - $K$: numero desiderato di attività distinte nel portafoglio;
> - $\varepsilon_i$: proporzione minima del portafoglio che deve essere detenuta nell'attività $i$ ($i=1,\dots,N$), se l'attività $i$ è detenuta;
> - $\delta_i$: proporzione massima del portafoglio che può essere detenuta nell'attività $i$ ($i=1,\dots,N$), se l'attività $i$ è detenuta;
> - $T$: orizzonte temporale per cui sono osservati i valori storici delle attività, con periodi $0,1,2,\dots,T$;
> - $v_{it}$: valore di un'unità dell'attività $i$ ($i=1,\dots,N$) al tempo $t$ ($t=0,\dots,T$);
> - $C_{cash}$: liquidità disponibile da investire nel portafoglio.
>
> **Variabili decisionali**
>
> - $x_i$: numero di unità dell'attività $i$ ($i=1,\dots,N$) che si sceglie di detenere in portafoglio;
> - $z_i = 1$ se una qualsiasi unità dell'attività $i$ ($i=1,\dots,N$) è detenuta in portafoglio, $0$ altrimenti.
>
> **Quantità utili**
>
> 1) $w_i$: proporzione di $C_{cash}$ investita al tempo $T$ nell'attività $i$ ($i=1,\dots,N$); $r_t$: rendimento a tempo continuo su un singolo periodo del portafoglio al tempo $t$ ($t=1,\dots,T$).
>
> 2) $$w_i = v_{iT} x_i / C_{cash}, \quad i=1,\dots,N$$
> $$r_t = \log_e\left\{\left(\sum_{i=1}^{N} v_{it} x_i\right)\Big/\left(\sum_{i=1}^{N} v_{i,t-1} x_i\right)\right\}, \qquad t=1,\dots,T$$
>
> **Problema di selezione (formulazione in $x_i$)**
>
> $$\text{Minimize} \;\; \lambda\left[\sum_{t=1;\,r_t<\bar r}^{T} \left(r_t-\bar r\right)^2/T\right] - (1-\lambda)\bar r$$
> $$\text{s.t.} \quad \sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le v_{iT} x_i / C_{cash} \le \delta_i z_i, \qquad i=1,\dots,N$$
> $$\sum_{i=1}^{N} v_{iT} x_i = C_{cash}$$
> $$x_i \ge 0, \qquad i=1,\dots,N$$
> $$z_i \in \{0,1\}, \qquad i=1,\dots,N$$
>
> **Sistema di vincoli equivalente (formulazione in $w_i$)**
>
> Il precedente sistema di vincoli è equivalente a:
>
> $$\sum_{i=1}^{N} w_i = 1$$
> $$0 \le w_i \le 1, \qquad i=1,\dots,N$$
> $$\sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le w_i \le \delta_i z_i, \qquad i=1,\dots,N$$
> $$r_t = \log_e\left\{\left(\sum_{i=1}^{N} w_i v_{it}/v_{iT}\right)\Big/\left(\sum_{i=1}^{N} w_i v_{i,t-1}/v_{iT}\right)\right\}, \qquad t=1,\dots,T$$
> $$z_i \in \{0,1\}, \qquad i=1,\dots,N$$
>
> Questa riformulazione mostra come sia possibile passare dalle quantità fisiche detenute ($x_i$, espresse in numero di unità) alle proporzioni di ricchezza investita ($w_i$), preservando esattamente lo stesso insieme ammissibile: è la formulazione in $w_i$ ad essere poi utilizzata nei modelli Mean-Variance, Semi-Variance, MAD e Mean-Variance-Skewness con vincoli misti-interi presentati in questo lucido.

*(slide 12–15)*

## Modello Mean Absolute Deviation con vincoli misti-interi

> [!abstract] Definizione
> $$\min \; \lambda\left[\sum_{t=1}^{T} \left|r_t-\bar r\right| \big/ T\right] - (1-\lambda)\bar r$$
> $$x_1,\dots,x_N;\;z_1,\dots,z_N$$
> $$st. \quad \sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le w_i \le \delta_i z_i \qquad i=1,\dots,N;$$
> $$\sum_{i=1}^{N} w_i = 1$$
> $$r_t = \log_e\!\left[\left(\sum_{i=1}^{N} w_i v_{it}/v_{iT}\right)\Big/\left(\sum_{i=1}^{N} w_i v_{i,t-1}/v_{iT}\right)\right] \qquad t=1,\dots,T;$$
> $$w_i \ge 0 \qquad i=1,\dots,N;$$
> $$z_i \in \{0,1\} \qquad i=1,\dots,N;$$
> $$\bar r = \frac{\sum_{t=1}^{T} r_t}{T}.$$
>
> La deviazione media assoluta e la varianza sono misure di variabilità abbastanza "simili". Differiscono sostanzialmente nel fatto che:
>
> - il problema di programmazione matematica associato alla deviazione media assoluta è **lineare**;
> - il problema di programmazione matematica associato alla varianza è **quadratico**.

*(slide 16–17)*

## Modello Mean-Variance with Skewness con vincoli misti-interi

> [!abstract] Definizione
> $$\min \; \lambda\left[\sum_{t=1}^{T} \left(r_t-\bar r\right)^2/T\right] - (1-\lambda)\bar r - \theta\left[\left(\sum_{t=1}^{T} \left(r_t-\bar r\right)^3/T\right)\Big/\left(\sum_{t=1}^{T} \left(r_t-\bar r\right)^2/T\right)^{3/2}\right]$$
> $$x_1,\dots,x_N;\;z_1,\dots,z_N$$
> $$st. \quad \sum_{i=1}^{N} z_i = K$$
> $$\varepsilon_i z_i \le w_i \le \delta_i z_i \qquad i=1,\dots,N;$$
> $$\sum_{i=1}^{N} w_i = 1$$
> $$r_t = \log_e\!\left[\left(\sum_{i=1}^{N} w_i v_{it}/v_{iT}\right)\Big/\left(\sum_{i=1}^{N} w_i v_{i,t-1}/v_{iT}\right)\right] \qquad t=1,\dots,T;$$
> $$w_i \ge 0 \qquad i=1,\dots,N;$$
> $$z_i \in \{0,1\} \qquad i=1,\dots,N;$$
> $$\bar r = \frac{\sum_{t=1}^{T} r_t}{T}.$$
>
> dove $\theta$ indica l'avversione/propensione all'asimmetria dell'investitore.
>
> Questo modello prende in considerazione anche il momento terzo della distribuzione dei rendimenti. Con riferimento al rendimento del portafoglio, il modello:
>
> - ne massimizza il valor medio;
> - ne minimizza la varianza;
> - ne massimizza l'asimmetria.

*(slide 18–19)*

## Dall'ottimizzazione vincolata alla PSO: funzioni di penalità e riformulazione dei vincoli

> [!abstract] Definizione
> **Alcuni aspetti tecnici.** La *Particle Swarm Optimization* (PSO) è una euristica/meta-euristica per l'**ottimizzazione non vincolata**. I modelli di selezione di portafoglio visti finora sono invece problemi di **ottimizzazione vincolata**.
>
> Il problema di ottimizzazione vincolata viene quindi riformulato in termini di problema di ottimizzazione non vincolata mediante il ricorso a opportune **funzioni di penalità**. Ciò richiede di riformulare opportunamente i vincoli.
>
> **Vincoli riformulati** (esemplificati sul modello Mean-Variance + vincoli misti-interi):
>
> $$\sum_{i=1}^{N} x_i = 1 \;\longrightarrow\; \left|\sum_{i=1}^{N} x_i - 1\right|$$
> $$\sum_{i=1}^{N} z_i = K \;\longrightarrow\; \left|\sum_{i=1}^{N} z_i - K\right|$$
> $$\varepsilon_i z_i \le x_i \;\; \text{per ogni } i \;\longrightarrow\; \sum_{i=1}^{N} \max\{0;\; \varepsilon_i z_i - x_i\}$$
> $$x_i \le \delta_i z_i \;\; \text{per ogni } i \;\longrightarrow\; \sum_{i=1}^{N} \max\{0;\; x_i - \delta_i z_i\}$$
> $$z_i \in \{0,1\} \;\; \text{per ogni } i \;\longrightarrow\; \sum_{i=1}^{N} \left|z_i(1-z_i)\right|$$
>
> **Modello riformulato** (non vincolato, con funzione di penalità pesata da $1/\varepsilon$):
>
> $$\min \; \lambda\left[\sum_{i=1}^{N}\sum_{j=1}^{N} x_i x_j \sigma_{ij}\right] - (1-\lambda)\left[\sum_{i=1}^{N} x_i \mu_i\right] + \frac{1}{\varepsilon}\Bigg[\left|\sum_{i=1}^{N} x_i - 1\right| + \left|\sum_{i=1}^{N} z_i - K\right|$$
> $$+ \sum_{i=1}^{N} \max\{0;\varepsilon_i z_i - x_i\} + \sum_{i=1}^{N} \max\{0; x_i-\delta_i z_i\} + \sum_{i=1}^{N} \left|z_i(1-z_i)\right|\Bigg]$$
>
> con variabili $x_1,\dots,x_N;\;z_1,\dots,z_N$.
>
> Similmente si procede per gli altri modelli (Semi-Variance, MAD, Mean-Variance-Skewness) descritti in precedenza: ciascun vincolo viene trasformato in un termine di penalità (valore assoluto dello scarto, o parte positiva della violazione) e sommato, pesato da $1/\varepsilon$, alla funzione obiettivo originaria.

*(slide 20–22)*

## Impostazione sperimentale: parametri della PSO e universo investibile

**Il settaggio** utilizzato per l'algoritmo PSO applicato al modello Mean-Variance + vincoli misti-interi è il seguente:

- numero di particelle: $40$;
- numero di iterazioni: $4000$;
- parametro di penalità: $0{,}0001$;
- peso di inerzia: $w = 0{,}7298$;
- coefficienti di accelerazione: $c_1 = c_2 = 1{,}49618$;
- percentuale minima del titolo $i$-esimo che può essere selezionata: $\varepsilon_i = 1\%$;
- percentuale massima del titolo $i$-esimo che può essere selezionata: $\delta_i = 50\%$;
- numero di titoli selezionabili: $K = 10,\, 20$;
- avversione alla varianza dell'investitore: $\lambda = 0{,}5$.

**I titoli** utilizzati nell'applicazione empirica sono quelli del FTSE-MIB, con dati dal 15.05.2007 al 31.12.2008:

| Titolo | Var. | Titolo | Var. | Titolo | Var. |
|---|---|---|---|---|---|
| A2A | x1 | Fiat | x15 | Parmalat | x29 |
| Alleanza | x2 | Finmeccanica | x16 | Pirelli & C. | x30 |
| Ansaldo STS. | x3 | Fondiaria-Sai | x17 | Prysmian | x31 |
| Atlantia | x4 | Generali | x18 | Saipem | x32 |
| Autogrill | x5 | Geox | x19 | Telecom Italia | x33 |
| Banca Mps | x6 | Impregilo | x20 | Tenaris | x34 |
| Banca Pop. Milano | x7 | Intesa San Paolo | x21 | Terna | x35 |
| Banco Popolare | x8 | Italcementi | x22 | Ubi Banca | x36 |
| Bulgari | x9 | Lottomatica | x23 | Unicredit | x37 |
| Buzzi Unicem | x10 | Luxottica Group | x24 | Unipol | x38 |
| Campari | x11 | Mediaset | x25 | | |
| Cir-Comp. I. R. | x12 | Mediobanca | x26 | | |
| Enel | x13 | Mediolanum | x27 | | |
| Eni | x14 | Mondadori Edit. | x28 | | |

*(slide 23–24)*

## Risultati numerici del modello Mean-Variance con vincoli misti-interi

> [!example] Esempio
> **Valore della funzione obiettivo e tempo di calcolo**, al variare del numero massimo di titoli selezionabili $K$:
>
> | K | Valore funzione obiettivo | Tempo impiegato |
> |---|---|---|
> | 10 | 15,2432 | 10,3341 |
> | 20 | 11,5738 | 11,9563 |
>
> **Composizione ottima del portafoglio (variabili $z_i$, $x_i$).** Il lucido riporta, per ciascuno dei 38 titoli, i valori ottimi delle variabili binarie di selezione $z_i$ e delle quote investite $x_i$ ottenuti dal modello MVM (Mean-Variance mixed-integer), separatamente per $K=10$ e $K=20$. Questi valori numerici compaiono solo come tabella incorporata nell'immagine della slide e non sono presenti nel layer di testo estratto dal PDF: per evitare di trascrivere cifre non verificabili (rischio di errore analogo a quello di leggere le decine di migliaia da un'immagine), non vengono riportate qui le singole cifre; si rimanda al lucido originale per i valori puntuali. Qualitativamente: coerentemente con il vincolo di cardinalità, per ciascun valore di $K$ esattamente $K$ titoli presentano $z_i \approx 1$ (titolo selezionato, con quota $x_i>0$), mentre i restanti presentano $z_i \approx 0$ e $x_i \approx 0$; alcuni valori mostrano lievi scostamenti dai valori teorici esatti (es. $z_i$ leggermente negativo o leggermente superiore a 1, $x_i$ leggermente negativo), dovuti alla natura euristica della PSO, che non garantisce il soddisfacimento esatto dei vincoli ma solo la loro minimizzazione tramite penalità.
>
> **Figura (pag. 27 del PDF) — Convergenza dell'algoritmo con $K=10$.** Grafico "CONVERGENZA DELL'ALGORITMO": in ascissa le iterazioni (0-4000), in ordinata il valore della funzione obiettivo (scala $\times 10^5$, da 0 a 4). La curva parte da un valore prossimo a $2\times 10^5$ e decresce rapidamente nelle prime centinaia di iterazioni, per poi stabilizzarsi vicino allo zero dopo circa 1200-1500 iterazioni, con un lieve gradino residuo intorno alle 3600 iterazioni. Mostra che l'algoritmo PSO converge in modo rapido e poi si stabilizza sul minimo trovato.
>
> **Figura (pag. 28 del PDF) — Performance out-of-sample con $K=10$, dal 01.01.2009 al 30.06.2009.** Grafico "ANDAMENTO DEL PORTAFOGLIO PER 6 MESI": in ascissa i giorni di negoziazione (0-160), in ordinata il valore del portafoglio (base 1 all'inizio del periodo, range 0,9-1,5). Il valore del portafoglio, dopo una breve flessione iniziale sotto 1 (minimo intorno a 0,92 nei primi giorni), cresce fino a circa 1,35 attorno al giorno 45, oscilla in un intervallo 1,20-1,35 fino al giorno 100 circa, per poi risalire stabilmente fino a un valore di circa 1,47 alla fine del periodo (giorno 150). Mostra che il portafoglio selezionato con il modello Mean-Variance e $K=10$ ha realizzato, fuori campione, un rendimento cumulato positivo e marcato nel semestre considerato, pur con una fase di flessione/lateralizzazione intermedia.

*(slide 25–28)*

## Codice MATLAB dell'algoritmo PSO per il modello Mean-Variance + vincoli misti-interi

> [!example] Esempio
> Il codice MATLAB implementa l'algoritmo di Particle Swarm Optimization applicato al modello Mean-Variance con vincoli misti-interi, secondo la riformulazione a funzioni di penalità vista in precedenza.
>
> ```matlab
> clc;
>
> % Caricamento dati storici
> [prezzi,testo] = xlsread('Dati');
> [n,numvar] = size(prezzi);
> rend = (prezzi(2:end,:) - prezzi(1:end-1,:))./prezzi(1:end-1,:);
>
> media = mean (rend);
> variance=cov(rend);
>
>
> % Inizializzazione dei parametri di PSO
> P=40; % numero particelle
> niter=4000; % numero iterazioni
> K=20; % numero massimo di titoli detenibili
>
> perc_min=ones(1,numvar)*0.01; % quota minima
> perc_max=ones(1,numvar)*0.5; % quota massima
>
> c1=1.49618;
> c2=1.49618;
> w=0.7298;
>
> vmaxx=zeros(1,numvar);
> vmaxz=zeros(1,numvar);
>
> % Lambda, Epsilon
> lambda=0.5;
> epsilon1=1.0e-004;
>
>
> % Vettori di appoggio per la funzione obiettivo (varianza, media, vincoli)
> var_port=zeros(P,1);
> med_port=zeros(P,1);
> vinc_1=zeros(P,1); % vincolo di bilancio
> vinc_2=zeros(P,1); % vincolo sul numero max di titoli (K)
> app_1=zeros(P,numvar);
> vinc_3=zeros(P,1); % x >= perc_min
> app_2=zeros(P,numvar);
> vinc_4=zeros(P,1); % x <= per_max
> app_3=zeros(P,numvar);
> vinc_5=zeros(P,1); % z è 0 o è 1
>
> % 1) Genera vettori; posizione, velocità, funzione obiettivo
> x=rand(P,numvar);
> vx=rand(P,numvar);
> z=rand(P,numvar);
> vz=rand(P,numvar);
> f=ones(P,1)*1.0e+015;
> x1=zeros(P,numvar);
> for p=1:P
>     for i=1:numvar
>         x1(p,i)=x(p,i)*z(p,i); % vettore di appoggio (x*z)
>     end;
> end;
>
> % pb=pbest, vettore dove c'è la posizione migliore assunta dalle particelle
> % nelle iterazioni precedenti; nell'ultima colonna c'è la funzione obiettivo
> % associata alla migliore posizione assunta
> pbx=[x f];
> pbz=z;
>
>
> % g=gbest, vettore che rappresenta la migliore posizione globale e
> % il valore della funzione obiettivo associata
> gx=zeros(1,numvar+1);
> gz=zeros(1,numvar);
>
> tic;
> for k=1:niter
>     % Individua il rande dinamico per la velocità massima
>     for i=1:numvar
>         vmaxx(i)=abs(max(x(:,i))-min(x(:,i)));
>         vmaxz(i)=abs(max(z(:,i))-min(z(:,i)));
>     end;
>
>
> % 2) Calcola la funzione obiettivo
>     for p=1:P
>         for i=1:numvar
>             x1(p,i)=x(p,i)*z(p,i);
>             app_1(p,i)=max(0,perc_min(i)*z(p,i)-x(p,i));
>             app_2(p,i)=max(0,x(p,i)-perc_max(i)*z(p,i));
>             app_3(p,i)=abs(z(p,i)*(1-z(p,i)));
>         end;
>
>        var_port(p)=(x1(p,:)*variance*x1(p,:)'); %varianza
>        med_port(p)=x1(p,:)*media'; %media
>        vinc_1(p)=abs(sum(x(p,:))-1); %somma delle quote=1
>        vinc_2(p)=abs(sum(z(p,:))-K); %max num titoli K
>        vinc_3(p)=sum(app_1(p,:)); %quota min
>        vinc_4(p)=sum(app_2(p,:)); %quota max
>        vinc_5(p)=sum(app_3(p,:)); %z è 0 o 1
>    end;
>
>
> %funzione obiettivo
>     f=lambda*var_port-(1-lambda)*med_port + ((1/epsilon1)*(vinc_1 + vinc_2 +
>     vinc_3 + vinc_4 + vinc_5));
>
>
> % 3) Confronta il valore della funzione obiettivo con il pbest
>     for p=1:P
>         if f(p)<pbx(p,numvar+1)
>             pbx(p,numvar+1)=f(p);
>             for i=1:numvar
>                 pbx(p,i)=x(p,i);
>                 pbz(p,i)=z(p,i);
>             end;
>         end;
>     end;
>
>
> % 4) Identifica la particella con migliore posizione
>     [minimo,posizione]=min(pbx(:,numvar+1));
>     gx(numvar+1)=minimo;
>     for i=1:numvar
>        gx(i)=pbx(posizione,i);
>        gz(i)=pbz(posizione,i);
>    end;
>
>
> % 5) Cambia la velocità e la posizione
>     for p=1:P
>         for i=1:numvar
>             vx(p,i)=w*vx(p,i)+c1*rand*(pbx(p,i)- x(p,i))+c2*rand*(gx(i)-x(p,i));
>             vz(p,i)=w*vz(p,i)+c1*rand*(pbz(p,i)- z(p,i))+c2*rand*(gz(i)-z(p,i));
>             if vx(p,i)>vmaxx(i)
>                 vx(p,i)=vmaxx(i);
>             end;
>             if vz(p,i)>vmaxz(i)
>                 vz(p,i)=vmaxz(i);
>             end;
>             z(p,i)=z(p,i)+vz(p,i);
>             x(p,i)=x(p,i)+vx(p,i);
>         end;
>     end;
>     converg(k,:)=gx(:,end);
>
>
> % 6) riparti dal 2) fino al criterio di stop
> end;
>
> toc;
>
> plot(converg)
> ```
>
> In sintesi, la struttura dell'algoritmo è:
>
> 1. caricamento dei prezzi storici e calcolo di rendimenti, media e matrice di covarianza;
> 2. inizializzazione dei parametri della PSO (numero di particelle $P=40$, iterazioni $niter=4000$, $K$, quote minime/massime, coefficienti $c_1,c_2,w$) e generazione casuale delle posizioni/velocità iniziali delle particelle (vettori $x$, $z$ e relative velocità);
> 3. ad ogni iterazione: calcolo della funzione obiettivo penalizzata (varianza e media di portafoglio, più i cinque termini di penalità per bilancio, cardinalità, quota minima, quota massima e binarietà di $z$), aggiornamento della miglior posizione individuale (*pbest*) e della miglior posizione globale (*gbest*), quindi aggiornamento di velocità e posizione di ciascuna particella;
> 4. al termine delle iterazioni, il vettore `converg` (valore della funzione obiettivo di *gbest* a ogni iterazione) viene tracciato con `plot(converg)`, producendo il grafico di convergenza mostrato in precedenza.

*(slide 29–33)*
