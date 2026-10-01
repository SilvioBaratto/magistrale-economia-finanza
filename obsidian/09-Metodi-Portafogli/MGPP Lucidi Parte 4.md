---
title: "Un approccio semplificato alla selezione di portafoglio: il modello diagonale di Sharpe"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-4.pdf"
pages: 16
text_layer: true
verified: true
generated: 2026-07-10
---

## Copertina

**Metodi per la Gestione dei Portafogli Personali**

*A simplified approach to portfolio selection: The Sharpe diagonal model*

Marco Corazza — Dipartimento di Economia, Università Ca' Foscari Venezia. A.a. 2024/2025.

Questa lezione presenta il modello diagonale di Sharpe come alternativa semplificata al modello di Markowitz per la selezione di portafoglio, motivata dalla necessità di ridurre il numero di parametri da stimare.

*(slide 1)*

## Introduzione: il problema della stima dei parametri nel modello di Markowitz

Il **modello di Markowitz** richiede la stima di molti parametri. La stima di molti parametri comporta molti errori di stima.

Dati $N$ titoli, è necessario stimare:
- $N$ rendimenti attesi,
- $N$ deviazioni standard/varianze dei rendimenti,
- $N(N-1)/2$ covarianze tra i rendimenti,

cioè

$$N + N + \frac{N(N-1)}{2} = \cdots = \frac{N^2+3N}{2}$$

parametri da stimare.

La tabella seguente mostra come il numero di parametri cresca rapidamente al crescere del numero di titoli $N$:

| Numero di titoli $N$ | Numero di parametri $(N^2+3N)/2$ |
|---|---|
| 2 | 5 |
| 3 | 9 |
| … | … |
| 10 | 65 |
| … | … |
| 100 | 5150 |
| … | … |
| 200 | 20300 |
| … | … |
| 350 | 61775 |
| … | … |

Questa esplosione combinatoria (dominata dal termine delle covarianze) è la motivazione principale per cercare un modello più parsimonioso: il modello diagonale di Sharpe.

*(slide 2–3)*

## Il modello di Sharpe: specificazione

