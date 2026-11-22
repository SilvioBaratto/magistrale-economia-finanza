---
title: "Avversione al rischio: concavità, misure di Arrow-Pratt, equivalente certo ed effetto ricchezza"
tags:
  - corso/economia-rischio-assicurazioni
  - tipo/lezione
corso: "[[Economia del Rischio e delle Assicurazioni]]"
source: "ERA_Slide_02_Avversione-al-Rischio.pdf"
text_layer: true
verified: true
generated: 2026-11-22
---

## Oggetto del capitolo

Il capitolo costruisce gli strumenti con cui si misura e si confronta l'avversione al rischio di un agente che sceglie secondo l'utilità attesa. Si colloca dopo la [[ERA 02 Teoria dell'Utilità Attesa|teoria dell'utilità attesa]], da cui riprende la funzione di utilità $u$ (di Bernoulli) dell'agente, e prima del [[ERA 04 Confronto di Opzioni Rischiose|confronto di opzioni rischiose]].

Il modo in cui un evento rischioso incide sul benessere di un agente dipende dalle sue preferenze, dalla sua ricchezza e da altri fattori, come l'inquadramento del problema (*framing*) e i rischi già assunti. Il capitolo considera le preferenze e la ricchezza. Ha due scopi: costruire misure di avversione al rischio e usarle per la statica comparativa, cioè per confrontare agenti con preferenze diverse e lo stesso agente a livelli diversi di ricchezza.

La disuguaglianza di Jensen lega l'avversione al rischio alla concavità di $u$. Su questa base si definiscono tre misure del grado di avversione (la trasformazione concava, le misure di Arrow-Pratt, l'equivalente certo con il premio per il rischio) e si dimostra che portano allo stesso confronto tra due agenti. L'ultima parte studia come il premio per il rischio varia con la ricchezza e classifica le funzioni di utilità di uso corrente.


## Notazione e ipotesi

Una convenzione di notazione vale per tutto il capitolo. $W$ indica la ricchezza come argomento di $u$, mentre $w$ è la ricchezza iniziale certa dell'agente. Una lotteria è una variabile casuale $X$ che si somma a $w$, per cui la ricchezza finale è $w+X$. Le lotterie hanno valore atteso nullo, $E[X]=0$, salvo diversa indicazione. La funzione $u$ è crescente, $u'>0$, perché l'agente preferisce più ricchezza a meno; dove si usano le derivate successive la si assume derivabile il numero di volte necessario.

## Tre funzioni di utilità di riferimento

Tre funzioni di utilità ritornano nel capitolo come esempi. Le misure di avversione al rischio sono rapporti tra derivate di $u$, perciò per ciascuna funzione si calcolano subito le prime tre derivate.

La prima è $u(W)=-e^{-\lambda W}/\lambda$, con $\lambda>0$. La seconda è $u(W)=W^{1-\gamma}/(1-\gamma)$, con $W>0$, $\gamma>0$ e $\gamma\neq1$. La terza è $u(W)=\ln W$, con $W>0$.

| $u(W)$ | $u'(W)$ | $u''(W)$ | $u'''(W)$ |
|---|---|---|---|
| $-e^{-\lambda W}/\lambda$ | $e^{-\lambda W}$ | $-\lambda e^{-\lambda W}$ | $\lambda^2 e^{-\lambda W}$ |
| $W^{1-\gamma}/(1-\gamma)$ | $W^{-\gamma}$ | $-\gamma W^{-\gamma-1}$ | $\gamma(\gamma+1)W^{-\gamma-2}$ |
| $\ln W$ | $1/W$ | $-1/W^2$ | $2/W^3$ |

Per $\gamma\in(0,1)$ la seconda funzione è positiva, crescente e concava. Le derivate della tabella valgono per ogni $\gamma>0$ con $\gamma\neq1$: se $\gamma>1$ la funzione è negativa, ma resta crescente e concava. Il logaritmo è il caso $\gamma=1$, perché è il limite per $\gamma\to1$ della funzione $(W^{1-\gamma}-1)/(1-\gamma)$, la quale ha le stesse derivate di $W^{1-\gamma}/(1-\gamma)$ dato che ne differisce per una costante. In tutti e tre i casi $u'>0$ e $u''<0$: l'utilità cresce con la ricchezza, e cresce con incrementi sempre minori.

## La disuguaglianza di Jensen

Una funzione $f$ definita su un intervallo $I$ è concava quando il suo grafico sta sopra ogni corda. La disuguaglianza di Jensen estende questa proprietà dalla media di due valori alla media rispetto a una distribuzione qualsiasi, e la caratterizza.

> [!abstract] Definizione
> Una funzione $f:I\to\mathbb{R}$ è **concava** se per ogni $x_1,x_2\in I$ e ogni $\pi\in[0,1]$
>
> $$f\big(\pi x_1+(1-\pi)x_2\big)\ \ge\ \pi f(x_1)+(1-\pi)f(x_2).$$

> [!tip] Teorema
> (Disuguaglianza di Jensen.) Una funzione $f$ è concava se e solo se, per ogni variabile casuale $X$ a valori in $I$ e con valore atteso finito,
>
> $$E[f(X)]\ \le\ f(E[X]).$$

Il valore atteso della funzione non supera la funzione del valore atteso. La lettura geometrica si vede con una variabile a due valori: $E[f(X)]$ è l'ordinata, sopra l'ascissa $E[X]$, del punto della corda che unisce $(x_1,f(x_1))$ e $(x_2,f(x_2))$, mentre $f(E[X])$ è l'ordinata del punto della curva sopra la stessa ascissa. Per $f$ concava la corda sta sotto la curva. Il teorema vale per ogni distribuzione e il capitolo lo usa più volte, per legare l'avversione al rischio alla concavità di $u$ e per confrontare i premi di due agenti. Per le variabili con un numero finito di valori si passa dalla proprietà per due punti al caso generale per induzione sul numero dei valori; la dimostrazione che segue copre questo caso.

