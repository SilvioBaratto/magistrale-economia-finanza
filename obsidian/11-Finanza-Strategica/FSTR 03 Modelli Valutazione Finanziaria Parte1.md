---
title: "Dal valore degli investimenti al valore d'impresa: i metodi DCF (modelli sintetici asset side ed equity side)"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_03_Modelli-Valutazione-Finanziaria-Parte1.pdf"
pages: 30
text_layer: true
verified: true
generated: 2026-08-30
---

## Introduzione e programma del corso

**Titolo del modulo:** Strategie di investimento — *Dal valore degli investimenti al valore d'impresa: i metodi DCF* — *I modelli sintetici asset side e equity side*.

**Lettura di riferimento:** Capitolo 8, fino a 8.4, Testo BBS.

**Argomenti del corso (in questo modulo si tratta il punto evidenziato):**
- Le decisioni di investimento per l'impresa indebitata
- **Dal valore degli investimenti al valore d'impresa (I): i metodi DCF** ← argomento di questa lezione
- Dal valore degli investimenti al valore d'impresa (II): i multipli di borsa
- Crescita esterna e valore delle operazioni di integrazione
- La Due Diligence

*(slide 1–2)*

## Le grandezze di riferimento per la valutazione dell'impresa

> [!abstract] Definizione
> La valutazione d'impresa può essere condotta secondo due ottiche alternative e complementari, **assets** ed **equity**, ciascuna con le proprie grandezze di riferimento a livello patrimoniale, reddituale, finanziario e di costo del capitale:
>
> | Dimensione | Ottica «ASSETS» | Ottica «EQUITY» |
> |---|---|---|
> | Valore stimato | Asset Value (EV) | Equity (MK CAP) |
> | Patrimoniale | CIN rettificato | Capitale proprio rettificato |
> | Reddituale | NOPAT normalizzato | Reddito di bilancio normalizzato |
> | Finanziario | FCFF / FCFO | FCFE |
> | Costo del capitale | WACC | Costo Equity |
>
> **Le grandezze da considerare** — schema di raccordo tra le due ottiche:
> - **Enterprise Value (Assets) = E.V.**
> - **Equity Value** = MK CAP (capitalizzazione di mercato) + Debt (NFP)
>
> In altri termini, l'Enterprise Value rappresenta il valore complessivo del capitale investito nell'attività operativa dell'impresa, mentre l'Equity Value (la capitalizzazione di mercato) ne rappresenta solo la componente di pertinenza degli azionisti, al netto della Posizione Finanziaria Netta (NFP).

*(slide 3–4)*

## Relazione tra Enterprise Value ed Equity Value: esempi numerici

> [!example] Esempio
> Relazione generale: $$EV = MK\,CAP + NFP$$ dove NFP (Posizione Finanziaria Netta) è il debito finanziario al netto della cassa.
>
> **Caso 1 — Impresa indebitata, NFP > 0**
>
> | Impresa | Enterprise Value (E.V.) | Equity Value (MK CAP) | Debt (NFP) |
> |---|---|---|---|
> | Alfa | €60m | €15m | €45m |
> | Beta | €70m | €15m | €55m |
>
> Verifica: Alfa 15+45=60; Beta 15+55=70. A parità di Equity Value, un maggiore indebitamento (NFP) fa aumentare l'Enterprise Value.
>
> **Caso 2 — Impresa non indebitata, NFP = 0**
>
> | Impresa | Enterprise Value (E.V.) | Equity Value (MK CAP) |
> |---|---|---|
> | Gamma | €95m | €95m |
> | Delta | €74m | €74m |
>
> In assenza di debito, Enterprise Value ed Equity Value coincidono numericamente.
>
> **Caso 3 — Impresa non indebitata con liquidità netta, NFP < 0**
>
> Rispetto al caso precedente, alle stesse imprese Gamma e Delta si aggiunge una componente di cassa (NFP negativo, cioè posizione di liquidità netta):
> - Impresa Gamma: Fixed Assets €95m + Cassa (NFP) €10m sul lato dell'attivo; Equity Value (MK CAP) €105m sul lato del passivo; il riquadro complessivo «EV — Enterprise Value» riportato in slide vale €105m (somma di Fixed Assets e Cassa).
> - Impresa Delta: Fixed Assets €74m + Cassa (NFP) €10m; Equity Value (MK CAP) €84m; il riquadro «EV» vale €84m.
>
> In entrambi i casi, non essendoci debito, l'Equity Value coincide con il totale dell'attivo (immobilizzazioni + cassa): la liquidità netta si somma, anziché sottrarsi, nel passaggio dal valore degli assets operativi al valore per gli azionisti.
>
> **Figura (pagine 5-7)** — Schemi a blocchi che scompongono l'Enterprise Value nelle componenti Equity Value (MK CAP) e Debt (NFP) per le imprese Alfa, Beta, Gamma e Delta, nei tre casi di indebitamento netto positivo, nullo e negativo. Illustrano graficamente come $MK\,CAP = EV - NFP$.

