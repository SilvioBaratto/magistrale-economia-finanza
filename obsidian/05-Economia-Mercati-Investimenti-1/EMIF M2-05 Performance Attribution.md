---
title: "Performance Attribution"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M2-05_Performance-Attribution.pdf"
pages: 30
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione e riferimenti bibliografici

Lezione 15 del corso di Economia dei Mercati ed Investimenti Finanziari (II parte), tenuta da Loriana Pelizzon, dedicata alla **Performance Attribution**.

**Riferimenti testuali:**
- EGBG, cap. 25 — Valutazione della performance di portafoglio
- BKM (Bodie, Kane, Marcus – *Investments*), cap. 24 — Portfolio Performance Evaluation

*(slide 1–2)*

## Le fasi dell'asset allocation

> [!abstract] Definizione
> L'attività di **asset allocation** può essere scomposta nelle seguenti fasi:
>
> - **Strategic Asset Allocation**: determinare le quote di portafoglio analizzando la performance di equilibrio nel lungo periodo di ciascuna categoria di asset. Si determina l'*asset mix* ottimale da detenere nel lungo periodo.
> - **Tactical Asset Allocation**: strategia il cui obiettivo è ottenere performance migliori rispetto all'asset mix di lungo periodo variando i pesi delle categorie di asset in modo sistematico (anche **Market Timing**).
> - **Security Selection**: scelta della composizione di ciascuna categoria di asset (nel caso di singoli titoli: **Stock Picking**).

*(slide 3)*

## Il ruolo della performance attribution nel processo di investimento

In un'ottica di performance attribution, ciascuna fase del processo di investimento è associata a un organo decisionale e a un obiettivo specifico:

- **Strategic Asset Allocation** → definizione del benchmark di riferimento → responsabilità del *Comitato strategico e cliente*
- **Tactical Asset Allocation** → variazioni di breve periodo delle quote di portafoglio al fine di ottenere una Information Ratio positiva → responsabilità del *Comitato investimenti*
- **Security Selection** → replicare il benchmark o ottenere performance migliori → responsabilità del *Gestore del fondo*

**Figura — Integrated Management Process.** Schema a blocchi che collega Cliente/Obiettivi del Cliente, Strategic Asset Allocation (Obiettivi, Guidelines, Benchmark), Tactical Asset Allocation (Risk Budgeting, Identificazione di opportunità, Definizione della Model Strategy, Monitoraggio), Implementazione (Portfolio Transaction, Ribilanciamento) e infine Performance Analysis (Perf Attribution, Perf Measurement), il cui output retroagisce sul cliente. Sulla sinistra il flusso di informazioni di mercato (Long Term Expectation / Short Term Opportunities) alimenta sia la Strategic sia la Tactical Asset Allocation. Il diagramma mostra che la performance attribution non è un esercizio a sé stante ma l'ultimo anello di un processo decisionale integrato: essa fornisce un feedback specifico per manager sulle decisioni di investimento e consente di accertare le responsabilità di ciascun livello decisionale (strategico, tattico, di selezione).

*(slide 4–5)*

## Classificazione delle analisi di performance attribution

> [!abstract] Definizione
> L'analisi di performance attribution si può distinguere rispetto a due dimensioni:
>
> **All'orizzonte temporale:**
> - uniperiodale;
> - multiperiodale (dinamica).
>
> **All'informazione disponibile:**
> - **Style Analysis**: si basa solo sul rendimento del portafoglio e del benchmark nei periodi di riferimento.
> - **Informazione piena**: richiede la composizione e il rendimento del portafoglio e del benchmark per ciascuna categoria di asset, compresi i singoli titoli, nei periodi di riferimento.
>
> L'attività consiste nella **decomposizione della performance totale** in diverse componenti, ciascuna legata a specifici elementi della gestione. Un sistema comune di decomposizione prevede, ad esempio, queste componenti:
>
> 1. **Broad Asset Market allocation** tra equity, fixed income e money market (scelta settore);
> 2. **Scelta dei titoli** all'interno di ogni settore;
> 3. **Market Timing**: movimenti del mercato (Up/Down).

*(slide 6–7)*

## Il portafoglio benchmark ("Bogey portfolio")