> [!note] Dimostrazione
> *Se.* Si supponga che la disuguaglianza valga per ogni $X$. Dati $x_1,x_2\in I$ e $\pi\in[0,1]$, sia $X$ la variabile che vale $x_1$ con probabilità $\pi$ e $x_2$ con probabilità $1-\pi$. Allora $E[f(X)]=\pi f(x_1)+(1-\pi)f(x_2)$ e $E[X]=\pi x_1+(1-\pi)x_2$, per cui la disuguaglianza di Jensen coincide con la definizione di concavità.
>
> *Solo se.* Sia $f$ concava. La dimostrazione tratta una variabile casuale $X$ con un numero finito di valori $x_1,\dots,x_n\in I$, con probabilità $\pi_1,\dots,\pi_n$ tutte positive (i valori di probabilità nulla non contribuiscono alle medie) e di somma 1. Per $n=2$ la tesi è la definizione di concavità.
>
> Il caso $n=3$ mostra il meccanismo. Si ponga $\pi_3=1-\pi_1-\pi_2>0$ e $y=\dfrac{\pi_1x_1+\pi_2x_2}{\pi_1+\pi_2}$. Poiché $\pi_1+\pi_2>0$, i primi due termini si possono scrivere come $\pi_1+\pi_2$ per una media con pesi normalizzati:
>
> $$E[f(X)]=(\pi_1+\pi_2)\Big[\tfrac{\pi_1}{\pi_1+\pi_2}f(x_1)+\tfrac{\pi_2}{\pi_1+\pi_2}f(x_2)\Big]+\pi_3f(x_3)$$
>
> $$\le(\pi_1+\pi_2)\,f(y)+\pi_3f(x_3)\ \le\ f\big((\pi_1+\pi_2)\,y+\pi_3x_3\big)=f(E[X]).$$
>
> La prima disuguaglianza è la concavità sul caso a due valori, con i pesi normalizzati $\pi_1/(\pi_1+\pi_2)$ e $\pi_2/(\pi_1+\pi_2)$, che sommano a 1. La seconda è la concavità applicata ai due punti $y$ e $x_3$, con pesi $\pi_1+\pi_2$ e $\pi_3$; il punto $y$ è una combinazione convessa di $x_1$ e $x_2$, quindi sta in $I$. L'ultima uguaglianza segue da $(\pi_1+\pi_2)\,y+\pi_3x_3=\pi_1x_1+\pi_2x_2+\pi_3x_3=E[X]$.
>
> Per $n$ valori si raggruppano i primi $n-1$ nello stesso modo. Si ponga $s=\pi_1+\dots+\pi_{n-1}=1-\pi_n>0$ e $y=\sum_{i<n}(\pi_i/s)\,x_i$. L'ipotesi induttiva, cioè la disuguaglianza di Jensen per $n-1$ valori, applicata ai pesi normalizzati $\pi_i/s$ dà $\sum_{i<n}(\pi_i/s)\,f(x_i)\le f(y)$. Quindi
>
> $$E[f(X)]=s\sum_{i<n}\frac{\pi_i}{s}f(x_i)+\pi_nf(x_n)\ \le\ s\,f(y)+\pi_nf(x_n)\ \le\ f\big(s\,y+\pi_nx_n\big)=f(E[X]),$$
>
> dove la seconda disuguaglianza è la concavità sui due punti $y$ e $x_n$, con pesi $s$ e $\pi_n$.

> [!example] Esempio
> Sia $f=\ln$, concava perché $f''(x)=-1/x^2<0$, e sia $X$ la variabile che vale 4 o 16 con probabilità $1/2$ ciascuno. Si ha $E[X]=10$ e
>
> $$E[\ln X]=\tfrac12\ln4+\tfrac12\ln16=\ln2+\ln4=\ln8\ \le\ \ln10=\ln E[X].$$
>
> La stessa coppia di valori compare, come ricchezza finale $10\pm6$, nell'esempio sull'equivalente certo.

## Avversione al rischio e concavità

> [!abstract] Definizione
> Un agente con funzione di utilità $u$ (di Bernoulli) è **avverso al rischio** se è avverso a ogni lotteria a valore atteso nullo, a qualsiasi livello di ricchezza: per ogni $w$ e per ogni $X$ con $E[X]=0$,
>
> $$E[u(w+X)]\ \le\ u(w).$$

La ricchezza aleatoria $w+X$ ha lo stesso valore atteso della ricchezza certa $w$, per cui la definizione confronta due ricchezze con lo stesso valore atteso, una certa e una aleatoria. L'agente avverso al rischio non ottiene dalla ricchezza aleatoria un'utilità attesa maggiore di quella della ricchezza certa $w$.

> [!tip] Teorema
> Un agente è avverso al rischio se e solo se la sua funzione di utilità $u$ è concava.

