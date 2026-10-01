---
title: "Value-at-Risk (VaR) e Average Value-at-Risk (AVaR/CVaR/ES)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-8-Value-at-Risk.pdf"
pages: 9
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione al Value-at-Risk

Il **Value-at-Risk (VaR)** è una misura di rischio ampiamente utilizzata a partire dagli anni '90.

- A metà degli anni '90 il VaR è stato approvato dal **Comitato di Basilea** come metodo per calcolare la riserva di capitale necessaria a coprire i rischi di mercato.
- Qualitativamente, il VaR è definito come il **livello minimo di perdita** a un dato livello di confidenza, per un orizzonte temporale predefinito.
- I livelli di confidenza raccomandati sono **95%** e **99%**.

**Esempio** — Se deteniamo un portafoglio con un VaR a 1 giorno al 99% pari a €1 milione, allora, sull'orizzonte di 1 giorno, il portafoglio può perdere **almeno** €1 milione con probabilità pari all'1%.

**Figura 5.2** — VaR al livello di confidenza del 95% di una variabile casuale $X$: il grafico superiore mostra la funzione di densità di $X$ con l'area evidenziata (tratteggiata) corrispondente alla probabilità di coda pari al 5%; il grafico inferiore mostra la funzione di ripartizione (distribuzione) di $X$, con la linea orizzontale a quota $0.05$ che interseca la curva in corrispondenza del valore VaR. La figura illustra visivamente come il VaR sia il quantile della distribuzione delle perdite/rendimenti corrispondente alla probabilità di coda scelta.

*(slide 1–2)*

## Definizione formale e proprietà del VaR

> [!abstract] Definizione
> Sia $X$ il payoff rischioso e $(1-\epsilon)$ il livello di confidenza. Formalmente il VaR è definito come
>
> $$VaR_\epsilon(X) = -\inf_x \{x \mid P(X \le x) \ge \epsilon\}.$$
>
> **Alcune proprietà:**
>
> - Sia $C$ un payoff privo di rischio (riskless). Allora
>
> $$VaR_\epsilon(X + C) = VaR_\epsilon(X) - C$$
>
>   (questa proprietà **non** vale per la varianza);
>
> - Sia $\lambda$ una costante positiva. Allora
>
> $$VaR_\epsilon(\lambda X) = \lambda \, VaR_\epsilon(X)$$
>
>   (anche questa proprietà **non** vale per la varianza).

*(slide 3)*

## Limiti (drawback) del VaR

Il VaR presenta alcuni limiti importanti:

- La perdita effettiva può essere **superiore** al VaR (il VaR non dice nulla sull'entità della perdita oltre la soglia).
- In alcuni casi non si osserva il ragionevole effetto di diversificazione: denotando con $X$ e $Y$ due payoff rischiosi, può accadere che

$$VaR_\epsilon(X + Y) > VaR_\epsilon(X) + VaR_\epsilon(Y),$$

  cioè il VaR non è, in generale, subadditivo (il rischio del portafoglio combinato può risultare maggiore della somma dei rischi individuali, contraddicendo il principio di diversificazione).

**Come calcolare il VaR di un'attività (asset)?**
- L'approccio del RiskMetrics Group.
- Il metodo storico.

**Come calcolare il VaR di un portafoglio?**
- L'approccio del RiskMetrics Group.
- Il metodo storico.

*(slide 4)*

## L'approccio del RiskMetrics Group

> [!abstract] Definizione
> **Ipotesi:** i rendimenti azionari (stock returns) seguono una distribuzione normale multivariata.
>
> **VaR di un'attività (asset):**
>
> Si considera la distribuzione normale standard del rendimento dell'attività. I quantili notevoli della normale standard utilizzati sono:
>
> $$z_{0.01} = -2.3263, \qquad z_{0.05} = -1.6449$$
>
> da cui si ricava il VaR come
>
> $$VaR_\epsilon = z_\epsilon \cdot \sigma_{return\_of\_asset} + \mu_{return\_of\_asset}$$
>
> dove $\sigma_{return\_of\_asset}$ e $\mu_{return\_of\_asset}$ sono rispettivamente la deviazione standard e la media del rendimento dell'attività.
>
> **Figura** — Grafico della distribuzione normale standard del rendimento dell'attività: una curva a campana simmetrica centrata in 0, con i due quantili critici $z_{0.01}=-2.3263$ e $z_{0.05}=-1.6449$ indicati da frecce sulla coda sinistra. La figura mostra come i quantili della normale standard, moltiplicati per la deviazione standard del rendimento e traslati per la media, forniscano direttamente il VaR ai livelli di confidenza del 99% e del 95%.
>
> **VaR di un portafoglio:** si procede allo stesso modo (stessa formula, applicata a media e deviazione standard del rendimento del portafoglio).
>
> **Il metodo storico:** si rimanda all'applicazione svolta in Excel (esercitazione pratica, non riportata nelle slide).

*(slide 5–6)*

## Average Value-at-Risk (AVaR), Conditional VaR (CVaR) ed Expected Shortfall (ES)

> [!abstract] Definizione
> L'**Average Value-at-Risk (AVaR)**, detto anche **Conditional Value-at-Risk (CVaR)** o **Expected Shortfall (ES)**, è una misura di rischio **coerente**, priva delle carenze del VaR, e con un'interpretazione intuitiva.
>
> **Definizione formale:**
>
> $$AVaR_\epsilon(X) := \frac{1}{\epsilon} \int_0^\epsilon VaR_p(X)\, dp$$
>
> **Interpretazione intuitiva (confronto VaR vs CVaR):**
>
> - VaR: *"Quanto spesso il mio portafoglio potrebbe perdere almeno $1 milione?"*
> - CVaR: *"Quando il mio portafoglio perde più di $1 milione, quanto potrebbe perdere?"*
>
> Il CVaR risponde quindi alla domanda su **quanto** si perde in media nella coda oltre la soglia del VaR, mentre il VaR risponde solo alla domanda sulla **frequenza/probabilità** del superamento della soglia.
>
> **Figura** — Istogramma delle perdite (asse orizzontale "Loss", asse verticale "Frequency") con indicati, a partire dalla media (Mean) verso destra: il valore **VaR**, il valore **CVaR** e la **perdita massima (Maximum loss)**. È evidenziata la probabilità $1-\alpha$ associata all'intervallo tra VaR e perdita massima. Sono inoltre indicate le distanze "VaR Deviation" (da Mean a VaR), "CVaR Deviation" (da Mean a CVaR) e "Maximum Loss Deviation" (da Mean a Maximum loss). La figura mostra come il CVaR si collochi più a destra del VaR nella coda della distribuzione delle perdite, rappresentando la perdita media condizionata al superamento della soglia VaR, ed è quindi una misura più prudenziale e informativa sull'entità delle perdite estreme.

*(slide 7–8)*

## Calcolo dell'AVaR

**Come calcolare l'AVaR di un'attività o di un portafoglio?**

- Metodo storico (l'unico metodo indicato nelle slide per il calcolo pratico dell'AVaR).

*(slide 9)*
