---
title: "Teoria di portafoglio"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-02_Teoria-di-portafoglio.pdf"
pages: 127
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: obiettivi della teoria di portafoglio e definizione di portafoglio

> [!abstract] Definizione
> Corso: *Economia dei mercati ed investimenti finanziari* (EM5002), docente Stefano Colonnello, Università Ca' Foscari Venezia. Il modulo segue questo filo logico: Definizioni → Preferenze (per il rischio) → Frontiera efficiente dei titoli rischiosi → Frontiera efficiente con titolo privo di rischio → Portafoglio ottimo.
>
> **Obiettivi della teoria di portafoglio**
> - Calcolare il rendimento atteso e il rischio del portafoglio.
> - Identificare portafogli ottimali in termini di relazione tra rischio e rendimento.
> - Fornire il punto di partenza per caratterizzare l'equilibrio del mercato dei capitali, al fine di determinare il prezzo e la misura appropriata del rischio per un singolo titolo.
>
> **Alcune importanti applicazioni**
> - *Industria del risparmio gestito*: decisioni di allocazione (ad es. tra diverse classi di asset).
> - *Copertura (hedging)*: banche, società di investimento, banche d'investimento e Sgr utilizzano la teoria di portafoglio per le decisioni di investimento e per la copertura dei rischi finanziari.
> - *Gestione del rischio*: ampiamente utilizzata nel calcolo dell'esposizione al rischio di un'istituzione finanziaria (ad es. Value-at-Risk).
>
> **Che cos'è un portafoglio?**
> È un paniere di attivi (finanziari) descritto dall'elenco degli importi (o delle proporzioni della ricchezza totale, i pesi) investiti nei singoli titoli.
>
> | Titolo | Importo (EUR) | Peso |
> |---|---|---|
> | Azione A | 100 | 20% |
> | Azione B | 150 | 30% |
> | Azione C | 250 | 50% |
> | Totale | 500 | 100% |
>
> L'importo investito in un'azione può essere negativo, cioè una posizione corta (short). Si procede ora a definire come calcolare le principali metriche di portafoglio, partendo dai singoli titoli e poi aggregandole a livello di portafoglio.

*(slide 1–4)*

## Rendimenti dei titoli: definizioni e proprietà

> [!abstract] Definizione
> **Figura (pag. 5)** — Prezzi di chiusura aggiustati mensili per NVIDIA e IBM. Il grafico mostra due serie di prezzi in livelli con andamento fortemente trending: la domanda retorica posta è se sembrino stazionarie (implicitamente no, i prezzi in livelli tipicamente non lo sono).
>
> **Rendimento netto (totale) aritmetico** del titolo $i$ (pedice omesso per brevità):
> $$r_t = \frac{P_t + D - P_{t-1}}{P_{t-1}} = \frac{P_t - P_{t-1}}{P_{t-1}} + \frac{D}{P_{t-1}} = \text{Tasso di apprezzamento} + \text{Dividend yield}$$
> dove $D$ è il dividendo pagato tra $t-1$ e $t$.
>
> Rendimento lordo: $R_t = 1 + r_t = \dfrac{P_t+D}{P_{t-1}}$.
>
> **Rendimento netto (totale) logaritmico**:
> $$r_t^{*} = \ln\!\left(\frac{P_t+D}{P_{t-1}}\right)$$
>
> **Figura (pag. 7)** — Rendimenti totali (log) mensili per NVIDIA e IBM. A differenza dei prezzi in livelli, le serie dei rendimenti appaiono oscillare attorno a un valore costante: sembrano stazionarie.
>
> **Quali rendimenti utilizzare?**
> Il rendimento logaritmico è un'approssimazione lineare del rendimento netto. Sviluppo di Taylor generale di $f(x)$ intorno ad $a$:
> $$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots$$
> Applicandolo a $f(r) = \ln(1+r)$ sviluppato intorno a $r=0$:
> $$\ln(1+r) = \ln(1) + r + \dots \;\Rightarrow\; \ln(1+r) \approx r \quad \text{per } r \text{ piccolo}$$
> L'approssimazione al primo ordine funziona bene per rendimenti "piccoli" (ad es. rendimenti azionari giornalieri).
>
> I rendimenti logaritmici sono **additivi nel tempo**:
> $$r^{*}_{t+1,t+3} = r^{*}_{t+1} + r^{*}_{t+2} + r^{*}_{t+3} \;\Rightarrow\; \text{adatti ad analisi di serie storiche}$$
> I rendimenti aritmetici sono **additivi tra titoli** $\Rightarrow$ adatti ad analisi di portafoglio, argomento su cui il corso si concentra.
>
> **Additività tra titoli**. Valore di un portafoglio buy-and-hold composto da $N$ titoli al tempo $t$: $\sum_{i=1}^N n_i P_{it}$, con $n_i$ numero di azioni dell'impresa $i$ detenute. Il rendimento aritmetico del portafoglio è funzione lineare dei rendimenti dei singoli titoli:
> $$r_{pt} = \frac{\sum_{i=1}^N n_i P_{it}}{\sum_{j=1}^k n_j P_{j,t-1}} - 1 = \sum_{i=1}^k \frac{n_i P_{it}}{\sum_{j=1}^k n_j P_{j,t-1}} - 1 = \sum_{i=1}^k \frac{n_i P_{i,t-1}}{\sum_{j=1}^k n_j P_{j,t-1}}\frac{P_{it}}{P_{i,t-1}} - 1 = \sum_{i=1}^k w_{it} r_{it}$$
> I pesi di portafoglio $\mathbf{w}' = [w_{1t},\dots,w_{Nt}]$ sommano a uno e rappresentano la percentuale del portafoglio investita in ciascun titolo al tempo $t-1$:
> $$w_{it} = \frac{n_i P_{i,t-1}}{\sum_{j=1}^k n_j P_{j,t-1}}$$
>
> Le cose si complicano nel caso dei rendimenti logaritmici:
> $$r_{pt}^{*} = \ln\!\left(\frac{\sum_{i=1}^N n_i P_{it}}{\sum_{j=1}^N n_j P_{j,t-1}}\right) = \ln\!\left(\sum_{i=1}^N \frac{n_i P_{i,t-1}}{\sum_{j=1}^N n_j P_{j,t-1}}\frac{P_{it}}{P_{i,t-1}}\right) = \ln\!\left(\sum_{i=1}^N w_{it} \exp(r_{it}^{*})\right)$$
> Il rendimento logaritmico del portafoglio **non è lineare** rispetto ai rendimenti logaritmici (o aritmetici) dei singoli titoli.

*(slide 5–10)*

## Rendimento atteso, varianza e semivarianza

> [!abstract] Definizione
> **Rendimento atteso.** Poiché il rendimento di un titolo $r_i$ è una variabile casuale, se ne calcola il valore atteso; dal punto di vista finanziario è un'indicazione della redditività dell'investimento:
> $$E(r_i) = \mu_i = \sum_{s\in S} \pi_s r_{is}$$
> dove $\pi_s$ è la probabilità dello stato $s$, $r_{is}$ il rendimento del titolo $i$ se si realizza lo stato $s$, con $0\le \pi_s \le 1$ e $\sum_{s\in S}\pi_s = 1$.
>
> **Varianza (e volatilità).** Dal punto di vista finanziario, la varianza misura la rischiosità dell'investimento; è la media degli scarti quadratici rispetto alla media:
> $$var(r_i) = \sigma_i^2 = E\left[(r_{is}-E(r_i))^2\right] = \sum_{s\in S}\pi_s(r_{is}-E(r_i))^2 = E(r_i^2) - E(r_i)^2$$
> Si considera la radice quadrata della varianza, cioè la deviazione standard (volatilità):
> $$sd(r_i) = \sigma_i = \sqrt{var(r_i)}$$
> Poiché il quadrato degli scarti dalla media è sempre positivo, la deviazione standard misura la distanza media della singola osservazione dal valore medio.
>
> **Semivarianza.** Considera solo gli scarti quadratici al di sotto della media (rischio di ribasso, *downside risk*), partendo dall'idea che rendimenti superiori alla media siano desiderabili:
> $$semivar(r_i) = \sum_{s\in S} \left(\min\{0, r_{is}-E(r_i)\}\right)^2 \pi_s$$
>
> **Esempio.** Distribuzione dei rendimenti per il titolo $i$:
>
> | Stato | Prob. | $r_s$ |
> |---|---|---|
> | Boom | 0,25 | 0,3100 |
> | Rialzo | 0,45 | 0,1400 |
> | Ribasso | 0,25 | -0,0675 |
> | Crollo | 0,05 | -0,5200 |
>
> $$E(r_i) = (0{,}25)(0{,}31) + (0{,}45)(0{,}14) + (0{,}25)(-0{,}0675) + (0{,}05)(-0{,}52) = 0{,}0976$$
> $$\sigma_i^2 = 0{,}25(0{,}31-0{,}0976)^2 + 0{,}45(0{,}14-0{,}0976)^2 + 0{,}25(-0{,}0675-0{,}0976)^2 + 0{,}05(-0{,}52-0{,}0976)^2 = 0{,}038$$
> $$\sigma_i = \sqrt{0{,}038} = 0{,}1949$$
> $$semivar(r_i) = 0{,}25(0)^2 + 0{,}45(0)^2 + 0{,}25(-0{,}0675-0{,}0976)^2 + 0{,}05(-0{,}52-0{,}0976)^2 = 0{,}026$$

*(slide 11–14)*

## Covarianza e correlazione

