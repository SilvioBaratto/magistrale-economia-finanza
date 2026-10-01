---
title: "Metodi per la Gestione di Portafogli Personali – Parte 3: Criterio Media-Varianza, Utilità Attesa e Selezione di Portafoglio con Titolo Privo di Rischio"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-3.pdf"
pages: 48
text_layer: true
verified: true
generated: 2026-07-10
---

## Consistenza tra il criterio media-varianza e il criterio dell'utilità attesa

> [!tip] Teorema
> **Domanda.** Il criterio di dominanza media-varianza è consistente con quello dell'utilità attesa?
>
> **Risposta.** Il criterio di dominanza media-varianza è consistente con quello dell'utilità attesa solo sotto due circostanze fra loro mutuamente esclusive:
>
> - o quando la funzione di utilità dell'agente economico, espressa in termini di $R_P$, è quella **quadratica**, cioè
> $$U(R_P) = R_P - \frac{a}{2}R_P^2, \quad \text{con } a>0;$$
> - oppure quando la funzione di distribuzione di probabilità congiunta di $R_1,\dots,R_N$ è una **multivariata ellittica**.
>
> **Domanda.** Che cos'è una distribuzione ellittica?
>
> **Risposta.** Senza entrare nei dettagli tecnici, una distribuzione ellittica è una distribuzione di probabilità caratterizzata dal fatto che le sue superfici di equi-densità sono ellissoidi.
>
> **Osservazioni.**
> - La funzione di utilità quadratica $U(X)$ ha un difetto ben noto: è crescente solo quando $X < 1/a$. Quindi, per utilizzarla correttamente, tutte le realizzazioni di $X$ devono essere inferiori a $1/a$.
> - Fra le altre, la distribuzione normale multivariata e la distribuzione $t$ di Student multivariata sono casi particolari di distribuzioni ellittiche multivariate.
>
> Come ammonisce la letteratura:
>
> > «if one uses a variance-covariance model for non–elliptic distributions one can severely underestimate events that cause the most severe losses.»
> > — Szegö G., *Measures of risk*, European Journal of Operational Research, 2005 (pag. 6)

*(slide 2–6)*

## Dimostrazione: la funzione di utilità quadratica è consistente col criterio media-varianza

> [!note] Dimostrazione
> Si consideri la funzione di utilità quadratica espressa in termini di $R_P$:
> $$U(R_P) = R_P - \frac{a}{2}R_P^2, \quad \text{con } a>0.$$
>
> Il suo valore atteso è
> $$
> \mathbb E[U(R_P)] = \mathbb E\left(R_P - \frac{a}{2}R_P^2\right) = \cdots = \mathbb E(R_P) - \frac{a}{2}\mathbb E\left(R_P^2\right) = r_P - \frac{a}{2}\left(r_P^2+\sigma_P^2\right).
> $$
>
> Questo valore atteso dipende **solo** da $r_P$ e da $\sigma_P^2$. Dunque, per la funzione di utilità quadratica espressa in termini di $R_P$, il criterio di dominanza dell'utilità attesa è consistente con quello media-varianza. $\blacksquare$
>
> **Osservazione — la curva di indifferenza è una circonferenza.** La generica curva di indifferenza della funzione di utilità quadratica attesa,
> $$
> r_P - \frac{a}{2}\left(r_P^2 - \sigma_P^2\right) = k,
> $$
> è una circonferenza. Infatti è facile riformularla come
> $$
> \sigma_P^2 + r_P^2 - \frac{2}{a}r_P + \frac{2}{a}k = 0,
> $$
> che è esattamente la rappresentazione canonica di una circonferenza di centro $\left(0,\dfrac1a\right)$ e di raggio $\sqrt{\dfrac{1-2ak}{a^2}}$.

*(slide 7–9)*

## Selezione del portafoglio ottimo tramite tangenza tra frontiera efficiente e curva di indifferenza

**Domanda.** Assumendo che il criterio di dominanza media-varianza sia consistente con quello dell'utilità attesa, come si individua il portafoglio (fra quelli efficienti) che massimizza l'utilità attesa?

**Risposta.** Scegliendo il portafoglio per il quale la frontiera efficiente è tangente alla curva di indifferenza dell'utilità attesa caratterizzata dal più alto valore di livello.

