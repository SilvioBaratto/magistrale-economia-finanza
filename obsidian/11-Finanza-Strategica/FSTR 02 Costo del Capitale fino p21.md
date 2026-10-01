---
title: "Le decisioni di investimento per l'impresa indebitata: il costo del capitale"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_02_Costo-del-Capitale-fino-p21.pdf"
pages: 22
text_layer: true
verified: true
generated: 2026-08-30
---

## Introduzione e programma del corso

**Corso:** Strategie di Investimento.

**Modulo:** Le decisioni di investimento per l'impresa indebitata — *Il costo del capitale*.

**Letture di riferimento:** Capitolo 7.3 fino a equazione 7.21 del testo di BBS (Berk, DeMarzo, Stefanini o equivalente — testo indicato con la sigla BBS).

**Argomenti del corso** (il modulo corrente tratta il primo punto):

1. Le decisioni di investimento per l'impresa indebitata *(argomento di questa lezione)*
2. Dal valore degli investimenti al valore d'impresa (I): i metodi DCF
3. Dal valore degli investimenti al valore d'impresa (II): i multipli di borsa
4. Crescita esterna e valore delle operazioni di integrazione

*(slide 1–2)*

## La struttura del tasso di sconto: dal WACC alle sue componenti

> [!abstract] Definizione
> Per valutare un progetto d'investimento occorre individuare il tasso di sconto appropriato. Lo stato patrimoniale a valori di mercato dell'impresa si scompone in:
>
> - **ASSETS** — l'insieme dei beni e delle risorse economiche dell'azienda: impianti, macchinari, immobili, brevetti, capitale circolante, competenze, tecnologia. Sono gli elementi che permettono all'azienda di produrre beni, erogare servizi e generare flussi di cassa. Il tasso a cui vengono attualizzati i flussi generati dagli assets è il **WACC** (Weighted Average Cost of Capital).
> - **EQUITY** — rappresenta la proprietà dell'azienda, che sopporta l'intero rischio residuo della gestione. Riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti e pretende un rendimento adeguato al rischio assunto, indicato con $r_E$.
> - **DEBTS** — tutte le forme di finanziamento ottenute da banche, obbligazionisti e altri creditori. Comportano un costo esplicito sotto forma di interessi ($r_D$), richiedono rimborsi programmati, godono di priorità rispetto agli azionisti nella distribuzione dei flussi e comportano un rischio minore rispetto all'equity.
>
> Il costo medio ponderato del capitale (WACC) combina il costo dell'equity e il costo del debito, pesati per il loro peso relativo nella struttura finanziaria:
>
> $$WACC = r_E \, \frac{E}{E+D} + r_D (1-t_c)\, \frac{D}{E+D}$$
>
> dove $r_D(1-t_c)$ è il costo del debito al netto dello scudo fiscale (l'aliquota $t_c$ riduce il costo effettivo del debito perché gli interessi passivi sono deducibili).
>
> - $r_E$ si stima tramite il **CAPM**.
> - $r_D$ corrisponde al tasso a cui l'impresa ottiene i propri prestiti (**tasso prestiti**).

*(slide 3–4)*

## L'aliquota fiscale da impiegare nella valutazione

> [!abstract] Definizione
> L'aliquota fiscale da utilizzare nella valutazione dipende dal contesto di impiego:
>
> | Contesto | Aliquota da utilizzare |
> |---|---|
> | **Margini** (es. calcolo del NOPAT sui margini operativi) | IRES (24%) + IRAP (3,9%) |
> | **WACC** (per lo scudo fiscale sugli interessi passivi) | Solo IRES (24%), perché è l'imposta che consente la deduzione degli interessi passivi |
>
> Negli esempi pratici si usano queste aliquote, ma resta comunque una semplificazione del carico fiscale effettivo della società.

*(slide 5)*

## Il costo del debito ($R_d$)

> [!abstract] Definizione
> $R_d$ rappresenta il rendimento richiesto dai finanziatori che prestano denaro all'impresa: banche, obbligazionisti, istituzioni finanziarie.
>
> Il creditore si aspetta un rendimento che compensi il valore del tempo e il rischio che l'impresa non rimborsi il finanziamento. Tale rendimento è il **tasso di interesse effettivo del prestito**.
>
> **Esempio numerico.** Un'azienda chiede un finanziamento di €1m al 5% annuo: $R_d = 5\%$.
>
> Con l'effetto fiscale (IRES 24%), l'onere effettivo diventa:
>
> $$R_d^{post\text{-}tax} = 5\% \times (1-24\%) = 3{,}8\%$$
>
> (Scudo fiscale: gli interessi passivi sono deducibili.)
>
> **Più finanziamenti contemporanei.** Quando un'azienda ha più finanziamenti, $R_d$ diventa la media ponderata del costo di tutti i debiti, pesata in base al valore di ciascun finanziamento: *"se l'impresa si finanzia con prestiti diversi, qual è il costo del suo debito?"* — si deve considerare sia il tasso, sia il peso di ogni debito nella struttura complessiva.
>
> $$R_d = \frac{\sum (Debito_i \times tasso_i)}{\sum Debito_i}$$
>
> $$R_d^{post\text{-}tax} = R_d \times (1-T)$$

*(slide 6–7)*

## Il costo del capitale proprio ($R_e$): definizione e caratteristiche

> [!abstract] Definizione
> $R_e$ rappresenta il rendimento che l'azionista si aspetta dall'investimento nell'impresa. L'azionista si espone al rischio dell'azienda e pretende un compenso adeguato. $R_e$ è l'obiettivo di rendimento che l'impresa deve garantire ai suoi proprietari affinché accettino di investire capitale rischioso.
>
> **Caratteristiche dell'equity:**
>
> - Il «capitale proprio» (Equity) non ha garanzie.
> - Assorbe i rischi operativi, finanziari e di mercato; riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti.
> - Nella pratica, quasi sempre $R_e$ risulta più elevato del costo del debito.

*(slide 8)*

## Il CAPM per la stima del costo del capitale proprio

> [!abstract] Definizione
> Il Capital Asset Pricing Model (CAPM) è il modello utilizzato per determinare il costo del capitale proprio:
>
> $$r_E = r_f + \beta (R_m - r_f)$$
>
> Interpretazione di ciascuna componente:
>
> | Componente | Significato | Interpretazione intuitiva |
> |---|---|---|
> | $r_E$ — Costo capitale proprio | Rendimento richiesto dagli investitori | — |
> | $r_f$ — Tasso privo di rischio | Remunerazione base | "Valore del tempo" |
> | $\beta$ — Moltiplicatore rischio sistematico | Sensibilità del titolo al rischio di mercato | "Quantità di rischio" |
> | $(R_m - r_f)$ — Premio per il rischio di mercato | Extra-rendimento richiesto per investire in azioni | "Prezzo del rischio" |
>
> Il termine $\beta (R_m - r_f)$ nel suo complesso costituisce il **premio per il rischio**.

*(slide 9)*

## Il rischio Paese: due alternative di trattamento nel CAPM

Il «rischio Paese» è la componente di rischiosità del Paese a cui l'investimento si riferisce: se l'azienda o il progetto valutato sono situati in Italia, si ragiona sulla «rischiosità» dell'Italia.

Nel CAPM, il premio per il rischio Paese può essere considerato in due modi alternativi, entrambi corretti purché applicati con coerenza:

- **Alternativa 1** — caricare il «rischio Paese» **nel tasso privo di rischio** ($r_f$).
- **Alternativa 2** — caricare il «rischio Paese» **nel premio per il rischio** di mercato.

> L'importante è la coerenza! Entrambi gli approcci sono corretti.

**Da cosa dipende il «rischio Paese»:**

- solidità dei conti pubblici;
- livello del debito sovrano;
- affidabilità delle istituzioni;
- stabilità politica;
- efficienza del sistema giudiziario;
- qualità delle infrastrutture;
- rating del Paese;
- spread sovrano e CDS.

**Figura** — Mappa mondiale del *Country Risk Assessment* di Coface ("160 countries under the magnifying glass"), con classificazione dei Paesi su scala da A1 (rischio molto basso) a E (rischio estremo), basata su expertise macroeconomica, comprensione del contesto di business e dati microeconomici raccolti su 70 anni di esperienza di pagamento. La mappa mostra che i Paesi del Nord Europa (inclusa la Germania, classificata A3 nell'area evidenziata) e Nord America presentano rating di rischio Paese più bassi rispetto a molte economie di Africa, Asia e Sud America; se ne trae la conclusione che il rischio Paese varia sensibilmente a livello globale e va quantificato Paese per Paese ai fini della valutazione.

*(slide 10–13)*

## Il tasso privo di rischio ($r_f$): definizione e riferimenti da utilizzare

> [!abstract] Definizione
> **Quale riferimento usare per il tasso «risk free»?**
>
> Si utilizza il tasso dei bond governativi a rischio minimo nel Paese/area di riferimento dell'impresa da valutare (il più prossimo in termini geografici).
>
> **Esempio:** per la valutazione delle imprese italiane si utilizza il **Bund tedesco a 10 anni** (es. 2,20%).
>
> > **Attenzione:** i BTP italiani NON sono «risk free»! Il loro tasso di rendimento incorpora già il rischio Paese «Italia».
>
> **Figura** — Tabella "Ten year government bond spreads": elenco di rendimenti dei titoli di stato decennali di numerosi Paesi (tra cui Germania e Italia, evidenziati) con il relativo spread rispetto al Bund tedesco. La tabella illustra visivamente come il rendimento del BTP italiano risulti superiore a quello del Bund tedesco proprio per effetto del rischio Paese incorporato, a conferma del punto precedente; i valori numerici non sono riportati qui poiché non presenti nel testo estratto del documento.

*(slide 14–15)*

## Applicazione dell'Alternativa 1: il rischio Paese caricato nel tasso privo di rischio

> [!example] Esempio
> Utilizzando l'**Alternativa 1**, il «rischio Paese» viene caricato nel tasso privo di rischio. Si ottengono quindi i due elementi del CAPM come segue:
>
> - **Tasso privo di rischio** = bond governativi nel Paese di riferimento dell'impresa da valutare (ITA BTP 10 anni = es. **4,40%**).
> - **Premio per il rischio di mercato** = premio per il rischio base, calcolato su Paesi con rischio Paese minimo (esempio gli U.S.A. con **4,12%**).

*(slide 16)*

## Applicazione dell'Alternativa 2: scomposizione del premio per il rischio di mercato in MRP e Country Risk Premium

> [!abstract] Definizione
> Con l'**Alternativa 2**, il premio per il rischio di mercato è formato da due componenti:
>
> **a) «MRP – Market Risk Premium» (premio rischio "base")**
>
> Il Market Risk Premium (MRP) rappresenta il premio che un investitore richiede per investire nel mercato azionario invece che in un titolo privo di rischio.
>
> - Si calcola sui mercati con rischio Paese molto contenuto (tipicamente U.S.A.).
> - Riflette il rischio sistematico globale, non specifico del Paese.
> - Deriva da serie storiche di rendimenti azionari e obbligazionari.
> - Viene aggiornato annualmente da Damodaran.
>
> **b) «Country Risk Premium» (spread rischio Paese specifico)**
>
> - Il CDS Italia (Credit Default Swap sul debito sovrano) misura il rischio percepito dagli investitori che lo Stato italiano possa non onorare i suoi impegni finanziari.
> - Da questo tasso si ricava il Country Risk Premium (CRP), cioè il premio specifico richiesto per investire in un Paese con rischiosità superiore a quella dei Paesi benchmark.
> - Riflette la percezione sul debito pubblico, le condizioni politiche ed economiche.
> - È comparabile allo spread.
> - Viene trasformato in Country Risk Premium tramite moltiplicazione per un coefficiente che corregge la volatilità relativa.
>
> In sintesi:
>
> | Componente | Descrizione | Fonte tipica |
> |---|---|---|
> | MRP (premio rischio "base") | Premi rischio mercato su Paesi con rischio Paese molto basso (esempio: U.S.A.) | Damodaran (2024) → **4,12%** (ERP – Equity Risk Premium) |
> | Country Risk Premium (CRP) | CDS/spread rating Paese "azionarizzati" (equiparabile allo «spread») | Country Risk Premium (CDS ITA), Damodaran (2024) → **1,08%** |
>
> **Totale premio per il rischio di mercato (Italia) = 4,12% + 1,08% = 5,20%**

