---
title: "Annotazioni sul Terminal Value nel modello dei DCF"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_05_Annotazioni-sul-Terminal-Value.pdf"
pages: 3
text_layer: true
verified: true
generated: 2026-08-30
---

## Il paradosso apparente del Terminal Value

Il Terminal Value (TV), pur essendo una perpetuità, in molti casi vale quanto "soli" 5 anni di piano (il periodo di previsione esplicita).

In prima analisi può sembrare contraddittorio affermare che il valore di una perpetuità — cioè di flussi che continuano per sempre — abbia un ordine di grandezza simile ai soli flussi dei primi cinque anni.

L'apparente paradosso nasce da tre elementi.

**1. L'attualizzazione riduce drasticamente il peso dei flussi lontani**

Il fattore di sconto $(1+WACC)^t$ cresce in modo esponenziale. Con un WACC del 9–10%, i flussi oltre 20 anni valgono poco a valore attuale.

Questo significa che, pur avendo una vita teoricamente infinita, i flussi generati molto avanti nel tempo contribuiscono in misura limitata al valore odierno, perché vengono scontati molte volte.

**2. La crescita di lungo periodo $g$ è molto bassa**

Nel Terminal Value non è possibile assumere che l'impresa cresca per sempre come nella fase espansiva del piano strategico. La crescita a regime è solitamente più prudente: tipicamente compresa tra 0% e 2%.

Ciò implica che i flussi della perpetuità non esplodono nel tempo: aumentano lentamente e quindi il loro valore complessivo rimane contenuto.

**3. La fase esplicita rappresenta gli anni in cui l'impresa crea più valore**

Nel piano (3–5 anni):
- l'impresa cresce sopra il mercato,
- migliora i margini,
- fa investimenti importanti,
- realizza rendimenti superiori alla media.

Nella perpetuità, invece, l'impresa è già in regime stabile: flussi regolari, margini normalizzati, crescita bassa. È quindi del tutto fisiologico che i primi anni, dove l'impresa sta realmente creando valore economico, abbiano un peso rilevante, nonostante la presenza della perpetuità.

**Conclusione.** Si può assumere che il TV rappresenti sì molti anni, ma flussi molto lontani e poco crescenti. Il piano strategico, invece, rappresenta pochi anni, ma flussi vicini e ad alta intensità di valore. L'effetto matematico è che la parte esplicita contribuisce in modo significativo al valore complessivo, e la perpetuità non domina automaticamente la valutazione.

*(slide 1)*

## Esempio 1 — TV al 75% (modello equilibrato)

> [!example] Esempio
> **Ipotesi**
> - $FCFF_0 = 100$
> - Crescita del piano: +20% annuo
> - $WACC = 10\%$
> - $g = 2\%$
> - Piano: 5 anni
>
> **1. Flussi del piano**
>
> $$FCFF_1 = 120, \quad FCFF_2 = 144, \quad FCFF_3 = 173, \quad FCFF_4 = 207, \quad FCFF_5 = 249$$
>
> **2. Valore attuale del piano**
>
> $$PV_{piano} = 653$$
>
> **3. Terminal Value**
>
> Flusso dell'anno 6:
>
> $$FCFF_6 = 249(1 + 0{,}02) = 254$$
>
> Formula della perpetuity:
>
> $$TV = \frac{254}{0{,}10 - 0{,}02} = 3.175$$
>
> Attualizzazione:
>
> $$PV_{TV} = \frac{3.175}{1{,}10^5} = 1.971$$
>
> **4. Risultato**
>
> $$V = 653 + 1.971 = 2.624$$
> $$Peso_{TV} = 75\%$$
>
> In questo scenario equilibrato (differenziale $WACC - g = 8\%$), il Terminal Value pesa il 75% del valore totale dell'impresa, mentre il piano esplicito contribuisce per il restante 25%.

*(slide 2)*

## Esempio 2 — TV al 90% (modello distorto)

> [!example] Esempio
> Si evidenzia cosa accade quando il differenziale $WACC - g$ diventa troppo piccolo.
>
> **Ipotesi**
> - $FCFF_0 = 100$
> - Crescita del piano: +10% annuo
> - $WACC = 7\%$
> - $g = 4\%$
> - Piano: 5 anni
>
> **1. Flussi del piano**
>
> $$FCFF_1 = 110, \quad FCFF_2 = 121, \quad FCFF_3 = 133, \quad FCFF_4 = 146, \quad FCFF_5 = 161$$
>
> $$PV_{piano} = 541$$
>
> **2. Terminal Value**
>
> Flusso dell'anno 6:
>
> $$FCFF_6 = 161(1 + 0{,}04) = 167$$
>
> $$TV = \frac{167}{0{,}07 - 0{,}04} = 5.567$$
>
> Attualizzazione:
>
> $$PV_{TV} = \frac{5.567}{1{,}07^5} = 3.976$$
>
> **Risultato**
>
> $$V = 541 + 3.976 = 4.517$$
> $$Peso_{TV} = 88\%$$
>
> Con un differenziale $WACC - g$ ridotto a soli 3 punti percentuali, il peso del Terminal Value sale all'88% del valore totale. Con un minimo aumento di $g$ al 4,5% il peso supererebbe immediatamente il 90%, illustrando quanto la valutazione diventi sensibile e potenzialmente distorta quando lo spread tra WACC e crescita di lungo periodo si comprime.

*(slide 3)*
