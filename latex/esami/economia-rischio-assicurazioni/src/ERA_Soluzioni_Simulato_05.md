---
title: "Economia del Rischio — appello simulato 05: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 05, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
$A=-u''/u'$ e $RR=W\,A$. L'utilità è CARA se $A$ è costante in $W$, CRRA se lo è $RR$. *(ERA 03, «Avversione assoluta e avversione relativa»)* *(ERA 03, «Le funzioni CARA e CRRA»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
Agente 1, $u_1=\ln W$: $u_1'=1/W$ e $u_1''=-1/W^2$, quindi
$$A_1(W)=\frac{1/W^2}{1/W}=\frac1W,\qquad RR_1(W)=W\,A_1(W)=1.$$
$RR_1$ è costante, $A_1$ no: CRRA (con $\gamma=1$), non CARA.

Agente 2, $u_2=-e^{-\lambda W}/\lambda$: $u_2'=e^{-\lambda W}$ e $u_2''=-\lambda e^{-\lambda W}$, quindi
$$A_2(W)=\lambda=\frac1{20},\qquad RR_2(W)=\lambda W=\frac W{20}.$$
$A_2$ è costante, $RR_2$ cresce con $W$: CARA, non CRRA.
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
Agente 1: $A_1(W)=1/W$, $RR_1(W)=1$: CRRA. Agente 2: $A_2(W)=\lambda=1/20$, $RR_2(W)=W/20$: CARA.
:::::

::::: {.callout kind="warning" heading="A.1 · Errore tipico"}
Le due classi non si sovrappongono: il logaritmo ha $RR$ costante ma $A=1/W$ decrescente, quindi non è CARA; l'esponenziale ha $A$ costante ma $RR=\lambda W$ crescente, quindi non è CRRA.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
L'equivalente certo è la ricchezza certa $CE$ con $u(CE)=E[u(w+X)]$; poiché $E[X]=0$, il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
La ricchezza finale vale $25-15=10$ oppure $25+15=40$, ciascuna con probabilità $1/2$. Con $u_1=\ln$:
$$E[u_1(w+X)]=\tfrac12\ln10+\tfrac12\ln40=\tfrac12\ln400=\ln20.$$
Da $\ln CE=\ln20$ segue $CE=20$, quindi $R=25-20=5$.
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
$CE=20$ €, $R=5$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
Non si può applicare il logaritmo alla ricchezza attesa: $\ln25>\ln20=E[\ln(w+X)]$, e la differenza è proprio il premio. $CE$ è una ricchezza, non un guadagno.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
Si deriva $E[u(w+X)]=u(w-R)$ rispetto a $w$: a sinistra la derivata passa sotto il segno di attesa, a destra si usa la regola della catena. Il segno di $\partial R/\partial w$ è quello del confronto fra $u'(w-R)$ e $E[u'(w+X)]$. *(ERA 03, «Come varia il premio con la ricchezza»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
Derivando,
$$E[u_1'(w+X)]=u_1'(w-R)\Big(1-\frac{\partial R}{\partial w}\Big)\quad\Longrightarrow\quad\frac{\partial R}{\partial w}=1-\frac{E[u_1'(w+X)]}{u_1'(w-R)}.$$
Con $u_1'(W)=1/W$, $w=25$ e $X=\pm15$ (per A.2, $w-R=CE=20$):
$$E[u_1'(w+X)]=\tfrac12\Big(\tfrac1{10}+\tfrac1{40}\Big)=\frac1{16},\qquad u_1'(CE)=\frac1{20},\qquad\frac{\partial R}{\partial w}=1-\frac{1/16}{1/20}=1-\frac54=-\frac14.$$
Controllo: $R(w)=w-\sqrt{w^2-225}$ dà $R'(w)=1-w/\sqrt{w^2-225}=1-25/20=-1/4$ (la derivata numerica dello script coincide).

Il segno è negativo: il premio decresce con la ricchezza, di $0{,}25$ € per ogni euro di ricchezza in più. È il caso di un'utilità DARA: per il logaritmo $A'(W)=-1/W^2<0$.
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
$\dfrac{\partial R}{\partial w}=1-\dfrac{E[u_1'(w+X)]}{u_1'(w-R)}=1-\dfrac{1/16}{1/20}=-\dfrac14$: il premio decresce con la ricchezza (l'avversione assoluta $1/W$ è decrescente).
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
Al denominatore compare $u_1'(w-R)$, cioè la derivata nell'equivalente certo $CE=20$, non in $w$: la derivata di $u(w-R)$ rispetto a $w$ porta con sé il fattore $1-\partial R/\partial w$.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
«Più avverso» richiede $A_j(W)\ge A_i(W)$ per ogni $W$. Per una lotteria piccola a media nulla il premio è circa $\tfrac12A(w)\,\mathrm{Var}(X)$: a parità di lotteria paga di più chi ha $A$ maggiore alla ricchezza di partenza. *(ERA 03, «Il premio per lotterie piccole»)* *(ERA 03, «Avversione assoluta e avversione relativa»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
$A_1(W)-A_2=\dfrac1W-\dfrac1{20}$ è positivo per $W<20$ e negativo per $W>20$: le due avversioni si eguagliano in $W=20$ e nessuna delle due è maggiore o uguale all'altra per ogni $W$. Nessun agente è più avverso dell'altro.

Per una lotteria piccola $R\approx\tfrac12A(w)\,\mathrm{Var}(X)$. A $w=10$, $A_1=1/10>A_2=1/20$: paga di più l'agente 1 (il doppio). A $w=40$, $A_1=1/40<A_2=1/20$: paga di più l'agente 2. Con $X=\pm1$ i premi esatti, calcolati nello script, lo confermano: a $w=10$ sono $0{,}0501$ (agente 1) e $0{,}0250$ (agente 2); a $w=40$ sono $0{,}0125$ e $0{,}0250$.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
No: $A_1(W)-A_2=1/W-1/20$ cambia segno in $W=20$, quindi nessun agente ha $A$ maggiore a ogni ricchezza. Per lotterie piccole $R\approx\frac12A(w)\mathrm{Var}(X)$: a $w=10$ ($A_1=1/10>1/20$) paga di più l'agente 1; a $w=40$ ($A_1=1/40<1/20$) l'agente 2.
:::::

::::: {.callout kind="warning" heading="A.4 · Errore tipico"}
Un agente può pagare di più a una ricchezza e di meno a un'altra senza essere «più avverso»: la definizione chiede la disuguaglianza fra le avversioni assolute a ogni livello di ricchezza, e qui l'ordine si inverte in $W=20$.
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
Per $\tilde y$ poco disperso e $R_f=1$, la formula $\phi=-\mathrm{Cov}(\tilde y,\tilde M)/P$ si approssima con $\phi\approx RR(\mu)\,\mathrm{Var}(\tilde y)/\mu^2$, $\mu=E[\tilde y]$. Per la CRRA $RR=\gamma$: $\phi\approx\gamma\,\mathrm{Var}(\tilde y)/E[\tilde y]^2$. *(ERA 06, «Dati osservati e calibrazione del modello»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Con $\mathrm{Var}(\tilde y)/E[\tilde y]^2=0{,}0009$ e $\gamma=5$:
$$\phi\approx5\cdot0{,}0009=0{,}0045=0{,}45\%.$$
Per un premio osservato del 4,5%: $\gamma\cdot0{,}0009=0{,}045$, cioè $\gamma=0{,}045/0{,}0009=50$.

Controllo (script): per $\tilde y=1\pm3\%$ con probabilità $1/2$ il premio esatto a $\gamma=5$ è $0{,}449\%$, quindi l'approssimazione è buona. A $\gamma=50$ non lo è più: per quei due valori il premio esatto è $2{,}79\%$ e non $4{,}5\%$. Per $\gamma$ grande la nota osserva uno scostamento, di verso opposto, che dipende dalla distribuzione: lì il valore esatto supera l'approssimazione ($2{,}86\%$ contro $2{,}24\%$ a $\gamma=40$), qui sta sotto ($2{,}79\%$ contro $4{,}5\%$). La domanda chiede il valore ottenuto con l'approssimazione.
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
$\phi\approx\gamma\,\mathrm{Var}(\tilde y)/E[\tilde y]^2=5\cdot0{,}0009=0{,}0045$, cioè $0{,}45\%$ (approssimazione). Per $4{,}5\%$: $\gamma\approx0{,}045/0{,}0009=50$, un'avversione relativa altissima: è l'*equity premium puzzle*.
:::::

::::: {.callout kind="warning" heading="B.1 · Errore tipico"}
$0{,}0009$ è già il quadrato del coefficiente di variazione ($\sigma/\mu=3\%$): non va elevato di nuovo al quadrato. Il risultato $0{,}45\%$ è un decimo del $4{,}5\%$ osservato.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
Con $u=\ln$ e $\alpha=1$ la FOC dà $P=E[\tilde y\,u'(\tilde y)]/(R_f\,E[u'(\tilde y)])=1/E[1/\tilde y]$, perché $\tilde y\,u'(\tilde y)=1$ *(ERA 06, «L'offerta e il prezzo di equilibrio»)*. Con integrazione la FOC del titolo $A$, $E[(\tilde y^A-P)/W]=0$, dà $P=E[\tilde y^A/W]/E[1/W]$. *(ERA 06, «Due paesi»)* *(ERA 06, «Il premio al rischio di mercato con integrazione»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
(i) Autarchia. $E[1/\tilde y]=\tfrac12\big(1+\tfrac13\big)=\tfrac23$, quindi $P=3/2$. Poi $E[\tilde y]=2$, $R=2/(3/2)=4/3$ e $\phi=R-R_f=1/3$.

(ii) Integrazione. La ricchezza $W=(\tilde y^A+\tilde y^B)/2$ vale $1$, $2$, $2$, $3$ con probabilità $1/4$ ciascuna (coppie $(1,1)$, $(1,3)$, $(3,1)$, $(3,3)$), quindi
$$E[1/W]=\tfrac14\Big(1+\tfrac12+\tfrac12+\tfrac13\Big)=\frac7{12},\qquad E[\tilde y^A/W]=\tfrac14\Big(1+\tfrac12+\tfrac32+1\Big)=1.$$
Il prezzo è $P=1/(7/12)=12/7\approx1{,}7143$, il rendimento atteso è $R=2/(12/7)=7/6$ e $\phi=1/6\approx0{,}1667$.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
(i) Autarchia: $\phi=1/3\approx0{,}3333$. (ii) Integrazione: $\phi=1/6\approx0{,}1667$.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
Con $u=\ln$ e due valori equiprobabili $a$ e $b$ il dimezzamento di $\phi$ è esatto per qualunque coppia: $\phi$ passa da $(a-b)^2/(4ab)$ a $(a-b)^2/(8ab)$, e con $1$ e $3$ da $1/3$ a $1/6$. Non è però una regola generale, perché dipende dalla forma di $u$ ($\ln$) e non dalla scelta dei numeri: con $u=-1/W$ ($\gamma=2$) e gli stessi valori, lo script dà $P=6/5$ e $\phi=2/3$ in autarchia, $P=42/29$ e $\phi=8/21$ con integrazione, con rapporto $4/7\approx0{,}5714$.
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
Con $\alpha_i=1$ per ogni titolo la ricchezza è $\tilde y$ e valgono $R_fP_i=E[\tilde y_i\tilde M]$ ed $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$, con $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$. Il segno del premio è quello di $-\mathrm{Cov}(\tilde R_i,\tilde M)$, non quello della correlazione con $\tilde y$. *(ERA 06, «Il pricing kernel»)* *(ERA 06, «Il premio al rischio di mercato di ciascun titolo»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
Con $u'(y)=1/y$ nei tre stati ($\tilde y=1,\,3,\,6$): $u'=\big(1,\tfrac13,\tfrac16\big)$ e $E[u']=\tfrac13\cdot\tfrac32=\tfrac12$. Il kernel è $\tilde M=u'/E[u']=2/\tilde y$:
$$\tilde M=\Big(2;\ \tfrac23;\ \tfrac13\Big),\qquad E[\tilde M]=1.$$
Prezzo: $P_a=E[\tilde y_a\tilde M]/R_f=\tfrac13\big(1\cdot2+0+1\cdot\tfrac13\big)=\dfrac79\approx0{,}7778$. Rendimento lordo: $\tilde R_a=\tilde y_a/P_a=\big(\tfrac97;\,0;\,\tfrac97\big)$, con
$$E[\tilde R_a]=\tfrac13\cdot\tfrac{18}7=\frac67\approx0{,}8571,\qquad E[\tilde R_a]-R_f=-\frac17\approx-0{,}1429.$$
Verifica: $E[\tilde R_a\tilde M]=1=R_f$ e $\mathrm{Cov}(\tilde R_a,\tilde M)=1-\tfrac67=\tfrac17$, quindi il premio è $-\mathrm{Cov}(\tilde R_a,\tilde M)=-\tfrac17$.

Il segno: $\mathrm{Cov}(\tilde R_a,\tilde y)=\tfrac17>0$, ma anche $\mathrm{Cov}(\tilde R_a,\tilde M)=\tfrac17>0$, perché il titolo $a$ paga nello stato 1, dove $\tilde y$ è basso e $\tilde M$ è alto. Per il teorema il premio è negativo: il titolo copre l'agente nello stato in cui l'utilità marginale è alta.

Unicità. Con tre stati i titoli $a$ e $b=(0;3;5)$ non sono collineari: il determinante della matrice delle covarianze è $25/27\neq0$ e l'ipotesi di unicità delle note vale *(ERA 06, «Il modello con $n$ titoli»)*.
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
$\tilde M=2/\tilde y$; $P_a=7/9\approx0{,}7778$ €; premio $E[\tilde R_a]-R_f=-1/7\approx-0{,}1429$: negativo, perché $\mathrm{Cov}(\tilde R_a,\tilde M)=1/7>0$, benché $\tilde R_a$ sia correlato positivamente con $\tilde y$.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
La correlazione positiva con $\tilde y$ implica un premio non negativo se $\tilde R_a$ è una funzione non decrescente di $\tilde y$ (allora $\mathrm{Cov}(\tilde R_a,\tilde M)\le0$). Qui non lo è: $\tilde R_a$ è alto negli stati 1 e 3 e nullo nel 2, e conta la covarianza con $\tilde M$, che nello stato 1 è alto.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
$\phi=-\mathrm{Cov}(\tilde y^A,\tilde M)/P$. Con l'integrazione il kernel dipende da $W=(\tilde y^A+\tilde y^B)/2$, con $\mathrm{Var}(W)=\mathrm{Var}(\tilde y)/2$ perché i valori sono i.i.d. *(ERA 06, «Il premio al rischio di mercato con integrazione»)*
:::::

::::: {.callout kind="example" heading="B.4 · Svolgimento"}
In autarchia il kernel è $u'(\tilde y^A)/E[u'(\tilde y^A)]$ e varia con il valore del titolo domestico: è alto quando $\tilde y^A$ è basso e covaria fortemente con $\tilde y^A$. Con l'integrazione ciascun agente diversifica, la sua ricchezza $W$ è meno variabile e il kernel $u'(W)/E[u'(W)]$ lo è altrettanto: la sua covarianza con $\tilde y^A$ è minore in valore assoluto, e con essa il premio $\phi$. La nota lo mostra con un calcolo esatto per l'utilità quadratica (la covarianza si dimezza) e numericamente per la CRRA; non ha una dimostrazione generale. Nei dati di B.2 il premio passa da $1/3$ a $1/6$.
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
Con l'integrazione ciascuno tiene metà di ciascun titolo: il kernel dipende da $W=(\tilde y^A+\tilde y^B)/2$, con varianza $\mathrm{Var}(\tilde y)/2$, e non da $\tilde y^A$. Come mostrano la nota e B.2, la sua covarianza con $\tilde y^A$ è minore in valore assoluto e, poiché $\phi=-\mathrm{Cov}(\tilde y^A,\tilde M)/P$, il premio scende e anche $P$ sale (in B.2 $\phi$: $1/3\to1/6$; $P$: $3/2\to12/7$).
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$F_2$ domina $F_1$ al primo ordine se $F_2(x)\le F_1(x)$ per ogni $x$; allora $E_{F_2}[u(X)]\ge E_{F_1}[u(X)]$ per ogni $u$ crescente, e con $u$ strettamente crescente e $F_2<F_1$ su un intervallo la disuguaglianza è stretta. *(ERA 04, «Dominanza stocastica del primo ordine»)* *(ERA 04, «Due lotterie uniformi»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Le c.d.f. sono $F_1(x)=(x-2)/4$ su $[2,6]$ e $F_2(x)=(x-4)/3$ su $[4,7]$, nulle a sinistra e uguali a 1 a destra. Nei punti $2,\,4,\,6,\,7$ valgono
$$F_1=\Big(0;\ \tfrac12;\ 1;\ 1\Big),\qquad F_2=\Big(0;\ 0;\ \tfrac23;\ 1\Big).$$
Fra un punto e il successivo le c.d.f. sono lineari, quindi basta il confronto nei punti: $F_2\le F_1$ ovunque, con disuguaglianza stretta in $(2,7)$ (su $[4,6]$ equivale a $(x-4)/3\le(x-2)/4$, cioè $x\le10$). Le medie sono $4$ e $11/2$, coerenti con il verso della dominanza.
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
$X_2$: la sua c.d.f. sta sotto quella di $X_1$ in ogni punto ($F_2(x)\le F_1(x)$, strettamente in $(2,7)$), cioè $X_2$ domina $X_1$ al primo ordine; ogni $u$ strettamente crescente preferisce $X_2$.
:::::

::::: {.callout kind="warning" heading="C.1 · Errore tipico"}
La media maggiore ($11/2>4$) è solo una condizione necessaria: la dominanza richiede $F_2\le F_1$ in ogni punto. Qui vale, ma va verificata, non dedotta dalla media o dalla lunghezza del supporto.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
La FOSD ordina le utilità attese per l'intera classe delle $u$ crescenti, senza altre condizioni sulla curvatura: la concavità serve alla SOSD, non alla FOSD. *(ERA 04, «Quale ordine per quale classe di utilità»)* *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Per ogni $u$ derivabile
$$E_{F_2}[u(X)]-E_{F_1}[u(X)]=\int u'(t)\,\big[F_1(t)-F_2(t)\big]\,dt,$$
e il segno dipende solo da $u'\ge0$ e da $F_1-F_2\ge0$. Una $u$ convessa è crescente come ogni altra, quindi rientra nella classe: la scelta resta $X_2$, e con $u$ strettamente crescente la preferenza è stretta.
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
$X_2$: la FOSD ordina le utilità attese per ogni $u$ crescente, convessa compresa, perché in $\int u'(t)\,[F_1(t)-F_2(t)]\,dt$ servono solo $u'\ge0$ e $F_2\le F_1$. L'amore per il rischio non cambia la scelta.
:::::

::::: {.callout kind="warning" heading="C.2 · Errore tipico"}
Con una $u$ convessa l'ordine di una coppia ordinata solo dalla SOSD si inverte (come per $Z_1$ e $Z_2$ in C.4, dove $e^x$ preferisce $Z_2$); quello di una coppia ordinata dalla FOSD, come qui, no: il primo ordine implica il secondo e non richiede la concavità.
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
Se $Z_2\overset{d}{=}Z_1+\tilde\varepsilon$ con $E[\tilde\varepsilon\mid z_1]=0$ (mean-preserving spread), allora $Z_1$ domina $Z_2$ al secondo ordine e ogni $u$ crescente e concava preferisce $Z_1$, per la disuguaglianza di Jensen. *(ERA 04, «Il *mean-preserving spread*»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
Le medie coincidono ($10$) e le distribuzioni sono diverse: la FOSD è esclusa, e infatti le c.d.f. si incrociano nella media. Sia $\tilde\varepsilon\sim\mathcal N(0,5)$ indipendente da $Z_1$: la somma di normali indipendenti ha media e varianza che si sommano, quindi $Z_1+\tilde\varepsilon\sim\mathcal N(10,\,4+5)=\mathcal N(10,9)$, la distribuzione di $Z_2$. Per l'indipendenza $E[\tilde\varepsilon\mid z_1]=0$: $Z_2$ è un mean-preserving spread di $Z_1$, quindi $Z_1$ domina $Z_2$ al secondo ordine. La preferenza è stretta perché $u$ è strettamente concava e $Z$ non è degenere (la Jensen stretta va oltre l'enunciato debole delle note).

Controlli dello script (non fanno parte della teoria delle note): l'integrale della c.d.f. di $Z_2$ sta sopra quello di $Z_1$ ovunque (a distanza $0{,}3989$ nella media). Con $u(x)=-e^{-x}$, strettamente crescente e concava, l'integrazione numerica dà $E[u(Z_1)]=-0{,}000335$ e $E[u(Z_2)]=-0{,}004087$, in accordo con la forma chiusa $-e^{-\mu+\sigma^2/2}$ della funzione generatrice dei momenti, che le note non hanno.
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
$Z_1$: $Z_2\overset d=Z_1+\tilde\varepsilon$ con $\tilde\varepsilon\sim\mathcal N(0,5)$ indipendente, quindi $E[\tilde\varepsilon\mid z_1]=0$: $Z_2$ è un mean-preserving spread di $Z_1$, che domina al secondo ordine; un agente strettamente avverso preferisce $Z_1$.
:::::

::::: {.callout kind="warning" heading="C.3 · Errore tipico"}
Il secondo parametro di $\mathcal N(\mu,\sigma^2)$ è la varianza: $Z_2$ ha varianza $9$ e deviazione standard $3$. La varianza del rumore è la differenza, $9-4=5$, non $3-2$.
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
La SOSD ordina solo le $u$ crescenti e concave; per una $u$ crescente qualunque serve la FOSD, che a medie uguali e distribuzioni diverse non vale in nessun verso. *(ERA 04, «Quale ordine per quale classe di utilità»)* *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
Le medie sono uguali e le distribuzioni diverse, quindi nessuna delle due domina l'altra al primo ordine. Fra le $u$ crescenti, le concave preferiscono $Z_1$ (C.3), ma una convessa inverte l'ordine. Poiché $Z_2$ è un mean-preserving spread di $Z_1$ (C.3), per ogni $v$ concava $E[v(Z_2)]\le E[v(Z_1)]$ *(ERA 04, «Il *mean-preserving spread*»)*; con $v=-u$ e $u$ convessa si ottiene $E[u(Z_2)]\ge E[u(Z_1)]$. Un esempio è $u(x)=e^x$, strettamente crescente e strettamente convessa su tutto $\mathbb R$, il supporto delle normali: l'agente preferisce $Z_2$.

Controllo dello script (integrazione numerica, in accordo con la forma chiusa $e^{\mu+\sigma^2/2}$ della funzione generatrice dei momenti, che le note non hanno): $E[e^{Z_1}]=e^{12}\approx162\,755$ e $E[e^{Z_2}]=e^{14{,}5}\approx1\,982\,759$.

La classe delle utilità crescenti non concorda su un ordine: la risposta non è univoca.
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
No: dalla sola crescenza non segue; con $u=e^x$ (crescente e convessa) si preferisce $Z_2$ ($e^{14{,}5}>e^{12}$), con $u$ concava $Z_1$.
:::::

::::: {.callout kind="warning" heading="C.4 · Errore tipico"}
La classe delle $u$ strettamente crescenti contiene anche la funzione lineare (concava e convessa insieme), con cui l'agente è indifferente fra $Z_1$ e $Z_2$ (medie uguali): oltre al verso, può mancare perfino la preferenza stretta.
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
La compagnia sceglie $(p,B_0,\dots,B_L)$ per massimizzare il profitto atteso con $e=1$ fissato, soggetta a PC (utilità almeno $\bar u$) e a IC (il cliente preferisce $e=1$ alla sola deviazione, $e'=0$). Gli indennizzi non dipendono da $e$, quindi $z_l$ è lo stesso nei due membri di IC. *(ERA 08, «Informazione asimmetrica»)* *(ERA 08, «Lagrangiana e condizioni del primo ordine»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
Con $z_l=w-p-l+B_l$ il profitto è $p-\sum_l\pi_l(1)B_l$ (premio incassato meno indennizzi attesi sotto $e=1$). PC chiede che l'utilità con $e=1$ non sia minore di $\bar u$; IC che non sia minore di quella che il cliente ottiene scegliendo $e=0$ con la stessa polizza. Poiché a parità di utilità sceglie l'impegno voluto, la disuguaglianza di IC è debole.
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
$$\max_{p,\,B_0,\dots,B_L}\ p-\sum_{l=0}^{L}\pi_l(1)\,B_l\quad\text{s.t.}\quad
\begin{cases}
g_{PC}=\sum_{l}\pi_l(1)\,u(z_l)-d(1)-\bar u\ \ge\ 0,\\[2pt]
g_{IC}=\sum_{l}\pi_l(1)\,u(z_l)-d(1)-\Big[\sum_{l}\pi_l(0)\,u(z_l)-d(0)\Big]\ \ge\ 0,
\end{cases}$$
con $z_l=w-p-l+B_l$.
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
In IC le probabilità cambiano ($\pi_l(1)$ a sinistra, $\pi_l(0)$ a destra) ma la polizza è la stessa, perché la compagnia non osserva $e$: scrivere un'altra polizza a destra, o un obiettivo con $\pi_l(0)$, è sbagliato.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
Un vincolo attivo è un vincolo che la compagnia non vorrebbe allentare: se fosse lasco potrebbe migliorare il profitto. IC dipende dalla polizza solo attraverso le $u(z_l)$, con pesi $\pi_l(1)-\pi_l(0)$ che sommano a 0. *(ERA 08, «Che cosa significa il risultato»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
PC. Se il cliente avesse più di $\bar u$, la compagnia potrebbe abbassare gli indennizzi in modo da ridurre della stessa quantità $u(z_l)$ in ogni stato: PC resterebbe valido, IC non cambierebbe perché $\sum_l[\pi_l(1)-\pi_l(0)]=0$ e il profitto salirebbe. Quindi all'ottimo PC è attivo.

IC. Un incentivo più forte del necessario richiede una ricchezza più sensibile alla perdita, cioè più rischio per un cliente avverso. La compagnia, che deve comunque garantirgli $\bar u$, dovrebbe compensarlo e guadagnerebbe meno: all'ottimo il cliente è indifferente fra i due impegni.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
PC: con più di $\bar u$ la compagnia potrebbe abbassare gli indennizzi, riducendo $u(z_l)$ della stessa quantità in ogni stato; IC non cambia (i pesi $\pi_l(1)-\pi_l(0)$ sommano a 0) e il profitto sale. IC: un incentivo più forte espone il cliente a più rischio, che va compensato per garantirgli $\bar u$: profitto minore.
:::::

::::: {.callout kind="warning" heading="D.2 · Errore tipico"}
Non basta dire che «un vincolo attivo è soddisfatto con uguaglianza»: la domanda chiede perché la compagnia non vuole di più, e la ragione è economica (il profitto aumenterebbe allentando il vincolo, o diminuirebbe stringendolo).
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
$u$ strettamente concava rende $u'$ strettamente decrescente, quindi iniettiva: $u'(z)=u'(z')$ implica $z=z'$. Per la polizza ottima con $e=1$ la (5) lega $z_l$ a $r_l$. La normalizzazione $B_0=0$ si impone dopo le condizioni del primo ordine. *(ERA 08, «Lagrangiana e condizioni del primo ordine»)* *(ERA 08, «La proprietà del rapporto di verosimiglianza monotono»)*
:::::

::::: {.callout kind="example" heading="D.3 · Svolgimento"}
Se $r_1=r_0$ i secondi membri della condizione coincidono per $l=0$ e $l=1$, quindi $1/u'(z_1)=1/u'(z_0)$, cioè $u'(z_1)=u'(z_0)$ e, per l'iniettività di $u'$, $z_1=z_0$. Con $z_l=w-p-l+B_l$:
$$-1+B_1=-0+B_0=0\quad\Longrightarrow\quad B_1=1=l.$$
Il cliente ha la stessa ricchezza finale $w-p$ senza perdita e con la perdita 1: la perdita 1 è coperta per intero. È il motivo per cui la MLR della nota richiede la crescita stretta di $r_l$: con $r_l$ strettamente crescente $B_l<l$ per ogni $l\ge1$ (copertura parziale).
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
Con $r_1=r_0$ i secondi membri della condizione coincidono per $l=0,1$, quindi $u'(z_1)=u'(z_0)$ e, essendo $u'$ iniettiva, $z_1=z_0$: $B_1-1=B_0=0$, cioè $B_1=1$. La perdita 1 è coperta per intero (copertura piena, non parziale).
:::::

::::: {.callout kind="warning" heading="D.3 · Errore tipico"}
Il risultato «$B_l<l$ per $l\ge1$» dipende dalla stretta crescita di $r_l$: senza di essa, due perdite con lo stesso rapporto $r_l$ ricevono la stessa ricchezza finale. Anche $B_0=0$ non è un dato del problema: è una normalizzazione lecita perché la traslazione $(p,B_l)\to(p+c,B_l+c)$ non cambia $z_l$ né il profitto.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
$V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$; con $u=-e^{-\lambda w}/\lambda$ si ha $u'(w)=e^{-\lambda w}$. Se $u_2=\phi\circ u_1$ con $\phi$ strettamente concava e $\alpha_2^*<W$, allora $\alpha_2^*<\alpha_1^*$. *(ERA 05, «La condizione del primo ordine»)* *(ERA 05, «Avversione al rischio e investimento»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
Rendimenti in eccesso: $\tilde x=\tilde x_0-r$ vale $-15\%-5\%=-\tfrac15$ oppure $35\%-5\%=\tfrac3{10}$, con $E[\tilde x]=5\%>0$, quindi $\alpha^*>0$.

FOC. $\tfrac12\cdot\tfrac3{10}\,e^{-\lambda(w_0+0{,}3\alpha)}-\tfrac12\cdot\tfrac15\,e^{-\lambda(w_0-0{,}2\alpha)}=0$. Il fattore $e^{-\lambda w_0}$ si semplifica:
$$\tfrac3{10}\,e^{-0{,}3\lambda\alpha}=\tfrac15\,e^{0{,}2\lambda\alpha}\ \Longrightarrow\ e^{0{,}5\lambda\alpha}=\frac32\ \Longrightarrow\ \alpha^*=\frac{2\ln(3/2)}{\lambda},$$
indipendente da $w_0$. Per $\lambda_1=0{,}02$: $\alpha_1^*=100\ln\tfrac32$; per $\lambda_2=0{,}04$: $\alpha_2^*=50\ln\tfrac32$. Con $\ln(3/2)\approx0{,}405$ si ha $\alpha_1^*\approx40{,}5$ e $\alpha_2^*\approx20{,}3$ (valori esatti dello script: $40{,}5465$ e $20{,}2733$).

Interni, a mano: da $1<3/2<e$ segue $0<\ln(3/2)<1$, quindi $0<\alpha_1^*=100\ln\tfrac32<100$ e $0<\alpha_2^*=\alpha_1^*/2<50<100$, cioè $0<\alpha_i^*<W$ (lo script lo conferma con il massimizzatore numerico).

Trasformazione. $u_1=-50\,e^{-0{,}02w}$, quindi $e^{-0{,}04w}=\big(e^{-0{,}02w}\big)^2=u_1^2/2500$ e $u_2=-25\,e^{-0{,}04w}=-u_1^2/100$. Dunque $\phi(t)=-0{,}01\,t^2$ per $t<0$ (dove $u_1$ prende valori), con $\phi'(t)=-0{,}02\,t>0$ e $\phi''(t)=-0{,}02<0$: $\phi$ è strettamente concava e l'agente 2 è più avverso.

Il teorema dice allora $\alpha_2^*<\alpha_1^*$ (essendo $\alpha_2^*<W$), ed è coerente: $\alpha_2^*=\alpha_1^*/2$.
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
FOC: $E[\tilde x\,e^{-\lambda(w_0+\alpha\tilde x)}]=0$, cioè $e^{\lambda\alpha/2}=3/2$, da cui $\alpha^*=2\ln(3/2)/\lambda$ (indipendente da $w_0$). $\alpha_1^*=100\ln(3/2)\approx40{,}5$ e $\alpha_2^*=50\ln(3/2)\approx20{,}3$ (con $\ln(3/2)\approx0{,}405$; esatti $40{,}55$ e $20{,}27$), entrambi in $(0,100)$ perché $1<3/2<e$. Vale $u_2=\phi(u_1)$ con $\phi(t)=-0{,}01\,t^2$, strettamente concava: il teorema dà $\alpha_2^*<\alpha_1^*$ (minore), e i numeri lo confermano.
:::::

::::: {.callout kind="warning" heading="E.1 · Errore tipico"}
La FOC va scritta con il rendimento in eccesso $\tilde x=\tilde x_0-r$ ($-20\%$ o $+30\%$), non con il rendimento netto $\tilde x_0$ ($-15\%$ o $+35\%$): con $\tilde x_0$ il rapporto sotto il logaritmo sarebbe diverso e anche $E[\tilde x]$ (10% invece di 5%).
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
Poiché $D>0$, il segno di $\partial\alpha^*/\partial w_0$ è l'opposto di quello dell'attesa $N=E[\tilde x\{-u''(w_0+\alpha^*\tilde x)\}]$, e con $-u''=A\,u'$ si ha $N=E[A(w_0+\alpha^*\tilde x)\,\tilde x\,u'(w_0+\alpha^*\tilde x)]$. Il DARA è $A'\le0$. *(ERA 05, «Ricchezza iniziale e investimento»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*Passo 1: riduzione.* Poiché $D>0$, $\partial\alpha^*/\partial w_0=-N/D$. Basta mostrare $N\le0$ con DARA e $N<0$ con DARA stretta.

*Passo 2: confronto stato per stato.* Sia $x\neq0$ una realizzazione di $\tilde x$. Poiché $\alpha^*>0$ (ottimo interno): se $x>0$ è $w_0+\alpha^*x>w_0$ e, con $A$ decrescente, $A(w_0+\alpha^*x)\le A(w_0)$; se $x<0$ è $w_0+\alpha^*x<w_0$ e $A(w_0+\alpha^*x)\ge A(w_0)$. In entrambi i casi $x\,[A(w_0+\alpha^*x)-A(w_0)]\le0$. Moltiplicando per $u'(w_0+\alpha^*x)>0$:
$$A(w_0+\alpha^*x)\,x\,u'(w_0+\alpha^*x)\ \le\ A(w_0)\,x\,u'(w_0+\alpha^*x),$$
con disuguaglianza stretta per $x\neq0$ se $A$ è strettamente decrescente; per $x=0$ vale l'uguaglianza.

*Passo 3: attesa e FOC.* Prendendo l'attesa e usando la condizione del primo ordine,
$$N\ \le\ A(w_0)\,E\big[\tilde x\,u'(w_0+\alpha^*\tilde x)\big]=0.$$
Se $A$ è strettamente decrescente la disuguaglianza è stretta, perché $\tilde x\neq0$ con probabilità positiva: $N<0$.

*Passo 4: conclusione.* $\partial\alpha^*/\partial w_0=-N/D\ge0$, e $>0$ con DARA stretta.

Controllo numerico (script): con $u=\ln$ ($A'=-1/w^2<0$), i rendimenti in eccesso di E.1 e $w_0=105$, l'ottimo è $\alpha^*=87{,}5$ e la formula $-N/D$ dà $\partial\alpha^*/\partial w_0=0{,}8333$, uguale alla derivata numerica di $\alpha^*(w_0)$: positiva, come previsto dalla DARA stretta.
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
Poiché $D>0$, basta mostrare $N=E[\tilde x\{-u''\}]\le0$. Con $-u''=A\,u'$ e $\alpha^*>0$, per ogni $x\neq0$ vale $A(w_0+\alpha^*x)\,x\,u'(\cdot)\le A(w_0)\,x\,u'(\cdot)$ (per $x>0$ è $A$ minore, per $x<0$ maggiore, e il segno di $x$ rimette l'ordine). Prendendo l'attesa e usando la FOC, $N\le A(w_0)\cdot0=0$: dunque $\partial\alpha^*/\partial w_0=-N/D\ge0$. Con $A'<0$ le disuguaglianze sono strette per $x\neq0$, e $N<0$, cioè $\partial\alpha^*/\partial w_0>0$.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
Il segno meno davanti a $N/D$: l'investimento cresce con la ricchezza se $N$ è negativa. Con CARA, $A$ è costante, $N=0$ e $\alpha^*$ non dipende da $w_0$ (come in E.1): il DARA debole include la CARA, quello stretto no.
:::::