*(slide 5–7)*

## Richiami: EBIT, EBITDA e NOPAT

> [!abstract] Definizione
> **Definizione.** Il **NOPAT** (Net Operating Profit After Taxes), traducibile come Utile netto operativo (EBIT) post imposte, misura il risultato operativo di una società al netto delle imposte. Di conseguenza misura il profitto netto generato dalle sole attività caratteristiche, indipendentemente dalla struttura finanziaria:
> $$NOPAT = EBIT \times (1 - t_c)$$
>
> **Esempio illustrativo (conto economico):**
>
> | Voce | Valore |
> |---|---|
> | Ricavi | 150.000 |
> | Costo del venduto | 70.000 |
> | **EBITDA** | **80.000** |
> | Ammortamenti | 25.000 |
> | **EBIT** | **55.000** |
> | Oneri finanziari | 10.000 |
> | **EBT** | **45.000** |
> | Imposte 20% | 9.000 |
> | **Reddito operativo** | **36.000** |
>
> $$NOPAT = EBIT \times (1-t_c) = 55.000 \times (1-20\%) = 44.000$$

*(slide 8)*

## Esercizio svolto: EBIT e NOPAT dell'azienda Alfa

> [!example] Esempio
> **Traccia.** L'azienda Alfa presenta un Fatturato di € 568.000 e costi di acquisto materie prime per € 372.000, costo del lavoro per € 58.000, costi per affitto immobile produttivo € 43.000, ammortamenti € 12.000, oneri finanziari € 22.000. Il carico fiscale stimato è pari al 27,9%.
>
> Richieste:
> 1. Calcolare EBITDA e NOPAT.
> 2. Calcolare il Reddito netto d'esercizio.
>
> **Soluzione — Conto economico:**
>
> | Voce | Valore |
> |---|---|
> | Fatturato | 568.000 |
> | Acquisto materie prime | -372.000 |
> | Costo del lavoro | -58.000 |
> | Affitti | -43.000 |
> | **EBITDA** | **95.000** |
> | Ammortamenti | -12.000 |
> | **EBIT** | **83.000** |
> | Oneri finanziari | -22.000 |
> | **EBT** | **61.000** |
> | Imposte d'esercizio | -17.019 |
> | **Reddito operativo** | **43.981** |
>
> **Calcolo del NOPAT:**
>
> | Voce | Valore |
> |---|---|
> | EBIT | 83.000 |
> | Imposte sull'EBIT | -23.157 |
> | **NOPAT** | **59.843** |
>
> **Nota (NB):** l'ammontare delle imposte calcolate sull'EBIT (23.157, cioè EBIT × 27,9%) è diverso dalle imposte d'esercizio (17.019, cioè EBT × 27,9%), perché diversa è la base imponibile a cui si applica l'aliquota (EBIT vs EBT).

*(slide 9–10)*

## Richiami: Capitale Investito Netto (CIN) e Capitale Circolante Netto (CCN)

> [!abstract] Definizione
> Lo stato patrimoniale riclassificato in ottica finanziaria contrappone il capitale investito alle fonti di finanziamento:
>
> | Capitale investito netto | Fonti di finanziamento |
> |---|---|
> | CCN: Capitale Circolante Netto | Patrimonio netto: Equity |
> | Capitale immobilizzato netto | PFN: Debt |
>
> **Definizione.** Il **capitale investito netto operativo (CIN)** è dato dalla somma tra capitale circolante commerciale (CCN) ed immobilizzazioni caratteristiche nette:
> $$CIN = CCN + \text{Immobilizzazioni caratteristiche nette}$$
> Specularmente, le fonti di finanziamento si compongono di Patrimonio Netto (Equity) e Posizione Finanziaria Netta (PFN, Debt).