> [!abstract] Definizione
> La **covarianza** tra i rendimenti di due titoli ($r_i$ e $r_j$) misura come i due si comportano l'uno rispetto all'altro:
> - se $r_i$ tende a essere positivo quando $r_j$ è positivo $\Rightarrow$ covarianza positiva;
> - se $r_i$ tende a essere negativo quando $r_j$ è positivo $\Rightarrow$ covarianza negativa;
> - se $r_i$ non mostra particolare tendenza quando $r_j$ è positivo $\Rightarrow$ covarianza = 0.
>
> $$cov(r_i,r_j) = \sigma_{ij} = E\left[(r_i-E(r_i))(r_j-E(r_j))\right] = \sum_{s\in S}\pi_s(r_{is}-E(r_i))(r_{js}-E(r_j)) = E(r_ir_j) - E(r_i)E(r_j)$$
>
> La covarianza di una variabile con se stessa è la sua varianza:
> $$Cov(r_i,r_i) = \sigma_{ii} = var(r_i) = \sigma_i^2$$
>
> Il coefficiente di **correlazione** tra $r_i$ e $r_j$ è il rapporto tra la covarianza e il prodotto delle deviazioni standard:
> $$\rho_{ij} = \frac{cov(r_i,r_j)}{\sigma_i \sigma_j}$$

*(slide 15–16)*

## Stima dei parametri dai rendimenti storici

> [!abstract] Definizione
> **Inferenza dai rendimenti storici.** Le vere medie e (co)varianze non sono osservabili: i possibili stati del mondo e le relative probabilità (soggettive degli investitori) sono sconosciuti. Medie e (co)varianze devono essere stimate a partire dai rendimenti realizzati, cioè occorre inferire le distribuzioni di probabilità da essi. Quando si usano dati storici, si tratta ogni osservazione come uno scenario equiprobabile:
> $$\pi_s = \frac{1}{T}$$
> dove $T$ è il numero di osservazioni nella serie storica disponibile.
>
> **Stimatori (media nota implicitamente stimata su T osservazioni)**:
> $$\hat\mu_i = \frac{1}{T}\sum_{t=1}^T r_{it} \qquad \hat\sigma_i^2 = \frac{1}{T}\sum_{t=1}^T (r_{it}-\hat\mu_i)^2 \qquad \hat{cov}(r_i,r_j) = \frac{1}{T}\sum_{t=1}^T (r_{it}-\hat\mu_i)(r_{jt}-\hat\mu_j)$$
>
> **Media geometrica.** Un modo alternativo per calcolare la media dei rendimenti storici è la media geometrica, anziché aritmetica. Valore terminale di un investimento:
> $$TV_i = V_{i0}\prod_{t=1}^T (1+r_{it})$$
> $$\bar r_{i,geom} = TV_i^{1/T} - 1$$
> La media aritmetica fornisce uno stimatore non distorto del rendimento atteso (futuro) per periodo; la media geometrica tiene conto della capitalizzazione composta per rappresentare accuratamente la performance passata.
>
> **Correzione per gradi di libertà.** Gli stimatori di varianza e covarianza sopra assumono nota la media della distribuzione, ma anche questa va di solito stimata. È quindi necessario il seguente aggiustamento (trascurabile per $T$ grande) per rendere lo stimatore non distorto:
> $$\hat\sigma_i^2 = \frac{1}{T-1}\sum_{t=1}^T (r_{it}-\bar r_i)^2 \qquad \hat{cov}(r_i,r_j) = \frac{1}{T-1}\sum_{t=1}^T (r_{it}-\bar r_i)(r_{jt}-\bar r_j)$$
>
> **Alcune osservazioni.** La frequenza dei dati (ad es. giornaliera vs. mensile) è rilevante solo per la stima delle (co)varianze: l'accuratezza aumenta all'aumentare della frequenza. La frequenza non è invece rilevante per i rendimenti medi: i rendimenti medi su 10 anni di dati dovrebbero essere gli stessi sia stimandoli da dati giornalieri sia da dati mensili o annuali. In assenza di correlazione seriale, le varianze per periodo si sommano semplicemente, ad esempio $\sigma^2_{annuo} = 12 \cdot \sigma^2_{mensile}$; la deviazione standard cresce quindi al tasso $\sqrt{T}$: $\sigma_{annuo} = \sqrt{12}\cdot \sigma_{mensile}$.

*(slide 17–21)*

## Misure a livello di portafoglio: due titoli e caso generale con N titoli

