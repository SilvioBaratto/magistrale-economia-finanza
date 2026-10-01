---
title: "I vincoli a variabili miste-intere nella selezione di portafogli azionari"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-5-I-vincoli-a-variabili-miste-intere.pdf"
pages: 22
text_layer: true
verified: true
generated: 2026-07-10
---

## Le tre categorie di vincoli a variabili miste-intere

Nei problemi di programmazione matematica per la selezione statica di portafogli azionari si distinguono tre principali categorie di vincoli a variabili miste-intere:

- **vincoli relativi ai lotti minimi di transazione**: un titolo deve essere acquistato o venduto solo in un numero intero di unità (lotti). Ad esempio, si devono acquistare o vendere solo quantità intere di lotti del titolo TELECOM IT TI, il cui lotto è costituito da 250 azioni;
- **vincoli relativi al massimo numero intero positivo di diversi titoli azionari** che possono essere acquistati e venduti; ad esempio, il portafoglio da selezionare deve essere costituito da al massimo 5 titoli;
- **vincoli relativi al minimo numero intero positivo di lotti minimi di transazione** di un dato titolo che deve essere acquistato; ad esempio, si devono acquistare o vendere almeno 2 lotti minimi del titolo TELECOM IT TI.

*(slide 1)*

## Implicazioni computazionali dei vincoli a variabili miste-intere

I vincoli a variabili miste-intere danno ai problemi di programmazione matematica per la selezione statica di portafogli azionari una valenza operativa maggiore di quella posseduta dai problemi classici (a sole variabili continue).

L'introduzione di queste categorie di vincoli comporta almeno due tipi di implicazioni non banali:

- **verificare l'ammissibilità** del sistema dei vincoli di questi problemi è, in generale, un **problema NP-completo**;
- **risolvere** questi problemi di programmazione matematica è, in generale, un **problema NP-hard**.

Informalmente:

- i problemi **NP-completi** sono problemi difficili da risolvere (dal punto di vista del tempo di calcolo necessario) in quanto **non** ammettono algoritmi polinomiali di risoluzione;
- i problemi **NP-hard** sono problemi difficili da risolvere **almeno quanto** i problemi NP-completi, e possono esserlo anche di più.

*(slide 2–3)*

## Formalizzazione generale e complessità dell'ammissibilità

> [!tip] Teorema
> Si consideri il seguente sistema di vincoli, nel quale compare un solo vincolo a variabili miste-intere (il vincolo di cardinalità):
>
> $$
> \begin{cases}
> Ax \le b \\
> \#(\{i : x_i > 0\}) \le K \\
> 0 \le x_i \le u_i \quad \forall i = 1,\dots,N
> \end{cases}
> $$
>
> dove:
>
> - $A$ è una matrice nota di ordine $M\times N$,
> - $x$ è il vettore $N$-dimensionale delle variabili decisionali,
> - $b$ è un vettore noto $M$-dimensionale,
> - $K$ è un numero intero positivo minore di $N$,
> - $\#(\cdot)$ indica la cardinalità dell'insieme argomento,
> - $u_i$, con $i=1,\dots,N$, sono upper bound.
>
> **Risultato** — È possibile dimostrare che, sotto specificate ipotesi, verificare l'ammissibilità di questo sistema è un problema NP-completo già quando
>
> $$
> M \ge 3,
> $$
>
> ovvero già quando la matrice $A$ ha un numero di righe maggiore o uguale a 3.

*(slide 4–5)*

## Vincoli sui lotti minimi di transazione: introduzione

Questi vincoli impongono che, dato un titolo azionario, quest'ultimo debba essere acquistato o venduto solo in un numero intero di lotti minimi di transazione.

Tra le categorie di vincoli a variabili miste-intere utilizzate nei problemi di programmazione matematica per la selezione statica di portafogli azionari, è presumibilmente la **più diffusa**.

Le variabili decisionali più "naturali" da considerare nella formulazione di questi problemi risultano essere il **numero di lotti**, piuttosto che le classiche percentuali del capitale inizialmente disponibile.

*(slide 6)*

## Modello di Andramonov e Corazza (2002)

