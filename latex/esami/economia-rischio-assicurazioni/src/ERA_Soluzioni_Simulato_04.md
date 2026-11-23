---
title: "Economia del Rischio — appello simulato 04: soluzioni"
subtitle: "Svolgimento degli esercizi e risposte da scrivere in esame"
stats: "17 domande svolte"
disclaimer: "Soluzioni dell'appello simulato 04, preparate a fini di studio. Non sono soluzioni ufficiali del docente."
---

# Domanda A (20 punti)

::::: {.callout kind="tip" heading="A.1 · Richiamo"}
$A=-u''/u'$ e $RR=W\,A$. L'utilità quadratica è quella con $u'(W)=a-bW$, qui $a=1$ e $b=1/c$: ha $u''=-b$ costante e $u'''=0$. *(ERA 03, «Avversione assoluta e avversione relativa»)* *(ERA 06, «Il premio al rischio di mercato con integrazione»)*
:::::

::::: {.callout kind="example" heading="A.1 · Svolgimento"}
$$u'(W)=1-\frac Wc=\frac{c-W}c,\qquad u''(W)=-\frac1c,\qquad u'''(W)=0.$$
$$A(W)=\frac{1/c}{(c-W)/c}=\frac1{c-W}=\frac1{100-W},\qquad RR(W)=W\,A(W)=\frac W{100-W}.$$
Nei due livelli di ricchezza delle domande seguenti (output dello script): $A(65)=1/35$ e $A(84)=1/16$, $RR(65)=13/7\approx1{,}8571$ e $RR(84)=21/4=5{,}25$. Né $A$ né $RR$ sono costanti, quindi l'utilità non è né CARA né CRRA.
:::::

::::: {.callout kind="success" heading="A.1 · Risposta"}
$A(W)=1/(100-W)$ e $RR(W)=W/(100-W)$. CARA: no, $A$ dipende da $W$ e cresce con $W$ ($1/35$ in 65, $1/16$ in 84). CRRA: no, $RR$ dipende da $W$ ($13/7$ in 65, $21/4$ in 84).
:::::

::::: {.callout kind="warning" heading="A.1 · Errore tipico"}
$u''$ costante non vuol dire $A$ costante: $A=-u''/u'$ ha $u'$ al denominatore, e qui $u'=(c-W)/c$ cala al crescere di $W$, quindi $A$ cresce.
:::::

::::: {.callout kind="tip" heading="A.2 · Richiamo"}
$CE$ è la ricchezza certa con $u(CE)=E[u(w+X)]$; poiché $E[X]=0$, il premio è $R=w-CE$. *(ERA 03, «Equivalente certo e premio per il rischio»)*
:::::

::::: {.callout kind="example" heading="A.2 · Svolgimento"}
Si scrive $u(W)=\big[c^2-(c-W)^2\big]/(2c)$. Con $E[X]=0$, $E\big[(c-w-X)^2\big]=(c-w)^2+E[X^2]$, quindi
$$E[u(w+X)]=\frac{c^2-(c-w)^2-E[X^2]}{2c}.$$
Uguagliando a $u(CE)=[c^2-(c-CE)^2]/(2c)$ si ottiene $(c-CE)^2=(c-w)^2+E[X^2]$. Con $w_1=65$ e $E[X^2]=12^2$: $(c-CE_1)^2=35^2+12^2=37^2$, cioè $c-CE_1=37$ (la radice positiva, perché $CE_1<c$). Dunque $CE_1=63$ e $R_1=65-63=2$.
:::::

::::: {.callout kind="success" heading="A.2 · Risposta"}
$CE_1=63$ €, $R_1=2$ €.
:::::

::::: {.callout kind="warning" heading="A.2 · Errore tipico"}
L'approssimazione $R\approx\tfrac12A(w)\,E[X^2]$ dà $\tfrac12\cdot\tfrac1{35}\cdot144\approx2{,}0571$, non $2$: la lotteria non è piccola rispetto a $c-w=35$, e l'approssimazione sovrastima il premio esatto.
:::::

::::: {.callout kind="tip" heading="A.3 · Richiamo"}
$A'(w)=A(w)\,[A(w)-P(w)]$: l'utilità è DARA se e solo se $P\ge A$, e per il teorema questo equivale a un premio non crescente con la ricchezza per ogni lotteria a media nulla. Se $u$ non è DARA il teorema non impone che il premio cali. *(ERA 03, «Prudenza e avversione assoluta»)* *(ERA 03, «Condizioni equivalenti per il DARA»)* *(ERA 03, «Come varia il premio con la ricchezza»)*
:::::

::::: {.callout kind="example" heading="A.3 · Svolgimento"}
Per $w_2=84$: $(c-CE_2)^2=16^2+12^2=20^2$, quindi $CE_2=80$ e $R_2=84-80=4$.