> [!abstract] Definizione
> Si aggregano ora le informazioni sui rendimenti dei singoli titoli al livello di portafoglio. Con un portafoglio a due titoli, di frazioni $w_1$ e $w_2$: $r_p = w_1 r_1 + w_2 r_2$.
>
> **Rendimento atteso di un portafoglio a due titoli**: media ponderata dei rendimenti attesi dei singoli titoli.
> $$E(r_p) = w_1 E(r_1) + w_2 E(r_2)$$
>
> **Varianza del rendimento di un portafoglio a due titoli.** Scarto dal rendimento medio:
> $$r_p - E(r_p) = w_1(r_1-E(r_1)) + w_2(r_2-E(r_2))$$
> Elevando al quadrato:
> $$(r_p-E(r_p))^2 = w_1^2(r_1-E(r_1))^2 + w_2^2(r_2-E(r_2))^2 + 2w_1w_2(r_1-E(r_1))(r_2-E(r_2))$$
> Prendendo il valore atteso di ciascun termine:
> $$var(r_p) = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_{12}$$
> $$\sigma_p = \sqrt{w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_{12}}$$
> Si noti che $\sigma_p = w_1\sigma_1 + w_2\sigma_2$ (media ponderata) solo se $\rho_{12}=1$ — nessuna diversificazione.
>
> **Esempio.** Titolo A: $E(r)=0{,}1$, $var=0{,}01$. Titolo B: $E(r)=0{,}2$, $var=0{,}05$. Covarianza $A,B = 0{,}015$. Pesi $w_A=0{,}3$, $w_B=0{,}7$.
> $$\hat\mu_p = 0{,}3\times 0{,}1 + 0{,}7\times 0{,}2 = 0{,}17$$
> $$\hat\sigma_p^2 = 0{,}3^2\times 0{,}01 + 0{,}7^2\times 0{,}05 + 2\times 0{,}3\times 0{,}7\times 0{,}015 = 0{,}0317$$
> $$\hat\sigma_p = \sqrt{0{,}0317} = 0{,}178$$
>
> **Generalizzazione a portafogli con $N$ titoli** (pesi $w_i$, $i=1,\dots,N$), in forma matriciale.
>
> Rendimento realizzato del portafoglio: $r_p = \sum_{i=1}^N w_i r_i = \underbrace{\mathbf{w}'}_{1\times N}\underbrace{\mathbf{r}}_{N\times 1}$.
>
> Rendimento atteso: $E(r_p) = \sum_{i=1}^N w_i E(r_i) = \underbrace{\mathbf{w}'}_{1\times N}\underbrace{\boldsymbol\mu}_{N\times 1}$.
>
> Varianza:
> $$var(r_p) = \sum_{i=1}^N w_i^2\sigma_i^2 + \sum_{i=1}^N\sum_{j\ne i} w_iw_j\sigma_{ij} = \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij} = \underbrace{\mathbf{w}'}_{1\times N}\underbrace{\boldsymbol\Sigma}_{N\times N}\underbrace{\mathbf{w}}_{N\times 1}$$
>
> Ogni coppia di titoli $(i,j)$ entra nella varianza di portafoglio con il termine $w_iw_j\sigma_{ij}$, dove $\sigma_{ij}$ è la covarianza tra $i$ e $j$ e $\sigma_{ii}$ è la varianza del titolo $i$:
> $$\boldsymbol\Sigma = \begin{bmatrix} \sigma_{11} & \sigma_{12} & \dots & \sigma_{1N} \\ \sigma_{21} & \sigma_{22} & \dots & \dots \\ \dots & \dots & \dots & \dots \\ \sigma_{N1} & \dots & \dots & \sigma_{NN} \end{bmatrix}$$
> La varianza totale del portafoglio è la somma degli elementi della matrice pesata:
> $$var(r_p) = \text{somma}\begin{bmatrix} w_1w_1\sigma_{11} & w_1w_2\sigma_{12} & \dots & w_1w_N\sigma_{1N} \\ w_2w_1\sigma_{21} & w_2w_2\sigma_{22} & \dots & \dots \\ \dots & \dots & \dots & \dots \\ w_Nw_1\sigma_{N1} & \dots & \dots & w_Nw_N\sigma_{NN} \end{bmatrix} = \mathbf{X}'\boldsymbol\Sigma \mathbf{X}$$

*(slide 22–27)*

## Rischio, incertezza e paradigma dell'utilità attesa

> [!abstract] Definizione
> **Rischio e incertezza.** Knight (1921) distingue tra:
> - *Rischio*: situazione in cui gli esiti futuri sono incerti ma è possibile assegnare loro probabilità misurabili.
> - *Incertezza*: situazione in cui non è possibile assegnare probabilità misurabili agli esiti futuri, perché manca una base statistica o una distribuzione definibile.
>
> **Decisioni in condizioni di incertezza**, caratterizzate da tre ingredienti:
> 1. *Incertezza*: modellata come la futura realizzazione di uno tra $S$ possibili stati del mondo.
> 2. *Azioni*: in finanza, scelta dei pesi del portafoglio $w_1,\dots,w_n$.
> 3. *Conseguenze*: in finanza, l'esito finale del portafoglio — la ricchezza — nello stato del mondo realizzato $k$:
> $$W_k = x_{1k}w_1 + x_{2k}w_2 + \dots + x_{nk}w_n$$
> dove $p_{ik}$ è il payoff realizzato del titolo $i$ nello stato $k$.
>
> Problema dell'investitore: scelta dei pesi di portafoglio che massimizzano la sua utilità *von Neumann–Morgenstern* (vNM): $\max_x U(W_1,\dots,W_S) \equiv U(W)$.
>
> **Paradigma dell'utilità attesa. Assunzioni:**
> 1. È possibile assegnare una probabilità a ciascuno stato del mondo, $\pi_s$.
> 2. Esiste un'utilità vNM $U(\cdot)$ che dipende solo dalle conseguenze:
> $$U(W) = U(W_1,\dots,W_S) = \pi_1 u(W_1) + \dots + \pi_S u(W_S) = E[u(W)]$$
> Gli investitori massimizzano l'utilità vNM:
> $$\max_w U(W) = \pi_1 u(W_1) + \dots + \pi_S u(W_S)$$
> Si tratta di una teoria **normativa** (come dovrebbe comportarsi un investitore), ma spesso usata come teoria **positiva** in finanza (per descrivere come gli investitori si comportano effettivamente).

*(slide 28–31)*

## Avversione al rischio, concavità dell'utilità ed equivalente certo

> [!note] Dimostrazione
> **Che cosa implicano le preferenze per il rischio in questo paradigma?** La forma della funzione di utilità vNM riflette le preferenze per il rischio. Si consideri una lotteria con ricchezza finale pari a $W_1$ oppure $W_2$.
>
> **Figura (pag. 32)** — Grafico di $u(W)$ crescente e concava, con i punti $u(W_1)$, $u(W_2)$ e $E[u(W)]$ (il segmento che congiunge $u(W_1)$ e $u(W_2)$ valutato in $E[W]$). Mostra che il valore atteso dell'utilità della lotteria, $E[u(W)]$, giace sotto la curva $u(W)$ se questa è concava.
>
> **Figura (pag. 33)** — Stessa costruzione con l'aggiunta del punto equivalente certo (CE): l'avversione al rischio implica che l'equivalente certo (CE) è minore del payoff atteso. Si conclude che una funzione di utilità vNM di un investitore avverso al rischio deve essere concava.
>
> Più precisamente, l'avversione al rischio implica concavità e, per la **disuguaglianza di Jensen**:
> $$u(CE) = E[u(W)] < u(E[W]) \;\Rightarrow\; CE < E[W]$$
> dove $CE \equiv u^{-1}(E[u(W)])$.
>
> **Premio per il rischio** $= E(W) - CE$.

*(slide 32–33)*

## Misure di avversione al rischio: ARA, RRA e le famiglie CARA/CRRA

> [!abstract] Definizione
> In finanza si assume che gli investitori siano avversi al rischio, cioè disposti ad accettarlo solo se adeguatamente remunerati. L'avversione al rischio dipende dalla derivata seconda della funzione di utilità, che a sua volta dipende dal parametro di scala; per eliminare questa dipendenza si standardizza rispetto alla derivata prima. Due misure standard:
>
> 1. **Avversione assoluta al rischio (Arrow–Pratt)**:
> $$ARA = -\frac{u''(W)}{u'(W)}$$
> 2. **Avversione relativa al rischio**:
> $$RRA = -\frac{u''(W)\,W}{u'(W)}$$
>
> **Funzioni di utilità CARA e CRRA.**
> - Avversione assoluta al rischio costante (**CARA**): $u(W) = -e^{-\rho W}$, con $ARA=\rho$.
> - Avversione relativa al rischio costante (**CRRA**):
> $$u(W) = \frac{W^{1-\gamma}}{1-\gamma}, \quad \gamma\ne 1 \qquad\qquad u(W) = \ln(W), \quad \gamma = 1$$
> con $RRA=\gamma$.
>
> Sia le preferenze CARA sia quelle CRRA sono comunemente utilizzate in asset pricing; il corso si concentra soprattutto sull'utilità media-varianza (quadratica).
>
> **Stimare l'avversione al rischio**: utilizzare questionari; osservare le decisioni degli individui in condizioni di rischio; osservare quanto le persone sono disposte a pagare per evitare il rischio.

*(slide 34–36)*

## Dal paradigma dell'utilità attesa all'approccio media-varianza

> [!note] Dimostrazione
> L'utilità attesa dipende dalla distribuzione di probabilità e dalla funzione di utilità. Si può approssimare la funzione di utilità intorno a $E(W)$ con uno sviluppo di Taylor:
> $$u(W) \approx u(E(W)) + u'(E(W))(W-E(W)) + \frac{u''(E(W))}{2}(W-E(W))^2 + \frac{u^{(III)}(E(W))}{6}(W-E(W))^3 + \frac{u^{(IV)}(E(W))}{24}(W-E(W))^4$$
> Prendendo i valori attesi, si approssima l'utilità vNM:
> $$E[u(W)] = U(W) \approx u(E(W)) + \frac{u''(E(W))}{2}var[W] + \frac{u^{(III)}(E(W))}{6}skew[W] + \frac{u^{(IV)}(E(W))}{24}kurt[W]$$
>
> **In quali condizioni $E[u(W)]$ dipende solo da media e deviazione standard?** Nella teoria di portafoglio dei primordi (ad es. Markowitz) si sono usate semplicemente media e varianza del rendimento — è l'approccio seguito nel corso. L'utilità media-varianza è spesso più trattabile della funzione di utilità vNM. È compatibile con il paradigma vNM sì, a certe condizioni: approssimativamente per rischi piccoli; esattamente se si assumono payoff (rendimenti) normalmente distribuiti oppure utilità quadratica.
>
> **Normalità congiunta.** Se tutti i titoli hanno payoff (rendimenti) normalmente distribuiti (la dipendenza non è un problema — richiede però uno spazio degli stati infinito), qualsiasi combinazione lineare di variabili congiuntamente normali è ancora normale. La distribuzione normale è completamente descritta dai suoi primi due momenti, $r \sim N(\mu,\sigma^2)$, quindi anche l'utilità attesa può essere espressa come funzione di soli due parametri.
>
> **Utilità quadratica.** Sia $u(W) = W - bW^2$. L'utilità attesa è allora:
> $$E[u(W)] = E(W) - bE[W^2] = E(W) - b\left(E(W)^2 + var(W)\right)$$
> Ignorando trasformazioni monotone che non influenzano le preferenze:
> $$E[u(W)] = E(W) - b\, var(W)$$
> Quindi l'utilità attesa è funzione solo della media $E(W)$ e della varianza $var(W)$ — le derivate di ordine superiore al secondo sono nulle. **Svantaggi**: ha un massimo, oltre il quale gli investitori preferiscono "meno a più"; ARA crescente, $ARA = \dfrac{b}{1-bW}$. Si tratta più di un'approssimazione trattabile che di una specificazione completa della funzione di utilità.

*(slide 37–40)*

## La funzione di utilità media-varianza

> [!abstract] Definizione
> Si consideri un'utilità media-varianza espressa in termini di rendimenti, dove $U=$ utilità attesa, $E(r)=$ rendimento atteso del titolo o del portafoglio, $A=$ coefficiente di avversione al rischio, $\sigma^2=$ varianza dei rendimenti, $\tfrac12=$ fattore di scala:
> $$U = E(r) - \frac{1}{2}A\sigma^2$$
> Derivate parziali:
> $$\frac{\partial U(r)}{\partial E(r)} > 0 \qquad\qquad \frac{\partial U(\tilde r)}{\partial \sigma(r)} = -A\,\sigma(r)$$
> $$u(r) = E(r) - \frac{1}{2}A\sigma^2(r)$$
> L'utilità aumenta al crescere del rendimento atteso; $A$ misura l'atteggiamento verso il rischio:
> - $A>0$: l'investitore preferisce varianza più bassa, cioè è avverso al rischio (maggiore $A$, maggiore avversione).
> - $A=0$: l'investitore è neutrale al rischio.
> - $A<0$: l'investitore ama il rischio.
>
> **Figure 6.1** — *The trade-off between risk and return of a potential investment portfolio, P.* Il piano $E(r)$–$\sigma$ è diviso in quattro quadranti (I, II, III, IV) rispetto a un portafoglio $P$; la direzione preferita ("Northwest") è quella di rendimento atteso maggiore e rischio minore, cioè verso il quadrante II.
>
> **Criterio media-varianza.** Il portafoglio $i$ domina il portafoglio $j$ se:
> $$E(r_i) \ge E(r_j) \quad \text{e} \quad \sigma_i \le \sigma_j$$
> e almeno una disuguaglianza è stretta.

*(slide 41–44)*

## Rischio e rendimento, premio per il rischio ed equivalente certo: un esempio numerico

> [!example] Esempio
> Un investitore ha un capitale di EUR 50.000 e due opportunità di investimento: una priva di rischio e una rischiosa. Il titolo privo di rischio, a fronte di un investimento iniziale di EUR 50.000, paga EUR 51.500 in un periodo. Il valore del titolo rischioso ha la stessa probabilità di raddoppiare o dimezzarsi: per un investimento iniziale di EUR 50.000, paga EUR 100.000 con probabilità 0,5 e EUR 25.000 con probabilità 0,5.
>
> Rendimento del titolo privo di rischio:
> $$r_f = \frac{51.500}{50.000} - 1 = 3\%$$
> Rendimento atteso dell'investimento rischioso:
> $$E(r) = \frac12\left(\frac{100}{50}-1\right) + \frac12\left(\frac{25}{50}-1\right) = 25\%$$
> Rendimento in eccesso, utile per decidere quale investimento scegliere: $r^e = r - r_f$.
>
> Il **premio per il rischio**, cioè il rendimento atteso in eccesso:
> $$E(r^e) = E(r-r_f) = \frac12(97\%) + \frac12(-53\%) = 22\%$$
> La rischiosità dell'investimento tramite la varianza: per il titolo privo di rischio la varianza è zero; per l'investimento rischioso:
> $$\sigma^2(\tilde r) = \frac12\left[(1{,}00-0{,}25)^2 + (-0{,}50-0{,}25)^2\right] = 0{,}56$$
> $$\sigma(\tilde r) = \sqrt{0{,}56} = 0{,}75 = 75\%$$
>
> **Il rendimento equivalente certo.** Il rendimento equivalente certo di un titolo rischioso (o portafoglio), $r_{CE}$, è il rendimento di un titolo privo di rischio che rende l'investitore indifferente (stessa utilità) tra il titolo rischioso e l'equivalente certo. Se $r_f \ge r_{CE}$, è ottimale investire nel titolo privo di rischio. Calcolo di $r_{CE}$:
> $$U(r_{CE}) = U(\tilde r)$$
> Data la specificazione dell'utilità:
> $$E[r_{CE}] - \frac12 A\sigma^2_{r_{CE}} = E[r] - \frac12 A\sigma^2(\tilde r)$$
> Poiché l'equivalente certo è privo di rischio ($\sigma^2_{r_{CE}}=0$):
> $$r_{CE} = E[\tilde r] - \frac12 A\sigma^2(\tilde r) = 0{,}25 - \frac12 A\cdot 0{,}56$$
>
> **Rendimento equivalente certo per diversi livelli di $A$** (NB: $r_f = 3\%$):
>
> | $A$ | $r_{CE}$ |
> |---|---|
> | 0,04 | 24% |
> | 0,50 | 11% |
> | 0,78 | 3% |
> | 1,00 | −3% |
>
> Domande poste sulla slide: per $A=0{,}50$, quale asset verrebbe scelto? Per quale livello di $A$ l'investitore è indifferente tra i due? All'aumentare di $A$, come varia $r_{CE}$ e perché? Quale dovrebbe essere il rendimento atteso (e il premio per il rischio) per rendere l'investitore indifferente tra l'asset rischioso e quello privo di rischio?

*(slide 45–50)*

## Curve di indifferenza

> [!note] Dimostrazione
> **Curva di indifferenza**: combinazioni di $E(r)$ e $\sigma$ che mantengono invariata l'utilità. Portafogli ugualmente desiderabili giacciono, nel piano media–deviazione standard, su una stessa curva di indifferenza, che unisce tutti i punti con lo stesso livello di utilità. Per un dato $A$, le curve di indifferenza non si intersecano.
>
> Con $A=0{,}5$: $U(\tilde r) = E(\tilde r) - \tfrac12 A\sigma^2(\tilde r) = E(\tilde r) - 0{,}25\,\sigma^2$. Esempi:
> $$E(r)=0{,}25,\ \sigma^2=0{,}56 \;\Rightarrow\; U = 0{,}25-0{,}25(0{,}56)=0{,}11 \ \text{(punto } Z\text{)}$$
> $$E(r)=0{,}25,\ \sigma^2=0{,}64 \;\Rightarrow\; U = 0{,}25-0{,}25(0{,}64)=0{,}09 \ \text{(punto } Y\text{)}$$
> $$E(r)=0{,}30,\ \sigma^2=0{,}56 \;\Rightarrow\; U = 0{,}30-0{,}25(0{,}56)=0{,}16 \ \text{(punto } X\text{)}$$
>
> Le curve sono **crescenti**: per un individuo avverso al rischio la curva di indifferenza ha pendenza positiva, poiché all'aumentare di $\sigma$ è necessario aumentare $E(r)$ per mantenere invariata l'utilità. Sono **convesse**: l'aumento di $E(r)$ richiesto per compensare incrementi di $\sigma$ cresce al crescere del rischio già assunto dall'investitore.
>
> **Equazione della curva di indifferenza.** Data $U(r) = E(r) - \tfrac12 A\sigma^2$, la condizione di indifferenza ($dU=0$) dà $c = E(r) - \tfrac12 A\sigma^2$, quindi:
> $$E(r) = c + \frac12 A\sigma^2$$
> Pendenza: $\dfrac{dE(r)}{d\sigma} = A\sigma$. Derivata seconda: $\dfrac{d^2E(r)}{d\sigma^2} = A>0 \Rightarrow$ la curva di indifferenza è convessa.
>
> **Figure 6.7** — *Indifference curves for U = .05 and U = .09 with A = 2 and A = 4.* Il grafico mostra quattro curve nel piano $E(r)$–$\sigma$ (per le combinazioni $U=0{,}05$/$U=0{,}09$ e $A=2$/$A=4$): a parità di $U$, curve con $A$ maggiore sono più ripide (l'investitore richiede una compensazione maggiore per lo stesso incremento di rischio).

*(slide 51–54)*

## Il problema di scelta del portafoglio e i concetti di frontiera efficiente

> [!abstract] Definizione
> **Problema di scelta del portafoglio.** Harry Markowitz sviluppò la moderna teoria di portafoglio nel 1952. All'interno del paradigma media-varianza, il problema si articola in tre fasi:
> 1. *Individuazione della frontiera efficiente dei titoli rischiosi* — costruire portafogli di titoli rischiosi con massimo $E(r_p)$ per ogni dato livello di $\sigma_p$.
> 2. *Individuazione della frontiera efficiente con titolo privo di rischio* — dato un titolo privo di rischio, determinare il portafoglio di tangenza e costruire la nuova frontiera efficiente.
> 3. *Individuazione del portafoglio ottimo* — date le preferenze dell'investitore (grado di avversione al rischio), scegliere il punto ottimale sulla frontiera efficiente con titolo privo di rischio.
>
> Le fasi 1. e 2. non dipendono dalle preferenze individuali, ma solo dal criterio media–varianza.
>
> **1. La frontiera efficiente dei titoli rischiosi.** Criterio media–varianza: gli investitori preferiscono rendimento atteso più elevato a parità di rischio, e rischio minore a parità di rendimento atteso. Un **portafoglio efficiente** è tale se e solo se non esiste un altro portafoglio ammissibile che offra lo stesso $E(r)$ con $\sigma$ inferiore, oppure $E(r)$ maggiore con lo stesso $\sigma$. I portafogli inefficienti sono dominati da almeno un'alternativa nell'insieme ammissibile. Da qui in avanti l'analisi si limita ai soli titoli rischiosi.
>
> **Insieme delle opportunità, frontiera media–varianza e frontiera efficiente.**
> - *Insieme delle opportunità (insieme ammissibile)*: tutti i portafogli ottenibili combinando i titoli rischiosi disponibili (efficienti e inefficienti).
> - *Frontiera media–varianza (MVF) / frontiera di minima varianza*: per ogni livello target di $E(r)$, il portafoglio con rischio minimo $\sigma$.
> - *Frontiera efficiente*: la parte della MVF costituita solo da portafogli efficienti, cioè non dominati.
>
> **Figura (pag. 58)** — Piano $E(r)$–$\sigma$ con l'insieme delle opportunità ("Opportunity set"), la frontiera media–varianza ("Mean-variance frontier") e, sopra il GMVP, l'insieme efficiente ("Efficient set"). Mostra che l'insieme efficiente è la porzione superiore della MVF a partire dal portafoglio globale di minima varianza.
>
> **Portafoglio globale di minima varianza (GMVP).** Sono efficienti solo i portafogli con rendimento atteso superiore a quello del GMVP. La frontiera efficiente dipende esclusivamente dall'insieme delle opportunità, non dalle preferenze individuali degli investitori. Il GMVP è il portafoglio con varianza minima e separa la parte inefficiente da quella efficiente della MVF; i suoi pesi non dipendono dai rendimenti attesi.

*(slide 55–59)*

## Portafoglio a due attività rischiose: rendimento, varianza e diversificazione

> [!abstract] Definizione
> Per comprendere la frontiera efficiente delle attività rischiose, si parte dal caso con due asset: un fondo obbligazionario ($D$, debt) e un fondo azionario ($E$, equity). Rendimento del portafoglio:
> $$r_p = w_D r_D + w_E r_E$$
> con $w_D$ = peso del fondo obbligazionario, $r_D$ = rendimento del fondo obbligazionario, $w_E$ = peso del fondo azionario, $r_E$ = rendimento del fondo azionario. Rendimento atteso:
> $$E(r_p) = w_D E(r_D) + w_E E(r_E), \quad \text{con } w_E = 1-w_D$$
>
> **Varianza**:
> $$\sigma_p^2 = w_D^2\sigma_D^2 + w_E^2\sigma_E^2 + 2w_Dw_E\, Cov(r_D,r_E) = w_D^2\sigma_D^2 + w_E^2\sigma_E^2 + 2w_Dw_E\rho_{DE}\sigma_D\sigma_E$$
> A differenza del rendimento atteso, la varianza del portafoglio **non** è una media ponderata delle varianze individuali; può essere riscritta come media ponderata delle covarianze:
> $$\sigma_p^2 = w_Dw_D\sigma_{DD} + w_Ew_E\sigma_{EE} + w_Dw_E\sigma_{DE} + w_Ew_D\sigma_{ED}$$
>
> **Diversificazione e correlazione.** La volatilità del portafoglio è inferiore alla media ponderata delle volatilità individuali se $\rho_{DE}<1$ (anche quando $\sigma_{DE}>0$):
> $$\sigma_p < w_D\sigma_D + w_E\sigma_E \quad \text{se} \quad \rho_{DE}<1$$
> Perché? Diversificazione. L'ammontare della possibile riduzione del rischio dipende dalla correlazione: $\rho=1$ correlazione positiva perfetta, $\rho=0$ asset non correlati, $\rho=-1$ correlazione negativa perfetta. Il potenziale di riduzione del rischio aumenta al diminuire della correlazione.
>
> Casi estremi:
> - $\rho=1$: nessuna riduzione del rischio possibile, $\sigma_p = w_D\sigma_D + w_E\sigma_E$.
> - $\rho=0$: $\sigma_p$ può essere inferiore alla deviazione standard di ciascuna attività, $\sigma_p = \sqrt{w_E^2\sigma_E^2 + w_D^2\sigma_D^2}$.
> - $\rho=-1$: è possibile un'immunizzazione dal rischio (*perfect hedge*) in assenza di vendite allo scoperto, $\sigma_p = |w_D\sigma_D - w_E\sigma_E|$ — portafoglio perfettamente coperto con $w_E = \dfrac{\sigma_D}{\sigma_D+\sigma_E} = 1-w_D$.
>
> **Esempio: portafoglio equipesato** ($w_D=w_E=0{,}50$):
>
> | | Fondo obbligazionario | Fondo azionario |
> |---|---|---|
> | $E(r)$ | 8% | 13% |
> | $\sigma$ | 12% | 20% |
> | $\sigma_{DE}$ | 72 | |
> | $\rho_{DE}$ | 0,30 | |
>
> $$E(r_p) = w_D E(r_D) + w_E E(r_E) = 0{,}50\times 8\% + 0{,}50\times 13\% = 10{,}5\%$$
> $$\sigma_p^2 = w_D^2\sigma_D^2 + w_E^2\sigma_E^2 + 2w_Dw_E\sigma_{DE} = (0{,}50)^2(12)^2 + (0{,}50)^2(20)^2 + 2(0{,}50)(0{,}50)(72) = 172$$
> $$\sigma_p = \sqrt{172} = 13{,}23\%$$
>
> **Grafico (pag. 65)** — *Rendimento atteso del portafoglio* al variare del peso azionario (asse: peso in azioni da −0,5 a 2,0). Le variazioni dei pesi influenzano linearmente $E(r_p)$; la vendita allo scoperto del fondo azionario per acquistare il fondo obbligazionario riduce $E(r_p)$, mentre la vendita allo scoperto del fondo obbligazionario (o l'indebitamento al costo del debito) per acquistare l'azione aumenta $E(r_p)$.
>
> **Grafico (pag. 66)** — *Deviazione standard del portafoglio* in funzione del peso nel fondo azionario, con quattro curve per $\rho=-1,0,0{,}30,1$. Mostra come la forma della relazione rischio–peso dipenda criticamente dalla correlazione: con $\rho=-1$ la deviazione standard può annullarsi per un peso interno, mentre con $\rho=1$ la relazione è lineare.

*(slide 60–66)*

## Frontiera efficiente con due attività rischiose: i casi di correlazione perfetta, negativa perfetta e imperfetta

> [!note] Dimostrazione
> **Grafico (pag. 67)** — Frontiera nel piano $\{E(r_p)-\sigma_p\}$ per i due asset rischiosi $D$ ed $E$, con curve per $\rho=-1,0,0{,}30,1$. Senza vendite allo scoperto la frontiera raggiunge i punti estremi $D$ ed $E$; il grafico introduce la domanda su cosa accada quando le vendite allo scoperto sono consentite.
>
> **Caso di correlazione positiva perfetta ($\rho_{DE}=1$).** Da $E(r_p) = w_D E(r_D) + w_E E(r_E)$ si ricava:
> $$w_D = \frac{E(r_p)-E(r_E)}{E(r_D)-E(r_E)} \tag{1}$$
> e se $\rho_{DE}=1$:
> $$\sigma_p = w_D\sigma_D + (1-w_D)\sigma_E \tag{2}$$
> Sostituendo $w_D$ dall'eq. (1) nell'eq. (2) si ottiene la frontiera lineare:
> $$E(r_p) = \underbrace{\frac{E(r_D)\sigma_E - E(r_E)\sigma_D}{\sigma_D-\sigma_E}}_{\text{intercetta}} + \underbrace{\frac{E(r_E)-E(r_D)}{\sigma_E-\sigma_D}}_{\text{pendenza}}\,\sigma_p$$
> **Figura (pag. 69)** — Retta $E(r)$–$\sigma$ che collega i punti $D$ ed $E$ (con $\rho_{DE}=1$ l'insieme delle opportunità coincide con la frontiera media–varianza). Le linee punteggiate indicano portafogli che richiedono vendite allo scoperto. Senza vendite allo scoperto, l'asset meno rischioso coincide con il GMVP; con vendite allo scoperto il GMVP ha rischio nullo. In assenza di vendite allo scoperto: insieme efficiente = MVF = insieme delle opportunità.
>
> **Caso di correlazione negativa perfetta ($\rho_{DE}=-1$).**
> $$\sigma_p = \begin{cases} w_D\sigma_D - (1-w_D)\sigma_E, & \text{se } w_D \ge \dfrac{\sigma_E}{\sigma_D+\sigma_E} \\[4pt] -w_D\sigma_D - (1-w_D)\sigma_E, & \text{se } w_D < \dfrac{\sigma_E}{\sigma_D+\sigma_E} \end{cases} \tag{3}$$
> dove i due casi garantiscono la non negatività di $\sigma_p$. Sostituendo $w_D$ dall'eq. (1) nell'eq. (3), si ottiene la frontiera lineare, ora composta da due parti:
> $$E(r_p) = \begin{cases} \dfrac{E(r_D)\sigma_E + E(r_E)\sigma_D}{\sigma_D+\sigma_E} - \dfrac{E(r_E)-E(r_D)}{\sigma_D+\sigma_E}\,\sigma_p, & \text{se } w_D \ge \dfrac{\sigma_E}{\sigma_D+\sigma_E} \\[6pt] \dfrac{E(r_D)\sigma_E + E(r_E)\sigma_D}{\sigma_D+\sigma_E} + \dfrac{E(r_E)-E(r_D)}{\sigma_D+\sigma_E}\,\sigma_p, & \text{se } w_D < \dfrac{\sigma_E}{\sigma_D+\sigma_E} \end{cases}$$
> con intercetta $\frac{E(r_D)\sigma_E+E(r_E)\sigma_D}{\sigma_D+\sigma_E}$ e pendenza $\mp\frac{E(r_E)-E(r_D)}{\sigma_D+\sigma_E}$.
>
> **Figura (pag. 71)** — Diagramma a "V" spezzata che unisce $D$ ed $E$ con vertice sull'asse $\sigma=0$. Le linee punteggiate indicano portafogli con vendite allo scoperto. Anche senza vendite allo scoperto è possibile individuare un portafoglio privo di rischio (immunizzazione perfetta): tale portafoglio è il GMVP.
>
> **Figura (pag. 72)** — Caso di correlazione imperfetta: curva concava-verso-destra che unisce $D$ ed $E$ passando per il GMVP, con tratteggio per i portafogli che richiedono vendite allo scoperto.
>
> **Determinazione del GMVP (due asset).** Minimizzando la varianza del portafoglio:
> $$\min_{w_D,w_E}\; w_D^2\sigma_D^2 + w_E^2\sigma_E^2 + 2w_Dw_E\sigma_{DE} \qquad \text{sub}\ w_E = 1-w_D$$
> I pesi del GMVP risultano:
> $$w_{D,GMVP} = \frac{\sigma_E^2-\sigma_{DE}}{\sigma_D^2+\sigma_E^2-2\sigma_{DE}}$$
> Con $\rho_{DE}=-1$ si ottiene $w_{D,GMVP} = \dfrac{\sigma_E}{\sigma_E+\sigma_D}$, cioè il portafoglio immunizzato. Con $\rho_{DE}=1$ si ottiene $w_{D,GMVP} = \dfrac{\sigma_E}{\sigma_E-\sigma_D}$ (il cui significato economico è lasciato come domanda).
>
> **Convessità della frontiera.** La frontiera non può diventare concava: la correlazione massima è pari a 1, e in tal caso i portafogli che combinano due titoli si troverebbero su una linea retta. Da qui la convessità.

*(slide 67–74)*

## Portafogli con tre o più titoli: dal caso specifico al caso generale con N titoli

> [!example] Esempio
> Tornando al caso più generale con più di due titoli: con tre o più titoli l'insieme dei portafogli possibili forma una regione. I portafogli sul bordo di questa regione sono detti **portafogli a varianza minima**; quello con la varianza più bassa è il GMVP; i portafogli a varianza minima al di sopra del GMVP sono detti **efficienti**.
>
> **Un esempio con tre titoli rischiosi.**
>
> | Titolo | $E[r]$ | $\sigma$ |
> |---|---|---|
> | A | 5% | 10% |
> | B | 10% | 20% |
> | C | 15% | 30% |
>
> Matrice di correlazione:
>
> | | A | B | C |
> |---|---|---|---|
> | A | 1,0 | 0 | 0,5 |
> | B | 0 | 1,0 | 0,5 |
> | C | 0,5 | 0,5 | 1,0 |
>
> **Grafico (pag. 77)** — *MVF con tre titoli*: nel piano $E(r)$–$\sigma$ è tracciata la frontiera curva che unisce i tre asset A, B, C, con il GMVP segnato sulla curva. Mostra la forma tipica "a parabola rovesciata di lato" della frontiera con più titoli.
>
> **Grafico (pag. 78)** — *Aggiunta di un titolo dominato in varianza*: si aggiunge un quarto titolo D con $E(r_D)=15\%$, $\sigma_D=45\%$, $\rho_{Di}=0$ con $i=A,B,C$. Il grafico sovrappone la nuova MVF (con D) a quella precedente: la nuova frontiera si sposta leggermente ma il punto D resta interno/dominato rispetto alla frontiera.
>
> **Grafico (pag. 79)** — *Aggiunta di un titolo dominato in media e varianza*: si sostituisce D con un titolo E tale che $E(r_E)=5\%$, $\sigma_E=45\%$, $\rho_{Ei}=-0{,}2$ con $i=A,B,C$. Anche questo titolo, pur con correlazione negativa, resta dominato rispetto alla frontiera a tre titoli.
>
> **I titoli dominati sono detenuti da qualcuno?** Si osserva la composizione del GMVP:
>
> | Peso | Tre titoli | Quattro titoli (D) | Quattro titoli (E) |
> |---|---|---|---|
> | A | 88,72% | 85,99% | 80,80% |
> | B | 28,69% | 27,82% | 27,20% |
> | C | -17,41% | -16,81% | -14,66% |
> | D | - | 3,00% | - |
> | E | - | - | 6,66% |
> | $E(r_{GMVP})$ | 4,69% | 5,01% | 4,89% |
> | $\sigma_{GMVP}$ | 7,91% | 7,79% | 7,27% |
>
> Nonostante siano individualmente dominati, i titoli D ed E ottengono un peso positivo nel GMVP grazie alla loro bassa (o negativa) correlazione con gli altri titoli, che riduce la varianza complessiva di portafoglio.
>
> **Il caso generale con $N$ titoli.** I casi visti sono particolari del caso generale con $N$ titoli rischiosi; tutti i portafogli sulla MVF dal GMVP in poi offrono le migliori combinazioni rischio-rendimento. Prima di affrontare la MVF generale, si studia il meccanismo della diversificazione.
>
> **L'impatto della correlazione sul rischio di portafoglio**:
>
> | Correlazione | Rischio portafoglio | Implicazione |
> |---|---|---|
> | $\rho_{ij}=1$ | $\sigma_p = \sum_{i=1}^N w_i\sigma_i$ | Nessuna riduzione del rischio: il rischio di portafoglio coincide con la media ponderata delle volatilità individuali |
> | $\rho_{ij}=0$ | $\sigma_p^2 = \sum_{i=1}^N w_i^2\sigma_i^2$ | Eliminazione del rischio idiosincratico: per $N\to\infty$ la varianza di portafoglio tende a zero |
> | $0<\rho_{ij}<1$ | $\sigma_p < \sum_{i=1}^N w_i\sigma_i$ | Beneficio della diversificazione: il rischio si riduce al di sotto della volatilità media ponderata, creando un'opportunità di riduzione del rischio senza rinunciare al rendimento atteso |
>
> In pratica la maggior parte dei titoli presenta $0<\rho<1$: ogniqualvolta $\rho<1$, la volatilità di portafoglio è strettamente inferiore alla media ponderata delle volatilità individuali, quindi la diversificazione riduce il rischio senza necessariamente ridurre il rendimento atteso. *Nota*: per $N>2$ non è possibile avere $\rho_{ij}=-1$ per ogni coppia di titoli — la matrice di correlazione non sarebbe semidefinita positiva e la varianza di portafoglio, $\mathbf{w}'\boldsymbol\Sigma\mathbf{w}$, non sarebbe economicamente ben definita (varianza negativa per alcuni $\mathbf{w}$).

*(slide 75–82)*

## Diversificazione: rischio di mercato vs. rischio specifico e la forza della diversificazione

> [!note] Dimostrazione
> **Grafico (pag. 83)** — *Diversificazione del portafoglio*: tipicamente mostra la deviazione standard del portafoglio in funzione del numero di titoli $N$, con la curva che decresce rapidamente per poi appiattirsi su un livello asintotico positivo.
>
> **Diversificazione del portafoglio: rischio di mercato e rischio specifico.**
> - *Rischio di mercato*: fonti di rischio a livello di mercato, non eliminabile tramite diversificazione; detto anche rischio sistematico o non diversificabile.
> - *Rischio specifico d'impresa*: rischio eliminabile tramite diversificazione; detto anche rischio diversificabile, idiosincratico o non sistematico.
>
> **L'importanza della covarianza.** La covarianza tra coppie di titoli e tra un titolo e il portafoglio svolge un ruolo fondamentale. Per un portafoglio ben diversificato (grande $N$), in cui tutti i titoli hanno (quasi) lo stesso peso, la varianza di portafoglio è determinata quasi interamente dalla covarianza media. La covarianza tra un singolo titolo e il portafoglio misura l'aumento marginale della varianza per un piccolo incremento di quel titolo nel portafoglio, finanziato mediante una posizione corta nel titolo privo di rischio.
>
> **La forza della diversificazione.** Si ricordi $\sigma_p^2 = \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij}$. Con portafoglio a pesi uguali $w_i = 1/N$, si definiscono varianza media $\bar\sigma^2 = \frac1N\sum_{i=1}^N \sigma_i^2$ e covarianza media $\overline{Cov} = \frac{1}{N(N-1)}\sum_{i=1}^N\sum_{\substack{j=1\\ j\ne i}}^N \sigma_{ij}$. Si può quindi esprimere la varianza di portafoglio come:
> $$\sigma_p^2 = \frac{1}{N}\bar\sigma^2 + \frac{N-1}{N}\overline{Cov}$$
> La varianza di portafoglio può essere ridotta a zero se la covarianza media è nulla; in generale, al crescere di $N$:
> $$\sigma_p^2 \xrightarrow{N\to\infty} \overline{Cov}$$
> Il rischio irriducibile di un portafoglio diversificato dipende dunque dalla covarianza dei rendimenti. Tali risultati valgono approssimativamente per qualunque portafoglio ben diversificato in cui $w_i$ sia sufficientemente piccolo per ogni $i$.
>
> **Tabella numerica** (deviazione standard del portafoglio equipesato e riduzione marginale, per $\rho=0$ e $\rho=0{,}40$):
>
> | N | Pesi (%) | Dev. st. (%), $\rho=0$ | Riduzione in $\sigma$, $\rho=0$ | Dev. st. (%), $\rho=0{,}40$ | Riduzione in $\sigma$, $\rho=0{,}40$ |
> |---|---|---|---|---|---|
> | 1 | 100 | 50,00 | 14,64 | 50,00 | 8,17 |
> | 2 | 50 | 35,36 | | 41,83 | |
> | 5 | 20 | 22,36 | 1,95 | 36,06 | 0,70 |
> | 6 | 16,67 | 20,41 | | 35,36 | |
> | 10 | 10 | 15,81 | 0,73 | 33,91 | 0,20 |
> | 11 | 9,09 | 15,08 | | 33,71 | |
> | 20 | 5 | 11,18 | 0,27 | 32,79 | 0,06 |
> | 21 | 4,76 | 10,91 | | 32,73 | |
> | 100 | 1 | 5,00 | 0,02 | 31,86 | 0,00 |
> | 101 | 0,99 | 4,98 | | 31,86 | |
>
> La tabella mostra come, aggiungendo titoli non perfettamente correlati, la deviazione standard del portafoglio equipesato scenda rapidamente per i primi titoli e poi si stabilizzi (riduzioni marginali via via più piccole), specialmente quando $\rho=0$; con $\rho=0{,}40$ il livello asintotico resta più elevato, coerentemente con $\sigma_p^2 \to \overline{Cov} > 0$.

*(slide 83–88)*

## La frontiera efficiente con N titoli: formulazione del problema di ottimizzazione

> [!abstract] Definizione
> Dopo aver visto il calcolo della MVF con due titoli rischiosi e come varia la varianza di un portafoglio equipesato al crescere di $N$, si considera ora il caso generale con $N$ titoli.
>
> **Formulazione come minimizzazione della varianza.** Per ottenere la frontiera efficiente dei titoli rischiosi occorre individuare i pesi $\mathbf{w}$ che minimizzano la varianza per un livello target del rendimento atteso del portafoglio, $\bar\mu_p$:
> $$\min_{\mathbf{w}}\; \sigma_p^2 = \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij} \qquad \text{sub}\ \sum_{i=1}^N w_i = 1,\ \ \sum_{i=1}^N w_iE(r_i) = \bar\mu_p$$
> La procedura si ripete per un numero sufficientemente elevato di valori obiettivo del rendimento atteso.
>
> **Formulazione equivalente come massimizzazione del rendimento.** In modo equivalente, si possono individuare i pesi che massimizzano il rendimento atteso per un livello target della varianza, $\bar\sigma^2$:
> $$\max_{\mathbf{w}}\; E(r_p) = \sum_{i=1}^N w_iE(r_i) \qquad \text{sub}\ \sum_{i=1}^N w_i = 1,\ \ \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij} = \bar\sigma_p^2$$
> Tali problemi possono essere risolti in forma chiusa, ma anche convenientemente con metodi numerici.
>
> **Determinazione del GMVP con $N$ titoli**:
> $$\min_{\mathbf{w}}\; \sigma_p^2 = \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij} \qquad \text{sub}\ \sum_{i=1}^N w_i = 1$$
>
> **Vincoli alle vendite allo scoperto.** Introducendo tali vincoli, l'ottimizzazione per la frontiera efficiente diventa:
> $$\min_{\mathbf{w}}\; \sigma_p^2 = \sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij} \qquad \text{sub}\ \sum_{i=1}^N w_i = 1,\ \ \mathbf{w}\ge 0,\ \ \sum_{i=1}^N w_iE(r_i) = \bar\mu_p$$
> In questo caso il problema deve essere risolto numericamente.

*(slide 89–93)*

## Stima degli input e struttura dei portafogli sulla frontiera

**Stima degli input.** Stime affidabili dei dati di input sono fondamentali per la corretta implementazione dell'ottimizzazione media-varianza. In generale, per calcolare la frontiera efficiente si utilizzano stime ottenute da serie storiche di rendimenti. Qualora le caratteristiche dei rendimenti siano stabili nel tempo (stazionarietà) e il campione sia sufficientemente lungo, si ottengono stime accurate. Tuttavia, rendimenti molto datati potrebbero non essere più rappresentativi dello stato attuale dell'impresa o dell'economia.

**Pesi di portafoglio e frontiera efficiente.** L'insieme dei portafogli ammissibili comprende quelli sulla frontiera e quelli al suo interno. I portafogli all'interno della frontiera possono avere qualsiasi struttura (purché i pesi sommino a uno). I portafogli sulla frontiera presentano invece una struttura particolare, coerente con il **teorema dei due fondi**: in sintesi, ciascun portafoglio a varianza minima può essere ottenuto come combinazione lineare di due portafogli a varianza minima.

*(slide 94–95)*

## Il teorema dei due fondi

> [!tip] Teorema
> **Enunciato.** Siano $\mathbf{w}_a$ e $\mathbf{w}_b$ i vettori dei pesi che definiscono due portafogli a varianza minima con rendimenti attesi tali che $E(r_a)\ne E(r_b)$. Allora ogni portafoglio a varianza minima può essere ottenuto come combinazione lineare di $\mathbf{w}_a$ e $\mathbf{w}_b$. Viceversa, ogni portafoglio generato come combinazione lineare di $\mathbf{w}_a$ e $\mathbf{w}_b$ è un portafoglio a varianza minima. In particolare, se $\mathbf{w}_a$ e $\mathbf{w}_b$ sono portafogli a varianza minima **efficienti** — sotto gli stessi vincoli — allora
> $$\alpha\mathbf{w}_a + (1-\alpha)\mathbf{w}_b$$
> è un portafoglio a varianza minima efficiente per $0\le \alpha \le 1$.
>
> **Implicazioni.** Ogni portafoglio sulla frontiera a varianza minima può essere formato come combinazione lineare di qualsiasi altra coppia di portafogli a varianza minima. Pertanto, un investitore potrebbe raggiungere un'allocazione ottima selezionando una combinazione di due portafogli a varianza minima (arbitrari), invece di scegliere tra gli $N$ titoli originari. Di conseguenza, due fondi comuni (portafogli) forniscono agli investitori tutte le scelte necessarie, purché siano portafogli a varianza minima.
>
> Siano $\mathbf{w}_a$ e $\mathbf{w}_b$ portafogli a varianza minima e sia $\mathbf{w}_c$ una loro combinazione lineare:
> $$\mathbf{w}_c = \alpha\mathbf{w}_a + (1-\alpha)\mathbf{w}_b$$
> Il rendimento atteso di $\mathbf{w}_c$ è la media ponderata dei rendimenti attesi di $\mathbf{w}_a$ e $\mathbf{w}_b$:
> $$E(r_c) = \alpha E(r_a) + (1-\alpha)E(r_b)$$
> Ne consegue che i pesi di portafoglio per un portafoglio sulla MVF sono funzioni lineari del suo rendimento atteso:
> $$\alpha = \frac{E(r_c)-E(r_b)}{E(r_a)-E(r_b)}$$
>
> **Esempio.**
>
> | Titolo | $E(r)$ | $w_a$ | $w_b$ | $w_c$ (50% in $w_a$ e $w_b$) |
> |---|---|---|---|---|
> | A | 10% | 50,0% | 30,0% | 40,0% |
> | B | 20% | 30,0% | 40,0% | 35,0% |
> | C | 30% | 20,0% | 30,0% | 25,0% |
> | $E(r_p)$ | | 17,0% | 20,0% | 18,5% |
>
> Se $\mathbf{w}_a$ e $\mathbf{w}_b$ sono portafogli a varianza minima, allora $\mathbf{w}_c = 0{,}5\,\mathbf{w}_a + 0{,}5\,\mathbf{w}_b$.

*(slide 96–99)*

## Frontiera efficiente con un titolo privo di rischio: indice di Sharpe e portafoglio di tangenza

> [!abstract] Definizione
> Per il teorema dei due fondi, ogni portafoglio a varianza minima può essere ottenuto come combinazione lineare di due portafogli a varianza minima. I due "fondi" da combinare in un portafoglio completo possono essere: il titolo privo di rischio, e un portafoglio rischioso lungo la frontiera efficiente dei titoli rischiosi. Il portafoglio rischioso più efficiente si individua massimizzando l'**indice di Sharpe** (Sharpe ratio), $SR_p$, per un dato tasso privo di rischio $r_f$:
> $$SR_p = \frac{E(r_p)-r_f}{\sigma_p}$$
>
> **Portafoglio completo: esempio.** Valore di mercato complessivo = \$300.000; MMF privo di rischio = \$90.000; Azioni = \$113.400; Obbligazioni = \$96.600; Totale titoli rischiosi = \$210.000. Pesi del portafoglio rischioso:
> $$w_E = \frac{113.400}{210.000} = 0{,}54 \qquad w_D = \frac{96.600}{210.000} = 0{,}46$$
> Pesi del portafoglio completo ($y$: peso del portafoglio rischioso):
> $$y = \frac{210.000}{300.000} = 0{,}7 \qquad 1-y = \frac{90.000}{300.000} = 0{,}3$$
> $$E = \frac{113.400}{300.000} = 0{,}378 \qquad D = \frac{96.600}{300.000} = 0{,}322$$
>
> **Il titolo privo di rischio.** Solo lo Stato può emettere titoli privi di rischio di insolvenza. Un titolo è privo di rischio in termini reali solo se il suo prezzo è indicizzato e la scadenza coincide con l'orizzonte di investimento dell'investitore. Le obbligazioni governative a breve scadenza e con elevato merito di credito sono spesso considerate titoli privi di rischio; in pratica, anche i fondi del mercato monetario sono spesso considerati privi di rischio.
>
> **Individuazione del portafoglio di tangenza: esempio.** Qualsiasi retta che colleghi $r_f$ (intercetta) a un dato portafoglio rischioso $p$ è detta **Capital Allocation Line (CAL)** — l'insieme dei portafogli ottenibili combinando linearmente $r_f$ e $p$.
>
> Portafoglio A: $E(r_A)=8{,}9\%$, $\sigma_A=11{,}45\%$:
> $$S_A = \frac{E(r_A)-r_f}{\sigma_A} = \frac{8{,}9\%-5\%}{11{,}45\%} = 0{,}34$$
> Portafoglio B: $E(r_B)=9{,}5\%$, $\sigma_B=11{,}70\%$:
> $$S_B = \frac{E(r_B)-r_f}{\sigma_B} = \frac{9{,}5\%-5\%}{11{,}70\%} = 0{,}38$$
> B domina A, ma è possibile fare meglio.
>
> **Individuazione geometrica del portafoglio di tangenza.** In termini geometrici, si mira a individuare la CAL tangente alla frontiera efficiente dei titoli rischiosi, cioè quella con la massima pendenza possibile ($=SR_p$). Ciò determina il **portafoglio di tangenza**.
>
> **Formulazione dell'ottimizzazione**:
> $$\max_{\mathbf{w}}\; SR_p = \frac{E(r_p)-r_f}{\sigma_p} \qquad \text{sub}\ \sum_{i=1}^N w_i=1,\ \ E(r_p)=\sum_{i=1}^N w_iE(r_i),\ \ \sigma_p = \sqrt{\sum_{i=1}^N\sum_{j=1}^N w_iw_j\sigma_{ij}}$$
> Il problema si risolve agevolmente numericamente.
>
> **Esempio — portafoglio di tangenza**: $E(r_p)=11\%$, $\sigma_p=14{,}2\%$,
> $$SR_p = \frac{E(r_p)-r_f}{\sigma_p} = \frac{11\%-5\%}{14{,}2\%} = 0{,}42$$
>
> **Intuizione economica.** Si ricerca la CAL con il massimo indice di Sharpe. Il portafoglio di tangenza viene detenuto da tutti, indipendentemente dal grado di avversione al rischio: investitori più avversi al rischio allocano una quota minore nel portafoglio di tangenza, investitori meno avversi al rischio ne allocano una quota maggiore. Il problema di scelta del portafoglio si scompone in due fasi indipendenti: la determinazione del portafoglio di tangenza è puramente tecnica; l'allocazione del portafoglio completo tra titolo privo di rischio e portafoglio di tangenza dipende dalle preferenze individuali verso il rischio.

*(slide 100–108)*

## L'equazione della frontiera efficiente con un titolo privo di rischio (CAL)

> [!tip] Teorema
> Si può costruire un portafoglio completo $C$ ripartendo i fondi tra il portafoglio di tangenza $T$ (peso $y$) e il titolo privo di rischio (peso $1-y$). Rendimento atteso del portafoglio completo:
> $$E(r_C) = y\,E(r_T) + (1-y)r_f$$
> Volatilità del portafoglio completo:
> $$\sigma_C = y\,\sigma_T$$
> Sostituendo $y=\sigma_C/\sigma_T$, si ottiene la frontiera efficiente con un titolo privo di rischio:
> $$E(r_C) = \underbrace{r_f}_{\text{intercetta}} + \underbrace{\frac{E(r_T)-r_f}{\sigma_T}}_{\text{pendenza } (SR_T)}\sigma_C$$
> In base al teorema dei due fondi, tale retta genera l'insieme delle opportunità di investimento efficienti: il modo più semplice per controllare il rischio consiste nel modificare il rapporto tra titoli rischiosi e titolo privo di rischio. Essa rappresenta la migliore CAL ottenibile.
>
> **Un esempio con tre titoli rischiosi e uno privo di rischio.** Si aggiunga un titolo privo di rischio con $r_f=3{,}5\%$ all'esempio con i tre titoli rischiosi A, B, C. Portafoglio di tangenza:
>
> | Titolo | Peso |
> |---|---|
> | $w_A$ | 1,84% |
> | $w_B$ | 47,04% |
> | $w_C$ | 51,12% |
> | $E(r_T)$ | 12,46% |
> | $\sigma_T$ | 21,70% |
> | $SR_T$ | 0,4131 |

*(slide 109–111)*

## Strategie passive e alcune evidenze empiriche

La **strategia passiva** evita l'analisi finanziaria dei titoli: le forze di domanda e offerta possono renderla ragionevole per molti investitori. Un candidato naturale per un titolo rischioso detenuto passivamente è l'S&P 500. La **Capital Market Line (CML)** è una CAL ottenuta investendo in due portafogli passivi: titoli di Stato a breve scadenza virtualmente privi di rischio (o un fondo del mercato monetario), e un fondo azionario che replica un ampio indice di mercato (si tornerà su questo punto nella lezione sul CAPM).

**Strategie passive: alcune evidenze.** Dal 1926 al 2015, il portafoglio rischioso passivo ha offerto in media un premio per il rischio pari a 8,3% con una deviazione standard di 20,59%, con un indice di Sharpe pari a 0,40. In media, il trading attivo tende a penalizzare i piccoli investitori.

**Figura (pag. 113)** — Evidenza empirica sulla relazione tra trading attivo e performance netta per gli investitori individuali. Fonte: Barber e Odean (2000). Mostra che una maggiore frequenza di trading è associata a rendimenti netti inferiori per il piccolo investitore.

**Figura (pag. 114)** — Ulteriore evidenza empirica sulle scelte di portafoglio degli investitori. Fonte: Calvet, Campbell e Sodini (2007).

*(slide 112–114)*

## La CAL: esempi numerici e il caso con tassi di prestito e di indebitamento differenti

> [!example] Esempio
> **CAL: esempio.** Dato un portafoglio rischioso $p$, con $r_f=7\%$, $E(r_p)=15\%$, $\sigma_{r_f}=0\%$, $\sigma_p=22\%$. Rendimento atteso del portafoglio completo:
> $$E(r_C) = y\,E(r_p) + (1-y)r_f = 7 + (15-7)y$$
> Volatilità del portafoglio completo:
> $$\sigma_C = y\,\sigma_p = 22y$$
> Pertanto:
> $$E(r_C) = r_f + \frac{\sigma_C}{\sigma_p}\left[E(r_p)-r_f\right] = 7 + \frac{8}{22}\sigma_C$$
>
> **Grafico (pag. 116)** — Rappresentazione della CAL così ottenuta nel piano $E(r_C)$–$\sigma_C$: retta con intercetta 7% e pendenza $8/22\approx 0{,}36$.
>
> **CAL con $r_f \ne$ tasso di indebitamento: esempio.** Si supponga di poter prestare a $r_f=7\%$ ma di poter prendere a prestito solo a $r_f^B=9\%$. La CAL con leva finanziaria presenta due tratti:
> - Pendenza nel "tratto di prestito" $= \dfrac{8}{22} = 0{,}36$
> - Pendenza nel "tratto di indebitamento" $= \dfrac{6}{22} = 0{,}27$
>
> La CAL cambia pendenza nel punto $P$ (il portafoglio rischioso pieno, $y=1$).
>
> **Figura (pag. 118)** — *L'insieme delle opportunità con $r_f \ne$ tasso di indebitamento*: in questo caso è possibile definire due distinti portafogli di tangenza, uno per il tratto "di prestito" (basato su $r_f=7\%$) e uno per il tratto "di indebitamento" (basato su $r_f^B=9\%$), con un tratto intermedio della frontiera efficiente dei soli titoli rischiosi che li collega.

*(slide 115–118)*

## Il portafoglio ottimale: massimizzazione dell'utilità e scelta della quota investita nel portafoglio rischioso

> [!note] Dimostrazione
> **3. Portafoglio ottimale.** Data la frontiera efficiente con un titolo privo di rischio, è possibile identificare il portafoglio ottimale lungo di essa, sulla base delle preferenze individuali dell'investitore rispetto al rischio. Si deve risolvere il seguente problema di massimizzazione vincolata dell'utilità:
> $$\max_{y}\; U(r_C) = E(r_C) - \frac12 A\sigma_C^2 \qquad \text{sub}\ E(r_C)=r_f+y\,E(r_T-r_f),\ \ \sigma_C^2 = y^2\sigma_T^2$$
>
> **Dimostrazione.** Sostituendo i vincoli nella funzione obiettivo:
> $$\max_{y}\; U(r_C) = \max_{y}\; r_f + y\,E(r_T-r_f) - \frac12 A y^2\sigma_T^2$$
> Condizione del primo ordine:
> $$\frac{\partial U(r_C)}{\partial y} = E(r_T-r_f) - Ay\sigma_T^2 = 0$$
> Soluzione:
> $$y^{*} = \frac{E(r_T)-r_f}{A\sigma_T^2}$$
>
> **Figure 6.5** — *Utility as a function of allocation to the risky asset, y.* Il grafico mostra l'utilità $U$ in funzione della quota $y$ allocata all'asset rischioso (asse orizzontale da 0 a 1,2): la curva cresce, raggiunge un massimo per un valore interno di $y$ (coerente con $y^{*}$) e poi decresce, illustrando graficamente la condizione del primo ordine appena derivata.

*(slide 119–122)*

## Curve di indifferenza e determinazione grafica del portafoglio ottimale: un esempio completo

> [!example] Esempio
> Si ricorda l'equazione delle curve di indifferenza: $E(r) = c + \tfrac12 A\sigma^2$, cioè, per un dato $A$ e un dato livello di utilità $U=c$: $E(r) = U + \tfrac{A}{2}\sigma^2$.
>
> **Table 6.5** — *Spreadsheet calculations of indifference curves (Entries in columns 2–4 are expected returns necessary to provide specified utility value).* Calcolata dalla formula $E(r) = U + \tfrac{A}{2}\sigma^2$ per $A=2$ (coefficiente $\tfrac{A}{2}=1$) e $A=4$ (coefficiente $\tfrac{A}{2}=2$), con $U=0{,}05$ e $U=0{,}09$:
>
> | $\sigma$ | $A=2,\ U=0{,}05$ | $A=2,\ U=0{,}09$ | $A=4,\ U=0{,}05$ | $A=4,\ U=0{,}09$ |
> |---|---|---|---|---|
> | 0 | 0,0500 | 0,0900 | 0,050 | 0,090 |
> | 0,05 | 0,0525 | 0,0925 | 0,055 | 0,095 |
> | 0,10 | 0,0600 | 0,1000 | 0,070 | 0,110 |
> | 0,15 | 0,0725 | 0,1125 | 0,095 | 0,135 |
> | 0,20 | 0,0900 | 0,1300 | 0,130 | 0,170 |
> | 0,25 | 0,1125 | 0,1525 | 0,175 | 0,215 |
> | 0,30 | 0,1400 | 0,1800 | 0,230 | 0,270 |
> | 0,35 | 0,1725 | 0,2125 | 0,295 | 0,335 |
> | 0,40 | 0,2100 | 0,2500 | 0,370 | 0,410 |
> | 0,45 | 0,2525 | 0,2925 | 0,455 | 0,495 |
> | 0,50 | 0,3000 | 0,3400 | 0,550 | 0,590 |
>
> **Figura (pag. 124)** — Grafico con la CAL dell'esempio precedente ($r_f=7\%$, punto $P$ con $E(r_p)=15\%$, $\sigma_p=22\%$) e quattro curve di indifferenza (per $A=4$) corrispondenti ai livelli di utilità $U=0{,}07$; $U=0{,}078$; $U=0{,}08653$; $U=0{,}094$. Il punto di tangenza $C$ tra la CAL e la curva $U=0{,}08653$ individua il portafoglio ottimale completo. Seguendo la notazione adottata sopra, in questo caso il portafoglio $P$ corrisponde al portafoglio $T$.
>
> **Table 6.6** — *Expected returns on four indifference curves and the CAL (Investor's risk aversion is $A=4$).* Colonna CAL calcolata come $E(r)=r_f+\frac{E(r_p)-r_f}{\sigma_p}\sigma = 0{,}07+\frac{8}{22}\sigma$; colonne $U$ calcolate come $E(r)=U+2\sigma^2$ (poiché $A=4$):
>
> | $\sigma$ | $U=0{,}07$ | $U=0{,}078$ | $U=0{,}08653$ | $U=0{,}094$ | CAL |
> |---|---|---|---|---|---|
> | 0 | 0,0700 | 0,0780 | 0,0865 | 0,0940 | 0,0700 |
> | 0,02 | 0,0708 | 0,0788 | 0,0873 | 0,0948 | 0,0773 |
> | 0,04 | 0,0732 | 0,0812 | 0,0897 | 0,0972 | 0,0845 |
> | 0,06 | 0,0772 | 0,0852 | 0,0937 | 0,1012 | 0,0918 |
> | 0,08 | 0,0828 | 0,0908 | 0,0993 | 0,1068 | 0,0991 |
> | 0,0902 | 0,0863 | 0,0943 | 0,1028 | 0,1103 | 0,1028 |
> | 0,10 | 0,0900 | 0,0980 | 0,1065 | 0,1140 | 0,1064 |
> | 0,12 | 0,0988 | 0,1068 | 0,1153 | 0,1228 | 0,1136 |
> | 0,14 | 0,1092 | 0,1172 | 0,1257 | 0,1332 | 0,1209 |
> | 0,18 | 0,1348 | 0,1428 | 0,1513 | 0,1588 | 0,1355 |
> | 0,22 | 0,1668 | 0,1748 | 0,1833 | 0,1908 | 0,1500 |
> | 0,26 | 0,2052 | 0,2132 | 0,2217 | 0,2292 | 0,1645 |
> | 0,30 | 0,2500 | 0,2580 | 0,2665 | 0,2740 | 0,1791 |
>
> Si noti che alla riga $\sigma=0{,}0902$ la colonna CAL (0,1028) coincide con la colonna $U=0{,}08653$ (0,1028): è esattamente il punto di tangenza $C$ mostrato nella figura precedente, con $\sigma_C\approx 0{,}0902$ ed $E(r_C)\approx 0{,}1028$.

*(slide 123–125)*

## Determinazione del portafoglio ottimale: un esempio completo con fondo azionario e obbligazionario

> [!example] Esempio
> Si torni all'esempio con il fondo azionario e il fondo obbligazionario (portafoglio di tangenza $E(r_P)=11\%$, $\sigma_P=14{,}2\%$, $r_f=5\%$) e si ponga $A=4$:
> $$y^{*} = \frac{E(r_P)-r_f}{A\sigma_P^2} = \frac{11\%-5\%}{4\times(14{,}2\%)^2} = 0{,}7439$$
> Seguendo la notazione adottata sopra, qui il portafoglio $P$ corrisponde al portafoglio $T$.
>
> **Grafico (pag. 126)** — Piano $E(r)$–$\sigma$ (in %) con: la retta CAL($P$) tangente all'insieme dei portafogli rischiosi ("Opportunity Set of Risky Assets") nel punto $P$ ("Optimal Risky Portfolio"); una curva di indifferenza tangente alla CAL nel punto indicante il "Optimal Complete Portfolio"; e il punto $r_f=5\%$ come intercetta. Illustra graficamente la soluzione $y^{*}=0{,}7439$ come combinazione tra titolo privo di rischio e portafoglio di tangenza $P$.
>
> **Le proporzioni del portafoglio completo ottimale.** Con $E(r_P)=11\%$, $\sigma_P=14{,}2\%$, $y=0{,}7439$, $r_f=5\%$:
> $$E(r_{C^{*}}) = y\times E(r_P) + (1-y)\times r_f = 0{,}7439\times 11\% + 0{,}2561\times 5\% = 9{,}46\%$$
> $$\sigma_{C^{*}} = 0{,}7439\times 14{,}2\% = 10{,}56\%$$
> $$SR_{C^{*}} = \frac{9{,}46\%-5\%}{10{,}56\%} = 0{,}42$$
>
> **Grafico (pag. 127)** — Diagramma a torta del portafoglio completo ottimale: "Portfolio P" pesa 74,39% del totale ed è a sua volta composto da Stocks (44,63% del totale) e Bonds (29,76% del totale); il restante 25,61% è in T-bills (titolo privo di rischio). Illustra concretamente come la scelta ottima si traduca in un'allocazione tra titoli azionari, obbligazionari e privi di rischio.

*(slide 126–127)*