*(slide 11)*

## La valutazione assoluta (DCF)

La valutazione assoluta (Discounted Cash Flow):
- È **focalizzata sull'impresa** e fondata:
  - sull'analisi delle sue **caratteristiche** (business model, strategie, management, patrimonio, ecc.) e sulla previsione delle future **performance economico-finanziarie**;
  - sulla considerazione delle sue **politiche finanziarie** (di finanziamento e di dividendo);
  - sulla misurazione del suo **rischio operativo e finanziario**.
- Si basa su un **criterio analitico di stima**.
- Conduce a **valori finanziari** (anche detti «fondamentali», o valori **intrinseci**) che hanno significato economico in quanto fondati sul principio di convenienza economica dell'investimento in capitale di rischio aziendale.

**Note terminologiche:**
- *Rischio operativo*: rischio di perdite derivanti da fallimenti o inadeguatezza dei processi interni, delle risorse umane e dei sistemi tecnologici, oppure derivanti da eventi esterni.
- *Rischio finanziario*: rischio che incide sulla liquidità aziendale, legato all'equilibrio tra flussi monetari in entrata e in uscita.

**Figura (pagina 13)** — Estratto del rendiconto finanziario consolidato di Brembo (esercizi 31/12/2020 e 31/12/2019), articolato in flusso monetario generato dalla gestione operativa, flusso da attività di investimento e flusso da attività di finanziamento, con riconciliazione della disponibilità liquida di inizio e fine periodo. L'esempio mostra concretamente come, a partire da un bilancio reale, si ricostruiscono i flussi di cassa che alimentano i modelli DCF di valutazione assoluta.

*(slide 12–13)*

## La valutazione relativa (multipli): definizione

> [!abstract] Definizione
> Nella logica comparativa, la valutazione:
> - esprime un **valore relativo** dell'impresa, fondato sulla comparazione con imprese simili (*comparables*);
> - richiede l'applicazione di moltiplicatori (i **multipli di mercato**) desumibili dalla dinamica dei prezzi che il mercato segna per i comparables;
> - conduce a **valori di mercato** (anche detti **prezzi probabili**).
>
> **Definizione.** I multipli di mercato sono **rapporti tra i prezzi di mercato (quotazioni) di uno strumento azionario e una data grandezza di bilancio**.

*(slide 14)*

## Esempio: individuazione dei comparables e calcolo dei multipli