Per la prudenza: $u'''=0$ e $u''=-1/c\neq0$, quindi $P(W)=-u'''/u''=0$. Per $A'$:
$$A'(W)=\frac{d}{dW}\,\frac1{100-W}=\frac1{(100-W)^2}=A(W)^2>0,$$
in accordo con $A(A-P)=A^2$ (lo script lo conferma per differenze finite). Poiché $P=0<A$ e $A'>0$, $u$ non è DARA: $A'\le0$ è falsa per ogni $W$.

Confronto: $R_2=4>R_1=2$, quindi sì. Poiché $u$ non è DARA, il teorema non impone che il premio cali con la ricchezza: $R_2>R_1$ è compatibile con esso.

C'è di più: con $P(W)<A(W)$ per ogni $W<100$, il ragionamento che lega $\partial R/\partial w$ a $A-P$, percorso al contrario, dà un premio crescente con la ricchezza per ogni lotteria a media nulla *(ERA 03, «Come varia il premio con la ricchezza»)*. Dunque $R_2>R_1$ non è un caso: per questa $u$ il premio cresce con la ricchezza per ogni lotteria, e un premio che cresce per una sola lotteria basta a escludere il DARA.
:::::

::::: {.callout kind="success" heading="A.3 · Risposta"}
$R_2=4$ €, $P(W)=0$, $A'(W)=1/(100-W)^2>0$. Sì, $R_2=4>R_1=2$: $u$ non è DARA ($P=0<A$, $A'>0$), quindi il teorema non impone che il premio cali con la ricchezza e l'aumento è compatibile con esso.
:::::

::::: {.callout kind="warning" heading="A.3 · Errore tipico"}
Il teorema sul DARA non dice che il premio cala sempre con la ricchezza: lo garantisce solo se $A'\le0$. Qui $A'>0$ e la condizione manca; letto al contrario, il teorema dice che un premio che cresce per una sola lotteria ($R_1=2$, $R_2=4$) basta a escludere il DARA.
:::::

::::: {.callout kind="tip" heading="A.4 · Richiamo"}
Se $u$ è concava vale la disuguaglianza di Jensen, $E[u(Y)]\le u\big(E[Y]\big)$. Il premio è definito, per $E[X]=0$, da $E[u(w+X)]=u(CE)=u(w-R)$. *(ERA 03, «Equivalente certo e premio per il rischio»)* *(ERA 03, «Avversione al rischio e concavità»)*
:::::

::::: {.callout kind="example" heading="A.4 · Svolgimento"}
Per Jensen applicata alla ricchezza finale $w+X$, con $E[w+X]=w$ perché $E[X]=0$:
$$u(w-R)=E[u(w+X)]\le u\big(E[w+X]\big)=u(w).$$
Poiché $u$ è crescente, $u(w-R)\le u(w)$ implica $w-R\le w$, cioè $R\ge0$. Se $u$ è strettamente concava e $X$ non è degenere, Jensen è stretta e $R>0$.
:::::

::::: {.callout kind="success" heading="A.4 · Risposta"}
Per Jensen, con $u$ concava e $E[X]=0$: $E[u(w+X)]\le u\big(E[w+X]\big)=u(w)$. Poiché $E[u(w+X)]=u(CE)$, si ha $u(CE)\le u(w)$ e, $u$ essendo strettamente crescente, $CE\le w$: dunque $R=w-CE\ge0$.
:::::

::::: {.callout kind="warning" heading="A.4 · Errore tipico"}
Senza $E[X]=0$ nessun segno è garantito: $w-CE$ include l'effetto della media (è negativa se la lotteria ha media positiva abbastanza alta), e ERA 03 definisce il premio solo per lotterie a media nulla.
:::::

# Domanda B (20 punti)

::::: {.callout kind="tip" heading="B.1 · Richiamo"}
Con prezzo comune $p$ il consumatore di tipo $\pi$ compra se $u(w-p)\ge\pi u(w-L)+(1-\pi)u(w)$, cioè se $\pi\ge h(p)=\dfrac{u(w)-u(w-p)}{u(w)-u(w-L)}$. Per la concavità stretta $h(p)<p/L$. *(ERA 07, «La congettura sul prezzo e la regola di acquisto»)*
:::::

::::: {.callout kind="example" heading="B.1 · Svolgimento"}
Con $u=\ln$: $h(p)=\dfrac{\ln\big(w/(w-p)\big)}{\ln\big(w/(w-L)\big)}$. Qui $w/(w-L)=18/8=(3/2)^2$ e, per $p=6$, $w/(w-p)=18/12=3/2$. Quindi
$$h(6)=\frac{\ln(3/2)}{2\ln(3/2)}=\frac12.$$
Confronto: $p/L=6/10=3/5>1/2$. Comprano i consumatori con $\pi\ge1/2$, quindi anche quelli con $1/2\le\pi<3/5$, per i quali $\pi L<6$: pagano più della propria polizza equa, perché l'avversione al rischio li spinge ad assicurarsi lo stesso. Questi consumatori esistono, perché l'intervallo $[0{,}5;\,0{,}6)$ sta dentro il supporto $[0{,}4;\,0{,}8]$ di $\pi$.
:::::

