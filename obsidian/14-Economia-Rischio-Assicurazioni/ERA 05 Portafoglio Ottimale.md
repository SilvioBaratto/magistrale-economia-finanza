---
title: "Portafoglio ottimale: investimento nel titolo rischioso e statica comparativa rispetto ad avversione, ricchezza e rischio"
tags:
  - corso/economia-rischio-assicurazioni
  - tipo/lezione
corso: "[[Economia del Rischio e delle Assicurazioni]]"
source: "ERA_Slide_04_Portafoglio-Ottimale.pdf"
text_layer: true
verified: true
generated: 2026-11-22
---

## Oggetto del capitolo

Il capitolo studia come un agente avverso al rischio ripartisce la propria ricchezza tra un titolo privo di rischio (a rischio zero) e un titolo rischioso. Con un solo titolo rischioso il problema è il modello standard di scelta del portafoglio. Le domande sono due: quanto denaro l'agente investe in ciascun titolo, e come la risposta dipende dall'avversione al rischio, dalla ricchezza iniziale e dal profilo di rischiosità del titolo rischioso. Ciascuno dei tre fattori ha una sezione di statica comparativa, cioè lo studio di come cambia la soluzione quando cambia un dato del problema.

Il capitolo segue il [[ERA 04 Confronto di Opzioni Rischiose|confronto di opzioni rischiose]] e usa le misure di [[ERA 03 Avversione al Rischio|avversione al rischio]] e la dominanza stocastica. Il capitolo [[ERA 06 Prezzo dei Titoli|prezzo dei titoli]] usa la condizione del primo ordine ricavata qui, e il segno della domanda, per spiegare i prezzi dei titoli. Prima di impostare il problema si richiamano gli strumenti già definiti, con l'aggiunta della prudenza relativa e delle condizioni di bordo del massimo su un intervallo.

## Strumenti richiamati dai capitoli precedenti

### Misure di avversione al rischio e prudenza relativa

Per una funzione di utilità $u$ (di Bernoulli) con $u'>0$ e $u''<0$, le misure di [[ERA 03 Avversione al Rischio|avversione al rischio]] a ricchezza $w$ sono l'avversione assoluta, l'avversione relativa e la prudenza assoluta:

$$A(w)=-\frac{u''(w)}{u'(w)},\qquad RR(w)=w\,A(w),\qquad P(w)=-\frac{u'''(w)}{u''(w)}.$$

Con $u''<0$ le prime due sono positive, e $P>0$ equivale a $u'''>0$. Il capitolo usa anche la prudenza relativa, che si ottiene dalla prudenza assoluta nello stesso modo in cui $RR$ si ottiene da $A$.

> [!abstract] Definizione
> La **prudenza relativa** è
>
> $$RP(w)=w\,P(w)=-w\,\frac{u'''(w)}{u''(w)}.$$

Le tre utilità di riferimento sono l'utilità con avversione assoluta al rischio costante (CARA, *constant absolute risk aversion*), $u(w)=-e^{-\lambda w}/\lambda$ con $\lambda>0$, l'utilità con avversione relativa al rischio costante (CRRA, *constant relative risk aversion*), $u(w)=w^{1-\gamma}/(1-\gamma)$ con $\gamma>0$ e $\gamma\neq1$, e il logaritmo, che è il caso $\gamma=1$ della CRRA. Le loro misure sono:

| $u(w)$ | $A(w)$ | $RR(w)$ | $P(w)$ | $RP(w)$ |
|---|---|---|---|---|
| CARA, $-e^{-\lambda w}/\lambda$ | $\lambda$ | $\lambda w$ | $\lambda$ | $\lambda w$ |
| CRRA, $w^{1-\gamma}/(1-\gamma)$ | $\gamma/w$ | $\gamma$ | $(1+\gamma)/w$ | $1+\gamma$ |
| logaritmo, $\ln w$ | $1/w$ | $1$ | $2/w$ | $2$ |

### Dominanza stocastica

Il confronto fra due distribuzioni del rendimento usa la dominanza stocastica del [[ERA 04 Confronto di Opzioni Rischiose|capitolo precedente]]. Con $E_F[v(\tilde x)]$ si indica l'attesa di $v(\tilde x)$ quando il rendimento $\tilde x$, una variabile casuale, ha funzione di ripartizione (c.d.f.) $F$, cioè $E_F[v(\tilde x)]=\int v\,dF$. Il materiale del corso scrive la stessa grandezza $E[v\mid F]$: la barra indica la distribuzione con cui si calcola l'attesa, non un condizionamento, e qui si usa il pedice, come lì, per non confonderla con il valore atteso condizionato $E[\cdot\mid\cdot]$. L'espressione «$F_2$ domina $F_1$» significa che $F_2$ è preferita a $F_1$; al secondo ordine, seguendo la convenzione del corso, si dice anche che è meno rischiosa, un uso che coincide con l'aumento del rischio del capitolo precedente quando le medie sono uguali. Resta da stabilire per quali funzioni $v$ la dominanza implica $E_{F_2}[v(\tilde x)]\ge E_{F_1}[v(\tilde x)]$.

> [!tip] Teorema
> Siano $F_1$ e $F_2$ due c.d.f.
>
> 1. Se $F_2$ domina $F_1$ al primo ordine (FOSD), cioè $F_2(x)\le F_1(x)$ per ogni $x$, allora $E_{F_2}[v(\tilde x)]\ge E_{F_1}[v(\tilde x)]$ per ogni funzione $v$ crescente.
> 2. Se $F_2$ domina $F_1$ al secondo ordine (SOSD), cioè $\int_{\underline x}^{x}F_2(\theta)\,d\theta\le\int_{\underline x}^{x}F_1(\theta)\,d\theta$ per ogni $x$, dove $\underline x$ è l'estremo inferiore dei valori possibili, allora $E_{F_2}[v(\tilde x)]\ge E_{F_1}[v(\tilde x)]$ per ogni funzione $v$ crescente e concava.

