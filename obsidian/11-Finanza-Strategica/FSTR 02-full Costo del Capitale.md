---
title: "Le decisioni di investimento per l'impresa indebitata: il costo del capitale"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_02-full_Costo-del-Capitale.pdf"
pages: 25
text_layer: true
verified: true
generated: 2026-08-30
---

## Introduzione e argomenti del corso

**Titolo del modulo:** Strategie di investimento — *Le decisioni di investimento per l'impresa indebitata: il costo del capitale*.

**Letture di riferimento:** Capitolo 7.3 fino a equazione 7.21 del testo di BBS.

**Argomenti del corso** (il presente modulo copre il primo punto):

1. Le decisioni di investimento per l'impresa indebitata
2. Dal valore degli investimenti al valore d'impresa (I): i metodi DCF
3. Dal valore degli investimenti al valore d'impresa (II): i multipli di borsa
4. Crescita esterna e valore delle operazioni di integrazione

*(slide 1–2)*

## La determinazione dell'appropriato tasso di sconto per un progetto: struttura Assets/Equity/Debts e WACC

> [!abstract] Definizione
> Il bilancio dell'impresa può essere letto, dal lato del passivo, come somma di due fonti di finanziamento con rischio e rendimento richiesto diversi.
>
> **ASSETS** — insieme dei beni e delle risorse economiche dell'azienda: impianti, macchinari, immobili, brevetti, capitale circolante, competenze, tecnologia. Sono gli elementi che permettono all'azienda di produrre beni, erogare servizi e generare flussi di cassa. Il tasso di sconto complessivo applicato agli assets è il **WACC**.
>
> **EQUITY** ($r_E$) — rappresenta la proprietà dell'azienda, che sopporta l'intero rischio residuo della gestione. Riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti. Pretende un rendimento adeguato al rischio assunto ($r_E$).
>
> **DEBTS** ($r_D$) — tutte le forme di finanziamento ottenute da banche, obbligazionisti e altri creditori. Comportano un costo esplicito sotto forma di interessi ($r_D$), richiedono rimborsi programmati, godono di priorità rispetto agli azionisti nella distribuzione dei flussi e comportano un rischio minore rispetto all'equity.
>
> La formula del costo medio ponderato del capitale (WACC) è:
>
> $$WACC = r_E\,\frac{E}{E+D} + r_D(1-t_c)\,\frac{D}{E+D}$$
>
> dove $r_E$ si determina tramite il **CAPM** e $r_D$ corrisponde al tasso richiesto sui prestiti (tasso prestiti).

*(slide 3–4)*

## L'aliquota fiscale: alcuni richiami

L'aliquota fiscale da impiegare nella valutazione dipende dal contesto d'uso:

- **Nei margini** (es. EBIT, flussi operativi): si utilizza IRES (24%) + IRAP (3,9%).
- **Nel WACC**: si utilizza l'imposta che deduce gli interessi passivi, cioè la sola IRES (24%), poiché lo scudo fiscale del debito agisce specificamente sull'IRES.

Negli esempi pratici si usano queste aliquote, ma è pur sempre una semplificazione del carico fiscale effettivo della società.

*(slide 5)*

## Il costo del debito ($R_d$)

> [!abstract] Definizione
> $R_d$ rappresenta il rendimento richiesto dai finanziatori che prestano denaro all'impresa: banche, obbligazionisti, istituzioni finanziarie.
>
> Il creditore si aspetta un rendimento che compensi il valore del tempo e il rischio che l'impresa non rimborsi il finanziamento. Tale rendimento è il **tasso di interesse effettivo del prestito**.
>
> **Esempio numerico.** Un'azienda chiede un finanziamento di €1m al 5% annuo: $R_d = 5\%$. Con l'effetto fiscale (IRES 24%) l'onere effettivo diventa:
>
> $$R_d^{\,post\text{-}tax} = 5\% \times (1-24\%) = 3{,}8\%$$
>
> Questo perché gli interessi passivi sono deducibili (scudo fiscale).
>
> **Caso di più finanziamenti.** Quando un'azienda ha più fonti di debito, $R_d$ diventa la media ponderata del costo di tutti i debiti, pesata in base al valore di ciascun finanziamento:
>
> $$R_d = \frac{\sum (Debito_i \times tasso_i)}{\sum Debito_i}$$
>
> $$R_d^{\,post\text{-}tax} = R_d \times (1-T)$$
>
> In sintesi: per determinare il costo del debito complessivo occorre considerare sia il tasso sia il peso di ciascun debito nella struttura finanziaria complessiva.