::::: {.callout kind="success" heading="B.1 · Risposta"}
$h(6)=1/2$. Sì: $p/L=3/5>h(p)$, quindi comprano anche i consumatori con $1/2\le\pi<3/5$ (nel supporto $[0{,}4;\,0{,}8]$), la cui polizza equa costerebbe meno di 6 €.
:::::

::::: {.callout kind="warning" heading="B.1 · Errore tipico"}
$h(p)=p/L$ vale solo per un agente neutrale al rischio. Con $u=\ln$ strettamente concava la soglia sta sotto $p/L$.
:::::

::::: {.callout kind="tip" heading="B.2 · Richiamo"}
Il prezzo $p^{**}=E[\pi]\,L$ azzera il profitto solo se comprano tutti; se comprano solo i consumatori con $\pi\ge h(p)$, la perdita attesa per polizza è $E[\pi\mid\pi\ge h(p)]\,L$. *(ERA 07, «La congettura sul prezzo e la regola di acquisto»)* *(ERA 07, «La selezione avversa»)*
:::::

::::: {.callout kind="example" heading="B.2 · Svolgimento"}
$E[\pi]=(0{,}4+0{,}8)/2=0{,}6$, quindi $p^{**}=0{,}6\cdot10=6$. Per $p=6$ la soglia è $h(6)=1/2$ (calcolata in B.1, perché $p^{**}$ coincide con il prezzo di B.1), compresa fra $0{,}4$ e $0{,}8$: la selezione è attiva. Non comprano i consumatori con $\pi<0{,}5$, un quarto della popolazione; comprano i tre quarti, con $\pi$ uniforme su $[0{,}5;\,0{,}8]$:
$$E[\pi\mid\pi\ge0{,}5]=\frac{0{,}5+0{,}8}2=0{,}65.$$
Profitto atteso per polizza venduta: $6-0{,}65\cdot10=-0{,}5<0$. Il prezzo $p^{**}$ non è di equilibrio.
:::::

::::: {.callout kind="success" heading="B.2 · Risposta"}
$p^{**}=6$ €, probabilità media fra gli acquirenti $0{,}65$ (comprano i $\pi\ge h(6)=1/2$), profitto $6-6{,}5=-0{,}5$ € per polizza. No, $p^{**}$ non è di equilibrio.
:::::

::::: {.callout kind="warning" heading="B.2 · Errore tipico"}
Non basta $E[\pi]L$: il profitto va calcolato sugli acquirenti. A $p^{**}$ escono i meno rischiosi e la perdita attesa per polizza ($6{,}5$) supera il prezzo ($6$): per questo un prezzo di equilibrio è maggiore di $p^{**}$ (selezione avversa).
:::::

::::: {.callout kind="tip" heading="B.3 · Richiamo"}
L'alto rischio sceglie la copertura piena a prezzo equo, $\psi_h^c=(L,\pi_hL)$, con utilità $u_h^c=u(w-\pi_hL)$. Il basso rischio sceglie il contratto sulla retta $p=\pi_lB$ che lascia l'alto rischio indifferente rispetto a $\psi_h^c$. *(ERA 07, «L'equilibrio separante»)* *(ERA 07, «Il contratto per il basso rischio sta sulla curva $u_h^c$»)*
:::::

::::: {.callout kind="example" heading="B.3 · Svolgimento"}
$\psi_h^c=(24;\,\tfrac12\cdot24)=(24;\,12)$: in entrambi gli stati la ricchezza è $27-12=15$ e $u_h^c=\ln15\approx2{,}7081$.

Contratto $\overline\psi_l=(8;\,2)$. Retta di profitto nullo del basso rischio: $p=\pi_lB$, e $\tfrac14\cdot8=2$, quindi ci sta. Alto rischio con $\overline\psi_l$: con perdita la ricchezza è $27-2-24+8=9$, senza perdita $27-2=25$ e
$$\tfrac12\ln9+\tfrac12\ln25=\ln3+\ln5=\ln15=u_h^c.$$
Il prodotto delle due ricchezze è $9\cdot25=225=15^2$ (output dello script). L'alto rischio è indifferente fra $\overline\psi_l$ e $\psi_h^c$; lo script verifica anche che $B=8$ risolve il sistema del teorema, con $B<L$.
:::::

::::: {.callout kind="success" heading="B.3 · Risposta"}
$\psi_h^c=(B,p)=(24;\,12)$ e $u_h^c=\ln15\approx2{,}708$. Per $\overline\psi_l=(8;\,2)$: $p=\pi_lB$ ($2=\tfrac14\cdot8$); l'alto rischio ha ricchezza 9 o 25, con utilità $\tfrac12\ln9+\tfrac12\ln25=\ln15=u_h^c$: è indifferente.
:::::

::::: {.callout kind="warning" heading="B.3 · Errore tipico"}
Il basso rischio non ha la copertura piena: $B=8<L=24$. La copertura piena a prezzo equo del basso rischio verrebbe scelta anche dall'alto rischio, che la preferirebbe a $\psi_h^c$; la copertura ridotta serve a non attirarlo.
:::::

::::: {.callout kind="tip" heading="B.4 · Richiamo"}
Le quattro condizioni caratterizzano i contratti solo se un equilibrio separante esiste, e l'esistenza non è garantita. *(ERA 07, «Esistenza e proprietà dell'equilibrio separante»)*
:::::