Per ogni agente con utilità crescente la FOSD basta a preferire $F_2$; per un agente con utilità crescente e concava, cioè avverso al rischio, basta la SOSD. Ogni dominanza del primo ordine è anche del secondo. Dimostrazioni e condizioni equivalenti sono nel capitolo di origine; qui servono solo queste implicazioni.

### Massimo di una funzione strettamente concava su un intervallo

Una funzione strettamente concava e derivabile ha al più un punto stazionario, che è il suo massimo globale ([[ERA 01 Ripasso|ripasso di matematica]]). Il problema di portafoglio richiede la versione su un intervallo chiuso $[a,b]$.

> [!tip] Teorema
> Sia $V:[a,b]\to\mathbb R$ strettamente concava e derivabile. Se $V'(\alpha^*)=0$ per un $\alpha^*\in(a,b)$, allora $\alpha^*$ è l'unico massimo di $V$ su $[a,b]$, e per ogni $\alpha\in[a,b]$ si ha $V'(\alpha)>0$ se e solo se $\alpha<\alpha^*$.

La dimostrazione è quella del punto 4 del teorema sulla condizione del primo ordine nel [[ERA 01 Ripasso|ripasso]]: la derivata di una funzione strettamente concava e derivabile è strettamente decrescente, positiva a sinistra di $\alpha^*$ e negativa a destra. Il risultato riguarda il massimo interno, in cui il vincolo dell'intervallo non è attivo. Agli estremi la derivata decrescente dà le condizioni di bordo: il massimo è in $a$ se e solo se $V'(a)\le0$, perché allora $V'\le0$ su tutto l'intervallo, ed è in $b$ se e solo se $V'(b)\ge0$. Se invece $V'(a)>0>V'(b)$ il massimo è interno e annulla la derivata.

## Il problema di portafoglio

Un agente ha ricchezza iniziale $W>0$ e una funzione di utilità $u$ crescente, concava e tre volte derivabile. La crescita di $u$ esprime la preferenza per una ricchezza maggiore, la concavità rende l'agente avverso al rischio. Dove serve un ottimo unico si assume $u''<0$. Investe un ammontare $\alpha$ nel titolo rischioso e il resto, $W-\alpha$, nel titolo privo di rischio. Un euro nel titolo privo di rischio diventa $1+r$, dove $r$ è il rendimento netto. Un euro nel titolo rischioso diventa $1+\tilde x_0$, dove il rendimento netto $\tilde x_0$ è una variabile casuale. La tilde segnala una variabile casuale; la stessa lettera senza tilde, $x$, indica una sua realizzazione.

La ricchezza finale dell'agente è

$$(W-\alpha)(1+r)+\alpha(1+\tilde x_0)=W(1+r)+\alpha(\tilde x_0-r)=w_0+\alpha\tilde x,$$

con $w_0=W(1+r)$ e $\tilde x=\tilde x_0-r$. Il numero $w_0$ è la ricchezza finale che l'agente ottiene con certezza se non investe nel titolo rischioso. La variabile $\tilde x$ è il **rendimento in eccesso** del titolo rischioso rispetto a quello privo di rischio: l'investimento nel titolo rischioso aggiunge a $w_0$ la quantità $\alpha\tilde x$. Il problema dell'agente è

$$\max_{\alpha\in[0,W]}V(\alpha)=E\big[u\big(w_0+\alpha\tilde x\big)\big],\qquad V(\alpha)=E\big[u\big((W-\alpha)(1+r)+\alpha(1+\tilde x_0)\big)\big].$$

L'attesa è calcolata con la distribuzione $F$ di $\tilde x$. Per una variabile con valori $x_s$ e probabilità $\pi_s$ è la somma $\sum_s\pi_s\,u(w_0+\alpha x_s)$ della [[ERA 02 Teoria dell'Utilità Attesa|teoria dell'utilità attesa]]; per una variabile con densità è l'integrale corrispondente.

Tre simboli hanno qui un significato diverso da quello dei capitoli precedenti. In [[ERA 03 Avversione al Rischio|avversione al rischio]] $W$ è l'argomento di $u$; qui è la ricchezza iniziale da investire, e l'argomento di $u$ si scrive sempre in modo esplicito. Il numero $w_0$ ha il ruolo del $w$ di quel capitolo: è la ricchezza certa a cui si somma la parte aleatoria $\alpha\tilde x$, che non ha media nulla. Il simbolo $\alpha$, che nella [[ERA 02 Teoria dell'Utilità Attesa|teoria dell'utilità attesa]] è un peso di miscela, indica qui l'ammontare investito nel titolo rischioso, non una quota.

Il modello poggia su alcune ipotesi. C'è un solo titolo rischioso, e il titolo privo di rischio è disponibile in quantità illimitata al rendimento $r$. La funzione $u$ è derivabile e si può derivare sotto il segno di attesa, il che è lecito se $\tilde x$ ha un numero finito di valori. Il vincolo $\alpha\in[0,W]$ esclude le vendite allo scoperto ($\alpha<0$) e l'indebitamento ($\alpha>W$). Senza il vincolo l'ottimo potrebbe essere negativo o superiore a $W$; con il vincolo le conclusioni sul segno dell'investimento cambiano solo quando il rendimento atteso è negativo, caso trattato più avanti.

## La condizione del primo ordine

Il metodo consiste nel sostituire la massimizzazione con l'annullarsi della derivata di $V$, procedimento detto *first-order approach*. Derivando $V$ sotto il segno di attesa si ottengono la derivata prima, cioè la condizione del primo ordine (FOC), e la derivata seconda:

$$V'(\alpha)=E\big[\tilde x\,u'(w_0+\alpha\tilde x)\big],\qquad V''(\alpha)=E\big[\tilde x^{2}\,u''(w_0+\alpha\tilde x)\big].$$

