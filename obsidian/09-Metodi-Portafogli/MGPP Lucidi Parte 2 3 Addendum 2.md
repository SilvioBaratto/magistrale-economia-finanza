---
title: "Il teorema dei due fondi comuni (Two Mutual Fund Theorem)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-2-3-Addendum-2.pdf"
pages: 7
text_layer: true
verified: true
generated: 2026-07-10
---

## Enunciato del Teorema dei due fondi comuni

> [!tip] Teorema
> **Two Mutual Fund Theorem.** Qualunque portafoglio situato sulla frontiera efficiente può essere costruito come combinazione di due qualsiasi portafogli efficienti appartenenti a quella stessa frontiera. Questi due portafogli sono i "fondi comuni" (mutual funds) a cui il teorema fa riferimento.
>
> Se il portafoglio obiettivo (target):
> - **si trova tra** i due fondi comuni sulla frontiera, allora entrambi i fondi vengono detenuti in quantità **positive**;
> - **si trova al di fuori** dell'intervallo generato dai due fondi, allora uno dei due deve essere venduto **allo scoperto** (short, cioè detenuto in quantità negativa), mentre la posizione nell'altro deve **eccedere il capitale disponibile dell'investitore**, con l'eccesso finanziato tramite l'indebitamento generato dalla posizione corta.

*(slide 1–2)*

## Figura: frontiera efficiente parabolica e frontiera efficiente lineare

**Figura** — Grafico con in ascissa la deviazione standard dei rendimenti $\sigma_p$ e in ordinata il valore atteso dei rendimenti $\mu_p$. Sono rappresentate:
- la **Parabolic EF** (frontiera efficiente parabolica, in blu), cioè la classica frontiera efficiente di Markowitz ottenuta con soli titoli rischiosi (ramo superiore continuo, ramo inferiore tratteggiato e non efficiente);
- la **Linear EF** (frontiera efficiente lineare, in rosso), cioè la semiretta che parte dal tasso privo di rischio ed è tangente all'iperbole;
- il punto **Risk-free rate** (pallino pieno rosso), sull'asse verticale, corrispondente a $\sigma_p = 0$;
- il punto **Tangency portfolio** (cerchio vuoto rosso), punto di tangenza tra la semiretta e la frontiera parabolica.

La figura mostra come, introducendo un asset privo di rischio, la nuova frontiera efficiente non sia più la porzione superiore dell'iperbole (frontiera di Markowitz per soli asset rischiosi) ma la semiretta che congiunge il tasso privo di rischio con il portafoglio di tangenza: questa semiretta domina (in termini di rapporto rendimento/rischio) l'iperbole stessa, poiché per ogni livello di rischio $\sigma_p$ consente un rendimento atteso $\mu_p$ maggiore o uguale.

*(slide 3)*

## L'asset privo di rischio e la nuova frontiera efficiente

> [!abstract] Definizione
> **L'asset privo di rischio (risk-free asset)** è un titolo che rende il tasso privo di rischio (risk-free rate). Esso:
> - ha **varianza del rendimento nulla**;
> - è **incorrelato** con tutti gli altri asset.
>
> Nella pratica, come asset privo di rischio si utilizzano **titoli di stato a breve termine** (short-term government securities).
>
> Quando un asset privo di rischio viene introdotto nell'analisi, la **semiretta** mostrata nella figura precedente diventa la **nuova frontiera efficiente**, sostituendo il ramo superiore dell'iperbole di Markowitz.
>
> **Caratteristiche principali della nuova frontiera efficiente:**
> - La sua **intercetta** corrisponde a un portafoglio investito al **100% nell'asset privo di rischio**.
> - Il **punto di tangenza** con l'iperbole corrisponde a un portafoglio investito al **100% nel portafoglio rischioso di tangenza** (risky tangency portfolio).
> - I portafogli **compresi tra questi due punti** contengono quantità positive sia dell'asset privo di rischio sia del portafoglio rischioso di tangenza.
> - I portafogli sulla semiretta **oltre il punto di tangenza** sono **portafogli a leva** (leveraged portfolios): comportano una quantità **negativa** dell'asset privo di rischio (cioè l'asset privo di rischio viene venduto allo scoperto; in altre parole, l'investitore si indebita al tasso privo di rischio) e **più del 100%** del capitale iniziale dell'investitore risulta investito nel portafoglio di tangenza.

*(slide 4–5)*

## Equazione della nuova frontiera efficiente lineare

> [!abstract] Definizione
> L'equazione della nuova semiretta efficiente è:
>
> $$\mathbb{E}(R_C) = R_F + \sigma_C \, \frac{\mathbb{E}(R_P) - R_F}{\sigma_P}$$
>
> dove:
> - $P$ indica il **portafoglio rischioso di tangenza**;
> - $F$ indica l'**asset privo di rischio** (free-risk asset);
> - $C$ indica **una qualsiasi combinazione** di $P$ e $F$.
>
> Si noti che il **portafoglio di tangenza** ha il **più alto rapporto di Sharpe** (Sharpe ratio) tra tutti i portafogli disponibili: il coefficiente angolare della semiretta, $\dfrac{\mathbb{E}(R_P) - R_F}{\sigma_P}$, è infatti proprio lo Sharpe ratio del portafoglio di tangenza, ed è il massimo ottenibile lungo la frontiera.

*(slide 6)*