::::: {.callout kind="example" heading="B.4 · Svolgimento"}
Con la quota $\alpha$ di bassi rischi la perdita attesa per unità di indennizzo di un contratto che attira entrambi i tipi è $\alpha\pi_l+(1-\alpha)\pi_h$, e la sua retta di profitto nullo è $p=[\alpha\pi_l+(1-\alpha)\pi_h]B$. Se $\alpha$ è alta questa retta sta vicino a quella del basso rischio. Una compagnia può offrire un solo contratto appena sopra la retta del gruppo, preferito da entrambi i tipi ai contratti separanti, e ha profitto positivo: l'offerta separante non resiste alla deviazione.
:::::

::::: {.callout kind="success" heading="B.4 · Risposta"}
Se $\alpha$ è alta, la retta di profitto nullo del gruppo, $p=[\alpha\pi_l+(1-\alpha)\pi_h]B$, sta vicino a quella del basso rischio. Una compagnia può offrire un contratto unico appena sopra, che attira entrambi i tipi con profitto positivo: la deviazione rompe l'equilibrio separante.
:::::

::::: {.callout kind="warning" heading="B.4 · Errore tipico"}
Nell'equilibrio separante il basso rischio non esce dal mercato: compra, con copertura parziale. Il problema è la deviazione con un contratto unico, non l'uscita dei bassi rischi.
:::::

# Domanda C (20 punti)

::::: {.callout kind="tip" heading="C.1 · Richiamo"}
$F_2$ domina $F_1$ al primo ordine se la c.d.f. di $F_2$ sta sotto quella di $F_1$ in ogni punto, e il teorema è «se e solo se»: equivale a dire che ogni $u$ crescente preferisce $F_2$. Una media non inferiore è necessaria ma non basta. *(ERA 04, «Dominanza stocastica del primo ordine»)*
:::::

::::: {.callout kind="example" heading="C.1 · Svolgimento"}
Le c.d.f. in $10,\ 50,\ 90$ € sono $(1/8;\,7/8;\,1)$ per $p$ e $(3/8;\,1/2;\,1)$ per $q$: in 10 € quella di $q$ sta sopra, in 50 € sta sotto. Si incrociano, quindi né $p$ né $q$ domina l'altra al primo ordine. Poiché il teorema è «se e solo se», esiste una $u$ crescente che preferisce $p$ e una che preferisce $q$: la scelta dipende da $u$ e i dati non la determinano.
:::::

::::: {.callout kind="success" heading="C.1 · Risposta"}
No. Le c.d.f. si incrociano: $(1/8;\,7/8;\,1)$ per $p$, $(3/8;\,1/2;\,1)$ per $q$. Nessuna lotteria domina l'altra al primo ordine e il teorema è «se e solo se»: esiste una $u$ crescente che sceglie $p$ e una che sceglie $q$.
:::::

::::: {.callout kind="warning" heading="C.1 · Errore tipico"}
$q$ ha la media maggiore ($55$ contro $50$), ma questo non basta: la dominanza del primo ordine richiede la c.d.f. di $q$ sotto quella di $p$ in ogni punto.
:::::

::::: {.callout kind="tip" heading="C.2 · Richiamo"}
$F_2$ domina $F_1$ al secondo ordine se $\int_a^xF_1\ge\int_a^xF_2$ per ogni $x$, e il teorema è «se e solo se»: equivale a dire che ogni $u$ crescente e concava preferisce $F_2$. La dimostrazione usa le $u_\theta(x)=\min(x,\theta)$, per cui $E[u_\theta]=\theta-\int_a^\theta F$. *(ERA 04, «Dominanza stocastica del secondo ordine»)*
:::::

::::: {.callout kind="example" heading="C.2 · Svolgimento"}
Gli integrali delle c.d.f. a partire da 10 €, in $10,\ 50,\ 90$ €, sono $(0;\,5;\,40)$ per $p$ e $(0;\,15;\,35)$ per $q$.

$q$ domina $p$ se $\int F_p\ge\int F_q$ ovunque: in 50 € vale $5<15$, quindi no. $p$ domina $q$ se $\int F_q\ge\int F_p$ ovunque: in 90 € vale $35<40$, quindi no. L'ultimo valore dell'integrale è $90-E[X]$, e la differenza $40-35=5$ è la differenza fra le medie, $55-50$.