> [!abstract] Definizione
> **Modello di**: Andramonov M.Y. e Corazza M., *Mixed-integer non-linear programming methods for mean-variance portfolio selection*, Rendiconti per gli Studi Economici Quantitativi, vol. 2001, 21-34, 2002.
>
> $$
> \begin{aligned}
> \min \quad & (PLx)'V(PLx) \\
> \text{s.t.} \quad &
> \begin{cases}
> (PLx)'r \ge \pi C \\
> f_1(x) \le \alpha C \\
> f_2(x) \le \beta C \\
> (PLx)'e \ge (1-\alpha-\beta)C \\
> x_i \ge 0 \quad \forall i \\
> x_j \in \mathbb{N} \quad \forall j \in I
> \end{cases}
> \end{aligned}
> $$
>
> dove:
>
> - $x$ è il vettore $(N+1)$-dimensionale delle variabili decisionali,
> - $P$ è la matrice diagonale nota dei prezzi correnti,
> - $L$ è la matrice diagonale nota dei numeri (interi positivi) di unità dei titoli azionari che costituiscono il corrispondente lotto,
> - $V$ è la matrice nota delle varianze e delle covarianze dei rendimenti dei titoli azionari,
> - $r$ è il vettore $(N+1)$-dimensionale noto dei valori medi dei rendimenti dei titoli azionari,
> - $\pi$ è il rendimento noto che il portafoglio da selezionare deve conseguire,
> - $C$ è il capitale inizialmente disponibile,
> - $f_1(\cdot)$ è un'opportuna funzione non lineare relativa ai costi di transazione,
> - $f_2(\cdot)$ è un'opportuna funzione non lineare relativa all'imposizione fiscale,
> - $e$ è il vettore $(N+1)$-dimensionale unitario,
>
> con $\alpha, \beta \ge 0$, e $\alpha + \beta < 1$.
>
> Si noti che la funzione obiettivo può essere riscritta come
>
> $$
> (PLx)'V(PLx) = x'(L'P'VPL)x.
> $$
>
> **Approccio risolutivo** — Per risolvere questo problema di programmazione matematica è stato proposto un approccio risolutivo iterativo articolato in due stadi, che si basa su tecniche algoritmiche di tipo **branch-and-bound** e su metodologie di tipo **cutting plane** e di tipo **sub-gradiente**.
>
> **Teorema** — Se almeno un titolo azionario è infinitamente divisibile, allora in un numero finito di iterazioni l'approccio risolutivo proposto o individua una soluzione ottima, o indica che la regione ammissibile è vuota.

*(slide 7–9)*

## Applicazione esemplificativa del modello Andramonov-Corazza

> [!example] Esempio
> Si considera la seguente applicazione esemplificativa del modello precedente, con $N=2$:
>
> $$
> N = 2, \qquad
> V = \begin{pmatrix} 0.60 & -0.50 \\ -0.50 & 1.00 \end{pmatrix}, \qquad
> P = \begin{pmatrix} 3.00 & 0.00 \\ 0.00 & 7.00 \end{pmatrix}, \qquad
> L = \begin{pmatrix} 1.00 & 0.00 \\ 0.00 & 1.00 \end{pmatrix},
> $$
>
> $$
> r' = (0.20,\ 0.40), \qquad \pi = 0.25, \qquad C = 100, \qquad \alpha = 0.10 \ \text{e} \ \beta = 0.20,
> $$
>
> $$
> f_1(x) = \frac{200}{81}\left(\sqrt{x_1} + \sqrt{x_2}\right), \qquad f_2(x) = 2(x_1 + x_2),
> $$
>
> da cui il problema si riscrive come:
>
> $$
> \begin{aligned}
> \min \quad & 0.6\, x_1^2 + x_2^2 - x_1 x_2 \\
> \text{s.t.} \quad &
> \begin{cases}
> 0.6\, x_1 + 2.8\, x_2 \ge 25 \\
> 3 x_1 + 7 x_2 \le 70 \\
> \sqrt{x_1} + \sqrt{x_2} \le 4.05 \\
> x_1 + x_2 \le 10 \\
> x_1, x_2 \ge 0 \\
> x_1, x_2 \in \mathbb{N}
> \end{cases}
> \end{aligned}
> $$
>
> **Figura (pag. 12)** — Quattro grafici $(x_1, x_2)$ che illustrano l'evoluzione dell'approccio risolutivo iterativo: *Starting feasible point: (0,10)*; *Second feasible point: (0,9)*; *Intermediate unfeasible point: (2,9)*; *Optimal solution: (1,9)*. I grafici mostrano la regione ammissibile (tratteggiata) delimitata dai vincoli lineari e non lineari del problema, e la traiettoria della procedura iterativa che parte dal punto ammissibile $(0,10)$, passa per il punto ammissibile $(0,9)$, esplora un punto intermedio non ammissibile $(2,9)$ e converge infine alla soluzione ottima $(1,9)$.