> [!abstract] Definizione
> Per attribuire la performance alle varie componenti si costruisce un portafoglio di riferimento, detto **"Benchmark"** o **"Bogey portfolio"** (BKM-Investments, cap. 24).
>
> Per ogni asset class si determinano degli indici assunti come benchmark (ad esempio lo S&P 500 per la parte azionaria). Il portafoglio Bogey ha **pesi fissi** per ogni asset class e il suo rendimento è dato da:
>
> $$\sum_{i=1}^{n} w_{Bi}\, r_{Bi}$$
>
> dove:
> - $w_{Bi}$: peso dell'asset class $i$-esima nel portafoglio Bogey;
> - $r_{Bi}$: rendimento dell'asset class $i$-esima nel portafoglio Bogey.

*(slide 8)*

## Decomposizione del rendimento attivo: derivazione

> [!note] Dimostrazione
> Il gestore sceglie i pesi in ogni asset class $w_{pi}$ sulla base delle proprie aspettative e, all'interno di ogni asset class, seleziona un portafoglio che avrà il rendimento $r_{pi}$ nel periodo di valutazione:
>
> $$r_p = \sum_{i=1}^{n} w_{pi} r_{pi}$$
>
> Si calcola il rendimento di entrambi i portafogli (gestito e Bogey), la cui differenza è:
>
> $$r_p - r_B = \sum_{i=1}^{n} w_{pi} r_{pi} - \sum_{i=1}^{n} w_{Bi} r_{Bi} = \sum_{i=1}^{n} \left( w_{pi} r_{pi} - w_{Bi} r_{Bi} \right)$$
>
> I termini di questa equazione possono essere riscritti in modo tale da mostrare come le decisioni di asset allocation e security selection contribuiscono alla performance totale, sommando e sottraendo il termine incrociato $w_{Pi} r_{Bi}$:
>
> $$\text{Contribution from asset allocation} = (w_{Pi} - w_{Bi})\, r_{Bi}$$
> $$+\ \text{Contribution from security selection} = w_{Pi} (r_{Pi} - r_{Bi})$$
> $$=\ \text{Total contribution from asset class } i = w_{Pi} r_{Pi} - w_{Bi} r_{Bi}$$
>
> Il primo termine isola l'effetto della scelta dei pesi (asset allocation) valutata al rendimento benchmark, il secondo isola l'effetto della scelta dei titoli/rendimento (security selection) pesata al peso effettivo di portafoglio.

*(slide 9–10)*

## Approccio di piena informazione: Alpha di Allocation e di Selection