> [!example] Esempio
> **Passo 1 — Identificazione dei comparables.** Partendo da Brembo (produttore di sistemi frenanti), si individua un insieme di comparables nel settore automotive tramite uno strumento di ricerca aziendale:
>
> | Azienda | Sede principale (HQ) | Dipendenti | Valutazione ($) |
> |---|---|---|---|
> | Brembo | Stezzano, IT | 10.868 (↑3%) | 3,5 miliardi |
> | Kongsberg Automotive | Zürich, CH | 11.234 (↑3%) | 265,9 milioni |
> | Ford Otosan | İstanbul, TR | 14.145 | N/A |
> | Subaru | Tokyo, JP | 36.910 | 13,2 miliardi |
> | BorgWarner | Auburn Hills, US | 49.300 (↓1%) | 9,2 miliardi |
>
> **Figura (pagina 15)** — Screenshot di uno strumento di ricerca comparables che affianca Brembo a quattro potenziali comparables del settore automotive, con sede, numero di dipendenti e valutazione. Mostra il primo passo pratico di selezione dell'insieme di comparables.
>
> **Passo 2 — Calcolo dei multipli su comparables più mirati.** Il set viene affinato a due comparables più simili a Brembo per attività (componentistica auto): Sogefi e Valeo.
>
> | Azienda | P/E | P/BV |
> |---|---|---|
> | Brembo | 16,48 | 2,02 |
> | Sogefi | 51,53 | 0,54 |
> | Valeo | 22,99 | 1,09 |
>
> **Figura (pagina 16)** — Confronto tra Brembo, Sogefi e Valeo sui multipli Price/Earnings (P/E) e Price/Book Value (P/BV). Evidenzia una forte eterogeneità di valutazione tra imprese dello stesso settore: Brembo presenta il P/E più basso ma il P/BV più alto del gruppo.
>
> **Passo 3 — Applicazione del multiplo EV/EBITDA nel settore alimentare (secondo esempio).**
>
> | Azienda | Capitalizzazione (mgl €) | EBITDA (mgl €) | Multiplo EBITDA |
> |---|---|---|---|
> | Conagra Foods Inc. | 17.383.003 € | 1.391.339 € | 12,49 |
> | General Mills Inc. | 35.364.038 € | 2.999.013 € | 11,79 |
> | Kellog Co. | 24.665.300 € | 2.319.281 € | 10,63 |
> | Marr S.p.A. | 1.269.299 € | 105.674 € | 12,01 |
> | Tyson Foods, Inc. | 19.542.863 € | 2.479.693 € | 7,88 |
>
> Valore medio del multiplo EBITDA nel gruppo: **10,96**.
>
> **Figura (pagina 17)** — Grafico a barre «Multiplo EBITDA» per le cinque aziende del settore alimentare, con linea orizzontale del valore medio (10,96). Mostra la dispersione dei multipli EV/EBITDA impliciti tra i comparables (da 7,88 di Tyson Foods a 12,49 di Conagra Foods), multipli che possono essere applicati all'EBITDA di un'impresa target (es. MARR S.p.A., evidenziata) per stimarne il valore per analogia di mercato.

*(slide 15–17)*

## Valutazione assoluta e valutazione relativa: un approccio complementare

L'approccio professionale oggi ritenuto più corretto è quello di **associare** le valutazioni assolute e relative.

Il ricorso ai multipli in senso **complementare** risponde all'esigenza di identificare le **leve del valore** e le **leve di prezzo** (variabili di contesto) che guidano i prezzi del mercato finanziario, nella prospettiva di una migliore copertura dello spettro di informazioni rilevanti ai fini della valutazione.

*(slide 18)*

## I metodi DCF: formule generali

> [!abstract] Definizione
> Le formule generali dei metodi DCF si distinguono per ottica di valutazione (Assets vs Equity):
>
> **Ottica Assets:**
> $$V = \sum_{t=1}^{\infty} \frac{FCFF_t}{(1 + WACC)^t}$$
>
> **Ottica Equity:**
> $$E = \sum_{t=1}^{\infty} \frac{FCFE_t}{(1 + r_E)^t}$$
>
> Le due grandezze sono legate dalla relazione:
> $$E = V - D$$
>
> **Nota importante:** Affinché sia possibile utilizzare tassi di sconto stabili (WACC e $r_E$ costanti nel tempo), tali metodi assumono **costanza nel tempo del rischio operativo e finanziario** dell'impresa.

*(slide 19)*

## I flussi finanziari di riferimento: dal MOL a FCFF e FCFE

> [!abstract] Definizione
> Il flusso di cassa rilevante per le valutazioni aziendali si costruisce a cascata a partire dal MOL, attraversando le diverse aree gestionali dell'impresa:
>
> | Area | Voce | Flusso intermedio |
> |---|---|---|
> | Area gestione corrente | MOL | |
> | | − Variazione CCNO | |
> | | | **CASH FLOW GESTIONALE LORDO** |
> | | − Flusso fiscale operativo (imposte + scudi fiscali − variazione debiti per imposte) | |
> | | | **CASH FLOW GESTIONALE NETTO** |
> | Area investimenti | −/+ Investimenti/Disinvestimenti in capitale fisso | |
> | | | **FREE CASH FLOW TO THE FIRM (FCFF)** |
> | Area straordinaria | +/− Proventi/Oneri straordinari | |
> | Area capitale di terzi | − Oneri finanziari netti | |
> | | + Scudo fiscale oneri finanziari | |
> | | +/− Aumento/Riduzione debiti finanziari | |
> | Area capitale proprio | | **FREE CASH FLOW TO EQUITY (FCFE)** |
>
> Il FCFF rappresenta il flusso disponibile per tutti i finanziatori (equity e debito), mentre il FCFE è il flusso residuo disponibile per i soli azionisti dopo aver remunerato e rimborsato/rifinanziato il debito.

