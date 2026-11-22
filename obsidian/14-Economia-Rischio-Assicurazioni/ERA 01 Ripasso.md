---
title: "Ripasso di matematica: calcolo, probabilità, funzioni concave e ottimizzazione"
tags:
  - corso/economia-rischio-assicurazioni
  - tipo/lezione
corso: "[[Economia del Rischio e delle Assicurazioni]]"
source: "ERA_Slide_00_Ripasso.pdf"
text_layer: true
verified: true
generated: 2026-11-22
---

## Oggetto del capitolo

Il capitolo ripassa gli strumenti matematici che il resto del corso dà per noti: il calcolo differenziale e integrale, le nozioni di probabilità, le funzioni convesse e concave, l'ottimizzazione con e senza vincoli. Si colloca dopo l'[[ERA 00 Introduzione al Corso|introduzione al corso]] e prima della [[ERA 02 Teoria dell'Utilità Attesa|teoria dell'utilità attesa]]. Serve da riferimento a cui tornare quando un capitolo successivo usa uno di questi risultati senza richiamarlo.

Il seguito del corso usa questi strumenti in punti precisi. Derivate e regola della catena compaiono già nell'[[ERA 03 Avversione al Rischio|avversione al rischio]], dove la concavità è legata alla disuguaglianza di Jensen, che questo capitolo non ripete. La funzione di ripartizione, l'integrazione per parti e l'indipendenza servono al [[ERA 04 Confronto di Opzioni Rischiose|confronto di opzioni rischiose]]. L'ottimizzazione non vincolata e la concavità stretta sono la base del [[ERA 05 Portafoglio Ottimale|portafoglio ottimale]], covarianza e indipendenza entrano nel [[ERA 06 Prezzo dei Titoli|prezzo dei titoli]] e il teorema di Kuhn-Tucker governa il problema dell'[[ERA 08 Assicurazioni e Azzardo Morale|azzardo morale]].

## Notazione

Le lettere $f$ e $g$ indicano funzioni generiche, e $F$ e $G$ lo stesso nell'integrazione per parti. Nella sezione di probabilità $f$ è la funzione di probabilità o la densità e $F$ la funzione di ripartizione; i due usi non compaiono mai nella stessa formula. Il simbolo $\mathbb P(\cdot)$ è la probabilità di un evento ed $E[\cdot]$ il valore atteso. L'esponente di una potenza si scrive $\alpha$, mentre il peso di una combinazione convessa si scrive $\pi$, come nel capitolo sull'avversione al rischio.

La lettera $\lambda$ indica qui il moltiplicatore di Lagrange. Nell'avversione al rischio è invece il parametro dell'utilità esponenziale, e per questo la costante dell'esempio sulla regola della catena si chiama $c$. Nell'ultimo esempio del capitolo $W$ è la ricchezza totale da ripartire, mentre nell'avversione al rischio è l'argomento della funzione di utilità.

## Calcolo differenziale

### Derivata e derivata seconda

Sia $f:\mathbb R\to\mathbb R$ una funzione a valori reali. La **derivata** di $f$ nel punto $x$ è il limite del rapporto incrementale

$$f'(x)=\lim_{\varepsilon\to0}\frac{f(x+\varepsilon)-f(x)}{\varepsilon}.$$

La funzione è derivabile in $x$ se il limite esiste ed è finito. In quel caso $f'(x)$ è la variazione di $f$ per unità di $x$, in corrispondenza di variazioni piccole dell'argomento; geometricamente è la pendenza della tangente al grafico nel punto $(x,f(x))$. La derivata seconda è la derivata della funzione $f'$,