La derivata prima è l'utilità marginale attesa di spostare un euro dal titolo privo di rischio a quello rischioso: quell'euro rende $\tilde x$ in più, valutato con l'utilità marginale $u'$ dello stato in cui il rendimento si realizza. All'ottimo i guadagni attesi pesati in questo modo compensano le perdite attese. Poiché $u''\le0$ e $\tilde x^2\ge0$, la derivata seconda è non positiva: la funzione obiettivo è concava in $\alpha$ e la FOC, oltre che necessaria all'interno, è sufficiente per un massimo.

> [!tip] Teorema
> Siano $u'>0$ e $u''<0$, e sia $\mathbb P(\tilde x\neq0)>0$. Allora $V$ è strettamente concava su $[0,W]$ e il problema ha una sola soluzione $\alpha^*$. Inoltre $\alpha^*=0$ se e solo se $V'(0)\le0$, $\alpha^*=W$ se e solo se $V'(W)\ge0$, e negli altri casi $0<\alpha^*<W$ e $\alpha^*$ è l'unica soluzione dell'equazione $V'(\alpha)=0$.

> [!note] Dimostrazione
> Con $u''<0$ il termine $\tilde x^2u''(w_0+\alpha\tilde x)$ è negativo nei casi in cui $\tilde x\neq0$, che hanno probabilità positiva, e nullo altrove. Ne segue che $V''(\alpha)<0$ per ogni $\alpha$ e $V$ è strettamente concava. Essendo continua sull'intervallo chiuso $[0,W]$, ha un massimo, unico per la stretta concavità. Le tre alternative sono le condizioni di bordo e il caso interno richiamati sopra, con $[a,b]=[0,W]$.

Un massimo interno richiede che $\tilde x$ assuma valori di segno diverso. Se $\tilde x>0$ in ogni stato, il titolo rischioso rende sempre più di quello privo di rischio, $V'(\alpha)>0$ per ogni $\alpha$ e l'agente investe tutto, $\alpha^*=W$. Se $\tilde x<0$ in ogni stato accade l'opposto e $\alpha^*=0$. D'ora in poi $\alpha^*$ indica la soluzione del problema.

## Quando investire nel titolo rischioso

La prima domanda è se l'agente investa qualcosa nel titolo rischioso. La risposta dipende solo dal segno del rendimento in eccesso atteso.

> [!tip] Teorema
> Siano $u'>0$, $u''<0$ e $\mathbb P(\tilde x\neq0)>0$. L'investimento nel titolo rischioso è positivo se e solo se il suo rendimento atteso supera quello del titolo privo di rischio:
>
> $$\alpha^*>0\iff E[\tilde x]>0\iff E[\tilde x_0]>r.$$

> [!note] Dimostrazione
> Si valuta la derivata di $V$ in $\alpha=0$. Poiché $w_0+0\cdot\tilde x=w_0$ è certo, $u'(w_0)$ esce dall'attesa:
>
> $$V'(0)=E\big[\tilde x\,u'(w_0)\big]=u'(w_0)\,E[\tilde x].$$
>
> Dato che $u'(w_0)>0$, il segno di $V'(0)$ è quello di $E[\tilde x]$. Se $E[\tilde x]>0$, allora $V'(0)>0$ e $\alpha=0$ non è un massimo: $V$ cresce subito a destra di 0, e il massimo si trova in un punto $\alpha^*>0$. Se $E[\tilde x]\le0$, allora $V'(0)\le0$; poiché $V'$ è non crescente, $V'(\alpha)\le V'(0)\le0$ per ogni $\alpha\ge0$, $V$ è non crescente su $[0,W]$ e il massimo è in $\alpha^*=0$.

Con $E[\tilde x]=0$ l'agente non investe nulla nel titolo rischioso, neppure una piccola somma. Con $E[\tilde x]<0$ resta $\alpha^*=0$ per effetto del vincolo; senza vincolo ammetterebbe una posizione corta, cioè un $\alpha^*$ negativo. Il risultato richiede la derivabilità di $u$ in $w_0$: con un punto angoloso in $w_0$ può accadere $\alpha^*=0$ anche con $E[\tilde x]>0$.

L'intuizione sta nell'ordine di grandezza. Per un piccolo ammontare $\varepsilon$ investito nel titolo rischioso il guadagno atteso è $\varepsilon E[\tilde x]$, proporzionale a $\varepsilon$. Il costo del rischio, misurato dal premio per il rischio, è invece, per $\varepsilon$ piccolo, approssimativamente proporzionale a $\varepsilon^2$, come mostra l'approssimazione del premio per rischi piccoli in [[ERA 03 Avversione al Rischio|avversione al rischio]]. Per $\varepsilon$ abbastanza piccolo il guadagno prevale se il rendimento atteso è positivo, anche di poco. D'ora in poi si assume $E[\tilde x]>0$.

> [!example] Esempio
> Sia $u=\ln$, $r=0$, $W=w_0=100$, e sia $\tilde x=-50\%$ oppure $+100\%$ con probabilità $\tfrac12$ ciascuna. Il rendimento atteso è $E[\tilde x]=25\%>0$, quindi $\alpha^*>0$. Con $u'(w)=1/w$ la FOC è
>
> $$\frac12\cdot\frac{-0{,}5}{100-0{,}5\,\alpha}+\frac12\cdot\frac{1}{100+\alpha}=0\ \Longrightarrow\ 100-0{,}5\,\alpha=0{,}5\,(100+\alpha)\ \Longrightarrow\ \alpha^*=50.$$
>
> L'agente investe metà della ricchezza nel titolo rischioso. Se invece $\tilde x=-50\%$ oppure $+50\%$, il rendimento atteso è nullo, $V'(0)=u'(100)\cdot0=0$ e $\alpha^*=0$.

## Avversione al rischio e investimento

Si confrontano due agenti con la stessa ricchezza $w_0$ e lo stesso rendimento in eccesso $\tilde x$, con $E[\tilde x]>0$, e funzioni di utilità $u_1$ e $u_2$. L'agente 2 è più avverso al rischio dell'agente 1 se $u_2=\phi\circ u_1$ per una funzione concava $\phi$, come in [[ERA 03 Avversione al Rischio|avversione al rischio]]. La funzione $\phi$ è anche crescente: da $u_2'=\phi'(u_1)\,u_1'$ e dalla positività di $u_1'$ e $u_2'$ segue $\phi'>0$.