*(slide 17–18)*

## Esempio "Italia": confronto tra i due metodi di stima di $r_E$

> [!example] Esempio
> Applicando il CAPM $r_E = r_f + \beta(R_m - r_f)$ secondo le due alternative viste, si ottengono due formulazioni equivalenti:
>
> **1° metodo (Alternativa 1 — rischio Paese nel tasso privo di rischio):**
>
> $$r_E = r_{BTP\ Italia} + \beta \, (MRP_{U.S.A.})$$
>
> con $r_{BTP\ Italia} = 4{,}40\%$ (tasso privo di rischio comprensivo del rischio Paese) e $MRP_{U.S.A.} = 4{,}12\%$ (mercato a rischio minimo).
>
> **2° metodo (Alternativa 2 — rischio Paese nel premio per il rischio):**
>
> $$r_E = r_{Bund\ tedesco} + \beta \, (MRP_{U.S.A.} + Premio\ Italia)$$
>
> con $r_{Bund\ tedesco} = 2{,}20\%$ (tasso risk free "puro"), $MRP_{U.S.A.} = 4{,}12\%$ (mercato a rischio minimo) e $Premio\ Italia = 1{,}08\%$ (rischio Italia, il Country Risk Premium).
>
> **Conclusione:** i risultati dei due metodi tendono a convergere, cioè producono una stima di $r_E$ sostanzialmente equivalente, indipendentemente da dove venga "allocato" contabilmente il rischio Paese all'interno della formula del CAPM.