*(slide 6–7)*

## Il costo del capitale proprio ($R_e$): definizione e caratteristiche

> [!abstract] Definizione
> $R_e$ rappresenta il rendimento che l'azionista si aspetta dall'investimento nell'impresa. L'azionista si espone al rischio dell'azienda e pretende un compenso adeguato: $R_e$ è l'obiettivo di rendimento che l'impresa deve garantire ai suoi proprietari affinché accettino di investire capitale rischioso.
>
> **Caratteristiche:**
>
> - Il «capitale proprio» (Equity) non ha garanzie.
> - Assorbe i rischi operativi, finanziari e di mercato; riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti.
> - Nella pratica, quasi sempre $R_e$ risulta più elevato del costo del debito.

*(slide 8)*

## La determinazione del costo del capitale proprio: il CAPM

> [!abstract] Definizione
> Il Capital Asset Pricing Model (CAPM) scompone il costo del capitale proprio in quattro componenti:
>
> $$r_E = r_f + \beta\,(R_m - r_f)$$
>
> | Componente | Nome | Interpretazione |
> |---|---|---|
> | $r_E$ | Costo capitale proprio | Rendimento richiesto dagli investitori |
> | $r_f$ | Tasso privo di rischio | "Valore del tempo" |
> | $\beta$ | Moltiplicatore rischio sistematico | "Quantità di rischio" |
> | $(R_m - r_f)$ | Premio per il rischio di mercato | "Prezzo del rischio" |
>
> Il termine $\beta(R_m - r_f)$ nel suo insieme costituisce il **premio per il rischio**.

*(slide 9)*

## Il tasso privo di rischio e il premio per il rischio di mercato: il rischio Paese

Nella costruzione del CAPM occorre decidere come trattare il **«rischio Paese»**, ossia la componente di rischiosità del Paese a cui si riferisce l'investimento. Se l'azienda o il progetto valutato sono situati in Italia, si ragionerà sulla «rischiosità» dell'Italia.

Esistono due modi equivalenti di considerarlo, purché applicati in modo coerente:

- **Alternativa 1** — caricare il «rischio Paese» nel tasso privo di rischio.
- **Alternativa 2** — caricare il «rischio Paese» nel premio per il rischio.

> L'importante è la coerenza! Entrambi gli approcci sono corretti.

**Da cosa dipende il «rischio Paese»:**

- solidità dei conti pubblici
- livello del debito sovrano
- affidabilità delle istituzioni
- stabilità politica
- efficienza del sistema giudiziario
- qualità delle infrastrutture
- rating del Paese
- spread sovrano e CDS

**Figura — "160 countries under the magnifying glass" (Coface, Country Risk Assessment).** Mappa mondiale che colora ciascun Paese secondo una scala di rischio da A1 (very low) a E (extreme), con indicazione di upgrade/downgrade recenti. La figura illustra visivamente come il rischio Paese vari fortemente da regione a regione (es. Nord America ed Europa occidentale in fascia di rischio basso, ampie aree di Africa, Sud America e Asia in fasce di rischio più elevato), giustificando la necessità di includere una componente di rischio Paese specifica nel costo del capitale quando si valutano investimenti fuori dai mercati a rischio minimo.

*(slide 10–13)*

## Definizione del tasso privo di rischio ($r_f$)

