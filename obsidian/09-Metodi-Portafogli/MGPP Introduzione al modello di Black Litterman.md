---
title: "Il modello Black-Litterman"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Introduzione-al-modello-di-Black-Litterman.pdf"
pages: 18
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: il portafoglio di mercato, le view e il ruolo del modello di Black-Litterman

**Corso**: Metodi per la Gestione dei Portafogli Personali — Marco Corazza, Dipartimento di Economia, Università Ca' Foscari Venezia, A.a. 2025/2026. Argomento della lezione: il modello Black-Litterman.

Nel quadro di equilibrio descritto dal **CAPM**, il portafoglio di mercato $M$ coincide con il portafoglio detenuto dall'investitore rappresentativo. Nel portafoglio di mercato $M$, i pesi dei singoli asset sono proporzionali alla loro incidenza sul valore totale degli asset investibili nell'economia.

**Figura** — Grafico con asse verticale "Expected return" e asse orizzontale "Standard deviation of return". Sono riportati il punto privo di rischio $R_F$, i portafogli rischiosi $I$, $M$, $J$, la retta che parte da $R_F$ e passa per $M$ (indicata come "New efficient frontier", cioè la Capital Market Line) e la curva delle sole attività rischiose tangente in $M$ ("Previous efficient frontier"). La figura illustra che, introducendo l'attività priva di rischio, tutti gli investitori razionali detengono combinazioni lineari di $R_F$ e del portafoglio di mercato $M$: quest'ultimo è il punto di tangenza fra le due frontiere ed è quindi il portafoglio rischioso ottimo per l'investitore rappresentativo.

In teoria, dunque, tutti gli investitori dovrebbero scegliere lo stesso portafoglio di attività rischiose, cioè il portafoglio di mercato $M$. In pratica, però, gli investitori hanno **opinioni** e **aspettative** diverse sugli asset presenti nel mercato. Queste opinioni e aspettative rappresentano le specifiche **view** di ogni investitore. Le view vengono espresse in termini di:
- **rendimento atteso assoluto** di un titolo, oppure
- **variazioni del rendimento atteso** di un titolo rispetto a quello di un altro titolo.

In fase di selezione di portafoglio, l'integrazione di queste view con quelle di mercato riveste un ruolo importante nelle decisioni di investimento. Il **modello di Black-Litterman** permette di integrare le view dell'investitore con quelle del mercato, bilanciandole sulla base della "fiducia" che l'investitore ha sulle proprie view.

**Figura** — Schema concettuale a blocchi: due riquadri di ingresso, "Market equilibrium $P(\mu)$" e "Investor's views $P(Q\mid\mu)$", confluiscono con due frecce in un unico riquadro di uscita, "Integrated views $P(\mu\mid Q)$". La figura mostra, in sintesi visiva, come il modello combini in chiave bayesiana la distribuzione a priori implicita nell'equilibrio di mercato con la distribuzione delle view dell'investitore, per produrre una distribuzione a posteriori integrata dei rendimenti attesi.

*(slide 1–4)*

## Il teorema di Bayes come fondamento del modello

> [!abstract] Definizione
> Il modello di Black-Litterman è costruito come un'applicazione del **teorema di Bayes**: la distribuzione a priori dei rendimenti, implicita nell'equilibrio di mercato, viene aggiornata alla luce della nuova informazione costituita dalle view dell'investitore, ottenendo una distribuzione a posteriori.
>
> $$\Pr(M|W) = \frac{\Pr(M)\Pr(W|A)}{\Pr(W)}$$
>
> dove:
> - $\Pr(M)$ indica la probabilità dello stato del mercato (**distribuzione a priori**);
> - $\Pr(W|M)$ indica la probabilità dello stato delle view condizionata alla probabilità dello stato del mercato;
> - $\Pr(W)$ indica la probabilità dello stato delle view;
> - $\Pr(M|W)$ indica la probabilità dello stato del mercato condizionata alla probabilità dello stato delle view (**distribuzione a posteriori**).

*(slide 5)*

## Il mercato: le assunzioni distributive dell'a priori

> [!abstract] Definizione
> Il punto di partenza del modello è la costruzione della distribuzione **a priori** dei rendimenti di mercato, basata su due assunzioni.
>
> **Assunzione 1.** Si considera un mercato composto da $N$ titoli a rendimento rischioso con rendimenti distribuiti normalmente come segue:
> $$\mathbf{R} \sim \mathcal{N}(\mathbf{r}, \mathbf{V})$$
> dove:
> - $\mathbf{R}$ indica il vettore dei rendimenti rischiosi;
> - $\mathbf{r}$ indica il vettore dei rendimenti attesi;
> - $\mathbf{V}$ indica la matrice di varianza e covarianza dei rendimenti rischiosi.
>
> **Assunzione 2.** Si considera un vettore dei rendimenti attesi distribuito normalmente come segue:
> $$\mathbf{r} \sim \mathcal{N}(\mathbf{\Pi}, \tau\mathbf{V})$$
> dove:
> - $\mathbf{\Pi}$ indica un opportuno vettore;
> - $\tau \in [0, +\infty)$ indica un opportuno fattore di incertezza.

