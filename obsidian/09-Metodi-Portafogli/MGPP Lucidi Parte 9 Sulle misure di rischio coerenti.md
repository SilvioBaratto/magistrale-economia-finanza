---
title: "Misure di rischio coerenti: VaR, TCE, WCE, Expected Shortfall e misure two-sided"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-9-Sulle-misure-di-rischio-coerenti.pdf"
pages: 16
text_layer: true
verified: true
generated: 2026-07-10
---

## Value at Risk (VaR): definizione, esempio e interpretazione grafica

> [!abstract] Definizione
> **Definizione.** Il VaR ad un livello di confidenza $\alpha \in [0;1]$, fissato un certo intervallo temporale (noto come *holding period*), indica qual è la **minima** perdita potenziale in cui il portafoglio sottostante può incorrere nell'$\alpha\%$ dei casi ed in un arco temporale pari all'*holding period*.
>
> **Esempio.** Se il VaR giornaliero al 5% di un portafoglio azionario è uguale a 50000 euro, allora vi è una probabilità del 5% che il valore del portafoglio perda almeno 50000 euro da un giorno all'altro. Informalmente, un tale VaR implica che il portafoglio in oggetto perda 50000 euro 1 giorno ogni 20 (1 è il 5% di 20).
>
> **Figura — Il Value-at-Risk come $(1-\alpha)$-esimo percentile della distribuzione dei rendimenti.** La figura mostra una distribuzione gaussiana dei "profitti e delle perdite" (asse orizzontale: rendimenti percentuali da $-3$ a $3$; asse verticale: probabilità da 0 a 0,45), con una linea verticale tratteggiata rossa posizionata poco a sinistra di $-1,6$ circa. Il testo a lato della figura precisa: "Il VaR al 95% è il quantile della distribuzione che lascia alla sua sinistra il 5% di probabilità":
> $$VaR_\alpha = \inf\{x \mid Pr(X>x) = \alpha\}.$$
> La conclusione grafica è che il VaR individua il punto della distribuzione oltre il quale (a sinistra) si concentra la probabilità $\alpha$ delle perdite peggiori.

*(slide 1–2)*

## Definizione probabilistica del VaR e sua critica

**Osservazione (definizione probabilistica).** Da un punto di vista probabilistico, il VaR a livello di confidenza $\alpha$ è quel valore il quale soddisfa la seguente uguaglianza:
$$P(L > VaR_\alpha) = 1-\alpha,$$
dove $L$ indica una generica distribuzione delle perdite.

**Osservazione (limite del VaR).** Essendo una misura indifferente a quanto ammontano realmente le perdite oltre la soglia, è possibile affermare che il VaR non si comporta in maniera idonea: non serve molta immaginazione per identificare portafogli con il medesimo $VaR_\alpha$, ma con livelli di perdite nel peggior $(1-\alpha)\%$ dei casi drammaticamente differenti.

**Figura — Distribuzione delle perdite di portafoglio (Portfolio loss).** L'istogramma di frequenza (Frequency) delle perdite di portafoglio mostra una distribuzione con una moda pronunciata vicino allo zero e una coda destra lunga e sottile. Sulla coda sono evidenziati, in ordine crescente: il **VaR**, il **CVaR** (posizionato più a destra del VaR, dentro la coda) e la **Maximum loss** (l'estremo destro della distribuzione osservata). L'intervallo tra VaR e Maximum loss è etichettato con "Probability $1-\beta$". La figura illustra visivamente come il VaR sia solo una soglia, mentre il CVaR si trovi più internamente nella coda e sintetizzi meglio la gravità delle perdite oltre tale soglia, fino alla perdita massima osservata.

**Osservazione (mancanza di coerenza del VaR).** Il V.a.R. non è una misura coerente di rischio perché in generale non soddisfa la proprietà di sub-additività. Uno dei pochi casi in cui la soddisfa è quando la distribuzione congiunta dei rendimenti è gaussiana.

*(slide 3–5)*

## Tail Conditional Expectation (TCE) e Worst Conditional Expectation (WCE)

> [!abstract] Definizione
> **Definizione (Tail Conditional Expectation).** La Tail Conditional Expectation (nota anche come "TailVaR") è una misura di rischio coerente definita come
> $$TCE_\alpha(X) \stackrel{def}{=} -E[X \mid X \le -VaR_\alpha(X)],$$
> in cui $X$ indica le performance del portafoglio.
>
> **Definizione (Worst Conditional Expectation).** La Worst Conditional Expectation è una misura di rischio coerente definita come
> $$WCE_\alpha(X) \stackrel{def}{=} -\inf\{E[X \mid A] \mid P[A] > \alpha\},$$
> in cui $A$ indica eventi/scenari sfavorevoli.