> [!abstract] Definizione
> **Quale riferimento usare per il tasso «risk free»?**
>
> Si utilizza il tasso dei bond governativi a rischio minimo nel Paese/area di riferimento dell'impresa da valutare (il più prossimo in termini geografici). Ad esempio, per la valutazione delle imprese italiane si usa il **Bund tedesco a 10 anni** (es. 2,20%).
>
> > **Attenzione:** i BTP italiani NON sono «risk free»! Il loro tasso di rendimento incorpora già il rischio Paese «Italia».
>
> **Figura — "Ten year government bond spreads".** Tabella che riporta, per un insieme di Paesi (tra cui Germania e Italia evidenziate), il rendimento più recente del bond governativo decennale e il relativo spread rispetto al Bund tedesco. La tabella mostra concretamente che il rendimento del BTP italiano include uno spread positivo rispetto al Bund tedesco, a conferma che il Bund (spread ≈ 0 per definizione) è il riferimento più adatto come tasso privo di rischio per le imprese italiane, mentre il BTP incorpora già un premio per il rischio Paese.
>
> **Applicazione — Alternativa 1** (rischio Paese caricato nel tasso privo di rischio): si utilizzano allora due elementi distinti nel CAPM:
>
> - Bond governativi del Paese di riferimento dell'impresa da valutare come tasso privo di rischio comprensivo di rischio Paese (esempio: BTP Italia 10 anni = 4,40%);
> - come rischio di mercato, il **premio per il rischio base**, cioè il premio dei Paesi con rischio Paese minimo (esempio: U.S.A. con 4,12%).

*(slide 14–16)*

## Il premio per il rischio di mercato: MRP e Country Risk Premium

> [!abstract] Definizione
> **Applicazione — Alternativa 2**: il premio per il rischio di mercato è formato da due componenti.
>
> **«MRP – Market Risk Premium» (premio rischio "base")**
>
> Rappresenta il premio che un investitore richiede per investire nel mercato azionario invece che in un titolo privo di rischio.
>
> - Si calcola sui mercati con rischio Paese molto contenuto (tipicamente U.S.A.).
> - Riflette il rischio sistematico globale, non specifico del Paese.
> - Deriva da serie storiche di rendimenti azionari e obbligazionari.
> - Viene aggiornato annualmente da Damodaran.
> - Corrisponde ai premi rischio mercato calcolati su Paesi con rischio Paese molto basso (es. U.S.A.).
>
> **«Country Risk Premium» (spread rischio Paese specifico)**
>
> - Il CDS Italia (Credit Default Swap sul debito sovrano) misura il rischio percepito dagli investitori che lo Stato italiano possa non onorare i suoi impegni finanziari.
> - Da questo tasso si ricava il Country Risk Premium (CRP), cioè il premio specifico richiesto per investire in un Paese con rischiosità superiore a quella dei Paesi benchmark.
> - Riflette la percezione sul debito pubblico, le condizioni politiche ed economiche; è comparabile allo spread.
> - Viene trasformato in Country Risk Premium tramite moltiplicazione per un coefficiente che corregge la volatilità relativa (CDS/spread rating Paese "azionarizzati", equiparabile allo «spread»).
>
> **Valori numerici (Damodaran, 2024):**
>
> - ERP – Equity Risk Premium (MRP U.S.A.): **4,12%**
> - Country Risk Premium (CDS ITA), Damodaran (2024): **1,08%**
> - Totale = 4,12% + 1,08% = **5,20%**

*(slide 17–18)*

## Esempio applicativo: il costo del capitale proprio per l'Italia

> [!example] Esempio
> Applicando il CAPM $r_E = r_f + \beta(R_m - r_f)$ al caso di un'impresa italiana, i due approcci (Alternativa 1 e Alternativa 2) si formulano così:
>
> **1° metodo** (rischio Paese nel tasso privo di rischio):
>
> $$r_E = \underbrace{r_{\text{BTP Italia}}}_{4{,}40\%} + \beta\,\underbrace{(\text{MRP U.S.A.})}_{4{,}12\%}$$
>
> dove il BTP Italia funge da tasso privo di rischio comprensivo di rischio Paese, e il premio di mercato è quello di un mercato a rischio minimo (U.S.A.).
>
> **2° metodo** (rischio Paese nel premio per il rischio):
>
> $$r_E = \underbrace{r_{\text{Bund tedesco}}}_{2{,}20\%} + \beta\,\underbrace{(\text{MRP U.S.A.} + \text{Premio Italia})}_{4{,}12\%\ +\ 1{,}08\%}$$
>
> dove il Bund tedesco è il tasso risk free "puro", il premio di mercato è quello di un mercato a rischio minimo (U.S.A.) a cui si somma il rischio Italia (Premio Italia = 1,08%).
>
> **Conclusione:** i risultati dei due metodi tendono a convergere, poiché la stessa componente di rischio Paese viene semplicemente allocata in un punto diverso della formula (nel tasso risk-free oppure nel premio per il rischio).

