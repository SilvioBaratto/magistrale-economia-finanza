---
title: "Economia del Rischio — appello simulato 03: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 03, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
$A(W)=-u''(W)/u'(W)$ e $RR(W)=W\,A(W)$. Un'utilità è CARA se $A$ non dipende da $W$, CRRA se $RR$ non dipende da $W$. *(ERA 03, «Avversione assoluta e avversione relativa»)* *(ERA 03, «Le funzioni CARA e CRRA»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
Con $u(W)=-e^{-\lambda W}/\lambda$ si ha $u'=e^{-\lambda W}$, $u''=-\lambda e^{-\lambda W}$, $u'''=\lambda^{2}e^{-\lambda W}$, quindi
$$A(W)=\frac{\lambda e^{-\lambda W}}{e^{-\lambda W}}=\lambda=2,\qquad RR(W)=W\,A(W)=\lambda W=2W.$$
$A$ è costante: l'utilità è CARA. $RR=2W$ cresce con $W$: non è costante, quindi l'utilità non è CRRA.
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
$A(W)=2$ (costante) e $RR(W)=2W$ (crescente in $W$). L'utilità è CARA, non è CRRA.
:::::

::::: {.callout kind="warning" heading="A.1 · Errore tipico"}
$\lambda=2$ è l'avversione assoluta, non quella relativa: per avere $RR$ si moltiplica per $W$. Per questo $RR$ non è costante e l'utilità non può essere anche CRRA.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
L'equivalente certo è la ricchezza certa $CE$ con $u(CE)=E[u(w+X)]$; con $E[X]=0$ il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)* Con utilità CARA $E[u(w+X)]=-e^{-\lambda w}\,E[e^{-\lambda X}]/\lambda$. *(ERA 03, «Condizioni equivalenti per il DARA»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
La lotteria ha valore atteso $\tfrac14\big(-\tfrac32\ln2\big)+\tfrac34\cdot\tfrac12\ln2=0$. Con $\lambda=2$, $e^{-\lambda X}=e^{3\ln2}=8$ se $X=-\tfrac32\ln2$ e $e^{-\lambda X}=e^{-\ln2}=\tfrac12$ se $X=\tfrac12\ln2$, quindi
$$E\big[e^{-\lambda X}\big]=\tfrac14\cdot8+\tfrac34\cdot\tfrac12=2+\tfrac38=\frac{19}{8}.$$
Da $-\tfrac{e^{-\lambda w}}{\lambda}\cdot\tfrac{19}{8}=-\tfrac{e^{-\lambda CE}}{\lambda}$ segue $e^{\lambda(w-CE)}=\tfrac{19}{8}$, cioè
$$R=\frac{\ln(19/8)}{\lambda}=\tfrac12\ln\tfrac{19}{8}\approx0{,}4325,\qquad CE=5-0{,}4325\approx4{,}5675.$$
Il premio non dipende da $w$: vale $0{,}4325$ anche a $w=1$ e a $w=20$ (script).
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
$R=\tfrac12\ln\tfrac{19}{8}\approx0{,}4325$ €; $CE=5-\tfrac12\ln\tfrac{19}{8}\approx4{,}5675$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
$CE$ è una ricchezza, non un guadagno: non è $-0{,}4325$ ma $w-R$. E nell'equazione $e^{\lambda R}=19/8$ il fattore $1/\lambda$ si applica dopo il logaritmo: $R=\ln(19/8)/\lambda$.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
Vale $A'(W)=A(W)\,[A(W)-P(W)]$, quindi con $A>0$ l'utilità è DARA (in senso debole) se e solo se $P\ge A$; ed è DARA se e solo se il premio $R(w,X)$ non cresce con $w$, per ogni $X$ a media nulla. *(ERA 03, «Prudenza e avversione assoluta»)* *(ERA 03, «Condizioni equivalenti per il DARA»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
$P(W)=-\dfrac{\lambda^{2}e^{-\lambda W}}{-\lambda e^{-\lambda W}}=\lambda=2$ e $A'(W)=\dfrac{d}{dW}\,2=0$. Verifica: $A(A-P)=2\,(2-2)=0=A'$.

Poiché $A'=0\le0$, l'utilità è DARA nel senso debole dei Dati (la CARA è il caso di bordo: $P=A$); non lo è in senso stretto, perché $A'<0$ non vale. Per il teorema sul DARA, $A'\le0$ equivale a $\partial R/\partial w\le0$ per ogni lotteria a media nulla: il premio non può crescere con la ricchezza. Per la CARA è anzi costante (nei calcoli dello script $0{,}4325$ a $w=1,\ 5,\ 20$).
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
$P(W)=2=A(W)$ e $A'(W)=0=A(A-P)$. Sì, è DARA nel senso debole (CARA, caso di bordo). No: il premio non può crescere con $w$, perché $A'\le0$ equivale a $\partial R/\partial w\le0$; con la CARA è costante.
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
La risposta «sì, DARA» dipende dalla convenzione: con $A'<0$ stretto la CARA non sarebbe DARA. La conclusione sul premio, invece, non cambia: $\partial R/\partial w\le0$ vale in ogni caso, ma solo con DARA stretta il premio decresce davvero.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
Se $E[X]=0$, anche $kX$ ha media nulla e il suo premio $R(k)$ soddisfa $R(k)=\tfrac12A(w)\,E[X^{2}]\,k^{2}+o(k^{2})$ per $k\to0$. *(ERA 03, «Il premio per lotterie piccole»)* Il passaggio dal confronto fra premi al confronto fra avversioni è l'implicazione $(3)\Rightarrow(2)$ del teorema di equivalenza. *(ERA 03, «Dal premio per il rischio all'avversione assoluta»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
Si fissano $w$ e una lotteria $X$ non degenere con $E[X]=0$ e con un numero finito di valori, per esempio quella di A.2: il passo $(3)\Rightarrow(2)$ lo richiede perché $R$ sia due volte derivabile. Per questa lotteria $E[X^{2}]>0$. Per ogni $k\ge0$ la lotteria $kX$ ha ancora media nulla, quindi l'ipotesi dà $R_2(k)\ge R_1(k)$, dove $R_i(k)$ è il premio dell'agente $i$ per $kX$. Per l'approssimazione di Arrow-Pratt $R_i(k)=\tfrac12A_i(w)\,E[X^{2}]\,k^{2}+o(k^{2})$ per $k\to0$. Si divide per $k^{2}$ e si passa al limite per $k\to0$:
$$\tfrac12A_2(w)\,E[X^{2}]\ \ge\ \tfrac12A_1(w)\,E[X^{2}],$$
e poiché $E[X^{2}]>0$ ne segue $A_2(w)\ge A_1(w)$. La ricchezza $w$ è arbitraria, quindi $A_2(W)\ge A_1(W)$ per ogni $W$. Esempio (script): per la lotteria di A.2 e l'agente dei Dati $E[X^{2}]=0{,}3603$ e $R''(0)=A\,E[X^{2}]=0{,}7207$, uguale alla derivata seconda numerica, cioè $R(k)\approx0{,}3603\,k^{2}$ (qui $\tfrac12A=1$, quindi il coefficiente coincide con $E[X^{2}]$) per $k$ piccolo.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
Sì. Per $kX$, con $X$ non degenere a media nulla e con un numero finito di valori (così $R$ è due volte derivabile), $R_2(k)\ge R_1(k)$ e $R_i(k)=\tfrac12A_i(w)\,E[X^{2}]\,k^{2}+o(k^{2})$. Dividendo per $k^{2}$ e facendo $k\to0$ si ottiene $A_2(w)\ge A_1(w)$, perché $E[X^{2}]>0$; $w$ è arbitraria.
:::::

::::: {.callout kind="warning" heading="A.4 · Errore tipico"}
Serve la disuguaglianza per tutte le lotterie $kX$ con $k\to0$: il confronto fra i premi di una sola lotteria fissata non dice nulla su $A_2$ e $A_1$. Per dividere serve anche $E[X^{2}]>0$, cioè una lotteria non degenere.
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
La lotteria composta $\alpha Q_a+(1-\alpha)Q_b$ ha probabilità $\pi_s=\alpha\pi_s^a+(1-\alpha)\pi_s^b$ e valore atteso $\alpha E[Q_a]+(1-\alpha)E[Q_b]$. *(ERA 02, «Lotterie semplici e composte»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Con $\alpha=\tfrac13$:
$$\pi_1=\tfrac13\cdot0+\tfrac23\cdot\tfrac34=\tfrac12,\qquad\pi_2=\tfrac13\cdot\tfrac14+\tfrac23\cdot\tfrac14=\tfrac14,\qquad\pi_3=\tfrac13\cdot\tfrac34+\tfrac23\cdot0=\tfrac14.$$
La lotteria semplice è $Q=(\tfrac12,\tfrac14,\tfrac14)$ e $E[Q]=\tfrac12\cdot1+\tfrac14\cdot25+\tfrac14\cdot81=27$. Controllo per linearità: $E[Q_a]=67$, $E[Q_b]=7$ e $\tfrac13\cdot67+\tfrac23\cdot7=27$.
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
$Q=(\tfrac12,\tfrac14,\tfrac14)$, $E[Q]=27$ €.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
$CE=u^{-1}\big(E[u(Q)]\big)$. Poiché $E[Q]\neq0$, ERA 03 definisce il premio solo per lotterie a media nulla: qui, per i Dati, $R=E[Q]-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
$u(1)=1$, $u(25)=5$, $u(81)=9$, quindi $E[u(Q)]=\tfrac12\cdot1+\tfrac14\cdot5+\tfrac14\cdot9=4$. Da $\sqrt{CE}=4$ segue $CE=16$, e $R=27-16=11$. Come deve essere per $u$ concava, $CE\le E[Q]$.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
$E[u(Q)]=4$, $CE=16$ €, $R=E[Q]-CE=27-16=11$ €.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
$4$ è un'utilità, non un importo: l'equivalente certo si ottiene invertendo $u$, cioè elevando al quadrato.
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
L'utilità max-min di una scommessa è il minimo, al variare del modello di probabilità nell'insieme $\mathcal M$, della sua utilità attesa. *(ERA 02, «Avversione all'ambiguità»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
Con $u(81)=9$ e $u(1)=1$, una scommessa che paga 81 € con probabilità $q$ ha utilità attesa $1+8q$. In $\mathcal M$ la probabilità di rossa è $\tfrac25$ e quella di blu $b\in[\tfrac15,\tfrac35]$, con verde $\tfrac35-b$.

- $T_1$ (rossa): $q=\tfrac25$ per ogni modello, quindi $U_{\min}=1+\tfrac{16}5=\tfrac{21}5=4{,}2$.
- $T_2$ (blu): $q=b$, minimo in $b=\tfrac15$: $U_{\min}=1+\tfrac85=\tfrac{13}5=2{,}6$.
- $T_3$ (rossa o verde): $q=\tfrac25+\big(\tfrac35-b\big)=1-b\in[\tfrac25,\tfrac45]$, minimo in $b=\tfrac35$: $U_{\min}=\tfrac{21}5=4{,}2$.
- $T_4$ (blu o verde): $q=\tfrac35$ per ogni modello, quindi $U_{\min}=1+\tfrac{24}5=\tfrac{29}5=5{,}8$.

L'agente max-min sceglie $T_1$ ($4{,}2$) su $T_2$ ($2{,}6$) e $T_4$ ($5{,}8$) su $T_3$ ($4{,}2$): sono le scelte del soggetto.
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
$U_{\min}(T_1)=\tfrac{21}5=4{,}2$, $U_{\min}(T_2)=\tfrac{13}5=2{,}6$, $U_{\min}(T_3)=\tfrac{21}5=4{,}2$, $U_{\min}(T_4)=\tfrac{29}5=5{,}8$. Sì: sceglie $T_1$ su $T_2$ e $T_4$ su $T_3$, come il soggetto.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
Il minimo si prende sull'utilità attesa al variare del modello, non sui premi: sui premi $T_1$ e $T_2$ avrebbero lo stesso minimo, $u(1)$, e $T_1\succ T_2$ non sarebbe spiegata.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
Il teorema dell'utilità attesa vale per preferenze fra lotterie con probabilità oggettive e note; le sue ipotesi sulle preferenze sono completezza, transitività, continuità e indipendenza. *(ERA 02, «Il teorema dell'utilità attesa»)* Nell'esperimento di Ellsberg l'inconsistenza riguarda qualunque assegnazione di probabilità soggettive. *(ERA 02, «Il paradosso di Ellsberg»)*
:::::

::::: {.callout kind="example" heading="B.4 · Svolgimento"}
Sia $b$ la probabilità soggettiva di blu, con $\mathbb P(\text{rossa})=\tfrac25$ e $\mathbb P(\text{verde})=\tfrac35-b$. Poiché $u(81)>u(1)$:

- $T_1\succ T_2$ equivale a $\tfrac25>b$;
- $T_4\succ T_3$ equivale a $\mathbb P(\text{blu o verde})=\tfrac35>1-b=\mathbb P(\text{rossa o verde})$, cioè $b>\tfrac25$.

Le due condizioni si contraddicono per ogni $b$ (lo script verifica che a $b=\tfrac25$ i due confronti sono pareggi) e non dipendono da $u$. L'agente max-min non ha una sola probabilità: valuta $T_2$ con $b=\tfrac15$ e $T_3$ con $b=\tfrac35$. Manca quindi il presupposto di probabilità oggettive e note: la composizione blu/verde è ignota.
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
Con $b=\mathbb P(\text{blu})$ e $\mathbb P(\text{rossa})=\tfrac25$ (e $u(81)>u(1)$): $T_1\succ T_2$ richiede $b<\tfrac25$, $T_4\succ T_3$ richiede $\tfrac35>1-b$, cioè $b>\tfrac25$: contraddizione per ogni $b$. Manca il presupposto di probabilità oggettive e note: qui la composizione blu/verde è ignota.
:::::

::::: {.callout kind="warning" heading="B.4 · Errore tipico"}
Il difetto non è l'avversione al rischio: la contraddizione vale per ogni $u$ crescente. Non è nemmeno l'indipendenza del teorema: quell'assioma confronta lotterie con probabilità note e qui non si applica; manca proprio una probabilità per il blu. È l'avversione all'ambiguità, cioè la preferenza per probabilità note, a non essere rappresentabile con un'unica probabilità soggettiva.
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$F_2$ domina $F_1$ al primo ordine se $F_2(x)\le F_1(x)$ per ogni $x$; allora ogni $u$ crescente dà $E_{F_2}[u]\ge E_{F_1}[u]$. Con un solo agente colpito, la variazione di reddito con $N$ membri è $(-B/N,\,p;\ 0,\,1-p)$. *(ERA 04, «Applicazione: condivisione del rischio con un solo agente colpito»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Per l'agente 1, $S=(-400,\tfrac15;\ 0,\tfrac45)$ e $G=(-200,\tfrac15;\ 0,\tfrac45)$. Le c.d.f. nei valori $-400,\ -200,\ 0$ sono $\big(\tfrac15,\tfrac15,1\big)$ per $S$ e $\big(0,\tfrac15,1\big)$ per $G$: quella di $G$ non sta mai sopra, ed è più bassa in $-400$. Quindi $G$ domina $S$ al primo ordine. Direttamente: $E[u\mid G]-E[u\mid S]=\tfrac15\,[u(-200)-u(-400)]>0$ perché $u$ è strettamente crescente.
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
Sì: G. La c.d.f. di G, $(0,\tfrac15,1)$, sta sotto quella di S, $(\tfrac15,\tfrac15,1)$: G domina S al primo ordine, e ogni $u$ crescente preferisce G (la perdita scende da 400 a 200 con la stessa probabilità).
:::::

::::: {.callout kind="warning" heading="C.1 · Errore tipico"}
Basta che $u$ sia crescente: la concavità non serve, perché la dominanza è del primo ordine. Con una $u$ solo crescente la risposta resta G.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
Stesso criterio di C.1, con i ruoli scambiati: per l'agente 2 la lotteria da cui parte è degenere in $0$. *(ERA 04, «Applicazione: condivisione del rischio con un solo agente colpito»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Per l'agente 2, $S$ è $0$ con certezza e $G=(-200,\tfrac15;\ 0,\tfrac45)$. Le c.d.f. nei valori $-200,\ 0$ sono $(0,1)$ per $S$ e $\big(\tfrac15,1\big)$ per $G$: quella di $S$ non sta mai sopra, quindi $S$ domina $G$ al primo ordine. Direttamente: $u(0)-E[u\mid G]=\tfrac15\,[u(0)-u(-200)]>0$. Entrando nella comunità l'agente 2 non ha alcun vantaggio, ma si espone a una perdita di 200.
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
Sì: S. Da solo l'agente 2 ha $0$ con certezza, con c.d.f. $(0,1)$ sotto quella di G, $(\tfrac15,1)$: S domina G al primo ordine. Nella comunità si espone a una perdita di 200 senza alcun vantaggio: la risposta è opposta a quella di C.1.
:::::

::::: {.callout kind="warning" heading="C.2 · Errore tipico"}
La condivisione non elimina il rischio, lo ridistribuisce: conviene a chi è esposto e costa a chi non lo è. Non va estesa a tutti la risposta di C.1.
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
Con medie uguali e distribuzioni diverse la dominanza del primo ordine è esclusa in entrambi i versi. Con shock indipendenti la variazione di reddito di un membro è $-B\,K/N$, con $K$ binomiale. *(ERA 04, «Dominanza stocastica del primo ordine»)* *(ERA 04, «Applicazione: condivisione del rischio con shock indipendenti»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
Con $N=1$: $(-400,\tfrac15;\ 0,\tfrac45)$. Con $N=2$ i colpiti sono 0, 1 o 2, con probabilità $\tfrac{16}{25}$, $\tfrac{8}{25}$, $\tfrac1{25}$: $(-400,\tfrac1{25};\ -200,\tfrac8{25};\ 0,\tfrac{16}{25})$. Le medie coincidono, $-80$. Le c.d.f. nei valori $-400,\ -200,\ 0$ sono $\big(\tfrac15,\tfrac15,1\big)$ per $N=1$ e $\big(\tfrac1{25},\tfrac9{25},1\big)$ per $N=2$: si incrociano ($\tfrac15>\tfrac1{25}$ in $-400$, $\tfrac15<\tfrac9{25}$ in $-200$), quindi nessuna domina l'altra.

Due utilità crescenti ordinano le situazioni in modo opposto (script): $u(x)=-(x-100)^{2}$, crescente e concava per $x<100$, dà $-58000$ con $N=1$ e $-45200$ con $N=2$ (preferisce $N=2$); $u(x)=(x+400)^{2}$, crescente e convessa per $x>-400$, dà $128000$ con $N=1$ e $115200$ con $N=2$ (preferisce $N=1$).
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
No. Le medie coincidono ($-80$) e le distribuzioni sono diverse: le c.d.f. si incrociano ($\tfrac15>\tfrac1{25}$ in $-400$, $\tfrac15<\tfrac9{25}$ in $-200$), nessuna FOSD. Utilità crescenti diverse ordinano in modo opposto: una concava preferisce $N=2$, una convessa $N=1$.
:::::

::::: {.callout kind="warning" heading="C.3 · Errore tipico"}
Con $N=2$ la dispersione diminuisce, ma una varianza minore non basta a far preferire $N=2$ a ogni $u$ crescente: lo fa solo con la concavità (C.4).
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
$F_1$ è un *mean-preserving spread* di $F_2$ se $X_1\overset d=X_2+\varepsilon$ con $E[\varepsilon\mid x_2]=0$ per ogni $x_2$; allora $F_2$ domina $F_1$ al secondo ordine e ogni $u$ concava (crescente) preferisce $F_2$. *(ERA 04, «Il *mean-preserving spread*»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
Si parte da $N=2$, $(-400,\tfrac1{25};\ -200,\tfrac8{25};\ 0,\tfrac{16}{25})$, e si aggiunge un rumore $\varepsilon$: nullo se il valore è $-400$ o $0$; pari a $-200$ o $+200$, con probabilità $\tfrac12$ ciascuno, se il valore è $-200$. Ha media condizionata nulla in ogni caso. Si ottiene
$$\mathbb P(-400)=\tfrac1{25}+\tfrac12\cdot\tfrac8{25}=\tfrac15,\qquad\mathbb P(0)=\tfrac{16}{25}+\tfrac12\cdot\tfrac8{25}=\tfrac45,$$
cioè la distribuzione con $N=1$. Dunque $N=1$ è un *mean-preserving spread* di $N=2$, e $N=2$ domina $N=1$ al secondo ordine. Poiché il rumore è diverso da zero con probabilità $\tfrac8{25}>0$ e $u$ è strettamente concava, la preferenza per $N=2$ è stretta (Jensen condizionale).
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
$N=2$: aggiungendo al valore $-200$ un rumore $\pm200$ equiprobabile (nullo altrove, media condizionata nulla) si ottiene $N=1$, che è un *mean-preserving spread* di $N=2$; ogni $u$ strettamente concava preferisce $N=2$.
:::::

::::: {.callout kind="warning" heading="C.4 · Errore tipico"}
Il rumore deve avere media condizionata nulla, non solo media nulla: qui dipende dal valore di $X^{(2)}$, perché è nullo agli estremi e $\pm200$ al centro. Un rumore indipendente dal valore non riprodurrebbe la distribuzione con $N=1$.
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
La pendenza della curva di indifferenza è il saggio marginale di sostituzione fra indennizzo e premio: il premio che il consumatore è disposto a pagare per un'unità in più di indennizzo. Si ricava dal differenziale totale di $EU$ posto a zero. *(ERA 07, «Preferenze e single-crossing»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
Si pongono $a=u'(w-p-L+B)>0$ e $b=u'(w-p)>0$. Le derivate parziali sono $EU_B=\pi\,a$ ed $EU_p=-\pi\,a-(1-\pi)\,b$. Lungo la curva di indifferenza $EU_B\,dB+EU_p\,dp=0$, quindi
$$s=\frac{dp}{dB}=-\frac{EU_B}{EU_p}=\frac{\pi\,a}{\pi\,a+(1-\pi)\,b}.$$
A $(B,p)$ fissato $a$ e $b$ sono fissati e il denominatore ha derivata $a-b$ rispetto a $\pi$:
$$\frac{\partial s}{\partial\pi}=\frac{a\,[\pi a+(1-\pi)b]-\pi a\,(a-b)}{[\pi a+(1-\pi)b]^{2}}=\frac{a\,b}{[\pi a+(1-\pi)b]^{2}}>0.$$
Nello stesso contratto la curva di indifferenza dell'alto rischio ha dunque pendenza maggiore di quella del basso rischio (single-crossing): le due curve si incrociano al più una volta. L'alto rischio ha più probabilità di incassare l'indennizzo e ne offre di più.

Esempio (script, $u=\ln$, $w=20$, $L=8$, contratto $(B,p)=(3;\,0{,}5)$): per $\pi=0{,}1$ e $\pi=0{,}4$ la pendenza è $0{,}1300$ e $0{,}4727$; in $\pi=0{,}4$ vale $\partial s/\partial\pi=1{,}0386$, uguale alla derivata numerica.
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
Con $a=u'(w-p-L+B)$ e $b=u'(w-p)$: $EU_B=\pi a$, $EU_p=-\pi a-(1-\pi)b$ e $s=\dfrac{dp}{dB}=\dfrac{\pi a}{\pi a+(1-\pi)b}$. A $(B,p)$ fissato $\dfrac{\partial s}{\partial\pi}=\dfrac{ab}{[\pi a+(1-\pi)b]^{2}}>0$. Nello stesso contratto la curva dell'alto rischio è più ripida di quella del basso rischio (single-crossing).
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
La derivata in $\pi$ si calcola a $(B,p)$ fissato, perché $a$ e $b$ dipendono solo dal contratto: la domanda confronta due tipi nello stesso punto, non due punti della stessa curva. La pendenza è $dp/dB$ (premio su indennizzo), non $dB/dp$.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
La pendenza della curva del tipo $\pi$ è $\pi a/(\pi a+(1-\pi)b)$ e quella della sua retta di profitto nullo è $\pi$. Se $B=L$ i due argomenti di $u'$ coincidono, $a=b$, e le due pendenze sono uguali. *(ERA 07, «Il contratto per l'alto rischio prevede la copertura piena»)* *(ERA 07, «Ogni contratto sta sulla propria retta di profitto nullo»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
Il contratto dell'alto rischio è $(B,\overline\pi B)$ e sta sulla retta $p=\overline\pi B$, di pendenza $\overline\pi$. La curva di indifferenza passante per quel punto ha pendenza $\overline\pi a/[\overline\pi a+(1-\overline\pi)b]$.

- Se $B=L$: $w-p-L+B=w-p$, quindi $a=b$ e la pendenza è $\overline\pi$. La curva è tangente alla retta e sta sotto di essa da entrambi i lati: sulla retta la ricchezza attesa è costante, $w-\overline\pi L$, e il rischio è minimo in $B=L$, quindi gli altri contratti della retta valgono meno per l'alto rischio. I contratti equivalenti hanno premio più basso e profitto negativo: nessuna deviazione conviene.
- Se $B<L$: $w-p-L+B<w-p$ e $u'$ decrescente danno $a>b$, quindi la pendenza supera $\overline\pi$. Se $B>L$ vale $a<b$ e la pendenza è minore di $\overline\pi$. In entrambi i casi la curva attraversa la retta: da un lato, sopra la retta, ci sono contratti equivalenti per l'alto rischio con profitto positivo. Riducendo di poco il premio diventano strettamente preferiti, con profitto ancora positivo.

In questo secondo caso l'altra compagnia li offre e attira l'alto rischio: il contratto non resta in equilibrio. L'unico punto della retta senza deviazione è $B=L$. Esempio (script, $u=\ln$, $w=20$, $L=8$, $\overline\pi=0{,}4$): sulla retta $p=0{,}4\,B$ la pendenza della curva dell'alto rischio è $0{,}4600$ in $B=4$, $0{,}4000$ in $B=8=L$ e $0{,}3455$ in $B=12$.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
Nel contratto $(B,\overline\pi B)$ la pendenza della curva di indifferenza dell'alto rischio è uguale a quella della retta $p=\overline\pi B$, cioè $\overline\pi$, solo se $B=L$ (allora i due stati hanno la stessa ricchezza). Se $B\neq L$ la curva attraversa la retta: da un lato ci sono contratti equivalenti con profitto positivo, che l'altra compagnia offre riducendo di poco il premio. Resiste solo $B=L$.
:::::

::::: {.callout kind="warning" heading="D.2 · Errore tipico"}
Non basta dire che la copertura piena «elimina il rischio»: la ragione è che solo con $B=L$ la curva è tangente alla retta e non esiste una deviazione redditizia. Va escluso anche $B>L$ (sovra-assicurazione), dove la pendenza è minore di $\overline\pi$ e la curva attraversa comunque la retta.
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
Con prezzo unico e $\pi$ uniforme su $[0,1]$ l'equilibrio $p^*=L$ non conclude nessuna transazione utile: nessun miglioramento paretiano viene realizzato. *(ERA 07, «La selezione avversa»)* Nel modello di screening il contratto nullo $(0,0)$ è sempre disponibile. *(ERA 07, «Il modello di screening»)* Nell'equilibrio separante l'alto rischio ottiene il first best (copertura piena a prezzo equo) e il basso rischio un second best, con copertura parziale $\overline B_l<L$. *(ERA 07, «Esistenza e proprietà dell'equilibrio separante»)*
:::::

::::: {.callout kind="example" heading="D.3 · Svolgimento"}
*Rispetto all'esito in cui nessuno si assicura.* Le compagnie hanno profitto nullo in entrambi i casi. Il contratto $(0,0)$ è sempre disponibile, quindi nessun tipo sta peggio con l'equilibrio separante che senza polizza; resta da vedere se ciascuno sta strettamente meglio.

- Alto rischio: con $(L,\overline\pi L)$ ha la ricchezza certa $w-\overline\pi L$, uguale alla ricchezza attesa senza polizza. Per Jensen stretta (certo contro rischioso) $u(w-\overline\pi L)$ supera l'utilità attesa senza polizza.
- Basso rischio: il contratto di equilibrio $(\overline B_l,\underline\pi\overline B_l)$ ha $0<\overline B_l<L$ (copertura parziale): $\overline B_l>0$ per ipotesi e $\overline B_l<L$ come in D.2, perché con $B=L$ al premio equo $\underline\pi L<\overline\pi L$ l'alto rischio preferirebbe quel contratto al proprio. Sulla retta di profitto nullo $p=\underline\pi B$ la sua utilità attesa è $EU(B)=EU(B,\underline\pi B;\underline\pi)=\underline\pi\,u\big(w-L+(1-\underline\pi)B\big)+(1-\underline\pi)\,u\big(w-\underline\pi B\big)$, con derivata $\dfrac{dEU}{dB}=\underline\pi(1-\underline\pi)\,[u'(a)-u'(b)]$, dove $a=w-L+(1-\underline\pi)B$ è la ricchezza nello stato di perdita e $b=w-\underline\pi B$ quella senza perdita. Per $B<L$ si ha $a<b$, quindi $u'(a)>u'(b)$ per la stretta concavità e $dEU/dB>0$ su $[0,L)$: $EU(\overline B_l)>EU(0)$, e $EU(0)$ è l'utilità attesa senza polizza.

Nessuno sta peggio e ciascun tipo sta strettamente meglio: è un miglioramento paretiano.

*Rispetto all'informazione perfetta.* Se le compagnie osservano il tipo, il basso rischio può avere la copertura piena equa $(L,\underline\pi L)$, che preferisce strettamente al contratto con $\overline B_l<L$; l'alto rischio conserva il proprio contratto e le compagnie restano a profitto nullo. Questa allocazione è fattibile con tipi osservabili e migliora l'equilibrio separante: rispetto a quelle allocazioni l'esito non è Pareto efficiente, e il costo dell'informazione privata ricade sul basso rischio, che ha una copertura parziale.
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
Sì: $(0,0)$ è sempre disponibile, quindi nessuno sta peggio. L'alto rischio ha la ricchezza certa $w-\overline\pi L$ e, per Jensen stretta, sta meglio; il basso rischio ($0<\overline B_l<L$) sta meglio: lungo $p=\underline\pi B$ l'utilità attesa cresce con $B<L$ ($u'$ decrescente). No rispetto all'informazione perfetta: il basso rischio avrebbe la copertura piena equa, preferita, senza danneggiare nessuno.
:::::

::::: {.callout kind="warning" heading="D.3 · Errore tipico"}
La Jensen stretta serve solo per l'alto rischio, che ha una ricchezza certa da confrontare con una rischiosa. Il basso rischio ha una copertura parziale e resta rischioso: «a parità di media è meno disperso» non basta, serve il segno di $dEU/dB$ lungo la retta $p=\underline\pi B$, positivo per $B<L$. Inoltre «efficiente» richiede l'insieme di riferimento: fra i contratti con profitto nullo che l'alto rischio non preferisce al proprio, quello del basso rischio è il migliore possibile (second best), e l'inefficienza c'è solo rispetto alle allocazioni fattibili con tipi osservabili.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
$V'(\alpha)=E[\tilde x\,u'(w_0+\alpha\tilde x)]$ e la condizione del primo ordine in un ottimo interno è $V'(\alpha^*)=0$. *(ERA 05, «La condizione del primo ordine»)* Se $u_2=\phi\circ u_1$ con $\phi$ strettamente concava e $\alpha_2^*<W$, allora $\alpha_2^*<\alpha_1^*$. *(ERA 05, «Avversione al rischio e investimento»)* Con CRRA l'ammontare è proporzionale alla ricchezza. *(ERA 05, «Ricchezza iniziale e investimento»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
Il rendimento in eccesso è $\tilde x=\tilde x_0-r$, cioè $-0{,}3-0{,}1=-\tfrac25$ oppure $1-0{,}1=\tfrac9{10}$, con probabilità $\tfrac12$: $E[\tilde x]=\tfrac14>0$ (infatti $E[\tilde x_0]=0{,}35>r$), quindi $\alpha^*>0$. La condizione del primo ordine è
$$\tfrac12\big(-\tfrac25\big)\,u'\big(w_0-\tfrac25\alpha\big)+\tfrac12\cdot\tfrac9{10}\,u'\big(w_0+\tfrac9{10}\alpha\big)=0\iff4\,u'\big(w_0-\tfrac25\alpha\big)=9\,u'\big(w_0+\tfrac9{10}\alpha\big).$$

*Logaritmo*, $u'(c)=1/c$: $\dfrac4{w_0-0{,}4\alpha}=\dfrac9{w_0+0{,}9\alpha}$, cioè $4w_0+3{,}6\alpha=9w_0-3{,}6\alpha$ e
$$\alpha^*=\frac{5\,w_0}{7{,}2}=\frac{25}{36}\,w_0.$$

*Utilità $v(c)=-1/c$*, $v'(c)=c^{-2}$: $\dfrac4{(w_0-0{,}4\alpha)^{2}}=\dfrac9{(w_0+0{,}9\alpha)^{2}}$, cioè $\Big(\dfrac{w_0+0{,}9\alpha}{w_0-0{,}4\alpha}\Big)^{2}=\dfrac94$. Le due ricchezze sono positive, quindi il rapporto è $\tfrac32$: $2w_0+1{,}8\alpha=3w_0-1{,}2\alpha$ e
$$\alpha^*=\frac{w_0}{3}.$$

Con $w_0=W(1+r)=1{,}1\,W$ si ha $\alpha^*_{\ln}=\tfrac{25}{36}\cdot\tfrac{11}{10}\,W=\tfrac{55}{72}\,W\approx0{,}7639\,W$ e $\alpha^*_v=\tfrac{11}{30}\,W\approx0{,}3667\,W$ (script). Entrambi sono minori di $W$: le soluzioni sono interne e rispettano il vincolo $\alpha\le W$, che riguarda la ricchezza investibile $W$, non $w_0$. L'ammontare è proporzionale a $w_0$ e la quota $\alpha^*/w_0$ è costante, $\tfrac{25}{36}\approx0{,}6944$ e $\tfrac13$ (script: con $W=100$, cioè $w_0=110$, gli ammontari sono $76{,}39$ e $36{,}67$; con $W=200$, cioè $w_0=220$, sono $152{,}78$ e $73{,}33$).

Ordine fra i due: $v(c)=-1/c=\phi(\ln c)$ con $\phi(t)=-e^{-t}$, $\phi'=e^{-t}>0$ e $\phi''=-e^{-t}<0$, strettamente concava. L'agente con $v$ è più avverso ($A_v(c)=2/c>1/c=A_{\ln}(c)$). Per il teorema, se $\alpha_v^*<W$ vale $\alpha_v^*<\alpha_{\ln}^*$ per ogni $w_0$ e ogni distribuzione con $E[\tilde x]>0$: l'ordine non dipende dai dati ($\tfrac{11}{30}W<\tfrac{55}{72}W$ è solo la sua verifica).
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
FOC: $E[\tilde x\,u'(w_0+\alpha^*\tilde x)]=0$, cioè $4u'(w_0-0{,}4\alpha)=9u'(w_0+0{,}9\alpha)$. Con $\ln$: $\alpha^*=\tfrac{25}{36}w_0\approx0{,}764\,W$. Con $v=-1/c$: $\big(\tfrac{w_0+0{,}9\alpha}{w_0-0{,}4\alpha}\big)^{2}=\tfrac94$, $\alpha^*=\tfrac13w_0\approx0{,}367\,W$. Entrambi sono $<W$. L'ammontare cresce in proporzione a $w_0$ e la quota è costante ($\tfrac{25}{36}$ e $\tfrac13$).

L'agente con $v$ investe meno: $v=\phi(\ln)$ con $\phi(t)=-e^{-t}$ strettamente concava ($A_v(c)=2/c>1/c$), quindi per il teorema $\alpha_v^*<\alpha_{\ln}^*$ per ogni $w_0$ e ogni distribuzione con $E[\tilde x]>0$ e ottimo interno.
:::::

::::: {.callout kind="warning" heading="E.1 · Errore tipico"}
Il vincolo è $\alpha\le W$, non $\alpha\le w_0$: con $r>0$ è $w_0=W(1+r)>W$, quindi $\tfrac{25}{36}<1$ non basta e va controllato $\tfrac{25}{36}(1+r)=\tfrac{55}{72}\le1$. Inoltre i due numeri $\tfrac{25}{36}$ e $\tfrac13$ valgono per questi dati, mentre l'ordine segue dal teorema. Con altri dati la soluzione della FOC per $\ln$ può superare $W$: allora $\alpha^*=W$, con $V'(W)\ge0$.
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
La funzione $h(y)=y\,u'(w_0+y)$ è crescente se $RR<1$ e concava se $RP<2$ e $P>0$; $P=-u'''/u''$ e $RP=c\,P$ sono valutate nella ricchezza finale $w_0+y$. Le condizioni sono sufficienti, non necessarie. *(ERA 05, «Quando la funzione è concava»)* *(ERA 05, «Condizioni per un investimento minore»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*(i)* $h'(y)=u'(w_0+y)+y\,u''(w_0+y)$ e
$$h''(y)=2u''(w_0+y)+y\,u'''(w_0+y).$$
Da $u'''=-P\,u''$ e da $y=(w_0+y)-w_0$ si ha $y\,u'''=-\big[(w_0+y)P-w_0P\big]u''=-\big[RP-w_0P\big]u''$, con $RP$ e $P$ in $w_0+y$. Quindi
$$h''(y)=u''(w_0+y)\,\big[2-RP(w_0+y)+w_0P(w_0+y)\big]=-u''(w_0+y)\,\big[RP(w_0+y)-2-w_0P(w_0+y)\big].$$

*(ii)* Poiché $u''<0$, $h''\le0$ equivale a $2-RP+w_0P\ge0$. Se $RP<2$ allora $2-RP>0$; se $P>0$ e $w_0>0$ allora $w_0P>0$. La somma è positiva, quindi $h''<0$ e $h$ è strettamente concava.

*(iii)* Per $u(c)=c^{1-\gamma}/(1-\gamma)$: $u'=c^{-\gamma}$, $u''=-\gamma c^{-\gamma-1}$, $u'''=\gamma(\gamma+1)c^{-\gamma-2}$, quindi $RR=\gamma$, $P=(1+\gamma)/c>0$ per ogni $\gamma>0$ e $RP=1+\gamma$. $RR<1$ e $RP<2$ equivalgono entrambe a $\gamma<1$: le tre condizioni valgono per $0<\gamma<1$. (Script: $\gamma=0{,}5$ dà $RR=0{,}5$ e $RP=1{,}5$; $\gamma=2$ dà $RR=2$ e $RP=3$.)

*(iv)* Per il logaritmo $RR=1$ e $RP=2$: le condizioni non valgono. Ma $h(y)=\dfrac{y}{w_0+y}$, quindi
$$h'(y)=\frac{w_0}{(w_0+y)^{2}}>0,\qquad h''(y)=-\frac{2w_0}{(w_0+y)^{3}}<0.$$
Nella formula del punto (i), $P(c)=2/c$ dà $2-RP+w_0P=2w_0/(w_0+y)>0$: il termine $w_0P$ compensa $RP=2$. Perciò $h$ è crescente e concava anche per il logaritmo, e la conclusione sull'investimento vale lo stesso. Lo script confronta la formula di $h''$ con le differenze finite per $\gamma=0{,}5,\ 1,\ 2$ in tre valori di $y$ ($w_0=10$).
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
(i) $h''(y)=2u''(w_0+y)+y\,u'''(w_0+y)=-u''(w_0+y)\,\big[RP(w_0+y)-2-w_0P(w_0+y)\big]$, usando $u'''=-Pu''$ e $y=(w_0+y)-w_0$.

(ii) Con $u''<0$, $h''\le0$ equivale a $2-RP+w_0P\ge0$: se $RP<2$ e $P>0$ vale $2-RP>0$ e $w_0P>0$, quindi $h''<0$ e $h$ è concava.

(iii) CRRA: $RR=\gamma$, $P=(1+\gamma)/c>0$, $RP=1+\gamma$: le tre condizioni valgono se e solo se $0<\gamma<1$.

(iv) Logaritmo ($RR=1$, $RP=2$): $h(y)=y/(w_0+y)$, $h'=w_0/(w_0+y)^{2}>0$ e $h''=-2w_0/(w_0+y)^{3}<0$: $h$ è crescente e concava anche se le condizioni non valgono.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
$P$ e $RP$ vanno valutate nella ricchezza finale $w_0+y$: scrivere $y=(w_0+y)-w_0$ è ciò che fa comparire $w_0P$, e senza quel termine il logaritmo sembrerebbe un caso a parte. Le condizioni $RP<2$ e $P>0$ sono solo sufficienti: non vale il contrario, e per $\gamma\ge1$ non si può concludere che $h$ non sia concava.
:::::