> [!tip] Teorema
> Siano $u_1$ e $u_2=\phi\circ u_1$ due utilità crescenti, con $u_1''<0$, e $\phi$ due volte derivabile e strettamente concava. Siano $\alpha_1^*$ e $\alpha_2^*$ gli investimenti ottimi dei due agenti. Se $\alpha_2^*<W$, allora
>
> $$\alpha_2^*<\alpha_1^*.$$
>
> Se $\phi$ è soltanto concava, vale $\alpha_2^*\le\alpha_1^*$, anche senza l'ipotesi $\alpha_2^*<W$.

> [!note] Dimostrazione
> Siano $V_1(\alpha)=E[u_1(w_0+\alpha\tilde x)]$ e $V_2(\alpha)=E[u_2(w_0+\alpha\tilde x)]$. Poiché $\phi'>0$, $\phi''\le0$ e $u_1''<0$, si ha $u_2''=\phi''(u_1)(u_1')^2+\phi'(u_1)u_1''<0$. Con $E[\tilde x]>0$, il teorema sul quando investire applicato a $u_2$ dà $\alpha_2^*>0$, e per ipotesi $\alpha_2^*<W$: la soluzione è interna e $V_2'(\alpha_2^*)=0$.
>
> *Riduzione.* La funzione $V_1$ è concava. Se $V_1'(\alpha_2^*)>0$, allora $V_1$ cresce a destra di $\alpha_2^*$ e, per concavità, $V_1(\beta)<V_1(\alpha_2^*)$ per ogni $\beta<\alpha_2^*$. Il massimo di $V_1$ sta quindi a destra di $\alpha_2^*$, cioè $\alpha_2^*<\alpha_1^*$. Basta dunque provare
>
> $$V_1'(\alpha_2^*)=E\big[\tilde x\,u_1'(w_0+\alpha_2^*\tilde x)\big]>0.$$
>
> *FOC del secondo agente.* Per la regola della funzione composta $u_2'=\phi'(u_1)\,u_1'$, e quindi
>
> $$0=E\big[\tilde x\,u_2'(w_0+\alpha_2^*\tilde x)\big]=E\big[\tilde x\,\phi'\big(u_1(w_0+\alpha_2^*\tilde x)\big)\,u_1'(w_0+\alpha_2^*\tilde x)\big].$$
>
> *Segno.* Poiché $\phi$ è concava, $\phi'$ è decrescente, strettamente se $\phi$ è strettamente concava. Sia $x\neq0$ una realizzazione di $\tilde x$. Se $x>0$, allora $w_0+\alpha_2^*x>w_0$ perché $\alpha_2^*>0$, quindi $u_1(w_0+\alpha_2^*x)>u_1(w_0)$ e $\phi'(u_1(w_0+\alpha_2^*x))<\phi'(u_1(w_0))$. Se $x<0$ valgono le disuguaglianze opposte. In entrambi i casi la differenza $\phi'(u_1(w_0+\alpha_2^*x))-\phi'(u_1(w_0))$ ha segno opposto a $x$, cioè
>
> $$x\,\phi'\big(u_1(w_0+\alpha_2^*x)\big)<x\,\phi'\big(u_1(w_0)\big),$$
>
> mentre per $x=0$ vale l'uguaglianza.
>
> *Conclusione.* Si moltiplica la disuguaglianza per $u_1'(w_0+\alpha_2^*x)>0$ e si prende l'attesa. L'attesa del primo membro è la FOC del secondo agente; poiché $\tilde x\neq0$ con probabilità positiva, la disuguaglianza resta stretta:
>
> $$0=E\big[\tilde x\,\phi'\big(u_1(w_0+\alpha_2^*\tilde x)\big)\,u_1'(w_0+\alpha_2^*\tilde x)\big]<\phi'\big(u_1(w_0)\big)\,E\big[\tilde x\,u_1'(w_0+\alpha_2^*\tilde x)\big].$$
>
> Dividendo per $\phi'(u_1(w_0))>0$ si ottiene $V_1'(\alpha_2^*)>0$, che è la tesi. Se $\phi$ è solo concava, la disuguaglianza è larga, $V_1'(\alpha_2^*)\ge0$ e il massimo di $V_1$ non sta a sinistra di $\alpha_2^*$: $\alpha_2^*\le\alpha_1^*$. Se $\alpha_2^*=W$, la disuguaglianza puntuale vale ancora con $W$ al posto di $\alpha_2^*$, perché non usa la FOC ma solo la positività di $\alpha_2^*$, e $W>0$; moltiplicando per $u_1'>0$ e prendendo l'attesa, $0\le V_2'(W)\le\phi'(u_1(w_0))\,V_1'(W)$, quindi $V_1'(W)\ge0$ e $\alpha_1^*=W$.

Nella FOC del secondo agente il fattore $\phi'(u_1(\cdot))$ è più grande negli stati con ricchezza bassa, quelli con $x<0$, e più piccolo negli stati con ricchezza alta, perché $\phi'$ è decrescente: le perdite pesano più dei guadagni. Perché l'attesa pesata si annulli, l'attesa senza questo fattore deve essere positiva, e il primo agente, a $\alpha_2^*$, ha ancora convenienza a investire di più. Senza stretta concavità l'uguaglianza è possibile: con $\phi$ affine, $u_2=c\,u_1+d$ con $c>0$, i due agenti hanno la stessa FOC e lo stesso investimento.