*(slide 10–12)*

## Modello di Corazza e Favaretto (2007) e teorema di esistenza

> [!tip] Teorema
> **Modello di**: Corazza M. e Favaretto D. (2007), *On the existence of solutions in the quadratic mixed-integer mean-variance portfolio selection problem*, European Journal of Operational Research, vol. 176(3), 1947-1960.
>
> $$
> \begin{aligned}
> \min \quad & (PLx)'V(PLx) \\
> \text{s.t.} \quad &
> \begin{cases}
> (PLx)'r \ge \pi C \\
> (PLx)'e \ge C \\
> x_i \in \mathbb{N}, \quad i = 2,\dots,N+1
> \end{cases}
> \end{aligned}
> $$
>
> **Teorema** — Sia $I = \{2, \dots, n+1\}$ l'insieme degli indici dei titoli azionari. Il problema di programmazione matematica considerato ammette una soluzione ammissibile se e solo se
>
> $$
> (r_1 \ge \pi) \ \lor\ \big((r_i < \pi) \land (\text{esiste } \bar\imath \in I \text{ tale che } r_{\bar\imath} > r_1)\big).
> $$

*(slide 13)*

## Vincoli sul massimo numero di titoli acquistabili e vendibili: introduzione

Questi vincoli impongono che il numero di diversi titoli azionari che possono essere acquistati e venduti non sia superiore ad un prefissato valore intero positivo.

L'utilizzo di questa categoria di vincoli a variabili miste-intere permette di limitare, seppure indirettamente ed in maniera imprecisa, i costi di transazione ed il prelievo derivante dall'imposizione fiscale.

*(slide 14)*

## Modello di Jansen e Van Dijk (2002): tracking error volatility

> [!abstract] Definizione
> **Modello di**: Jansen R. e Van Dijk R. (2002), *Optimal benchmark tracking with small portfolios*, The Journal of Portfolio Management, Winter, 33-39.
>
> $$
> \begin{aligned}
> \min \quad & TEV(x) \\
> \text{s.t.} \quad &
> \begin{cases}
> x'e = 1 \\
> \#(\{i : x_i > 0\}) = K \\
> x_i \ge 0, \quad i = 1,\dots,N
> \end{cases}
> \end{aligned}
> $$
>
> dove $TEV(\cdot)$ è un'opportuna funzione di **tracking error volatility**.
>
> **N.B.** — Il tracking error volatility misura la "vicinanza" delle performance del portafoglio a quelle del benchmark prescelto, solitamente mediante il calcolo della volatilità della differenza tra il rendimento del portafoglio e quello del benchmark:
>
> $$
> TEV(x) = Var(r_{Portafoglio} - r_{Benchmark}).
> $$

*(slide 15)*

## Approccio risolutivo approssimato per il vincolo di cardinalità

> [!note] Dimostrazione
> Data la complessità del problema di Jansen e Van Dijk (che contiene un vincolo di cardinalità a variabili miste-intere), se ne risolve una versione approssimata a variabili (tutte) continue.
>
> L'approccio risolutivo è articolato nei seguenti passi:
>
> 1. Dapprima si riformula il problema di programmazione matematica come segue:
>
> $$
> \begin{aligned}
> \min \quad & TEV(x) + c\cdot \#(\{i : x_i > 0\}) \\
> \text{s.t.} \quad &
> \begin{cases}
> x'e = 1 \\
> x_i \ge 0, \quad i = 1,\dots,N
> \end{cases}
> \end{aligned}
> $$
>
> con $c \ge 0$.
>
> 2. Si ricorda che vale il seguente risultato teorico:
>
> $$
> \#(\{i : x_i > 0\}) = \lim_{p \downarrow 0} \left(x_1^p, \dots, x_N^p\right)'e.
> $$
>
> 3. Si utilizza quest'ultimo risultato teorico per effettuare una sostituzione approssimata nella funzione obiettivo, determinando la seguente versione approssimata dell'originario problema di programmazione matematica:
>
> $$
> \begin{aligned}
> \min \quad & TEV(x) + c \cdot \left(x_1^p, \dots, x_N^p\right)'e \\
> \text{s.t.} \quad &
> \begin{cases}
> x'e = 1 \\
> x_i \ge 0, \quad i = 1,\dots,N.
> \end{cases}
> \end{aligned}
> $$