Nessuna domina al secondo ordine, quindi l'ordine dipende da $u$. Con $u(x)=x$, crescente e concava, si preferisce $q$ ($E=55$ contro $50$). Con $u(x)=\min(x,50)$, crescente e concava, si preferisce $p$ ($E=45$ contro $35$): è la $u_\theta$ con $\theta=50$, e infatti $E[u_\theta]=50-\int_{10}^{50}F$ vale $50-5=45$ per $p$ e $50-15=35$ per $q$ (output dello script).
:::::

::::: {.callout kind="success" heading="C.2 · Risposta"}
No. Gli integrali delle c.d.f. in 10, 50, 90 € sono $(0;\,5;\,40)$ per $p$ e $(0;\,15;\,35)$ per $q$: si incrociano, nessuna domina al secondo ordine. Infatti $u(x)=x$ sceglie $q$ ($55>50$), $u(x)=\min(x,50)$ sceglie $p$ ($45>35$).
:::::

::::: {.callout kind="warning" heading="C.2 · Errore tipico"}
Aggiungere la concavità non fa preferire $p$ per forza: a medie diverse la dominanza del secondo ordine deve valere anche all'ultimo punto, dove conta la differenza fra le medie, qui a favore di $q$.
:::::

::::: {.callout kind="tip" heading="C.3 · Richiamo"}
$F_1$ è un *mean-preserving spread* di $F_2$ se $\tilde x_1\overset d=\tilde x_2+\tilde\varepsilon$ con $E[\tilde\varepsilon\mid x_2]=0$ per ogni $x_2$; allora $F_2$ domina $F_1$ al secondo ordine. *(ERA 04, «Il *mean-preserving spread*»)* *(ERA 04, «Il valore atteso condizionato»)*
:::::

::::: {.callout kind="example" heading="C.3 · Svolgimento"}
Le medie sono uguali: $E_{F_2}[\tilde x]=E_{F_1}[\tilde x]=10\%$ (output dello script). Da $-60\%$ e da $60\%$ non si può spostare la massa restando nel supporto con media condizionata nulla, quindi $\tilde\varepsilon=0$. Dal valore centrale $20\%$ si sposta massa verso gli estremi:

| $x_2$ | valori di $\tilde\varepsilon$ | probabilità condizionate |
|---|---|---|
| $-60\%$ | $0$ | $1$ |
| $20\%$ | $-80,\ 0,\ +40$ punti | $1/4,\ 1/4,\ 1/2$ |
| $60\%$ | $0$ | $1$ |

Media condizionata in $x_2=20\%$: $\tfrac14(-80)+\tfrac12(40)=-20+20=0$. Le probabilità di $\tilde x_2+\tilde\varepsilon$ sono
$$P(-60\%)=\tfrac14+\tfrac12\cdot\tfrac14=\tfrac38,\quad P(20\%)=\tfrac12\cdot\tfrac14=\tfrac18,\quad P(60\%)=\tfrac14+\tfrac12\cdot\tfrac12=\tfrac12,$$
cioè $F_1=(3/8;\,1/8;\,4/8)$. Gli integrali delle c.d.f. in $-60\%,\ 20\%,\ 60\%$ sono $(0;\,1/5;\,1/2)$ per $F_2$ e $(0;\,3/10;\,1/2)$ per $F_1$: $\int F_1\ge\int F_2$ ovunque, come richiede la dominanza di $F_2$.
:::::

::::: {.callout kind="success" heading="C.3 · Risposta"}
$\tilde\varepsilon=0$ se $x_2=-60\%$ o $60\%$; se $x_2=20\%$, $\tilde\varepsilon=-80;\,0;\,+40$ punti con probabilità $1/4;\,1/4;\,1/2$ (media $-20+20=0$). Allora $\tilde x_2+\tilde\varepsilon$ ha probabilità $(3/8;\,1/8;\,4/8)=F_1$.
:::::

::::: {.callout kind="warning" heading="C.3 · Errore tipico"}
Il rumore non può essere simmetrico in questo esempio: dal valore centrale gli scarti verso gli estremi sono $-80$ e $+40$, e la media condizionata si annulla solo se le probabilità sono $1/4$ e $1/2$, non uguali.
:::::

::::: {.callout kind="tip" heading="C.4 · Richiamo"}
Se $F_2$ domina $F_1$ al secondo ordine e per ogni ricchezza finale ammissibile valgono $RR<1$, $P>0$ e $RP<2$, allora $g(x)=x\,u'(w_0+\alpha_1^*x)$ è crescente e concava e $\alpha_2^*\ge\alpha_1^*$. Le condizioni sono sufficienti, non necessarie. *(ERA 05, «Quando la funzione è concava»)* *(ERA 05, «Il risultato»)*
:::::