> [!example] Esempio
> Nell'esempio precedente l'agente con $u_1=\ln$ investe $\alpha_1^*=50$. Sia $u_2(w)=-1/w$, la CRRA con $\gamma=2$. Si ha $u_2=\phi(\ln w)$ con $\phi(t)=-e^{-t}$, concava e crescente, quindi l'agente 2 è più avverso al rischio; infatti $A_2(w)=2/w>A_1(w)=1/w$. Con $u_2'(w)=w^{-2}$ la FOC diventa
>
> $$\frac{-0{,}5}{(100-0{,}5\,\alpha)^2}+\frac{1}{(100+\alpha)^2}=0\ \Longrightarrow\ (100-0{,}5\,\alpha)^2=\tfrac12\,(100+\alpha)^2,$$
>
> e prendendo la radice positiva si trova $\alpha_2^*=300\sqrt2-400\approx24{,}26$. L'agente più avverso investe meno della metà di quanto investe l'agente con il logaritmo.

## Tassazione e sussidi dei rendimenti

Una politica fiscale modifica il rendimento in eccesso, e il modello ne prevede l'effetto sull'investimento.

> [!example] Esempio
> Il governo tassa i guadagni di capitale con aliquota $\tau\in(0,1)$ e sussidia le perdite di capitale con la stessa aliquota. Quale effetto ha la politica sull'investimento nel titolo rischioso? (1) Lo fa aumentare. (2) Lo fa diminuire. (3) L'effetto dipende dai casi.
>
> *Risposta: (1).* Si assume che l'imposta colpisca il rendimento in eccesso, e che la parte investita nel titolo privo di rischio resti fuori, per cui $w_0$ non cambia. Una posizione $\alpha$ rende allora $(1-\tau)\,\alpha\tilde x$ al posto di $\alpha\tilde x$, e il nuovo problema è $\max_\alpha E[u(w_0+\alpha(1-\tau)\tilde x)]=\max_\alpha V(\alpha(1-\tau))$. La FOC è
>
> $$(1-\tau)\,E\big[\tilde x\,u'\big(w_0+\alpha(1-\tau)\tilde x\big)\big]=0,$$
>
> che è la FOC originaria con $\alpha(1-\tau)$ al posto di $\alpha$. È risolta da $\alpha(1-\tau)=\alpha^*$, cioè
>
> $$\alpha^*_{\text{dopo}}=\frac{\alpha^*}{1-\tau}>\alpha^*.$$
>
> Lo Stato assorbe una quota $\tau$ dei guadagni e delle perdite, per cui, a parità di esposizione dopo le imposte, l'agente può esporsi di più. Con il vincolo $\alpha\le W$ il nuovo investimento è $\min\{\alpha^*/(1-\tau),W\}$.

Nel caso limite $\tau=1$ il rendimento in eccesso dopo le imposte è nullo in ogni stato, $V$ è costante e l'investimento è indeterminato. Per $\tau\to1$ il valore $\alpha^*/(1-\tau)$ tende all'infinito, e con il vincolo l'investimento è $W$ per ogni $\tau\ge1-\alpha^*/W$. La risposta (1) dipende dall'ipotesi sulla base imponibile: se fosse tassato anche l'interesse del titolo privo di rischio, $w_0$ diminuirebbe e, con preferenze DARA, l'effetto ricchezza della sezione seguente andrebbe in senso opposto, con un esito che dipende dai casi.

## Ricchezza iniziale e investimento

Un agente la cui avversione assoluta al rischio diminuisce al crescere della ricchezza è disposto a esporsi di più quando è più ricco: con avversione assoluta strettamente decrescente l'investimento nel titolo rischioso cresce con la ricchezza, con avversione assoluta costante non cambia. L'avversione assoluta al rischio decrescente (DARA, *decreasing absolute risk aversion*) è definita in [[ERA 03 Avversione al Rischio|avversione al rischio]] in senso debole, $A'(w)\le0$, con la CARA come caso di bordo. Qui conta anche la versione stretta, $A'(w)<0$ per ogni $w$. La derivata si calcola rispetto a $w_0=W(1+r)$; poiché $1+r>0$, la derivata rispetto a $w_0$ e quella rispetto a $W$ hanno lo stesso segno.

> [!tip] Teorema
> Siano $u'>0$, $u''<0$ ed $E[\tilde x]>0$, e sia $\alpha^*(w_0)$ interno. Se $A'\le0$ (DARA), allora $\partial\alpha^*(w_0)/\partial w_0\ge0$. Se $A'<0$ (DARA stretta), allora $\partial\alpha^*(w_0)/\partial w_0>0$. Se $u$ è CARA, $\alpha^*$ non dipende da $w_0$.

> [!note] Dimostrazione
> *Derivata dell'ottimo.* L'investimento ottimo soddisfa, per ogni $w_0$, la FOC
>
> $$E\big[\tilde x\,u'\big(w_0+\alpha^*(w_0)\,\tilde x\big)\big]=0.$$
>
> La derivata di questa espressione rispetto ad $\alpha$ è $V''(\alpha^*)<0$, perciò per il teorema della funzione implicita $\alpha^*(w_0)$ è derivabile. Derivando la FOC rispetto a $w_0$, la derivata dell'argomento di $u'$ è $1+\tilde x\,\partial\alpha^*/\partial w_0$ e si ottiene
>
> $$E\big[\tilde x\,u''(w_0+\alpha^*\tilde x)\big]+E\Big[\tilde x^{2}\,u''(w_0+\alpha^*\tilde x)\,\frac{\partial\alpha^*(w_0)}{\partial w_0}\Big]=0.$$
>
> La derivata $\partial\alpha^*/\partial w_0$ non dipende dallo stato ed esce dall'attesa. Posto $D=-E[\tilde x^2u''(w_0+\alpha^*\tilde x)]$, che è positivo perché $u''<0$ e $\tilde x\neq0$ con probabilità positiva, si ricava
>
> $$\frac{\partial\alpha^*(w_0)}{\partial w_0}=-\frac{E\big[\tilde x\,\{-u''(w_0+\alpha^*\tilde x)\}\big]}{D}.$$
>
> Il segno della derivata è opposto a quello di $E[\tilde x\{-u''(w_0+\alpha^*\tilde x)\}]$: l'ottimo cresce con la ricchezza se e solo se questa attesa è negativa.
>
> *Uso del DARA.* Poiché $-u''=A\,u'$,
>
> $$E\big[\tilde x\{-u''(w_0+\alpha^*\tilde x)\}\big]=E\big[A(w_0+\alpha^*\tilde x)\,\tilde x\,u'(w_0+\alpha^*\tilde x)\big].$$
>
> Per il teorema sull'investimento positivo $\alpha^*>0$. Sia $x\neq0$ una realizzazione di $\tilde x$. Se $x>0$, allora $w_0+\alpha^*x>w_0$ e, con $A$ decrescente, $A(w_0+\alpha^*x)\le A(w_0)$. Se $x<0$, allora $w_0+\alpha^*x<w_0$ e $A(w_0+\alpha^*x)\ge A(w_0)$. In entrambi i casi il prodotto $x\,[A(w_0+\alpha^*x)-A(w_0)]$ è non positivo e, moltiplicando per $u'(w_0+\alpha^*x)>0$,
>
> $$A(w_0+\alpha^*x)\,x\,u'(w_0+\alpha^*x)\le A(w_0)\,x\,u'(w_0+\alpha^*x)\qquad\text{per ogni }x,$$
>
> con la disuguaglianza stretta per $x\neq0$ se $A$ è strettamente decrescente. Prendendo l'attesa e usando la FOC nell'ultimo passaggio:
>
> $$E\big[A(w_0+\alpha^*\tilde x)\,\tilde x\,u'(w_0+\alpha^*\tilde x)\big]\ \le\ A(w_0)\,E\big[\tilde x\,u'(w_0+\alpha^*\tilde x)\big]=0.$$
>
> L'attesa è dunque non positiva, e negativa se $A$ è strettamente decrescente, perché $\tilde x\neq0$ con probabilità positiva. Ne seguono $\partial\alpha^*/\partial w_0\ge0$ con DARA e $\partial\alpha^*/\partial w_0>0$ con DARA stretta. Se $u$ è CARA, $A$ è costante e vale l'uguaglianza: la derivata è nulla.

Per la CARA il risultato si vede anche direttamente: con $u'(w)=e^{-\lambda w}$ il fattore $e^{-\lambda w_0}$ si semplifica nella FOC e $\alpha^*$ non contiene $w_0$. L'ammontare investito non cambia con la ricchezza, a differenza della DARA stretta, per cui cresce.

> [!example] Esempio
> Un agente ha utilità $u(w)=w^{1-\gamma}/(1-\gamma)$ con $\gamma\in(0,1)$, per cui $u>0$. Come varia l'investimento nel titolo rischioso al crescere della ricchezza iniziale? (1) Aumenta. (2) Diminuisce. (3) Dipende dai casi.
>
> *Risposta: (1).* Per la CRRA $A(w)=\gamma/w$ e $A'(w)=-\gamma/w^2<0$: l'utilità è DARA in senso stretto, e il teorema dà $\partial\alpha^*/\partial w_0>0$. Si può dire di più. Posto $\alpha=\kappa\,w_0$, la FOC diventa
>
> $$E\big[\tilde x\,(w_0+\kappa w_0\tilde x)^{-\gamma}\big]=w_0^{-\gamma}\,E\big[\tilde x\,(1+\kappa\tilde x)^{-\gamma}\big]=0,$$
>
> che determina $\kappa$ indipendentemente da $w_0$, con $\kappa>0$ se $E[\tilde x]>0$. Ne segue $\alpha^*(w_0)=\kappa\,w_0$: l'ammontare investito è proporzionale alla ricchezza e la quota investita è costante. Se $\kappa(1+r)\ge1$ il vincolo $\alpha\le W$ è attivo a ogni livello di ricchezza e l'ammontare è $W$, che cresce anch'esso con la ricchezza.

> [!example] Esempio
> Si riprende l'esempio con $r=0$ e $\tilde x=-50\%$ oppure $+100\%$, e si porta la ricchezza da $W=w_0=100$ a $W=w_0=200$. Con il logaritmo l'investimento passa da 50 a 100. Con la CRRA con $\gamma=2$ passa da $24{,}26$ a $48{,}53$, cioè raddoppia. Con la CARA con $\lambda=0{,}01$ la FOC diventa $-0{,}5\,e^{0{,}5\lambda\alpha}+e^{-\lambda\alpha}=0$, da cui $\alpha^*=\ln2/(1{,}5\,\lambda)\approx46{,}21$ per ogni valore di $w_0$, purché $W\ge46{,}21$.

## Rischiosità del titolo e investimento

Si può essere indotti a credere che la domanda di un titolo rischioso diminuisca quando il titolo diventa più rischioso. Questa convinzione non è corretta in generale. Un cambiamento di rischio può migliorare l'utilità attesa di ogni agente avverso al rischio e tuttavia indurre alcuni di essi a ridurre la domanda del titolo, come hanno mostrato Rothschild e Stiglitz. La dominanza del secondo ordine ordina le distribuzioni secondo l'utilità attesa; la domanda dipende invece dalla derivata dell'utilità attesa rispetto ad $\alpha$, e questa è l'attesa di una funzione diversa.

### Che cosa si vuole dimostrare

Siano $F_1$ e $F_2$ le distribuzioni del rendimento in eccesso di due titoli, con $F_2$ che domina $F_1$ al secondo ordine: il titolo con distribuzione $F_1$ è più rischioso. Sia $V_i(\alpha)=E_{F_i}[u(w_0+\alpha\tilde x)]$ la funzione obiettivo sotto $F_i$; in questa sezione l'indice indica la distribuzione e non l'agente. Sia $\alpha_1^*\in(0,W)$ l'investimento ottimo sotto $F_1$, che soddisfa la FOC con l'attesa calcolata sotto $F_1$. Se la derivata di $V$ sotto $F_2$, calcolata in $\alpha_1^*$, è non negativa, allora il massimo $\alpha_2^*$ di $V_2$ non sta a sinistra di $\alpha_1^*$: la domanda non diminuisce quando il titolo diventa meno rischioso. L'obiettivo è quindi mostrare che

$$E_{F_1}\big[\tilde x\,u'(w_0+\alpha_1^*\tilde x)\big]=0\ \Longrightarrow\ E_{F_2}\big[\tilde x\,u'(w_0+\alpha_1^*\tilde x)\big]\ge0.$$

Con la barra al posto del pedice, come nel materiale del corso, la stessa implicazione si scrive $E[\tilde x\,u'(w_0+\alpha_1^*\tilde x)\mid F_1]=0\Rightarrow E[\tilde x\,u'(w_0+\alpha_1^*\tilde x)\mid F_2]\ge0$.

Si pone $g(x)=x\,u'(w_0+\alpha_1^*x)$. L'ipotesi è $E_{F_1}[g(\tilde x)]=0$ e la tesi $E_{F_2}[g(\tilde x)]\ge0$. Se $g$ fosse crescente e concava, per il teorema sulla dominanza si avrebbe $E_{F_2}[g(\tilde x)]\ge E_{F_1}[g(\tilde x)]=0$. Ma $g$ non è in generale né crescente né concava, e senza queste proprietà la dominanza non permette di concludere. Le domande da porsi sono due: in quali casi $g$ è crescente, e in quali è crescente e concava.

Per studiare $g$ conviene eliminare $\alpha_1^*$. Posto $h(y)=y\,u'(w_0+y)$ e $\alpha_1^*>0$, vale $g(x)=h(\alpha_1^*x)/\alpha_1^*$, da cui $g'(x)=h'(\alpha_1^*x)$ e $g''(x)=\alpha_1^*\,h''(\alpha_1^*x)$. La funzione $g$ è crescente e concava se e solo se lo è $h$, e si studia $h$, per i valori di $y$ per cui $w_0+y$ è una ricchezza ammissibile.

### Quando la funzione è crescente

> [!note] Dimostrazione
> La derivata di $h$ è
>
> $$h'(y)=u'(w_0+y)+y\,u''(w_0+y).$$
>
> Da $u''=-A\,u'$ e da $y=(w_0+y)-w_0$ si ha $y\,A(w_0+y)=RR(w_0+y)-w_0A(w_0+y)$, quindi
>
> $$h'(y)=u'(w_0+y)\big[1-RR(w_0+y)+w_0A(w_0+y)\big].$$

La funzione è non decrescente se questa derivata è non negativa e strettamente crescente se è positiva. Poiché $u'>0$, $w_0>0$ e $A\ge0$, il termine $w_0A$ non è negativo: la derivata è positiva se $RR(w_0+y)<1$. La condizione $RR<1$ è sufficiente e non necessaria: per il logaritmo $RR=1$, ma la parentesi vale $w_0A(w_0+y)>0$. Per la CRRA con $\gamma\in(0,1)$ si ha $RR=\gamma<1$ e $h$ è crescente.

### Quando la funzione è concava

> [!note] Dimostrazione
> La derivata seconda di $h$ è
>
> $$h''(y)=2u''(w_0+y)+y\,u'''(w_0+y).$$
>
> Da $u'''=-P\,u''$ e da $y=(w_0+y)-w_0$ si ha $y\,u'''=-y\,P\,u''=-[RP(w_0+y)-w_0P(w_0+y)]\,u''$, quindi
>
> $$h''(y)=u''(w_0+y)\big[2-RP(w_0+y)+w_0P(w_0+y)\big]=-u''(w_0+y)\big[RP(w_0+y)-2-w_0P(w_0+y)\big].$$

La funzione è concava se $h''\le0$. Poiché $-u''>0$, ciò accade se e solo se $2-RP(w_0+y)+w_0P(w_0+y)\ge0$. Con $w_0>0$ la condizione è soddisfatta se $RP<2$ e $P>0$: allora $2-RP>0$ e $w_0P>0$. Anche questa condizione non è necessaria. Per il logaritmo $RP=2$ e $P=2/w$ e la parentesi vale $w_0P>0$: la funzione è concava, e infatti $h(y)=y/(w_0+y)$ ha $h''(y)=-2w_0/(w_0+y)^3<0$.

### Il risultato

> [!tip] Teorema
> Siano $F_2$ che domina $F_1$ al secondo ordine e $\alpha_1^*\in(0,W)$ l'investimento ottimo sotto $F_1$. Se per ogni livello ammissibile di ricchezza finale $w$ valgono $RR(w)<1$, $P(w)>0$ e $RP(w)<2$, allora l'investimento ottimo sotto $F_2$ è almeno $\alpha_1^*$: $\alpha_2^*\ge\alpha_1^*$. In altri termini la domanda del titolo non cresce quando il titolo diventa più rischioso.

> [!note] Dimostrazione
> Sia $g(x)=x\,u'(w_0+\alpha_1^*x)$. Per quanto visto sopra, $RR<1$ rende $h$ crescente e $RP<2$ con $P>0$ la rende concava, quindi $g$ è crescente e concava. Poiché $F_2$ domina $F_1$ al secondo ordine, il teorema sulla dominanza dà
>
> $$E_{F_2}[g(\tilde x)]\ \ge\ E_{F_1}[g(\tilde x)]=0,$$
>
> dove l'ultima uguaglianza è la FOC sotto $F_1$. Il primo membro è la derivata della funzione obiettivo sotto $F_2$ in $\alpha_1^*$: $V_2'(\alpha_1^*)\ge0$. La funzione $V_2$ è concava, per cui per ogni $\beta<\alpha_1^*$ si ha $V_2(\beta)\le V_2(\alpha_1^*)+V_2'(\alpha_1^*)(\beta-\alpha_1^*)\le V_2(\alpha_1^*)$. Il massimo non sta a sinistra di $\alpha_1^*$: $\alpha_2^*\ge\alpha_1^*$.

Se vale soltanto $RR<1$, $g$ è crescente e il ragionamento si ripete con la FOSD al posto della SOSD: se $F_2$ domina $F_1$ al primo ordine, l'investimento ottimo sotto $F_2$ non è inferiore a quello sotto $F_1$.

> [!example] Esempio
> Quiz. Il rendimento $\tilde x$ del titolo rischioso, che qui si legge come rendimento in eccesso, è sempre positivo. Si viene a sapere che il rendimento non è $\tilde x$ ma una variabile che vale $\tilde x$ con probabilità $q\in(0,1)$ e $0$ con probabilità $1-q$. Come cambia l'investimento nel titolo rischioso? (i) Aumenta. (ii) Diminuisce. (iii) Dipende. (iv) Nessuna delle tre.
>
> *Risposta: (iv), l'investimento non cambia.* Siano $V_1$ la funzione obiettivo con $\tilde x$ e $V_2$ quella con la nuova variabile: qui la distribuzione con indice 2 è quella peggiore. La derivata di $V_2$ è
>
> $$V_2'(\alpha)=q\,E\big[\tilde x\,u'(w_0+\alpha\tilde x)\big]+(1-q)\cdot0\cdot u'(w_0)=q\,V_1'(\alpha),$$
>
> che in ogni $\alpha$ ha lo stesso segno di $V_1'(\alpha)$, per ogni $q>0$. Le condizioni di bordo e il caso interno dipendono solo da questo segno, quindi $V_1$ e $V_2$ hanno lo stesso punto di massimo su $[0,W]$: $\alpha_2^*=\alpha_1^*$. La positività di $\tilde x$ serve a ordinare le due distribuzioni. Con $F_1$ la c.d.f. di $\tilde x$, che vale $0$ per $x\le0$, la nuova c.d.f. vale $0$ per $x<0$ e $(1-q)+qF_1(x)$ per $x\ge0$, e $(1-q)+qF_1(x)\ge F_1(x)$ equivale a $(1-q)[1-F_1(x)]\ge0$. Ne segue che $F_1$ domina la nuova distribuzione al primo ordine: la nuova distribuzione è peggiore nel senso FOSD, eppure l'investimento non diminuisce.

Sotto la premessa del quiz non esiste un massimo interno: $V_1'(\alpha)>0$ e $V_2'(\alpha)=qV_1'(\alpha)>0$ per ogni $\alpha$, e in entrambi i casi l'ottimo è $\alpha=W$. Se invece il rendimento che si annulla fosse quello netto $\tilde x_0$ del titolo rischioso, con $r>0$, il rendimento in eccesso sarebbe $-r$ con probabilità $1-q$; la derivata diventerebbe $V_2'(\alpha)=q\,V_1'(\alpha)-(1-q)\,r\,u'(w_0-\alpha r)$, che in un $\alpha_1^*$ interno vale $-(1-q)\,r\,u'(w_0-\alpha_1^*r)<0$, e l'investimento diminuirebbe.

> [!example] Esempio
> Quiz. Due titoli rischiosi hanno rendimenti netti $X_1$ e $X_2$, con $F_2$ che domina $F_1$ al secondo ordine. Quale portafoglio preferisce un agente avverso al rischio? (i) Quello composto dal titolo $X_1$ e dal titolo privo di rischio. (ii) Quello composto dal titolo $X_2$ e dal titolo privo di rischio.
>
> *Risposta: (ii).* Per ogni $\alpha\in[0,W]$ la funzione $x\mapsto u\big(w_0+\alpha(x-r)\big)$ è crescente e concava in $x$, perché $u$ è crescente e concava e $\alpha\ge0$. Per il teorema sulla dominanza, $E_{F_2}[u(w_0+\alpha(X-r))]\ge E_{F_1}[u(w_0+\alpha(X-r))]$ per ogni $\alpha$, e quindi anche per il massimo rispetto ad $\alpha$: l'utilità attesa del portafoglio ottimo con $X_2$ non è inferiore a quella con $X_1$. Il vincolo $\alpha\ge0$ è necessario: con vendite allo scoperto la funzione sarebbe decrescente in $x$ e l'argomento cadrebbe.

La preferenza fra i due portafogli ottimi non dipende da quanto l'agente investe in ciascun titolo. L'ammontare ottimo obbedisce a un criterio diverso: la dominanza da sola non basta a ordinarlo, e servono le condizioni su $RR$, $P$ e $RP$.

## Condizioni per un investimento minore

Un agente investe di meno in un titolo rischioso in tre casi, ciascuno corrispondente a una delle tre sezioni di statica comparativa. In ogni caso il capitolo dimostra che l'investimento non aumenta; nei primi due casi, con le ipotesi strette indicate, diminuisce.

1. L'agente diventa più avverso al rischio: $u_2=\phi\circ u_1$ con $\phi$ concava dà $\alpha_2^*\le\alpha_1^*$, e con $\phi$ strettamente concava e soluzione interna $\alpha_2^*<\alpha_1^*$.
2. Le sue preferenze sono DARA in senso stretto ($A'<0$) e l'agente diventa più povero: con soluzione interna $\partial\alpha^*/\partial w_0>0$, per cui una riduzione di $w_0$ riduce l'investimento. Con la sola DARA debole l'investimento non aumenta, e con la CARA, finché la soluzione resta interna, non cambia.
3. Il titolo diventa più rischioso, nel senso che la sua distribuzione è dominata al secondo ordine, e le preferenze soddisfano $RR<1$, $P>0$ e $RP<2$ per tutti i valori ammissibili della ricchezza finale.

Le condizioni del terzo caso garantiscono la conclusione senza essere necessarie. La condizione $RR<1$ è restrittiva: le utilità CRRA la soddisfano solo per $\gamma<1$. Il logaritmo, con $RR=1$ e $RP=2$, non soddisfa le condizioni, ma per lui $h$ è crescente e concava e la conclusione vale ugualmente. Per le CRRA le tre condizioni equivalgono a $\gamma<1$, perché $RR=\gamma$, $RP=1+\gamma$ e $P=(1+\gamma)/w>0$.