**Figura** — Piano $\mathrm E(X)$–$\mathrm{Var}(X)$: la frontiera efficiente (curva crescente e concava verso il basso) e una famiglia di curve di indifferenza (archi di circonferenza crescenti verso l'alto-sinistra, nella direzione della freccia che indica livelli di utilità più alti). Il punto $\mathbf X^{*}$ è il portafoglio ottimo, individuato dal punto di tangenza tra la frontiera efficiente e la curva di indifferenza di livello più alto raggiungibile.

*(slide 10–11)*

## Il caso N ≥ 2 titoli rischiosi e 1 titolo privo di rischio: formalizzazione

> [!abstract] Definizione
> **Domanda.** È possibile effettuare la selezione di portafoglio considerando, oltre ai titoli rischiosi, anche titoli privi di rischio?
>
> **Risposta.** Sì: in ogni mercato finanziario sono disponibili attività prive di rischio (conti correnti, non ovunque; titoli di Stato; ecc.).
>
> **Notazione.** Si considerino:
> - $X_1,\dots,X_N$: $N$ scelte di investimento rischiose;
> - $R_1,\dots,R_N$: i tassi di rendimento (aleatori) di $X_1,\dots,X_N$, rispettivamente;
> - $X_{N+1}$: la scelta di investimento priva di rischio più redditizia fra quelle disponibili;
> - $r_{N+1}$: il tasso di rendimento (deterministico) di $X_{N+1}$ (ovviamente $\mathbb E(r_{N+1})=r_{N+1}$, $\mathbb{Var}(r_{N+1})=0$ e $\rho_{i,N+1}=0$ per ogni $i=1,\dots,N$);
> - $\tilde{\mathbf r}' = (r_1,\dots,r_N,r_{N+1}) = (\mathbf r', r_{N+1})$: il vettore $(N+1)$-dimensionale delle medie di $R_1,\dots,R_N,R_{N+1}$, dove $\mathbf r$ ha il significato usuale;
>
> $$
> \tilde{\mathbf V} = \begin{pmatrix}
> \sigma_1^2 & \sigma_{1,2} & \cdots & \sigma_{1,N-1} & \sigma_{1,N} & 0 \\
> \sigma_{2,1} & \sigma_2^2 & \cdots & \sigma_{2,N-1} & \sigma_{2,N} & 0 \\
> \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
> \sigma_{N-1,1} & \sigma_{N-1,2} & \cdots & \sigma_{N-1}^2 & \sigma_{N-1,N} & 0 \\
> \sigma_{N,1} & \sigma_{N,2} & \cdots & \sigma_{N,N-1} & \sigma_N^2 & 0 \\
> 0 & 0 & \cdots & 0 & 0 & 0
> \end{pmatrix}
> = \begin{pmatrix}\mathbf V & \mathbf 0_N \\ \mathbf 0_N' & 0 \end{pmatrix}:
> $$
> la matrice $(N+1)\times(N+1)$ di varianze e covarianze di $R_1,\dots,R_N,R_{N+1}$, dove $\mathbf V$ ha il significato usuale;
>
> - $\tilde{\mathbf e}' = (\mathbf e', 1)$: il vettore $(N+1)$-dimensionale di uni, dove $\mathbf e$ ha il significato usuale;
> - $\tilde{\mathbf x}' = (x_1,\dots,x_N,x_{N+1}) = (\mathbf x', x_{N+1})$: il vettore $(N+1)$-dimensionale delle percentuali del capitale (iniziale) da investire in $X_1,\dots,X_N,X_{N+1}$, dove $\mathbf x$ ha il significato usuale.
>
> **Ipotesi aggiuntive:**
> - $r_{N+1} < \max_i\{r_i,\ i=1,\dots,N\}$;
> - ipotesi di mercato senza frizioni (*Frictionless Market*);
> - ipotesi di agente price-taker (*Price–Taker*);
> - ipotesi di assenza di restrizioni istituzionali (*No–Institutional Restrictions*) — prima parte;
> - «if there exists a riskless security, then the borrowing rate equals the lending rate.» (*No–Institutional Restrictions*, seconda parte) — Merton R.C., *Continuous–Time Finance*, 1990 (pag. 18).
>
> **Formulazione del problema.** La versione del problema di selezione di portafoglio relativa al caso $N\ge 2$ titoli rischiosi e 1 titolo privo di rischio è:
> $$
> \min_{x_1,\dots,x_{N+1}} \ \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}
> $$
> $$
> \text{s.t.} \quad \begin{cases} \tilde{\mathbf x}'\tilde{\mathbf r} = \pi \\ \tilde{\mathbf x}'\tilde{\mathbf e} = 1 \end{cases}
> $$