*(slide 19–20)*

## Il coefficiente Beta: definizione e calcolo

> [!abstract] Definizione
> Il **Beta** misura quanto varia il rendimento di un titolo al variare del rendimento di mercato:
>
> $$\beta = \frac{COV(R_t; R_m)}{VAR(R_m)}$$
>
> - La **covarianza** rappresenta una sorta di "correlazione" tra i rendimenti del mercato e quelli del titolo valutato.
> - La **varianza** esprime la variabilità dei rendimenti di mercato.
>
> **Calcolo pratico:** si utilizzano i rendimenti di mercato (es. FTSE MIB o S&P) e i rendimenti del titolo, calcolati su base giornaliera o settimanale, relativi agli ultimi due/cinque anni.

*(slide 21)*

## I fattori che influenzano il Beta

Il Beta dipende da due tipologie di rischio (con Beta > 1 tipicamente associato a):

- **Livelli di rischio operativo** (rapporto tra costi fissi e costi variabili).
- **Livelli di rischio finanziario** (leverage, cioè il grado di indebitamento).

Mentre la ciclicità dei ricavi e il livello di rischio operativo possono presentare difformità più contenute tra imprese dello stesso settore, **il rischio finanziario può essere sensibilmente diverso** — problema tipicamente italiano legato alla sottocapitalizzazione delle PMI.

Di conseguenza, quando si confrontano i Beta di imprese comparabili con strutture finanziarie diverse, è necessaria una **rettifica per la leva finanziaria** (per "spogliare" il Beta osservato dall'effetto del diverso indebitamento e renderlo confrontabile).

*(slide 22)*