*(slide 20)*

## I metodi DCF: funzionamento — modelli sintetici e analitici

> [!abstract] Definizione
> I metodi DCF si distinguono in due modelli alternativi di funzionamento:
>
> | Modello sintetico | Modello analitico |
> |---|---|
> | Il valore degli assets o dell'equity viene ottenuto con **formule compatte** che, ad esempio, prevedono: flussi costanti; flussi con tasso di crescita costante | Il valore degli assets o dell'equity viene ottenuto come **somma tra**: un valore frutto di un piano esplicito (3-7 anni); un **terminal value** attualizzato, frutto di un metodo sintetico |
>
> **Nota importante:** solitamente si utilizza il metodo analitico; tuttavia il vantaggio dei metodi sintetici rispetto a quello analitico si manifesta nel caso di «periodi di discontinuità» (grossi investimenti pluriennali, abbattimento debito, ecc.), dove i modelli sintetici — con la loro semplicità — restano comunque utili come base per stimare il terminal value nel metodo analitico.

*(slide 21)*

## I flussi finanziari FCFF e FCFE nelle ipotesi Steady State e Steady Growth

> [!abstract] Definizione
> Le formule generali del flusso di cassa (si veda la sezione precedente) si semplificano notevolmente sotto due ipotesi limite.
>
> **Ipotesi Steady State (flussi costanti nel tempo):**
>
> | Formula generale | Steady state |
> |---|---|
> | MOL | MOL |
> | − Variazione CCNO | − (nulla) |
> | CASH FLOW GESTIONALE LORDO | → MOL |
> | − Flusso fiscale operativo | − Imposte operative |
> | CASH FLOW GESTIONALE NETTO | → MOL netto |
> | −/+ Investimenti/Disinvestimenti capitale fisso | −/+ Ammortamenti |
> | FREE CASH FLOW TO THE FIRM (FCFF) | → **NOPAT** |
> | +/− Proventi/Oneri straordinari | +/− Proventi/Oneri straordinari |
> | − Oneri finanziari netti | − Oneri finanziari netti |
> | + Scudo fiscale oneri finanziari | + Scudo fiscale oneri finanziari |
> | +/− Aumento/Riduzione debiti finanziari | − (nulla) |
> | FREE CASH FLOW TO EQUITY (FCFE) | → **RIS. BIL.** (Reddito di bilancio) |
>
> In steady state, non essendovi variazioni di capitale circolante, investimenti netti in eccesso rispetto agli ammortamenti, né variazioni del debito finanziario, il **FCFF coincide con il NOPAT** e il **FCFE coincide con il Reddito di bilancio**.
>
> **Ipotesi Steady Growth (flussi che crescono a un tasso costante g):**
>
> | Formula generale | Steady growth |
> |---|---|
> | MOL | MOL × (1+g) |
> | − Variazione CCNO | − g × CCNO |
> | CASH FLOW GESTIONALE LORDO | → MOL×(1+g) − g×CCNO |
> | − Flusso fiscale operativo | − Imposte operative × (1+g) |
> | CASH FLOW GESTIONALE NETTO | → MOL netto×(1+g) − g×CCNO |
> | −/+ Investimenti/Disinvestimenti capitale fisso | − (g×C.F. + Amm.×(1+g)) |
> | FREE CASH FLOW TO THE FIRM (FCFF) | → **NOPAT×(1+g) − g×CINO** |
> | +/− Proventi/Oneri straordinari | +/− Proventi/Oneri straordinari × (1+g) |
> | − Oneri finanziari netti | − Oneri finanziari netti × (1+g) |
> | + Scudo fiscale oneri finanziari | + Scudo fiscale × (1+g) |
> | +/− Aumento/Riduzione debiti finanziari | + g × Debiti finanziari |
> | FREE CASH FLOW TO EQUITY (FCFE) | → **RIS. BIL.×(1+g) − g×C.P.** |
>
> In steady growth, tutte le componenti crescono al tasso costante g; il FCFF risulta pari a NOPAT×(1+g) al netto del reinvestimento necessario a sostenere la crescita del capitale investito netto operativo (CINO), e analogamente il FCFE è pari al Reddito di bilancio×(1+g) al netto del reinvestimento in capitale proprio (C.P.) necessario a sostenere la crescita.