*(slide 6–7)*

## Determinazione dei rendimenti attesi di equilibrio (Π*)

> [!note] Dimostrazione
> Il modello distingue due possibili processi, legati dalla teoria dell'utilità attesa, che mettono in relazione rendimenti attesi, rischio e pesi di portafoglio.
>
> **Processo diretto.** Dati i rendimenti attesi e la matrice di varianza-covarianza, si massimizza l'utilità attesa per ottenere i pesi ottimi di portafoglio:
> $$\mathbf{r}, \mathbf{V} \;\rightarrow\; \max \mathbb{E}[U(\mathbf{r}, \mathbf{V})] \;\rightarrow\; \mathbf{x}^*\ [?]$$
> dove $\mathbf{x}^*$ indica il vettore (**incognito**) dei pesi dei singoli asset.
>
> **Processo inverso.** Partendo dai pesi di mercato, noti (ad esempio tramite il modello di equilibrio CAPM), si risale per via inversa ai rendimenti attesi di equilibrio che li giustificano:
> $$[?]\ \mathbf{\Pi}^* \;\leftarrow\; \max \mathbb{E}[U(\mathbf{\Pi}^*, \mathbf{V})] \;\leftarrow\; \mathbf{x}_M, \mathbf{V}$$
> dove:
> - $\mathbf{x}_M$ indica il vettore (**noto**) dei pesi dei singoli asset determinati mediante il modello di equilibrio CAPM;
> - $\mathbf{\Pi}^*$ indica il vettore (**incognito**) dei rendimenti attesi di equilibrio.
>
> Il modello di Black-Litterman utilizza il **processo inverso**. Il vettore dei rendimenti attesi di equilibrio si ottiene dalla massimizzazione della funzione di utilità quadratica attesa:
> $$\max_{\mathbf{x}} \; \mathbf{x}_M' \mathbf{\Pi} - \frac{a}{2}\, \mathbf{x}_M' \mathbf{V} \mathbf{x}_M$$
>
> Le condizioni di ottimalità (del primo ordine) sono soddisfatte ponendo
> $$\frac{\partial U}{\partial \mathbf{x}_M} = 0,$$
> da cui
> $$\mathbf{\Pi} - a\mathbf{V}\mathbf{x}_M = \mathbf{0},$$
> da cui, infine,
> $$\mathbf{\Pi}^* = a\mathbf{V}\mathbf{x}_M.$$
>
> Il vettore $\mathbf{\Pi}^*$ così ottenuto rappresenta i rendimenti attesi impliciti nell'equilibrio di mercato: costituisce la media della distribuzione a priori del modello di Black-Litterman (cfr. Assunzione 2).

*(slide 8–10)*

## Le view dell'investitore

> [!abstract] Definizione
> Le view dell'investitore vengono specificate tramite la relazione
> $$\mathbf{P}\mathbf{r} \sim (\mathbf{Q}, \mathbf{\Omega})$$
> dove:
> - $\mathbf{P}$ è una matrice $(K, N)$ che rappresenta la **mappatura delle view** dell'investitore;
> - $\mathbf{Q}$ è un vettore $(K, 1)$ che riporta le view dell'investitore in termini di **rendimenti**;
> - $\mathbf{\Omega}$ è una matrice **diagonale** $(K, K)$ che riporta le **varianze** delle view dell'investitore;
>
> con $K \le N$ pari al numero di asset sui quali l'investitore ha formulato le proprie view.
>
> Le view possono essere formulate:
> - in **termini assoluti**, cioè sul rendimento atteso di un singolo titolo;
> - in **termini relativi**, cioè in termini di rendimento di un titolo rispetto a quello di un altro titolo.

*(slide 11–12)*

## Il modello Black-Litterman: la distribuzione a posteriori

> [!tip] Teorema
> Combinando, secondo il teorema di Bayes, la distribuzione a priori dei rendimenti di mercato ($\mathbf{r} \sim \mathcal{N}(\mathbf{\Pi}^*, \tau\mathbf{V})$, con $\mathbf{\Pi}^* = a\mathbf{V}\mathbf{x}_M$) con la distribuzione delle view dell'investitore ($\mathbf{P}\mathbf{r} \sim (\mathbf{Q}, \mathbf{\Omega})$), si ottiene la distribuzione a posteriori dei rendimenti secondo il modello di Black-Litterman:
> $$\mathbf{R}_{BL} \sim (\mathbf{r}_{BL}, \mathbf{V}_{BL})$$
> dove
> $$\mathbf{r}_{BL} = \left[(\tau\mathbf{V})^{-1} + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{P}\right]^{-1} \cdot \left[(\tau\mathbf{V})^{-1}\mathbf{\Pi}^* + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{Q}\right]$$
> $$\mathbf{V}_{BL} = \left[(\tau\mathbf{V})^{-1} + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{P}\right]^{-1}$$
>
> Il vettore $\mathbf{r}_{BL}$ è dunque una media ponderata fra i rendimenti impliciti di equilibrio $\mathbf{\Pi}^*$ e le view dell'investitore $\mathbf{Q}$: i pesi relativi dipendono dall'incertezza sull'equilibrio di mercato (attraverso $\tau\mathbf{V}$) e dall'incertezza sulle view stesse (attraverso $\mathbf{\Omega}$). Quanto più $\mathbf{\Omega}$ è piccola — cioè quanto maggiore è la fiducia dell'investitore nelle proprie view — tanto più $\mathbf{r}_{BL}$ si avvicina a $\mathbf{Q}$; viceversa, quanto più $\mathbf{\Omega}$ è grande, tanto più $\mathbf{r}_{BL}$ si avvicina a $\mathbf{\Pi}^*$.

