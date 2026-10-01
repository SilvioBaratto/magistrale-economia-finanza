---
title: "Metodi per la Gestione dei Portafogli Personali — Parte 2: la teoria di selezione del portafoglio (Modern Portfolio Theory)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-2.pdf"
pages: 78
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: la funzione di utilità di von Neumann–Morgenstern e i portafogli efficienti media–varianza

> [!abstract] Definizione
> Lezione "Part 2 – Metodi per la Gestione dei Portafogli Personali" di Marco Corazza (Dipartimento di Economia, Università Ca' Foscari di Venezia).
>
> **Funzione di utilità di von Neumann–Morgenstern.** Per individuare la scelta di investimento ottima tra quelle efficienti, si considera una funzione di utilità di tipo von Neumann–Morgenstern $U(X)$ tale che
> $$
> \mathbb{E}[U(X)] =: V(r_X,\sigma_X^2).
> $$
> Come di consueto si richiede
> $$
> \frac{\partial V(r_X,\sigma_X^2)}{\partial r_X} > 0,
> $$
> e, poiché l'agente economico considerato è avverso al rischio,
> $$
> \frac{\partial V(r_X,\sigma_X^2)}{\partial \sigma_X^2} < 0.
> $$
>
> **Portafogli efficienti media–varianza.** Come sottolinea Ingersoll:
>
> > «the class of potentially optimal portfolios for such investors are therefore those with the greatest expected return for a given level of variance and, simultaneously, the smallest variance for a given expected return. [...] Such portfolios are termed mean–variance efficient.»
> > — Ingersoll J.E. jr., *Theory of Financial Decision Making*, 1987 (pag. 82)
>
> Con riferimento al caso "la varianza minima per un dato rendimento atteso", la scelta di investimento ottima tra quelle efficienti è illustrata dalla figura seguente.
>
> **Figura (pag. 4)** — Piano $E(X)$–$\mathrm{Var}(X)$ con due livelli di rendimento atteso $\bar r_1 > \bar r_2$ evidenziati da rette orizzontali tratteggiate; su ciascuna retta sono collocati diversi portafogli (punti) con varianze diverse; curve di indifferenza convesse (frecce $\mathbf{x}_1$ verso l'alto e $\mathbf{x}_2$ verso il basso indicano la direzione di preferenza crescente dell'investitore). Il grafico mostra che, a parità di rendimento atteso, l'investitore avverso al rischio sceglie il portafoglio con varianza minima, cioè il punto più a sinistra su ciascuna retta orizzontale.

*(slide 1–4)*

## Il problema di selezione del portafoglio: rendimento, media e varianza

> [!abstract] Definizione
> **Il problema di scelta dell'investimento.** Come osserva Merton:
>
> > «The basic investment–choice problem for an individual is to determine the optimal allocation or his or her wealth among the available investment opportunities. The solution to the general problem of choosing the best investment mix is called portfolio–selection theory. The study of portfolio–selection theory begins with its classic one–period or static formulation.»
> > — Merton R.C., *Continuous–Time Finance*, 1990 (pag. 17)
>
> **Ipotesi.** Si assumono:
> - l'ipotesi di mercato senza attriti (*Frictionless Market assumption*);
> - l'ipotesi di price–taker (*Price–Taker assumption*);
> - l'ipotesi di assenza di vincoli istituzionali, prima parte (*No–Institutional Restrictions assumption*).
>
> **Rendimento del portafoglio.** Si specifica anzitutto il tasso di rendimento del portafoglio stesso:
> $$
> R_P = x_1 R_1 + \dots + x_N R_N = \sum_{i=1}^N x_i R_i;
> $$
> $R_P$ è una variabile casuale.
>
> **Media del rendimento del portafoglio.**
> $$
> \begin{aligned}
> \mathbb{E}(R_P) &= \mathbb{E}(x_1R_1+\dots+x_NR_N) = \mathbb{E}(x_1R_1)+\dots+\mathbb{E}(x_NR_N) =\\
> &= x_1\mathbb{E}(R_1)+\dots+x_N\mathbb{E}(R_N) = x_1r_1+\dots+x_Nr_N = \sum_{i=1}^N x_i r_i =: r_P.
> \end{aligned}
> $$
> Si noti che $\mathbb{E}(\cdot)$ è un operatore lineare; per $r_P$ si usa anche la notazione vettoriale $r_P = \mathbf{x}'\mathbf{r}$.
>
> **Varianza del rendimento del portafoglio.** Si parte da
> $$
> \begin{aligned}
> \mathbb{V}\mathrm{ar}(R_P) &= \mathbb{V}\mathrm{ar}(x_1R_1+\dots+x_NR_N) = \mathbb{V}\mathrm{ar}(x_1R_1)+\dots+\mathbb{V}\mathrm{ar}(x_NR_N)+\\
> &\quad+\mathbb{C}\mathrm{ovar}(x_1R_1,x_2R_2)+\dots+\mathbb{C}\mathrm{ovar}(x_1R_1,x_NR_N)+\\
> &\quad+\mathbb{C}\mathrm{ovar}(x_2R_2,x_1R_1)+\dots+\mathbb{C}\mathrm{ovar}(x_2R_2,x_NR_N)+\dots+\\
> &\quad+\mathbb{C}\mathrm{ovar}(x_{N-1}R_{N-1},x_1R_1)+\dots+\mathbb{C}\mathrm{ovar}(x_{N-1}R_{N-1},x_NR_N)+\\
> &\quad+\mathbb{C}\mathrm{ovar}(x_NR_N,x_1R_1)+\dots+\mathbb{C}\mathrm{ovar}(x_NR_N,x_{N-1}R_{N-1}) =\\[2mm]
> &= x_1^2\mathbb{V}\mathrm{ar}(R_1)+\dots+x_N^2\mathbb{V}\mathrm{ar}(R_N)+\\
> &\quad+x_1x_2\mathbb{C}\mathrm{ovar}(R_1,R_2)+\dots+x_1x_N\mathbb{C}\mathrm{ovar}(R_1,R_N)+\dots+\\
> &\quad+x_{N-1}x_1\mathbb{C}\mathrm{ovar}(R_{N-1},R_1)+\dots+x_Nx_{N-1}\mathbb{C}\mathrm{ovar}(R_N,R_{N-1}) =:\\[2mm]
> &=: x_1^2\sigma_1^2+\dots+x_N^2\sigma_N^2+x_1x_2\sigma_{1,2}+\dots+x_Nx_{N-1}\sigma_{N,N-1} =\\
> &= \sum_{i=1}^N x_i^2\sigma_i^2 + \sum_{i=1}^N\sum_{j=1,j\neq i}^N x_ix_j\sigma_{i,j} = \sum_{i=1}^N x_i^2\sigma_i^2 + 2\sum_{i=1}^N\sum_{j=i+1}^N x_ix_j\sigma_{i,j} =: \sigma_P^2.
> \end{aligned}
> $$
>
> **Osservazioni.** $\mathbb{V}\mathrm{ar}(\cdot)$ non è un operatore lineare. Per $\sigma_P^2$ si usa anche la notazione vettoriale $\sigma_P^2 = \mathbf{x}'\mathbf{V}\mathbf{x}$, dove
> $$
> \mathbf{V} = \begin{pmatrix}
> \sigma_1^2 & \sigma_{1,2} & \dots & \sigma_{1,N-1} & \sigma_{1,N}\\
> \sigma_{2,1} & \sigma_2^2 & \dots & \sigma_{2,N-1} & \sigma_{2,N}\\
> \vdots & \vdots & \vdots & \vdots & \vdots\\
> \sigma_{N-1,1} & \sigma_{N-1,2} & \dots & \sigma_{N-1}^2 & \sigma_{N-1,N}\\
> \sigma_{N,1} & \sigma_{N,2} & \dots & \sigma_{N,N-1} & \sigma_N^2
> \end{pmatrix}
> $$
> è la matrice di varianze e covarianze.
>
> Ricordando che $\sigma_{i,j} = \rho_{i,j}\sigma_i\sigma_j$, dove $\rho_{i,j}\in[-1,1]$ è il coefficiente di correlazione lineare di Bravais–Pearson tra $R_i$ e $R_j$, si può riformulare $\sigma_P^2$ come:
> $$
> \sigma_P^2 = \sum_{i=1}^N x_i^2\sigma_i^2 + \sum_{i=1}^N\sum_{j=1,j\neq i}^N x_ix_j\rho_{i,j}\sigma_i\sigma_j = \sum_{i=1}^N x_i^2\sigma_i^2 + 2\sum_{i=1}^N\sum_{j=i+1}^N x_ix_j\rho_{i,j}\sigma_i\sigma_j.
> $$
> Ricordando infine che se $i=j$ allora $\rho_{i,j}=1$, si può riscrivere $\sigma_P^2$ in forma di doppia sommatoria compatta:
> $$
> \sigma_P^2 = \sum_{i=1}^N\sum_{j=1}^N x_ix_j\rho_{i,j}\sigma_i\sigma_j = \sum_{i=1}^N\sum_{j=1}^N x_ix_j\sigma_{i,j}.
> $$
>
> **La versione base del problema di selezione del portafoglio.**
> $$
> \min_{x_1,\dots,x_N} \sigma_P^2 \quad \text{s.t.} \quad \begin{cases} r_P = \pi\\ \mathbf{x}'\mathbf{e}=1,\end{cases}
> $$
> cioè, in notazione vettoriale,
> $$
> \min_{x_1,\dots,x_N} \mathbf{x}'\mathbf{V}\mathbf{x} \quad \text{s.t.} \quad \begin{cases} \mathbf{x}'\mathbf{r} = \pi\\ \mathbf{x}'\mathbf{e}=1,\end{cases}
> $$
> dove $\pi$ è il rendimento atteso che l'investitore desidera che il portafoglio selezionato realizzi.

*(slide 5–16)*

## Il ruolo del numero di titoli N: il portafoglio equipesato

> [!note] Dimostrazione
> $N$ gioca un ruolo di rilievo nel determinare $\sigma_P^2$. Per illustrare questo ruolo, prima di affrontare la (versione base della) selezione del portafoglio, si considera il portafoglio costituito da titoli equipesati.
>
> **Il caso "portafoglio equipesato".**
>
> 1. Si parte da un portafoglio per cui $x_i = \dfrac{1}{N}$, con $i=1,\dots,N$.
>
> 2. Sostituendo $x_i=1/N$ nell'espressione di $\sigma_P^2$, dopo alcuni passaggi si ottiene:
> $$
> \sigma_P^2 = \frac{1}{N}\sum_{i=1}^N \frac{\sigma_i^2}{N} + \frac{N-1}{N}\sum_{i=1}^N\sum_{j=1,j\neq i}^N \frac{\sigma_{i,j}}{N(N-1)}.
> $$
>
> 3. Definendo $\displaystyle\sum_{i=1}^N \frac{\sigma_i^2}{N} := \overline\sigma_i^2(N)$, media delle varianze dei tassi di rendimento dei titoli, e $\displaystyle\sum_{i=1}^N\sum_{j=1,j\neq i}^N \frac{\sigma_{i,j}}{N(N-1)} := \overline\sigma_{i,j}(N)$, media delle covarianze tra i tassi di rendimento dei titoli, si può riscrivere la varianza del rendimento del portafoglio come:
> $$
> \sigma_P^2 = \frac{1}{N}\overline\sigma_i^2(N) + \frac{N-1}{N}\overline\sigma_{i,j}(N).
> $$
>
> 4. Infine, se $\overline\sigma_i^2(N) = o(N)$ per $N \to +\infty$, calcolando il limite per $N\to+\infty$ dell'espressione precedente di $\sigma_P^2$, si ottiene:
> $$
> \lim_{N\to+\infty}\sigma_P^2 = \lim_{N\to+\infty}\left(\frac{1}{N}\overline\sigma_i^2(N)+\frac{N-1}{N}\overline\sigma_{i,j}(N)\right) = \overline\sigma_{i,j}(N).
> $$
>
> **Domanda.** Quando $\overline\sigma_i^2 = o(N)$ per $N\to+\infty$?
>
> **Risposta.** In generale, quando $\Delta t$ è sufficientemente piccolo ($\Delta t = 1$ giorno, $\Delta t = 1$ settimana, $\Delta t = 1$ mese, ...).
>
> **Osservazione.** I coefficienti $\rho_{i,j}$, con $i,j=1,\dots,N$ e $i\neq j$, giocano un ruolo cruciale nel determinare $\sigma_P^2$. Per illustrare questo ruolo, prima di affrontare la (versione base della) selezione del portafoglio, si considera il portafoglio più semplice possibile, quello costituito da sole due scelte di investimento.

*(slide 17–23)*

## Il caso N = 2 scelte di investimento rischiose: formulazione generale

> [!abstract] Definizione
> **Ipotesi e notazione.** Si considerano:
> - $X_1$ e $X_2$: due scelte di investimento;
> - $R_1$ e $R_2$: i tassi di rendimento (casuali) di $X_1$ e $X_2$, rispettivamente;
> - $r_1$ e $\sigma_1^2$: la media e la varianza di $R_1$;
> - $r_2$ e $\sigma_2^2$: la media e la varianza di $R_2$;
> - $\sigma_{1,2} = \rho_{1,2}\sigma_1\sigma_2$: la covarianza tra $R_1$ e $R_2$;
> - $x_1$ e $x_2$: le percentuali del capitale (iniziale) da investire in $X_1$ e $X_2$, rispettivamente.
>
> Inoltre si assume che $r_1 < r_2$ e $\sigma_1^2 < \sigma_2^2$ (o, equivalentemente, che $r_1 > r_2$ e $\sigma_1^2 > \sigma_2^2$), e che $x_1,x_2 \in [0,1]$ (ipotesi non restrittiva).
>
> **Rendimento, media e varianza del portafoglio.** Il tasso di rendimento (casuale) del portafoglio è $R_P = x_1R_1+x_2R_2$. Ricordando che $x_1+x_2=1$, sostituendo $x_2=1-x_1$ si ha:
> $$
> R_P = x_1R_1 + (1-x_1)R_2.
> $$
> Quindi
> $$
> \mathbb{E}(R_P) = x_1r_1+(1-x_1)r_2 := r_P
> $$
> e
> $$
> \mathbb{V}\mathrm{ar}(R_P) = x_1^2\sigma_1^2+(1-x_1)^2\sigma_2^2+2x_1(1-x_1)\rho_{1,2}\sigma_1\sigma_2 := \sigma_P^2.
> $$
>
> **Osservazione (segni dei termini).** Poiché $x_1,x_2\in[0,1]$ per ipotesi:
> $$
> \sigma_P^2 = \underbrace{\underbrace{x_1^2}_{\in[0,1]}\sigma_1^2}_{\le \sigma_1^2} + \underbrace{\underbrace{(1-x_1)^2}_{\in[0,1]}\sigma_2^2}_{\le \sigma_2^2} + 2\underbrace{x_1(1-x_1)}_{\in[0,1]}\underbrace{\rho_{1,2}}_{\in[-1,1]}\sigma_1\sigma_2,
> $$
> con il terzo addendo che è $<0$ se $\rho_{1,2}\in[-1,0)$, $=0$ se $\rho_{1,2}=0$, $>0$ se $\rho_{1,2}\in(0,1]$. Il primo addendo è sempre $\le\sigma_1^2$ e il secondo è sempre $\le\sigma_2^2$: il segno (e la grandezza) della covarianza determina quindi se, e quanto, la diversificazione riduce la varianza del portafoglio rispetto alle varianze dei singoli titoli.

*(slide 24–27)*

## Sottocaso ρ₁,₂ = 1 (correlazione lineare massima positiva): derivazione della frontiera

> [!note] Dimostrazione
> Si considera $\rho_{1,2}=1$, cioè la massima correlazione lineare positiva tra $R_1$ e $R_2$. In questo caso $R_1 = a+bR_2$, con $a\in\mathbb{R}$ e $b\in\mathbb{R}^+$, o equivalentemente $R_2 = -\dfrac{a}{b}+\dfrac{1}{b}R_1$.
>
> **Derivazione.**
>
> 1. Dall'espressione di $r_P$, dopo alcuni passaggi, si ottiene:
> $$
> x_1 = \frac{r_P - r_2}{r_1-r_2}.
> $$
>
> 2. Sostituendo $\rho_{1,2}=1$ nell'espressione di $\sigma_P^2$, dopo alcuni passaggi si ottiene:
> $$
> \sigma_P^2 = \left[\, \underbrace{x_1}_{\in[0,1]}\underbrace{\sigma_1}_{\ge 0} + \underbrace{(1-x_1)}_{\in[0,1]}\underbrace{\sigma_2}_{\ge 0} \,\right]^2,
> $$
> dove entrambi gli addendi entro parentesi sono $\ge 0$, da cui
> $$
> \sigma_P = x_1\sigma_1 + (1-x_1)\sigma_2.
> $$
>
> 3. Sostituendo l'espressione ottenuta per $x_1$ in quella per $\sigma_P$, dopo alcuni passaggi si ottiene:
> $$
> r_P = \frac{r_2\sigma_1-r_1\sigma_2}{\sigma_1-\sigma_2} + \underbrace{\frac{r_1-r_2}{\sigma_1-\sigma_2}}_{>0}\, \sigma_P.
> $$
>
> **Osservazioni.** Questa relazione è detta frontiera dei portafogli efficienti, o, in breve, frontiera efficiente; il rendimento atteso del portafoglio $r_P$ è una trasformazione affine positiva della deviazione standard del rendimento del portafoglio $\sigma_P$.
>
> Nel sottocaso "$\rho_{1,2}=1$" non vi è alcuna contrazione della deviazione standard (o, equivalentemente, della varianza) del rendimento del portafoglio: non esiste alcun beneficio di diversificazione. Questo limite è illustrato dall'esempio seguente.

*(slide 28–33)*

## Esempio numerico: ρ₁,₂ = 1

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai due titoli (fittizi) $X_1$ e $X_2$. Media, varianza e coefficiente di correlazione lineare dei tassi di rendimento di $X_1$ e $X_2$ sono rispettivamente:
>
> | Parametro | Valore |
> |---|---|
> | $r_1$ | $0.0125$ |
> | $\sigma_1^2$ | $0.0400$ |
> | $r_2$ | $0.0305$ |
> | $\sigma_2^2$ | $0.0900$ |
> | $\rho_{1,2}$ | $1.0000$ (per ipotesi) |
>
> **Figura (pag. 35)** — Piano $\mathrm{SD}(X)$–$E(X)$: frontiera efficiente (simbolo "+") rappresentata da un unico segmento rettilineo che congiunge $X_1$ (triangolo, $\mathrm{SD}\approx 0.20$, $E\approx 0.0125$) a $X_2$ (triangolo capovolto, $\mathrm{SD}\approx 0.30$, $E\approx 0.0305$). Il grafico conferma che con $\rho_{1,2}=1$ tutte le combinazioni dei due titoli giacciono su una retta: non c'è alcuna riduzione del rischio rispetto alla combinazione lineare diretta delle deviazioni standard dei due titoli, cioè nessun beneficio di diversificazione.

*(slide 34–35)*

## Sottocaso ρ₁,₂ = −1 (correlazione lineare massima negativa): derivazione della frontiera

> [!note] Dimostrazione
> Si considera $\rho_{1,2}=-1$, cioè la minima correlazione lineare (massima negativa) tra $R_1$ e $R_2$. In questo caso $R_1 = a+bR_2$, con $a\in\mathbb{R}$ e $b\in\mathbb{R}^-$, o equivalentemente $R_2 = -\dfrac{a}{b}+\dfrac{1}{b}R_1$.
>
> **Derivazione.**
>
> 1. Sostituendo $\rho_{1,2}=-1$ nell'espressione di $\sigma_P^2$, dopo alcuni passaggi si ottiene:
> $$
> \sigma_P^2 = \left[\, \underbrace{x_1}_{\in[0,1]}\underbrace{\sigma_1}_{\ge 0} - \underbrace{(1-x_1)}_{\in[0,1]}\underbrace{\sigma_2}_{\ge 0}\,\right]^2,
> $$
> da cui
> $$
> \sigma_P = \left| x_1\sigma_1 - (1-x_1)\sigma_2 \right|,
> $$
> cioè
> $$
> \sigma_P = \begin{cases} x_1\sigma_1-(1-x_1)\sigma_2 & \text{se } x_1 \ge \dfrac{\sigma_2}{\sigma_1+\sigma_2}\\[2mm] -x_1\sigma_1+(1-x_1)\sigma_2 & \text{se } x_1 < \dfrac{\sigma_2}{\sigma_1+\sigma_2}. \end{cases}
> $$
>
> **Osservazione.** Se $\mathbf{x} = \left(\dfrac{\sigma_2}{\sigma_1+\sigma_2},\dfrac{\sigma_1}{\sigma_1+\sigma_2}\right)$ allora $\sigma_P=0$, **qualunque** siano $\sigma_1^2$ e $\sigma_2^2$! È possibile costruire un portafoglio a rischio nullo (copertura perfetta).
>
> 2. Sostituendo l'espressione ottenuta per $x_1$ in quella per $\sigma_P$, dopo alcuni passaggi si ottiene:
> $$
> r_P = \begin{cases}
> \dfrac{r_2\sigma_1+r_1\sigma_2}{\sigma_1+\sigma_2} + \dfrac{r_1-r_2}{\sigma_1+\sigma_2}\,\sigma_P & \text{se } r_P \ge r_2 + \dfrac{\sigma_2}{\sigma_1+\sigma_2}(r_1-r_2)\\[3mm]
> \dfrac{r_2\sigma_1+r_1\sigma_2}{\sigma_1+\sigma_2} - \dfrac{r_1-r_2}{\sigma_1+\sigma_2}\,\sigma_P & \text{se } r_P < r_2 + \dfrac{\sigma_2}{\sigma_1+\sigma_2}(r_1-r_2)
> \end{cases}
> $$
> Nel primo ramo il coefficiente di $\sigma_P$ (cioè $+\dfrac{r_1-r_2}{\sigma_1+\sigma_2}$) è $<0$ (dato che $r_1<r_2$); nel secondo ramo il coefficiente di $\sigma_P$ (cioè $-\dfrac{r_1-r_2}{\sigma_1+\sigma_2}$) è $>0$.
>
> **Osservazioni.** Il primo ramo di questa relazione è detto frontiera dei portafogli inefficienti, o, in breve, frontiera inefficiente; il secondo ramo è detto frontiera dei portafogli efficienti, o, in breve, frontiera efficiente. In entrambi i rami il rendimento atteso del portafoglio $r_P$ è una trasformazione affine della deviazione standard del rendimento del portafoglio $\sigma_P$ (positiva nel ramo efficiente, negativa in quello inefficiente).
>
> Nel sottocaso "$\rho_{1,2}=-1$" vi è la possibilità di contrarre la deviazione standard (o, equivalentemente, la varianza) del rendimento del portafoglio, fino ad annullarla. Questa possibilità è illustrata dall'esempio seguente.

*(slide 36–41)*

## Esempio numerico: ρ₁,₂ = −1

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai due titoli (fittizi) $X_1$ e $X_2$. Media, varianza e coefficiente di correlazione lineare dei tassi di rendimento di $X_1$ e $X_2$ sono rispettivamente:
>
> | Parametro | Valore |
> |---|---|
> | $r_1$ | $0.0125$ |
> | $\sigma_1^2$ | $0.0400$ |
> | $r_2$ | $0.0305$ |
> | $\sigma_2^2$ | $0.0900$ |
> | $\rho_{1,2}$ | $-1.0000$ (per ipotesi) |
>
> **Figura (pag. 43)** — Piano $\mathrm{SD}(X)$–$E(X)$: due semirette che si dipartono da un punto di intercetta a rischio quasi nullo (etichettato "Intercept", posto a $E(X)\approx0.0197$, calcolabile come $\frac{r_2\sigma_1+r_1\sigma_2}{\sigma_1+\sigma_2}$); la frontiera efficiente ("+") sale da tale intercetta fino a $X_2$ ($\mathrm{SD}=0.30$, $E=0.0305$), mentre la frontiera inefficiente ("×") scende dall'intercetta fino a $X_1$ ($\mathrm{SD}=0.20$, $E=0.0125$). Il grafico mostra concretamente la possibilità, con correlazione perfettamente negativa, di ridurre drasticamente il rischio del portafoglio combinando i due titoli, fino a un punto di rischio pressoché nullo.

*(slide 42–43)*

## Sottocaso ρ₁,₂ ∈ (−1, 1): correlazioni lineari intermedie

Si considera $\rho_{1,2}\in(-1,1)$, cioè correlazioni lineari intermedie tra $R_1$ e $R_2$.

**Domanda.** Nel sottocaso "$\rho_{1,2}\in(-1,1)$", esiste ancora la possibilità di contrarre la deviazione standard (o, equivalentemente, la varianza) del rendimento del portafoglio?

**Risposta.** Dipende dal valore di $\rho_{1,2}\in(-1,1)$. Tale possibilità è illustrata dagli esempi seguenti.

*(slide 44)*

## Esempio numerico: effetto della correlazione intermedia sulla frontiera efficiente

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai due titoli (fittizi) $X_1$ e $X_2$. Media, varianza e coefficiente di correlazione lineare dei tassi di rendimento di $X_1$ e $X_2$ sono rispettivamente:
>
> | Parametro | Valore |
> |---|---|
> | $r_1$ | $0.0125$ |
> | $\sigma_1^2$ | $0.0400$ |
> | $r_2$ | $0.0305$ |
> | $\sigma_2^2$ | $0.0900$ |
> | $\rho_{1,2}$ | $\in(-1.0000, 1.0000)$ (per ipotesi) |
>
> **Figura (pag. 46)** — Piano $\mathrm{Var}(X)$–$E(X)$: cinque curve corrispondenti a $\rho_{1,2}=-0.90,\,-0.45,\,0.00,\,0.45,\,0.90$, tutte congiungenti $X_1$ ($\mathrm{Var}\approx0.04$) a $X_2$ ($\mathrm{Var}\approx0.09$). Al diminuire di $\rho_{1,2}$ la curva si inarca maggiormente verso sinistra (varianza minore a parità di rendimento atteso): il beneficio di diversificazione cresce al decrescere della correlazione.
>
> **Osservazione.** Per opportuni valori di $\rho_{1,2}$ possono esistere portafogli per cui
> $$
> \sigma_P^2 < \min\{\sigma_1^2,\sigma_2^2\},
> $$
> cioè portafogli il cui rendimento ha varianza inferiore alla più piccola delle varianze dei rendimenti dei titoli che li costituiscono.
>
> **Figura (pag. 48)** — Stesso piano $\mathrm{Var}(X)$–$E(X)$, ristretto a $\rho_{1,2}=0.45,\,0.60,\,0.75,\,0.90$: al crescere di $\rho_{1,2}$ verso $1$ la curva si appiattisce progressivamente verso il segmento rettilineo (caso limite $\rho_{1,2}=1$), confermando che il beneficio di diversificazione si riduce quando la correlazione tra i titoli aumenta.

*(slide 45–48)*

## Sottocaso N = 2 con un titolo privo di rischio e uno rischioso: derivazione della frontiera

> [!note] Dimostrazione
> Si considerano: $X_1$, la scelta di investimento priva di rischio; $\pi_1$, il tasso di rendimento (certo) di $X_1$. Si assume inoltre che $\pi_1 < r_2$.
>
> **Osservazioni.** $\mathbb{E}(\pi_1)=r_1=\pi_1$; $\mathbb{V}\mathrm{ar}(\pi_1)=\sigma_1^2=0$; $\rho_{1,2}=0$; $\mathbb{C}\mathrm{ovar}(\pi_1,R_2)=\rho_{1,2}\sigma_1\sigma_2=0$.
>
> **Rendimento del portafoglio.** $R_P = x_1\pi_1+x_2R_2$. Sostituendo $x_2=1-x_1$:
> $$
> R_P = x_1\pi_1+(1-x_1)R_2,
> $$
> quindi
> $$
> \mathbb{E}(R_P) = x_1\pi_1+(1-x_1)r_2 := r_P, \qquad \mathbb{V}\mathrm{ar}(R_P) = (1-x_1)^2\sigma_2^2 := \sigma_P^2.
> $$
>
> **Derivazione.**
>
> 1. Dall'espressione di $r_P$, dopo alcuni passaggi si ottiene:
> $$
> x_1 = \frac{r_P-r_2}{\pi_1-r_2}.
> $$
>
> 2. Dall'espressione $\sigma_P^2 = \underbrace{(1-x_1)^2}_{\in[0,1]}\underbrace{\sigma_2^2}_{\ge0}$ si ottiene:
> $$
> \sigma_P = (1-x_1)\sigma_2.
> $$
>
> 3. Sostituendo l'espressione di $x_1$ in quella di $\sigma_P$, dopo alcuni passaggi si ottiene:
> $$
> r_P = \pi_1 + \underbrace{\frac{r_2-\pi_1}{\sigma_2}}_{>0}\,\sigma_P.
> $$
>
> **Osservazioni.** Questa relazione è detta frontiera dei portafogli efficienti, o, in breve, frontiera efficiente; il rendimento atteso del portafoglio $r_P$ è una trasformazione affine positiva della deviazione standard del rendimento del portafoglio $\sigma_P$.

*(slide 49–55)*

## Esempio numerico: titolo privo di rischio e titolo rischioso

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai due titoli (fittizi) $X_1$ e $X_2$. Media, varianza e coefficiente di correlazione lineare dei tassi di rendimento di $X_1$ e $X_2$ sono rispettivamente:
>
> | Parametro | Valore |
> |---|---|
> | $\pi_1$ | $0.0125$ |
> | $\sigma_1^2$ | $0.0000$ |
> | $r_2$ | $0.0305$ |
> | $\sigma_2^2$ | $0.0900$ |
> | $\rho_{1,2}$ | $0.0000$ (per ipotesi) |
>
> **Figura (pag. 57)** — Piano $\mathrm{SD}(X)$–$E(X)$: frontiera efficiente ("+") rappresentata da un unico segmento rettilineo dal punto $X_1$ ($\mathrm{SD}=0$, $E=0.0125$) a $X_2$ ($\mathrm{SD}\approx0.30$, $E=0.0305$); non compare alcun ramo inefficiente, poiché $r_P$ è ovunque trasformazione affine positiva di $\sigma_P$.
>
> **Osservazioni.** Il comportamento qualitativo della frontiera efficiente del sottocaso "$N=2$ scelte di investimento, una priva di rischio e una rischiosa" è lo stesso del comportamento qualitativo della frontiera efficiente del sottocaso "$N=2$ scelte rischiose e $\rho_{1,2}=-1$". Se $\pi_1 = \dfrac{r_2\sigma_1+r_1\sigma_2}{\sigma_1+\sigma_2}$ allora tali frontiere efficienti coincidono.

*(slide 56–58)*

## Il caso generale N ≥ 2 scelte di investimento rischiose: formulazione e convessità del problema

> [!abstract] Definizione
> Si torna a considerare la versione base del problema di selezione del portafoglio:
> $$
> \min_{x_1,\dots,x_N} \mathbf{x}'\mathbf{V}\mathbf{x} \quad \text{s.t.} \quad \begin{cases} \mathbf{x}'\mathbf{r}=\pi\\ \mathbf{x}'\mathbf{e}=1.\end{cases}
> $$
>
> Come osservano Constantinides e Malliaris:
>
> > «Technically, we minimize a convex function subject to linear constraints. Observe that $\mathbf{x}'\mathbf{V}\mathbf{x}$ is convex because $\mathbf{V}$ is positive definite and also note that the two linear constraints define a convex set. Therefore, the problem has a unique solution and we only need to obtain the first–order conditions.»
> > — Constantinides G.M. e Malliaris A.G., in Jarrow R.A., Maksimovic V. e Ziemba W.T. (a cura di), *Finance*, 1995 (pag. 4)
>
> **Osservazioni (convessità).** Se le $R_i$, con $i=1,\dots,N$, non sono variabili casuali degeneri, cioè se $\sigma_i^2>0$ per ogni $i$, allora:
> - $\dfrac{\partial^2 \mathbf{x}'\mathbf{V}\mathbf{x}}{\partial x_i^2} = 2\sigma_i^2 > 0$ per ogni $i$ (quindi $\mathbf{x}'\mathbf{V}\mathbf{x}$ è una funzione convessa);
> - $\mathbf{x}'\mathbf{V}\mathbf{x}$, che è una varianza, è positiva per ogni $\mathbf{x}\neq\mathbf{0}_N$, dove $\mathbf{0}_N$ è il vettore nullo di dimensione $N$ (quindi $\mathbf{V}$ è una matrice definita positiva).
>
> Si risolve ora la versione base del problema di selezione del portafoglio mediante il teorema che segue.

*(slide 59–62)*

## Teorema di soluzione del problema di selezione del portafoglio e dimostrazione

> [!tip] Teorema
> **Teorema.** Sia $\mathbf{V}$ una matrice $N\times N$ di varianze e covarianze e sia $\mathbf{r}$ un vettore $N$-dimensionale di medie. Se $\mathbf{V}$ è non singolare e definita positiva e se $r_i\neq r_j$ per qualche $i,j=1,\dots,N$, allora il problema (base) di selezione del portafoglio ha l'unica soluzione seguente:
> $$
> \mathbf{x}^* = \frac{(\gamma\mathbf{V}^{-1}\mathbf{r}-\beta\mathbf{V}^{-1}\mathbf{e})\,\pi + (\alpha\mathbf{V}^{-1}\mathbf{e}-\beta\mathbf{V}^{-1}\mathbf{r})}{\alpha\gamma-\beta^2},
> $$
> dove
> $$
> \alpha = \mathbf{r}'\mathbf{V}^{-1}\mathbf{r}, \qquad \beta = \mathbf{r}'\mathbf{V}^{-1}\mathbf{e} = \mathbf{e}'\mathbf{V}^{-1}\mathbf{r}, \qquad \gamma = \mathbf{e}'\mathbf{V}^{-1}\mathbf{e}.
> $$
>
> **Dimostrazione (traccia).**
>
> Si forma il Lagrangiano:
> $$
> \mathfrak{L} = \mathbf{x}'\mathbf{V}\mathbf{x} - \lambda_1(\mathbf{x}'\mathbf{r}-\pi) - \lambda_2(\mathbf{x}'\mathbf{e}-1).
> $$
> Si ottiene il sistema delle condizioni del primo ordine:
> $$
> \begin{cases}
> \dfrac{\partial\mathfrak{L}}{\partial\mathbf{x}} = 2\mathbf{x}'\mathbf{V} - \lambda_1\mathbf{r}' - \lambda_2\mathbf{e}' = \mathbf{0}_N\\[2mm]
> \dfrac{\partial\mathfrak{L}}{\partial\lambda_1} = -\mathbf{x}'\mathbf{r}+\pi \;(=-\mathbf{r}'\mathbf{x}+\pi)= 0\\[2mm]
> \dfrac{\partial\mathfrak{L}}{\partial\lambda_2} = -\mathbf{x}'\mathbf{e}+1 \;(=-\mathbf{e}'\mathbf{x}+1)= 0.
> \end{cases}
> $$
>
> Questo sistema ha un'unica soluzione se il determinante della matrice dei coefficienti è diverso da zero, cioè se
> $$
> \begin{vmatrix} 2\mathbf{V} & \mathbf{r} & \mathbf{e}\\ \mathbf{r}' & 0 & 0\\ \mathbf{e}' & 0 & 0\end{vmatrix} \neq 0.
> $$
> È possibile dimostrare che tale condizione è soddisfatta sotto le ipotesi fatte su $\mathbf{V}$ e $\mathbf{r}$.
>
> Si risolve il sistema delle condizioni del primo ordine. Ricordando che $\mathbf{V}$ è non singolare, dopo alcuni passaggi il sistema si riscrive come:
> $$
> \begin{cases}
> \mathbf{x}' = \dfrac{1}{2}\lambda_1\mathbf{r}'\mathbf{V}^{-1} + \dfrac{1}{2}\lambda_2\mathbf{e}'\mathbf{V}^{-1}\\[2mm]
> \mathbf{x}'\mathbf{r} = \pi\\[1mm]
> \mathbf{x}'\mathbf{e} = 1.
> \end{cases}
> $$
>
> Sostituendo l'espressione di $\mathbf{x}'$ nelle ultime due condizioni del primo ordine, dopo ulteriori passaggi il sistema diventa:
> $$
> \begin{cases}
> \mathbf{x}' = \dfrac{1}{2}\lambda_1\mathbf{r}'\mathbf{V}^{-1} + \dfrac{1}{2}\lambda_2\mathbf{e}'\mathbf{V}^{-1}\\[2mm]
> \dfrac{1}{2}\lambda_1 = \dfrac{\pi\gamma-\beta}{\alpha\gamma-\beta^2}\\[2mm]
> \dfrac{1}{2}\lambda_2 = \dfrac{\alpha-\pi\beta}{\alpha\gamma-\beta^2}.
> \end{cases}
> $$
>
> Infine, sostituendo le espressioni di $\tfrac{1}{2}\lambda_1$ e $\tfrac{1}{2}\lambda_2$ in quella di $\mathbf{x}'$, e trasponendo $\mathbf{x}'$, si ottiene:
> $$
> \mathbf{x} = \frac{(\gamma\mathbf{V}^{-1}\mathbf{r}-\beta\mathbf{V}^{-1}\mathbf{e})\pi + (\alpha\mathbf{V}^{-1}\mathbf{e}-\beta\mathbf{V}^{-1}\mathbf{r})}{\alpha\gamma-\beta^2} := \mathbf{x}^*. \qquad \Box
> $$
>
> **Osservazioni sulla soluzione.** Con riferimento alla soluzione della versione base del problema di selezione del portafoglio:
> - $\mathbb{E}(R_{P^*}) = r_{P^*} = \mathbf{x}^{*\prime}\mathbf{r} = \pi$ (ovviamente);
> - $\mathbb{V}\mathrm{ar}(R_{P^*}) = \sigma_{P^*}^2 = \mathbf{x}^{*\prime}\mathbf{V}\mathbf{x}^* = \dots = \dfrac{\gamma\pi^2-2\beta\pi+\alpha}{\alpha\gamma-\beta^2}$, che descrive una **parabola** nel piano varianza–media;
> - $\mathbb{S}\mathrm{t}\mathbb{D}\mathrm{ev}(R_{P^*}) = \sigma_{P^*} = (\mathbf{x}^{*\prime}\mathbf{V}\mathbf{x}^*)^{1/2} = \dots = \left(\dfrac{\gamma\pi^2-2\beta\pi+\alpha}{\alpha\gamma-\beta^2}\right)^{1/2}$, che descrive una **iperbole** nel piano deviazione standard–media.
>
> Si illustra il comportamento tipico di tale parabola e iperbole nei rispettivi piani di riferimento mediante l'esempio che segue.

