---
title: "Il terminal value nei modelli DCF"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_05_Annotazioni-sul-Terminal-Value.pdf"
text_layer: true
verified: true
generated: 2026-08-30
---

## Il paradosso apparente del Terminal Value

Il Terminal Value (TV) è il valore di una perpetuità, ma in molti casi ha un ordine di grandezza simile a quello dei flussi dei soli cinque anni del piano, il periodo di previsione esplicita. A prima vista appare contraddittorio che flussi destinati a continuare per sempre valgano quanto quelli dei primi cinque anni. Il paradosso è solo apparente e dipende da tre elementi.

### L'attualizzazione riduce il peso dei flussi lontani

Il fattore di sconto $(1+WACC)^t$ cresce in modo esponenziale con $t$. Con un WACC del 9–10% un flusso del ventesimo anno viene diviso per un fattore compreso tra 5,6 e 6,7 ($1{,}09^{20} \approx 5{,}6$; $1{,}10^{20} \approx 6{,}7$), e i flussi ancora più lontani per fattori maggiori. Pur avendo una vita teoricamente infinita, l'impresa genera quindi flussi molto distanti nel tempo che, scontati molte volte, contribuiscono in misura limitata al valore odierno.

### La crescita di lungo periodo è molto bassa

Nel Terminal Value non si può assumere che l'impresa continui a crescere come nella fase espansiva del piano strategico. La crescita a regime è più prudente e di norma sta tra lo 0% e il 2%. I flussi della perpetuità aumentano perciò lentamente, e il loro valore complessivo resta contenuto.

### La fase esplicita è quella in cui l'impresa crea più valore

Nel piano, di 3–5 anni, l'impresa cresce più del mercato, migliora i margini, effettua investimenti importanti e ottiene rendimenti superiori alla media. Nella perpetuità si trova invece già in regime stabile, con flussi regolari, margini normalizzati e crescita bassa. È dunque coerente che i primi anni, in cui si crea effettivamente valore economico, abbiano un peso rilevante nonostante la presenza della perpetuità.

Il TV copre molti anni, ma di flussi molto lontani e poco crescenti; il piano copre pochi anni, ma di flussi vicini e ad alta intensità di valore. Ne segue che la parte esplicita contribuisce in misura significativa al valore complessivo e che la perpetuità non domina automaticamente la valutazione. Il peso del TV dipende da WACC, da $g$ e dalla crescita del piano: nei due esempi seguenti è pari al 75% e all'88% del valore totale.

## La formula del Terminal Value e le condizioni di validità

Il Terminal Value al termine dell'anno $N$ dell'orizzonte esplicito è il valore, a quella data, dei flussi successivi, assunti crescenti al tasso costante $g$ a partire da $FCFF_{N+1}$. La somma è una progressione geometrica, la perpetuità crescente (modello di Gordon):

$$TV_N = \sum_{k=1}^{\infty} \frac{FCFF_{N+1}(1+g)^{k-1}}{(1+WACC)^k} = \frac{FCFF_{N+1}}{WACC - g}$$

Il valore attuale del TV si ottiene dividendolo per $(1+WACC)^N$.

La serie converge solo se $g < WACC$: per $g \to WACC$ il TV tende a infinito e per $g \ge WACC$ la formula perde significato. Il fattore $\frac{1}{WACC - g}$ moltiplica il flusso: vale 12,5 con un differenziale dell'8%, 33,3 con il 3%, 40 con il 2,5%. Quando il differenziale si restringe, il TV diventa quindi molto sensibile a piccole variazioni di $g$ e del WACC. Come limite superiore per $g$ si assume in genere la crescita nominale di lungo periodo dell'economia in cui opera l'impresa.

Il flusso $FCFF_{N+1}$ deve inoltre essere coerente con $g$, perché la crescita richiede investimenti. Nella formulazione completa del [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|terminal value con flussi in crescita]] il flusso della perpetuità è $NOPAT_N(1+g) - CINO_N \cdot g$, dove $CINO_N$ è il capitale investito netto operativo a fine anno $N$ e $CINO_N \cdot g$ è il reinvestimento che lo fa crescere al tasso $g$. Gli esempi che seguono adottano una semplificazione: ottengono $FCFF_6$ moltiplicando $FCFF_5$ per $(1+g)$, senza scomporre il flusso in NOPAT e reinvestimento.

Indicando con $ROIC = NOPAT_{N+1}/CINO_N$ il rendimento del capitale investito, il reinvestimento assorbe la quota $g/ROIC$ del NOPAT e il TV diventa

$$TV_N = \frac{NOPAT_{N+1}\left(1 - \dfrac{g}{ROIC}\right)}{WACC - g}$$