*(slide 22–23)*

## I modelli sintetici DCF: le formule di Steady State e Steady Growth

> [!abstract] Definizione
> Applicando le semplificazioni di flusso viste nella sezione precedente alle formule generali di valutazione, si ottengono le formule compatte dei modelli sintetici:
>
> **Steady state:**
> $$V = \frac{NOPAT}{WACC}$$
> $$E = \frac{R.BILANCIO}{r_E}$$
>
> **Steady growth:**
> $$V = \frac{NOPAT(1+g) - CINO \cdot g}{WACC - g}$$
> $$E = \frac{R.BILANCIO(1+g) - C.P. \cdot g}{r_E - g}$$
>
> dove $V$ è il valore in ottica assets (Enterprise Value), $E$ il valore in ottica equity (Equity Value), $g$ il tasso di crescita costante, $CINO$ il Capitale Investito Netto Operativo, $C.P.$ il Capitale Proprio, $WACC$ il costo medio ponderato del capitale e $r_E$ il costo dell'equity (rendimento atteso dagli azionisti).

*(slide 24)*

## Esempio «Steady State»: valutazione dell'impresa Alfa

> [!example] Esempio
> **Traccia.** Considerando l'esempio precedente dell'azienda Alfa (pagine 9-10 di queste slides), si calcoli l'Enterprise Value e l'Equity Value sapendo che è stato stimato un WACC del 5,8% ed un rendimento atteso per gli azionisti ($r_E$) pari al 7,5%.
>
> Domanda: Quanto vale l'impresa Alfa? In ottica Assets? In ottica Equity?
>
> **Soluzione.** Applicando le formule dello steady state con NOPAT = 59.843 e Reddito operativo = 43.981 (calcolati nell'esercizio delle pagine 9-10):
>
> | EV = NOPAT / WACC | |
> |---|---|
> | 59.843 / 5,8% = | **1.031.776** |
>
> | Equity Value = Redd. Operativo / $r_E$ | |
> |---|---|
> | 43.981 / 7,5% = | **586.413** |
>
> **Risultato finale:**
> - Enterprise Value (ottica Assets) = **1.031.776**
> - Equity Value (ottica Equity) = **586.413**
> - Posizione Finanziaria Netta implicita: $NFP = EV - Equity\,Value = 1.031.776 - 586.413 = $ **445.363**

*(slide 25–27)*

## Esempio «Steady Growth»: valutazione dell'impresa Alfa

> [!example] Esempio
> **Traccia.** Considerando l'esempio precedente dell'azienda Alfa, si calcoli l'Enterprise Value e l'Equity Value sapendo che è stato stimato un WACC del 5,8% ed un rendimento atteso per gli azionisti ($r_E$) pari al 7,5%. Sappiamo inoltre che l'azienda presenta un Capitale Investito Netto Operativo di Euro 760.000, un Capitale Proprio di Euro 302.000 e prevede di crescere ad un tasso costante del 2,0%.
>
> Domanda: Quanto vale l'impresa Alfa? In ottica Assets? In ottica Equity?
>
> **Soluzione.** Applicando le formule dello steady growth:
>
> | EV = [NOPAT × (1+g) − CINO×g] / (WACC−g) | |
> |---|---|
> | Numeratore | 45.840 |
> | Denominatore | 3,80% |
> | **EV=** | **1.206.312** |
>
> | Equity value = [Redd. Operativo × (1+g) − Cap Proprio×g] / ($r_E$−g) | |
> |---|---|
> | Numeratore | 38.821 |
> | Denominatore | 5,50% |
> | **Equity value=** | **705.829** |
>
> **Risultato finale:**
> - Enterprise Value (ottica Assets) = **1.206.312**
> - Equity Value (ottica Equity) = **705.829**
> - Posizione Finanziaria Netta implicita: $NFP = EV - Equity\,value = 1.206.312 - 705.829 = $ **500.483**

*(slide 28–30)*
