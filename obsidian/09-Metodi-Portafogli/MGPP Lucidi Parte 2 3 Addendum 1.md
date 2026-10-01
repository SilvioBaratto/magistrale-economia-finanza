---
title: "Addendum 1 — Frontiera con due titoli rischiosi: i casi limite di correlazione perfetta (ρ = +1 e ρ = −1)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-2-3-Addendum-1.pdf"
pages: 2
text_layer: false
verified: true
generated: 2026-07-10
---

## Impostazione: portafoglio con due titoli rischiosi (N = 2)

Si considera un portafoglio composto da $N=2$ titoli rischiosi, con pesi $x_1, x_2 \in \mathbb{R}$: a differenza del caso con vincolo $x_1,x_2\in[0,1]$ (solo posizioni lunghe), qui si ammettono esplicitamente vendite allo scoperto (short selling), cioè pesi negativi o superiori a 1. Vale comunque il vincolo di bilancio implicito $x_1+x_2=1$, per cui $x_2 = 1-x_1$.

L'obiettivo dell'addendum è studiare come cambia la forma della frontiera nel piano $(\sigma, r)$ — rischio (deviazione standard) in ascissa, rendimento atteso in ordinata — nei due casi estremi di correlazione tra i due titoli: $\rho_{1,2}=+1$ (correlazione perfetta positiva) e $\rho_{1,2}=-1$ (correlazione perfetta negativa). In entrambi i grafici, i due titoli sono rappresentati da due punti: il titolo 1 a rischio più basso $(\sigma_1, r_1)$ e il titolo 2 a rischio più alto $(\sigma_2, r_2)$, con $\sigma_2>\sigma_1>0$.

*(slide 1)*

## Correlazione perfetta positiva (ρ = +1): frontiera lineare, portafoglio privo di rischio e portafoglio dominante

> [!tip] Teorema
> **Caso $\rho_{1,2}=+1$.**
>
> **Grafico** — Nel piano $(\sigma,r)$ i due titoli sono collegati da un **segmento di retta** (non da una curva concava come nel caso generale): ciò riflette il fatto che con correlazione perfetta positiva non vi è alcun beneficio di diversificazione. Per pesi $x_1,x_2\in[0,1]$ (nessuna vendita allo scoperto) si ottiene esattamente il tratto di retta compreso tra i due titoli (parte continua del grafico). La stessa retta può essere prolungata in entrambe le direzioni ammettendo vendite allo scoperto:
> - a sinistra del titolo 1 (rischio ancora più basso), il tratto tratteggiato corrisponde a pesi $x_1>1,\; x_2<0$;
> - a destra del titolo 2 (rischio ancora più alto), il tratto tratteggiato corrisponde a pesi $x_1<0,\; x_2>1$.
>
> Da questa configurazione derivano due risultati.
>
> **Risultato 1 — Esiste un portafoglio privo di rischio.** Poiché con $\rho=+1$ non c'è diversificazione, il rischio del portafoglio è semplicemente la combinazione lineare (in valore assoluto) dei rischi individuali; per $x_1\in[0,1]$ vale:
> $$\sigma_p = x_1\sigma_1+(1-x_1)\sigma_2$$
> Imponendo $\sigma_p=0$ e risolvendo per $x_1$:
> $$x_1\sigma_1+(1-x_1)\sigma_2=0 \;\Longrightarrow\; x_1(\sigma_1-\sigma_2)=-\sigma_2 \;\Longrightarrow\; x_1=\frac{\sigma_2}{\sigma_2-\sigma_1}$$
> e di conseguenza:
> $$x_2 = 1-x_1 = -\frac{\sigma_1}{\sigma_2-\sigma_1}$$
> Poiché $\sigma_2>\sigma_1>0$, si ha $x_1>1$ e $x_2<0$: il portafoglio privo di rischio richiede quindi di vendere allo scoperto il titolo 2 e di investire più del 100% della ricchezza nel titolo 1. Questo è coerente con la regione di sinistra del grafico ($x_1>1,x_2<0$), che infatti si estende fino a $\sigma_p=0$.
>
> **Risultato 2 — Esiste un portafoglio rischioso che domina il titolo 2 in rendimento.** È possibile costruire un portafoglio per cui $r_p > r_2$ (pur avendo anche $\sigma_p>\sigma_2$): ciò corrisponde alla regione a destra del titolo 2 nel grafico, ottenuta con pesi $x_1<0,\;x_2>1$ (vendita allo scoperto del titolo 1, posizione a leva sul titolo 2).

*(slide 1–2)*

## Correlazione perfetta negativa (ρ = −1): frontiera spezzata e portafoglio privo di rischio senza vendite allo scoperto

**Caso $\rho_{1,2}=-1$.**

**Grafico** — Nel piano $(\sigma,r)$ la frontiera è ora costituita da **due segmenti di retta** che si incontrano in un punto sull'asse verticale, cioè con $\sigma_p=0$: a differenza del caso $\rho=+1$, questo portafoglio privo di rischio si ottiene già con pesi $x_1,x_2\in[0,1]$, cioè **senza bisogno di vendite allo scoperto**. Dal punto a rischio nullo partono due rami:
- un ramo passa per il titolo 1 e, oltre il titolo 1, continua come tratteggio corrispondente a pesi $x_1>1,\;x_2<0$; questo intero ramo (compreso il tratto verso il titolo 1) è etichettato come **"PORTAFOGLI INEFFICIENTI"**;
- l'altro ramo passa per il titolo 2 e, oltre il titolo 2, continua come tratteggio corrispondente a pesi $x_1<0,\;x_2>1$.

La conclusione è che, nel caso limite opposto di correlazione perfetta negativa, la copertura reciproca tra i due titoli è talmente forte da permettere l'azzeramento completo del rischio di portafoglio usando solo posizioni lunghe. Tuttavia solo uno dei due rami che si dipartono dal punto a rischio nullo è efficiente (quello con il rendimento atteso più alto a parità di rischio); il ramo verso il titolo con rendimento più basso — e il suo prolungamento ottenuto con $x_1>1,x_2<0$ — è dominato, a parità di $\sigma_p$, da portafogli sull'altro ramo con rendimento maggiore, e viene perciò classificato come insieme di portafogli inefficienti.

*(slide 2)*