*(slide 12–17)*

## Proprietà della forma quadratica associata al problema con titolo privo di rischio

> [!note] Dimostrazione
> **Osservazioni.** Se gli $R_i$, con $i=1,\dots,N$, non sono variabili aleatorie degeneri, cioè se $\sigma_i^2>0$ per $i=1,\dots,N$, allora:
>
> - $\dfrac{\partial^2 \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}}{\partial x_i^2} = 2\sigma_i^2 > 0$ per $i=1,\dots,N$, mentre $\dfrac{\partial^2 \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}}{\partial x_{N+1}^2} = 0$ (perciò $\tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}$ **non** è una funzione concava);
> - $\tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}$, che è una varianza, è positiva per ogni $\tilde{\mathbf x}\neq \tilde{\mathbf 0}_{N+1}$, dove $\tilde{\mathbf 0}_{N+1}$ è il vettore $(N+1)$-dimensionale di zeri (perciò $\tilde{\mathbf V}$ è una matrice definita positiva).
>
> **Verifica.** Sviluppando la forma quadratica:
> $$
> \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x} = \sum_{i=1}^{N+1} x_i^2\sigma_i^2 + 2\sum_{i=1}^{N+1}\sum_{j=i+1}^{N+1} x_1x_j\rho_{i,j}\sigma_i\sigma_j
> $$
> $$
> = \sum_{i=1}^{N} x_i^2\sigma_i^2 + \underbrace{x_{N+1}^2\sigma_{N+1}^2}_{=0} + 2\sum_{i=1}^{N}\sum_{j=i+1}^{N} x_1x_j\rho_{i,j}\sigma_i\sigma_j + \underbrace{2\sum_{i=1}^{N} x_ix_{N+1}\rho_{i,N+1}\sigma_1\sigma_{N+1}}_{=0} = \mathbf x'\mathbf V\mathbf x.
> $$
>
> Poiché $\sigma_{N+1}^2=0$ e $\rho_{i,N+1}=0$, i termini contenenti $x_{N+1}$ si annullano, e la forma quadratica estesa $\tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}$ si riduce esattamente a $\mathbf x'\mathbf V\mathbf x$, la varianza del solo sottoportafoglio rischioso.

*(slide 18–19)*

## Teorema di soluzione del problema di selezione di portafoglio con titolo privo di rischio

