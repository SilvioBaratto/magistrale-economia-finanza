---
title: "Economia del Rischio — appello simulato 06: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 06, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
Per $u=W^{1-\gamma}/(1-\gamma)$ le derivate sono $u'=W^{-\gamma}$, $u''=-\gamma W^{-\gamma-1}$, $u'''=\gamma(\gamma+1)W^{-\gamma-2}$, da cui $A=\gamma/W$, $RR=\gamma$, $P=(\gamma+1)/W$. *(ERA 03, «Tre funzioni di utilità di riferimento»; «Le funzioni CARA e CRRA»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
Con $\gamma=3$ è $u(W)=-\dfrac1{2W^2}$ e
$$u'=W^{-3},\qquad u''=-3W^{-4},\qquad u'''=12W^{-5}.$$
Quindi
$$A(W)=\frac{3W^{-4}}{W^{-3}}=\frac3W,\qquad RR(W)=W\,A(W)=3,\qquad P(W)=\frac{12W^{-5}}{3W^{-4}}=\frac4W.$$
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
$A(W)=3/W$, $RR(W)=3$ (costante: l'utilità è CRRA), $P(W)=4/W$.
:::::

::::: {.callout kind="warning" heading="A.1 · Errore tipico"}
Con $\gamma=3$ l'esponente di $u'$ è $-3$ e non $-2$: $u=-1/(2W^2)$ ha $u'=W^{-3}$. Con $RR$ costante l'utilità è CRRA, ma $A=3/W$ non è costante: decresce con $W$.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
L'equivalente certo è il livello di ricchezza certa $CE$ con $u(CE)=E[u(w+X)]$; poiché $E[X]=0$, il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
La ricchezza finale vale $20-15=5$ oppure $20+15=35$, ciascuna con probabilità $1/2$. Con $u(W)=-1/(2W^2)$:
$$E[u(w+X)]=-\frac14\Big(\frac1{5^2}+\frac1{35^2}\Big)=-\frac14\Big(\frac{49}{1225}+\frac1{1225}\Big)=-\frac14\cdot\frac{50}{1225}=-\frac1{98}.$$
Da $u(CE)=-1/(2\,CE^2)=-1/98$ segue $CE^2=49$, cioè $CE=7$ (la radice è presa positiva, perché $W>0$). Il premio è $R=20-7=13$.

La radice è esatta per costruzione: per $\gamma=3$ si ha $CE=\dfrac{w^2-b^2}{\sqrt{w^2+b^2}}$ con $b=15$, e $20^2+15^2=25^2$, quindi $CE=\dfrac{175}{25}=7$.
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
$CE=7$ €, $R=20-7=13$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
$-1/98$ è l'utilità attesa, non l'equivalente certo: va invertita $u$. $CE$ è una ricchezza, non un guadagno: il premio è la differenza $w-CE$.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
Per $k$ piccolo, $R(k)\approx\tfrac12A(w)\,E[X^2]\,k^2$, con $A$ calcolata nella ricchezza iniziale $w$: l'approssimazione è accurata se la lotteria è piccola rispetto alla ricchezza. *(ERA 03, «Il premio per lotterie piccole»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
$A(20)=3/20$ e $E[X^2]=\tfrac12\cdot15^2+\tfrac12\cdot15^2=225$. L'approssimazione è
$$\tfrac12\cdot\frac3{20}\cdot225=\frac{135}8=16{,}875.$$
Il premio esatto di A.2 è $13$: l'approssimazione è maggiore, di $3{,}875$.

Lo scarto non è piccolo perché $b/w=3/4$ non è piccolo (con $b=15$): la formula è lo sviluppo per $k\to0$ e trascura i termini di ordine superiore, che qui pesano; il verso dello scarto dipende da $u$. Con $\gamma=3$ l'approssimazione sovrastima ($16{,}875>13$); per $\ln$ la tabella di ERA 03 mostra il verso opposto.
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
Approssimazione $\tfrac12\cdot\tfrac3{20}\cdot225=135/8=16{,}875$, maggiore del premio esatto $13$ (scarto $3{,}875$). Lo scarto non è piccolo perché $b/w=3/4$ non è piccolo ($b=15$): la formula è lo sviluppo per $k\to0$ e trascura i termini di ordine superiore, che qui pesano; il verso dello scarto dipende da $u$.
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
L'approssimazione usa $A(w)$ nella ricchezza iniziale $w=20$ ($A=3/20$), non nella ricchezza finale; e il confronto è con il premio esatto $R=13$, non con $CE=7$.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
Derivando rispetto a $k$ l'identità $E[u(w+kX)]=u(w-R(k))$ si ottiene $E[X\,u'(w+kX)]+u'(w-R(k))\,R'(k)=0$. *(ERA 03, «Il premio per lotterie piccole»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
Poiché $E[X]=0$, è $E[X]\,u'(w)=0$ e quindi, per $k>0$,
$$u'\big(w-R(k)\big)\,R'(k)=-E\big[X\,u'(w+kX)\big]=-E\Big[X\big(u'(w+kX)-u'(w)\big)\Big].$$
Con $u$ concava, $u'$ non cresce. Se $X>0$ è $w+kX>w$ e $u'(w+kX)-u'(w)\le0$; se $X<0$ la differenza è $\ge0$. In ogni caso $X\big(u'(w+kX)-u'(w)\big)\le0$: il membro di destra è $\ge0$ e, essendo $u'>0$, $R'(k)\ge0$. L'argomento vale per ogni $k$, non solo per $k$ piccolo.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
Derivando: $u'(w-R)\,R'=-E[X(u'(w+kX)-u'(w))]$ ($E[X]=0$); con $u'$ non crescente ogni termine $X(u'(w+kX)-u'(w))$ è $\le0$, quindi $R'\ge0$.
:::::

::::: {.callout kind="warning" heading="A.4 · Errore tipico"}
L'approssimazione quadratica $\tfrac12A\,E[X^2]\,k^2$ cresce con $k$, ma vale solo per $k$ piccolo: non dimostra la monotonia per ogni $k$ (A.3 mostra che per $k$ grande non è affidabile).
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
L'agente è indifferente fra accettare e rifiutare se l'utilità attesa della ricchezza aleatoria uguaglia quella della ricchezza certa, $E[u(w+X)]=u(w)$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Con $u=\ln$: $\theta\ln120+(1-\theta)\ln15=\ln30$, cioè $\theta\,(\ln120-\ln15)=\ln30-\ln15$, ovvero
$$\theta\ln8=\ln2\quad\Longrightarrow\quad\theta=\frac{\ln2}{3\ln2}=\frac13.$$
Controllo con potenze intere: $120^{1}\cdot15^{2}=27000=30^{3}$.
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
$\theta=1/3$.
:::::

::::: {.callout kind="warning" heading="B.1 · Errore tipico"}
Indifferenza significa $E[u(w+X)]=u(w)$, non $E[X]=0$: un agente strettamente avverso al rischio accetta una scommessa solo se il suo valore atteso è positivo.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
Se $E[u(w+X)]=u(w)$ allora $CE=w$. Con $E[X]\neq0$ il premio è la ricchezza attesa meno $CE$. Per $u$ strettamente concava e $X$ non degenere, Jensen è stretta: $E[u(w+X)]<u(E[w+X])$. *(ERA 03, «Equivalente certo e premio per il rischio»; «Avversione al rischio e concavità»)* *(ERA 07, «Il benchmark: informazione perfetta»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
$E[X]=\tfrac13\cdot90-\tfrac23\cdot15=30-10=20$. All'indifferenza $E[\ln(w+X)]=\ln w$, quindi $CE=w=30$. La ricchezza attesa è $E[w+X]=50$ e il premio è $R=50-30=20$: coincide con $E[X]$, perché $CE=w$.

Perché $E[X]>0$: per Jensen stretta, $u(w)=E[u(w+X)]<u\big(w+E[X]\big)$; poiché $u$ è crescente, $w<w+E[X]$, cioè $E[X]>0$. Con $E[X]\le0$ l'agente rifiuterebbe.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
$E[X]=20$ €, $CE=30$ €, $R=50-30=20$ €. $E[X]>0$ perché $u$ è strettamente concava: per Jensen $u(w)=E[u(w+X)]<u(w+E[X])$, e $u$ crescente dà $E[X]>0$.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
Con $E[X]\neq0$ il premio non è $w-CE$: quella differenza qui vale $30-30=0$. Il premio è la ricchezza attesa meno l'equivalente certo, $E[w+X]-CE$.
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
Con ricchezza $2w=60$ l'agente accetta se $E[\ln(60+X)]>\ln60$. Elevando alla terza (il denominatore di $\theta$) il confronto si fa con numeri interi. *(ERA 03, «L'effetto ricchezza»; «Condizioni equivalenti per il DARA»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
La ricchezza finale è $60+90=150$ con probabilità $1/3$ oppure $60-15=45$ con probabilità $2/3$. Accetta se
$$\tfrac13\ln150+\tfrac23\ln45>\ln60\iff150\cdot45^2>60^3.$$
Si ha $150\cdot45^2=303750$ e $60^3=216000$ (in unità di 15: $10\cdot3^2=90$ contro $4^3=64$), con rapporto $1{,}406$. L'utilità attesa supera quella della ricchezza certa di $\tfrac13\ln1{,}406=0{,}1136$: l'agente accetta. Con $w=30$ valeva l'uguaglianza, $120\cdot15^2=30^3=27000$.
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
Accetta: $E[\ln(60+X)]>\ln60$ equivale a $150\cdot45^2=303750>60^3=216000$.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
«Più ricco, quindi accetta» senza motivazione non basta: via diretta, il confronto con potenze intere (si eleva alla terza per togliere i logaritmi); via teorica, la DARA stretta di $\ln$ (B.4). Il $\theta$ è lo stesso $1/3$ di B.1.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
Il premio per il rischio di una lotteria a media nulla non cresce con la ricchezza se $u$ è DARA ($A'\le0$) e decresce strettamente se $A'<0$; con la CARA non dipende dalla ricchezza. *(ERA 03, «Condizioni equivalenti per il DARA»; «Classificare le tre utilità di riferimento»)*
:::::

::::: {.callout kind="example" heading="B.4 · Svolgimento"}
ERA 03 enuncia l'effetto ricchezza per lotterie a media nulla, mentre qui $E[X]=20\neq0$. Si scrive quindi $X=E[X]+Y$ con $E[Y]=0$ (qui $Y$ vale $70$ o $-35$) e si applica la nota a $Y$, indicando con $R_Y(v)$ il suo premio a ricchezza $v$, definito da $E[u(v+Y)]=u(v-R_Y(v))$. A ricchezza $w'$ la scommessa si accetta se $E[u(w'+E[X]+Y)]\ge u(w')$, cioè $w'+E[X]-R_Y(w'+E[X])\ge w'$, cioè $R_Y(w'+E[X])\le E[X]$. Con $w'=30$ vale l'uguaglianza (indifferenza: $R_Y(50)=E[X]=20$, come in B.2).

Per $\ln$ è $A(W)=1/W$ e $A'(W)=-1/W^2<0$: DARA in senso stretto, e secondo la nota il premio di $Y$ è strettamente decrescente nella ricchezza $v$. Con $w'=2w=60$ è $v=80>50$, quindi $R_Y(80)<R_Y(50)=E[X]$ e l'agente accetta, come in B.3.

Per un agente CARA, con $u(W)=-\exp(-\rho W)/\rho$, è $u(w+x)=\exp(-\rho w)\,u(x)$: il segno di $E[u(w+X)]-u(w)$ non dipende da $w$. Se è indifferente a $w$, lo è anche a $2w$: il premio non dipende dalla ricchezza e non c'è effetto ricchezza.
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
DARA, in senso stretto: per $\ln$ è $A(W)=1/W$ decrescente, quindi il premio per il rischio cala con la ricchezza e a $2w$ pesa meno del guadagno atteso. Un agente CARA, indifferente a $w$, resta indifferente a $2w$: il suo premio non dipende dalla ricchezza.
:::::

::::: {.callout kind="warning" heading="B.4 · Errore tipico"}
La CARA è DARA solo in senso debole ($A'=0$): non dà un effetto ricchezza. La decisione cambia con $\ln$, strettamente DARA, e non con una CARA.
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$p$ domina $q$ al primo ordine se la c.d.f. di $p$ sta sotto quella di $q$ in ogni punto; solo allora ogni utilità crescente preferisce $p$. Una media maggiore non basta. *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Le c.d.f. nei premi $10$, $30$, $70$ sono
$$\text{c.d.f. di }p:\ (0{,}1;\ 0{,}7;\ 1),\qquad\text{c.d.f. di }q:\ (0{,}4;\ 0{,}6;\ 1).$$
In $10$ la c.d.f. di $p$ è sotto ($0{,}1<0{,}4$), in $30$ è sopra ($0{,}7>0{,}6$): si incrociano, quindi nessuna delle due domina l'altra al primo ordine. Le medie sono $E[p]=40>E[q]=38$, ma non basta. Due utilità crescenti ordinano le lotterie in modo opposto: con $u(x)=\mathbf 1_{\{x>10\}}$ si preferisce $p$ (probabilità $0{,}9$ contro $0{,}6$ di superare 10), con $u(x)=\mathbf 1_{\{x>30\}}$ si preferisce $q$ ($0{,}4$ contro $0{,}3$ del premio $70$).
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
No: le c.d.f. si incrociano, $(0{,}1;\,0{,}7;\,1)$ per $p$ e $(0{,}4;\,0{,}6;\,1)$ per $q$, quindi nessuna domina l'altra al primo ordine. La media maggiore di $p$ ($40>38$) non basta.
:::::

::::: {.callout kind="warning" heading="C.1 · Errore tipico"}
Né le medie né la probabilità del premio più alto decidono: la FOSD si legge sulle c.d.f. in ogni punto.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
$p$ domina $q$ al secondo ordine se $\int_{10}^{x}F_p\le\int_{10}^{x}F_q$ per ogni $x$; allora ogni $u$ crescente e concava preferisce $p$. La SOSD non richiede medie uguali, mentre un *mean-preserving spread* le conserva. *(ERA 04, «Dominanza stocastica del secondo ordine»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Gli integrali delle c.d.f. a partire dal premio $10$, nei premi $10$, $30$, $70$, sono
$$p:\ \Big(0;\ 20\cdot0{,}1=2;\ 2+40\cdot0{,}7=30\Big),\qquad q:\ \Big(0;\ 20\cdot0{,}4=8;\ 8+40\cdot0{,}6=32\Big).$$
L'integrale di $p$ non supera mai quello di $q$ ($0\le0$, $2<8$, $30<32$): $p$ domina $q$ al secondo ordine. Gli ultimi valori sono $70-E[p]=30$ e $70-E[q]=32$: le medie sono diverse ($40$ e $38$), quindi nessuna delle due è un *mean-preserving spread* dell'altra e la dominanza è solo del secondo ordine.

Con $u$ strettamente crescente e concava la preferenza per $p$ è anche stretta:
$$E_p[u]-E_q[u]=0{,}3\,[u(30)-u(10)]-0{,}1\,[u(70)-u(30)]\ \ge\ 0{,}1\,[u(30)-u(10)]>0,$$
perché la concavità dà $u(70)-u(30)\le2\,[u(30)-u(10)]$ (la pendenza su $[30,70]$, lungo $40$, non supera quella su $[10,30]$, lungo $20$).
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
$p$: gli integrali delle c.d.f. nei premi 10, 30, 70 sono $0,\,2,\,30$ per $p$ e $0,\,8,\,32$ per $q$, mai maggiori per $p$, quindi $p$ domina $q$ al secondo ordine (medie diverse) e un agente avverso la preferisce.
:::::

::::: {.callout kind="warning" heading="C.2 · Errore tipico"}
Non cercare un *mean-preserving spread*: con medie diverse non può esistere. Basta la condizione sugli integrali delle c.d.f.
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
Se $E[\tilde\varepsilon\mid x]=0$ per ogni $x$, la lotteria $x+\tilde\varepsilon$ è un *mean-preserving spread* di quella di $x$ e viene dominata al secondo ordine: ogni $u$ crescente e concava preferisce la lotteria meno dispersa. *(ERA 04, «Il *mean-preserving spread*»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
$E[p']=\dfrac{2\cdot10+3\cdot30+1\cdot70}6=30$, il premio intermedio. La lotteria composta è $q'=\tfrac12p'+\tfrac12c=(1/6;\ 3/4;\ 1/12)$.

Da $q'$ si ottiene $p'$ lasciando fermi i premi $10$ e $70$ e spargendo la probabilità $3/4$ del premio $30$ su $10$, $30$, $70$ con probabilità condizionate $2/9$, $2/3$, $1/9$. Il rumore ha media condizionata nulla: $\tfrac29(-20)+\tfrac19(40)=0$. Le probabilità finali sono $\tfrac16+\tfrac34\cdot\tfrac29=\tfrac13$, $\tfrac34\cdot\tfrac23=\tfrac12$, $\tfrac1{12}+\tfrac34\cdot\tfrac19=\tfrac16$: quelle di $p'$. Quindi $p'$ è un *mean-preserving spread* di $q'$. Lo conferma il confronto degli integrali delle c.d.f. nei premi $10$, $30$, $70$: $(0;\ 10/3;\ 40)$ per $q'$ e $(0;\ 20/3;\ 40)$ per $p'$, con medie uguali.

Per via diretta, con $u$ strettamente concava: $E_{p'}[u]=\tfrac12\big[\tfrac23u(10)+\tfrac13u(70)\big]+\tfrac12u(30)$ e, poiché $30=\tfrac23\cdot10+\tfrac13\cdot70$, vale $\tfrac23u(10)+\tfrac13u(70)<u(30)$. Quindi $E_{p'}[u]<u(30)$ e $E_{q'}[u]=\tfrac12E_{p'}[u]+\tfrac12u(30)>E_{p'}[u]$.
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
$q'$: $p'$ ha media 30 ed è un *mean-preserving spread* di $q'$, che mette metà della probabilità sui 30 € certi; quindi $q'$ domina $p'$ al secondo ordine e un agente strettamente avverso la preferisce.
:::::

::::: {.callout kind="warning" heading="C.3 · Errore tipico"}
Le medie coincidono (30): la FOSD è esclusa e la preferenza viene dalla concavità, non dal valore atteso. Con $u$ convessa l'ordine si invertirebbe.
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
L'utilità attesa è lineare nelle combinazioni di lotterie, $U\big(\alpha L^a+(1-\alpha)L^b\big)=\alpha U(L^a)+(1-\alpha)U(L^b)$; l'indipendenza dice che le preferenze fra due lotterie non cambiano se si combinano entrambe con una terza. *(ERA 02, «Preferenze e utilità attesa»)* *(ERA 02, «Gli assiomi»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
Per ipotesi $U(p')=U(c)$, con $c$ i 30 € certi. Per linearità
$$U(q')=\tfrac12U(p')+\tfrac12U(c)=\tfrac12U(p')+\tfrac12U(p')=U(p').$$
Con l'indipendenza: da $p'\sim c$ segue $\tfrac12p'+\tfrac12c\sim\tfrac12c+\tfrac12c=c\sim p'$. La concavità di $u$ non interviene.
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
Indifferente: per la linearità dell'utilità attesa $U(q')=\tfrac12U(p')+\tfrac12U(c)=U(p')$, perché $U(c)=U(p')$. Non serve la concavità.
:::::

::::: {.callout kind="warning" heading="C.4 · Errore tipico"}
Non è la stessa risposta di C.3: lì $u$ è strettamente concava e $q'$ è strettamente preferita; qui l'indifferenza fra $p'$ e i 30 € certi esclude la stretta concavità (con $u$ strettamente concava e $E[p']=30$ si avrebbe $c\succ p'$).
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
Con $u=\ln$ è $u'(z)=1/z$, quindi $1/u'(z_l)=z_l$ e la (5) diventa $z_l=\lambda+\beta(1-r_l)$. Con $B_0=0$ si ha $z_0=w-p$. *(ERA 08, «Lagrangiana e condizioni del primo ordine»)* *(ERA 08, «Che cosa significa il risultato»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
Dalla (5), $z_l=w-p-l+B_l=\lambda+\beta(1-r_l)$ per ogni $l$. Per $l=0$, con $B_0=0$, è $z_0=w-p=\lambda+\beta(1-r_0)$ (da cui anche $p=w-\lambda-\beta\,(1-r_0)$, non richiesto). Sottraendo la relazione per $l=0$ da quella per $l$,
$$B_l-l=z_l-z_0=\beta(1-r_l)-\beta(1-r_0)=-\beta\,(r_l-r_0),\qquad l-B_l=\beta\,(r_l-r_0).$$
Rapporti: $r_0=\dfrac{3/10}{6/10}=\dfrac12$, $r_1=\dfrac{3/10}{3/10}=1$, $r_2=\dfrac{4/10}{1/10}=4$. Sono strettamente crescenti (MLR) e $r_0<1<r_2$. Franchigia: per $l=1$ è $\beta\big(1-\tfrac12\big)=\tfrac\beta2$; per $l=2$ è $\beta\big(4-\tfrac12\big)=\tfrac{7\beta}2$. Si assume $\lambda>3\beta$, così che $1/u'(z_l)=\lambda+\beta(1-r_l)>0$ per ogni $l$ ($r_l\le4$).

Verifica (script) con $\lambda=4$, $\beta=\tfrac12$, $w=20$: $p=63/4$ e $B=(0;\ 3/4;\ 1/4)$, e la (5) è soddisfatta per ogni $l$.
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
$B_l-l=-\beta\,(r_l-r_0)$. Dalla tabella: $r_0=1/2$, $r_1=1$, $r_2=4$. Franchigia $l-B_l=\beta\,(r_l-r_0)$: $\beta/2$ per $l=1$ e $7\beta/2$ per $l=2$.
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
$B_l-l$ si ricava dalla differenza $z_l-z_0$, non dal solo $z_l$: la costante $w-p$ dipende dalla normalizzazione $B_0=0$. Senza di essa la soluzione è unica solo a meno di una traslazione di $p$ e di tutti i $B_l$.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
$r_l=\pi_l(0)/\pi_l(1)$ misura quanto la perdita $l$ è più probabile con l'impegno basso che con l'alto: indica più probabilmente $e=0$ se $r_l>1$. Con $\beta>0$ il vincolo IC è attivo: il cliente è indifferente fra $e=1$ e $e=0$. *(ERA 08, «Che cosa significa il risultato»)* *(ERA 08, «La proprietà del rapporto di verosimiglianza monotono»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
La compagnia osserva soltanto la perdita, che è il solo canale attraverso cui il compenso può dipendere, indirettamente, dall'impegno. La polizza premia con ricchezza più alta le perdite che indicano più probabilmente un impegno alto ($r_l$ basso) e penalizza quelle che indicano più probabilmente un impegno basso ($r_l$ alto).

Non è sfiducia: in equilibrio la compagnia sa che il cliente sceglie $e=1$. Il legame serve a far valere IC. Il vantaggio atteso in utilità dell'impegno alto, $\sum_l[\pi_l(1)-\pi_l(0)]\,u(z_l)$, deve eguagliare il suo costo $d(1)-d(0)>0$: con $z_l$ costante sarebbe nullo e il cliente sceglierebbe $e=0$ (per questo $\beta=0$ è impossibile). Facendo scendere $z_l$ dove $r_l$ è alto, la deviazione a $e=0$ sposta probabilità verso le perdite con ricchezza bassa e non conviene più.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
La compagnia osserva solo la perdita, e $r_l$ alto indica che $l$ è più probabile con impegno basso. Legare $z_l$ a $r_l$ rende l'impegno alto vantaggioso (IC): deviare a $e=0$ sposta probabilità sulle perdite con ricchezza bassa. Non è sfiducia: IC è attivo e il cliente è indifferente.
:::::

::::: {.callout kind="warning" heading="D.2 · Errore tipico"}
La ricchezza bassa non è una sanzione per chi ha deviato: in equilibrio $e=1$ è noto. Serve a togliere ogni vantaggio alla deviazione, non a punirla.
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
Azzardo morale (*hidden action*): il principale non osserva un'azione dell'agente scelta dopo la stipula. Selezione avversa (*hidden information*): il principale non conosce una caratteristica dell'agente già presente alla stipula. *(ERA 08, «L'azzardo morale»)* *(ERA 07, «Informazione imperfetta e asimmetrie informative»)*
:::::

::::: {.callout kind="example" heading="D.3 · Svolgimento"}
(i) Abitare in un quartiere con molti furti è una caratteristica del richiedente, già presente alla stipula e non scelta dopo, nota a lui e non alla compagnia: informazione nascosta, quindi selezione avversa (a premio unico comprano soprattutto i più esposti).

(ii) L'accensione dei bruciatori è un'azione scelta dopo la stipula, che la compagnia non può verificare e che cambia la probabilità del danno: azione nascosta, quindi azzardo morale (con il rimborso pieno il frutticoltore non ricava vantaggio dal sostenerne il costo).
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
(i) Selezione: il quartiere in cui abita il richiedente è una caratteristica nascosta, già presente alla stipula e non scelta dopo. (ii) Azzardo: i bruciatori sono un'azione scelta dopo la stipula, che la compagnia non osserva e che cambia la probabilità del danno.
:::::

::::: {.callout kind="warning" heading="D.3 · Errore tipico"}
Non basta che l'informazione sia nascosta: conta l'oggetto e il momento. In (i) è una caratteristica già presente alla stipula e non scelta dopo; in (ii) è un'azione scelta dopo. Dove si tiene la bicicletta di notte sarebbe invece un comportamento scelto dopo la stipula: azzardo morale.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
Con l'imposta una posizione $\alpha$ rende $(1-\tau)\,\alpha\tilde x$ al posto di $\alpha\tilde x$: l'obiettivo è $V$ valutata in $\alpha(1-\tau)$. *(ERA 05, «Tassazione e sussidi dei rendimenti»)* *(ERA 05, «La condizione del primo ordine»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
Poiché è tassato solo il rendimento in eccesso, $w_0$ non cambia e il nuovo problema è
$$\max_{\alpha\in[0,W]}E\big[u\big(w_0+\alpha(1-\tau)\tilde x\big)\big]=\max_{\alpha\in[0,W]}V\big(\alpha(1-\tau)\big).$$
La condizione del primo ordine (soluzione interna) è
$$(1-\tau)\,E\big[\tilde x\,u'\big(w_0+\alpha(1-\tau)\tilde x\big)\big]=0\iff V'\big(\alpha(1-\tau)\big)=0,$$
dividendo per $1-\tau>0$. Poiché $V$ è strettamente concava, $V'$ si annulla solo in $\alpha^*$: $\alpha(1-\tau)=\alpha^*$, cioè $\alpha=\dfrac{\alpha^*}{1-\tau}>\alpha^*$. La funzione obiettivo è ancora strettamente concava in $\alpha$, per cui con il vincolo $\alpha\le W$ l'ammontare investito nel titolo rischioso, al lordo dell'imposta, è
$$\min\Big\{\frac{\alpha^*}{1-\tau},\,W\Big\}.$$
Con $\alpha^*=56$ e $W=120$: per $\tau=\tfrac18$ è $\dfrac{56}{7/8}=64<120$, mentre l'esposizione netta $\alpha(1-\tau)$ resta $56$.

Osservazione, non richiesta: il vincolo è attivo se $\dfrac{\alpha^*}{1-\tau}\ge W$, cioè $\tau\ge1-\dfrac{\alpha^*}{W}=1-\dfrac{56}{120}=\dfrac8{15}\approx0{,}533$. Per $\tau=\tfrac34$ sarebbe $\dfrac{56}{1/4}=224>120$, quindi l'investimento è $120$.

Controllo (script): $u=\ln$, $r=1/20$, $W=120$ ($w_0=126$), rendimenti netti $-2/5$ e $+4/5$ equiprobabili, che danno $\alpha^*=56$: l'ottimo con imposta è $64$ per $\tau=\tfrac18$ e $120$ per $\tau=\tfrac34$.
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
Nuovo problema $\max_{\alpha\in[0,W]}E[u(w_0+(1-\tau)\alpha\tilde x)]$, con FOC $(1-\tau)E[\tilde x\,u'(w_0+(1-\tau)\alpha\tilde x)]=0$, risolta da $(1-\tau)\alpha=\alpha^*$. Ammontare investito, al lordo dell'imposta: $\min\{\alpha^*/(1-\tau),W\}$. Con $\alpha^*=56$, $W=120$ e $\tau=1/8$: $56/(7/8)=64$ (l'esposizione netta $\alpha(1-\tau)$ resta $56$).
:::::

::::: {.callout kind="warning" heading="E.1 · Errore tipico"}
Il vincolo $\alpha\le W$ riguarda l'ammontare investito, non $(1-\tau)\alpha$: l'imposta con sussidio consente un'esposizione maggiore, ma non più budget. Se fosse tassato anche l'interesse sul titolo privo di rischio, $w_0$ calerebbe e l'esito dipenderebbe dai casi: qui è escluso dall'ipotesi. Non confondere $\alpha$ con $\alpha(1-\tau)$: l'ammontare investito è $64$, non $56$.
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
Una funzione strettamente concava su $[0,W]$ ha il massimo determinato dal segno della derivata: in $0$ se $V'(0)\le0$, in $W$ se $V'(W)\ge0$, altrimenti nell'unica radice di $V'$. FOSD: $F_2$ domina $F_1$ se $F_2(x)\le F_1(x)$ per ogni $x$. *(ERA 05, «La condizione del primo ordine»; «Il risultato»)* *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*(a) Ottimo invariato.* Per $\tilde y$ la derivata è
$$\hat V'(\alpha)=s\,E\big[\tilde x\,u'(w_0+\alpha\tilde x)\big]+(1-s)\cdot0\cdot u'(w_0)=s\,V'(\alpha).$$
Ha lo stesso segno di $V'(\alpha)$ per ogni $\alpha$, e $\hat V$ è strettamente concava ($\mathbb P(\tilde y\neq0)=s\,\mathbb P(\tilde x\neq0)>0$). Le condizioni di bordo e la radice interna dipendono solo da questo segno: $\hat V'(0)\le0\iff V'(0)\le0$, $\hat V'(W)\ge0\iff V'(W)\ge0$, e la radice è la stessa. Quindi $\hat\alpha=\alpha^*$. Esempio (script): $u=\ln$, $r=\tfrac1{20}$, $W=120$, rendimenti netti $-\tfrac25$ e $+\tfrac45$ equiprobabili, $s=\tfrac12$: $\alpha^*=56$ e anche $\hat\alpha=56$.

*(b) Primo ordine con $\tilde x>0$.* Con $\tilde x>0$ è $F(x)=0$ per $x\le0$. La variabile $\tilde y$ vale $0$ con probabilità $1-s$ e $\tilde x$ con probabilità $s$:
$$G(x)=0\ \ (x<0),\qquad G(x)=(1-s)+s\,F(x)\ \ (x\ge0).$$
Allora $G(x)-F(x)=(1-s)\big(1-F(x)\big)\ge0$ per ogni $x$: $F(x)\le G(x)$, cioè la distribuzione di $\tilde x$ domina quella di $\tilde y$ al primo ordine. Eppure l'investimento non diminuisce: con $\tilde x>0$ è $V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]>0$ per ogni $\alpha$, quindi $\alpha^*=W$, e $\hat V'=s\,V'>0$ dà $\hat\alpha=W$. Esempio (script): $\tilde x\in\{\tfrac15,\tfrac35\}$ equiprobabili, $s=\tfrac12$; nei punti $0$, $\tfrac15$, $\tfrac35$ si ha $F=(0;\ \tfrac12;\ 1)$ e $G=(\tfrac12;\ \tfrac34;\ 1)$, e la pendenza in $W$ è positiva per entrambe.

*(c) Si annulla il rendimento netto.* Se $\tilde x_0$ è sostituito da una variabile che vale $\tilde x_0$ con probabilità $s$ e $0$ con probabilità $1-s$, il rendimento in eccesso $\tilde y'$ vale $\tilde x$ con probabilità $s$ e $0-r=-r$ con probabilità $1-s$:
$$\hat V'(\alpha)=s\,V'(\alpha)+(1-s)\,(-r)\,u'(w_0-\alpha r).$$
In un $\alpha^*$ interno $V'(\alpha^*)=0$, quindi
$$\hat V'(\alpha^*)=-(1-s)\,r\,u'(w_0-\alpha^*r)<0,$$
perché $r>0$ e $u'>0$ ($w_0-\alpha^*r\ge W>0$). $\hat V$ è strettamente concava e ha derivata negativa in $\alpha^*$: il massimo sta a sinistra, $\hat\alpha<\alpha^*$. L'investimento diminuisce. Esempio (script, stessi dati di (a)): $\hat V'(\alpha^*)=-(1-s)\,r/(w_0-\alpha^*r)=-0{,}000203$ e il nuovo ottimo è $35{,}9623<56$.
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
(a) $\hat V'(\alpha)=s\,V'(\alpha)$ ha il segno di $V'(\alpha)$ e $\hat V$ è strettamente concava: stesso massimo, $\hat\alpha=\alpha^*$. (b) $G(x)=(1-s)+sF(x)$ per $x\ge0$ e $0$ per $x<0$: $G\ge F$, quindi $\tilde x$ domina $\tilde y$ al primo ordine; ma $V'>0$ e $\hat V'>0$, e l'investimento è $W$ in entrambi i casi. (c) $\hat V'(\alpha^*)=-(1-s)\,r\,u'(w_0-\alpha^*r)<0$: $\hat\alpha<\alpha^*$, l'investimento diminuisce.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
Conta quale variabile si annulla. Se è il rendimento in eccesso $\tilde x$ l'investimento non cambia (a); se è il rendimento netto $\tilde x_0$ con $r>0$, l'eccesso diventa $-r<0$ e l'investimento scende (c). La dominanza di (b) ordina le utilità attese, non l'ammontare investito.
:::::
