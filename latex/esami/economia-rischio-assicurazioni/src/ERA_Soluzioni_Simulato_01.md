---
title: "Economia del Rischio — appello simulato 01: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 01, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
$A(W)=-u''(W)/u'(W)$ e $RR(W)=W\,A(W)$. L'utilità è CARA se $A$ è costante, CRRA se $RR$ è costante. *(ERA 03, «Avversione assoluta e avversione relativa»; «Le funzioni CARA e CRRA»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
Per $u(W)=-1/W$:
$$u'(W)=\frac1{W^2},\qquad u''(W)=-\frac2{W^3},\qquad A(W)=\frac{2/W^3}{1/W^2}=\frac2W,\qquad RR(W)=W\cdot\frac2W=2.$$
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
$A(W)=2/W$, decrescente in $W$. $RR(W)=2$, costante: l'utilità è CRRA (con $\gamma=2$), non CARA.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
L'equivalente certo è il livello di ricchezza certa $CE$ con $u(CE)=E[u(w+X)]$; poiché $E[X]=0$, il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
Con $w_1=4$ la ricchezza finale vale $2$ con probabilità $2/3$ e $8$ con probabilità $1/3$:
$$E[u]=-\frac23\cdot\frac12-\frac13\cdot\frac18=-\frac13-\frac1{24}=-\frac38.$$
Da $-1/CE=-3/8$ segue $CE=8/3$, quindi $R_1=4-8/3=4/3$.
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
$CE=8/3\approx2{,}67$ €, $R_1=w_1-CE=4/3\approx1{,}33$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
$CE$ è una ricchezza, non un guadagno: $8/3$ non è il premio. Il premio è la differenza $w_1-CE=4/3$.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
Con $P(W)=-u'''/u''$ vale $A'(W)=A(W)\,[A(W)-P(W)]$: $A'\le0$ (DARA) se e solo se $P\ge A$, e allora il premio per il rischio non cresce con la ricchezza; se $A'<0$, cioè $P>A$, decresce strettamente. *(ERA 03, «Prudenza e avversione assoluta»; «Condizioni equivalenti per il DARA»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
Con $w_2=6$ la ricchezza finale vale $4$ con probabilità $2/3$ e $10$ con probabilità $1/3$:
$$E[u]=-\frac23\cdot\frac14-\frac13\cdot\frac1{10}=-\frac16-\frac1{30}=-\frac15,\qquad CE=5,\qquad R_2=6-5=1.$$
In forma chiusa, per questa lotteria $R(w)=8/(w+2)$, decrescente in $w$.

Prudenza: $u'''(W)=6/W^4$, quindi
$$P(W)=-\frac{6/W^4}{-2/W^3}=\frac3W>\frac2W=A(W),\qquad A'(W)=A\,(A-P)=-\frac2{W^2}<0.$$
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
$R_2=1$ € ($CE=5$ €). $P(W)=3/W>A(W)=2/W$ per ogni $W>0$, quindi $A'(W)=A(A-P)<0$: l'utilità è DARA in senso stretto e il premio decresce con la ricchezza. Per questo $R_2=1<R_1=4/3$.
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
Il segno di $A'=A\,(A-P)$ è opposto a quello di $P-A$: $P>A$ vuol dire $A$ decrescente, cioè meno avversione quando si è più ricchi.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
Per $kX$ con $E[X]=0$ il premio $R(k)$ ha $R(0)=0$, $R'(0)=0$, $R''(0)=A(w)\,E[X^2]$, quindi $R(k)\approx\tfrac12A(w)\,E[X^2]\,k^2$. *(ERA 03, «Il premio per lotterie piccole»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
Lo sviluppo di Taylor al secondo ordine dà $R(k)\approx\tfrac12R''(0)\,k^2$: il premio è proporzionale a $k^2$, cioè alla varianza di $kX$, e $R(2k)\approx4R(k)$.

Con i dati: $A(4)=1/2$, $E[X^2]=\tfrac23\cdot4+\tfrac13\cdot16=8$, quindi $R(k)\approx2k^2$. Il valore esatto è $R(k)=8k^2/(4+2k)$: il rapporto $R(2k)/R(k)$ vale $3{,}98$ per $k=0{,}01$ e $3{,}82$ per $k=0{,}1$, vicino a 4 per $k$ piccolo.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
Il premio si moltiplica per circa 4, cioè quadruplica: per $k$ piccolo $R(k)\approx\tfrac12A(w)E[X^2]k^2$ è proporzionale alla varianza di $kX$, e raddoppiare $k$ quadruplica la varianza.
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
Il prezzo equo azzera il profitto atteso: $p^*=\pi L$. Con $u$ strettamente concava e una perdita non degenere, la disuguaglianza di Jensen è stretta: $E[u(W)]<u(E[W])$. *(ERA 07, «Il benchmark: informazione perfetta»; ERA 03, «La disuguaglianza di Jensen»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Premio equo: $p^*=\tfrac14\cdot20=5$ €. Senza assicurazione la ricchezza vale $16$ con probabilità $1/4$ e $36$ con probabilità $3/4$:
$$EU=\frac14\sqrt{16}+\frac34\sqrt{36}=1+\frac92=\frac{11}2=5{,}5.$$
Con la copertura piena a $p^*$ la ricchezza certa è $36-5=31$ e $u=\sqrt{31}\approx5{,}57$. Si confrontano i quadrati: $5{,}5^2=30{,}25<31$, quindi $5{,}5<\sqrt{31}$.
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
Il premio equo è $5$ €. Senza copertura $EU=11/2=5{,}5$; con copertura piena $EU=\sqrt{31}\approx5{,}57$. Preferisce la copertura piena: per la disuguaglianza di Jensen stretta ($u$ strettamente concava, perdita non degenere) $E[u(\text{ricchezza})]<u(E[\text{ricchezza}])=u(31)$.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
Il consumatore paga al più $w-CE$ per la copertura piena, perché $u(w-p)\ge E[u]=u(CE)$ se e solo se $p\le w-CE$. Il premio per il rischio è la ricchezza attesa meno $CE$; la ricchezza attesa è $w-\pi L$. *(ERA 03, «Equivalente certo e premio per il rischio»; ERA 07, «Il benchmark: informazione perfetta»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
Da $\sqrt{CE}=EU=11/2$ segue $CE=121/4=30{,}25$. Il premio massimo è $p_{\max}=36-30{,}25=5{,}75$. La ricchezza attesa è $36-5=31$, quindi il premio per il rischio è $31-30{,}25=0{,}75$. Controllo: $0{,}75=p_{\max}-\pi L=5{,}75-5$.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
$CE=121/4=30{,}25$ €. Premio massimo $=w-CE=5{,}75$ €. Premio per il rischio $=31-30{,}25=0{,}75$ €, cioè la parte del premio massimo che supera la perdita attesa di $5$ €.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
Con $E[X]\neq0$ la differenza $w-CE=5{,}75$ non è il premio per il rischio: comprende anche la perdita attesa di $5$ €.
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
Il consumatore di tipo $\pi$ compra se $\pi\ge h(p)$, con $h(p)=\dfrac{u(w)-u(w-p)}{u(w)-u(w-L)}$. Il profitto per polizza è $p-E[\pi\mid\pi\ge h(p)]\,L$; con $\pi$ uniforme su $[0,1]$, $E[\pi\mid\pi\ge t]=(1+t)/2$. Un prezzo è di equilibrio se il profitto è nullo. *(ERA 07, «La congettura sul prezzo e la regola di acquisto»; «Un esempio con distribuzione uniforme»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
*Prezzo $p=11$.* Ricchezza con la polizza: $36-11=25$. Il tipo $\pi$ compra se
$$\sqrt{25}\ \ge\ \pi\sqrt{16}+(1-\pi)\sqrt{36}\iff5\ge6-2\pi\iff\pi\ge\frac12,$$
quindi $h(11)=1/2$. Gli acquirenti sono i tipi in $[1/2,1]$ e la loro probabilità media è $3/4$. La perdita attesa per polizza è $\tfrac34\cdot20=15$, il profitto è $11-15=-4$.

*Prezzo $p=L=20$.* Ricchezza con la polizza: $36-20=16=w-L$, quindi $h(20)=\dfrac{6-4}{6-4}=1$. Compra solo chi ha $\pi=1$ (a parità di utilità compra): la probabilità media è $1$ (come limite per $t\to1$), il costo per polizza è $1\cdot20=20$ e il profitto è $20-20=0$. Con questi dati $L$ è anche l'unico prezzo di equilibrio in $[0,L]$: per $p<L$, con $s=\sqrt{36-p}\in(4,6]$, la soglia è $h=(6-s)/2$, il costo per polizza è $L\,(1+h)/2=10+5(6-s)$ e il profitto è $p-\text{costo}=-(s-1)(s-4)<0$.
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
Per $p=11$: $h(11)=1/2$, $E[\pi\mid\pi\ge1/2]=3/4$, profitto per polizza $11-\tfrac34\cdot20=-4$ €: non è un prezzo di equilibrio (le compagnie perdono). Per $p=L=20$: $h=1$, probabilità media degli acquirenti $=1$, profitto $20-20=0$: è di equilibrio, ma compra solo chi ha $\pi=1$ e il mercato scompare.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
Il costo per polizza si calcola sugli acquirenti ($3/4$), non su tutta la popolazione ($1/2$): con la media di tutti il costo sarebbe $10$ e a $p=11$ si troverebbe un profitto positivo di $1$ €, che non c'è.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
La pendenza della curva di indifferenza nel piano $(B,p)$ è $s=\dfrac{\pi a}{\pi a+(1-\pi)b}$, crescente in $\pi$: nello stesso contratto la curva dell'alto rischio è più ripida (single-crossing). Il contratto del basso rischio sta sulla sua retta di profitto nullo $p=\pi_lB$ e non deve essere preferito dall'alto rischio a $(L,\pi_hL)$. *(ERA 07, «Preferenze e single-crossing»; «Il contratto per il basso rischio non è imitabile»)*
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
Con $B=L$ e prezzo equo $\pi_lL<\pi_hL$ l'alto rischio lo preferirebbe al proprio contratto: non separerebbe. Le sue curve di indifferenza sono più ripide (single-crossing): riducendo $B$ lungo $p=\pi_lB$ l'alto rischio perde utilità più in fretta del basso rischio, finché non preferisce più il contratto al proprio. Quindi $B<L$.
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$F_2$ domina $F_1$ al primo ordine se $F_2(x)\le F_1(x)$ per ogni $x$: allora ogni agente con $u$ crescente preferisce $F_2$. A medie uguali e distribuzioni diverse la dominanza del primo ordine è esclusa. *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Medie: $E[p]=2+21+8=31$ e $E[q]=4+15+12=31$. Le c.d.f. nei premi $20,30,40$ sono
$$F_p=\Big(\tfrac1{10};\ \tfrac45;\ 1\Big),\qquad F_q=\Big(\tfrac15;\ \tfrac7{10};\ 1\Big),\qquad F_p-F_q=\Big(-\tfrac1{10};\ +\tfrac1{10};\ 0\Big):$$
la differenza cambia segno, le c.d.f. si incrociano. Un agente con $u=\sqrt{x}$ preferisce $p$, uno con $u=x^2$ (crescente e convessa) preferisce $q$.
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
No: medie uguali ($31$ €) e c.d.f. incrociate, quindi nessuna dominanza del primo ordine; $u$ crescenti diverse ordinano le due lotterie in modo opposto.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
Se $F_1$ è un mean-preserving spread di $F_2$, allora $F_2$ domina $F_1$ al secondo ordine, e ogni agente con $u$ crescente e concava preferisce $F_2$. *(ERA 04, «Dominanza stocastica del secondo ordine»; «Il *mean-preserving spread*»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Si ha $q=p+\tilde\varepsilon$ con rumore a media condizionata nulla: dal premio $30$ (probabilità $7/10$) si passa a $20$ o a $40$ con probabilità $1/7$ ciascuno ($\pm10$) e si resta in $30$ con probabilità $5/7$; negli altri premi il rumore è nullo. Si ottiene $P(20)=\tfrac1{10}+\tfrac7{10}\cdot\tfrac17=\tfrac2{10}$, $P(30)=\tfrac7{10}\cdot\tfrac57=\tfrac5{10}$, $P(40)=\tfrac2{10}+\tfrac1{10}=\tfrac3{10}$: è $q$.

Lo conferma il confronto degli integrali delle c.d.f. da $20$: fino a $30$ valgono $1$ per $p$ e $2$ per $q$, fino a $40$ valgono $9$ per entrambi, quindi $\int F_p\le\int F_q$ ovunque.
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
Preferisce $p$: $q$ è un mean-preserving spread di $p$ (stessa media, più massa sugli estremi), quindi $p$ domina $q$ al secondo ordine e, con $u$ strettamente concava, la preferenza è stretta (con $u$ solo concava, magari lineare, sarebbe debole).
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
Indipendenza: per ogni $\alpha\in(0,1]$ e ogni terza lotteria $L^3$, $L^1\succeq L^2\iff\alpha L^1+(1-\alpha)L^3\succeq\alpha L^2+(1-\alpha)L^3$. *(ERA 02, «Gli assiomi»; «Lotterie semplici e composte»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
Ridotte ai tre premi, $p'=\big(\tfrac1{20};\,\tfrac{17}{20};\,\tfrac1{10}\big)$ e $q'=\big(\tfrac1{10};\,\tfrac34;\,\tfrac3{20}\big)$, con la stessa media $30{,}5$. Non serve calcolare utilità attese: $p'$ e $q'$ sono $p$ e $q$ mescolate con la stessa $L_c$ e lo stesso peso $\alpha=1/2$.
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
Sceglie $p'$: è l'indipendenza con $\alpha=1/2$ e terza lotteria $L_c$, che conserva la preferenza per $p$. La SOSD non basterebbe: l'agente può non essere avverso al rischio.
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
Nel triangolo di Machina l'utilità attesa è affine nelle coordinate, quindi le curve di indifferenza sono rette parallele; per due segmenti paralleli e con lo stesso verso l'utilità cambia nello stesso verso. *(ERA 02, «Le rette di indifferenza nel triangolo»; «Lettura nel triangolo»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
Con coordinate $(\pi_{20},\pi_{40})$: $p=(\tfrac1{10},\tfrac15)$, $q=(\tfrac15,\tfrac3{10})$, $p'=(\tfrac1{20},\tfrac1{10})$, $q'=(\tfrac1{10},\tfrac3{20})$. Allora $q-p=(\tfrac1{10},\tfrac1{10})$ e $q'-p'=(\tfrac1{20},\tfrac1{20})=\tfrac12\,(q-p)$: i segmenti $pq$ e $p'q'$ sono paralleli (pendenza 1) e orientati allo stesso modo. Con l'utilità attesa le rette di indifferenza sono parallele, quindi $q\succ p\iff q'\succ p'$: preferire strettamente $q$ a $p$ e $p'$ a $q'$ viola l'equivalenza (è la struttura di Allais: scelta sicura nella coppia mescolata con il premio intermedio certo, scelta rischiosa nell'altra). La stretta preferenza conta: un agente indifferente fra $p$ e $q$, come chi ha utilità lineare, lo sarebbe anche fra $p'$ e $q'$ e non violerebbe nulla.
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
No: $q'-p'=\tfrac12(q-p)$, segmenti paralleli e concordi; con l'utilità attesa le rette di indifferenza sono parallele, quindi l'ordine si conserva ($q\succ p$ implicherebbe $q'\succ p'$).
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
Kuhn-Tucker: con il constraint scritto $g\ge0$, $\mathcal L=f+\lambda g$ e valgono $\lambda\ge0$, $g\ge0$, $\lambda g=0$. Con $u$ strettamente concava $u'$ è strettamente decrescente, quindi iniettiva. *(ERA 08, «Il problema della compagnia»; «La polizza ottima per un impegno fissato»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
Posto $z_l=w-p-l+B_l$,
$$\mathcal L=p-\sum_{l=0}^L\pi_l(e)\,B_l+\lambda\Big[\sum_{l=0}^L\pi_l(e)\,u(z_l)-d(e)-\bar u\Big].$$
Poiché $\partial z_l/\partial p=-1$ e $\partial z_l/\partial B_l=1$, le condizioni del primo ordine sono
$$\frac{\partial\mathcal L}{\partial p}=1-\lambda\sum_{l=0}^L\pi_l(e)\,u'(z_l)=0,\qquad \frac{\partial\mathcal L}{\partial B_l}=-\pi_l(e)+\lambda\,\pi_l(e)\,u'(z_l)=0\quad(l=0,\dots,L).$$
La prima è l'opposto della somma delle altre (perché $\sum_l\pi_l(e)=1$), quindi è ridondante. Dividendo la seconda per $\pi_l(e)>0$: $\lambda\,u'(z_l)=1$ per ogni $l$. Poiché $u'(z_l)>0$ è finita, $\lambda>0$, e $u'(z_l)=1/\lambda$ non dipende da $l$. Per l'iniettività di $u'$ anche $z_l$ è lo stesso in ogni stato, cioè $-l+B_l$ è costante in $l$; con $B_0=0$ la costante è $0$ e $B_l=l$. Poiché $\lambda>0$, la complementarità dà $g=0$: il constraint vale con uguaglianza e il premio è $p=w-u^{-1}\big(d(e)+\bar u\big)$.
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
$\mathcal L=p-\sum_l\pi_l(e)B_l+\lambda\big[\sum_l\pi_l(e)u(w-p-l+B_l)-d(e)-\bar u\big]$. Le FOC in $B_l$ danno $\lambda\,u'(z_l)=1$ per ogni $l$, con $z_l=w-p-l+B_l$ (la FOC in $p$ è l'opposto della loro somma). Allora $\lambda>0$ e $u'(z_l)=1/\lambda$ è costante: per la stretta concavità $z_l$ è costante, cioè $B_l-l$ è costante e, con $B_0=0$, $B_l=l$ per ogni $l$: copertura piena. Il constraint vale con uguaglianza: $u(w-p)=d(e)+\bar u$.
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
Senza la normalizzazione $B_0=0$ si ottiene solo che $B_l-l$ è costante: la soluzione è unica a meno della traslazione $(p,B_l)\mapsto(p+c,B_l+c)$, che non cambia né $z_l$ né il profitto.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
Con $e$ non osservabile il problema ha in più il constraint IC. Aggiungere un constraint a un problema di massimo non può far aumentare il massimo: se la soluzione del problema senza IC lo soddisfa, è ottima anche con IC. *(ERA 08, «La polizza ottima per l'impegno basso»; «Informazione asimmetrica»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
La soluzione di D.1 con $e=0$ ha $z_l=w-p$ in ogni stato. Poiché $\sum_l\pi_l(0)=\sum_l\pi_l(1)=1$, IC diventa
$$u(w-p)-d(0)\ \ge\ u(w-p)-d(1)\iff d(0)\le d(1),$$
vera perché l'impegno è faticoso ($d(1)>d(0)$). Il cliente, avendo la stessa ricchezza in ogni stato, non ha alcun vantaggio dall'impegno e sceglie quello basso.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
Con $B_l=l$ la ricchezza è $w-p$ in ogni stato, quindi IC diventa $u(w-p)-d(0)\ge u(w-p)-d(1)$, cioè $d(0)\le d(1)$: vera. La polizza di D.1 soddisfa anche IC, e un constraint in più non può far salire il massimo: resta ottima.
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
Il profitto del first best è $\Pi^{FB}(e)=p(e)-\sum_l\pi_l(e)\,l$ e $e^*$ lo massimizza. Il second best con $e$ non osservabile è il massimo profitto fra le polizze che soddisfano PC e IC. *(ERA 08, «Polizza ottima ed efficienza»; «La scelta dell'impegno»)*
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
No: con $e=0$ la polizza del first best soddisfa IC; indurre $e=1$ rende al più $\Pi^{FB}(1)<\Pi^{FB}(0)$; si ottiene la stessa allocazione del first best, che è Pareto efficiente.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
Si deriva $V$ sotto il segno di attesa (lecito, $\tilde x$ ha un numero finito di valori). Con $V''<0$ la FOC determina $\alpha^*$ e, per il teorema della funzione implicita, $\alpha^*$ è derivabile in $w_0$. *(ERA 05, «La condizione del primo ordine»; «Ricchezza iniziale e investimento»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
Derivata prima e seconda:
$$V'(\alpha)=E\big[\tilde x\,u'(w_0+\alpha\tilde x)\big],\qquad V''(\alpha)=E\big[\tilde x^2\,u''(w_0+\alpha\tilde x)\big]<0,$$
la seconda negativa perché $u''<0$ e $\mathbb P(\tilde x\neq0)>0$: $V$ è strettamente concava e la FOC è anche sufficiente. Con $\alpha^*$ interno, la FOC è $E\big[\tilde x\,u'(w_0+\alpha^*\tilde x)\big]=0$ per ogni $w_0$; agli estremi la condizione è invece $V'(0)\le0$ (per $\alpha^*=0$) o $V'(W)\ge0$ (per $\alpha^*=W$).

Derivando la FOC rispetto a $w_0$, con $\alpha^*=\alpha^*(w_0)$ (la derivata dell'argomento di $u'$ è $1+\tilde x\,d\alpha^*/dw_0$):
$$E\big[\tilde x\,u''(w_0+\alpha^*\tilde x)\big]+E\big[\tilde x^2\,u''(w_0+\alpha^*\tilde x)\big]\frac{d\alpha^*}{dw_0}=0,$$
perché $d\alpha^*/dw_0$ non dipende dallo stato. Quindi
$$\frac{d\alpha^*}{dw_0}=-\frac{E\big[\tilde x\,u''(w_0+\alpha^*\tilde x)\big]}{E\big[\tilde x^2\,u''(w_0+\alpha^*\tilde x)\big]}.$$
Il denominatore è $V''(\alpha^*)<0$: il segno di $d\alpha^*/dw_0$ è quello di $E[\tilde x\,u''(w_0+\alpha^*\tilde x)]$.

Controllo numerico, con $r=0$, $W=w_0=100$ e $\tilde x=-50\%$ o $+100\%$ equiprobabili: $u=\ln$ dà $\alpha^*=50$ e $d\alpha^*/dw_0=0{,}5$; $u=-1/w$ dà $\alpha^*=24{,}26$ e $0{,}2426$; la CARA con $\lambda=0{,}01$ dà $\alpha^*=46{,}21$ e $0$.
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
$V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$, $V''(\alpha)=E[\tilde x^2u''(w_0+\alpha\tilde x)]<0$. FOC per un ottimo interno: $E[\tilde x\,u'(w_0+\alpha^*\tilde x)]=0$.

Per la funzione implicita
$$\frac{d\alpha^*}{dw_0}=-\frac{E[\tilde x\,u''(w_0+\alpha^*\tilde x)]}{E[\tilde x^2u''(w_0+\alpha^*\tilde x)]}.$$
Il denominatore è negativo, quindi il segno è quello di $E[\tilde x\,u''(w_0+\alpha^*\tilde x)]$: $\alpha^*$ cresce con $w_0$ se e solo se $E[\tilde x\{-u''(w_0+\alpha^*\tilde x)\}]<0$.
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
Se $F_2$ domina $F_1$ al secondo ordine, $E_{F_2}[G]\ge E_{F_1}[G]$ per ogni $G$ crescente e concava. La derivata di $V_2$ in $\alpha_1^*$ è $E_{F_2}[g(\tilde x)]$, con $g(x)=x\,u'(w_0+\alpha_1^*x)$. *(ERA 05, «Che cosa si vuole dimostrare»; «Quando la funzione è crescente»; «Il risultato»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*Passo 1: che cosa mostrare.* Per la FOC sotto $F_1$ in $\alpha_1^*$ interno, $E_{F_1}[g(\tilde x)]=0$. Basta mostrare $E_{F_2}[g(\tilde x)]\ge0$.

*Passo 2: $g$ è crescente.* Con $h(y)=y\,u'(w_0+y)$ si ha $g(x)=h(\alpha_1^*x)/\alpha_1^*$, quindi $g'(x)=h'(\alpha_1^*x)$. Poiché $u''=-A\,u'$,
$$h'(y)=u'(w_0+y)+y\,u''(w_0+y)=u'(w_0+y)\big[1-y\,A(w_0+y)\big].$$
Da $y=(w_0+y)-w_0$ segue $y\,A(w_0+y)=RR(w_0+y)-w_0\,A(w_0+y)$, quindi
$$h'(y)=u'(w_0+y)\Big[1-RR(w_0+y)+w_0\,A(w_0+y)\Big].$$
Con $u'>0$, $w_0>0$ e $A>0$ il termine $w_0A$ è positivo: se $RR(w)<1$ la parentesi è positiva, $h'>0$ e $g$ è strettamente crescente.

*Passo 3: dominanza.* $g$ è crescente (passo 2) e concava (ipotesi), e $F_2$ domina $F_1$ al secondo ordine: $E_{F_2}[g(\tilde x)]\ge E_{F_1}[g(\tilde x)]=0$, cioè $V_2'(\alpha_1^*)\ge0$.

*Passo 4: conclusione.* $V_2$ è strettamente concava, quindi $V_2'$ è strettamente decrescente: da $V_2'(\alpha_1^*)\ge0$ segue $V_2'(\alpha)>0$ per $\alpha<\alpha_1^*$, e $V_2$ è crescente su $[0,\alpha_1^*]$. Il massimo non sta a sinistra di $\alpha_1^*$: $\alpha_2^*\ge\alpha_1^*$.
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
La FOC sotto $F_1$ dà $E_{F_1}[g(\tilde x)]=0$ con $g(x)=x\,u'(w_0+\alpha_1^*x)$, e $V_2'(\alpha_1^*)=E_{F_2}[g(\tilde x)]$. Con $h(y)=y\,u'(w_0+y)$, $g'(x)=h'(\alpha_1^*x)$ e
$$h'(y)=u'(w_0+y)\big[1-RR(w_0+y)+w_0A(w_0+y)\big]>0\quad\text{se }RR<1,$$
perché $w_0A>0$: $g$ è crescente. Essendo anche concava, e $F_2$ SOSD $F_1$, $E_{F_2}[g]\ge E_{F_1}[g]=0$, cioè $V_2'(\alpha_1^*)\ge0$. $V_2$ è concava, quindi il massimo non sta a sinistra di $\alpha_1^*$: $\alpha_2^*\ge\alpha_1^*$.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
Le due proprietà di $g$ hanno condizioni diverse: la monotonia usa $RR<1$, la concavità (data qui) è garantita da $RP<2$ e $P>0$, condizione sufficiente. E $RR<1$ è sufficiente, non necessaria: per il logaritmo $RR=1$ ma $h'=u'\,w_0A>0$.
:::::