> [!note] Dimostrazione
> *Se.* Sia $u$ concava, e siano $w$ una ricchezza e $X$ una lotteria con $E[X]=0$. Si pone $Y=w+X$, per cui $E[Y]=w$. La disuguaglianza di Jensen, applicata a $u$ e alla variabile $Y$, dà
>
> $$E[u(w+X)]=E[u(Y)]\ \le\ u(E[Y])=u(w).$$
>
> *Solo se.* Si supponga che $E[u(w+X)]\le u(w)$ per ogni $w$ e per ogni $X$ con $E[X]=0$. Dati due punti $x_1,x_2$ e $\pi\in(0,1)$, si pone $w=\pi x_1+(1-\pi)x_2$ e si sceglie la lotteria $X$ che vale $x_1-w$ con probabilità $\pi$ e $x_2-w$ con probabilità $1-\pi$. Si ha $E[X]=\pi x_1+(1-\pi)x_2-w=0$, e $w+X$ vale $x_1$ con probabilità $\pi$ e $x_2$ con probabilità $1-\pi$. L'ipotesi diventa
>
> $$\pi u(x_1)+(1-\pi)u(x_2)\ \le\ u\big(\pi x_1+(1-\pi)x_2\big),$$
>
> che è la definizione di concavità di $u$ (per $\pi\in\{0,1\}$ è un'uguaglianza).

Il teorema traduce un'attitudine verso le lotterie in una proprietà della forma di $u$. Dice se l'agente è avverso al rischio, non quanto lo sia. Per confrontare il grado di avversione di due agenti servono misure quantitative, e il capitolo ne sviluppa tre.

## Tre misure di avversione al rischio

Le tre misure sono la trasformazione concava, le misure di Arrow-Pratt e la coppia formata dall'equivalente certo e dal premio per il rischio. Le prime due si introducono qui, la terza nella sezione successiva; il teorema di equivalenza mostra che ordinano gli agenti allo stesso modo.

### La trasformazione concava

> [!abstract] Definizione
> L'agente 2, con utilità $u_2$, è **più avverso al rischio** dell'agente 1, con utilità $u_1$, se $u_2$ è «più concava» di $u_1$: esiste una funzione concava $\phi$ tale che
>
> $$u_2=\phi\circ u_1,\qquad\text{cioè}\qquad u_2(W)=\phi\big(u_1(W)\big).$$

Il confronto è debole: «più avverso» va letto come «almeno altrettanto avverso». La definizione non chiede che $\phi$ sia crescente, ma lo è comunque: se $u_1$ e $u_2$ sono crescenti, $\phi=u_2\circ u_1^{-1}$ è la composizione di funzioni crescenti. Poiché $\phi$ è crescente, i due agenti ordinano allo stesso modo le ricchezze certe; la concavità di $\phi$ cambia il modo in cui l'agente 2 valuta le lotterie rispetto all'agente 1.

### Avversione assoluta e avversione relativa

La seconda misura confronta le derivate di $u_1$ e $u_2$ senza passare dalla funzione $\phi$. Si considerano funzioni $u$ due volte derivabili con $u'>0$.

> [!abstract] Definizione
> Le due misure di Arrow-Pratt a ricchezza $W$ sono l'**avversione assoluta al rischio**
>
> $$A(W)=-\frac{u''(W)}{u'(W)}$$
>
> e l'**avversione relativa al rischio**
>
> $$RR(W)=W\,A(W)=-W\,\frac{u''(W)}{u'(W)}.$$

L'avversione assoluta rapporta la derivata seconda di $u$, cambiata di segno, alla sua pendenza; l'avversione relativa la moltiplica per il livello di ricchezza. Con $u'>0$ il segno di $A$ è quello di $-u''$: $A$ è positiva se $u''<0$, nulla se $u$ è lineare e negativa dove $u$ è convessa; lo stesso vale per $RR$ con $W>0$. Nella maggior parte del capitolo si usano utilità con $u''<0$, per le quali le misure sono positive.

Il teorema seguente collega la prima misura alla seconda: confrontare due utilità con la trasformazione concava equivale a confrontare le loro avversioni assolute.

> [!tip] Teorema
> Siano $u_1$ e $u_2$ due utilità due volte derivabili con $u_i'>0$, e sia $u_2=\phi\circ u_1$ con $\phi$ due volte derivabile. Allora
>
> $$\phi''\big(u_1(W)\big)=\frac{u_2'(W)}{\big(u_1'(W)\big)^2}\,\big[A_1(W)-A_2(W)\big],\qquad A_i(W)=-\frac{u_i''(W)}{u_i'(W)}.$$
>
> Di conseguenza $\phi$ è concava se e solo se $A_1(W)\le A_2(W)$ per ogni $W$, e $\phi''<0$ se e solo se $A_1(W)<A_2(W)$.

> [!note] Dimostrazione
> Si deriva due volte $u_2(W)=\phi\big(u_1(W)\big)$. La derivata prima è $u_2'=\phi'(u_1)\,u_1'$, da cui $\phi'(u_1)=u_2'/u_1'$. La derivata seconda, per la regola della funzione composta e del prodotto, è
>
> $$u_2''=\phi''(u_1)\,(u_1')^2+\phi'(u_1)\,u_1''=\phi''(u_1)\,(u_1')^2+\frac{u_2'}{u_1'}\,u_1''.$$
>
> Si isola $\phi''(u_1)$ e si raccoglie $u_2'$:
>
> $$\phi''(u_1)=\frac{1}{(u_1')^2}\Big[u_2''-\frac{u_2'\,u_1''}{u_1'}\Big]=\frac{u_2'}{(u_1')^2}\Big[\frac{u_2''}{u_2'}-\frac{u_1''}{u_1'}\Big]=\frac{u_2'}{(u_1')^2}\,\big[A_1-A_2\big],$$
>
> perché $u_i''/u_i'=-A_i$. Il fattore $u_2'/(u_1')^2$ è positivo, quindi $\phi''$ ha il segno di $A_1-A_2$. Una funzione due volte derivabile è concava se e solo se la sua derivata seconda è non positiva in ogni punto. Il dominio di $\phi$ è l'immagine di $u_1$, che $u_1(W)$ percorre per intero al variare di $W$: la funzione $\phi$ è dunque concava se e solo se $A_1(W)\le A_2(W)$ per ogni $W$.

L'agente 2 è dunque più avverso al rischio dell'agente 1, nel senso della trasformazione concava, quando la sua avversione assoluta è maggiore o uguale a quella dell'agente 1 a ogni livello di ricchezza.

> [!example] Esempio
> Sia $u_1(W)=\ln W$, con $A_1(W)=1/W$. Per ciascuna delle tre utilità $u_2$ seguenti si chiede quale agente sia più avverso al rischio.
>
> (a) $u_2(W)=\ln\ln W$, definita per $W>1$. Per $W>1$ si ha $u_1(W)=\ln W>0$, quindi $u_2=\phi(u_1)$ con $\phi(x)=\ln x$, che è concava: l'agente 2 è più avverso. Lo conferma il calcolo delle avversioni. Le derivate sono
>
> $$u_2'(W)=\frac{1}{W\ln W},\qquad u_2''(W)=-\frac{\ln W+1}{(W\ln W)^2},$$
>
> da cui
>
> $$A_2(W)=\frac{\ln W+1}{W\ln W}=A_1(W)+\frac{1}{W\ln W}>A_1(W).$$
>
> (b) $u_2(W)=(\ln W)^2$, per $W>1$. Qui $u_1=\sqrt{u_2}$, cioè $u_1=\phi(u_2)$ con $\phi(x)=\sqrt{x}$, che è concava: è l'agente 1 il più avverso. Le derivate sono
>
> $$u_2'(W)=\frac{2\ln W}{W},\qquad u_2''(W)=\frac{2(1-\ln W)}{W^2},$$
>
> da cui
>
> $$A_2(W)=\frac{\ln W-1}{W\ln W}=A_1(W)-\frac{1}{W\ln W}<A_1(W).$$
>
> La funzione $u_2$ non è concava ovunque: $u_2''$ è negativa solo per $W>e$, e per $1<W<e$ è positiva, quindi in quell'intervallo $u_2$ è convessa e $A_2<0$. La lettura $u_2=\phi(u_1)$ con $\phi(x)=x^2$ non dà un confronto, perché $x^2$ è convessa.
>
> (c) $u_2(W)=e^{\ln W}=W$, per $W>0$. La funzione è lineare, perciò l'agente 2 è neutrale al rischio: $E[u_2(w+X)]=u_2(w)$ per ogni lotteria a valore atteso nullo, e $A_2=0<A_1$. Si ha $u_1=\ln u_2$ con $\ln$ concava, quindi l'agente 1 è il più avverso.

### Le funzioni CARA e CRRA

Le funzioni di utilità si classificano secondo il modo in cui $A$ e $RR$ dipendono dalla ricchezza.

> [!abstract] Definizione
> Un'utilità ha **avversione assoluta al rischio costante** (CARA, *constant absolute risk aversion*) se $A(W)$ non dipende da $W$, e ha **avversione relativa al rischio costante** (CRRA, *constant relative risk aversion*) se $RR(W)$ non dipende da $W$.

> [!example] Esempio
> Si calcolano le due misure per le tre utilità di riferimento, con le derivate della tabella.
>
> $$u=-\frac{e^{-\lambda W}}{\lambda}:\qquad A(W)=-\frac{-\lambda e^{-\lambda W}}{e^{-\lambda W}}=\lambda,\qquad RR(W)=\lambda W.$$
>
> $$u=\frac{W^{1-\gamma}}{1-\gamma}:\qquad A(W)=-\frac{-\gamma W^{-\gamma-1}}{W^{-\gamma}}=\frac{\gamma}{W},\qquad RR(W)=\gamma.$$
>
> $$u=\ln W:\qquad A(W)=-\frac{-1/W^2}{1/W}=\frac{1}{W},\qquad RR(W)=1.$$
>
> La prima utilità è CARA, con avversione assoluta pari al parametro $\lambda$. La seconda è CRRA, perché la sua avversione relativa è costante e pari a $\gamma$. Il logaritmo è il caso limite $\gamma=1$ della seconda utilità: la formula $A=\gamma/W$ dà $1/W$ e $RR=\gamma=1$, quindi è CRRA.

## Equivalente certo e premio per il rischio

La terza misura confronta due agenti attraverso la somma certa che ciascuno considera equivalente a una stessa lotteria.

> [!abstract] Definizione
> L'**equivalente certo** (*certainty equivalent*, $CE$) di una lotteria $X$ a ricchezza iniziale $w$ è il livello di ricchezza certa che dà la stessa utilità attesa della lotteria:
>
> $$E[u(w+X)]=u(CE).$$
>
> Se $E[X]=0$, il **premio per il rischio** $R$ è la differenza fra la ricchezza iniziale e l'equivalente certo, $R=w-CE$. Vale quindi
>
> $$E[u(w+X)]=u(CE)=u(w-R).$$

L'equivalente certo risponde alla domanda: se l'agente dovesse cedere la sua ricchezza aleatoria $w+X$ in cambio di una ricchezza certa, quale ricchezza chiederebbe? Il premio per il rischio risponde a quest'altra: quanto è disposto a pagare l'agente per evitare di affrontare una lotteria a valore atteso nullo? Nel capitolo $CE$ è un livello di ricchezza certa, non un guadagno. In altri testi l'equivalente certo è espresso come guadagno certo $C$ rispetto alla ricchezza iniziale, con $u(w+C)=E[u(w+X)]$: i due modi sono legati da $C=CE-w$, e per $E[X]=0$ vale $C=-R$. L'equazione che definisce $CE$ non richiede $E[X]=0$ e si applica a qualunque lotteria. Il premio nella forma $R=w-CE$ ha il significato di prezzo del rischio per le lotterie a valore atteso nullo.

Per un agente avverso al rischio il premio non è negativo. Dalla definizione di $R$ e dall'avversione al rischio si ha $u(w-R)=E[u(w+X)]\le u(w)$, e poiché $u$ è crescente ne segue $w-R\le w$, cioè $R\ge0$. L'agente è disposto a rinunciare a una parte della ricchezza attesa per eliminare il rischio: il premio misura quanta, e ordina gli agenti per grado di avversione, perché a parità di lotteria chi è più avverso rinuncia a più ricchezza.

> [!example] Esempio
> Sia $u(W)=\ln W$. Si calcolano equivalente certo e premio per due lotterie equiprobabili.
>
> (i) Ricchezza iniziale $w=10$ e lotteria $X$ che vale $+6$ o $-6$, ciascuno con probabilità $1/2$. L'utilità attesa è
>
> $$\tfrac12\ln16+\tfrac12\ln4=\ln4+\ln2=\ln8=\ln(10-R),$$
>
> quindi $CE=8$ e $R=2$.
>
> (ii) Ricchezza iniziale $w=26$ e lotteria che vale $+10$ o $-10$, ciascuno con probabilità $1/2$. L'utilità attesa è
>
> $$\tfrac12\ln36+\tfrac12\ln16=\ln6+\ln4=\ln24=\ln(26-R),$$
>
> quindi $CE=24$ e $R=2$.
>
> Nel caso (i) l'agente è indifferente tra la ricchezza aleatoria $10\pm6$ e 8 di ricchezza certa. La ricchezza aleatoria ha valore atteso 10 e utilità attesa $\ln8$, inferiore a $\ln10$, l'utilità della ricchezza certa 10: l'agente accetta di rinunciare a 2 della ricchezza attesa per non sostenere il rischio. Il premio coincide nei due casi per una coincidenza dei numeri scelti.

## Equivalenza fra le tre misure

Le tre misure danno lo stesso ordinamento degli agenti. Nell'enunciato $CE_i(w,X)$ e $R_i(w,X)$ sono equivalente certo e premio dell'agente $i$ per la stessa lotteria $X$ e la stessa ricchezza $w$, e le utilità $u_1$ e $u_2$ sono due volte derivabili con $u_i'>0$. In queste ipotesi la funzione $\phi$ tale che $u_2=\phi\circ u_1$ è anch'essa due volte derivabile, perché $\phi'=u_2'/u_1'$ calcolata in $u_1^{-1}$.

> [!tip] Teorema
> Le tre condizioni seguenti sono equivalenti.
>
> 1. $u_2=\phi\circ u_1$ con $\phi$ concava.
> 2. $A_2(w)\ge A_1(w)$ per ogni $w$.
> 3. $CE_2(w,X)\le CE_1(w,X)$ per ogni $w$ e per ogni lotteria $X$ con $E[X]=0$.
>
> Poiché $CE_i=w-R_i$, la condizione (3) equivale a $R_2(w,X)\ge R_1(w,X)$: l'agente più avverso paga di più per evitare la stessa lotteria.

La (1) riguarda la forma delle funzioni: $u_2$ si ottiene da $u_1$ con una trasformazione concava. La (2) è un confronto locale, ricchezza per ricchezza, delle derivate seconde normalizzate. La (3) è un confronto di comportamento: per ogni lotteria a valore atteso nullo e a ogni ricchezza, in cambio della ricchezza aleatoria $w+X$ l'agente 2 si accontenta di una ricchezza certa non maggiore di quella chiesta dall'agente 1.

L'equivalenza fra (1) e (2) è il teorema della sottosezione «Avversione assoluta e avversione relativa». Restano da dimostrare l'implicazione da (1) a (3) e quella da (3) a (2). Con le tre implicazioni $(3)\Rightarrow(2)\Rightarrow(1)\Rightarrow(3)$ il cerchio si chiude.

### Dalla trasformazione concava al premio per il rischio

> [!note] Dimostrazione
> Dell'implicazione $(1)\Rightarrow(3)$. Sia $u_2=\phi\circ u_1$ con $\phi$ concava, e siano $R_1$ e $R_2$ i premi dei due agenti per la lotteria $X$ a ricchezza $w$. Si applicano in ordine la definizione di $R_2$, la relazione $u_2=\phi\circ u_1$, la disuguaglianza di Jensen alla funzione concava $\phi$ e alla variabile $u_1(w+X)$, la definizione di $R_1$ e ancora la relazione $u_2=\phi\circ u_1$:
>
> $$u_2(w-R_2)=E[u_2(w+X)]=E\big[\phi\big(u_1(w+X)\big)\big]\ \le\ \phi\big(E[u_1(w+X)]\big)=\phi\big(u_1(w-R_1)\big)=u_2(w-R_1).$$
>
> La disuguaglianza di Jensen interviene una volta sola, nel terzo passaggio. Poiché $u_2$ è strettamente crescente, da $u_2(w-R_2)\le u_2(w-R_1)$ si può togliere $u_2$ da entrambi i lati e si ottiene $w-R_2\le w-R_1$, cioè $R_2\ge R_1$. Con $CE_i=w-R_i$ questo equivale a $CE_2\le CE_1$.

### Il premio per lotterie piccole

Per passare da (3) a (2) occorre sapere come si comporta il premio quando la lotteria è piccola. Si considera la lotteria $kX$, con $E[X]=0$ e $k\ge0$ che ne scala la dimensione. Il premio $R(k)$ per $kX$ a ricchezza $w$ è definito da

$$E[u(w+kX)]=u\big(w-R(k)\big).$$

Si assume $u$ due volte derivabile con $u'>0$ e $R$ due volte derivabile (condizione soddisfatta se $X$ assume un numero finito di valori). Si deriva l'identità rispetto a $k$. A sinistra la derivata del valore atteso è il valore atteso della derivata, e $\frac{d}{dk}\,u(w+kX)=X\,u'(w+kX)$. A destra la regola della funzione composta dà $\frac{d}{dk}\,u\big(w-R(k)\big)=-u'\big(w-R(k)\big)\,R'(k)$. Portando tutto a sinistra si ottiene la derivata prima e, derivando ancora, la derivata seconda:

$$E\big[X\,u'(w+kX)\big]+u'\big(w-R(k)\big)\,R'(k)=0,$$

$$E\big[X^2u''(w+kX)\big]-u''\big(w-R(k)\big)\,\big(R'(k)\big)^2+u'\big(w-R(k)\big)\,R''(k)=0.$$

Il secondo termine della seconda equazione viene da $\frac{d}{dk}\big[u'(w-R)\,R'\big]=-u''(w-R)\,(R')^2+u'(w-R)\,R''$.

> [!tip] Teorema
> (Approssimazione di Arrow-Pratt.) Valgono $R(0)=0$, $R'(0)=0$ e
>
> $$R''(0)=A(w)\,E[X^2].$$
>
> Poiché $R$ è due volte derivabile in $0$, vale lo sviluppo di Taylor con resto di Peano $R(k)=\tfrac12\,A(w)\,E[X^2]\,k^2+o(k^2)$ per $k\to0$. Di conseguenza, per $k$ piccolo,
>
> $$R(k)\ \approx\ \tfrac12\,A(w)\,E\big[(kX)^2\big]=\tfrac12\,A(w)\,\mathrm{Var}(kX).$$

> [!note] Dimostrazione
> Per $k=0$ la definizione dà $u(w)=u\big(w-R(0)\big)$, e poiché $u$ è strettamente crescente $R(0)=0$. Nella derivata prima a $k=0$ si ha $u'(w)\,E[X]+u'(w)\,R'(0)=0$; essendo $E[X]=0$ resta $u'(w)\,R'(0)=0$, e poiché $u'(w)>0$ si conclude $R'(0)=0$. Il fatto che $R'(0)$ si annulli dipende quindi da $E[X]=0$, mentre $R(0)=0$ serve a riconoscere che $u'(w-R(0))=u'(w)$.
>
> Nella derivata seconda a $k=0$, con $R(0)=0$ e $R'(0)=0$, il termine in $(R')^2$ scompare e rimane $E[X^2]\,u''(w)+u'(w)\,R''(0)=0$, da cui
>
> $$R''(0)=-\frac{u''(w)}{u'(w)}\,E[X^2]=A(w)\,E[X^2].$$
>
> Lo sviluppo di Taylor di $R$ in $k=0$ è $R(k)\approx R(0)+R'(0)\,k+\tfrac12R''(0)\,k^2=\tfrac12A(w)\,E[X^2]\,k^2$. Poiché $E[kX]=0$, si ha $E[(kX)^2]=\mathrm{Var}(kX)$.

Per lotterie piccole il premio è dunque proporzionale alla varianza della lotteria, con coefficiente $\tfrac12A(w)$. Se $k$ raddoppia, la varianza di $kX$ quadruplica e, per $k$ piccolo, quadruplica anche il premio. L'avversione assoluta misura quindi, a meno del fattore $\tfrac12$, il premio per unità di varianza. Lo stesso risultato spiega perché $A$ ordina gli agenti: a parità di ricchezza e di lotteria con $E[X^2]>0$, se $A_2(w)>A_1(w)$ l'agente 2 ha, per $k$ abbastanza piccolo, un premio maggiore.

Per un agente avverso al rischio ($u$ concava) il premio non diminuisce al crescere della dimensione della lotteria. Dalla derivata prima, per $k>0$, e usando $E[X]\,u'(w)=0$, si ha

$$u'\big(w-R(k)\big)\,R'(k)=-E\big[X\,u'(w+kX)\big]=-E\Big[X\big(u'(w+kX)-u'(w)\big)\Big].$$

Poiché $u$ è concava, $u'$ non cresce. Se $X>0$ allora $w+kX>w$ e $u'(w+kX)-u'(w)\le0$; se $X<0$ la differenza è non negativa. In ogni caso $X\big(u'(w+kX)-u'(w)\big)\le0$, per cui il membro di destra è non negativo e, essendo $u'>0$, $R'(k)\ge0$.

La tabella confronta il premio esatto con l'approssimazione per $u=\ln W$, $w=10$ e $X=\pm1$ con uguale probabilità; qui $A(10)=1/10$ e $E[X^2]=1$, per cui l'approssimazione è $0{,}05\,k^2$.

| $k$ | $R(k)$ esatto | approssimazione |
|---|---|---|
| 0,5 | 0,0125 | 0,0125 |
| 1 | 0,0501 | 0,05 |
| 2 | 0,2020 | 0,2 |
| 3 | 0,4606 | 0,45 |
| 5 | 1,3397 | 1,25 |
| 8 | 4,0000 | 3,2 |
| 9,9 | 8,5893 | 4,9005 |

L'approssimazione è accurata finché $k$ è piccolo rispetto alla ricchezza e si deteriora al crescere di $k$; il premio esatto tende a 10 quando $k$ tende a 10, cioè quando la lotteria può azzerare la ricchezza.

Il teorema permette anche di controllare i due esempi con il logaritmo. Per il caso (i), $w=10$ e $E[X^2]=36$, l'approssimazione dà $\tfrac12\cdot\tfrac1{10}\cdot36=1{,}8$; per il caso (ii), $w=26$ e $E[X^2]=100$, dà $\tfrac12\cdot\tfrac1{26}\cdot100\approx1{,}923$. I valori esatti sono entrambi 2. Lo scarto è contenuto ma non nullo, perché le lotterie dell'esempio non sono piccole rispetto alla ricchezza.

### Dal premio per il rischio all'avversione assoluta

> [!note] Dimostrazione
> Dell'implicazione $(3)\Rightarrow(2)$. Si supponga vera la condizione (3) e si fissino la ricchezza $w$ e una lotteria $X$ non degenere, con un numero finito di valori e $E[X]=0$. Anche $kX$ ha valore atteso nullo per ogni $k\ge0$, quindi la (3) dà $R_2(k)\ge R_1(k)$ per ogni $k\ge0$, dove $R_i(k)$ è il premio dell'agente $i$ per $kX$. Per il teorema di approssimazione, $R_i(k)=\tfrac12A_i(w)\,E[X^2]\,k^2+o(k^2)$ per $k\to0$. Si divide la disuguaglianza per $k^2$ e si passa al limite per $k\to0$: $\tfrac12A_2(w)\,E[X^2]\ge\tfrac12A_1(w)\,E[X^2]$. Poiché $E[X^2]>0$, ne segue $A_2(w)\ge A_1(w)$. La ricchezza $w$ è arbitraria, quindi vale (2).

Lo sviluppo di Taylor da solo mostrerebbe che (2) implica (3) soltanto al secondo ordine e per lotterie piccole. Che l'implicazione valga per lotterie di qualsiasi dimensione dipende dal passaggio per (1), dove interviene la disuguaglianza di Jensen.

## L'effetto ricchezza

Gli agenti tendono a essere meno avversi al rischio quando sono più ricchi. In termini di premio, per ogni lotteria $X$ a valore atteso nullo il premio $R(w,X)$ non cresce con la ricchezza iniziale:

$$\frac{\partial R(w,X)}{\partial w}\ \le\ 0\qquad\text{per ogni }w.$$

«Meno avverso» significa «premio per il rischio più basso». Resta da stabilire quando la condizione vale nel modello, cioè per quali funzioni di utilità. La risposta passa dall'avversione assoluta al rischio.

### Come varia il premio con la ricchezza

Il premio $R(w,X)$ è definito da $E[u(w+X)]=u\big(w-R(w,X)\big)$. Si assume $R$ derivabile rispetto a $w$. Derivando ambo i membri rispetto a $w$:

$$E[u'(w+X)]=u'\big(w-R\big)\Big(1-\frac{\partial R}{\partial w}\Big),\qquad\text{da cui}\qquad\frac{\partial R(w,X)}{\partial w}=1-\frac{E[u'(w+X)]}{u'(w-R(w,X))}.$$

Poiché $u'>0$, il segno della derivata si legge dal rapporto:

$$\frac{\partial R}{\partial w}\le0\iff E[u'(w+X)]\ge u'(w-R)\iff E[-u'(w+X)]\le-u'(w-R).$$

La condizione centrale confronta l'utilità marginale attesa in presenza del rischio, $E[u'(w+X)]$, con l'utilità marginale in corrispondenza dell'equivalente certo, $u'(w-R)$. Per vedere quando vale si usa la terza forma, che ha la struttura di una disuguaglianza di avversione al rischio applicata alla funzione $v=-u'$ al posto di $u$.

Si assume $u''<0$, per cui $v'=-u''>0$ e $v$ è crescente, come si richiede a una funzione di utilità. Siano $R_v$ il premio dell'agente con utilità $v$, definito da $v(w-R_v)=E[v(w+X)]$, e $R_u$ il premio dell'agente con utilità $u$, entrambi per la lotteria $X$ a ricchezza $w$. La terza forma dice $v(w-R_v)=E[v(w+X)]\le v(w-R_u)$. Poiché $v$ è strettamente crescente, questa disuguaglianza equivale a $w-R_v\le w-R_u$, cioè a $R_v\ge R_u$, e il ragionamento si può percorrere in senso inverso. Il premio di $u$ non cresce dunque con la ricchezza, per ogni $X$ e ogni $w$, se e solo se il premio di $-u'$ non è mai inferiore a quello di $u$. In questo caso $-u'$ è più avversa al rischio di $u$, nel senso della terza misura.

### Prudenza e avversione assoluta

Per applicare il teorema di equivalenza alla coppia $u$ e $-u'$ si calcola l'avversione assoluta di $-u'$. Si assume $u$ tre volte derivabile, con $u''<0$, così che $A>0$ e il rapporto $u'''/u''$ sia definito.

> [!abstract] Definizione
> Il **coefficiente di prudenza assoluta** di $u$ è
>
> $$P(W)=-\frac{u'''(W)}{u''(W)}.$$

Per $v=-u'$ si ha $v'=-u''$ e $v''=-u'''$, quindi

$$A_{-u'}(w)=-\frac{v''(w)}{v'(w)}=-\frac{-u'''(w)}{-u''(w)}=-\frac{u'''(w)}{u''(w)}=P(w).$$

La prudenza è dunque l'avversione assoluta della funzione $-u'$. Il legame con la variazione di $A$ si ottiene derivando $A=-u''/u'$:

$$A'(w)=-\frac{u'''}{u'}+\Big(\frac{u''}{u'}\Big)^2=-\frac{u'''}{u'}+A^2.$$

Il primo termine si scrive $-\dfrac{u'''}{u'}=\Big(-\dfrac{u'''}{u''}\Big)\dfrac{u''}{u'}=P\cdot(-A)$, per cui

$$A'(w)=A(w)\,\big[A(w)-P(w)\big].$$

Poiché $A>0$, il segno di $A'$ è quello di $A-P$: vale $A'\le0$ se e solo se $P\ge A$.

### Condizioni equivalenti per il DARA

> [!abstract] Definizione
> Un'utilità ha **avversione assoluta al rischio decrescente** (DARA, *decreasing absolute risk aversion*) se $A(w)$ è decrescente in $w$. Nel capitolo «decrescente» è inteso in senso debole: $A'(w)\le0$ per ogni $w$, cioè $A$ non cresce mai. Il caso CARA, con $A'=0$, è il caso di bordo che soddisfa la definizione.

> [!tip] Teorema
> Sia $u$ tre volte derivabile, con $u'>0$ e $u''<0$. Le condizioni seguenti sono equivalenti.
>
> 1. $u$ ha avversione assoluta al rischio decrescente (DARA): $A'(w)\le0$ per ogni $w$.
> 2. Il premio per il rischio $R(w,X)$ è decrescente in $w$ per ogni lotteria $X$ a valore atteso nullo: $\partial R/\partial w\le0$.
> 3. $-u'$ è più concava, cioè più avversa al rischio, di $u$.
> 4. $P(w)\ge A(w)$ per ogni $w$.

> [!note] Dimostrazione
> Le equivalenze seguono dai risultati ottenuti sopra, che si richiamano in ordine.
>
> (2) $\Leftrightarrow$ (3): la derivata di $R$ rispetto a $w$ è non positiva per ogni $X$ e ogni $w$ se e solo se $R_{-u'}\ge R_u$ per ogni $X$ e ogni $w$. Con $u_1=u$ e $u_2=-u'$ questa è la condizione (3) del teorema di equivalenza, che per lo stesso teorema equivale alla (1): $-u'=\phi\circ u$ con $\phi$ concava, cioè $-u'$ è più avversa al rischio di $u$.
>
> (3) $\Leftrightarrow$ (4): per l'equivalenza fra le condizioni (1) e (2) del teorema di equivalenza, con $u_1=u$ e $u_2=-u'$, la condizione «$-u'$ è più concava di $u$» equivale a $A_{-u'}(w)\ge A_u(w)$ per ogni $w$. Poiché $A_{-u'}=P$, equivale a $P(w)\ge A(w)$.
>
> (4) $\Leftrightarrow$ (1): dall'identità $A'=A\,(A-P)$ con $A>0$, $P\ge A$ equivale a $A'\le0$.

La forma debole include CARA, per cui $A'=0$ e $P=A$. Con le disuguaglianze strette ($A'<0$, $P>A$, premio strettamente decrescente in $w$) si ha la convenzione alternativa: in essa $A'<0$ equivale a $P>A$, e il caso CARA, che soddisfa la forma debole, non soddisfa quella stretta.

Due esempi mostrano la differenza tra un'utilità con $A$ costante e una con $A$ decrescente. In entrambi la lotteria è $X=\pm1{,}5$ con uguale probabilità.

> [!example] Esempio
> *CARA.* Per $u(W)=-e^{-\lambda W}/\lambda$ si ha $E[u(w+X)]=-e^{-\lambda w}\cosh(1{,}5\lambda)/\lambda$, e uguagliandolo a $u(w-R)=-e^{-\lambda(w-R)}/\lambda$ si trova $e^{\lambda R}=\cosh(1{,}5\lambda)$, cioè
>
> $$R=\frac{\ln\cosh(1{,}5\lambda)}{\lambda},$$
>
> che non dipende da $w$. Con $\lambda=0{,}7$ il premio è $R=0{,}6748$ a $w=1$, a $w=5$ e a $w=20$: con utilità CARA la ricchezza iniziale non modifica il premio, quindi non c'è effetto ricchezza.
>
> *CRRA con $\gamma=2$.* La funzione è $u(W)=-1/W$ per $W>0$, e la ricchezza finale $w-1{,}5$ è positiva se $w>1{,}5$. L'utilità attesa è $E[u(w+X)]=-\tfrac12\Big(\dfrac1{w+1{,}5}+\dfrac1{w-1{,}5}\Big)=-\dfrac{w}{w^2-2{,}25}$, e uguagliandola a $u(w-R)=-1/(w-R)$ si ottiene $w-R=(w^2-2{,}25)/w$, cioè
>
> $$R=\frac{2{,}25}{w}.$$
>
> Il premio vale $0{,}75$ a $w=3$, $0{,}45$ a $w=5$ e $0{,}1125$ a $w=20$: decresce con la ricchezza.

## Classificare le tre utilità di riferimento

Si chiede quali tra le tre utilità di riferimento siano CARA, CRRA e DARA. Per ciascuna si calcolano $A$, $A'$, $RR$ e il coefficiente di prudenza $P=-u'''/u''$, con le derivate della tabella iniziale.

| $u(W)$ | $A(W)$ | $A'(W)$ | $RR(W)$ | $P(W)$ | CARA | CRRA | DARA |
|---|---|---|---|---|---|---|---|
| $-e^{-\lambda W}/\lambda$ | $\lambda$ | $0$ | $\lambda W$ | $\lambda$ | sì | no | solo in senso debole |
| $W^{1-\gamma}/(1-\gamma)$ | $\gamma/W$ | $-\gamma/W^2$ | $\gamma$ | $(1+\gamma)/W$ | no | sì | sì |
| $\ln W$ | $1/W$ | $-1/W^2$ | $1$ | $2/W$ | no | sì ($\gamma=1$) | sì |

La prima utilità è CARA, perché $A=\lambda$ è costante. Non è CRRA, perché $RR=\lambda W$ cresce con $W$. Ha $A'=0$ e $P=A=\lambda$, perciò soddisfa la definizione debole di DARA come caso di bordo e non la soddisfa in senso stretto. La seconda è CRRA con $RR=\gamma$, ed è DARA in senso stretto: $A'=-\gamma/W^2<0$ e $P=(1+\gamma)/W>A=\gamma/W$. Il logaritmo è il caso CRRA con $\gamma=1$, con $RR=1$, ed è DARA in senso stretto: $A'=-1/W^2<0$ e $P-A=1/W>0$.

Il risultato vale per ogni utilità CRRA, che è sempre DARA: se $RR=c>0$ è costante allora $A(W)=c/W$ e $A'(W)=-c/W^2<0$. Per il teorema sul DARA, con un'utilità CRRA il premio per una lotteria data non cresce con la ricchezza, e il calcolo con $\gamma=2$ svolto sopra lo mostra.