*(slide 19–20)*

## Il coefficiente Beta

> [!abstract] Definizione
> Il **Beta** misura quanto varia il rendimento di un titolo al variare del rendimento di mercato:
>
> $$\beta = \frac{COV(R_t; R_m)}{VAR(R_m)}$$
>
> dove la covarianza rappresenta una sorta di "correlazione" tra i rendimenti del mercato e quelli del titolo valutato, mentre la varianza esprime la variabilità dei rendimenti di mercato.
>
> **Calcolo:** si utilizzano i rendimenti di mercato (es. FTSE MIB o S&P) e del titolo su base giornaliera/settimanale degli ultimi due/cinque anni.
>
> **Da cosa è influenzato il Beta.** Il Beta dipende da:
>
> - livelli di rischio operativo (costi fissi – variabili);
> - livelli di rischio finanziario (leverage).
>
> Mentre la ciclicità dei ricavi e il livello di rischio operativo possono presentare difformità più contenute tra imprese dello stesso settore, il **rischio finanziario può essere sensibilmente diverso** (è il tipico problema italiano della sottocapitalizzazione delle PMI). Per questo motivo, nei confronti tra imprese con leva finanziaria diversa, si applica una **rettifica per la leva finanziaria** (si veda la sezione sul Beta unlevered).
>
> **Valori del Beta e interpretazione settoriale:**
>
> | Valore | Interpretazione | Esempi di settore |
> |---|---|---|
> | $\beta > 1$ | Il titolo (l'azienda) varia più che proporzionalmente al variare del mercato | Settore fortemente ciclico: automotive, costruzioni, lusso e alta moda, turismo, compagnie aeree, high-tech |
> | $\beta = 1$ | Il titolo (l'azienda) varia proporzionalmente al variare del mercato | Settore ciclico al pari dell'economia: trasporti, assicurazioni |
> | $0 < \beta < 1$ | Il titolo (l'azienda) varia meno che proporzionalmente al variare del mercato (assorbe il ciclo economico) | Settore non ciclico: energie rinnovabili, utilities, farmaceutico, healthcare, gestione rifiuti, telecomunicazioni, beni di consumo primari. Caratteristiche: contratti pluriennali, tariffe regolate (utility), abbonamenti periodici |

*(slide 21–23)*

## Tasso di sconto per un progetto: criticità e Beta unlevered

> [!note] Dimostrazione
> **Criticità nell'uso di un tasso di sconto per valutare un progetto:**
>
> 1. Struttura finanziaria del progetto non nota al momento della valutazione (quanto Equity? quanto Debito?).
> 2. Impresa non quotata (difficilmente comparabile).
> 3. Il progetto potrebbe essere effettuato in un settore differente rispetto a quello in cui l'impresa solitamente opera.
>
> **Soluzione:** si utilizza un **Beta unlevered** dell'impresa o del settore in cui il progetto viene lanciato. Si ipotizza cioè che il progetto sia finanziato interamente con equity (quindi $r_{E,D=0} \to r_0$, ottenuto tramite il Beta unlevered).
>
> Questo approccio si giustifica anche perché un progetto dovrebbe essere accettato/respinto a prescindere dai benefici derivanti dalla politica finanziaria (il debito riduce il costo delle fonti di finanziamento, ma questo è un effetto della struttura finanziaria, non del progetto in sé).
>
> **Determinazione del Beta unlevered.** Il calcolo dipende dal segno della posizione finanziaria netta (NFP) dell'impresa comparabile:
>
> - **Se la posizione finanziaria netta è positiva** (Assets = Equity + Debts):
>
> $$\beta_U = \frac{\beta_L}{1 + \dfrac{NFP}{E}(1-t_c)}$$
>
> - **Se la posizione finanziaria netta è negativa** (Assets = Equity, al netto della cassa: Assets + Cash = Equity):
>
> $$\beta_U = \beta_L\,\frac{E}{E+NFP}$$
>
> In entrambi i casi, il **Beta del debito è implicitamente considerato pari a zero**.

*(slide 24–25)*