> [!tip] Teorema
> Si risolve ora la versione del problema di selezione di portafoglio relativa al caso $N\ge2$ titoli rischiosi e 1 titolo privo di rischio.
>
> **Teorema.** Sia $\tilde{\mathbf V}$ una matrice $(N+1)\times(N+1)$ di varianze e covarianze e sia $\tilde{\mathbf r}$ un vettore $(N+1)$-dimensionale di medie. Se $\mathbf V$ è non singolare e definita positiva, e se $r_i\neq r_j$ per qualche $i,j=1,\dots,N+1$, allora il problema di selezione di portafoglio considerato ha la seguente soluzione unica:
> $$
> \tilde{\mathbf x}^{*\prime} = \left(\mathbf x_N^{*\prime}, x_{N+1}^{*}\right)
> $$
> dove
> $$
> \mathbf x_N^{*} = \frac{\pi - r_{N+1}}{\gamma r_{N+1}^2 - 2\beta r_{N+1} + \alpha}\, \mathbf V^{-1}(\mathbf r - r_{N+1}\mathbf e),
> $$
> $$
> x_{N+1}^{*} = \frac{\pi(\gamma r_{N+1}-\beta) + \alpha - \beta r_{N+1}}{\gamma r_{N+1}^2 - 2\beta r_{N+1} + \alpha},
> $$
> con
> $$
> \alpha = \mathbf r'\mathbf V^{-1}\mathbf r, \qquad \beta = \mathbf r'\mathbf V^{-1}\mathbf e = \mathbf e'\mathbf V^{-1}\mathbf r, \qquad \gamma = \mathbf e'\mathbf V^{-1}\mathbf e.
> $$
>
> **Osservazione.** In generale $\mathbf x_N^{*}\neq \mathbf x^{*}$ (la soluzione del sotto-vettore rischioso non coincide con la soluzione del problema senza titolo privo di rischio).
>
> **Dimostrazione (sketch of proof).**
>
> Si forma la Lagrangiana:
> $$
> \mathfrak L = \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x} - \lambda_1(\tilde{\mathbf x}'\tilde{\mathbf r}-\pi) - \lambda_2(\tilde{\mathbf x}'\tilde{\mathbf e}-1) = \mathbf x'\mathbf V\mathbf x - \lambda_1(\tilde{\mathbf x}'\tilde{\mathbf r}-\pi)-\lambda_2(\tilde{\mathbf x}'\tilde{\mathbf e}-1).
> $$
>
> Si ottiene il sistema delle condizioni del primo ordine:
> $$
> \begin{cases}
> \dfrac{\partial \mathfrak L}{\partial \mathbf x} = 2\mathbf x'\mathbf V - \lambda_1\mathbf r' - \lambda_2\mathbf e' = \mathbf 0_N \\[4pt]
> \dfrac{\partial \mathfrak L}{\partial x_{N+1}} = -\lambda_1 r_{N+1} - \lambda_2 = 0 \\[4pt]
> \dfrac{\partial \mathfrak L}{\partial \lambda_1} = -\tilde{\mathbf x}'\tilde{\mathbf r}+\pi = -\mathbf x'\mathbf r - x_{N+1}r_{N+1}+\pi = 0 \\[4pt]
> \dfrac{\partial \mathfrak L}{\partial \lambda_2} = -\tilde{\mathbf x}'\tilde{\mathbf e}+1 = -\mathbf x'\mathbf e - x_{N+1}+1 = 0
> \end{cases}
> $$
>
> Questo sistema ha soluzione unica se il determinante della matrice dei coefficienti è diverso da zero, cioè se
> $$
> \begin{vmatrix}
> 2\mathbf V & \mathbf 0_N & \mathbf r & \mathbf e \\
> \mathbf 0_N' & 0 & r_{N+1} & 1 \\
> \mathbf r' & r_{N+1} & 0 & 0 \\
> \mathbf e' & 1 & 0 & 0
> \end{vmatrix} \neq 0.
> $$
> È possibile dimostrare che questa condizione è soddisfatta sotto le ipotesi fatte su $\mathbf V$ e $\tilde{\mathbf r}$.
>
> Ricordando che $\mathbf V$ è non singolare, dopo alcuni passaggi il sistema si riscrive come:
> $$
> \begin{cases}
> \mathbf x' = \dfrac12\lambda_1\mathbf r'\mathbf V^{-1} + \dfrac12\lambda_2\mathbf e'\mathbf V^{-1} \\[4pt]
> \lambda_1 r_{N+1}+\lambda_2 = 0 \\[4pt]
> \mathbf x'\mathbf r + x_{N+1}r_{N+1} = \pi \\[4pt]
> \mathbf x'\mathbf e + x_{N+1} = 1
> \end{cases}
> $$
>
> Sostituendo l'espressione ottenuta per $\mathbf x'$ nelle ultime due condizioni del primo ordine, dopo ulteriori passaggi il sistema diventa:
> $$
> \begin{cases}
> \mathbf x' = \dfrac12\lambda_1\mathbf r'\mathbf V^{-1} + \dfrac12\lambda_2\mathbf e'\mathbf V^{-1} \\[6pt]
> \dfrac12\lambda_2 = \dfrac{-\pi r_{N+1}+r_{N+1}^2}{\gamma r_{N+1}^2 - 2\beta r_{N+1}+\alpha} \\[6pt]
> \dfrac12\lambda_1 = \dfrac{\pi - r_{N+1}}{\gamma r_{N+1}^2 -2\beta r_{N+1}+\alpha} \\[6pt]
> x_{N+1} = 1 - \dfrac12\lambda_1(\beta - \gamma r_{N+1})
> \end{cases}
> $$
>
> Infine, sostituendo le espressioni ottenute per $\tfrac12\lambda_1$ e $\tfrac12\lambda_2$ in quelle ottenute per $\mathbf x'$ e $x_{N+1}$, e trasponendo $\mathbf x'$, si ottiene:
> $$
> \mathbf x_M^{*} = \frac{\pi - r_{N+1}}{\gamma r_{N+1}^2 - 2\beta r_{N+1} + \alpha}\, \mathbf V^{-1}(\mathbf r - r_{N+1}\mathbf e)
> $$
> e
> $$
> x_{N+1}^{*} = \frac{\pi(\gamma r_{N+1}-\beta) + \alpha - \beta r_{N+1}}{\gamma r_{N+1}^2 - 2\beta r_{N+1} + \alpha}. \qquad \blacksquare
> $$

*(slide 20–28)*

## Media, varianza e deviazione standard del portafoglio ottimo: la frontiera efficiente con titolo privo di rischio

> [!tip] Teorema
> Con riferimento alla soluzione del problema con $N\ge2$ titoli rischiosi e 1 titolo privo di rischio:
>
> - $\mathbb E(R_{P^*}) = r_{P^*} = \tilde{\mathbf x}^{*\prime}\tilde{\mathbf r}^{*} = \pi$ (ovviamente, per costruzione);
> - $\mathbb{Var}(R_{P^*}) = \sigma_{P^*}^2 = \cdots = \tilde{\mathbf x}^{*\prime}\tilde{\mathbf V}^{*}\tilde{\mathbf x}^{*} = \dfrac{(\pi-r_{N+1})^2}{\gamma r_{N+1}^2 - 2\beta r_{N+1}+\alpha}$, che descrive una **parabola** nel piano varianza-media;
> - $\mathbb{S}t\mathbb{D}ev(R_{P^*}) = \sigma_{P^*} = \left(\mathbf x^{*\prime}\mathbf V\mathbf x^{*}\right)^{1/2} = \cdots = \left(\dfrac{(\pi-r_{N+1})^2}{\gamma r_{N+1}^2-2\beta r_{N+1}+\alpha}\right)^{1/2} = \dfrac{|\pi-r_{N+1}|}{\sqrt{\gamma r_{N+1}^2-2\beta r_{N+1}+\alpha}}$
> $$
> = \begin{cases}
> \dfrac{\pi-r_{N+1}}{\sqrt{\gamma r_{N+1}^2-2\beta r_{N+1}+\alpha}} & \text{se } \pi\ge r_{N+1} \\[8pt]
> \dfrac{r_{N+1}-\pi}{\sqrt{\gamma r_{N+1}^2-2\beta r_{N+1}+\alpha}} & \text{se } \pi < r_{N+1}
> \end{cases}
> $$
> che descrive la frontiera dei portafogli nel piano deviazione standard-media (frontiera fatta di due semirette, per la presenza del titolo privo di rischio).

*(slide 29–30)*

## Esempio numerico: portafoglio con tre titoli azionari italiani e un conto corrente

> [!example] Esempio
> Si illustra il tipico comportamento delle frontiere dei portafogli, nei rispettivi piani di riferimento, tramite l'esempio che segue.
>
> Sia $\mathbb X$ l'insieme delle scelte di investimento costituito dalle seguenti attività finanziarie del mercato azionario italiano:
> - $X_1 =$ Alleanza Assicurazioni;
> - $X_2 =$ Fondiaria–Sai;
> - $X_3 =$ Unicredito Italiano;
> - $X_4 =$ conto corrente bancario (*bank account*).
>
> Le medie, le varianze e i coefficienti di correlazione lineare relativi ai tassi di rendimento di $X_1$, $X_2$ e $X_3$ (valutati su dati giornalieri dal 23 agosto 2006 al 21 settembre 2006), rispettivamente, sono:
>
> $$r_1 = 4.037\text E{-}04 \text{ e } \sigma_1^2 = 1.229\text E{-}04;$$
> $$r_2 = 9.901\text E{-}04 \text{ e } \sigma_2^2 = 1.514\text E{-}04;$$
> $$r_3 = 1.213\text E{-}03 \text{ e } \sigma_3^2 = 7.794\text E{-}05;$$
> $$\rho_{1,2} = 1.600\text E{-}01,\quad \rho_{1,3} = -8.291\text E{-}02, \quad \rho_{2,3} = 4.150\text E{-}01.$$
>
> Il tasso di rendimento (giornaliero) di $X_4$ è:
> $$r_4 = 7.500\text E{-}04.$$
>
> **Portafogli ottimi al variare di $\pi$:**
>
> | $\pi$ | $(x_1^*, x_2^*, x_3^*, x_4^*)$ |
> |---|---|
> | $-0.00300$ | $(2.739, -0.737, -5.666, 4.664)$ |
> | $\cdots$ | $\cdots$ |
> | $-0.00175$ | $(1.826, -0.491, -3.778, 3.443)$ |
> | $\cdots$ | $\cdots$ |
> | $0.00050$ | $(0.183, -0.049, -0.378, 1.244)$ |
> | $\cdots$ | $\cdots$ |
> | $0.00225$ | $(-1.096, 0.295, 2.267, -0.466)$ |
> | $\cdots$ | $\cdots$ |
> | $0.00400$ | $(-2.374, 0.639, 4.911, -2.176)$ |
>
> **Figura (pag. 35)** — Piano $\mathrm E(X)$–$\mathrm{Var}(X)$: sono riportati la frontiera efficiente (punti «+»), la frontiera inefficiente (punti «×»), e i tre titoli rischiosi presi singolarmente: Alleanza Assicurazioni (▲), Fondiaria–Sai (■), Unicredito Italiano (●). La frontiera ha la tipica forma a parabola con vertice a sinistra; i tre titoli singoli, non diversificati, giacciono ben all'interno della regione dominata dalla frontiera, a conferma del beneficio della diversificazione.
>
> **Figura (pag. 36)** — Stesso confronto nel piano $\mathrm E(X)$–$\mathrm{StDev}(X)$: la frontiera assume la caratteristica forma a "V" leggermente ricurva (rami quasi rettilinei, per l'effetto del titolo privo di rischio $X_4$), con i medesimi punti rappresentativi dei tre titoli rischiosi ben interni ad essa.

*(slide 31–36)*

## Confronto tra il caso di soli titoli rischiosi e il caso con titolo privo di rischio

Si richiama la regola di scelta del portafoglio ottimo già enunciata: assumendo la consistenza tra criterio media-varianza e criterio dell'utilità attesa, il portafoglio che massimizza l'utilità attesa è quello per cui la frontiera efficiente è tangente alla curva di indifferenza di livello più alto.

**Domanda.** Quali sono le differenze fra il caso "$N\ge2$ titoli rischiosi" e il caso "$N\ge2$ titoli rischiosi e 1 titolo privo di rischio"?

**Risposta.** Le si illustra qualitativamente e quantitativamente tramite le figure che seguono, riferite all'esempio dei tre titoli azionari italiani più il conto corrente.

**Figura (pag. 39)** — Piano $\mathrm E(X)$–$\mathrm{Var}(X)$: sono sovrapposte la frontiera efficiente/inefficiente del caso a soli titoli rischiosi (curva più esterna, a forma di parabola, già vista nell'esempio precedente) e quella del caso con il titolo privo di rischio aggiunto (curva più interna, tangente alla precedente). Il confronto mostra che l'introduzione del titolo privo di rischio consente di ottenere, per lo stesso livello di rendimento atteso $\pi$, una varianza uguale o inferiore rispetto al caso di soli titoli rischiosi: la frontiera si sposta verso sinistra.

**Figura (pag. 40)** — Stesso confronto nel piano $\mathrm E(X)$–$\mathrm{StDev}(X)$: la frontiera del caso con titolo privo di rischio (rami pressoché rettilinei) risulta tangente e più stretta rispetto a quella del caso di soli titoli rischiosi (curva a "naso" più ampia), illustrando come la possibilità di investire nell'attività priva di rischio migliori il trade-off rischio-rendimento disponibile all'investitore.

*(slide 37–40)*

## Il caso "nessuna vendita allo scoperto consentita": vincoli di non negatività

> [!abstract] Definizione
> Non tutti gli investitori possono effettuare vendite allo scoperto (*short-selling*). Questo divieto si formalizza aggiungendo, al problema di selezione di portafoglio, vincoli di non negatività su ciascuna percentuale del capitale (iniziale) da investire nelle varie scelte di investimento, cioè:
> $$
> x_i \ge 0 \quad \text{per ogni } i=1,\dots,N \ \text{ oppure } \ i=1,\dots,N+1.
> $$
>
> Adottando la notazione già introdotta per il caso "$N\ge2$ titoli rischiosi e 1 titolo privo di rischio", e mantenendo le ipotesi di mercato senza frizioni, di agente price-taker e di assenza di restrizioni istituzionali (solo la prima parte), la versione del problema di selezione di portafoglio con vincoli di non negatività si formula come:
> $$
> \min_{x_1,\dots,x_{N+1}} \ \tilde{\mathbf x}'\tilde{\mathbf V}\tilde{\mathbf x}
> $$
> $$
> \text{s.t.} \quad \begin{cases} \tilde{\mathbf x}'\tilde{\mathbf r} = \pi \\ \tilde{\mathbf x}'\tilde{\mathbf e} = 1 \\ x_i \ge 0,\ i=1,\dots,N+1 \end{cases}
> $$

*(slide 41–42)*

## Teorema: la frontiera efficiente con vincoli di non negatività è un arco limitato

> [!tip] Teorema
> Come osserva Szegő:
>
> > «In the case ["$N\ge2$ risky investment choice(s) and 1 riskless" (or "$N\ge2$ risky investment choices")] the boundary turned out to be a parabola, i.e., the region of admissible portfolios is an unbounded portion of the [variance–mean plane], allowing the investor to obtain portfolios characterized by arbitrarily values of $\pi$ and $[\sigma^2]$. This is of course impossible when the nonnegativity constraint on the allocation vector is taken into account.»
> > — Szegö G.P., *Portfolio Theory. With Application to Bank Asset Management*, 1980 (pag. 130)
>
> Questa affermazione si formalizza nel teorema che segue.
>
> **Teorema.** Si consideri la versione del problema di selezione di portafoglio con vincoli di non negatività. Sia $r_{\min} = \min_i\{r_i,\ i=1,\dots,N+1\}$, sia $\sigma_{\min}^2$ la varianza dell'$R_i$ a cui corrisponde $\mathbb E(R_i)=r_{\min}$; sia $r_{\max} = \max_i\{r_i,\ i=1,\dots,N+1\}$, e sia $\sigma_{\max}^2$ la varianza dell'$R_i$ a cui corrisponde $\mathbb E(R_i)=r_{\max}$ (se esiste più di un $R_i$ a cui corrisponde $\mathbb E(R_i)=r_{\min}/r_{\max}$, allora $\sigma_{\min}^2/\sigma_{\max}^2$ è la più piccola varianza fra quelle corrispondenti). Allora la frontiera efficiente nel piano varianza-media è un **arco limitato** che ha come punti estremi $(\sigma_{\min}^2, r_{\min})$ e $(\sigma_{\max}^2, r_{\max})$.
>
> **Dimostrazione (sketch of proof).**
>
> > «Since [the nonnegativity constraints] does not allow short selling and borrowing, the largest value of $\pi$ can be achieved by investing the whole unit capital in the investment with the largest expected return $r_{\max}$, while the smallest value of $\pi$ can correspondingly be reached only by investing the whole capital unit in the investment with the smallest expected return $r_{\min}$.»
> > — Szegö G.P., *Portfolio Theory. With Application to Bank Asset Management*, 1980 (pag. 131)
>
> **Figura** — Piano $\mathrm E(X)$–$\mathrm{Var}(X)$: la frontiera efficiente (linea continua) è un arco limitato che va dal punto $(\sigma_{\min}^2, r_{\min})$ al punto $(\sigma_{\max}^2, r_{\max})$; la porzione tratteggiata al di sotto rappresenta la parte inefficiente. A differenza dei casi senza vincoli di non negatività (dove la frontiera è una parabola illimitata), qui la regione dei portafogli ammissibili è delimitata: l'investitore non può ottenere valori arbitrariamente estremi di $\pi$ e $\sigma^2$.

*(slide 43–46)*

## Nota sul metodo di risoluzione: le funzioni di penalità esterne

A causa della presenza dei vincoli di non negatività, in generale non è agevole determinare la soluzione ottima del problema di selezione di portafoglio con gli approcci risolutivi standard. Come osservano Corazza e Favaretto:

> «on account of the presence of non–negativity constraints, in general it is not easy to determine the optimal solution of [the considered portfolio selection] problem by standard solution approaches. Nevertheless, there exist some programming techniques by which it is possible to generate a sequence of closed form expressions converging, with the desired precision, to the optimal one [...]. In order to solve [the considered portfolio selection] problem, we use a programming technique which is based on the so–called external penalty functions.»
> — Corazza M. e Favaretto D., *On the existence of solutions to the quadratic mixed–integer mean–variance portfolio selection problem*, European Journal of Operational Research, 2007 (pag. 1948)

*(slide 47–48)*
