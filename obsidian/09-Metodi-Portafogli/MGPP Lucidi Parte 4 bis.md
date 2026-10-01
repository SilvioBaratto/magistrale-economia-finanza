---
title: "Alcuni limiti della Modern Portfolio Theory: la scelta operativa del rendimento obiettivo"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-4-bis.pdf"
pages: 7
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: i limiti pratici della MPT

Il modello media-varianza (Modern Portfolio Theory, MPT) non è utilizzato in modo intensivo dai professionisti della finanza. Il problema principale che si affronta in questa parte del corso è la **scelta operativa del rendimento obiettivo** (*target return*).

Nell'ottimizzazione media-varianza classica, l'investitore deve specificare un rendimento desiderato $r_P = \pi$. Tuttavia può risultare difficile individuare un valore di $\pi$ "coerente", specialmente in contesti finanziari instabili. In particolare, un investitore rischia di selezionare:

- un portafoglio con un $\pi$ **alto**, caratterizzato da varianza eccessiva;
- oppure un portafoglio con un $\pi$ **basso**, "lasciando sul tavolo" rendimento atteso.

Per affrontare questo problema esistono tre possibili procedure operative, illustrate nelle sezioni seguenti:

1. sfruttare il cosiddetto **tangency portfolio** (portafoglio tangente);
2. massimizzare direttamente l'**utilità attesa** dell'investitore;
3. scegliere il massimo tra $r_{1/N}$ e $r_{GMV}$.

*(slide 1–2)*

## Procedura 1 — Il portafoglio tangente (tangency portfolio)

> [!abstract] Definizione
> Seguendo il **teorema di separazione dei fondi** (*fund separation theorem*), l'investitore sceglie di detenere una combinazione dell'attività priva di rischio e del **portafoglio tangente**.
>
> L'espressione analitica del portafoglio tangente è:
>
> $$\boldsymbol{x} = \frac{\boldsymbol{V}^{-1}(\boldsymbol{r} - r_c \boldsymbol{e})}{\boldsymbol{e}' \boldsymbol{V}^{-1}(\boldsymbol{r} - r_c \boldsymbol{e})}$$
>
> dove $\boldsymbol{V}$ è la matrice di varianza-covarianza dei rendimenti, $\boldsymbol{r}$ il vettore dei rendimenti attesi, $r_c$ il rendimento privo di rischio ed $\boldsymbol{e}$ il vettore unitario.
>
> Questa procedura consente di evitare la specificazione diretta di $\pi$, poiché la combinazione tra attività priva di rischio e portafoglio tangente determina implicitamente il punto sulla frontiera efficiente.
>
> **Limite pratico:** in genere i portafogli tangenti stimati campionariamente (*sample tangency portfolios*) hanno una performance scadente fuori campione (*out of sample*).

*(slide 3)*

## Procedura 2 — Massimizzazione diretta dell'utilità attesa

> [!abstract] Definizione
> La massimizzazione diretta dell'"utilità attesa" dell'investitore non richiede di specificare $\pi$.
>
> Il problema di programmazione matematica da risolvere è:
>
> $$\min_x \; \boldsymbol{x}'\boldsymbol{r} - \frac{\lambda}{2}\boldsymbol{x}'\boldsymbol{V}\boldsymbol{x}$$
> $$\text{s.t.} \quad \boldsymbol{x}'\boldsymbol{e} = 1$$
>
> La soluzione a questo problema è:
>
> $$\boldsymbol{x} = \frac{1}{\lambda}\boldsymbol{V}^{-1}\left(\boldsymbol{r} - \frac{\boldsymbol{e}'\boldsymbol{V}^{-1}\boldsymbol{r} - \lambda}{\boldsymbol{e}'\boldsymbol{V}^{-1}\boldsymbol{e}}\right)$$
>
> **Limite pratico:** questo approccio presenta uno svantaggio, legato alla scelta del parametro di avversione al rischio $\lambda$. Diversi studiosi hanno stimato che $\lambda$ appartenga all'intervallo $[0, 5]$.

*(slide 4)*

## Procedura 3 — Il massimo tra $r_{1/N}$ e $r_{GMV}$

> [!abstract] Definizione
> Un altro modo per selezionare un portafoglio media-varianza ottimale senza specificare $\pi$ consiste nel porre il rendimento obiettivo pari a:
>
> $$\max(r_{1/N}, r_{GMV})$$
>
> Il problema di programmazione matematica da risolvere per selezionare il portafoglio basato su $r_{GMV}$ (Global Minimum Variance) è:
>
> $$\min_x \; \boldsymbol{x}'\boldsymbol{V}\boldsymbol{x}$$
> $$\text{s.t.} \quad \boldsymbol{x}'\boldsymbol{e} = 1$$
>
> La soluzione a questo problema è:
>
> $$\boldsymbol{x} = \frac{\boldsymbol{V}^{-1}\boldsymbol{e}}{\boldsymbol{e}'\boldsymbol{V}^{-1}\boldsymbol{e}}$$
>
> Sia il portafoglio basato su $r_{1/N}$ (equipesato, "1 su N") sia quello basato su $r_{GMV}$ presentano proprietà interessanti, illustrate di seguito.

*(slide 5)*

## Confronto tra portafoglio $r_{1/N}$ e portafoglio $r_{GMV}$

In generale, gli investitori sono interessati al portafoglio basato su $r_{GMV}$ solo se esso domina, in senso media-varianza, il portafoglio basato su $r_{1/N}$.

**Caratteristiche interessanti del portafoglio $r_{1/N}$ (equipesato):**

- è facile da implementare;
- è stato dimostrato che genera una performance apprezzabile;
- evita grandi concentrazioni nello stesso asset;
- investe sempre negli asset che performano meglio;
- non performa mai peggio dell'asset peggiore;
- in caso di grande errore di stima nel processo di ottimizzazione media-varianza, ci si attende che superi in performance l'ottimizzazione media-varianza stessa.

**Caratteristiche interessanti del portafoglio $r_{GMV}$ (varianza minima globale):**

- è efficiente;
- non è influenzato dagli errori di stima relativi ai rendimenti attesi degli asset. [Considerando distribuzioni normali i.i.d. per i rendimenti degli asset, l'intervallo di confidenza per le medie è circa il 40% più ampio dell'intervallo di confidenza per la deviazione standard.]

A seguito della crisi finanziaria del 2007, gli investitori si sono spostati verso portafogli meno rischiosi.

*(slide 6–7)*