*(slide 6)*

## TCE, WCE e la loro relazione con il CVaR

**Osservazione (coincidenza con il CVaR).** Nel caso di variabili casuali continue, come generalmente si assume per i rendimenti finanziari, la TCE coincide con un'altra misura di rischio coerente: il cosiddetto Conditional Value at Risk (CvaR):
$$\frac{1}{\alpha}\int_0^\alpha VaR_\gamma(X)\, d\gamma.$$

**Osservazione ("how bad is bad").** Finanziariamente, la TCE e la WCE tengono conto di "how bad is bad" perché si focalizzano sulla forma della coda sinistra della distribuzione dei rendimenti — dove risiedono le perdite — e ne prendono il valor medio condizionatamente al fatto che le perdite siano superiori ad un certo valore.

**Osservazione (ordinamento tra le due misure).**
$$TCE_\alpha \le WCE_\alpha.$$

**Osservazione (Acerbi e Tasche, 2002b).** Acerbi e Tasche (2002b) evidenziano come, se da un lato la WCE risponda agli assiomi di coerenza, sebbene sia ampiamente diffusa solo in ambito teorico in quanto richiede la conoscenza dell'intero spazio di probabilità sottostante, dall'altro lato la TCE è sicuramente più maneggevole da utilizzare anche in ambito applicativo, seppur non soddisfi pienamente gli assiomi di coerenza in quanto non è sempre subadditiva.

*(slide 7–8)*

## Richiamo: la funzione di ripartizione

> [!abstract] Definizione
> Nel calcolo delle probabilità la **funzione di ripartizione**, o funzione di probabilità cumulata, di una variabile casuale $X$ a valori reali è la funzione che associa a ciascun valore $x$ la probabilità dell'evento "la variabile casuale $X$ assume valori minori o uguali ad $x$".
>
> In altre parole, è la funzione $F: \mathbb{R} \to [0,1]$ con dominio la retta reale e immagine l'intervallo $[0,1]$ definita da
> $$F(x) = P(X \le x).$$
>
> Una funzione $F$ è una valida funzione di ripartizione se è non decrescente, continua a destra e
> $$F(x) \ge 0, \quad \forall x$$
> $$\lim_{x\to+\infty} F(x) = 1$$
> $$\lim_{x\to-\infty} F(x) = 0$$
>
> Una funzione di ripartizione non è necessariamente continua a sinistra (e dunque continua globalmente): se $X$ è una variabile casuale discreta e $z$ un punto del suo supporto, allora $F$ è una funzione a gradino e dunque
> $$\lim_{x\to z^-} F(x) = \lim_{x\to z^-} \sum_{i=1}^n p(x_i) = \sum_{i=1}^n p(x_i)$$
> (ponendo senza restrizioni di generalità $x_1 < x_2 < \dots < x_n < x < z$) poiché è una costante indipendente da $x$, mentre
> $$F(z) = \sum_{i=1}^n p(x_i) + p(z)$$
> dunque essendo $p(z) \ne 0$ si ha che $F$ non è continua.

*(slide 9)*

## Expected Shortfall (ES): definizione e formule equivalenti

> [!abstract] Definizione
> **Definizione.** Data una distribuzione dei profitti e delle perdite $X$ e specificati *holding period* e livello di significatività $\alpha \in [0;1]$, l'Expected Shortfall è definito come segue:
> $$ES_\alpha(X) \stackrel{def}{=} -\frac{1}{\alpha}\Big(E\big[X\,\mathbb{1}_{\{X \le x^{(\alpha)}\}}\big] - x^{(\alpha)}\big(P[X \le x^{(\alpha)}] - \alpha\big)\Big),$$
> dove $x^{(\alpha)}$ equivale al $VaR_\alpha$.
>
> **Alternativamente.** Indicando con $F(x)$ la funzione di densità di probabilità tale che $P(X \le x)$ ed introducendo la funzione inversa di $F(x)$,
> $$F^{-1}(\alpha) = \inf\{x \mid F(x) \ge \alpha\},$$
> è dimostrabile (Acerbi e Tasche, 2002a), che l'ES può essere espressa come
> $$ES_\alpha(X) = -\frac{1}{\alpha}\int_0^\alpha F^{-1}(p)\, dp.$$
>
> **Figura — Il Value-at-Risk come $(1-\alpha)$-esimo percentile della distribuzione dei rendimenti.** Stessa distribuzione gaussiana di profitti e perdite già vista in precedenza, con la linea tratteggiata rossa che individua $VaR_\alpha$ e, più a sinistra nella coda (attorno a $-2,4$), un segmento verde aggiuntivo. Il segmento verde indica la posizione dell'Expected Shortfall nella coda della distribuzione: la figura mostra come l'ES si collochi più a sinistra del VaR, sintetizzando la gravità media delle perdite oltre la soglia individuata dal VaR anziché limitarsi alla sola soglia.