> [!abstract] Definizione
> Il **modello di Sharpe** descrive il rendimento dei titoli come segue:
>
> $$R_i = A_i + B_i I + C_i, \quad \text{con } i = 1, \dots, N$$
>
> dove:
> - $A_i$ e $B_i$ sono parametri da stimare;
> - $I$ è un **fattore di rischio comune a tutti i titoli** (l'unica e medesima fonte di rischio per tutti gli $N$ titoli);
> - $C_i$ è un termine di errore casuale tale che
>
> $$E(C_i) = 0, \qquad Var(C_i) = Q_i, \qquad Covar(C_i, C_j) = 0 \ \text{per ogni } i \neq j.$$
>
> Inoltre, il fattore di rischio comune $I$ è a sua volta modellato come:
>
> $$I = A_{N+1} + C_{N+1}$$
>
> dove:
> - $A_{N+1}$ è un parametro da stimare;
> - $C_{N+1}$ è un termine di errore casuale tale che
>
> $$E(C_{N+1}) = 0, \qquad Var(C_{N+1}) = Q_{N+1}, \qquad Covar(C_{N+1}, C_i) = 0 \ \text{per ogni } i \neq N+1.$$

*(slide 4–5)*

## Numero di parametri nel modello di Sharpe e confronto con Markowitz

Il modello di Sharpe richiede la stima dei seguenti parametri:
- $A_i$, $B_i$ e $Q_i$ per ciascun titolo, quindi $3N$ parametri;
- $A_{N+1}$ e $Q_{N+1}$ per il fattore di rischio, quindi $2$ parametri;

cioè

$$3N + 2$$

parametri da stimare (contro gli $(N^2+3N)/2$ del modello di Markowitz).

La tabella seguente confronta il numero di parametri richiesti dai due modelli, e il loro rapporto percentuale:

| $N$ | $(N^2+3N)/2$ (Markowitz) | $3N+2$ (Sharpe) | Sharpe/Markowitz % |
|---|---|---|---|
| 2 | 5 | 8 | 160.00% |
| 3 | 9 | 11 | 122.22% |
| … | … | … | … |
| 10 | 65 | 32 | 49.23% |
| … | … | … | … |
| 100 | 5150 | 302 | 5.86% |
| … | … | … | … |
| 200 | 20300 | 602 | 2.97% |
| … | … | … | … |
| 350 | 61775 | 1052 | 1.70% |
| … | … | … | … |

Si osserva che per pochi titoli ($N=2,3$) il modello di Sharpe richiede addirittura *più* parametri di Markowitz (160% e 122.22%), ma al crescere di $N$ il rapporto crolla rapidamente: già con $N=10$ Sharpe richiede meno della metà dei parametri (49.23%), e con $N=350$ appena l'1.70%. Il modello di Sharpe è quindi drasticamente più parsimonioso per portafogli con molti titoli.

*(slide 6–7)*

## Valore atteso del rendimento dell'i-esimo titolo

> [!note] Dimostrazione
> **Proposizione.** Nel modello di Sharpe, il rendimento atteso dell'$i$-esimo titolo è $E(R_i) = A_i + B_i A_{N+1}$.
>
> **Dimostrazione.**
>
> $$E(R_i) = E(A_i + B_i I + C_i) = E\big(A_i + B_i(A_{N+1}+C_{N+1}) + C_i\big) =$$
> $$= E(A_i) + E\big(B_i(A_{N+1}+C_{N+1})\big) + E(C_i) =$$
> $$= A_i + E(B_iA_{N+1}+B_iC_{N+1}) + 0 = A_i + E(B_iA_{N+1}) + E(B_iC_{N+1}) =$$
> $$= A_i + B_iA_{N+1} + B_iE(C_{N+1}) = A_i + B_iA_{N+1} + B_i \cdot 0 =$$
> $$= \boxed{A_i + B_iA_{N+1}}$$
>
> Si utilizzano il fatto che $A_i$ e $A_{N+1}$ sono costanti (parametri), la linearità del valore atteso, e $E(C_{N+1})=0$.

*(slide 8)*

## Varianza del rendimento dell'i-esimo titolo

> [!note] Dimostrazione
> **Proposizione.** Nel modello di Sharpe, la varianza del rendimento dell'$i$-esimo titolo è $Var(R_i) = B_i^2 Q_{N+1} + Q_i$.
>
> **Dimostrazione.**
>
> $$Var(R_i) = Var(A_i+B_iI+C_i) = Var\big(A_i+B_i(A_{N+1}+C_{N+1})+C_i\big) =$$
> $$= Var(A_i+B_iA_{N+1}+B_iC_{N+1}+C_i) =$$
> $$= \underbrace{Var(A_i)}_{=0} + \underbrace{\sum 2\,Covar(A_i,\dots)}_{=0} +$$
> $$+ \underbrace{Var(B_iA_{N+1})}_{=0} + \underbrace{\sum 2\,Covar(B_iA_{N+1},\dots)}_{=0} +$$
> $$+ \underbrace{Var(B_iC_{N+1})}_{=B_i^2 Q_{N+1}} + \underbrace{2\,Covar(B_iC_{N+1}, C_i)}_{=0} +$$
> $$+ \underbrace{Var(C_i)}_{=Q_i} = \boxed{B_i^2 Q_{N+1} + Q_i}$$
>
> I termini che coinvolgono le costanti $A_i$ e $A_{N+1}$ hanno varianza e covarianza nulle (perché sono parametri, non variabili casuali); le covarianze incrociate tra $C_{N+1}$ e $C_i$ sono nulle per ipotesi del modello.

*(slide 9)*

## Covarianza tra i rendimenti di due titoli

> [!note] Dimostrazione
> **Proposizione.** Nel modello di Sharpe, la covarianza tra i rendimenti dell'$i$-esimo e del $j$-esimo titolo è $Covar(R_i,R_j) = B_iB_jQ_{N+1}$.
>
> **Dimostrazione.**
>
> $$Covar(R_i, R_j) = Covar(A_i+B_iI+C_i,\ A_j+B_jI+C_j) =$$
> $$= Covar(B_iI+C_i,\ B_jI+C_j) =$$
> $$= Covar\big(B_i(A_{N+1}+C_{N+1})+C_i,\ B_j(A_{N+1}+C_{N+1})+C_j\big) =$$
> $$= Covar(B_iA_{N+1}+B_iC_{N+1}+C_i,\ B_jA_{N+1}+B_jC_{N+1}+C_j) =$$
> $$= Covar(B_iC_{N+1}+C_i,\ B_jC_{N+1}+C_j) =$$
> $$= \underbrace{Covar(B_iC_{N+1}, B_jC_{N+1})}_{=B_iB_jQ_{N+1}} + \underbrace{Covar(B_iC_{N+1}, C_j)}_{=0} +$$
> $$+ \underbrace{Covar(C_i, B_jC_{N+1})}_{=0} + \underbrace{Covar(C_i, C_j)}_{=0} =$$
> $$= \boxed{B_iB_jQ_{N+1}}$$
>
> Questo è il risultato chiave del modello: la covarianza tra due titoli qualsiasi dipende **solo** dai loro coefficienti di sensibilità $B_i$, $B_j$ al fattore comune e dalla varianza del fattore di rischio $Q_{N+1}$ — non serve stimare direttamente ciascuna delle $N(N-1)/2$ covarianze come in Markowitz.

*(slide 10)*

## Rendimento di portafoglio: il fattore di rischio come ulteriore titolo

> [!note] Dimostrazione
> Il rendimento del portafoglio è, per definizione:
>
> $$R_P = \sum_{i=1}^{N} X_i R_i = \sum_{i=1}^{N} X_i (A_i+B_iI+C_i) = \sum_{i=1}^{N} X_i(A_i+C_i) + \sum_{i=1}^{N} X_iB_iI.$$
>
> Sostituendo $I = A_{N+1}+C_{N+1}$:
>
> $$R_P = \sum_{i=1}^{N} X_i(A_i+C_i) + X_{N+1}I = \sum_{i=1}^{N} X_i(A_i+C_i) + X_{N+1}(A_{N+1}+C_{N+1}) =$$
> $$= \sum_{i=1}^{N+1} X_i(A_i+C_i)$$
>
> dove
>
> $$\sum_{i=1}^{N} X_iB_i = X_{N+1}.$$
>
> In altre parole, definendo $X_{N+1} = \sum_{i=1}^N X_iB_i$, il fattore di rischio $I$ viene trattato formalmente come un **ulteriore ($N+1$-esimo) titolo** del portafoglio, con peso $X_{N+1}$. Questo permette di riscrivere il rendimento di portafoglio come somma su $N+1$ "titoli" invece che $N$, semplificando i calcoli successivi.

*(slide 11–12)*

## Valore atteso del rendimento di portafoglio

> [!note] Dimostrazione
> **Proposizione.** Il rendimento atteso di portafoglio è $E(R_P) = \sum_{i=1}^{N} X_i(A_i+B_iA_{N+1})$.
>
> **Dimostrazione.**
>
> $$E(R_P) = E\left(\sum_{i=1}^{N+1} X_i(A_i+C_i)\right) = E\left(\sum_{i=1}^{N+1} X_iA_i\right) + E\left(\sum_{i=1}^{N+1} X_iC_i\right) =$$
> $$= \sum_{i=1}^{N+1} X_iA_i =$$
> $$= \sum_{i=1}^{N} X_iA_i + X_{N+1}A_{N+1} = \sum_{i=1}^{N} X_iA_i + \sum_{i=1}^{N} X_iB_iA_{N+1} =$$
> $$= \sum_{i=1}^{N} X_i(A_i+B_iA_{N+1})$$
>
> Il secondo passaggio sfrutta $E\left(\sum X_iC_i\right)=0$ (poiché $E(C_i)=0$ per ogni $i$, incluso $i=N+1$); l'ultimo passaggio sostituisce $X_{N+1}=\sum_{i=1}^N X_iB_i$ ricavata in precedenza.

*(slide 13)*

## Varianza del rendimento di portafoglio

> [!note] Dimostrazione
> **Proposizione.** La varianza del rendimento di portafoglio è
>
> $$Var(R_P) = \sum_{i=1}^{N} X_i^2\big(Q_i+B_i^2Q_{N+1}\big) + 2\sum_{i=1}^{N}\sum_{j=i+1}^{N} X_iX_jB_iB_jQ_{N+1}.$$
>
> **Dimostrazione.**
>
> $$Var(R_P) = E\big(R_P - E(R_P)\big)^2 =$$
> $$= E\left(\left(\sum_{i=1}^{N+1} X_i(A_i+C_i) - \sum_{i=1}^{N+1} X_iA_i\right)^2\right) = E\left(\left(\sum_{i=1}^{N+1} X_iC_i\right)^2\right) =$$
> $$= \cdots =$$
> $$= \sum_{i=1}^{N} X_i^2\big(Q_i+B_i^2Q_{N+1}\big) + 2\sum_{i=1}^{N}\sum_{j=i+1}^{N} X_iX_jB_iB_jQ_{N+1}$$
>
> **Nota conclusiva.** La varianza del rendimento di portafoglio dipende **solo** dalle varianze dei rendimenti dei titoli (ma non dalle covarianze tra i rendimenti dei titoli) e dalla varianza del rendimento del fattore di rischio $Q_{N+1}$. Questa è la proprietà fondamentale che rende il modello di Sharpe "diagonale": non è più necessario stimare esplicitamente le $N(N-1)/2$ covarianze tra titoli, perché tutta la dipendenza tra i titoli passa attraverso l'unico fattore comune $I$.

*(slide 14)*

## Osservazioni finali: il problema di selezione del portafoglio nel modello di Sharpe

Nel modello di Sharpe, il fattore di rischio è trattato come un ulteriore titolo (l'$(N+1)$-esimo).

Il vettore dei rendimenti attesi è

$$\begin{pmatrix} A_1+B_1A_{N+1} \\ A_2+B_2A_{N+1} \\ \vdots \\ A_N+B_NA_{N+1} \end{pmatrix}$$

Nel modello di Sharpe, il problema di selezione del portafoglio è:

$$\max_{x_1,\dots,x_N} \ \lambda \mathbf{x}'\mathbf{r} - \mathbf{x}'\mathbf{V}\mathbf{x}$$
$$\text{s.t.} \begin{cases} \mathbf{x}'\mathbf{e} = 1 \\ x_i \geq 0 \ \ \forall i = 1,\dots,N \end{cases}$$

dove $\mathbf{r}$ è il vettore dei rendimenti attesi sopra riportato e $\mathbf{V}$ è la matrice di varianza-covarianza dei rendimenti (che nel modello di Sharpe assume una struttura semplificata, essendo determinata dai soli $B_i$, $Q_i$ e $Q_{N+1}$, come mostrato nelle sezioni precedenti). Il problema è formalmente identico a quello di Markowitz (massimizzazione di un trade-off rendimento-rischio pesato dal parametro $\lambda$, soggetto a vincolo di budget e non negatività dei pesi), ma richiede la stima di un numero di parametri drasticamente inferiore, come mostrato in precedenza.

*(slide 15)*