*(slide 63–69)*

## Esempio applicativo: tre titoli del mercato azionario italiano e coordinate del vertice della frontiera

> [!example] Esempio
> Sia $\mathbb{X}$ l'insieme delle scelte di investimento costituito dai seguenti titoli del mercato azionario italiano:
> - $X_1$ = Alleanza Assicurazioni;
> - $X_2$ = Fondiaria–Sai;
> - $X_3$ = Unicredito Italiano.
>
> **Dati.** Media, varianza e coefficienti di correlazione lineare dei tassi di rendimento di $X_1$, $X_2$ e $X_3$ (valutati su dati giornalieri dal 23 agosto 2006 al 21 settembre 2006) sono rispettivamente:
>
> | Parametro | Valore |
> |---|---|
> | $r_1$ | $4.037E{-}04$ |
> | $\sigma_1^2$ | $1.229E{-}04$ |
> | $r_2$ | $9.901E{-}04$ |
> | $\sigma_2^2$ | $1.514E{-}04$ |
> | $r_3$ | $1.213E{-}03$ |
> | $\sigma_3^2$ | $7.794E{-}05$ |
> | $\rho_{1,2}$ | $1.600E{-}01$ |
> | $\rho_{1,3}$ | $-8.291E{-}02$ |
> | $\rho_{2,3}$ | $4.150E{-}01$ |
>
> **Pesi ottimi per diversi livelli di rendimento atteso $\pi$.**
>
> | $\pi$ | $(x_1^*, x_2^*, x_3^*)$ |
> |---|---|
> | $-0.00300$ | $(5.252,\, -0.170,\, -4.082)$ |
> | $\dots$ | $\dots$ |
> | $-0.00175$ | $(3.681,\, -0.073,\, -2.608)$ |
> | $\dots$ | $\dots$ |
> | $0.00050$ | $(0.853,\, 0.102,\, 0.045)$ |
> | $\dots$ | $\dots$ |
> | $0.00225$ | $(-1.347,\, 0.238,\, 2.108)$ |
> | $\dots$ | $\dots$ |
> | $0.00400$ | $(-3.546,\, 0.374,\, 4.172)$ |
>
> **Figura (pag. 74)** — Piano $\mathrm{Var}(X)$–$E(X)$: la frontiera a forma di parabola presenta un tratto efficiente ("+", superiore) e un tratto inefficiente ("×", inferiore); sono riportati anche i tre titoli singoli: Alleanza Assicurazioni (triangolo, basso rendimento) giace sul tratto inefficiente, Fondiaria–Sai (quadrato) è nettamente all'interno della frontiera (varianza elevata a fronte di un rendimento intermedio: titolo dominato), Unicredito Italiano (cerchio) è prossimo al tratto efficiente.
>
> **Figura (pag. 75)** — Stesso esempio nel piano $\mathrm{StDev}(X)$–$E(X)$: la frontiera assume la caratteristica forma a iperbole, con lo stesso posizionamento relativo dei tre titoli osservato nella figura precedente.
>
> **Coordinate del vertice.** Il vertice della parabola che descrive la relazione tra media e varianza dei rendimenti dei portafogli soluzione del problema base ha coordinate:
> $$
> \left(\sigma_{P,v}^2 = \frac{1}{\gamma},\; r_{P,v} = \frac{\beta}{\gamma}\right).
> $$
> Il vertice dell'iperbole che descrive la relazione tra media e deviazione standard dei rendimenti dei portafogli soluzione del problema base ha coordinate:
> $$
> \left(\sigma_{P,v} = \left(\frac{1}{\gamma}\right)^{1/2},\; r_{P,v} = \frac{\beta}{\gamma}\right).
> $$
>
> **Figura (pag. 78)** — Piano $[\mathrm{StDev}(X)-\mathrm{Var}(X)]$–$E(X)$: la stessa frontiera (rami efficiente "+" e inefficiente "×") e gli stessi tre titoli sono rappresentati rispetto alla differenza tra deviazione standard e varianza, una scala che comprime i valori vicini a zero; il posizionamento relativo dei titoli rispetto alla frontiera resta qualitativamente lo stesso delle figure precedenti.

*(slide 70–78)*