::::: {.callout kind="example" heading="C.4 · Svolgimento"}
$F_2$ domina $F_1$ al secondo ordine (C.3; lo script lo verifica). Con $u(z)=\sqrt z$: $u'(z)=1/(2\sqrt z)$, $A(z)=1/(2z)$, quindi $RR=zA=1/2<1$; $P=-u'''/u''=3/(2z)>0$ e $RP=zP=3/2<2$ per ogni $z>0$ (lo script lo controlla sulle ricchezze finali ammissibili, da $100(1-0{,}6)=40$ a $100(1+0{,}6)=160$ €). Le condizioni del teorema di ERA 05 valgono. Per verifica diretta, con $w_0=W=100$ e $h(y)=y\,u'(100+y)=y/\big(2\sqrt{100+y}\big)$ (la funzione $h$ di ERA 05, non la soglia $h(p)$ di B), si ha $g(x)=h(\alpha_1^*x)/\alpha_1^*$ e
$$h'(y)=\frac{200+y}{4(100+y)^{3/2}}>0,\qquad h''(y)=-\frac{400+y}{8(100+y)^{5/2}}<0,$$
quindi $g$ è crescente e concava. Allora $V_2'(\alpha_1^*)=E_{F_2}[g(\tilde x)]\ge E_{F_1}[g(\tilde x)]=0$, dove l'ultima uguaglianza è la FOC sotto $F_1$. Poiché $V_2$ è concava, $\alpha_2^*\ge\alpha_1^*$.

Numeri (script): $\alpha_1^*=59{,}80$ e $\alpha_2^*=85{,}14$, entrambi interni a $[0,100]$; $V_2'(\alpha_1^*)=0{,}0018>0$.
:::::

::::: {.callout kind="success" heading="C.4 · Risposta"}
Sì. $F_2$ domina $F_1$ al secondo ordine e per $u=\sqrt z$ valgono $RR=1/2<1$, $P>0$, $RP=3/2<2$ (ERA 05): $g(x)=x\,u'(100+\alpha_1^*x)$ è crescente e concava, quindi $V_2'(\alpha_1^*)\ge0$ e $\alpha_2^*\ge\alpha_1^*$.
:::::

::::: {.callout kind="warning" heading="C.4 · Errore tipico"}
La dominanza del secondo ordine ordina le utilità attese. In generale, per altre coppie, la sola SOSD non ordina gli ammontari *(ERA 05, «Rischiosità del titolo e investimento»)*; il teorema chiede condizioni su $u$, che qui si verificano per $u=\sqrt z$.
:::::

# Domanda D (20 punti)

::::: {.callout kind="tip" heading="D.1 · Richiamo"}
Con impegno osservabile la polizza ottima ha copertura piena, $z_l=w-p(e)$ in ogni stato, e il premio è fissato da $u(w-p(e))=d(e)+\bar u$. Il profitto è $\Pi^{FB}(e)=p(e)-\sum_l\pi_l(e)\,l$ e la compagnia sceglie l'$e$ che lo massimizza. *(ERA 08, «La polizza ottima per un impegno fissato»)* *(ERA 08, «La scelta dell'impegno»)*
:::::

::::: {.callout kind="example" heading="D.1 · Svolgimento"}
*Confronto dei premi.* Da $d(1)>d(0)$: $u(w-p(1))=d(1)+\bar u>d(0)+\bar u=u(w-p(0))$. Poiché $u$ è strettamente crescente, $w-p(1)>w-p(0)$, cioè $p(1)<p(0)$.

*Premi.* Con $u^{-1}(v)=-1/v$: $w-p(0)=-1/(0-0{,}5)=2$, quindi $p(0)=3-2=1$; $w-p(1)=-1/(0{,}1-0{,}5)=2{,}5$, quindi $p(1)=3-2{,}5=0{,}5$.

*Profitti.* Perdite attese: $E[l\mid e=0]=0{,}1\cdot1+0{,}4\cdot2=0{,}9$ e $E[l\mid e=1]=0{,}1\cdot1+0{,}1\cdot2=0{,}3$. Dunque $\Pi^{FB}(0)=1-0{,}9=0{,}1$ e $\Pi^{FB}(1)=0{,}5-0{,}3=0{,}2$. Il massimo è unico e $e^*=1$. (Lo script verifica che $\bar u$ non è inferiore all'utilità senza polizza, per entrambi i livelli di impegno.)
:::::

::::: {.callout kind="success" heading="D.1 · Risposta"}
Da $u(w-p(e))=d(e)+\bar u$ e $d(1)>d(0)$: $w-p(1)>w-p(0)$, cioè $p(0)>p(1)$. Dati: $p(0)=1$, $p(1)=0{,}5$. $\Pi^{FB}(0)=0{,}1$, $\Pi^{FB}(1)=0{,}2$, quindi $e^*=1$.
:::::

::::: {.callout kind="warning" heading="D.1 · Errore tipico"}
$p(0)>p(1)$ non basta a scegliere $e=0$: con $e=0$ la compagnia incassa $0{,}5$ in più di premio, ma paga $0{,}6$ in più di perdita attesa ($0{,}9$ contro $0{,}3$). Il segno della differenza dei profitti dipende dai dati.
:::::

::::: {.callout kind="tip" heading="D.2 · Richiamo"}
Con copertura piena la ricchezza finale è la stessa in ogni stato: l'impegno non migliora la sorte del cliente e gli costa $d(e)$. La polizza del benchmark per $e=1$ viola il vincolo IC. *(ERA 08, «La polizza ottima per l'impegno basso»)* *(ERA 08, «Lagrangiana e condizioni del primo ordine»)* *(ERA 08, «Polizza ottima ed efficienza»)*
:::::

