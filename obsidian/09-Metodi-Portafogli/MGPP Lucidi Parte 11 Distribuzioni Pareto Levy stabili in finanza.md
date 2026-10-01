---
title: "Introduzione alla classe delle distribuzioni Lévy-Pareto stabili"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-11-Distribuzioni-Pareto-Levy-stabili-in-finanza.pdf"
pages: 44
text_layer: true
verified: true
generated: 2026-07-10
---

## Presentazione e contesto

Lezione di Marco Corazza, Dipartimento di Economia – Università Ca' Foscari Venezia, tenuta nell'ambito del workshop *"Distribuzioni Lévy-Pareto stabili. Fondamenta per affrontare le turbolenze dei mercati finanziari"*, Venezia, 10 novembre 2011.

*(slide 1)*

## Introduzione: quale distribuzione seguono i rendimenti logaritmici?

**Figura** — *Foot Locker, Inc. – 05 gennaio 1970, 15 settembre 2011.* Istogramma delle frequenze relative dei rendimenti giornalieri (classi sull'asse orizzontale) del titolo Foot Locker. Il grafico mostra una distribuzione fortemente concentrata attorno allo zero, con un picco centrale molto elevato (circa 0.17 di frequenza relativa nella classe centrale) e code sottili che si estendono fino a valori estremi (da −0.28 a +0.20): è l'evidenza empirica di partenza che motiva la domanda sulla vera distribuzione dei rendimenti.

**Domanda**: che distribuzione segue il rendimento logaritmico
$$r_{t,1} = \ln\left(\frac{P_t}{P_{t-1}}\right) \, ?$$

**Risposta**: distribuzione normale vs. distribuzione Lévy Pareto stabile.

**Alcune differenze fra le due ipotesi:**

| Distribuzione normale | Distribuzione Lévy Pareto stabile |
|---|---|
| Varianza finita. | Varianza infinita. |
| Code "normali". | Code grosse (*fat tails*). |
| Rischio minore. | Rischio maggiore. |

**Cronologia degli sviluppi storici che portano alla domanda:**

| Quando | Chi | Cosa | Conseguenze/Implicazioni |
|---|---|---|---|
| 1897 | V. Pareto | Legge di distribuzione del reddito: $Pr\{Y>y\}=y^{-\alpha}$ | $\alpha = 1.7$. Varianza di $Y$ infinita. |
| 1900 | L. Bachelier | Nascita della finanza matematica: *"Théorie de la spéculation"*, Annales Scientifiques de l'École Normale Supérieure, **3**, 21–86 | $r_{t,1}=\ln(P_t/P_{t-1})$ si distribuisce normalmente. ["Honorable" e non "Très honorable"]. |
| 1925 | P. Lévy | Variabili causali stabili: *"Calcul des Probabilitiés"*, Gauthier Villars, Parigi | $\alpha\in(0,2]$. Varianza delle variabili casuali stabili infinita. |
| 1963 | B. Mandelbrot | Rendimento logaritmico come variabile casuale stabile: 1. *"New methods in statistical economics"*, The Journal of Political Economic, **71**, 421–440. 2. *"The variation of certain speculative prices"*, Journal of Business, **36**, 394-419 | Varianza dei rendimenti logaritmici infinita. Fat tails. |
| 1963 | E.F. Fama | Rendimento logaritmico come variabile casuale stabile: *"Mandelbrot and the stable Paretian hypothesis"*, The Journal of Business, **36**, 420–429 | Idem come sopra. |

Domanda che chiude l'introduzione: se i rendimenti seguono, in generale, una distribuzione stabile non normale, cosa comporta ciò per la teoria e la pratica finanziaria?

*(slide 2–5)*

## Cos'è una variabile casuale stabile: le definizioni 1, 2 e 3 (approccio per convoluzione)

> [!abstract] Definizione
> Le quattro definizioni di v.c. stabile che seguono sono fra loro equivalenti: scelta una di esse come "di partenza", le rimanenti tre si possono ottenere come teoremi a partire da essa.
>
> **Definizione 1** — Una v.c. $X$ si definisce **stabile** se per ogni coppia di costanti $a,b>0$ esistono altre due costanti $c>0$ e $d\in\mathbb{R}$ tali che
> $$aX_1+bX_2 =_d cX+d,$$
> in cui $X_1, X_2$ e $X$ sono vv.cc. indipendentemente ed identicamente distribuite, e $=_d$ indica l'uguaglianza in distribuzione.
>
> *Interpretazione light*: la "somma" di due vv.cc. è ancora una v.c. stabile.
>
> **Definizione 2** — Una v.c. $X$ si definisce **stabile** se per ogni numero intero $n\ge2$ esistono due successioni di costanti $a_1,a_2,\cdots,a_i,\cdots,a_n>0$ e $b_1,b_2,\cdots,b_i,\cdots,b_n\in\mathbb{R}$ tali che
> $$X_1+X_2+\cdots+X_n =_d a_nX+b_n,$$
> in cui $X_1,X_2,\cdots,X_i,\cdots,X_n$ e $X$ sono vv.cc. indipendentemente ed identicamente distribuite.
>
> *Interpretazione light*: la "somma" di $n$ vv.cc. stabili è ancora una v.c. stabile.
>
> **Definizione 3** — Una v.c. $X$ si definisce **stabile** se ha un dominio di attrazione, cioè se esiste una successione di vv.cc. indipendentemente ed identicamente distribuite $X_1,X_2,\cdots,X_i,\cdots$ ed esistono due successioni di costanti $c_1,c_2,\cdots,c_i,\cdots>0$ e $d_1,d_2,\cdots,d_i,\cdots\in\mathbb{R}$ tali che
> $$\frac{X_1+X_2+\cdots+X_i+\cdots+X_n}{c_n}+d_n \to_d X \quad \text{quando } n\to+\infty,$$
> in cui $\to_d$ indica la convergenza in distribuzione.
>
> *Interpretazione light*: la "somma" di un numero "sufficientemente grande" di vv.cc. (anche non stabili) normalizzate è una v.c. stabile.
>
> **Osservazioni sulle relazioni fra le tre definizioni:**
> - le definizioni 1 e 2 sono "sorelle";
> - la definizione 3 è "cugina" delle definizioni 1 e 2 (e viceversa);
> - le vv.cc. normali soddisfano tutte e tre le definizioni date.
>
> **Interpretazione finanziaria delle definizioni 1 e 2 — esempio del rendimento settimanale.**
>
> Si consideri il rendimento settimanale $r_{t,5}=\ln(P_t/P_{t-5})$. Sviluppando:
> $$r_{t,5} = \ln(P_t/P_{t-5}) = \ln(P_t)-\ln(P_{t-5})$$
> $$= \ln(P_t) - \ln(P_{t-1})+\ln(P_{t-1})-\ln(P_{t-2})+\ln(P_{t-2})-\ln(P_{t-3})+\ln(P_{t-3})-\ln(P_{t-4})+\ln(P_{t-4})-\ln(P_{t-5})$$
> $$= \ln(P_t/P_{t-1})+\ln(P_{t-1}/P_{t-2})+\ln(P_{t-2}/P_{t-3})+\ln(P_{t-3}/P_{t-4})+\ln(P_{t-4}/P_{t-5})$$
> $$= r_{t,1}+r_{t-1,1}+r_{t-2,1}+r_{t-3,1}+r_{t-4,1}.$$
>
> **Conclusione**: se i rendimenti giornalieri sono vv.cc. stabili, allora la loro somma, cioè il rendimento settimanale, è una v.c. stabile.
>
> **Interpretazione finanziaria della definizione 3 — esempio del rendimento annuo.**
>
> Si consideri, analogamente, il rendimento annuo (calcolato su 250 giorni di contrattazione), che sulla slide è indicato riutilizzando la notazione dell'esempio precedente:
> $$r_{t,5} = \ln(P_t/P_{t-250}).$$
> Da questo si ha (per esteso, telescopando i rapporti dei prezzi giorno per giorno):
> $$r_{t,5} = \ln(P_t/P_{t-5}) = \ln(P_t)-\ln(P_{t-5}) = \cdots$$
> $$= \ln(P_t/P_{t-1})+\ln(P_{t-1}/P_{t-2})+\cdots+\ln(P_{t-248}/P_{t-249})+\ln(P_{t-249}/P_{t-250})$$
> $$= r_{t,1}+r_{t-1,1}+\cdots+r_{t-248,1}+r_{t-249,1}.$$
>
> **Conclusione**: se i rendimenti giornalieri sono v.c. (anche non stabili), allora la somma di un numero sufficientemente grande di queste vv.cc., cioè il rendimento annuo, è ben approssimato da una v.c. casuale stabile.

*(slide 6–13)*

## Cos'è una variabile casuale stabile: la definizione 4 (funzione caratteristica) e i casi particolari

> [!abstract] Definizione
> **Definizione 4** — Una v.c. $X$ si definisce **stabile** se esistono quattro parametri $\alpha\in(0,2]$, $\beta\in[-1,1]$, $\mu\in\mathbb{R}$ e $\sigma\in[0,+\infty)$, tali che la funzione caratteristica di $X$ è data da
> $$E\left(e^{i\vartheta X}\right) = \begin{cases} \exp\left\{-\sigma^{\alpha}|\vartheta|^{\alpha}\left(1-i\cdot\beta\cdot sgn(\vartheta)\cdot tg\left(\dfrac{\alpha\cdot\pi}{2}\right)\right)+i\cdot\mu\cdot\vartheta\right\} & \text{se } \alpha\neq1\\[2mm] \exp\left\{-\sigma|\vartheta|\left(1-i\cdot\beta\dfrac{2}{\pi}sgn(\vartheta)\cdot\log(|\vartheta|)\right)+i\cdot\mu\cdot\vartheta\right\} & \text{se } \alpha=1 \end{cases}$$
> in cui $i=\sqrt{-1}$.
>
> Con la notazione $X\sim S(\alpha,\beta,\mu,\sigma)$ si indica che la v.c. $X$ segue una distribuzione stabile di parametri $\alpha,\beta,\mu$ e $\sigma$.
>
> **Osservazione**: la funzione caratteristica può essere specificata in forma chiusa per ogni v.c..
>
> **A cosa serve la funzione caratteristica di una v.c.?**
> - *Risposta 1*: può permettere di specificare in forma chiusa la funzione di densità di probabilità della v.c. medesima.
> - *Risposta 2*: fornisce uno strumento (alternativo ad altri più standard) per il calcolo dei momenti della v.c. medesima.
>
> **Osservazione**: con riferimento alla risposta 1, data una v.c. che segue una distribuzione stabile di parametri $\alpha,\beta,\mu$ e $\sigma$, non è quasi mai possibile specificare in forma chiusa la funzione di densità di probabilità della v.c. medesima.
>
> **Osservazione**: la funzione di densità di probabilità della v.c. si può specificare in forma chiusa solo in pochi casi.
>
> **Caso 1**: $\alpha=1$ e $\beta=0$. Allora la distribuzione stabile $S(1,0,\mu,\sigma)$ si particolarizza nella **distribuzione di Cauchy**, avente funzione di densità di probabilità
> $$f(x) = \frac{\sigma}{\pi[\sigma^{2}+(x-\mu)^{2}]}.$$
>
> **Caso 2**: $\alpha=2$. Allora la distribuzione stabile $S(2,*,\mu,\sigma)$ si particolarizza nella **distribuzione normale** $N(\mu, 2\cdot\sigma^{2})$.

*(slide 14–17)*

## Il parametro α: esponente caratteristico (indice di stabilità)

> [!abstract] Definizione
> $\alpha\in(0,2]$ è detto **esponente caratteristico** o **indice di stabilità**. È una quantità legata alla curtosi della distribuzione di probabilità e fornisce una "misura" dell'area, cioè della probabilità, sottesa dalle code della distribuzione medesima.
>
> - $\alpha\downarrow \Rightarrow$ area sottesa dalle code della distribuzione di probabilità $\uparrow$, cioè $\alpha\downarrow \Rightarrow$ probabilità che si verifichino eventi estremi $\uparrow$ (*fat tails*).
> - Quindi, in corrispondenza di $\alpha=2$, cioè la distribuzione di probabilità normale, si ha la più bassa probabilità che si verifichino eventi estremi.
>
> **Figura** — Densità di probabilità stabili al variare di $\alpha \in \{2.0,\,1.5,\,1.0,\,0.5\}$, con $\beta=0$, $c=1$, $\mu=0$. Il grafico mostra che al diminuire di $\alpha$ la densità diventa più appuntita al centro (curtosi maggiore) e le code diventano progressivamente più spesse: la curva con $\alpha=2$ (la normale) è la più "piatta" al centro e con le code più sottili, mentre quella con $\alpha=0.5$ ha il picco più alto e le code più pesanti.
>
> **Implicazioni sulla varianza e sulla media:**
> - Se $\alpha<2$, allora la varianza della distribuzione di probabilità è infinita. Quindi, l'unica distribuzione stabile con varianza finita si ha in corrispondenza di $\alpha=2$, cioè della distribuzione normale.
> - *Osservazione*: in termini finanziari ciò non vuol dire che il rischio è infinito ma, più semplicemente, che la varianza non è una "buona" misura di rischio.
> - Se $\alpha<1$, allora anche la media della distribuzione di probabilità è infinita.

*(slide 18–20)*

## Il parametro μ: parametro di localizzazione

> [!tip] Teorema
> $\mu\in\mathbb{R}$ è detto **parametro di localizzazione**. È una quantità legata alla posizione della distribuzione di probabilità.
>
> - Se $\alpha\in[1,2]$, allora $\mu$ coincide con il valore medio della distribuzione di probabilità.
>
> **Teorema**: data una costante $k\in\mathbb{R}$, se $X\sim S(\alpha,\beta,\mu,\sigma)$, allora
> $$X+k \sim S(\alpha,\beta,\mu+k,\sigma).$$
>
> *Interpretazione light*: sommando una costante $k$ ad una v.c. stabile si trasla di $k$ la v.c. stabile medesima.
>
> *Osservazione light*: $\mu$ si comporta come una media.

*(slide 21)*

## Il parametro β: parametro di asimmetria

> [!abstract] Definizione
> $\beta\in[-1,1]$ è detto **parametro di asimmetria**. È una quantità legata alla simmetria/asimmetria della distribuzione di probabilità:
> $$\begin{cases} \beta<0 \text{ indica asimmetria a sinistra rispetto a } \mu \\ \beta=0 \text{ allora simmetria rispetto a } \mu \\ \beta>0 \text{ indica asimmetria a sinistra rispetto a } \mu \end{cases}$$
> (Nota: così come riportato testualmente nella slide originale, anche il caso $\beta>0$ è descritto come "asimmetria a sinistra"; l'osservazione seguente, però, chiarisce che a $\beta=1$ corrisponde l'asimmetria completa *a destra*, per cui il caso $\beta>0$ va inteso come asimmetria verso destra.)
>
> **Osservazione:**
> - $\beta=-1$ indica completa asimmetria a sinistra.
> - $\beta=1$ indica completa asimmetria a destra.
>
> **Figura** — Densità di probabilità stabili al variare di $\beta \in \{0.00,\,0.25,\,0.50,\,0.75,\,1.00\}$, con $\alpha=0.5$, $c=1$, $\mu=0$. Il grafico mostra che, mantenendo fisso $\alpha$, all'aumentare di $\beta$ da 0 a 1 la distribuzione perde la simmetria attorno a $\mu$ e si inclina progressivamente verso destra, con la coda destra che diventa più pesante di quella sinistra.

*(slide 22–23)*

## Il parametro σ: parametro di scala

> [!tip] Teorema
> $\sigma\in[0,+\infty)$ è detto **parametro di scala**. È una quantità legata alla dispersione della distribuzione di probabilità.
>
> **Teorema**: data una costante $k\in\mathbb{R}$, se $X\sim S(\alpha,\beta,\mu,\sigma)$, allora
> $$k\cdot X \sim \begin{cases} S(\alpha,\, sgn(k)\cdot\beta,\, k\cdot\mu,\, |k|\sigma) & \text{se } \alpha\neq1 \\[1mm] S\!\left(1,\, sgn(k)\cdot\beta,\, k\cdot\mu-\dfrac{2}{\pi}k\cdot\log(k)\,\sigma\cdot\beta,\, |k|\sigma\right) & \text{se } \alpha=1 \end{cases}.$$
>
> *Interpretazione light*: moltiplicando una costante $k$ per una v.c. stabile si ottiene una nuova v.c. stabile avente stesso esponente caratteristico della v.c. di partenza ma, in generale, una "forma" diversa.
>
> *Osservazione light*: $\sigma$ si comporta come una deviazione standard, quindi può essere utilizzata come una misura per il rischio.

*(slide 24)*

## Una digressione storica: da dove nasce l'ipotesi di normalità dei rendimenti

**Domanda**: da dove nasce l'idea originaria secondo cui $r_{t,1}=\ln(P_t/P_{t-1})$ segue una distribuzione normale, detta anche gaussiana?

**Risposta 1 (ragionevole ma non corretta)**: dall'osservazione empirica.

**Figura** — *Foot Locker, Inc. – 05 gennaio 1970, 15 settembre 2011.* Stesso istogramma delle frequenze relative dei rendimenti giornalieri già mostrato nell'introduzione (pagina 2): a un primo sguardo la forma "a campana" concentrata attorno allo zero potrebbe suggerire una spiegazione empirica dell'ipotesi di normalità.

**Risposta 2 (non ragionevole ma corretta)**: l'ipotesi di normalità nasce da un ben fondato impianto teorico-metodologico relativo al comportamento dei mercati finanziari, dovuto a L. J.-B. A. Bachelier (1900), *"Théorie de la spéculation"*, Annales Scientifiques de l'École Normale Supérieure, **3**, 21–86.

Citazione a commento del lavoro di Bachelier:

> «[…] Bachelier begins the mathematical modeling of stock price movements and formulates the principle that "the expectation of the speculator is zero." Obviously, he understands here by expectation the conditional expectation given the past information. In other words, he implicitly accepts as an axiom that the market evaluates assets using a martingale measure. The further hypothesis is that the price evolves as a continuous Markov process, homogeneous in time and space. Bachelier shows that the density of one-dimensional distributions of this process satisfies the relation known now as the Chapman–Kolmogorov equation and notes that the Gaussian density with the linearly increasing variance solves this equation. The question of the uniqueness is not discussed, but Bachelier provides some further arguments to confirm his conclusion. He arrives at the same law by considering the price process as a limit of random walks.»
>
> J.-M. Courtault, Y. Kabanov, B. Bru, P. Crépel, I. Lebon e A. Le Marchand (2000), *"Louis Bachelier. On the centenary of the Théorie de la spéculation"*, Mathematical Finance, **10**, 341-353 [pagina 343].

**Osservazione**: Bachelier si concentrò sulla «Gaussian density» e non su funzioni di densità di probabilità più generali, quali sono le Lévy Pareto stabili, perché queste ultime ancora non esistevano.

Bisognerà attendere fino al 1925 per l'introduzione delle vv.cc. stabili: P. Lévy (1925), *"Calcul des Probabilitiés"*, Gauthier Villars, Parigi.

Bisognerà poi attendere fino al 1963 per l'utilizzo delle vv.cc. stabili in ambito finanziario, ad esempio in:
- B. Mandelbrot (1963), *"New methods in statistical economics"*, The Journal of Political Economic, **71**, 421–440;
- B. Mandelbrot (1963), *"The variation of certain speculative prices"*, Journal of Business, **36**, 394-419;
- E.F. Fama (1963), *"Mandelbrot and the stable Paretian hypothesis"*, The Journal of Business, **36**, 420–429.

Citazione dall'articolo di Fama:

> «[…] This new approach […] makes two basic assertions: (1) the variances of the empirical distribution behave as if they were infinite, and (2) the empirical distributions conform best to the non-Gaussian members of a family of limiting distributions which Mandelbrot as called stable Paretian.
> The infinite variance assumption of the stable Paretian has extreme implications. From a purely statistical standpoint, if the population variance of first differences is infinite, the sample variance is probably a meaningless measure of dispersion.»
>
> E.F. Fama (1963), *"Mandelbrot and the stable Paretian hypothesis"*, The Journal of Business, **36**, 420–429 [pagina 421].

**Problema**: nella stessa ottica di E.F. Fama, se la varianza dei rendimenti logaritmici fosse infinita:
- cosa sarebbe dei modelli di selezione di portafoglio alla Markowitz?
- cosa sarebbe delle misure di *performance* corrette per il rischio del tipo Sharpe ratio?
- cosa sarebbe dei modelli di *option pricing* alla Black-Scholes e Merton?
- cosa sarebbe …?

*(slide 25–33)*

## Lévy Pareto stabilità in finanza? Confronto fra i due impianti teorici

**Problema**: è possibile mantenere il ben fondato impianto teorico-metodologico alla Bachelier "sostituendone" il pezzo relativo alla distribuzione di probabilità stabile normale dei rendimenti logaritmici con quella stabile non normale?

**Risposta**:

> «It is important to distinguish between the stable Paretian distribution and the stable Paretian hypothesis. Under both the stable Paretian and the Gaussian hypotheses it is assumed that the underlying distribution is stable Paretian. The conflict between the two hypotheses involves the value of the characteristic exponent $\alpha$. The Gaussian hypothesis says that $\alpha=2$, while the stable Paretian hypothesis says that $\alpha$ is strictly less than 2.»
>
> E.F. Fama (1963), *"Mandelbrot and the stable Paretian hypothesis"*, The Journal of Business, **36**, 420–429 [pagina 422].

In altri termini, il confronto fra i due impianti teorico-metodologici è riassunto nella tabella seguente:

| | Impianto teorico-metodologico alla Bachelier | Variante alla Lévy-Mandelbrot-Fama |
|---|---|---|
| Distribuzioni | Stabili | Stabili |
| $\alpha$ | $2$ | $(0,2]$ |
| Rischio | Minore | Maggiore |
| Misura per il rischio | Volatilità | ? |

La domanda che resta aperta, e che motiva la parte empirica successiva, è quindi: quale misura per il rischio adottare nella variante non gaussiana, dato che la volatilità (varianza) perde di significato quando $\alpha<2$?

*(slide 34–35)*

## I rendimenti azionari si distribuiscono stabilmente? Metodologia e dati

> [!example] Esempio
> Stimare i quattro parametri $\alpha,\beta,\mu,\sigma$ non è agevole. Esistono diversi metodi, tutti numerici, sviluppati prevalentemente nel periodo 1971-2001.
>
> I risultati che seguono si basano su un metodo di stima iterativo proposto in:
> - I.A. Koutrouvelis (1980), *"Regression-type estimation of the parameters of stable laws"*, Journal of the American Statistical Association, **75**, 918–928;
> - I.A. Koutrouvelis (1981), *"An iterative procedure for the estimation of the parameters of stable laws"*, Communications in Statistics. Simulation and Computation, **10**, 17–28.
>
> **Dati utilizzati.** Rendimenti giornalieri dei seguenti indici azionari:
>
> | Indice | Da | A | Numerosità |
> |---|---|---|---|
> | COMIT Bancario | 1984 | 1992 | circa 2000 |
> | COMIT Finanziario | 1984 | 1992 | circa 2000 |
> | COMIT Assicurativo | 1984 | 1992 | circa 2000 |
> | COMIT Comunicazioni | 1984 | 1992 | circa 2000 |
> | COMIT Immobiliare | 1984 | 1992 | circa 2000 |
> | COMIT Industriale | 1984 | 1992 | circa 2000 |
>
> Rendimenti giornalieri dei seguenti titoli azionari:
>
> | Titoli azioni | Da | A | Numerosità |
> |---|---|---|---|
> | Ansaldo | 1986 | 1992 | circa 1750 |
> | Benetton | 1986 | 1992 | circa 1750 |
> | FIAT | 1979 | 1992 | circa 3500 |
> | FIAT privilegiate | 1986 | 1992 | circa 1750 |
>
> **Domanda**: perché intervalli temporali "non contemporanei" (cioè non tutti riferiti allo stesso periodo di calendario)?
>
> **Risposta 1**: perché risultati su intervalli temporali "contemporanei" verranno presentati da altri relatori del workshop.
>
> **Risposta 2**: per motivi affettivi (si tratta del secondo lavoro dell'autore, del 1992).

*(slide 36–38)*

## I rendimenti azionari si distribuiscono stabilmente? Risultati delle stime

> [!example] Esempio
> **Risultati per gli indici settoriali COMIT**: tra parentesi l'$\bar R^2$ (quando calcolabile) della regressione utilizzata dal metodo di stima di $\alpha$ e di $\beta$.
>
> | Indice | α | β | μ | σ |
> |---|---|---|---|---|
> | C. Bancario | 1.729 (0.998) | 0.122 (0.970) | 0.001 | 0.007 |
> | C. Finanziario | 1.656 (0.997) | 0.065 (0.782) | 0.001 | 0.007 |
> | C. Assicurativo | 1.659 (0.998) | 0.151 (0.952) | 0.002 | 0.008 |
> | C. Comunicaz. | 1.631 (0.995) | 0.037 (0.566) | 0.000 | 0.007 |
> | C. Immobiliare | 1.680 (0.997) | 0.179 (0.968) | 0.001 | 0.005 |
> | C. Industriale | 1.672 (0.997) | 0.117 (0.686) | 0.001 | 0.007 |
>
> **Risultati per i singoli titoli azionari**: tra parentesi l'$\bar R^2$ (quando calcolabile).
>
> | Titolo azionario | α | β | μ | σ |
> |---|---|---|---|---|
> | Ansaldo | 1.504 (0.994) | 0.059 (0.993) | 0.001 | 0.007 |
> | Benetton | 1.562 (0.997) | 0.063 (0.966) | 0.001 | 0.008 |
> | FIAT | 1.719 (0.998) | 0.368 (0.998) | 0.003 | 0.011 |
> | FIAT privileg. | 1.675 (0.998) | 0.095 (0.993) | 0.001 | 0.011 |
>
> **Figura** — Istogramma dei log-rendimenti del DAX, con sovrapposte due curve di densità stimate (una a campana più stretta e alta, l'altra più larga e piatta). Fonte: S.T. Rachev (Ed.) (2003), *"Handbook of Heavy Tailed Distributions in Finance"*, Elsevier/North-Holland, Amsterdam [pagina 160]. Il grafico mostra che l'istogramma empirico ha un picco centrale più alto e code più pesanti di quanto previsto dalla curva normale, mentre la curva della distribuzione stabile (non gaussiana) riproduce meglio sia il picco sia le code dei dati osservati.
>
> **Osservazione conclusiva sui risultati**: questi risultati sono rappresentativi delle distribuzioni dei rendimenti azionari. Cioè:
> - in generale i rendimenti si distribuiscono stabilmente;
> - raramente i rendimenti si distribuiscono normalmente ($\alpha\neq2$);
> - generalmente $\alpha\in(1,2)$, a cui corrisponde:
>   - una media dei rendimenti finita;
>   - una varianza dei rendimenti infinita.

*(slide 39–42)*

## Per concludere: applicazioni finanziarie delle distribuzioni Lévy-Pareto stabili

**Domanda**: dove si utilizzano in finanza le distribuzioni Lévy Pareto stabili?

**Risposta**: si utilizzano, tra l'altro:
- nell'*asset liability management*;
- nei modelli per il rischio di credito;
- nei modelli per il *risk management*;
- nella selezione di portafoglio;
- nei modelli per la struttura a termine dei tassi di interesse;
- nella valutazione di opzioni;
- ….

Esistono inoltre legami tra la distribuzione Lévy Pareto stabile e la struttura frattale dei rendimenti finanziari.

La ricerca su questi temi è tuttora attivissima.

*Slide finale*: "Grazie per l'attenzione."

*(slide 43–44)*