*(slide 13)*

## Esempio numerico completo di applicazione del modello

> [!example] Esempio
> **Passo 0 — Dati di partenza.**
>
> $N = 3$
>
> $\mathbf{x}_M = (0.50, 0.20, 0.30)'$
>
> Matrice di varianza-covarianza $\mathbf{V}$:
>
> | | Asset 1 | Asset 2 | Asset 3 |
> |---|---|---|---|
> | **Asset 1** | 0.0225 | 0.0060 | 0.0027 |
> | **Asset 2** | 0.0060 | 0.0400 | 0.0090 |
> | **Asset 3** | 0.0027 | 0.0090 | 0.0324 |
>
> Coefficiente di avversione al rischio: $a = 2.5$.
>
> **Passo 1 — Rendimenti attesi di equilibrio (a priori).**
>
> $$\mathbf{R}\sim \mathcal{N}(\mathbf{r}, \mathbf{V}) \qquad \mathbf{r}\sim \mathcal{N}(\mathbf{\Pi}, \tau\mathbf{V}) \qquad \mathbf{\Pi}^* = -a\mathbf{V}\mathbf{x}_M$$
>
> $$\mathbf{\Pi}^* = -a\mathbf{V}\mathbf{x}_M = \cdots = (0.0340, 0.0420, 0.0263)'$$
>
> *(Nota: nella slide dell'esempio la formula di $\mathbf{\Pi}^*$ compare con il segno negativo, mentre nella derivazione generale del modello — Sezione "Determinazione dei rendimenti attesi di equilibrio" — compare con il segno positivo; si riporta qui fedelmente quanto indicato nel materiale del corso.)*
>
> **Passo 2 — Formulazione delle view.**
>
> - $K = 2$
> - View 1: $\mathbb{E}(r_1) = 0.06$ (view assoluta)
> - View 2: $\mathbb{E}(r_2 - r_3) = 0.02$ (view relativa)
>
> **Passo 3 — Matrici delle view.**
>
> $$\mathbf{Q} = (0.06, 0.02)$$
>
> $$\mathbf{\Omega} = \begin{pmatrix} 0.0004 & 0 \\ 0 & 0.0009 \end{pmatrix}$$
>
> $$\mathbf{P} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \end{pmatrix}$$
>
> **Passo 4 — Distribuzione a posteriori Black-Litterman.**
>
> $$\mathbf{r}_{BL} = \left[(\tau\mathbf{V})^{-1} + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{P}\right]^{-1} \cdot \left[(\tau\mathbf{V})^{-1}\mathbf{\Pi}^* + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{Q}\right]$$
> $$\mathbf{V}_{BL} = \left[(\tau\mathbf{V})^{-1} + \mathbf{P}'\mathbf{\Omega}^{-1}\mathbf{P}\right]^{-1}$$
>
> Risultati numerici:
>
> $$\mathbf{r}_{BL} = (0.0532, 0.0478, 0.0281)$$
>
> | | Asset 1 | Asset 2 | Asset 3 |
> |---|---|---|---|
> | **Asset 1** | 0.0002956 | 0.0000605 | 0.0000496 |
> | **Asset 2** | 0.0000605 | 0.0013017 | 0.0009225 |
> | **Asset 3** | 0.0000496 | 0.0009225 | 0.0012185 |
>
> **Passo 5 — Pesi ottimi di portafoglio secondo Black-Litterman.**
>
> $$\mathbf{x}_M = \frac{1}{a}\mathbf{V}^{-1}\mathbf{r}_{BL} = (0.627, 0.230, 0.143)$$
>
> **Figura** — Grafico a barre con asse verticale "Peso in portafoglio", che affianca, per ciascuno dei tre asset, i "Pesi di mercato" (la serie $\mathbf{x}_M = (0.50, 0.20, 0.30)$ di partenza) e i "Pesi BL normalizzati" (la serie $(0.627, 0.230, 0.143)$ ottenuta al Passo 5). Il grafico mostra visivamente come le view dell'investitore modifichino l'allocazione ottima rispetto ai soli pesi di mercato: l'asset su cui è stata formulata la view assoluta di rendimento più elevato (Asset 1, view al 6%) vede aumentare sensibilmente il proprio peso rispetto al 50% di partenza, a scapito degli altri due asset.

*(slide 14–17)*