*(slide 10–11)*

## Proprietà dell'Expected Shortfall

**Osservazione (coincidenza con il CvaR).** Nel caso di variabili casuali continue, come generalmente si assume per i rendimenti finanziari, l'ES coincide con un'altra misura di rischio coerente: il cosiddetto CvaR.

**Osservazione (calcolo empirico ordinando le realizzazioni).** L'ES è ottenuta ordinando le $n$ possibili realizzazioni e, una volta fissato il livello di significatività desiderato, selezionando l'$(1-\alpha)\%$ delle maggiori perdite ottenendo il seguente risultato:
$$ES_\alpha(X) = -\frac{\sum_{i=1}^{w} X_{i:n}}{w},$$
dove $w$ rappresenta la parte intera di $n \times (1-\alpha)\%$ ovvero $w = \max\{m \mid m \le n(1-\alpha),\ m \in \mathbb{N}\}$.

**Osservazione (universalità e robustezza dell'ES).** L'ES risulta essere una misura di rischio universale, nel senso che è applicabile ad ogni strumento finanziario e ad ogni fonte di rischio sottostante. Inoltre, gode delle proprietà di semplicità e completezza, in quanto produce un unico numero anche nel caso di portafogli esposti a differenti fonti di rischio, e di robustezza, poiché a differenza delle altre misure di rischio basate sulla coda delle distribuzioni, utilizzando l'ES per la misurazione ci si assicura una certa convergenza nei risultati anche variando il livello di confidenza di qualche punto base. Quest'ultimo aspetto non è invece garantito nel caso in cui si applichino VaR, TCE o WCE.

*(slide 12–13)*

## Misure di rischio coerenti two-sided: definizione

> [!abstract] Definizione
> **Definizione.** La combinazione convessa della 1-norma dell'*upside* di $X$ e della $p$-norma del *downside* di $X$ portano ad una nuova misura di rischio coerente, concepita come segue:
> $$\rho_{a,p}(X) \stackrel{def}{=} a\,\sigma_1^+(X) + (1-a)\,\sigma_p^-(X) - E[X] = a\left\|(X-E[X])^+\right\|_1 + (1-a)\left\|(X-E[X])^-\right\|_p - E[X].$$
>
> **N.B.** La norma $p$ di un vettore $\mathbf{x}$ è definita come
> $$\|\mathbf{x}\|_p := \left(\sum_{i=1}^n |x_i|^p\right)^{1/p}.$$

*(slide 14)*

## Interpretazione finanziaria delle misure two-sided e ruolo dei parametri $a$ e $p$

Questa misura di rischio è interpretabile finanziariamente come una combinazione lineare sia di momenti positivi che di momenti negativi della distribuzione dei rendimenti, con pesi pari rispettivamente ad $a$ ed $1-a$. In particolare, la 1-norma prende in considerazione i rendimenti superiori al rendimento atteso, mentre la $p$-norma fa riferimento a quelli inferiori "aggiustati", ovvero considera un momento centrato della distribuzione dei rendimenti influenzato dal parametro $p$, il quale riflette il grado di penetrazione dell'analisi distributiva ed è strettamente connesso al grado di avversione al rischio dell'investitore.

**Osservazione.** I due parametri, $a$ e $p$, dai quali dipende la misura, modellizzano l'avversione al rischio dell'investitore. In particolare:

- $a \in [0;1]$, è un fattore di rischio globale che rispecchia l'equilibrio desiderato dall'investitore tra volatilità positiva e volatilità negativa;
- $p \in [1;+\infty[$, è un fattore di rischio locale che cresce proporzionalmente con l'avversione al rischio dell'investitore. Esso incorpora anche le informazioni legate alle caratteristiche della distribuzione dei rendimenti, come asimmetria e curtosi.

*(slide 15–16)*