> [!abstract] Definizione
> Dato l'Alpha totale del portafoglio:
>
> $$Alpha = \sum_{i=1}^{N} \left( W_{P,i}\, r_{P,i} - W_{B,i}\, r_{B,i} \right)$$
>
> Conoscendo la composizione del portafoglio e le sue variazioni nel tempo, possiamo scomporre l'Alpha in due componenti:
>
> $$Alpha = Alpha_{Allocation} + Alpha_{Selection}$$
>
> $$Alpha_{Allocation} = \sum_{i=1}^{N} \left( W_{P,i} - W_{B,i} \right) \cdot r_B$$
>
> $$Alpha_{Selection} = \sum_{i=1}^{N} \left( r_{P,i} - r_{B,i} \right) \cdot W_{P,i}$$
>
> **Figura 24.11 — "Performance attribution of $i$th asset class. Enclosed area indica total rate of return."** Il grafico rappresenta sull'asse verticale il rendimento nell'asset class (con i livelli $r_{Bi}$ e $r_{Pi}$) e sull'asse orizzontale il peso nell'asset class (con i livelli $w_{Bi}$ e $w_{Pi}$). L'area rosa (rettangolo di base $w_{Bi}$ e altezza $r_{Bi}$) rappresenta il *Bogey return from $i$th asset class* $= r_{Bi} w_{Bi}$; la colonna aggiuntiva fino a $w_{Pi}$ rappresenta l'**Allocation**; la fascia superiore ("Added by Selection") rappresenta il contributo della **selection**, con il "Mixed Origin" (attribuito alla selection) all'angolo in alto a destra. La figura mostra visivamente come l'area totale racchiusa (il rendimento complessivo dell'asset class) si scomponga geometricamente nella componente di allocation (variazione di peso a rendimento benchmark) e nella componente di selection (variazione di rendimento al peso di portafoglio).

*(slide 11–12)*

## Esempio numerico: contributo di asset allocation e security selection

> [!example] Esempio
> Esempio (BKM) di applicazione dell'approccio Bogey a un portafoglio composto da Equity, Bonds e Cash.
>
> **Bogey Performance and Excess Return**
>
> | Component | Benchmark Weight | Return of Index during Month (%) |
> |---|---|---|
> | Equity (S&P 500) | .60 | 5.81 |
> | Bonds (Barclays Aggregate Index) | .30 | 1.45 |
> | Cash (money market) | .10 | 0.48 |
>
> Bogey = (.60 × 5.81) + (.30 × 1.45) + (.10 × 0.48) = 3.97%
>
> | | |
> |---|---|
> | Return of managed portfolio | 5.34% |
> | − Return of bogey portfolio | 3.97 |
> | **Excess return of managed portfolio** | **1.37%** |
>
> **A. Contribution of Asset Allocation to Performance**
>
> | Market | (1) Actual Weight in Market | (2) Benchmark Weight in Market | (3) Active or Excess Weight | (4) Market Return (%) | (5) = (3)×(4) Contribution to Performance (%) |
> |---|---|---|---|---|---|
> | Equity | .70 | .60 | .10 | 5.81 | .5810 |
> | Fixed-income | .07 | .30 | −.23 | 1.45 | −.3335 |
> | Cash | .23 | .10 | .13 | .48 | .0624 |
> | **Contribution of asset allocation** | | | | | **.3099** |
>
> **B. Contribution of Selection to Total Performance**
>
> | Market | (1) Portfolio Performance (%) | (2) Index Performance (%) | (3) Excess Performance (%) | (4) Portfolio Weight | (5) = (3)×(4) Contribution (%) |
> |---|---|---|---|---|---|
> | Equity | 7.28 | 5.81 | 1.47 | .70 | 1.03 |
> | Fixed-income | 1.89 | 1.45 | 0.44 | .07 | 0.03 |
> | **Contribution of selection within markets** | | | | | **1.06** |
>
> **Equity Asset Selection in dettaglio** (scomposizione settoriale della componente equity)
>
> | Sector | (1) Portfolio Beginning-of-Month Weight (%) | (2) S&P 500 Beginning-of-Month Weight (%) | (3) Active Weights (%) | (4) Sector Return (%) | (5) = (3)×(4) Sector Allocation Contribution |
> |---|---|---|---|---|---|
> | Basic materials | 1.96 | 8.3 | −6.34 | 6.9 | −0.4375 |
> | Business services | 7.84 | 4.1 | 3.74 | 7.0 | 0.2618 |
> | Capital goods | 1.87 | 7.8 | −5.93 | 4.1 | −0.2431 |
> | Consumer cyclical | 8.47 | 12.5 | −4.03 | 8.8 | 0.3546 |
> | Consumer noncyclical | 40.37 | 20.4 | 19.97 | 10.0 | 1.9970 |
> | Credit sensitive | 24.01 | 21.8 | 2.21 | 5.0 | 0.1105 |
> | Energy | 13.53 | 14.2 | −0.67 | 2.6 | −0.0174 |
> | Technology | 1.95 | 10.9 | −8.95 | 0.3 | −0.0269 |
> | **TOTALE** | | | | | **1.2898** |
>
> **Riassunto**
>
> | Voce | Contribution (basis points) |
> |---|---|
> | 1. Asset allocation | 31 |
> | 2. Selection | |
> | &nbsp;&nbsp;a. Equity excess return (basis points) | |
> | &nbsp;&nbsp;&nbsp;&nbsp;i. Sector allocation | 129 |
> | &nbsp;&nbsp;&nbsp;&nbsp;ii. Security selection | 18 |
> | &nbsp;&nbsp;&nbsp;&nbsp;147 × .70 (portfolio weight) = | 102.9 |
> | &nbsp;&nbsp;b. Fixed-income excess return, 44 × .07 (portfolio weight) = | 3.1 |
> | **Total excess return of portfolio** | **137.0** |

*(slide 13–16)*

## Il modello di Brinson, Hood e Beebower

> [!abstract] Definizione
> Il modello di **Brinson, Hood e Beebower** rappresenta la performance attribution come una matrice 2×2, incrociando la dimensione **Asset Allocation** (Attiva/Passiva) con la dimensione **Security Selection** (Attiva/Passiva):
>
> | | Security Selection: Attiva | Security Selection: Passiva |
> |---|---|---|
> | **Asset Allocation: Attiva** | **IV** — Rendimento di portafoglio totale | **II** — Rendimento Asset Allocation Tattica |
> | **Asset Allocation: Passiva** | **III** — Rendimento Security Selection | **I** — Rendimento Benchmark |
>
> I quattro rendimenti di quadrante sono definiti, in funzione dei pesi e rendimenti di portafoglio ($W_{P,i}, r_{P,i}$) e di benchmark ($W_{B,i}, r_{B,i}$), come:
>
> $$\text{IV (Totale)} = \sum_{i=1}^{N} W_{P,i}\cdot r_{P,i} \qquad \text{II (Tattica)} = \sum_{i=1}^{N} W_{P,i}\cdot r_{B,i}$$
>
> $$\text{III (Security Selection)} = \sum_{i=1}^{N} W_{B,i}\cdot r_{P,i} \qquad \text{I (Benchmark)} = \sum_{i=1}^{N} W_{B,i}\cdot r_{B,i}$$
>
> Tale scomposizione dell'Actual Asset Portfolio Return consente di definire le seguenti quantità:
>
> - **ASSET ALLOCATION TATTICA**: $II - I$
> - **SECURITY SELECTION**: $III - I$
> - **ALTRO**: $IV - II - III - I$
> - **PERFORMANCE TOTALE (ALPHA)**: $IV - I$
>
> In cui:
> - $W_{Pi}$: pesi del portafoglio per la categoria di asset $i$
> - $r_{Pi}$: rendimenti del portafoglio per la categoria di asset $i$
> - $W_{Bi}$: pesi del benchmark per la categoria di asset $i$
> - $r_{Bi}$: rendimenti del benchmark per la categoria di asset $i$
> - $N$: numero di categorie di asset
>
> La disponibilità di serie storiche relative ai pesi delle categorie di asset nel portafoglio ($W_P$) e nel Benchmark ($W_B$) consente di quantificare la scomposizione del rendimento complessivo. Le stesse quattro quantità possono essere espresse come sommatorie esplicite dell'attribuzione di performance alle diverse componenti dell'attività di gestione:
>
> $$\text{ASSET ALLOCATION TATTICA} = \sum_{i=1}^{N} \left( W_{P,i}\, r_{B,i} - W_{B,i}\, r_{B,i} \right)$$
>
> $$\text{SECURITY SELECTION} = \sum_{i=1}^{N} \left( W_{B,i}\, r_{P,i} - W_{B,i}\, r_{B,i} \right)$$
>
> $$\text{ALTRO o INTERAZIONE} = \sum_{i=1}^{N} \left( W_{P,i}\, r_{P,i} - W_{P,i}\, r_{B,i} - W_{B,i}\, r_{P,i} + W_{B,i}\, r_{B,i} \right)$$
>
> $$\text{PERFORMANCE TOTALE (ALPHA)} = \sum_{i=1}^{N} \left( W_{Pi}\cdot r_{P,i} - W_{B,i}\cdot r_{B,i} \right)$$

*(slide 17–21)*

## Esempio applicativo del modello Brinson-Hood-Beebower

> [!example] Esempio
> Applicazione numerica della matrice 2×2:
>
> | | Security Selection: Attiva | Security Selection: Passiva |
> |---|---|---|
> | **Asset Allocation: Attiva** | Totale (IV) = 13.41% | Active, Policy (II) = 13.23% |
> | **Asset Allocation: Passiva** | Security Selection (III) = 13.75% | Policy (I) = 13.49% |
>
> Il rendimento attivo è dovuto a:
>
> | Componente | Valore |
> |---|---|
> | Asset Allocation Tattica | −0.26% |
> | Security Selection | +0.26% |
> | Altro | −0.07% |
> | **Totale** | **−0.07%** |

*(slide 22–23)*

## L'effetto di interazione: esempio Case 1 (Equity/Bond)

> [!example] Esempio
> **Case 1: The Interaction Effect.** Dati di partenza:
>
> | | Weight Benchmark | Weight Portfolio | Return Benchmark | Return Portfolio |
> |---|---|---|---|---|
> | Equity | 50% | 70% | 3.0% | 5.0% |
> | Bond | 50% | 30% | 2.0% | 3.0% |
> | **Totale** | **100%** | **100%** | **2.5%** | **4.4%** |
>
> Le decisioni di **Asset Allocation** (sovrapesare Equity, sottopesare Bond) e di **Stock/Bond Selection** (risultato in Equity e Bond, con maggior rendimento rispetto al benchmark) contribuiscono entrambe all'out-performance di 1.9 punti percentuali (4.4% − 2.5%). La performance attribution separa l'impatto delle decisioni di asset allocation da quello delle decisioni di stock selection.
>
> **Equity Attribution.** Rendimento benchmark equity 3.0%, rendimento medio del Balanced Portfolio Benchmark 2.5%:
> - **A — Asset allocation return**: excess return dovuto alla decisione di Asset Allocation = 0.5% × 20% overweight = **0.1%** (la stock selection non è considerata)
> - **S — Stock Selection return**: excess return dovuto alla decisione di Stock Selection = 2% selection return × 50% = **1.0%** (l'asset allocation non è considerata)
> - **I — Interaction**: effetto risultante dall'incrocio tra le due decisioni indipendenti = 20% overweight × 2% selection return = **0.4%**
>
> **Equity e Bond Attribution.** Ripetendo la scomposizione anche per i Bond (peso benchmark 50%, peso attivo −20% rispetto al benchmark, benchmark return 2%, out-performance selection 1%):
> - Equity: S = 1.0%, A = 0.1%, I = 0.4%
> - Bond: S = 0.5%, A = 0.1%, I = −0.20%
>
> **Dati Portfolio e Performance — riepilogo.** Ripetendo la tabella dati (identica a quella di Case 1, differenza di rendimento 4.4% − 2.5% = 1.90%), la scomposizione per asset class in Selection, Allocation, Interaction è:
>
> | | Selection | Allocation | Interaction | Sum |
> |---|---|---|---|---|
> | Equity | 1.00% | 0.1% | 0.4% | 1.5% |
> | Bond | 0.50% | 0.1% | −0.2% | 0.4% |
> | **Totale** | **1.5%** | **0.2%** | **0.2%** | **1.9%** |

*(slide 24–27)*

## Interpretazione dell'effetto di interazione

L'effetto di interazione si può esprimere come prodotto tra la componente di allocation e la componente di selection:

$$\text{Interaction} = \underbrace{(\text{Sotto/sovrapesare})}_{\text{Allocation}} \times \underbrace{(\text{Sotto/sovraperformance})}_{\text{Selection}}$$

- **Small Interaction Effect**: la performance deriva principalmente da una sola decisione (fra allocation e selection).
- **Large Positive Interaction Effect**: la responsabilità del risultato positivo non è chiara, perché può derivare da: (i) buone abilità di selection combinate con un sovrapeso della specifica asset class; oppure (ii) selezione sfortunata, ma mitigata da un sottopeso di quella asset class, che attenua il risultato negativo.
- **Large Negative Interaction Effect**: *"The left hand did not known what the right hand was doing"* — le asset class con la migliore (peggiore) selection sono state sotto- (sovra-) pesate, cioè le decisioni di allocation e di selection sono andate in direzioni opposte, penalizzando il risultato complessivo.

*(slide 28)*

## Esempio finale: performance attribution multi-asset rispetto al benchmark

> [!example] Esempio
> Esempio di performance attribution rispetto al rendimento benchmark su tre categorie di asset (Azioni, Obbligazioni, Liquidità):
>
> | | Quote Portfolio | Quote Benchmark | Rendimenti Portfolio | Rendimenti Benchmark | Allocation | Selection | Alpha |
> |---|---|---|---|---|---|---|---|
> | Azioni | 0,2 | 0,45 | -7 | -5,5 | 1,00625 | -0,3 | 0,70625 |
> | Obbligazioni | 0,4 | 0,45 | 3 | 2 | -0,17375 | 0,4 | 0,22625 |
> | Liquidità | 0,4 | 0,1 | 1 | 1 | 0,7425 | 0 | 0,7425 |
> | **Totale** | | | | | **1,575** | **0,1** | **1,675** |
>
> $$R_P = 0.2 \qquad R_B = -1.475 \qquad Alpha = (0.2 - (-1.475)) = 1.675$$
>
> L'analisi può continuare considerando i **Settori di attività** all'interno di ciascuna categoria, fino all'analisi dei singoli titoli.

*(slide 29)*

## Conclusioni

Per costruire un sistema di performance attribution è fondamentale comprendere:

- il processo di investimento;
- come le decisioni di active management sono prese.

Un buon sistema di performance attribution:

- fornisce un feedback alla decisione dei gestori;
- garantisce l'accertamento delle responsabilità.

*(slide 30)*