::::: {.callout kind="example" heading="D.2 · Svolgimento"}
Con $B_l=l$ e $p(1)=0{,}5$ la ricchezza è $w-p(1)=2{,}5$ in ogni stato e $u(2{,}5)=-0{,}4$. Utilità con $e=0$: $-0{,}4-d(0)=-0{,}4$; con $e=1$: $-0{,}4-d(1)=-0{,}5$. Il cliente sceglie $e=0$, strettamente.

Con $e=0$ la compagnia incassa $p(1)=0{,}5$ e paga la perdita attesa $E[l\mid e=0]=0{,}9$: profitto $0{,}5-0{,}9=-0{,}4$, contro $\Pi^{FB}(1)=0{,}2$. La compagnia non ottiene $\Pi^{FB}(1)$ e perde denaro.
:::::

::::: {.callout kind="success" heading="D.2 · Risposta"}
Sceglie $e=0$: con copertura piena la ricchezza è la stessa in ogni stato, l'impegno non dà vantaggi e costa $d(1)>d(0)$ (utilità $-0{,}4$ contro $-0{,}5$). No: la compagnia incassa $0{,}5$ ma paga la perdita attesa $0{,}9$, quindi ottiene $-0{,}4<\Pi^{FB}(1)=0{,}2$.
:::::

::::: {.callout kind="warning" heading="D.2 · Errore tipico"}
La compagnia non ottiene nemmeno $\Pi^{FB}(0)=0{,}1$: incassa il premio basso, $p(1)$, tipico di chi si impegna, ma sopporta le perdite di chi non si impegna.
:::::

::::: {.callout kind="tip" heading="D.3 · Richiamo"}
Nel benchmark la compagnia osserva l'impegno e può legare il contratto ad esso; con impegno non osservabile il premio non può dipendere dall'azione del cliente. *(ERA 08, «Incentivi nella pratica»)*
:::::

::::: {.callout kind="success" heading="D.3 · Risposta"}
Lo sconto lega il premio a un comportamento che la compagnia osserva (la scatola nera, la frequenza in palestra): rende in parte osservabile l'impegno, e ci si avvicina al benchmark. Solo in parte, perché il comportamento è un indizio dell'impegno, non l'impegno stesso: l'azzardo morale resta sulle azioni non osservate.
:::::

::::: {.callout kind="warning" heading="D.3 · Errore tipico"}
Lo sconto non elimina l'asimmetria informativa: la compagnia vede se la scatola nera è installata, non se si guida con prudenza.
:::::

# Domanda E (20 punti)

::::: {.callout kind="tip" heading="E.1 · Richiamo"}
La ricchezza finale con la quota $\alpha$ è $W=R_fP+\alpha\,(\tilde y-R_fP)$. Il mercato si chiude se la quota ottima è $\alpha=1$. Il segno della domanda si legge in $\alpha=0$, dove la ricchezza $R_fP$ è certa. *(ERA 06, «La domanda dell'agente rappresentativo»)* *(ERA 06, «L'offerta e il prezzo di equilibrio»)*
:::::

::::: {.callout kind="example" heading="E.1 · Svolgimento"}
*Obiettivo e FOC.* $V(\alpha)=E\big[u\big(\alpha\tilde y+(1-\alpha)R_fP\big)\big]$. La ricchezza ha derivata $\tilde y-R_fP$ rispetto ad $\alpha$, quindi
$$V'(\alpha)=E\Big[(\tilde y-R_fP)\,u'\big(\alpha\tilde y+(1-\alpha)R_fP\big)\Big]=0.$$

*Segno della domanda.* In $\alpha=0$ la ricchezza finale è $R_fP$ con certezza, quindi $u'(R_fP)$ esce dall'attesa:
$$V'(0)=u'(R_fP)\,E[\tilde y-R_fP]=u'(R_fP)\,\big(E[\tilde y]-R_fP\big)=u'(R_fP)\,P\,(R-R_f),$$
perché $E[\tilde y]=RP$. Poiché $u'>0$ e $P>0$, $V'(0)$ ha il segno di $R-R_f$.

*Perché la FOC basta.* $V''(\alpha)=E\big[(\tilde y-R_fP)^2\,u''(W)\big]<0$: $u''<0$ e, poiché il titolo è rischioso, $\tilde y\neq R_fP$ con probabilità positiva. $V$ è strettamente concava, quindi $V'$ è decrescente e si annulla al più una volta: la FOC è necessaria e sufficiente, e la quota ottima è positiva se e solo se $V'(0)>0$, cioè $R>R_f$.
:::::