$$f''(x)=\frac{df'(x)}{dx},$$

e presuppone che $f'$ sia definita attorno a $x$ e derivabile in $x$. Misura come cambia la pendenza al crescere di $x$, e il suo segno permette più avanti di riconoscere le funzioni convesse e concave.

### Derivate notevoli

Tre derivate ricorrono in tutto il corso:

$$\frac{d\exp(x)}{dx}=\exp(x),\qquad\frac{d\ln(x)}{dx}=\frac1x,\qquad\frac{d\,(x^{\alpha})}{dx}=\alpha x^{\alpha-1}.$$

L'esponenziale è definito su tutto $\mathbb R$. Il logaritmo e la potenza con esponente reale $\alpha$ richiedono $x>0$; se $\alpha$ è un intero positivo la terza formula vale su tutto $\mathbb R$.

### Regola della catena (o della funzione composta)

Per la funzione composta $g\circ f(x)=g(f(x))$ vale

$$\frac{d\,g\circ f(x)}{dx}=g'(f(x))\cdot f'(x),$$

purché $f$ sia derivabile in $x$ e $g$ sia derivabile in $f(x)$. La derivata della funzione esterna si calcola nel valore che assume la funzione interna e si moltiplica per la derivata di quest'ultima.

> [!example] Esempio
> Sia $c$ una costante, $f(x)=cx$ e $g=\exp$. Allora $g'(f(x))=\exp(cx)$ e $f'(x)=c$, quindi
>
> $$\frac{d\exp(cx)}{dx}=\frac{d\exp(cx)}{d(cx)}\cdot\frac{d(cx)}{dx}=c\,\exp(cx).$$
>
> Il primo fattore è la derivata dell'esponenziale calcolata nel punto $cx$, il secondo è la derivata dell'argomento $cx$ rispetto a $x$.

### Derivate parziali

Sia $f:\mathbb R^n\to\mathbb R$ una funzione a valori reali di $n$ variabili. La **derivata parziale** di $f$ rispetto a $x_i$ è

$$\frac{\partial f(x)}{\partial x_i}=\lim_{\varepsilon\to0}\frac{f(x_1,\dots,x_i+\varepsilon,\dots,x_n)-f(x_1,\dots,x_i,\dots,x_n)}{\varepsilon},$$

cioè la derivata ordinaria rispetto a $x_i$, calcolata tenendo fisse le altre variabili. Le derivate seconde si ottengono derivando una seconda volta una derivata parziale. In $\partial^2 f(x)/\partial x_i^2$ si deriva due volte rispetto a $x_i$; in $\partial^2 f(x)/\partial x_i\,\partial x_j$ si deriva rispetto a $x_i$ la derivata parziale rispetto a $x_j$.

Sia $g:\mathbb R\to\mathbb R$ una funzione di una sola variabile. La regola della catena diventa

$$\frac{\partial\,g\circ f(x)}{\partial x_i}=g'(f(x))\cdot\frac{\partial f(x)}{\partial x_i}.$$

La ragione è che, fissate le altre variabili, $f$ è una funzione della sola $x_i$ e si applica la regola a una variabile. Le derivate che compaiono devono esistere.

> [!example] Esempio
> Per $f(x,y)=x^2+xy+y^2$ le derivate parziali prime sono
>
> $$\frac{\partial f(x,y)}{\partial x}=2x+y,\qquad\frac{\partial f(x,y)}{\partial y}=x+2y,$$
>
> e le derivate seconde sono
>
> $$\frac{\partial^2 f(x,y)}{\partial x^2}=2,\qquad\frac{\partial^2 f(x,y)}{\partial y^2}=2,\qquad\frac{\partial^2 f(x,y)}{\partial x\,\partial y}=1.$$
>
> La derivata mista si ottiene derivando $x+2y$ rispetto a $x$. Derivando invece $2x+y$ rispetto a $y$ si trova ancora 1: per questo polinomio l'ordine di derivazione non cambia il risultato.

## Integrali

### L'integrale come limite di somme

Sia $[a,b]$ un intervallo e $f:\mathbb R\to\mathbb R$. Una **partizione** di $[a,b]$ è una famiglia di intervalli $[a_j,a_{j+1})$, per $j=1,\dots,n$, con $a=a_1<a_2<\dots<a_{n+1}=b$; l'ultimo intervallo si prende chiuso, $[a_n,b]$, perché contenga $b$. La somma di Riemann $\sum_{j=1}^{n}f(a_j)\,[a_{j+1}-a_j]$ è la somma delle aree di rettangoli con base $a_{j+1}-a_j$ e altezza $f(a_j)$, il valore di $f$ nell'estremo sinistro di ciascun intervallo. L'ampiezza della partizione è la lunghezza del suo intervallo più lungo, $\max_j(a_{j+1}-a_j)$.

Se $f$ è Riemann-integrabile, l'integrale è il limite di queste somme quando la partizione si infittisce, cioè quando la sua ampiezza tende a zero:

$$\int_a^b f(x)\,dx=\lim_{\max_j(a_{j+1}-a_j)\to0}\ \sum_{j=1}^{n}f(a_j)\,[a_{j+1}-a_j].$$

Il punto in cui si valuta $f$ in ogni intervallo può essere uno qualsiasi, e qui è l'estremo sinistro. Ogni funzione continua su $[a,b]$ è Riemann-integrabile. Che il numero $n$ di intervalli tenda all'infinito non basta: occorre che anche l'intervallo più lungo si accorci.

> [!example] Esempio
> Sia $f(x)=x$ su $[0,1]$. Si prenda una partizione il cui primo intervallo è sempre $[0,\tfrac12)$, mentre gli altri $n-1$ hanno tutti la stessa ampiezza e coprono $[\tfrac12,1]$. Il primo intervallo contribuisce $f(0)\cdot\tfrac12=0$, e il resto delle somme tende, per $n\to\infty$, all'integrale di $x$ su $[\tfrac12,1]$, cioè a $\tfrac38$. L'integrale su $[0,1]$ vale invece $\tfrac12$. Le somme non convergono all'integrale perché l'ampiezza della partizione non scende mai sotto $\tfrac12$.

### Teorema fondamentale del calcolo

L'integrazione è la procedura inversa della derivazione. Una funzione $g$ con $g'=f$ si dice primitiva di $f$. Una primitiva è definita a meno di una costante additiva, che si cancella nella differenza $g(b)-g(a)$.

> [!tip] Teorema
> (Teorema fondamentale del calcolo.) Siano $f$ e $g$ funzioni a valori reali definite sull'intervallo chiuso $[a,b]$. Se $g$ è continua su $[a,b]$, derivabile in $(a,b)$ con $g'(x)=f(x)$ per ogni $x\in(a,b)$, e $f$ è Riemann-integrabile, allora
>
> $$\int_a^b f(x)\,dx=g(b)-g(a)=g(x)\Big|_a^b.$$

Il teorema riduce il calcolo di un limite di somme a una sottrazione: basta trovare una primitiva e valutarla agli estremi, e il risultato è la variazione complessiva di $g$ sull'intervallo, ricostruita sommando le variazioni infinitesime $f(x)\,dx$. Le condizioni di regolarità sono quelle dell'enunciato, e sono soddisfatte in particolare quando $f$ è continua. Vale anche il verso opposto: se $f$ è continua, la funzione $x\mapsto\int_a^x f(t)\,dt$ è derivabile e la sua derivata è $f$.

### Integrali notevoli

Con $s$ variabile di integrazione e $x$ estremo superiore, tre integrali ricorrono nel corso:

$$\int_0^x\exp(s)\,ds=\exp(s)\Big|_0^x=\exp(x)-1,$$

$$\int_1^x\frac1s\,ds=\ln(s)\Big|_1^x=\ln(x)-\ln(1)=\ln(x),$$

$$\int_0^x s^{\alpha}\,ds=\frac{s^{1+\alpha}}{1+\alpha}\Big|_0^x=\frac{x^{1+\alpha}}{1+\alpha}.$$

Il primo vale per ogni $x$. Il secondo richiede $x>0$, e per $x<1$ l'integrale è orientato, cioè con l'estremo superiore minore dell'inferiore. Il terzo richiede $x>0$ e $\alpha>-1$; per $\alpha$ intero non negativo vale per ogni $x$. Per $-1<\alpha<0$ la funzione $s^\alpha$ non è limitata vicino a zero, e l'integrale è improprio ma converge. Per $\alpha\le-1$ l'integrale tra $0$ e $x$ diverge. Il caso $\alpha=-1$ è quello del logaritmo, che per questo ha l'estremo inferiore in $1$ e non in $0$.

### Integrazione per parti

Siano $F$ e $G$ funzioni continuamente derivabili su $[a,b]$. Allora

$$\int_a^b F(x)\,G'(x)\,dx=F(x)G(x)\Big|_a^b-\int_a^b G(x)\,F'(x)\,dx.$$

La formula serve nelle dimostrazioni sulla dominanza stocastica, nel capitolo sul [[ERA 04 Confronto di Opzioni Rischiose|confronto di opzioni rischiose]].

> [!note] Dimostrazione
> Per la regola del prodotto, $(FG)'=F'G+FG'$. Poiché $F$ e $G$ sono continuamente derivabili, il secondo membro è continuo, quindi integrabile su $[a,b]$, e $FG$ è una sua primitiva. Per il teorema fondamentale del calcolo,
>
> $$F(b)G(b)-F(a)G(a)=\int_a^b F'(x)G(x)\,dx+\int_a^b F(x)G'(x)\,dx.$$
>
> Portando il primo integrale a primo membro si ottiene la formula.

## Probabilità

In questa parte del capitolo $f$ e $F$ hanno il significato fissato nella notazione.

### Variabile casuale

Un esperimento aleatorio è descritto da un insieme $\Omega$ dei suoi risultati elementari e da una distribuzione di probabilità $\mathbb P$, che assegna una probabilità agli eventi, cioè a sottoinsiemi di $\Omega$ (a tutti, quando $\Omega$ è finito come nel lancio di una moneta). La coppia $(\Omega,\mathbb P)$ è lo spazio di probabilità. Nel lancio di una moneta $\Omega=\{\text{Testa},\text{Croce}\}$ e $\mathbb P(\text{Testa})=\mathbb P(\text{Croce})=\tfrac12$.

Lo spazio di probabilità descrive i risultati, che possono non essere numeri, e non è ancora una variabile casuale. Questa si ottiene associando un numero a ogni risultato.

> [!abstract] Definizione
> Una **variabile casuale** reale è una funzione $X:\Omega\to\mathbb R$ che a ogni risultato elementare associa un numero. A rigore la funzione deve essere misurabile, condizione tecnica che qui si dà per soddisfatta. La distribuzione di $X$ è quella che $\mathbb P$ induce sui valori di $X$: $\mathbb P(X=x)$ è la probabilità dell'insieme dei risultati a cui $X$ assegna il valore $x$.

Poiché $X$ è una funzione, a ogni condizione sui suoi valori corrisponde un evento: $\{X\le x\}$ è l'insieme dei risultati $\omega$ per cui $X(\omega)\le x$, e $\mathbb P(X\le x)$ è la probabilità di quell'insieme. Il corso considera variabili casuali a valori reali. Nell'esempio della moneta si sceglie $X(\text{Testa})=1$ e $X(\text{Croce})=0$, per cui $\mathbb P(X=1)=\mathbb P(X=0)=\tfrac12$.

### Funzione di ripartizione, funzione di probabilità e densità

La **funzione di ripartizione** (*cumulative distribution function*, c.d.f.) di $X$ è

$$F(x)=\mathbb P(X\le x).$$

È non decrescente, con $0\le F\le1$, tende a $0$ per $x\to-\infty$ e a $1$ per $x\to+\infty$, e per $a<b$ vale $\mathbb P(a<X\le b)=F(b)-F(a)$.

Per una variabile discreta la **funzione di probabilità** (*probability mass function*, p.m.f.) è

$$f(x)=\mathbb P(X=x),$$

con $f\ge0$ e $\sum_x f(x)=1$. Per una variabile continua la **densità** (*probability density function*, p.d.f.) è

$$f(x)=F'(x),$$

con $f\ge0$ e $\int_{-\infty}^{\infty}f(x)\,dx=1$. Le due scritture si corrispondono attraverso il teorema fondamentale del calcolo: se $F(x)=\int_{-\infty}^{x}f(t)\,dt$ per ogni $x$, allora $F'(x)=f(x)$ in ogni punto in cui $f$ è continua. In una variabile continua ogni singolo valore ha probabilità zero, per cui $\mathbb P(a\le X\le b)=\mathbb P(a<X\le b)=F(b)-F(a)=\int_a^b f(x)\,dx$, e $f(x)$ dà una probabilità solo se integrata su un intervallo.

### Valore atteso e varianza

Il **valore atteso** di una variabile casuale è

$$E[X]=\int x\,f(x)\,dx\ \ (\text{densità})\qquad\text{oppure}\qquad E[X]=\sum_x x\,f(x)\ \ (\text{funzione di probabilità}).$$

Il valore atteso è la media dei valori di $X$ pesati con le loro probabilità. La **varianza** è il valore atteso dello scarto quadratico dalla media, e misura quanto i valori si disperdono attorno a essa:

$$\mathrm{Var}(X)=E\big[(X-E[X])^2\big]=\int(x-E[X])^2f(x)\,dx\ \ \text{oppure}\ \ \sum_x(x-E[X])^2f(x).$$

Entrambe esistono se gli integrali o le serie convergono. Per la variabile della moneta, con $X(\text{Testa})=1$ e $X(\text{Croce})=0$, si ha $E[X]=\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$ e $\mathrm{Var}(X)=\tfrac12\big(1-\tfrac12\big)^2+\tfrac12\big(0-\tfrac12\big)^2=\tfrac14$.

Per il calcolo conviene una forma equivalente della varianza.

> [!tip] Teorema
> Se $E[X^2]$ è finito, $\mathrm{Var}(X)=E[X^2]-(E[X])^2$.

> [!note] Dimostrazione
> Si sviluppa il quadrato: $(X-E[X])^2=X^2-2E[X]\,X+(E[X])^2$. Poiché $E[X]$ è una costante e il valore atteso è lineare,
>
> $$\mathrm{Var}(X)=E[X^2]-2E[X]\,E[X]+(E[X])^2=E[X^2]-(E[X])^2.$$

> [!example] Esempio
> Sia $X\sim U[0,1]$, la variabile uniforme su $[0,1]$. La sua densità è $f(x)=1$ per $x\in[0,1]$ e $0$ altrove, e la sua funzione di ripartizione è $F(x)=x$ su $[0,1]$. Il valore atteso è
>
> $$E[X]=\int_0^1 x\,dx=\tfrac12,$$
>
> e la varianza è
>
> $$\mathrm{Var}(X)=\int_0^1\Big(x-\tfrac12\Big)^2dx=\Big[\tfrac{(x-1/2)^3}{3}\Big]_0^1=\tfrac1{24}+\tfrac1{24}=\tfrac1{12}.$$
>
> Come controllo, $E[X^2]=\int_0^1x^2\,dx=\tfrac13$ e $\tfrac13-\tfrac14=\tfrac1{12}$.

### Variabili casuali congiunte e indipendenza

Date due variabili casuali $X$ e $Y$ sullo stesso spazio di probabilità, la funzione di ripartizione congiunta è

$$F(x,y)=\mathbb P(X\le x,\,Y\le y).$$

Per variabili discrete la funzione di probabilità congiunta è $f(x,y)=\mathbb P(X=x,\,Y=y)$. Per variabili continue la densità congiunta è

$$f(x,y)=\frac{\partial^2F(x,y)}{\partial x\,\partial y}.$$

Le distribuzioni delle singole variabili si ricavano dalla congiunta e si dicono marginali. Con un pedice per distinguerle dalla congiunta, $f_X(x)=\sum_y f(x,y)$ nel caso discreto e $f_X(x)=\int f(x,y)\,dy$ nel caso continuo; allo stesso modo si ottiene $f_Y$.

> [!abstract] Definizione
> Due variabili casuali $X$ e $Y$ sono **indipendenti** se, per ogni coppia di valori $(x,y)$,
>
> $$f(x,y)=f_X(x)\,f_Y(y).$$

La condizione è equivalente a $F(x,y)=F_X(x)\,F_Y(y)$, dove $F_X$ e $F_Y$ sono le funzioni di ripartizione delle singole variabili: la distribuzione congiunta di due variabili indipendenti è il prodotto delle marginali. In termini di informazione, conoscere il valore di una delle due non cambia la distribuzione dell'altra.

### Covarianza

La **covarianza** di $X$ e $Y$ è

$$\mathrm{Cov}(X,Y)=E\big[(X-E[X])(Y-E[Y])\big]=E[XY]-E[X]\,E[Y].$$

La covarianza misura se, rispetto alle rispettive medie, le due variabili tendono a spostarsi nella stessa direzione o in direzioni opposte. La seconda uguaglianza segue dalla linearità del valore atteso. Il prodotto si sviluppa in $XY-E[Y]\,X-E[X]\,Y+E[X]\,E[Y]$, e prendendone il valore atteso si ottiene $E[XY]-E[Y]E[X]-E[X]E[Y]+E[X]E[Y]=E[XY]-E[X]E[Y]$.

> [!abstract] Definizione
> Due variabili casuali sono **correlate positivamente** (**negativamente**) se $\mathrm{Cov}(X,Y)>0$ ($<0$).

> [!example] Esempio
> Due titoli, Apple e Microsoft, hanno ciascuno un prezzo alto o basso, come una moneta con due facce. Sia $X$ il prezzo di Apple e $Y$ quello di Microsoft, con alto codificato $1$ e basso codificato $0$; qualunque codifica crescente dà lo stesso segno alla covarianza, perché $\mathrm{Cov}(aX+b,\,cY+d)=ac\,\mathrm{Cov}(X,Y)$ con $a,c>0$. Siano $p_X=\mathbb P(X=1)$ e $p_Y=\mathbb P(Y=1)$, e sia $\mathbb P(Y=1\mid X=1)=\mathbb P(X=1,\,Y=1)/\mathbb P(X=1)$ la probabilità che $Y$ sia alto quando si sa che $X$ è alto. Allora
>
> $$\mathrm{Cov}(X,Y)=\mathbb P(X=1,Y=1)-p_Xp_Y=p_X\big[\mathbb P(Y=1\mid X=1)-p_Y\big].$$
>
> Se un prezzo alto di Apple implica un prezzo alto di Microsoft, la probabilità condizionata vale $1$ e $\mathrm{Cov}(X,Y)=p_X(1-p_Y)>0$, purché $p_X>0$ e $p_Y<1$: le variabili sono correlate positivamente. Se un prezzo alto di Apple implica un prezzo basso di Microsoft, la probabilità condizionata vale $0$ e $\mathrm{Cov}(X,Y)=-p_Xp_Y<0$, purché $p_X>0$ e $p_Y>0$: sono correlate negativamente. Con due monete eque la covarianza vale $+\tfrac14$ se le monete cadono sempre uguali, $-\tfrac14$ se cadono sempre opposte e $0$ se sono indipendenti.
>
> Per due variabili con due soli valori, come queste, e con $p_X>0$, la covarianza è positiva esattamente quando sapere che $X$ è alto rende più probabile che lo sia anche $Y$: il suo segno è quello di $\mathbb P(Y=1\mid X=1)-p_Y$.

## Funzioni convesse e concave

### Definizioni

> [!abstract] Definizione
> Una funzione $f:\mathbb R^n\to\mathbb R$ è **convessa** se, per ogni $\pi\in[0,1]$ e per ogni $x,y\in\mathbb R^n$,
>
> $$f\big(\pi x+(1-\pi)y\big)\ \le\ \pi f(x)+(1-\pi)f(y).$$
>
> La funzione $f$ è **concava** se $-f$ è convessa, cioè se per ogni $\pi\in[0,1]$ e per ogni $x,y\in\mathbb R^n$
>
> $$f\big(\pi x+(1-\pi)y\big)\ \ge\ \pi f(x)+(1-\pi)f(y).$$

Al variare di $\pi$ da $0$ a $1$ il punto $\pi x+(1-\pi)y$ percorre il segmento che va da $y$ a $x$, e il membro destro è la media pesata dei valori di $f$ agli estremi. Per $n=1$ il membro destro è l'ordinata, nel punto $\pi x+(1-\pi)y$, della corda che unisce $(x,f(x))$ e $(y,f(y))$. La funzione è convessa se il grafico sta sotto ogni corda, concava se sta sopra. La definizione richiede che il segmento tra $x$ e $y$ appartenga al dominio: su $\mathbb R^n$ è sempre vero, su un sottoinsieme occorre che sia convesso, come un intervallo.

> [!abstract] Definizione
> La funzione $f$ è **strettamente convessa** se la disuguaglianza della convessità è stretta per $x\neq y$ e $\pi\in(0,1)$. È **strettamente concava** se $-f$ è strettamente convessa.

Una funzione che è sia convessa sia concava è affine; per $n=1$ è una retta. Per una funzione affine la disuguaglianza vale sempre come uguaglianza, quindi non è mai strettamente convessa né strettamente concava. La disuguaglianza di Jensen, che estende la concavità dalla media di due valori alla media rispetto a una distribuzione qualsiasi, è nel capitolo sull'[[ERA 03 Avversione al Rischio|avversione al rischio]].

### Il criterio della derivata seconda

> [!tip] Teorema
> Sia $f$ due volte derivabile su un intervallo $I$. Allora $f$ è convessa su $I$ se e solo se $f''(x)\ge0$ per ogni $x\in I$, ed è concava su $I$ se e solo se $f''(x)\le0$ per ogni $x\in I$. Se $f''>0$ su tutto $I$ la funzione è strettamente convessa; se $f''<0$ è strettamente concava.

Il verso opposto per le versioni strette non vale: $f(x)=x^4$ è strettamente convessa, ma $f''(0)=0$.

La richiesta che il dominio sia un intervallo è essenziale. La funzione $1/x^2$ su $\mathbb R\setminus\{0\}$ ha derivata seconda positiva, ma non è convessa perché il suo dominio non lo è. Per $f:\mathbb R^n\to\mathbb R$ valgono condizioni analoghe, più complesse, che riguardano le derivate parziali seconde e che qui non si enunciano.

### Classificazione di tre funzioni

> [!example] Esempio
> Si classifichino $f(x)=\ln x$ su $(0,\infty)$, $g(x)=x^3$ su $\mathbb R$ e $h(x)=x$ su $\mathbb R$.
>
> La funzione $\ln x$ è concava, anzi strettamente concava, perché $f''(x)=-1/x^2<0$ su tutto $(0,\infty)$.
>
> La funzione $x^3$ non è né convessa né concava su $\mathbb R$: $g''(x)=6x$ cambia segno. Con $\pi=\tfrac12$, la convessità è violata da $x=-2$ e $y=0$, perché $g(-1)=-1$ è maggiore di $\tfrac12\big(g(-2)+g(0)\big)=-4$. La concavità è violata da $x=1$ e $y=2$, perché $g\big(\tfrac32\big)=\tfrac{27}8$ è minore di $\tfrac12\big(g(1)+g(2)\big)=\tfrac92$. Ristretta a $[0,\infty)$, dove $g''\ge0$, è convessa; ristretta a $(-\infty,0]$, dove $g''\le0$, è concava.
>
> La funzione $h(x)=x$ è sia convessa sia concava, ma non strettamente: $h(\pi x+(1-\pi)y)=\pi x+(1-\pi)y=\pi h(x)+(1-\pi)h(y)$, e $h''=0$.

## Ottimizzazione

### Ottimizzazione non vincolata

Sia $f:\mathbb R^n\to\mathbb R$ differenziabile con derivate parziali continue, ipotesi che garantisce la regola della catena lungo una retta. Nel resto del capitolo ogni funzione di cui si calcolano le derivate la soddisfa. Il problema è

$$\max_x f(x).$$

Il **gradiente** di $f$ in $x^*$ è il vettore delle derivate parziali calcolate in $x^*$,

$$\nabla f(x^*):=\left(\frac{\partial f(x)}{\partial x_1},\dots,\frac{\partial f(x)}{\partial x_n}\right)\Bigg|_{x=x^*}.$$

Un punto $x^*$ è un massimo locale se $f(x^*)\ge f(x)$ per ogni $x$ in un intorno di $x^*$, ed è un massimo globale se la disuguaglianza vale per ogni $x\in\mathbb R^n$. La condizione $\nabla f(x^*)=0$ è la **condizione del primo ordine** (FOC, *first-order condition*): in $x^*$ nessuna variabile, spostata da sola, fa crescere $f$ al primo ordine. Il teorema seguente dice quando la condizione è necessaria, quando è sufficiente e che cosa ne segue.

> [!tip] Teorema
> (Condizione del primo ordine.) Sia $f$ differenziabile con derivate parziali continue.
>
> 1. Se $x^*$ è un massimo locale di $f$, allora $\nabla f(x^*)=0$.
> 2. Se $f$ è concava, un punto con $\nabla f(x^*)=0$ è un massimo globale, e ogni massimo locale è globale.
> 3. Se $f$ è strettamente concava, il massimo, se esiste, è unico.
> 4. Se $n=1$ e $f$ è strettamente concava, con $f'(x^*)=0$, allora $f'(x)>0$ per $x<x^*$ e $f'(x)<0$ per $x>x^*$.

La condizione è necessaria per ogni funzione derivabile, ma in generale non basta: $x^3$ ha derivata nulla in $0$ e nessun massimo. Il punto 2 dà un'ipotesi sotto cui basta, la concavità. L'esistenza del massimo non è garantita nemmeno per una funzione strettamente concava: $f(x)=-e^{-x}$ ha $f'(x)=e^{-x}>0$ ovunque, quindi $f$ cresce sempre e non ha massimo.

> [!note] Dimostrazione
> *Punto 1.* Per ogni $i$ la funzione di una variabile $\psi(t)=f(x^*+t\,e_i)$, dove $e_i$ è il vettore con $1$ in posizione $i$ e $0$ altrove, ha un massimo locale in $t=0$ e $\psi'(0)=\partial f(x^*)/\partial x_i$. Per $t$ piccolo il rapporto $(\psi(t)-\psi(0))/t$ è non positivo se $t>0$ e non negativo se $t<0$. Il suo limite per $t\to0$, che è $\psi'(0)$, è quindi sia $\le0$ sia $\ge0$, dunque nullo. Vale per ogni $i$.
>
> *Una disuguaglianza utile.* Se $f$ è concava, per ogni $x,y$ (il punto indica il prodotto scalare)
>
> $$f(y)\ \le\ f(x)+\nabla f(x)\cdot(y-x),$$
>
> cioè il grafico sta sotto il piano tangente. Per $t\in(0,1]$ la concavità dà $f(x+t(y-x))\ge(1-t)f(x)+t\,f(y)$, quindi $\big[f(x+t(y-x))-f(x)\big]/t\ge f(y)-f(x)$. Per $t\to0^+$ il primo membro tende a $\nabla f(x)\cdot(y-x)$ per la differenziabilità di $f$ (ipotesi del teorema), e la disuguaglianza segue. Se $f$ è strettamente concava e $y\ne x$ la disuguaglianza è stretta. Si prenda infatti il punto medio $z=(x+y)/2$: la stretta concavità dà $f(z)>\tfrac12\big(f(x)+f(y)\big)$, mentre la disuguaglianza appena provata, applicata a $x$ e $z$, dà $f(z)\le f(x)+\tfrac12\nabla f(x)\cdot(y-x)$. Confrontando le due relazioni si ottiene $f(y)<f(x)+\nabla f(x)\cdot(y-x)$.
>
> *Punto 2.* Se $\nabla f(x^*)=0$, la disuguaglianza utile con $x=x^*$ dà $f(y)\le f(x^*)$ per ogni $y$: $x^*$ è un massimo globale. Un massimo locale ha gradiente nullo per il punto 1, quindi è globale per quanto appena visto.
>
> *Punto 3.* Un massimo $x^*$ ha gradiente nullo per il punto 1. Se $f$ è strettamente concava, la versione stretta della disuguaglianza dà $f(y)<f(x^*)$ per ogni $y\neq x^*$, quindi nessun altro punto è un massimo.
>
> *Punto 4.* La versione stretta, scritta per $(x,y)$ e per $(y,x)$, dà $f(y)<f(x)+f'(x)(y-x)$ e $f(x)<f(y)+f'(y)(x-y)$. Sommando, $0<\big(f'(x)-f'(y)\big)(y-x)$. Per $x<y$ questo significa $f'(x)>f'(y)$: la derivata è strettamente decrescente. Poiché $f'(x^*)=0$, la derivata è positiva a sinistra di $x^*$ e negativa a destra.

### Ottimizzazione vincolata e teorema di Kuhn-Tucker

Siano $f,g:\mathbb R^n\to\mathbb R$ come nel paragrafo precedente. Il problema vincolato è

$$\max_x f(x)\quad\text{s.t.}\quad g(x)\ge0,$$

dove s.t. sta per *subject to* («soggetto a»). Il vincolo è **attivo** in un punto se $g(x)=0$ e **lasco** se $g(x)>0$. La **Lagrangiana** del problema è $\mathcal L(x,\lambda)=f(x)+\lambda\,g(x)$, e $\lambda$ è il **moltiplicatore** del vincolo.

> [!tip] Teorema
> (Kuhn-Tucker.) Sia $x^*$ un massimo locale del problema, e valga una condizione di qualificazione dei vincoli, per esempio $g$ affine, cioè $g(x)=a\cdot x+b$. Allora esiste un moltiplicatore $\lambda\ge0$ tale che
>
> $$\nabla f(x^*)+\lambda\,\nabla g(x^*)=0,\qquad g(x^*)\ge0,\qquad\lambda\,g(x^*)=0.$$

La prima condizione è la stazionarietà della Lagrangiana rispetto a $x$, $\partial\mathcal L/\partial x=0$. Quando il vincolo è attivo, $\nabla g(x^*)$ punta verso la regione in cui $g$ cresce, cioè verso l'interno dell'insieme ammissibile; la condizione $\nabla f(x^*)=-\lambda\nabla g(x^*)$ con $\lambda\ge0$ dice che $f$ cresce nella direzione opposta, verso l'esterno, e quindi che ogni spostamento ammissibile non può migliorare $f$ al primo ordine. La seconda è l'ammissibilità e coincide con $\partial\mathcal L/\partial\lambda\ge0$, perché $\partial\mathcal L/\partial\lambda=g(x^*)$. La terza è la **condizione di complementarità**: se il vincolo è lasco, $g(x^*)>0$ impone $\lambda=0$ e il vincolo non pesa sull'ottimo, che soddisfa la condizione del primo ordine del problema non vincolato; se $\lambda>0$ il vincolo è attivo e $g(x^*)=0$. Nei testi di ottimizzazione il teorema si chiama anche di Karush-Kuhn-Tucker (KKT).

Con più vincoli $g_j(x)\ge0$, per $j=1,\dots,m$, la Lagrangiana è $\mathcal L=f+\sum_j\lambda_jg_j$ con un moltiplicatore $\lambda_j\ge0$ per ciascun vincolo. La stazionarietà diventa $\nabla f(x^*)+\sum_j\lambda_j\nabla g_j(x^*)=0$, mentre ammissibilità e complementarità valgono vincolo per vincolo: $g_j(x^*)\ge0$ e $\lambda_jg_j(x^*)=0$ per ogni $j$. La qualificazione vale, per esempio, se tutti i $g_j$ sono affini.

Due esempi mostrano perché servono la complementarità e la qualificazione dei vincoli.

> [!example] Esempio
> *Senza complementarità la stazionarietà non basta.* Sia $\max\,-x^2$ con $x+3\ge0$. Nel punto $x=1$ la condizione $-2x+\lambda=0$ è soddisfatta con $\lambda=2\ge0$, ma $g(1)=4>0$, per cui la complementarità richiederebbe $\lambda=0$. Il punto non è un massimo: $f(1)=-1<f(0)=0$.
>
> *Senza qualificazione il teorema è falso.* Sia $\max x$ con $-x^2\ge0$. L'unico punto ammissibile è $x^*=0$, che è quindi il massimo. Lì $f'(x^*)+\lambda g'(x^*)=1+\lambda\cdot0=1\ne0$ per ogni $\lambda$, e la condizione di stazionarietà non è soddisfatta. Il vincolo non è affine e non soddisfa nessuna qualificazione, benché $g(x)=-x^2$ sia concava: la sola concavità del vincolo non garantisce la qualificazione.

Il teorema dà condizioni necessarie. Quando $f$ e $g$ sono concave le stesse condizioni sono anche sufficienti: un punto che le soddisfa con un moltiplicatore $\lambda\ge0$ è un massimo globale del problema vincolato e massimizza $f+\lambda g$ su tutto $\mathbb R^n$, senza vincoli.

> [!tip] Teorema
> Siano $f$ e $g$ concave, e sia $x^*$ un punto con $g(x^*)\ge0$ per cui esiste $\lambda\ge0$ con $\nabla f(x^*)+\lambda\nabla g(x^*)=0$ e $\lambda\,g(x^*)=0$. Allora $x^*$ è un massimo globale del problema vincolato, e massimizza anche la funzione non vincolata $f(x)+\lambda g(x)$.

> [!note] Dimostrazione
> La funzione $\mathcal L(x)=f(x)+\lambda g(x)$ è concava, perché $\lambda\ge0$ e la somma di funzioni concave è concava. Il suo gradiente in $x^*$ è nullo per ipotesi, quindi $x^*$ massimizza $\mathcal L$ su $\mathbb R^n$ per il punto 2 del teorema sulla condizione del primo ordine. Sia ora $x$ ammissibile, cioè con $g(x)\ge0$. Poiché $\lambda g(x)\ge0$ e $\lambda g(x^*)=0$,
>
> $$f(x)\ \le\ f(x)+\lambda g(x)=\mathcal L(x)\ \le\ \mathcal L(x^*)=f(x^*)+\lambda g(x^*)=f(x^*).$$
>
> Nessun punto ammissibile fa meglio di $x^*$.

Il passaggio dal problema vincolato al problema non vincolato su $f+\lambda g$ richiede tre cautele. Il valore di $\lambda$ non è dato: è quello che il teorema di Kuhn-Tucker determina insieme a $x^*$. Senza concavità, $x^*$ può non massimizzare $f+\lambda g$: per $f(x)=x^3$ e $g(x)=1-x$ il massimo vincolato è $x^*=1$, con $\lambda=3$, ma $f+\lambda g=x^3-3x+3$ vale $1$ in $x^*$ e $5$ in $x=2$. Anche con $f$ e $g$ concave, infine, $f+\lambda g$ può avere altri punti di massimo che non risolvono il problema vincolato: per $f(x)=x$ e $g(x)=1-x$ si ha $x^*=1$ e $\lambda=1$, e $f+\lambda g=1$ è costante, per cui la massimizza anche $x=2$, che non rispetta il vincolo. Quando $f$ è strettamente concava e $g$ è concava, $f+\lambda g$ è strettamente concava e $x^*$ ne è l'unico punto di massimo (punto 3 del teorema sulla condizione del primo ordine).

### Esempio: consumo in due periodi

> [!example] Esempio
> Un agente ripartisce la ricchezza totale $W>0$ tra i consumi $x_1$ e $x_2$ di due periodi, senza sconto e senza interesse. Il problema è
>
> $$\max_{x_1,x_2}\ \ln x_1+\ln x_2\quad\text{s.t.}\quad W-x_1-x_2\ge0,$$
>
> con la Lagrangiana $\mathcal L=\ln x_1+\ln x_2+\lambda\,(W-x_1-x_2)$. Il logaritmo richiede $x_1,x_2>0$: i risultati precedenti valgono senza modifiche quando $f$ è definita su un insieme aperto e convesso, come qui il quadrante positivo. Il vincolo è affine, quindi non c'è condizione di qualificazione da verificare.
>
> Le condizioni del primo ordine sono $1/x_1-\lambda=0$ e $1/x_2-\lambda=0$, da cui $x_1=x_2=1/\lambda$. Il moltiplicatore è positivo, perché $\lambda=0$ renderebbe impossibile $1/x_1=0$. Per la complementarità $\lambda\,(W-x_1-x_2)=0$ il vincolo è allora attivo, $x_1+x_2=W$, e quindi
>
> $$x_1=x_2=\frac W2,\qquad\lambda=\frac2W,\qquad\text{valore ottimo}\ \ 2\ln\frac W2.$$
>
> Il punto è un massimo globale: $\ln x_1+\ln x_2$ è concava, perché somma di due funzioni concave, e il vincolo, affine, è concavo: valgono le condizioni sufficienti del teorema precedente. È anche l'unico massimo, perché ogni massimo deve soddisfare le condizioni di Kuhn-Tucker e il sistema ha una sola soluzione. Con $\lambda=2/W$ fissato, la funzione non vincolata $\ln x_1+\ln x_2+\lambda(W-x_1-x_2)$ è massimizzata proprio in $(W/2,\,W/2)$. Per $W=10$ si ottiene $x_1=x_2=5$ e valore ottimo $2\ln5\approx3{,}21888$. Con questa utilità il consumo è uguale nei due periodi.