Se $ROIC = WACC$ il TV è pari a $NOPAT_{N+1}/WACC$ per qualunque $g$: la crescita assorbe capitale con un rendimento pari al costo del capitale e non aggiunge valore. Con $ROIC > WACC$ il TV aumenta al crescere di $g$, con $ROIC < WACC$ diminuisce.

## Esempio 1: TV al 75% (modello equilibrato)

> [!example] Esempio
> **Ipotesi**
> - $FCFF_0 = 100$
> - crescita del piano: +20% annuo
> - $WACC = 10\%$
> - $g = 2\%$
> - piano esplicito di 5 anni
>
> Gli importi sono arrotondati all'unità.
>
> **1. Flussi del piano**
>
> $$FCFF_1 = 120, \quad FCFF_2 = 144, \quad FCFF_3 = 173, \quad FCFF_4 = 207, \quad FCFF_5 = 249$$
>
> **2. Valore attuale del piano**
>
> $$PV_{piano} = \sum_{t=1}^{5} \frac{FCFF_t}{1{,}10^t} = 654$$
>
> **3. Terminal Value**
>
> Flusso dell'anno 6:
>
> $$FCFF_6 = 249(1 + 0{,}02) = 254$$
>
> Perpetuità crescente:
>
> $$TV = \frac{254}{0{,}10 - 0{,}02} = 3.175$$
>
> Attualizzazione al tempo 0:
>
> $$PV_{TV} = \frac{3.175}{1{,}10^5} = 1.971$$
>
> **4. Risultato**
>
> $$V = 654 + 1.971 = 2.625$$
> $$Peso_{TV} = \frac{1.971}{2.625} = 75\%$$
>
> Con un differenziale $WACC - g = 8\%$ il TV pesa il 75% del valore totale e il piano esplicito contribuisce per il restante 25%.

## Esempio 2: TV all'88% (modello distorto)

> [!example] Esempio
> L'esempio mostra che cosa accade quando il differenziale $WACC - g$ diventa troppo piccolo.
>
> **Ipotesi**
> - $FCFF_0 = 100$
> - crescita del piano: +10% annuo
> - $WACC = 7\%$
> - $g = 4\%$
> - piano esplicito di 5 anni
>
> Gli importi sono arrotondati all'unità.
>
> **1. Flussi del piano**
>
> $$FCFF_1 = 110, \quad FCFF_2 = 121, \quad FCFF_3 = 133, \quad FCFF_4 = 146, \quad FCFF_5 = 161$$
>
> $$PV_{piano} = \sum_{t=1}^{5} \frac{FCFF_t}{1{,}07^t} = 543$$
>
> **2. Terminal Value**
>
> Flusso dell'anno 6:
>
> $$FCFF_6 = 161(1 + 0{,}04) = 167$$
>
> $$TV = \frac{167}{0{,}07 - 0{,}04} = 5.567$$
>
> Attualizzazione al tempo 0:
>
> $$PV_{TV} = \frac{5.567}{1{,}07^5} = 3.969$$
>
> **3. Risultato**
>
> $$V = 543 + 3.969 = 4.512$$
> $$Peso_{TV} = \frac{3.969}{4.512} = 88\%$$
>
> **Variante con $g = 4{,}5\%$**
>
> $$FCFF_6 = 161(1 + 0{,}045) = 168, \quad TV = \frac{168}{0{,}07 - 0{,}045} = 6.720, \quad PV_{TV} = \frac{6.720}{1{,}07^5} = 4.791$$
>
> $$V = 543 + 4.791 = 5.334, \qquad Peso_{TV} = \frac{4.791}{5.334} \approx 89{,}8\%$$

Con un differenziale $WACC - g$ ridotto a 3 punti percentuali il TV pesa l'88% del valore totale. Un aumento di $g$ di mezzo punto, al 4,5%, porta il differenziale a 2,5 punti e il peso a circa l'89,8%, quasi il 90%, mentre il valore dell'impresa sale da 4.512 a 5.334 (+18%). La valutazione risulta quindi molto sensibile a $g$ e potenzialmente distorta quando lo spread tra WACC e crescita di lungo periodo si comprime. Il valore $g = 4\%$ supera inoltre l'intervallo 0–2% indicato come tipico per la crescita a regime.

Nel [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|controllo del peso del terminal value]] un rapporto $TV/V$ superiore a circa l'85–90% è considerato un segnale di anomalia: possibili errori nei flussi espliciti, un orizzonte esplicito troppo breve, oppure l'inutilità di una stima analitica rispetto a un metodo sintetico. Entrambi gli scenari di questo esempio rientrano in quella fascia.