*(slide 16–17)*

## Discontinuità della frontiera efficiente ed esempio di Jobst et al.

> [!example] Esempio
> In generale, in relazione a questa categoria di vincoli, è da notare come la loro presenza possa rendere **discontinua la frontiera efficiente**.
>
> **Modello di**: Jobst N.J., Horniman M.D., Lucas C.A. e Mitra G. (2001), *Computational aspects of alternative portfolio selection models in the presence of discrete asset choice constraints*, Quantitative Finance, 1, 1-13, con $N=4$ e $K=2$.
>
> **Figura (pag. 18)** — Grafico rendimento atteso (*Expected Return*) contro varianza (*Variance*), da cui risulta la frontiera efficiente del modello con $N=4$ e $K=2$. La curva mostrata è composta da due archi separati e non congiunti: si osserva chiaramente la discontinuità della frontiera efficiente causata dalla presenza del vincolo di cardinalità a variabili miste-intere.

*(slide 18)*

## Vincoli sul minimo numero di lotti di transazione acquistabili: introduzione

Questi vincoli impongono che il numero minimo di lotti minimi di transazione di un dato titolo azionario che deve essere acquistato non sia inferiore ad un prefissato valore intero positivo.

Questa categoria di vincoli a variabili miste-intere è **una delle meno diffuse**.

*(slide 19)*

## Modello di Jobst, Horniman, Lucas e Mitra (2001)

> [!abstract] Definizione
> **Modello di**: Jobst N.J., Horniman M.D., Lucas C.A. e Mitra G. (2001), *Computational aspects of alternative portfolio selection models in the presence of discrete asset choice constraints*, Quantitative Finance, 1, 1-13.
>
> $$
> \begin{aligned}
> \min \quad & \sum_{i=1}^{N}\sum_{j=1}^{N} \sigma_{ij}\, x_i x_j \\
> \text{s.t.} \quad &
> \begin{cases}
> \displaystyle\sum_{i=1}^{N} x_i r_i = \pi \\[4pt]
> \displaystyle\sum_{i=1}^{N} x_i = 1 \\[4pt]
> l_i \cdot \delta_i \le x_i \le u_i \cdot \delta_i, \quad i = 1,\dots,N \\
> \delta_i \in \{0,1\}, \quad \forall i \\[4pt]
> \displaystyle\sum_{i=1}^{N} \delta_i = K
> \end{cases}
> \end{aligned}
> $$
>
> dove $l_i$ e $u_i$, con $i=1,\dots,N$, sono rispettivamente lower e upper bound.
>
> In questo problema viene anche preso in considerazione un vincolo relativo al massimo numero intero positivo di diversi titoli azionari che possono essere acquistati e venduti (l'ultimo vincolo del sistema, $\sum_i \delta_i = K$).
>
> **Approccio risolutivo** — L'approccio risolutivo utilizzato per risolvere questo problema di programmazione matematica si basa su tecniche algoritmiche di tipo **branch-and-bound tree search**.

*(slide 20–21)*

## Osservazioni conclusive

In sintesi, riguardo ai vincoli a variabili miste-intere trattati:

- verificare l'ammissibilità del sistema dei vincoli di problemi di programmazione matematica del tipo considerato è un **problema NP-completo**;
- risolvere problemi di programmazione matematica del tipo considerato è un **problema NP-hard**;
- in relazione alla risoluzione di questi problemi, esiste un **numero ridotto di risultati teorici costruttivi**;
- la presenza di vincoli a variabili miste-intere **distrugge proprietà analitiche significative della frontiera efficiente**.

*(slide 22)*
