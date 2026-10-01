---
title: "Risk Management: il framework di Enterprise Risk Management e la valutazione forward-looking del rischio"
tags:
  - corso/misurazione-rischio
  - tipo/lezione
corso: "[[Misurazione Rischio]]"
source: "MDR_Slide_risk-management-framework.pdf"
pages: 5
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione

Lezione di **Risk Management** tenuta da Andrea Giacomelli (Università Ca' Foscari Venezia). Il materiale introduce il framework di Enterprise Risk Management (ERM) e propone un approccio *forward-looking* alla valutazione del rischio, esteso poi al tema della doppia materialità (finanziaria e di impatto) e confrontato con l'approccio tradizionale frequenza-severità.

*(slide 1)*

## Il framework di Enterprise Risk Management (ERM)

> [!abstract] Definizione
> **Definizione (ERM framework).** Un framework di Enterprise Risk Management deve includere politiche, procedure, limiti di rischio e controlli di rischio che assicurino una identificazione, misurazione, monitoraggio, gestione, mitigazione e reporting dei rischi adeguati, tempestivi e continui, a livello di business line, di istituzione e su base consolidata o sub-consolidata.
>
> *(Fonte: FINAL REPORT ON GUIDELINES ON INTERNAL GOVERNANCE, EBA 2021)*
>
> Nell'ambito del framework ERM, la valutazione del rischio (*risk assessment*) si articola in **4 passi principali**:
>
> - **Step 1 – Risk Identification**: identificare i fattori di rischio che influenzano in modo significativo i KPI dell'impresa. Nell'identificare i rischi, l'impresa deve considerare sia una prospettiva *forward-looking* (prospettica) sia una *backward-looking* (retrospettiva).
>
> - **Step 2 – Risk Measurement**: stimare il profilo di rischio dei KPI dell'impresa, cioè il range di valori potenziali dei KPI influenzati dai fattori di rischio. Nel misurare i rischi, l'impresa deve sviluppare metodologie appropriate che includano sia la prospettiva forward-looking sia quella backward-looking.
>   Il profilo di rischio si basa sulla stima di:
>   - probabilità di accadimento dei fattori di rischio;
>   - severità dei KPI dell'impresa colpiti dall'accadimento dei fattori di rischio.
>
> - **Step 3 – Risk Appetite Statement**: stabilire limiti interni coerenti con la propensione al rischio (*risk appetite*) dell'impresa e commisurati alla sua solidità operativa, forza finanziaria, base patrimoniale (*Risk Capacity*) e obiettivi strategici.
>
> - **Step 4 – Risk Monitoring**: valutare il profilo di rischio a confronto con il risk appetite dell'impresa e con la sua risk capacity (il profilo di rischio deve essere mantenuto entro i limiti stabiliti nel Risk Appetite Statement).
>
> Questi quattro passi si riassumono nella relazione:
>
> $$\text{Risk Profile} \leq \text{Risk Appetite} \leq \text{Risk Capacity}$$

*(slide 2)*

## Valutazione forward-looking del rischio: schema generale

> [!abstract] Definizione
> Lo schema generale della valutazione forward-looking del rischio collega quattro elementi tramite altrettante trasformazioni funzionali, secondo una catena causale che va dal fattore di rischio fino all'impatto sugli stakeholder, con un meccanismo di retroazione (feedback).
>
> **Elementi della catena:**
>
> 1. **Risk Factor** $X$: il fattore di rischio, caratterizzato da una distribuzione di probabilità sul dominio dell'intensità di rischio (*Risk intensity Domain X*).
>
> 2. **Firm KPI (ESG & financial): Severity**, definito come
>    $$Y = h(X)$$
>    cioè il KPI dell'impresa (di natura sia ESG sia finanziaria) come funzione del fattore di rischio. È rappresentato da una distribuzione degli scostamenti (*deviations distribution*) sul dominio del KPI (*KPI Domain Y*), attorno a un valore obiettivo (*Target*), entro un intervallo detto **corridoio degli scostamenti** (*deviations corridor*, delimitato da *Target* e *Deviations*).
>
> 3. **Criticality of impacts on stakeholders**, definita come
>    $$W = g(Y)$$
>    cioè l'impatto sugli stakeholder in funzione dello scostamento del KPI. È rappresentato da una distribuzione sul dominio degli impatti (*Impacts domain W*). Su questo dominio viene individuata la **probabilità di impatti critici** (*probability of critical impacts*): gli impatti entro il target e gli scostamenti attesi sono contrassegnati come accettabili (✓✓✓✓✓), mentre quelli oltre una **soglia** (*threshold*) — corrispondente al risk appetite / risk capacity — sono contrassegnati come **impatti critici** (✗✗).
>
> 4. **Feedback**: un nuovo fattore di rischio, innescato dagli impatti sugli stakeholder, secondo
>    $$X = v(W)$$
>    Questo chiude il ciclo: gli impatti critici generati da un fattore di rischio possono generare essi stessi un nuovo fattore di rischio, alimentando iterativamente il processo di valutazione.
>
> **Figura (pag. 3)** — Schema a blocchi con tre distribuzioni di probabilità in cascata (fattore di rischio → KPI d'impresa → impatti sugli stakeholder) collegate dalle funzioni $Y=h(X)$ e $W=g(Y)$, più una freccia di retroazione $X=v(W)$ che riporta gli impatti critici a diventare un nuovo fattore di rischio. Il grafico mostra come, muovendo dal dominio X al dominio W, l'informazione probabilistica (l'intera forma della distribuzione, non solo il suo valore atteso) venga propagata lungo la catena, permettendo di individuare la probabilità di superare una soglia critica (risk appetite/risk capacity) anziché il solo valore medio.

*(slide 3)*

## Doppia materialità (Double Materiality)

> [!abstract] Definizione
> Lo schema generale forward-looking (pag. 3) viene esteso al concetto di **doppia materialità**, distinguendo due percorsi paralleli a partire dallo stesso fattore di rischio $X$:
>
> - **Financial materiality** (materialità finanziaria): il fattore di rischio ESG $X$ (con la propria distribuzione di probabilità sul dominio dell'intensità del fattore di rischio ESG, *ESG Factor Risk intensity Domain X*) genera un impatto sul **Financial KPI**, tramite
>   $$Y_{\text{fin}} = h(X)$$
>   rappresentato dalla distribuzione degli scostamenti del KPI finanziario (*Financial KPI: deviations distribution*), con relativo target e corridoio degli scostamenti (*Deviations corridor*).
>
> - **Impact materiality** (materialità di impatto): lo stesso fattore di rischio $X$ genera un impatto sul **ESG KPI**, tramite
>   $$Y_{\text{ESG}} = h(X)$$
>   rappresentato dalla distribuzione degli scostamenti del KPI ESG (*ESG KPI: deviations distribution*), anch'essa con target e corridoio degli scostamenti proprio.
>
> In entrambi i rami, lo scostamento del KPI (finanziario o ESG) genera un impatto sugli stakeholder secondo
> $$W = g(Y)$$
> con la relativa distribuzione sul dominio degli impatti (*Impacts domain W*), la soglia critica (*threshold*, risk appetite/risk capacity) e la marcatura degli impatti accettabili (✓✓✓✓✓) rispetto a quelli critici (✗✗), esattamente come nello schema generale.
>
> Infine, i due rami convergono in un unico meccanismo di **feedback**: un nuovo fattore di rischio innescato dagli impatti sugli stakeholder, secondo
> $$X = v(W)$$
>
> **Figura (pag. 4)** — Schema a due colonne parallele ("FINANCIAL MATERIALITY" a sinistra e "IMPACT MATERIALITY" a destra), entrambe originate dallo stesso fattore di rischio ESG $X$ e convergenti in un'unica freccia di feedback $X=v(W)$. La figura mostra che un unico fattore di rischio ESG produce simultaneamente un effetto sui risultati finanziari dell'impresa (materialità finanziaria, la prospettiva "outside-in": come l'ESG impatta l'impresa) e un effetto sugli stakeholder esterni tramite il KPI ESG (materialità di impatto, la prospettiva "inside-out": come l'impresa impatta l'ambiente/società), e che entrambi i percorsi possono retroagire generando nuovi fattori di rischio.

*(slide 4)*

## Confronto con l'approccio tradizionale frequenza-severità

> [!example] Esempio
> Questa sezione confronta l'approccio forward-looking basato su distribuzioni di probabilità (schema delle pagine 3-4) con il tradizionale **approccio frequenza-severità** (*Frequency-severity Approach*), utilizzando lo stesso esempio numerico applicato a un fattore di rischio ESG.
>
> **Approccio forward-looking (a sinistra nella figura).**
> Il fattore di rischio ESG $X$ ha una distribuzione di probabilità continua sul dominio dell'intensità del rischio (*ESG Factor Risk intensity Domain X*), con valori di riferimento sull'asse pari a **64** e **120**.
> Questo fattore genera, tramite $Y=h(X)$, una distribuzione degli scostamenti del KPI finanziario (*Financial KPI: deviations distribution*) sul dominio $Y$, con valori di riferimento sull'asse pari a:
>
> | Valore 1 | Valore 2 | Valore 3 | Valore 4 | Valore 5 | Valore 6 | Valore 7 |
> |---|---|---|---|---|---|---|
> | 0 | 0 | 0 | 0 | 40 | 40 | 400 |
>
> Da questa distribuzione si ricava la **perdita attesa** (*expected loss*), calcolata come valore atteso sull'intera distribuzione dei possibili scostamenti del KPI finanziario.
>
> **Approccio frequenza-severità (a destra nella figura).**
> L'approccio tradizionale semplifica il fenomeno in due soli stati:
> - l'evento di rischio **non si verifica** (*Risk event doesn't occur*), con KPI finanziario pari a **0**;
> - l'evento di rischio **si verifica** (*Risk event occurs*), con probabilità **35%** e KPI finanziario pari a **220**.
>
> La perdita attesa si calcola quindi come:
> $$\text{Expected loss} = \text{frequency} \times \text{severity} = 0.35 \times 220 = 77$$
>
> **Limiti dell'approccio frequenza-severità.** Rispetto all'approccio forward-looking basato sull'intera distribuzione di probabilità, l'approccio frequenza-severità:
>
> - ✓ non coglie le diverse intensità del fattore di rischio, e quindi non coglie i loro effetti differenziati;
> - ✓ considera solo la severità attesa, quindi non coglie le severità critiche che l'impresa deve affrontare e gestire;
> - ✓ non consente di individuare alcuna soglia di resilienza (*resilience threshold*), legata alle severità critiche, a supporto dei processi decisionali.
>
> **Figura (pag. 5)** — Confronto grafico fra la distribuzione completa del fattore di rischio ESG e del KPI finanziario (approccio forward-looking, colonna di sinistra) e la rappresentazione binaria "evento non accade / evento accade con probabilità 35%" tipica dell'approccio frequenza-severità (colonna di destra). La figura mostra come il modello a distribuzione completa preservi informazione su intensità e severità critiche (e quindi sulla probabilità di superare una soglia di resilienza), mentre il modello frequenza-severità la comprima in un singolo numero atteso (77), perdendo la possibilità di individuare impatti critici e soglie di risk appetite/risk capacity.

*(slide 5)*