::::: {.callout kind="success" heading="E.1 · Risposta"}
$V(\alpha)=E[u(\alpha\tilde y+(1-\alpha)R_fP)]$, FOC $E[(\tilde y-R_fP)\,u'(\alpha\tilde y+(1-\alpha)R_fP)]=0$. In $\alpha=0$ la ricchezza $R_fP$ è certa: $V'(0)=u'(R_fP)\,E[\tilde y-R_fP]=u'(R_fP)\,P\,(R-R_f)$. $V''=E[(\tilde y-R_fP)^2u'']<0$: $V$ è strettamente concava e la FOC basta.
:::::

::::: {.callout kind="warning" heading="E.1 · Errore tipico"}
$V'(0)$ non è la FOC dell'ottimo: la FOC si impone nella quota ottima, mentre $V'(0)$ serve a leggere il segno della domanda ($V'(0)>0$ se e solo se $R>R_f$). Senza $V''<0$ la FOC darebbe solo un punto stazionario, non un massimo.
:::::

::::: {.callout kind="tip" heading="E.2 · Richiamo"}
Ogni $\alpha_i$ compare linearmente nella ricchezza finale con coefficiente $\tilde y_i-R_fP_i$, e in equilibrio la ricchezza è $\tilde y$. Il kernel $\tilde M$ ha $E[\tilde M]=1$ ed è una funzione di $\tilde y$. *(ERA 06, «Il modello con $n$ titoli»)* *(ERA 06, «Il pricing kernel»)* *(ERA 06, «Il premio al rischio di mercato di ciascun titolo»)*
:::::

::::: {.callout kind="example" heading="E.2 · Svolgimento"}
*(a) Equilibrio e FOC.* La FOC in $\alpha_i$ è $E\big[(\tilde y_i-R_fP_i)\,u'(W)\big]=0$ con $W=\sum_j[\alpha_j\tilde y_j+(1-\alpha_j)R_fP_j]$. In equilibrio $\alpha_j=1$ per ogni $j$, quindi $W=\tilde y$ e $E[\tilde y_i\,u'(\tilde y)]=R_fP_i\,E[u'(\tilde y)]$. Si divide per $P_i\,E[u'(\tilde y)]>0$:
$$E\Big[\frac{\tilde y_i}{P_i}\,\frac{u'(\tilde y)}{E[u'(\tilde y)]}\Big]=R_f,\qquad\text{cioè}\qquad E[\tilde R_i\,\tilde M]=R_f.$$

*(b) Premio e covarianza.* Con $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$ e $E[\tilde M]=1$:
$$R_f=E[\tilde R_i\tilde M]=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i]\,E[\tilde M]=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i],$$
da cui $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$.

*(c) Valore indipendente dal valore del portafoglio di mercato.* $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$ è una funzione di $\tilde y$. Se $\tilde y_i$ è indipendente da $\tilde y$, lo è anche da $\tilde M$, e $\tilde R_i=\tilde y_i/P_i$ con $P_i$ costante: $\mathrm{Cov}(\tilde R_i,\tilde M)=0$. Per (b), $E[\tilde R_i]-R_f=0$: il rischio idiosincratico non è prezzato. Di conseguenza $P_i=E[\tilde y_i]/R_f$.

*Controllo numerico (script).* Con $u=\ln$, $R_f=1$, $\tilde y\in\{4,6\}$ e $\tilde y_i\in\{1,3\}$ indipendenti ed equiprobabili (gli altri titoli rendono $\tilde y-\tilde y_i\ge1$, mai negativo): $P_i=2=E[\tilde y_i]/R_f$ e premio $0$. Se invece $\tilde y_i=\tilde y/2$, il prezzo è $P_i=12/5$ e il premio è $1/24>0$. In questo caso il titolo $i$ e il resto del mercato sono collineari (entrambi $\tilde y/2$): le quote non sono uniche *(ERA 06, «Il modello con $n$ titoli»)*, ma $P_i=E[\tilde y_i\tilde M]/R_f$ resta corretto.
:::::

::::: {.callout kind="success" heading="E.2 · Risposta"}
(a) Con $\alpha_j=1$ la ricchezza è $\tilde y$ e la FOC in $\alpha_i$ dà $E[\tilde y_i\,u'(\tilde y)]=R_fP_i\,E[u'(\tilde y)]$; dividendo per $P_i\,E[u'(\tilde y)]$, $E[\tilde R_i\tilde M]=R_f$. (b) $R_f=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i]\,E[\tilde M]$ con $E[\tilde M]=1$, quindi $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$. (c) $\tilde M$ è funzione di $\tilde y$: se $\tilde y_i$ è indipendente da $\tilde y$, $\mathrm{Cov}(\tilde R_i,\tilde M)=0$ e il premio è nullo.
:::::

::::: {.callout kind="warning" heading="E.2 · Errore tipico"}
Premio nullo non vuol dire titolo privo di rischio: il titolo ha rischio proprio, ma indipendente da $\tilde y$ e perciò non prezzato. Dividere per $P_i\,E[u'(\tilde y)]$ richiede $P_i>0$ e $u'>0$.
:::::
