---
title: "Economia del Rischio — appello simulato 02: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 02, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
$A=-u''/u'$, $RR=W\,A$, $P=-u'''/u''$. Vale $A'(W)=A(W)\,[A(W)-P(W)]$: con $A>0$ l'utilità è DARA se e solo se $P\ge A$. «Più avverso» è un confronto debole: $A_2(W)\ge A_1(W)$ per ogni $W$. *(ERA 03, «Avversione assoluta e avversione relativa»; «Prudenza e avversione assoluta»; «Condizioni equivalenti per il DARA»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
Agente 1, $u_1=\sqrt W$:
$$u_1'=\tfrac12W^{-1/2},\quad u_1''=-\tfrac14W^{-3/2},\quad u_1'''=\tfrac38W^{-5/2},$$
$$A_1=\frac{\tfrac14W^{-3/2}}{\tfrac12W^{-1/2}}=\frac1{2W},\qquad RR_1=W\,A_1=\frac12,\qquad P_1=\frac{\tfrac38W^{-5/2}}{\tfrac14W^{-3/2}}=\frac3{2W}.$$
Agente 2, $u_2=\ln W$: $u_2'=1/W$, $u_2''=-1/W^2$, $u_2'''=2/W^3$, quindi
$$A_2=\frac1W,\qquad RR_2=1,\qquad P_2=\frac2W.$$
Confronto: $A_2-A_1=\dfrac1{2W}>0$ per ogni $W>0$. DARA: $P_1-A_1=\dfrac1W>0$ e $P_2-A_2=\dfrac1W>0$, quindi $A_1'=A_1(A_1-P_1)=-\dfrac1{2W^2}<0$ e $A_2'=A_2(A_2-P_2)=-\dfrac1{W^2}<0$.
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
Agente 1: $A_1(W)=1/(2W)$, $RR_1=1/2$, $P_1(W)=3/(2W)$. Agente 2: $A_2(W)=1/W$, $RR_2=1$, $P_2(W)=2/W$. L'agente 2 è più avverso: $A_2-A_1=1/(2W)\ge0$ per ogni $W$. Entrambi sono DARA: $P>A$ ($3/(2W)>1/(2W)$ e $2/W>1/W$), cioè $A'<0$.
:::::

::::: {.callout kind="warning" heading="A.1 · Errore tipico"}
Con $RR$ costante le due utilità sono CRRA, non CARA: $A$ non è costante, e infatti decresce con $W$. Il segno di $A'=A\,(A-P)$ è opposto a quello di $P-A$: $P>A$ vuol dire $A$ decrescente.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
L'equivalente certo è il livello di ricchezza certa $CE$ con $u(CE)=E[u(w+X)]$; poiché $E[X]=0$, il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
La ricchezza finale vale $w-20=9=3^2$ oppure $w+20=49=7^2$, ciascuna con probabilità $1/2$.

Agente 1: $E[u_1]=\tfrac12(\sqrt9+\sqrt{49})=\tfrac12(3+7)=5$. Da $\sqrt{CE_1}=5$ segue $CE_1=25$, quindi $R_1=29-25=4$.

Agente 2: $E[u_2]=\tfrac12(\ln9+\ln49)=\ln(3\cdot7)=\ln21$, quindi $CE_2=21$ e $R_2=29-21=8$.
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
Agente 1: $CE_1=25$ €, $R_1=4$ €. Agente 2: $CE_2=21$ €, $R_2=8$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
Per $u_1=\sqrt W$ l'equivalente certo non è $E[u_1]=5$: bisogna invertire $u_1$, cioè elevare al quadrato, $CE_1=5^2=25$. $CE$ è una ricchezza, non un guadagno: il premio è la differenza $w-CE$.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
Se $u_2=\phi\circ u_1$, derivando due volte si ottiene $\phi''(u_1)=\dfrac{u_2'}{(u_1')^2}\,[A_1-A_2]$: il fattore $u_2'/(u_1')^2$ è positivo, quindi $\phi''$ ha il segno di $A_1-A_2$. *(ERA 03, «La trasformazione concava»; «Avversione assoluta e avversione relativa»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
Posto $x=u_1(W)=\sqrt W$ si ha $W=x^2$ e $u_2=\ln(x^2)=2\ln x$, quindi
$$\phi(x)=2\ln x,\qquad\phi'(x)=\frac2x,\qquad\phi''(x)=-\frac2{x^2}<0.$$
Valutata in $x=u_1(W)=\sqrt W$: $\phi''(u_1(W))=-\dfrac2W$ (per $W=4$ vale $-0{,}5$).

Secondo membro: $u_2'=1/W$ e $(u_1')^2=1/(4W)$, quindi $u_2'/(u_1')^2=4$; $A_1-A_2=\dfrac1{2W}-\dfrac1W=-\dfrac1{2W}$. Il prodotto è $4\cdot\left(-\dfrac1{2W}\right)=-\dfrac2W$, uguale al primo membro.
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
$\phi(x)=2\ln x$, $\phi''(x)=-2/x^2$ (negativa: $\phi$ è concava). La formula è verificata: entrambi i membri valgono $-2/W$.
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
Il segno di $\phi''$ è quello di $A_1-A_2$, non di $A_2-A_1$: l'agente più avverso è quello con $A$ maggiore, e per lui $\phi$ è concava, cioè $\phi''<0$.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
Se $u_2=\phi\circ u_1$ con $\phi$ concava, la disuguaglianza di Jensen, applicata a $\phi$ e alla variabile $u_1(w+X)$, dà $R_2\ge R_1$ per ogni $w$ e ogni $X$ con $E[X]=0$. *(ERA 03, «Dalla trasformazione concava al premio per il rischio»; «La disuguaglianza di Jensen»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
Per A.3, $u_2=\phi\circ u_1$ con $\phi=2\ln$ concava. Dalle definizioni di $R_2$ e $R_1$:
$$u_2(w-R_2)=E[\phi(u_1(w+X))]\ \le\ \phi\big(E[u_1(w+X)]\big)=\phi\big(u_1(w-R_1)\big)=u_2(w-R_1).$$
La disuguaglianza è quella di Jensen, usata una volta sola. Poiché $u_2$ è strettamente crescente, $w-R_2\le w-R_1$, cioè $R_2\ge R_1$. Con i dati di A.2: $8\ge4$.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
Sì. Per A.3 $u_2=\phi\circ u_1$ con $\phi=2\ln$ concava, quindi per Jensen $u_2(w-R_2)=E[\phi(u_1(w+X))]\le\phi(E[u_1(w+X)])=u_2(w-R_1)$. Con $u_2$ crescente segue $R_2\ge R_1$, per ogni $w$ e ogni $X$ con $E[X]=0$.
:::::

::::: {.callout kind="warning" heading="A.4 · Errore tipico"}
Il confronto numerico di A.2 ($8>4$) vale per una sola coppia $(w,X)$: non dimostra l'ordine per ogni ricchezza e ogni lotteria. Serve la relazione fra le utilità (qui $u_2=\phi\circ u_1$ con $\phi$ concava) o, in modo equivalente, $A_2(W)\ge A_1(W)$ per ogni $W$.
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
All'equilibrio $\alpha=1$ la ricchezza è $\tilde y$ e la condizione del primo ordine dà $P=\dfrac{E[\tilde y\,u'(\tilde y)]}{R_f\,E[u'(\tilde y)]}$. Il premio al rischio di mercato è $\phi=R-R_f$, con $R=E[\tilde y]/P$. *(ERA 06, «L'offerta e il prezzo di equilibrio»; «Il premio al rischio di mercato»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Con $u=\ln$ si ha $u'(\tilde y)=1/\tilde y$ e $\tilde y\,u'(\tilde y)=1$ in entrambi gli stati. Quindi
$$E[u'(\tilde y)]=\tfrac12\Big(\tfrac12+\tfrac13\Big)=\frac5{12},\qquad P=\frac{1}{1\cdot 5/12}=\frac{12}5=2{,}4.$$
Poi $E[\tilde y]=\tfrac12(2+3)=\tfrac52$, quindi
$$R=\frac{5/2}{12/5}=\frac{25}{24}\approx1{,}0417,\qquad\phi=R-R_f=\frac1{24}\approx0{,}0417.$$
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
$P=12/5=2{,}4$ €, $R=25/24\approx1{,}0417$, $\phi=1/24\approx0{,}0417$.
:::::

::::: {.callout kind="warning" heading="B.1 · Errore tipico"}
Il prezzo non è $E[\tilde y]/R_f=2{,}5$: con quel prezzo il rendimento atteso sarebbe $R_f$ e il premio nullo. $P=2{,}4<2{,}5$ perché $\tilde y$ e $u'(\tilde y)$ sono correlati negativamente: l'agente paga meno un titolo che rende poco quando l'utilità marginale è alta.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
$\tilde M=u'(\tilde y)/E[u'(\tilde y)]$ ha $E[\tilde M]=1$. Per ogni titolo $i$ vale $R_fP_i=E[\tilde y_i\tilde M]$, quindi $E[\tilde R_i\tilde M]=R_f$ e $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$. *(ERA 06, «Il pricing kernel»; «Il premio al rischio di mercato di ciascun titolo»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
Kernel, con $E[u'(\tilde y)]=5/12$ da B.1: nello stato 1 ($\tilde y=2$) $\tilde M=\dfrac{1/2}{5/12}=\dfrac65$, nello stato 2 ($\tilde y=3$) $\tilde M=\dfrac{1/3}{5/12}=\dfrac45$, con $E[\tilde M]=\tfrac12\big(\tfrac65+\tfrac45\big)=1$.

Prezzo del titolo $b$:
$$P_b=E[\tilde y_b\tilde M]=\tfrac12\Big(\tfrac12\cdot\tfrac65+1\cdot\tfrac45\Big)=\tfrac12\Big(\tfrac35+\tfrac45\Big)=\frac7{10}=0{,}7.$$
Rendimento lordo $\tilde R_b=\tilde y_b/P_b=\big(\tfrac57;\ \tfrac{10}7\big)$, con $E[\tilde R_b]=\dfrac{15}{14}\approx1{,}0714$ e premio $E[\tilde R_b]-R_f=\dfrac1{14}\approx0{,}0714$.

Covarianza: $E[\tilde R_b\tilde M]=\tfrac12\big(\tfrac57\cdot\tfrac65+\tfrac{10}7\cdot\tfrac45\big)=\tfrac12\big(\tfrac67+\tfrac87\big)=1=R_f$, quindi
$$\mathrm{Cov}(\tilde R_b,\tilde M)=1-\frac{15}{14}=-\frac1{14}\approx-0{,}0714,$$
e $-\mathrm{Cov}(\tilde R_b,\tilde M)=1/14$ è il premio.

Unicità. Poiché $\tilde y_a=\tilde y_b+1$ e $P_a=P-P_b=1{,}7$, per entrambi i titoli $\tilde y_i-R_fP_i$ vale $(-0{,}2;\ 0{,}3)$ negli stati 1 e 2: è determinata solo la somma $\alpha_a+\alpha_b$, e l'ipotesi di unicità delle note (matrice delle covarianze invertibile) non vale *(ERA 06, «Il modello con $n$ titoli»)*. I prezzi restano unici e corretti perché le FOC in $\alpha_i=1$ sono necessarie: $P_i=E[\tilde y_i\tilde M]/R_f$.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
$\tilde M=6/5=1{,}2$ nello stato 1 e $4/5=0{,}8$ nello stato 2. $P_b=7/10=0{,}7$ €. Premio $E[\tilde R_b]-R_f=1/14\approx0{,}0714$. $\mathrm{Cov}(\tilde R_b,\tilde M)=-1/14\approx-0{,}0714$: il premio è uguale a $-\mathrm{Cov}(\tilde R_b,\tilde M)$.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
Il prezzo del titolo $b$ non è $E[\tilde y_b]/R_f=0{,}75$: va pesato con il kernel, che è più alto nello stato 1 dove il titolo paga poco. Il premio è positivo perché $\tilde R_b$ è alto proprio dove $\tilde M$ è basso: covarianza negativa.
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
Con partecipazione $k$ ciascun partecipante tiene $1/k$ quote e ha ricchezza $W_k=R_fP+(\tilde y-R_fP)/k$. La sua condizione del primo ordine in $\alpha=1/k$ è $E[(\tilde y-R_fP)\,u'(W_k)]=0$ e determina $P(k)$, radice minore dell'equazione. *(ERA 06, «Il modello con partecipazione $k$»; «Il premio al rischio di mercato con partecipazione limitata»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
Con $k=1/3$ e $R_f=1$: $W_k=\dfrac{\tilde y}{k}+\dfrac{k-1}{k}P=3\tilde y-2P$. Con $u'=1/W$ la condizione del primo ordine è
$$E\Big[\frac{\tilde y-P}{3\tilde y-2P}\Big]=0\iff\frac{2-P}{6-2P}+\frac{3-P}{9-2P}=0.$$
Moltiplicando per i denominatori, $(2-P)(9-2P)+(3-P)(6-2P)=0$, cioè $(18-13P+2P^2)+(18-12P+2P^2)=0$:
$$4P^2-25P+36=0,\qquad\Delta=625-576=49=7^2,\qquad P=\frac{25\pm7}8\in\Big\{\frac94;\ 4\Big\}.$$
Con $P=4$ la ricchezza $3\tilde y-8$ vale $-2$ nello stato 1: negativa, e $\ln$ non è definito. Con $P=9/4$ la ricchezza vale $3\tilde y-\tfrac92=\big(\tfrac32;\ \tfrac92\big)$ e la condizione è soddisfatta: $\dfrac{-1/4}{3/2}+\dfrac{3/4}{9/2}=-\dfrac16+\dfrac16=0$. Quindi $P(k)=9/4$ e
$$\phi(k)=\frac{E[\tilde y]}{P(k)}-R_f=\frac{5/2}{9/4}-1=\frac{10}9-1=\frac19\approx0{,}1111.$$
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
$W_k=3\tilde y-2P(k)$. Condizione del primo ordine $E[(\tilde y-P)/W_k]=0$, cioè $4P^2-25P+36=0$ con radici $9/4$ e $4$; si prende la minore, $P(k)=9/4=2{,}25$ €. $\phi(k)=\tfrac{5/2}{9/4}-1=1/9\approx0{,}1111$.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
La radice maggiore, $P=4$, supera $E[\tilde y]=2{,}5$ e darebbe un premio negativo e una ricchezza negativa. Il prezzo scende al diminuire di $k$ (da $2{,}4$ con $k=1$ a $2{,}25$ con $k=1/3$): è il segno che il premio sale.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
Con partecipazione limitata i partecipanti detengono $1/k$ quote e la loro ricchezza è più variabile di $\tilde y$, perché $\mathrm{Var}(W_k)=\mathrm{Var}(\tilde y)/k^2$: chiedono un premio maggiore. Il modello con agente rappresentativo e $\gamma=2$ dà un premio di circa lo 0,11% contro il 6% osservato. Riserva della nota: con la calibrazione $\gamma=2$ la partecipazione limitata non sposta in modo apprezzabile il premio al rischio di mercato finché $k$ supera circa il 30%; sotto questa soglia l'effetto cresce abbastanza da avvicinare il valore osservato. *(ERA 06, «Il modello con partecipazione $k$»; «Il premio al rischio di mercato con partecipazione limitata»; «Le spiegazioni proposte»)*
:::::

::::: {.callout kind="example" heading="B.4 · Svolgimento"}
$\mathrm{Var}(\tilde y)=\tfrac14$ e $\mathrm{Var}(W_k)=\mathrm{Var}(3\tilde y)=\tfrac94=\mathrm{Var}(\tilde y)/k^2$: nove volte più grande. Il kernel dei partecipanti è $\tilde M(k)=\big(\tfrac32;\ \tfrac12\big)$, più disperso di quello con $k=1$, $\big(\tfrac65;\ \tfrac45\big)$, e la covarianza con $\tilde y$ è più negativa: $-\tfrac14$ contro $-\tfrac1{10}$. Perciò $\phi(k)=\dfrac{1/4}{9/4}=\dfrac19>\phi=\dfrac{1/10}{12/5}=\dfrac1{24}$. I valori $1/9$ e $1/24$ sono quelli dell'esempio con $u=\ln$, non della calibrazione con $\gamma=2$.
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
I partecipanti tengono $1/k=3$ quote: la loro ricchezza ha varianza $\mathrm{Var}(\tilde y)/k^2$, nove volte quella di $\tilde y$, quindi chiedono un premio maggiore ($\phi(k)=1/9>\phi=1/24$). Il rischio aggregato ricade su pochi agenti e alza il premio verso il valore osservato: per questo è proposta come spiegazione del puzzle, con effetto apprezzabile per $k$ sotto circa il 30%.
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$F_2$ domina $F_1$ al primo ordine (FOSD) se la c.d.f. di $F_2$ sta sotto quella di $F_1$ in ogni punto; allora $E_{F_2}[v(\tilde x)]\ge E_{F_1}[v(\tilde x)]$ per ogni $v$ crescente. *(ERA 04, «Dominanza stocastica del primo ordine»)* *(ERA 05, «Dominanza stocastica»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Le c.d.f. nei valori $-20\%,\ 10\%,\ 40\%$ sono
$$\text{c.d.f. di }F_1:\ \Big(\tfrac4{10};\ \tfrac8{10};\ 1\Big),\qquad\text{c.d.f. di }F_2:\ \Big(\tfrac3{10};\ \tfrac6{10};\ 1\Big),$$
e la seconda sta sotto la prima in ogni punto, con disuguaglianza stretta nei primi due: $F_2$ domina $F_1$ al primo ordine. Con $\alpha>0$ la funzione $x\mapsto u(w_0+\alpha x)$ è crescente, perché $u$ lo è: la FOSD basta.
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
Sì, $F_2$: la sua c.d.f. $(3/10;\,6/10;\,1)$ sta sotto quella di $F_1$, $(4/10;\,8/10;\,1)$, quindi $F_2$ domina $F_1$ al primo ordine; con $\alpha>0$ la ricchezza $w_0+\alpha x$ cresce con $x$ e ogni $u$ crescente preferisce $F_2$.
:::::

::::: {.callout kind="warning" heading="C.1 · Errore tipico"}
La condizione $\alpha>0$ serve: con $\alpha<0$ (vendita allo scoperto) la ricchezza $w_0+\alpha x$ decresce con $x$ e l'ordine si invertirebbe.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
Con $u(x)=x$, che è crescente, la FOSD implica $E_{F_2}[\tilde x]\ge E_{F_1}[\tilde x]$. Il viceversa è falso: una media più alta non basta. *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Poiché $F_2$ domina $F_1$ al primo ordine, $F_2$ ha il rendimento atteso maggiore: $E_{F_1}[\tilde x]=4\%$ e $E_{F_2}[\tilde x]=13\%$ (la differenza, $9\%$, è l'area fra le due c.d.f.: $0{,}1\cdot0{,}3+0{,}2\cdot0{,}3$).

Una media maggiore non basta: su $\{-20\%;\,10\%;\,40\%\}$ siano $G_1=(0;\,1;\,0)$, media $10\%$, e $G_2=(3/10;\,0;\,7/10)$, media $22\%$. La c.d.f. di $G_1$ è $(0;\,1;\,1)$ e quella di $G_2$ è $(3/10;\,3/10;\,1)$: in $-20\%$ la seconda supera la prima, quindi $G_2$ non domina $G_1$. Con la funzione crescente $u(x)=\min(x,\,10\%)$ è $E_{G_1}[u(\tilde x)]=10\%>E_{G_2}[u(\tilde x)]=1\%$.
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
Sì, $F_2$: domina $F_1$ al primo ordine, e la FOSD implica la media maggiore ($13\%>4\%$). No: una media maggiore è necessaria ma non basta, perché la FOSD richiede la c.d.f. di $F_2$ sotto quella di $F_1$ in ogni punto.
:::::

::::: {.callout kind="warning" heading="C.2 · Errore tipico"}
La FOSD implica la media maggiore, non viceversa: due distribuzioni con la stessa media e diverse, come $F_3$ e $F_4$, non sono mai ordinate dalla FOSD.
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
Se $F_3$ è un *mean-preserving spread* di $F_4$, cioè $\tilde x_3\overset{d}{=}\tilde x_4+\tilde\varepsilon$ con $E[\tilde\varepsilon\mid\tilde x_4]=0$ (dove $\tilde x_i$ ha distribuzione $F_i$), allora $F_4$ domina $F_3$ al secondo ordine e ogni $u$ crescente e concava dà $E_{F_4}[u(\tilde x)]\ge E_{F_3}[u(\tilde x)]$. Per $\alpha\ge0$ la funzione $x\mapsto u(w_0+\alpha x)$ è crescente e concava, quindi la preferenza vale a ogni $\alpha$. *(ERA 04, «Il *mean-preserving spread*»)* *(ERA 05, «Il risultato»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
Le medie coincidono: $E_{F_3}[\tilde x]=\dfrac{-20\cdot2+10\cdot1+40\cdot3}6=15\%=E_{F_4}[\tilde x]$, quindi la FOSD è esclusa. Si legge $\tilde x_3\overset{d}{=}\tilde x_4+\tilde\varepsilon$: dal valore $10\%$, che ha probabilità $3/6$ in $F_4$, il rumore è $-30$, $0$ o $+30$ punti con probabilità $1/3$ ciascuno, media condizionata nulla; negli altri valori il rumore è nullo. Si ottiene
$$P(-20\%)=\tfrac16+\tfrac36\cdot\tfrac13=\tfrac26,\qquad P(10\%)=\tfrac36\cdot\tfrac13=\tfrac16,\qquad P(40\%)=\tfrac26+\tfrac36\cdot\tfrac13=\tfrac36,$$
cioè $F_3$. Lo conferma il confronto degli integrali delle c.d.f. a partire da $-20\%$, con i rendimenti in decimali: nei tre valori $-20\%$, $10\%$, $40\%$ valgono $0$, $\tfrac1{10}$, $\tfrac14$ per $F_3$ e $0$, $\tfrac1{20}$, $\tfrac14$ per $F_4$, quindi l'integrale per $F_3$ è maggiore o uguale a quello per $F_4$ ovunque, con uguaglianza all'ultimo valore (medie uguali).

Sia $V_i(\alpha)=E_{F_i}[u(w_0+\alpha\tilde x)]$. Per ogni $\alpha\in[0,W]$ vale $V_4(\alpha)\ge V_3(\alpha)$, in particolare in $\alpha_3^*$: $\max V_4\ge V_4(\alpha_3^*)\ge V_3(\alpha_3^*)=\max V_3$. La disuguaglianza è stretta: $E_{F_3}[\tilde x]=15\%>0$ implica $\alpha_3^*>0$ e $u$ è strettamente concava.
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
$F_4$: $F_3$ è un *mean-preserving spread* di $F_4$, quindi $F_4$ domina $F_3$ al secondo ordine; per ogni $\alpha\ge0$ la funzione $x\mapsto u(w_0+\alpha x)$ è crescente e concava, quindi $V_4(\alpha)\ge V_3(\alpha)$ per ogni $\alpha$ e $\max V_4\ge\max V_3$.
:::::

::::: {.callout kind="warning" heading="C.3 · Errore tipico"}
La concavità serve: con una $u$ convessa l'ordine si inverte. Con $u(w)=w^2$, $w_0=W=100$ e $\alpha=100$ l'utilità attesa con $F_3$ supera quella con $F_4$ di $300$.
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
La SOSD ordina le utilità attese a parità di $\alpha$, quindi anche i loro massimi; l'ammontare ottimo obbedisce a un altro criterio, il segno di $V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$, e per ordinarlo servono condizioni su $u$ (RR, P, RP). *(ERA 05, «Rischiosità del titolo e investimento»; «Condizioni per un investimento minore»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
La funzione $g(x)=x\,u'(w_0+\alpha x)$ che entra nella derivata non è in generale crescente e concava, e senza queste proprietà la dominanza non permette di concludere. Controesempio (verificato nello script), con quattro valori: $\tilde x\in\{-10\%;\,20\%;\,40\%;\,60\%\}$, $G=(0{,}05;\,0{,}05;\,0{,}85;\,0{,}05)$ e $H=(0{,}05;\,0{,}45;\,0{,}05;\,0{,}45)$, cioè $H$ si ottiene da $G$ spostando la probabilità del $40\%$ sul $20\%$ e sul $60\%$ in parti uguali: stessa media ($37{,}5\%$) e $G$ domina $H$ al secondo ordine. Per $u(w)=-(w-50)^{-5}/5$, strettamente crescente e concava per $w>50$, con $w_0=W=100$, l'ammontare ottimo è $\alpha_H^*=93{,}04>\alpha_G^*=87{,}92$: l'agente investe di più nel titolo più rischioso.

Per questa $u$ si ha $u'(w)=(w-50)^{-6}$, $u''(w)=-6\,(w-50)^{-7}$, $A(w)=6/(w-50)$ e $RR(w)=w\,A(w)=6w/(w-50)>1$ per ogni $w>50$: le condizioni sufficienti di ERA 05 ($RR<1$, $P>0$, $RP<2$) non valgono, e per questo il controesempio non contraddice il risultato della nota. *(ERA 05, «Condizioni per un investimento minore»)*
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
No. La SOSD ordina le utilità attese a parità di $\alpha$, non gli ammontari ottimi $\alpha_G^*$ e $\alpha_H^*$, che dipendono da $E[\tilde x\,u'(w_0+\alpha\tilde x)]$: servono condizioni su $u$; senza, può essere $\alpha_H^*>\alpha_G^*$.
:::::

::::: {.callout kind="warning" heading="C.4 · Errore tipico"}
Non confondere le due domande di C.3 e C.4: C.3 confronta le utilità dei portafogli ottimi e la risposta segue dalla sola SOSD; C.4 confronta gli ammontari investiti e la SOSD non basta. Per i tre valori di $F_3$ e $F_4$ l'ordine $\alpha_3^*\le\alpha_4^*$ vale comunque (lo script lo conferma su 1000 utilità marginali casuali e su una tabella CRRA e CARA), ma lo garantisce la forma di quei dati, non la sola dominanza.
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
Con il vincolo scritto nella forma $g\ge0$ la Lagrangiana è $f+\lambda g_{PC}+\beta g_{IC}$. Poiché $\partial z_l/\partial B_l=1$ e $B_l$ compare solo nell'addendo di indice $l$ di ciascuna somma, la derivata rispetto a $B_l$ ha un termine per il profitto, uno per PC e due per IC. *(ERA 08, «Lagrangiana e condizioni del primo ordine»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
$$\frac{\partial\mathcal L}{\partial B_l}=-\pi_l(1)+\lambda\,\pi_l(1)\,u'(z_l)+\beta\,\big[\pi_l(1)-\pi_l(0)\big]u'(z_l)=0\qquad(l=0,1,\dots,L).$$
La condizione vale anche per $l=0$, perché prima della normalizzazione $B_0$ è ancora una variabile di scelta: $B_0=0$ si impone solo dopo la derivazione. Si divide per $\pi_l(1)\,u'(z_l)>0$:
$$-\frac1{u'(z_l)}+\lambda+\beta\Big[1-\frac{\pi_l(0)}{\pi_l(1)}\Big]=0\quad\Longrightarrow\quad\frac1{u'(z_l)}=\lambda+\beta\,(1-r_l).$$
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
Per ogni $l=0,\dots,L$, prima di porre $B_0=0$: $\dfrac{\partial\mathcal L}{\partial B_l}=-\pi_l(1)+\lambda\,\pi_l(1)\,u'(z_l)+\beta\,[\pi_l(1)-\pi_l(0)]\,u'(z_l)=0$. Dividendo per $\pi_l(1)\,u'(z_l)>0$ si ottiene $1/u'(z_l)=\lambda+\beta\,(1-r_l)$ con $r_l=\pi_l(0)/\pi_l(1)$.
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
Nel vincolo IC l'indennizzo $B_l$ compare in entrambe le somme, quella con $\pi_l(1)$ e quella con $\pi_l(0)$, e per questo il coefficiente di $\beta$ è la differenza $\pi_l(1)-\pi_l(0)$: dimenticare la seconda somma toglie il termine $r_l$ dalla condizione.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
Per Kuhn-Tucker $\lambda\ge0$ e, per la complementarità, $\lambda>0$ implica che PC valga con uguaglianza. Dalla MLR e da $\sum_l\pi_l(0)=\sum_l\pi_l(1)=1$ segue $\sum_l\pi_l(1)(r_l-1)=0$: poiché $r_l$ è strettamente crescente, $r_0<1<r_L$. *(ERA 08, «La proprietà del rapporto di verosimiglianza monotono»; «Lagrangiana e condizioni del primo ordine»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
Poiché $\sum_l\pi_l(1)\,r_l=\sum_l\pi_l(0)=1$, si ha $\sum_l\pi_l(1)(r_l-1)=0$ con pesi positivi. Se fosse $r_L\le1$ sarebbe $r_l<1$ per ogni $l<L$ e la somma sarebbe negativa: quindi $r_L>1$ (e analogamente $r_0<1$).

Supponi $\lambda\le0$. La condizione di D.1 dice $1/u'(z_l)=\lambda+\beta\,(1-r_l)$ per ogni $l$. Con $\beta>0$ e $r_l$ strettamente crescente il secondo membro è minore nello stato $l=L$, dove, poiché $r_L>1$, vale $\lambda+\beta\,(1-r_L)<\lambda\le0$. Il primo membro $1/u'(z_L)$ è invece positivo: contraddizione. Per Kuhn-Tucker $\lambda\ge0$, quindi $\lambda>0$ e, per la complementarità $\lambda\,g_{PC}=0$, il vincolo di partecipazione vale con uguaglianza.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
Se fosse $\lambda\le0$, per $l=L$ il secondo membro di D.1, $\lambda+\beta(1-r_L)$, sarebbe negativo ($\beta>0$ e $r_L>1$, da $\sum_l\pi_l(1)(r_l-1)=0$ con MLR), mentre $1/u'(z_L)>0$. Poiché per Kuhn-Tucker $\lambda\ge0$, segue $\lambda>0$ e PC vale con uguaglianza.
:::::

::::: {.callout kind="warning" heading="D.2 · Errore tipico"}
La contraddizione non sta in $l=0$: lì il secondo membro può essere positivo, in accordo con $1/u'>0$. Serve $l=L$, dove la MLR impone $r_L>1$; per questo non basta dire che $r_l$ cresce, bisogna usare anche che le probabilità sommano a 1 in entrambi i casi.
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
Con informazione simmetrica la polizza ottima ha copertura piena (ricchezza $z_l$ costante) e il profitto $\Pi^{FB}(e)$ è massimo in $e^*$. Con $e$ non osservabile si aggiunge IC. Un'allocazione, cioè una polizza con l'impegno $(e,p,B_0,\dots,B_L)$, è Pareto efficiente se, fra le allocazioni fattibili quando l'impegno è osservabile, nessuna dà a uno dei due almeno quanto ha e all'altro strettamente di più. *(ERA 08, «Polizza ottima ed efficienza»; «Efficienza del benchmark»)*
:::::

::::: {.callout kind="example" heading="D.3 · Svolgimento"}
Con $e^*=1$ la polizza a copertura piena del *first best* non soddisfa IC: con $z_l$ costante IC diventa $u(z)-d(1)\ge u(z)-d(0)$, cioè $d(1)\le d(0)$, falsa. La compagnia ha due strade.

(a) Induce $e=1$ con la polizza ottima per l'impegno alto, a copertura parziale ($B_l<l$ per $l\ge1$, per la MLR con $\beta>0$): PC vale con uguaglianza ($\lambda>0$, D.2), quindi il cliente ha $\bar u$, come nel *first best*; la polizza è ammissibile nel problema con $e$ osservabile ma non ne è la soluzione, quindi il profitto è strettamente minore di $\Pi^{FB}(1)$.

(b) Induce $e=0$ con copertura piena: il cliente ha $\bar u$ e il profitto è $\Pi^{FB}(0)<\Pi^{FB}(1)$, perché $e^*=1$ è l'unico massimo.

In entrambi i casi il cliente ottiene $\bar u$ e la compagnia meno del *first best*. L'allocazione del *first best* con $e=1$ è fattibile quando l'impegno è osservabile e dà al cliente $\bar u$ e alla compagnia $\Pi^{FB}(1)$, strettamente più del *second best*: è un miglioramento paretiano, quindi l'esito con impegno non osservabile non è Pareto efficiente rispetto a quelle allocazioni.
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
No. Con $e^*=1$ la copertura piena viola IC (con $z_l$ costante il cliente sceglie $e=0$): la compagnia induce $e=1$ con copertura parziale o ripiega su $e=0$. In entrambi i casi il cliente ha $\bar u$ e il profitto è minore che nel *first best*: perde la compagnia, e il *first best*, fattibile con impegno osservabile, è un miglioramento paretiano.
:::::

::::: {.callout kind="warning" heading="D.3 · Errore tipico"}
L'inefficienza non ricade sul cliente: PC resta attivo e la sua utilità è $\bar u$ in ogni caso. Il caso $e^*=0$ è l'opposto: lì il *first best* soddisfa IC e l'esito è efficiente.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
$V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$ e $V''(\alpha)=E[\tilde x^2u''(w_0+\alpha\tilde x)]<0$: $V'$ è strettamente decrescente. Per un importo $\varepsilon$ piccolo il guadagno atteso è proporzionale a $\varepsilon$ e il premio per il rischio della parte a media nulla $\varepsilon(\tilde x-E[\tilde x])$ è circa $\tfrac12A(w_0)\,\mathrm{Var}(\tilde x)\,\varepsilon^2$. *(ERA 05, «La condizione del primo ordine»; «Quando investire nel titolo rischioso»)* *(ERA 03, «Il premio per lotterie piccole»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
Derivata: $V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$. In $\alpha=0$ la ricchezza $w_0$ è certa e $u'(w_0)$ esce dall'attesa:
$$V'(0)=u'(w_0)\,E[\tilde x].$$
Poiché $u'(w_0)>0$, il segno di $V'(0)$ è quello di $E[\tilde x]$. $V$ è strettamente concava, quindi $V'$ è strettamente decrescente.

Se $E[\tilde x]>0$, allora $V'(0)>0$: $V$ cresce subito a destra di $0$, $\alpha=0$ non è un massimo e $\alpha^*>0$. Se $E[\tilde x]\le0$, allora $V'(0)\le0$ e $V'(\alpha)<0$ per ogni $\alpha>0$: $V$ decresce su $[0,W]$ e $\alpha^*=0$. Poiché $E[\tilde x]=E[\tilde x_0]-r$, vale $\alpha^*>0\iff E[\tilde x_0]>r$.

Ordine di grandezza. Investire una piccola somma $\varepsilon$ dà un guadagno atteso $\varepsilon\,E[\tilde x]$, di ordine $\varepsilon$. Il costo del rischio è il premio per la parte a media nulla $\varepsilon(\tilde x-E[\tilde x])$, per la quale ERA 03 definisce il premio (lotterie con $E[X]=0$): per $\varepsilon$ piccolo vale circa $\tfrac12A(w_0)\,\mathrm{Var}(\varepsilon\tilde x)=\tfrac12A(w_0)\mathrm{Var}(\tilde x)\,\varepsilon^2$, di ordine $\varepsilon^2$. Per $\varepsilon$ abbastanza piccolo il termine lineare prevale, qualunque sia $E[\tilde x]>0$.

Esempio (script): $u=\ln$, $w_0=100$, $\tilde x=-10\%$ o $+11\%$ con probabilità $1/2$, quindi $E[\tilde x]=0{,}5\%$ e $\mathrm{Var}(\tilde x)=0{,}011025$. Il premio per la parte a media nulla è circa $0{,}000055\,\varepsilon^2$. Per $\varepsilon=1$ il guadagno atteso è $0{,}0050$ contro un premio di $0{,}000055$; per $\varepsilon=10$ è $0{,}0500$ contro $0{,}0055$; con l'approssimazione quadratica $\tfrac12A(w_0)\mathrm{Var}(\tilde x)\,\varepsilon^2$ il guadagno e il premio si pareggiano solo intorno a $\varepsilon\approx90{,}7$. L'investimento ottimo è $\alpha^*=45{,}45>0$.
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
$V'(0)=u'(w_0)\,E[\tilde x]$. Poiché $V$ è strettamente concava e $V'$ è decrescente: se $E[\tilde x]>0$ allora $V'(0)>0$, $V$ cresce subito a destra di $0$ e $\alpha^*>0$; se $E[\tilde x]\le0$ allora $V'(\alpha)<0$ per $\alpha>0$ e $\alpha^*=0$. Quindi $\alpha^*>0\iff E[\tilde x]>0\iff E[\tilde x_0]>r$.

Basta un rendimento atteso positivo anche piccolo perché, per un importo $\varepsilon$ piccolo, il guadagno atteso $\varepsilon E[\tilde x]$ è di ordine $\varepsilon$ e il premio per il rischio della parte a media nulla $\varepsilon(\tilde x-E[\tilde x])$ è di ordine $\varepsilon^2$: per $\varepsilon$ abbastanza piccolo il guadagno prevale.
:::::

::::: {.callout kind="warning" heading="E.1 · Errore tipico"}
Con $E[\tilde x]=0$ l'investitore non investe nulla, neppure una piccola somma: $V'(0)=0$ e $V'$ decresce. Il risultato richiede $u$ derivabile in $w_0$: con un punto angoloso in $w_0$ può essere $\alpha^*=0$ anche con $E[\tilde x]>0$.
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
Da $u_2=\phi\circ u_1$ segue $u_2'=\phi'(u_1)\,u_1'$, e $\phi''<0$ rende $\phi'$ strettamente decrescente. $V_1'$ è strettamente decrescente: se $V_1'(\alpha_2^*)>0$, il massimo di $V_1$ sta a destra di $\alpha_2^*$. *(ERA 05, «Avversione al rischio e investimento»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*Passo 1: riduzione.* $V_1$ è strettamente concava, quindi $V_1'$ è strettamente decrescente. Se $V_1'(\alpha_2^*)>0$, $V_1$ cresce in $\alpha_2^*$ e il suo massimo sta a destra: $\alpha_2^*<\alpha_1^*$. Resta da provare
$$V_1'(\alpha_2^*)=E\big[\tilde x\,u_1'(w_0+\alpha_2^*\tilde x)\big]>0.$$

*Passo 2: FOC dell'agente 2.* Poiché $0<\alpha_2^*<W$, $V_2'(\alpha_2^*)=0$, e per la regola della catena
$$0=E\big[\tilde x\,\phi'\big(u_1(w_0+\alpha_2^*\tilde x)\big)\,u_1'(w_0+\alpha_2^*\tilde x)\big].$$

*Passo 3: confronto stato per stato.* Sia $x\neq0$ una realizzazione di $\tilde x$. Se $x>0$, poiché $\alpha_2^*>0$ si ha $w_0+\alpha_2^*x>w_0$, quindi $u_1(w_0+\alpha_2^*x)>u_1(w_0)$ e, con $\phi'$ strettamente decrescente, $\phi'\big(u_1(w_0+\alpha_2^*x)\big)<\phi'\big(u_1(w_0)\big)$. Se $x<0$ valgono le disuguaglianze opposte. In entrambi i casi, moltiplicando per $x$,
$$x\,\phi'\big(u_1(w_0+\alpha_2^*x)\big)<x\,\phi'\big(u_1(w_0)\big),$$
e per $x=0$ vale l'uguaglianza.

*Passo 4: conclusione.* Si moltiplica per $u_1'(w_0+\alpha_2^*x)>0$ e si prende l'attesa. Poiché $\tilde x\neq0$ con probabilità positiva, la disuguaglianza resta stretta:
$$0=V_2'(\alpha_2^*)<\phi'\big(u_1(w_0)\big)\,E\big[\tilde x\,u_1'(w_0+\alpha_2^*\tilde x)\big]=\phi'\big(u_1(w_0)\big)\,V_1'(\alpha_2^*).$$
Con $\phi'(u_1(w_0))>0$ segue $V_1'(\alpha_2^*)>0$ e, per il passo 1, $\alpha_2^*<\alpha_1^*$.

Controllo numerico (script): con le coppie $(u_1,\phi)=(\ln w,\,-e^{-t})$, $(\sqrt w,\,\ln t)$ e $(\sqrt w,\,-1/t)$, su $641$, $389$ e $553$ distribuzioni casuali a tre valori con $r=0$, $w_0=W=100$ e $E[\tilde x]>0$, si trova sempre $\alpha_2^*<\alpha_1^*$ e $V_1'(\alpha_2^*)>0$.
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
Poiché $V_1$ è strettamente concava, basta mostrare $V_1'(\alpha_2^*)>0$. La FOC dell'agente 2, con $u_2'=\phi'(u_1)\,u_1'$, è $0=E[\tilde x\,\phi'(u_1(w_0+\alpha_2^*\tilde x))\,u_1'(w_0+\alpha_2^*\tilde x)]$. Per ogni $x\neq0$, essendo $\alpha_2^*>0$ e $\phi'$ strettamente decrescente, $x\,\phi'(u_1(w_0+\alpha_2^*x))<x\,\phi'(u_1(w_0))$: per $x>0$ $\phi'$ è minore, per $x<0$ è maggiore, e il segno di $x$ rimette l'ordine. Moltiplicando per $u_1'>0$ e prendendo l'attesa, $0<\phi'(u_1(w_0))\,V_1'(\alpha_2^*)$, cioè $V_1'(\alpha_2^*)>0$ e quindi $\alpha_2^*<\alpha_1^*$.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
La disuguaglianza $x\,\phi'(u_1(w_0+\alpha_2^*x))<x\,\phi'(u_1(w_0))$ vale per entrambi i segni di $x$: per $x<0$ è $\phi'$ a essere maggiore, ma la moltiplicazione per $x<0$ rovescia il verso. Con $\phi$ solo concava, e non strettamente, si ottiene $\alpha_2^*\le\alpha_1^*$: con $\phi$ affine i due agenti hanno la stessa FOC e lo stesso investimento.
:::::
