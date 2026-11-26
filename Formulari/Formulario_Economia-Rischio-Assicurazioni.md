---
title: "Economia del Rischio e delle Assicurazioni — formulario"
subtitle: "Formule, quando usarle e come si dimostrano"
coursecode: "EM2080"
disclaimer: "Formulario personale a fini di studio (Economia del Rischio e delle Assicurazioni EM2080, prof. Valerio Dotti), costruito sulle note verificate del corso. Non è materiale ufficiale del docente."
---

# Come usare il formulario

L'esame è scritto, in presenza e **a libro chiuso**: 1 ora e 30, 100 punti, sufficienza a 55. L'unico testo disponibile (il Mock exam del 13/06/2025) ha cinque domande da 20 punti, con limiti di righe e piccoli «Consigli»:

| Domanda | Che cosa chiede |
|---|---|
| **A** e **B** | calcoli di avversione al rischio con una $u$ data: misure di Arrow-Pratt, equivalente certo, premio per il rischio, prezzo di acquisto e di vendita, e una spiegazione di 3 righe |
| **C** | due distribuzioni su tre valori: quale preferisce un agente con $u$ crescente, e se $u$ è anche concava (dominanza del primo e del secondo ordine, senza calcolare utilità attese) |
| **D** | azzardo morale: scrivere la Lagrangiana, spiegare perché $\beta>0$, che cosa implica la MLR |
| **E** | portafoglio ottimale: scrivere la FOC e fare una dimostrazione guidata sulla statica comparativa |

Nel Mock D è azzardo morale ed E è portafoglio, ma l'elenco delle dimostrazioni del docente ha sei voci anche su prezzo dei titoli e asimmetrie informative: quei capitoli vanno saputi. Non si può consultare nulla, quindi le formule e gli **scheletri delle dimostrazioni** (capitolo «Dimostrazioni da sapere») vanno imparati a memoria. Le risposte devono essere sintetiche: conviene saper dire ogni risultato in due righe (capitolo «Risposte brevi per l'esame»).

Ogni voce ha la stessa forma: **Quando** si usa, **Formula**, **Come si decide**, **Trappola**. Il simbolo † segna una formula o un risultato ricavato qui che le note non scrivono come tale, ma che una domanda può richiedere (per esempio il prezzo di acquisto e di vendita del Mock).

## Simboli che cambiano senso

Le lettere sono riusate da un capitolo all'altro. In una risposta d'esame conviene dichiarare che cosa si sta usando.

| Simbolo | Utilità attesa e avversione | Portafoglio | Prezzo dei titoli | Selezione avversa | Azzardo morale |
|---|---|---|---|---|---|
| $W$ | argomento di $u$ | ricchezza iniziale | ricchezza finale | | |
| $w$ | ricchezza iniziale certa | | | ricchezza iniziale | ricchezza iniziale |
| $R$ | premio per il rischio | | rendimento lordo atteso | | |
| $P$ | prudenza assoluta | | prezzo del titolo | | |
| $p$ | | | | prezzo della polizza | premio della polizza |
| $\alpha$ | peso di miscela | ammontare investito | quota del titolo | quota di basso rischio | |
| $L$ | | | | perdita | perdita massima ($l$ livello) |
| $\lambda$ | parametro CARA | | | | moltiplicatore di PC |

## Convenzioni

- **Rendimenti.** Netti nel capitolo «Portafoglio ottimale» ($\tilde x=\tilde x_0-r$, $w_0=W(1+r)$, $\alpha\in[0,W]$), lordi in «Prezzo dei titoli» ($R_f$, $\tilde R_i=\tilde y_i/P_i$).
- **Premio per il rischio.** Per lotterie a media nulla $R=w-CE$. Per $E[X]\neq0$ si usa † $R=w+E[X]-CE$ (ricchezza attesa meno equivalente certo, come nelle assicurazioni). Il $CE$ è un **livello di ricchezza**, non un guadagno. Dichiarare nella risposta la definizione usata.
- **Stretto e debole.** «Più avverso» e DARA sono in senso debole ($A_2\ge A_1$, $A'\le0$): la CARA è DARA solo in senso debole.

# Dal testo alla formula

| Il testo dà o chiede | Si usa | Capitolo |
|---|---|---|
| una $u$ e «calcola l'avversione assoluta e relativa» | $A=-u''/u'$, $RR=W\,A$ | Avversione al rischio |
| «quanto paga per averla / per evitarla», «equivalente certo», «premio» | $E[u]=u(CE)$, premio | Avversione al rischio |
| «a quanto la venderebbe?» | prezzo di vendita † | Avversione al rischio |
| «i prezzi di acquisto e vendita sono uguali?» | effetto ricchezza: CARA sì, DARA no | Avversione al rischio |
| «quale dei due agenti è più avverso?» | $A_2\ge A_1$, trasformazione concava, $CE_2\le CE_1$ | Avversione al rischio |
| «il premio cresce con la ricchezza?», «DARA?» | $P\ge A$, segno di $A'$ | Avversione al rischio |
| due lotterie, «quale preferisce un agente con $u$ crescente / concava?» | c.d.f.: FOSD, SOSD, mean-preserving spread | Confronto di opzioni rischiose |
| «condividere il rischio lo riduce?» | FOSD (un solo colpito), SOSD (shock indipendenti) | Confronto di opzioni rischiose |
| «scrivi la FOC», «quanto investe?» | $E[\tilde x\,u'(w_0+\alpha\tilde x)]=0$ | Portafoglio ottimale |
| «investe nel titolo rischioso?» | segno di $E[\tilde x]$ | Portafoglio ottimale |
| «più avverso / più ricco / titolo più rischioso / tassa: che cosa cambia?» | statica comparativa | Portafoglio ottimale, Prontuario |
| «prezzo di equilibrio del titolo», «premio al rischio di mercato» | $P=E[\tilde y\tilde M]/R_f$, $\phi=-\mathrm{Cov}(\tilde y,\tilde M)/P$ | Prezzo dei titoli |
| «solo una quota $k$ partecipa», «due paesi», «$n$ titoli» | partecipazione limitata, integrazione, titoli multipli | Prezzo dei titoli |
| «perché il mercato assicurativo non funziona», «prezzo di equilibrio» | $h(p)$ e punto fisso | Selezione avversa e screening |
| «contratti per i due tipi», «single-crossing», «cream skimming» | screening | Selezione avversa e screening |
| «scrivi la Lagrangiana», «impegno non osservabile» | PC e IC, condizione (5) | Azzardo morale |
| «perché $\beta>0$?», «che cosa implica la MLR?» | $B_l-l$ decrescente | Azzardo morale |
| Allais, Ellsberg, triangolo | indipendenza, max-min | Utilità attesa e paradossi |

# Richiami di matematica

**Quando.** Servono in ogni capitolo; il Mock chiede soprattutto derivate di $e^{x}$, $\ln x$, potenze e la Lagrangiana.

$$\begin{gathered}\frac{d\,e^{x}}{dx}=e^{x},\qquad \frac{d\ln x}{dx}=\frac1x, \\ \frac{d\,x^{\alpha}}{dx}=\alpha x^{\alpha-1},\qquad \frac{d\,g(f(x))}{dx}=g'(f(x))\,f'(x)\end{gathered}$$

Per esempio $\dfrac{d}{dx}e^{cx}=c\,e^{cx}$. Integrali e integrazione per parti:

$$\begin{gathered}\int_0^x e^{s}ds=e^{x}-1,\qquad \int_1^x\frac{ds}{s}=\ln x, \\ \int_0^x s^{\alpha}ds=\frac{x^{1+\alpha}}{1+\alpha}\ (\alpha>-1),\qquad \int_a^b F\,G'\,dx=FG\Big|_a^b-\int_a^b G\,F'\,dx\end{gathered}$$

## Probabilità

$$F(x)=\mathbb P(X\le x),\quad f=F'\ \text{(densità)},\quad E[X]=\int x f\,dx=\sum_x x f(x),\quad \mathrm{Var}(X)=E[X^2]-E[X]^2$$

$$\begin{gathered}\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y],\qquad \mathrm{Cov}(aX+b,\,cY+d)=ac\,\mathrm{Cov}(X,Y), \\ \mathrm{Cov}(X,c)=0,\qquad \mathrm{Cov}(X,X)=\mathrm{Var}(X)\end{gathered}$$

Due variabili sono indipendenti se $f(x,y)=f_X(x)f_Y(y)$, e allora $\mathrm{Cov}=0$ (il viceversa è falso). Per $X\sim U[0,1]$: $E[X]=\tfrac12$, $\mathrm{Var}(X)=\tfrac1{12}$. Legge delle aspettative iterate, e un caso utile:

$$\begin{gathered}E[g(X,Y)]=E_X\big[E[g(x,Y)\mid x]\big], \\ E[Y\mid x]=0\ \forall x\ \Longrightarrow\ E[X+Y]=E[X]\end{gathered}$$

**Trappola.** La media condizionata nulla è più debole dell'indipendenza con $E[Y]=0$: il rumore può avere varianza diversa a seconda di $x$.

## Concavità e ottimizzazione

Una funzione due volte derivabile è concava se e solo se $f''\le0$. Se $f''<0$ è strettamente concava (il viceversa è falso: $-x^4$). Per $f$ differenziabile:

1. massimo locale $\Rightarrow\nabla f=0$ (FOC, necessaria);
2. $f$ concava e $\nabla f(x^*)=0$ $\Rightarrow$ $x^*$ massimo globale;
3. $f$ strettamente concava $\Rightarrow$ il massimo, se esiste, è unico; per $n=1$ la derivata è strettamente decrescente, positiva a sinistra di $x^*$ e negativa a destra.

Su un intervallo $[a,b]$, con $V$ strettamente concava: massimo in $a$ se e solo se $V'(a)\le0$; in $b$ se e solo se $V'(b)\ge0$; interno, con $V'=0$, se $V'(a)>0>V'(b)$.

**Kuhn-Tucker.** Per $\max_x f(x)$ sotto $g(x)\ge0$ si scrive $\mathcal L=f+\lambda g$ e all'ottimo valgono

$$\begin{gathered}\nabla f+\lambda\nabla g=0,\qquad g\ge0, \\ \lambda\ge0,\qquad \lambda\,g=0\ \text{(complementarità)}\end{gathered}$$

Se il vincolo è lasco $\lambda=0$; se $\lambda>0$ il vincolo è attivo. Con più vincoli un moltiplicatore ciascuno. Se $f$ e $g$ sono concave le condizioni sono anche sufficienti.

**Trappola.** Il teorema vale solo con una condizione di qualificazione dei vincoli (basta $g$ affine). Con $\max x$ sotto $-x^2\ge0$ la stazionarietà non è soddisfatta anche se $g$ è concava. Senza complementarità la stazionarietà non basta.

> **Esempio.** $\max\ln x_1+\ln x_2$ sotto $W-x_1-x_2\ge0$: le FOC danno $x_1=x_2=1/\lambda$, $\lambda>0$, vincolo attivo, $x_1=x_2=W/2$, $\lambda=2/W$.

# Utilità attesa e paradossi

## Lotterie

**Quando.** Il testo dà premi con probabilità, anche a stadi.

$$\begin{gathered}E[L]=\sum_{s}\pi_s x_s, \\ \alpha L^a+(1-\alpha)L^b:\ \ \pi_s=\alpha\pi^a_s+(1-\alpha)\pi^b_s, \\ E[\alpha L^a+(1-\alpha)L^b]=\alpha E[L^a]+(1-\alpha)E[L^b]\end{gathered}$$

Conta solo la probabilità finale di ogni premio (**riduzione**): una lotteria composta è la lotteria semplice con le stesse probabilità finali. Per esempio giocare con probabilità $\tfrac23$ la lotteria (200, 100 equiprobabili) e prendere 60 con probabilità $\tfrac13$ dà 200, 100 e 60 con probabilità $\tfrac13$ ciascuno e media 120.

## Assiomi e teorema dell'utilità attesa

Le preferenze sono complete e transitive, e soddisfano:

- **continuità (C)**: se $L^1\succeq L^2\succeq L^3$ esiste $\alpha\in[0,1]$ con $L^2\sim\alpha L^1+(1-\alpha)L^3$;
- **indipendenza (IIA)**: $L^1\succeq L^2\iff\alpha L^1+(1-\alpha)L^3\succeq\alpha L^2+(1-\alpha)L^3$ per ogni terza lotteria e ogni $\alpha\in(0,1]$.

$$L^1\succeq L^2\iff U(L^1)\ge U(L^2),\qquad U(L)=\sum_s\pi_s u_s=E[u(L)],\quad u_s=u(x_s)$$

Avere questa forma equivale a $U$ lineare nelle combinazioni: $U(\alpha L^1+(1-\alpha)L^2)=\alpha U(L^1)+(1-\alpha)U(L^2)$. La $u$ di Bernoulli è crescente; concavità e avversione al rischio non si assumono qui.

**Scheletro della dimostrazione.** (1) Esistono una migliore e una peggiore lotteria, $\overline L$ e $\underline L$ (si prendono degeneri, per induzione con l'indipendenza). (2) Per la continuità $L\sim\alpha(L)\,\overline L+(1-\alpha(L))\,\underline L$, con $\alpha(L)$ unico: è l'utilità di $L$. (3) $\alpha$ è lineare e $L^1\succeq L^2\iff\alpha(L^1)\ge\alpha(L^2)$; per linearità $U(L)=\sum_s\pi_su_s$ con $u_s=\alpha(L_s)$.

**Trappola.** Completezza e transitività non bastano (le preferenze lessicografiche non hanno utilità). IIA qui è l'indipendenza, non quella della scelta sociale. Il caso $\alpha=0$ è escluso dall'indipendenza.

## Il triangolo di Machina

Con tre premi $x_1<x_2<x_3$ una lotteria è il punto $(\pi_1,\pi_3)$, con $\pi_2=1-\pi_1-\pi_3$; i vertici sono le lotterie degeneri. La lotteria composta sta sul segmento tra le due componenti.

$$\begin{gathered}U(\pi_1,\pi_3)=u_2+\pi_1(u_1-u_2)+\pi_3(u_3-u_2), \\ \text{rette di indifferenza parallele:}\quad \frac{d\pi_3}{d\pi_1}=\frac{u_2-u_1}{u_3-u_2}>0\end{gathered}$$

L'utilità cresce verso nord-ovest ($\pi_3$ su, $\pi_1$ giù). Due segmenti paralleli con lo stesso orientamento ($L^b-L^a=c\,(M^b-M^a)$, $c>0$) danno la stessa preferenza: $L^a\succeq L^b\iff M^a\succeq M^b$.

## Il paradosso di Allais

| Opzione | Nulla | 1 milione | 5 milioni |
|---|---|---|---|
| 1A | 0% | 100% | 0% |
| 1B | 1% | 89% | 10% |
| 2A | 89% | 11% | 0% |
| 2B | 90% | 0% | 10% |

Molti scelgono 1A e 2B. Con il valore atteso (in milioni 1; 1,39; 0,11; 0,5) si sceglierebbe 1B e 2B. **Perché viola l'indipendenza:** con $A'=[1]$ e $B'$ = (0 con prob. $\tfrac1{11}$, 5 con prob. $\tfrac{10}{11}$),

$$\begin{gathered}1A=0{,}11A'+0{,}89[1],\quad 1B=0{,}11B'+0{,}89[1]\\ 2A=0{,}11A'+0{,}89[0],\quad 2B=0{,}11B'+0{,}89[0]\\ \Longrightarrow\quad 1A\succeq1B\iff A'\succeq B'\iff 2A\succeq2B\end{gathered}$$

Con l'utilità attesa $U(1A)-U(1B)=U(2A)-U(2B)=0{,}11\,u(1)-0{,}01\,u(0)-0{,}10\,u(5)$: nessuna $u$ spiega (1A, 2B). Nel triangolo (premi 0, 1, 5; coordinate $\pi_1,\pi_3$) i segmenti $1A\,1B$ e $2A\,2B$ sono paralleli, con vettore $(0{,}01;\,0{,}10)$ e pendenza 10. Spiegazioni: *framing* e *status quo* (nulla è una perdita nell'esperimento 1).

## Il paradosso di Ellsberg

Urna con 30 palline rosse e 60 nere o gialle in proporzione ignota; ogni opzione paga 100 se si verifica un evento: A rossa, B nera, C rossa o gialla, D nera o gialla. Le scelte tipiche sono $A\succ B$ e $D\succ C$.

$$\begin{gathered}A\succ B\iff\mathbb P(\mathrm N)<\tfrac13,\qquad D\succ C\iff\mathbb P(\mathrm N)>\tfrac13\\ \text{(contraddittorie per ogni probabilità soggettiva)}\end{gathered}$$

**Avversione all'ambiguità, utilità max-min** (Gilboa-Schmeidler): $U_{\min}=\min_{\mathbb P\in\mathcal M}E_{\mathbb P}[u]$, con $\mathcal M=\{\mathbb P:\mathbb P(\mathrm R)=\tfrac13\}$. Con $u(100)=1$, $u(0)=0$:

$$U_{\min}(A)=\tfrac13,\quad U_{\min}(B)=0,\quad U_{\min}(C)=\tfrac13,\quad U_{\min}(D)=\tfrac23$$

che spiega $A\succ B$ e $D\succ C$. **Trappola.** Il minimo si prende sulle **utilità attese** al variare del modello, non sui premi (sui premi A e B varrebbero entrambe $u(0)$).

# Avversione al rischio

## Jensen, concavità e le tre funzioni di riferimento

**Quando.** Ogni domanda A o B parte da una $u$: prima si calcolano $u'$, $u''$, $u'''$.

$$\begin{gathered}f\ \text{concava}\iff E[f(X)]\le f(E[X])\ \ \forall X\quad(\text{Jensen}), \\ \text{avverso al rischio}\iff E[u(w+X)]\le u(w)\ \ \forall w,\ \forall X\ \text{con}\ E[X]=0\iff u\ \text{concava}\end{gathered}$$

Si assume $u'>0$ (crescente) e, per l'avversione, $u''<0$.

| $u(W)$ | $u'$ | $u''$ | $u'''$ | $A$ | $RR$ | $P$ | $RP$ |
|---|---|---|---|---|---|---|---|
| CARA $-e^{-\lambda W}/\lambda$ (o $1-e^{-\lambda W}$) | $e^{-\lambda W}$ | $-\lambda e^{-\lambda W}$ | $\lambda^2e^{-\lambda W}$ | $\lambda$ | $\lambda W$ | $\lambda$ | $\lambda W$ |
| CRRA $W^{1-\gamma}/(1-\gamma)$ | $W^{-\gamma}$ | $-\gamma W^{-\gamma-1}$ | $\gamma(\gamma+1)W^{-\gamma-2}$ | $\gamma/W$ | $\gamma$ | $(1+\gamma)/W$ | $1+\gamma$ |
| $\ln W$ ($\gamma=1$) | $1/W$ | $-1/W^2$ | $2/W^3$ | $1/W$ | $1$ | $2/W$ | $2$ |
| $\sqrt W$ ($\gamma=1/2$, a meno di una costante) | $1/(2\sqrt W)$ | $-1/(4W^{3/2})$ | $3/(8W^{5/2})$ | $1/(2W)$ | $1/2$ | $3/(2W)$ | $3/2$ |
| quadratica $aW-bW^2/2$ † | $a-bW$ | $-b$ | $0$ | $b/(a-bW)$ | $bW/(a-bW)$ | $0$ | $0$ |

Una trasformazione affine crescente di $u$ non cambia $A$, $RR$, $CE$ né le scelte. La CRRA è sempre DARA. La quadratica ha $A$ crescente (IARA) e $P=0<A$.

## Le tre misure di avversione e il loro confronto

$$A(W)=-\frac{u''(W)}{u'(W)}\ \text{(assoluta)},\qquad RR(W)=W\,A(W)\ \text{(relativa)}$$

L'agente 2 è **più avverso** dell'agente 1 se vale una (e allora valgono tutte) delle tre condizioni equivalenti:

1. $u_2=\phi\circ u_1$ con $\phi$ concava (trasformazione concava);
2. $A_2(w)\ge A_1(w)$ per ogni $w$;
3. $CE_2(w,X)\le CE_1(w,X)$ per ogni $w$ e ogni $X$ con $E[X]=0$, cioè $R_2\ge R_1$.

Il legame fra (1) e (2) è

$$\phi''\big(u_1(W)\big)=\frac{u_2'(W)}{\big(u_1'(W)\big)^2}\big[A_1(W)-A_2(W)\big]$$

**Come si decide.** Per due utilità date si calcolano $A_1$ e $A_2$: se $A_2\ge A_1$ ovunque, 2 è più avverso. Se $A_1-A_2$ cambia segno, i due agenti **non sono confrontabili**. Per verificarlo con $\phi$: scrivere $u_2=\phi(u_1)$ e controllare che $\phi$ sia concava (per $\ln W$ e $\ln\ln W$: $\phi=\ln$, concava, quindi $\ln\ln W$ è più avversa).

**Trappola.** Il confronto è debole. Una funzione può essere convessa su un intervallo ($(\ln W)^2$ per $W<e$) e allora $A<0$ lì.

## Equivalente certo e premio per il rischio

**Quando.** «Quanto è disposto a pagare», «a quanto è indifferente».

$$E[u(w+X)]=u(CE),\qquad R=w-CE\ \ (E[X]=0),\qquad \text{in generale } R=w+E[X]-CE\ \dagger$$

Per un agente avverso al rischio $R\ge0$. Per ottenere $CE$ si inverte $u$ sull'utilità attesa $E[u]$ della ricchezza aleatoria $W$:

| $u$ | equivalente certo di una ricchezza aleatoria $W$ |
|---|---|
| CARA $-e^{-\lambda W}/\lambda$ (o $1-e^{-\lambda W}$) | $CE=-\dfrac1\lambda\ln E\big[e^{-\lambda W}\big]$ |
| CRRA $W^{1-\gamma}/(1-\gamma)$ | $CE=\big(E[W^{1-\gamma}]\big)^{1/(1-\gamma)}$ |
| $\ln W$ | $CE=\exp\big(E[\ln W]\big)$ |
| $\sqrt W$ | $CE=\big(E[\sqrt W]\big)^2$ |
| quadratica $aW-bW^2/2$ † | $CE=\dfrac ab-\sqrt{\Big(\dfrac ab-E[W]\Big)^2+\mathrm{Var}(W)}$ |

Con CARA il premio non dipende da $w$: per $X=\pm h$ equiprobabile $R=\dfrac{\ln\cosh(\lambda h)}{\lambda}$. Con $u=\ln$, $w=10$, $X=\pm6$: $\ln8=\ln(10-R)$, $CE=8$, $R=2$.

**Trappola.** $CE$ è un livello di ricchezza: il guadagno certo equivalente è $CE-w$. Per $\sqrt W$ e $\ln W$ si ragiona sulla ricchezza finale $w+X$ (per $w=0$ la ricchezza finale è la lotteria).

> **Esempio dal Mock, domanda A.** $u=1-e^{-W}$ (CARA con $\lambda=1$): $u'=e^{-W}$, $u''=-e^{-W}$, quindi $A=1$ e $RR=W$. Con $w=10$ e $X=0$ o $\ln3$ equiprobabili: $E[e^{-X}]=\tfrac12\big(1+\tfrac13\big)=\tfrac23$.
>
> **Esempio dal Mock, domanda B.** $u=\sqrt W$, $w=0$, $X=0$ con prob. $1-p$ e $4$ con prob. $p$, $CE=1$: $E[u]=2p=\sqrt{CE}=1$, quindi $p=\tfrac12$. $E[X]=2$, premio $=2-1=1$. Con 9 al posto di 4 e lo stesso $p$: $E[u]=\tfrac32$, $CE=\tfrac94$, $E[X]=\tfrac92$, premio $=\tfrac94$. Il premio sale perché la lotteria è più rischiosa (la ricchezza iniziale è la stessa, 0), non per un effetto ricchezza.

## Prezzo di acquisto e prezzo di vendita †

**Quando.** «Se non possiede la lotteria quanto è disposto a pagare?», «se la possiede a quanto la venderebbe?» (Mock A.2 e A.3).

$$\begin{gathered}\text{acquisto } b:\ E[u(w+X-b)]=u(w), \\ \text{vendita } s:\ u(w+s)=E[u(w+X)]\ \Longleftrightarrow\ s=CE-w\end{gathered}$$

**Come si decide.** Con CARA le due definizioni danno lo stesso numero, $b=s=-\frac1\lambda\ln E[e^{-\lambda X}]$, perché la ricchezza iniziale si semplifica. Con DARA, chi compra parte più povero di $b$ ed è più avverso, quindi $b<s$ (per CRRA $\gamma=2$, $X\in\{0,2\}$, $w=3$: $b\approx0{,}697$, $s=0{,}75$). Nel Mock A: $b=s=\ln\tfrac32\approx0{,}405$, premio $\tfrac12\ln3-\ln\tfrac32\approx0{,}144$.

**Trappola.** Il prezzo di vendita è il $CE$ come guadagno ($CE-w$), non il $CE$.

## Approssimazione di Arrow-Pratt

**Quando.** Lotterie piccole; spiega perché $A$ ordina gli agenti.

Per $kX$ con $E[X]=0$ e $R(k)$ definito da $E[u(w+kX)]=u(w-R(k))$: $R(0)=0$, $R'(0)=0$, $R''(0)=A(w)\,E[X^2]$, quindi

$$\begin{gathered}R(k)\approx\tfrac12\,A(w)\,\mathrm{Var}(kX)\quad(k\ \text{piccolo}), \\ R'(k)\ge0\ \text{se } u \text{ concava}\end{gathered}$$

Con $u=\ln$, $w=10$, $X=\pm1$: $R(1)=0{,}0501$ contro $0{,}05$; $R(5)=1{,}3397$ contro $1{,}25$; $R(9{,}9)=8{,}5893$ contro $4{,}9005$. **Trappola.** L'approssimazione è buona solo se la lotteria è piccola rispetto alla ricchezza; raddoppiare $k$ quadruplica il premio solo per $k$ piccolo.

## Effetto ricchezza, prudenza e DARA

**Quando.** «Il premio cresce o decresce con la ricchezza?», «il prezzo di acquisto e quello di vendita sono uguali?».

$$\begin{gathered}\frac{\partial R(w,X)}{\partial w}=1-\frac{E[u'(w+X)]}{u'(w-R)}, \\ P(W)=-\frac{u'''(W)}{u''(W)},\qquad A'(w)=A(w)\big[A(w)-P(w)\big]\end{gathered}$$

Le seguenti condizioni sono **equivalenti** (con $u'>0$, $u''<0$, $u$ tre volte derivabile):

1. DARA: $A'(w)\le0$ per ogni $w$;
2. il premio $R(w,X)$ non cresce con $w$, per ogni $X$ a media nulla;
3. $-u'$ è più avversa al rischio di $u$;
4. $P(w)\ge A(w)$ per ogni $w$.

La prudenza è l'avversione assoluta di $-u'$: $A_{-u'}=P$. CARA: $A'=0$, $P=A=\lambda$, premio costante. CRRA e logaritmo: $A'<0$, $P>A$, premio decrescente (CRRA $\gamma=2$ e $X=\pm1{,}5$: $R=2{,}25/w$).

**Trappola.** La definizione debole ($A'\le0$) include la CARA; con la forma stretta ($A'<0\iff P>A$) la CARA è esclusa.

# Confronto di opzioni rischiose

**Quando.** Il testo dà due lotterie (a tre valori, uniformi, normali) e chiede quale preferisce un agente con $u$ crescente, o crescente e concava. Si lavora sulle **c.d.f.**, senza calcolare utilità attese.

$$\begin{gathered}E_F[u(X)]=u(b)-\int_a^b u'(t)\,F(t)\,dt, \\ E_{F_2}[u]-E_{F_1}[u]=\int_a^b u'(t)\big[F_1(t)-F_2(t)\big]dt, \\ E[X]=b-\int_a^bF(t)\,dt\end{gathered}$$

## Dominanza del primo e del secondo ordine

| Ordine | Condizione su $F_2$ contro $F_1$ | Equivale a $E_{F_2}[u]\ge E_{F_1}[u]$ per |
|---|---|---|
| **FOSD** | $F_2(x)\le F_1(x)$ per ogni $x$ | ogni $u$ crescente |
| **SOSD** | $\displaystyle\int_a^xF_2(\theta)\,d\theta\le\int_a^xF_1(\theta)\,d\theta$ per ogni $x$ | ogni $u$ crescente e concava |

FOSD implica SOSD. Con $u(x)=x$: FOSD e SOSD implicano $E[X_2]\ge E[X_1]$; il viceversa è falso. **A medie uguali la FOSD è esclusa** (a meno che le distribuzioni coincidano): le c.d.f. si incrociano, e resta da verificare la SOSD. Una varianza minore da sola non basta.

**Mean-preserving spread.** $F_1$ è un MPS di $F_2$ se $X_1\overset d=X_2+\tilde\varepsilon$ con $E[\tilde\varepsilon\mid x_2]=0$ per ogni $x_2$. Allora $E[X_1]=E[X_2]$ e $F_2$ domina $F_1$ al secondo ordine (la dimostrazione è barrata nell'elenco del docente, ma è breve: torre più Jensen). A medie uguali vale anche il viceversa (Rothschild-Stiglitz, non dimostrato).

## Procedura per due distribuzioni su tre valori †

Premi $x_1<x_2<x_3$, probabilità $p=(p_1,p_2,p_3)$ e $q=(q_1,q_2,q_3)$. Intervalli $d_1=x_2-x_1$, $d_2=x_3-x_2$.

1. Calcolare le medie: una distribuzione che ne domina un'altra (al primo o al secondo ordine) ha media non minore.
2. Calcolare le c.d.f. in $x_1$ e $x_2$ ($F(x_1)=p_1$, $F(x_2)=p_1+p_2$). **FOSD** di $p$ su $q$ se $F_p(x_1)\le F_q(x_1)$ e $F_p(x_2)\le F_q(x_2)$. A medie uguali non c'è FOSD, salvo che le distribuzioni coincidano.
3. **SOSD** di $p$ su $q$ (anche a medie diverse) se
$$F_q(x_1)\ge F_p(x_1)\qquad\text{e}\qquad d_1F_q(x_1)+d_2F_q(x_2)\ \ge\ d_1F_p(x_1)+d_2F_p(x_2)$$
(due controlli bastano perché gli integrali sono lineari a tratti; a medie uguali il secondo vale con uguaglianza).
4. Risposta: con $u$ solo crescente si conclude solo con la FOSD; con $u$ anche concava basta la SOSD (e allora l'agente preferisce la distribuzione meno rischiosa).

> **Mock, domanda C.1.** $X=\{1,3,5\}$, $p=(\tfrac1{12},\tfrac56,\tfrac1{12})$, $q=(\tfrac16,\tfrac46,\tfrac16)$: stessa media 3. $F_p=(\tfrac1{12},\tfrac{11}{12},1)$, $F_q=(\tfrac16,\tfrac56,1)$ si incrociano. (a) $u$ crescente: **non si può dire** (nessuna FOSD, l'ordine dipende da $u$). (b) $u$ anche concava: $q$ è un MPS di $p$ (più massa sugli estremi), $p$ domina $q$ al secondo ordine, **preferisce $p$**.
>
> **Mock, domanda C.2.** $p'=(\tfrac18,\tfrac48,\tfrac38)$, $q'=(\tfrac28,\tfrac38,\tfrac38)$: $F_{p'}=(\tfrac18,\tfrac58,1)\le F_{q'}=(\tfrac28,\tfrac58,1)$. (a) **Sì**: $p'$ domina $q'$ al primo ordine, la preferisce ogni $u$ crescente. (b) **Non cambia**: la concavità è superflua, perché la FOSD implica la SOSD.

## Condivisione del rischio

Comunità di $N$ agenti, shock di reddito $-B$ con probabilità $p$, perdite divise in parti uguali.

- **Un solo agente colpito.** $X_1=(-B,p;\,0,1-p)$ e $X_2=(-B/2,p;\,0,1-p)$. $F_2\le F_1$ (la differenza sta tutta in $[-B,-B/2)$): $N=2$ domina $N=1$ al **primo** ordine. Per ogni $u$ crescente $E[u(X_2)]-E[u(X_1)]=p\,[u(-B/2)-u(-B)]\ge0$.
- **Shock indipendenti.** La variazione di reddito è $-BK/N$, con $K\sim\mathrm{Bin}(N,p)$: media $-pB$ per ogni $N$, varianza $B^2p(1-p)/N$ decrescente. La media non cambia, quindi niente FOSD: $N+1$ domina $N$ al **secondo** ordine, perché $X_N$ è un MPS di $X_{N+1}$. Per $N=2\to3$ i valori di $X_3$ si spostano solo verso i valori vicini di $X_2$ (con rumore a media condizionata nulla).

## Esempi rapidi

- $X_1\sim U[0,1]$ e $X_2\sim U[-1,1]$: $F_1(x)\le F_2(x)$ ovunque, **$F_1$ domina $F_2$ al primo ordine** (medie $\tfrac12$ e $0$).
- $X_1\sim\mathcal N(0,1)$ e $X_2\sim\mathcal N(0,2)$ (secondo parametro = varianza): $X_2=X_1+\tilde\varepsilon$ con $\tilde\varepsilon\sim\mathcal N(0,1)$ indipendente. **$F_1$ domina $F_2$ al secondo ordine**, non al primo (le c.d.f. si incrociano in 0).

**Trappola.** Con medie diverse la SOSD vale senza MPS (se $X_2=X_1+10$ è già FOSD). La SOSD ordina solo le $u$ concave: una $u$ crescente e convessa può invertire l'ordine ($X_3=1$ contro $X_4=(0,2)$ equiprobabili: con $u=x^2$ vince $X_4$).

# Portafoglio ottimale

**Quando.** Un agente con ricchezza $W$ investe $\alpha$ nel titolo rischioso e $W-\alpha$ in quello privo di rischio. È la domanda E del Mock.

$$\begin{gathered}\text{ricchezza finale}=(W-\alpha)(1+r)+\alpha(1+\tilde x_0)=w_0+\alpha\tilde x, \\ w_0=W(1+r),\quad \tilde x=\tilde x_0-r\ \text{(rendimento in eccesso)}\end{gathered}$$

$$\max_{\alpha\in[0,W]}V(\alpha)=E\big[u(w_0+\alpha\tilde x)\big]$$

## FOC e unicità

$$\begin{gathered}V'(\alpha)=E\big[\tilde x\,u'(w_0+\alpha\tilde x)\big]=0, \\ V''(\alpha)=E\big[\tilde x^2u''(w_0+\alpha\tilde x)\big]<0\end{gathered}$$

Con $u''<0$ e $\mathbb P(\tilde x\ne0)>0$: $V$ strettamente concava, soluzione unica. $\alpha^*=0$ se e solo se $V'(0)\le0$; $\alpha^*=W$ se e solo se $V'(W)\ge0$; altrimenti $0<\alpha^*<W$ risolve $V'=0$. Se $\tilde x>0$ in ogni stato $\alpha^*=W$; se $\tilde x<0$ in ogni stato $\alpha^*=0$.

**Come si risolve.** Scrivere la FOC con la $u'$ data e isolare $\alpha$. **Trappola.** Il segno della FOC cambia tra gli stati: un massimo interno richiede $\tilde x$ di segno diverso. Si derivano $u'$ e le attese **sotto il segno di attesa**; con $\alpha$ misurato in euro, non in quota.

## Quando investire

$$V'(0)=u'(w_0)\,E[\tilde x]\qquad\Longrightarrow\qquad \alpha^*>0\iff E[\tilde x]>0\iff E[\tilde x_0]>r$$

Con $E[\tilde x]=0$ non investe nulla, neppure una piccola somma; con $E[\tilde x]<0$ resta $\alpha^*=0$ per il vincolo (senza vincolo andrebbe corto). **Intuizione.** Per un piccolo $\varepsilon$ il guadagno atteso è proporzionale a $\varepsilon$, il costo del rischio (premio) a $\varepsilon^2$.

> **Esempio.** $u=\ln$, $r=0$, $W=w_0=100$, $\tilde x=-50\%$ o $+100\%$ equiprobabili: $E[\tilde x]=25\%>0$; la FOC $\tfrac12\frac{-0{,}5}{100-0{,}5\alpha}+\tfrac12\frac1{100+\alpha}=0$ dà $\alpha^*=50$. Con $\tilde x=\pm50\%$, $E[\tilde x]=0$ e $\alpha^*=0$.

## Avversione al rischio e investimento

Se $u_2=\phi\circ u_1$ con $\phi$ concava (agente 2 più avverso), stessa $w_0$ e stessa $\tilde x$ con $E[\tilde x]>0$: $\alpha_2^*\le\alpha_1^*$; con $\phi$ strettamente concava e $\alpha_2^*<W$: $\alpha_2^*<\alpha_1^*$. Con $\phi$ affine i due agenti investono lo stesso.

> **Esempio.** Stesso titolo: $u_1=\ln$ investe 50; $u_2=-1/w$ (CRRA $\gamma=2$) ha FOC $(100-0{,}5\alpha)^2=\tfrac12(100+\alpha)^2$ e investe $\alpha_2^*=300\sqrt2-400\approx24{,}26$.

## Ricchezza iniziale e investimento

$$\begin{gathered}\frac{\partial\alpha^*}{\partial w_0}=-\frac{E\big[\tilde x\,\{-u''(w_0+\alpha^*\tilde x)\}\big]}{D}, \\ D=-E\big[\tilde x^2u''(w_0+\alpha^*\tilde x)\big]>0\end{gathered}$$

DARA ($A'\le0$) $\Rightarrow\partial\alpha^*/\partial w_0\ge0$; DARA stretta ($A'<0$) $\Rightarrow>0$; CARA $\Rightarrow$ $\alpha^*$ non dipende da $w_0$ (il fattore $e^{-\lambda w_0}$ si semplifica nella FOC). Con CRRA vale $\alpha^*=\kappa\,w_0$: la **quota** investita è costante e l'ammontare cresce con la ricchezza.

> **Esempio.** $\tilde x=-50\%$ o $+100\%$, $W$ da 100 a 200: con $\ln$ l'investimento passa da 50 a 100; con CRRA $\gamma=2$ da 24,26 a 48,53; con CARA $\lambda=0{,}01$ resta $\alpha^*=\ln2/(1{,}5\lambda)\approx46{,}21$.

## Rischiosità del titolo e investimento

Siano $F_2$ che domina $F_1$ al secondo ordine (il titolo 1 è più rischioso) e $\alpha_1^*\in(0,W)$ ottimo sotto $F_1$. Si vuole $E_{F_1}[g(\tilde x)]=0\Rightarrow E_{F_2}[g(\tilde x)]\ge0$, con $g(x)=x\,u'(w_0+\alpha_1^*x)$. Basta che $g$ sia **crescente e concava**. Con $h(y)=y\,u'(w_0+y)$ e $g(x)=h(\alpha_1^*x)/\alpha_1^*$:

$$\begin{gathered}h'(y)=u'(w_0+y)\big[1-RR(w_0+y)+w_0A(w_0+y)\big], \\ h''(y)=u''(w_0+y)\big[2-RP(w_0+y)+w_0P(w_0+y)\big]\end{gathered}$$

$$\begin{gathered}RR<1\ \Rightarrow\ g\ \text{crescente}, \\ RP<2\ \text{e}\ P>0\ \Rightarrow\ g\ \text{concava (perché }h''\le0)\end{gathered}$$

**Risultato.** Se $RR(w)<1$, $P(w)>0$ e $RP(w)<2$ per ogni ricchezza finale ammissibile, allora $\alpha_2^*\ge\alpha_1^*$: **la domanda non cresce quando il titolo diventa più rischioso** (nel Mock E.2 la crescita di $g$ è data, resta da mostrare la concavità). Con la sola $RR<1$ e la FOSD vale lo stesso. Per le CRRA le tre condizioni equivalgono a $\gamma<1$; il logaritmo ($RR=1$, $RP=2$) non le soddisfa ma $h$ è comunque crescente e concava.

**Trappola.** La dominanza ordina le utilità attese dei portafogli ottimi, non gli ammontari investiti: il portafoglio ottimo con $X_2$ è preferito per ogni agente avverso al rischio, ma l'ammontare dipende da $RR$, $P$, $RP$. Le condizioni sono sufficienti, non necessarie.

> **Quiz.** $\tilde x>0$ sempre; si scopre che il rendimento vale $\tilde x$ con probabilità $q$ e $0$ con probabilità $1-q$. $V_2'(\alpha)=q\,V_1'(\alpha)$ ha lo stesso segno, quindi **l'investimento non cambia** (qui $\alpha^*=W$). Se il rendimento che si annulla fosse il rendimento netto $\tilde x_0$ con $r>0$, il rendimento in eccesso sarebbe $-r$ con probabilità $1-q$ e l'investimento **diminuirebbe**.

## Tassazione dei rendimenti

Imposta di aliquota $\tau$ sui guadagni di capitale, con sussidio delle perdite alla stessa aliquota, sul solo rendimento in eccesso: il problema diventa $\max_\alpha V(\alpha(1-\tau))$, la FOC è risolta da $\alpha(1-\tau)=\alpha^*$.

$$\begin{gathered}\alpha^*_{\text{dopo}}=\frac{\alpha^*}{1-\tau}>\alpha^*, \\ \text{con il vincolo: }\min\Big\{\frac{\alpha^*}{1-\tau},\,W\Big\}\end{gathered}$$

Lo Stato assorbe una quota dei guadagni e delle perdite, quindi a parità di esposizione dopo le imposte l'agente si espone di più. **Trappola.** Vale se la base imponibile è il solo rendimento in eccesso ($w_0$ invariato); se fosse tassato anche l'interesse sul titolo privo di rischio, $w_0$ scenderebbe e con DARA l'effetto ricchezza andrebbe in senso opposto.

# Prezzo dei titoli

**Quando.** Il prezzo del titolo è un risultato di equilibrio; si usano rendimenti **lordi**.

Un periodo; titolo rischioso con prezzo $P$ oggi e valore $\tilde y$ domani (nessun dividendo); titolo privo di rischio con rendimento lordo $R_f$ in offerta netta nulla. L'agente rappresentativo tiene $\alpha$ quote:

$$\begin{gathered}W=\alpha\tilde y+(1-\alpha)R_fP=R_fP+\alpha(\tilde y-R_fP), \\ R=\frac{E[\tilde y]}{P},\qquad \phi=R-R_f\ \text{(premio al rischio di mercato)}\end{gathered}$$

## Domanda e prezzo di equilibrio

$$\begin{gathered}V'(\alpha)=E\big[(\tilde y-R_fP)\,u'(W)\big]=0, \\ V'(0)=u'(R_fP)\,P\,(R-R_f)\ \Rightarrow\ \alpha^*>0\iff R>R_f\end{gathered}$$

Non c'è controparte: il mercato si chiude se $\alpha=1$ (anche il titolo privo di rischio è allora in equilibrio). Con $\alpha=1$ la ricchezza è $\tilde y$ e

$$\begin{gathered}P=\frac{E[\tilde y\,u'(\tilde y)]}{R_f\,E[u'(\tilde y)]} \\ \text{(il secondo membro non dipende da }P)\end{gathered}$$

## Pricing kernel e premio al rischio di mercato

$$\begin{gathered}\tilde M=\frac{u'(\tilde y)}{E[u'(\tilde y)]},\quad E[\tilde M]=1, \\ R_fP=E[\tilde y\,\tilde M],\qquad P=\frac{E[\tilde y]+\mathrm{Cov}(\tilde y,\tilde M)}{R_f}\end{gathered}$$

$$\boxed{\ \phi=-\frac{\mathrm{Cov}(\tilde y,\tilde M)}{P}=-\frac{\mathrm{Cov}\big(\tilde y,u'(\tilde y)\big)}{P\,E[u'(\tilde y)]}\ }$$

Se $u''<0$ e $\tilde y$ non è degenere, $\phi>0$: $\tilde M$ è decrescente in $\tilde y$ (l'utilità marginale è alta dove il titolo rende poco), quindi la covarianza è negativa e il prezzo sta sotto $E[\tilde y]/R_f$. Per un agente **neutrale al rischio** $\tilde M\equiv1$ e $\phi=0$. Il fattore di sconto stocastico dei testi di finanza è $m=\tilde M/R_f$ ($P=E[m\tilde y]$).

> **Esempio.** $u=\ln$, $R_f=1$, $\tilde y\in\{1,2\}$ equiprobabili: $E[u'(\tilde y)]=\tfrac34$, $P=\tfrac43$, $\tilde M=(\tfrac43;\tfrac23)$, $\mathrm{Cov}(\tilde y,\tilde M)=-\tfrac16$, $R=\tfrac98$, $\phi=\tfrac18=\tfrac16\big/\tfrac43$.

## L'equity premium puzzle

Per $\tilde y$ poco disperso attorno a $\mu=E[\tilde y]$ (con $R_f=1$):

$$\phi\approx RR(\mu)\,\frac{\mathrm{Var}(\tilde y)}{\mu^2}\ \overset{\text{CRRA}}{=}\ \gamma\,\frac{\mathrm{Var}(\tilde y)}{E[\tilde y]^2}$$

Dati (USA 1889-1978): rendimento reale medio dell'indice 6,98%, tasso privo di rischio 0,80%, **premio osservato 6,18%**. Calibrazione sul PIL pro capite 1963-92: $\mathrm{Var}/E^2=0{,}056\%$, quindi con $\gamma=2$ il modello dà $\phi\approx0{,}11\%$. Per avere il valore osservato servirebbe $\gamma>40$: con $\gamma=40$ e una scommessa $\pm30\%$ della ricchezza, $CE=0{,}7126\,w$ (si pagherebbe il 29% della ricchezza per evitarla). Spiegazioni: il campione, l'eterogeneità degli agenti, preferenze diverse dall'utilità attesa (avversione alle perdite, ambiguità), politiche pubbliche.

## Partecipazione limitata

Solo una frazione $k\in(0,1]$ può tenere il titolo rischioso. I non partecipanti vendono la quota, la investono a $R_f$ e consumano $R_fP(k)$ con certezza. Chiusura del mercato: $k\alpha=1$, cioè $\alpha=1/k$.

$$\begin{gathered}W_k=R_fP(k)+\frac{\tilde y-R_fP(k)}{k},\quad \mathrm{Var}(W_k)=\frac{\mathrm{Var}(\tilde y)}{k^2}, \\ E\big[(\tilde y-R_fP(k))\,u'(W_k)\big]=0,\qquad \phi(k)=-\frac{\mathrm{Cov}\big(\tilde y,\tilde M(k)\big)}{P(k)}\end{gathered}$$

con $\tilde M(k)=u'(W_k)/E[u'(W_k)]$. Per $k<1$ la ricchezza del partecipante è più rischiosa, quindi $\phi$ è più alto (risultato **numerico**, non dimostrato in generale). Con $\gamma=2$ e dati USA il premio si muove in modo apprezzabile solo se $k$ scende sotto circa il 30%.

> **Esempio** ($\ln$, $R_f=1$, $\tilde y\in\{1,2\}$): $(2-2k)P^2-(6-3k)P+4=0$, $P(k)$ è la radice minore. $k=1$: $P=1{,}3333$, $\phi=0{,}125$; $k=\tfrac12$: $P=1{,}2192$, $\phi=0{,}2303$; $k=\tfrac15$: $P=1{,}0979$, $\phi=0{,}3663$. Per $k\to0$, $\phi\to\tfrac12$.

## Mercato internazionale

Due paesi, $\tilde y^A$ e $\tilde y^B$ i.i.d., prezzi uguali, preferenze uguali. Per simmetria $\alpha^A=\alpha^B=\tfrac12$ (diversificazione perfetta), $W=(\tilde y^A+\tilde y^B)/2$, $\mathrm{Var}(W)=\mathrm{Var}(\tilde y)/2$.

$$\begin{gathered}\tilde M=\frac{u'\big((\tilde y^A+\tilde y^B)/2\big)}{E\big[u'\big((\tilde y^A+\tilde y^B)/2\big)\big]}, \\ \phi=-\frac{\mathrm{Cov}(\tilde y^A,\tilde M)}{P}\end{gathered}$$

La covarianza con il kernel si riduce, quindi **l'integrazione riduce il premio al rischio di mercato**: con utilità quadratica la covarianza esattamente dimezza; con CRRA il calcolo numerico dà circa la metà ($\gamma=2$: 0,11% $\to$ 0,06%; $\gamma=40$: 2,86% $\to$ 1,42%).

> **Esempio** ($\ln$, $R_f=1$, $\tilde y\in\{1,2\}$): $E[1/W]=\tfrac{17}{24}$, $P=\tfrac{24}{17}\approx1{,}4118$ (da $\tfrac43$), $\phi=\tfrac1{16}$ (da $\tfrac18$).

## Titoli multipli

$n$ titoli con quota totale 1; $P=\sum P_i$, $\tilde y=\sum\tilde y_i$. In equilibrio $\alpha_i=1$ per ogni $i$ e il consumo dell'agente è $\tilde y$. Con $\tilde R_i=\tilde y_i/P_i$:

$$\begin{gathered}R_f=E[\tilde R_i\,\tilde M],\qquad E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M), \\ \tilde M=\frac{u'(\tilde y)}{E[u'(\tilde y)]}\end{gathered}$$

Il premio del titolo $i$ è positivo se e solo se il suo rendimento è correlato negativamente con il kernel. Un titolo il cui valore è **indipendente** da $\tilde y$ ha $E[\tilde R_i]=R_f$: il rischio idiosincratico non è prezzato.

**Trappola.** Correlazione positiva con il valore di mercato $\tilde y$ non equivale in generale a premio positivo: conta il segno della covarianza con $\tilde M$ (controesempio con CRRA $\gamma=2$ e valori $(2;0;3)$: covarianza con $\tilde y$ positiva, con $\tilde M$ positiva, premio $-\tfrac1{36}$). Qui $P$ non è la prudenza e $R$ non è il premio per il rischio.

# Selezione avversa e screening

**Quando.** Mercato assicurativo con consumatori che differiscono per la probabilità di incidente $\pi_i$ (informazione nascosta).

Ogni consumatore ha ricchezza $w$, perdita $L$ ($0<L<w$), $u$ strettamente crescente e concava; le compagnie sono neutrali al rischio, senza costi, in concorrenza (profitto nullo), e vendono copertura piena indivisibile. Profitto atteso di una polizza venduta a $i$ al prezzo $p_i$: $p_i-\pi_iL$. Con la polizza la ricchezza certa è $w-p_i$. $\pi$ è sempre una probabilità, $p$ un prezzo.

## Informazione perfetta

$$\begin{gathered}p_i^*=\pi_iL\ \ (\text{prezzo equo}), \\ \pi_iu(w-L)+(1-\pi_i)u(w)<u(w-\pi_iL)\ \ (0<\pi_i<1)\end{gathered}$$

Ogni consumatore con $0<\pi_i<1$ compra **esattamente una** polizza (con $k$ polizze la ricchezza attesa resta $w-\pi_iL$ e Jensen stretta preferisce $k=1$, nessun rischio); con $\pi_i\in\{0,1\}$ è indifferente. L'allocazione è Pareto efficiente. La differenza fra ricchezza attesa $w-\pi L$ e equivalente certo senza assicurazione è il premio per il rischio.

## Un solo prezzo e informazione asimmetrica

Le compagnie non osservano $\pi_i$ (supporto $[\underline\pi,\overline\pi]$, c.d.f. $F$ continua): in equilibrio il prezzo è lo stesso per tutti. Il consumatore di tipo $\pi$ compra se e solo se $u(w-p)\ge\pi u(w-L)+(1-\pi)u(w)$, cioè

$$\begin{gathered}\pi\ge h(p)=\frac{u(w)-u(w-p)}{u(w)-u(w-L)}, \\ h(0)=0,\ h(L)=1,\ h'>0,\ h''\ge0,\ h(p)<\frac pL\ (0<p<L)\end{gathered}$$

Il profitto per polizza venduta è $p-E[\pi\mid\pi\ge h(p)]\,L$. **Prezzo di equilibrio**: punto fisso

$$\begin{gathered}p^*=E\big[\pi\mid\pi\ge h(p^*)\big]\,L, \\ E[\pi\mid\pi\ge t]=\frac{\int_t^{\overline\pi}\pi\,dF(\pi)}{1-F(t)}\end{gathered}$$

- $p^*\ge p^{**}=E[\pi]L$, con disuguaglianza **stretta** se e solo se $h(p^*)>\underline\pi$ (una parte non compra). Se la selezione non è attiva (probabilità poco disperse) compra tutti e $p^*=p^{**}$.
- **Esistenza**: se $\overline\pi<1$ esiste un punto fisso in $[0,\overline\pi L]$ (teorema dei valori intermedi su $g(p)-p$). L'**unicità non è garantita**.
- **Selezione avversa**: comprano i consumatori con $\pi\ge h(p^*)$, i più rischiosi; i migliori escono, il gruppo è in media più rischioso, la perdita attesa per polizza sale con il prezzo.
- Con $\pi\sim U[0,1]$: $E[\pi\mid\pi\ge t]=\tfrac{1+t}2$ e $p^*=L$ è **sempre** un equilibrio (mercato che fallisce: compra solo chi ha $\pi=1$, ed è come non comprare); con $\ln$ e $w=1$, per $L=0{,}8$ ce ne sono due, $p^*\approx0{,}696$ e $0{,}8$.

> **Esempio** ($\ln$, $w=1$, $L=0{,}5$, $\pi\sim U[0{,}05;0{,}5]$): $p^{**}=0{,}1375$ ma $h(0{,}1375)\approx0{,}2134>\underline\pi$, quindi a quel prezzo il profitto sarebbe negativo; $p^*\approx0{,}2100$, compra circa il 36% (chi ha $\pi\ge0{,}3401$), probabilità media di incidente $0{,}4201$.

## Screening: modello e single-crossing

Due tipi: basso rischio $\underline\pi$ (quota $\alpha$) e alto rischio $\overline\pi$, $0<\underline\pi<\overline\pi<1$. Un contratto è $(B,p)$ (indennizzo, premio); sono ammessi $B\neq L$. Le compagnie propongono i contratti, poi i consumatori scelgono fra questi e $(0,0)$.

$$\begin{gathered}EU(B,p;\pi)=\pi\,u(w-p-L+B)+(1-\pi)\,u(w-p), \\ \text{profitto}=p-\pi B,\qquad \text{rette di profitto nullo: }p=\underline\pi B,\ \ p=\overline\pi B\end{gathered}$$

Con $a=u'(w-p-L+B)$ e $b=u'(w-p)$, la pendenza della curva di indifferenza nel piano $(B,p)$ è

$$\begin{gathered}s(B,p;\pi)=\frac{dp}{dB}=\frac{\pi a}{\pi a+(1-\pi)b}, \\ \frac{\partial s}{\partial\pi}=\frac{ab}{[\pi a+(1-\pi)b]^2}>0\end{gathered}$$

**Single-crossing**: nello stesso punto la curva dell'alto rischio è **più ripida**; due curve di tipi diversi si incrociano al più una volta. A $B=L$ si ha $a=b$ e $s=\pi$: la curva è **tangente** alla retta di profitto nullo del tipo. Con $B<L$ si ha $s>\pi$; con $B>L$, $s<\pi$.

## Equilibrio separante

Se esiste un equilibrio separante, i contratti sono univoci:

$$\begin{gathered}\psi_h^c=(L,\ \overline\pi L)\\ \overline\psi_l=(\overline B_l,\overline p_l)\ \ \text{con }\overline B_l<L,\ \text{soluzione di}\\ \overline p_l=\underline\pi\,\overline B_l,\qquad \overline\pi\,u(w-\overline p_l-L+\overline B_l)+(1-\overline\pi)\,u(w-\overline p_l)=u(w-\overline\pi L)\end{gathered}$$

Quattro condizioni (ognuna dal comportamento di una compagnia che cerca di deviare):

1. **ogni contratto sta sulla retta di profitto nullo del proprio tipo** (sopra, l'altra compagnia riduce di poco il premio; sotto, perde chi lo offre);
2. **copertura piena per l'alto rischio**: solo a $B=L$ la curva è tangente alla retta, altrimenti c'è una deviazione profittevole;
3. **il contratto del basso rischio non è imitabile**: sta sulla curva $u_h^c$ o sopra e a sinistra, altrimenti l'alto rischio lo preferirebbe a $\psi_h^c$ (compatibilità degli incentivi);
4. **sta sulla curva $u_h^c$**: a sinistra c'è una regione $\mathcal R$ dove un'altra compagnia attira i soli bassi rischi con profitto positivo (**cream skimming**); a destra l'alto rischio lo preferirebbe. Il tipo ad alto rischio è indifferente fra i due contratti.

**Proprietà.** L'alto rischio ottiene il *first best*; il basso rischio un *second best* (copertura $<L$, ridotta per non attirare l'alto rischio). Profitti nulli; è un miglioramento paretiano rispetto al fallimento del mercato. L'equilibrio può non esistere se $\alpha$ è alto: un contratto unico appena sopra $p=[\alpha\underline\pi+(1-\alpha)\overline\pi]B$ attira entrambi i tipi (con i parametri dell'esempio, per $\alpha>0{,}86$ circa).

> **Esempio** ($\ln$, $w=10$, $L=6$, $\underline\pi=0{,}15$, $\overline\pi=0{,}5$): $\psi_h^c=(6;3)$, $u_h^c=\ln7\approx1{,}9459$; $\overline\psi_l\approx(1{,}161;\,0{,}1741)$. Il basso rischio ottiene $2{,}1833$ contro $2{,}1651$ senza assicurazione e $2{,}2083$ con la copertura piena equa $(6;0{,}9)$.

**Trappola.** Nello screening $\underline\pi$ e $\overline\pi$ sono i due soli valori possibili, non gli estremi del supporto della sezione precedente. Il signalling (è il consumatore a differenziare i contratti) non è nel programma, e nemmeno gli equilibri pooling.

# Azzardo morale

**Quando.** La compagnia (principale) non osserva l'impegno dell'assicurato (agente): azione nascosta.

**Modello.** Perdita $l\in\{0,1,\dots,L\}$ ($l=0$: nessun incidente), impegno $e\in\{0,1\}$ (basso, alto), probabilità $\pi_l(e)>0$ con $\sum_l\pi_l(e)=1$, disutilità $d(1)>d(0)$, utilità additiva $u(z)-d(e)$ con $u$ **strettamente** crescente e concava, ricchezza $w>L$. Una polizza è $(p,B_0,\dots,B_L)$ e la ricchezza finale è

$$\begin{gathered}z_l=w-p-l+B_l,\qquad \text{profitto}=p-\sum_l\pi_l(e)B_l, \\ \text{utilità del cliente}=\sum_l\pi_l(e)\,u(z_l)-d(e)\end{gathered}$$

La compagnia è una sola, neutrale al rischio; $\bar u$ è l'utilità di riserva del cliente (non una curva di indifferenza).

## La proprietà MLR

$$\begin{gathered}r_l=\frac{\pi_l(0)}{\pi_l(1)}\ \text{strettamente crescente in }l\\ \Longrightarrow\quad r_0<1<r_L,\quad \sum_l\pi_l(0)x_l>\sum_l\pi_l(1)x_l\ \text{per }x_l\ \text{crescente}\end{gathered}$$

Lettura: più grande è la perdita osservata, più è probabile che derivi da impegno basso (con la regola di Bayes il rapporto a posteriori è $r_l\cdot\mathbb P(e=0)/\mathbb P(e=1)$). In particolare la perdita attesa è minore con $e=1$ ($x_l=l$). La crescita stretta esclude $r_l$ costante (che sarebbe 1).

## Benchmark: impegno osservabile

La compagnia sceglie anche $e$ (può condizionare l'indennizzo all'impegno):

$$\max_{e,p,B_0,\dots,B_L}\ p-\sum_l\pi_l(e)B_l\quad\text{sotto}\quad \text{(PC)}\ \ \sum_l\pi_l(e)\,u(w-p-l+B_l)-d(e)\ge\bar u$$

Per $e$ fissato, $\mathcal L=p-\sum_l\pi_l(e)B_l+\lambda\big[\sum_l\pi_l(e)u(z_l)-d(e)-\bar u\big]$ e le FOC sono

$$\begin{gathered}\frac{\partial\mathcal L}{\partial p}=1-\lambda\sum_l\pi_l(e)u'(z_l)=0, \\ \frac{\partial\mathcal L}{\partial B_l}=-\pi_l(e)+\lambda\,\pi_l(e)\,u'(z_l)=0\ \ (l=0,\dots,L)\end{gathered}$$

La FOC in $p$ è ridondante (somma di quelle in $B_l$). Risulta $\lambda\,u'(z_l)=1$ per ogni $l$, quindi $\lambda>0$ e $z_l$ costante ($u'$ iniettiva): **copertura piena**, $B_l=l$ con la normalizzazione $B_0=0$ (lecita perché $(p,B_l)\mapsto(p+c,B_l+c)$ lascia invariati $z_l$ e profitto), PC con uguaglianza:

$$\begin{gathered}u\big(w-p(e)\big)=d(e)+\bar u,\qquad p(e)=w-u^{-1}\big(d(e)+\bar u\big), \\ \Pi^{FB}(e)=p(e)-\sum_l\pi_l(e)\,l\end{gathered}$$

Due effetti opposti sulla scelta di $e$: $p(0)>p(1)$ (con $d(1)>d(0)$) ma la perdita attesa è minore con $e=1$. L'allocazione è **Pareto efficiente** (rispetto alle allocazioni fattibili quando l'impegno è osservabile). Se $u$ fosse lineare la copertura piena sarebbe una soluzione fra infinite.

## Impegno non osservabile: PC e IC

La compagnia non osserva $e$, quindi aggiunge il vincolo di compatibilità degli incentivi:

$$\begin{gathered}\text{(PC)}\ \sum_l\pi_l(e)\,u(z_l)-d(e)\ge\bar u, \\ \text{(IC)}\ \sum_l\pi_l(e)\,u(z_l)-d(e)\ge\sum_l\pi_l(e')\,u(z_l)-d(e'),\ \ e'\neq e\end{gathered}$$

**Impegno basso ($e=0$).** La polizza ottima è quella del benchmark (copertura piena): soddisfa IC perché con ricchezza costante IC diventa $d(0)\le d(1)$, vera. Il cliente sceglie volontariamente l'impegno basso.

**Impegno alto ($e=1$).** Moltiplicatore $\lambda$ per PC e $\beta$ per IC (nel problema con $e=1$, la sola deviazione è $e'=0$):

$$\begin{aligned}\mathcal L={}&p-\sum_l\pi_l(1)B_l+\lambda\Big[\sum_l\pi_l(1)u(z_l)-d(1)-\bar u\Big]\\ &+\beta\Big[\sum_l\pi_l(1)u(z_l)-d(1)-\sum_l\pi_l(0)u(z_l)+d(0)\Big]\end{aligned}$$

$$\frac{\partial\mathcal L}{\partial B_l}=-\pi_l(1)+\lambda\,\pi_l(1)\,u'(z_l)+\beta\big[\pi_l(1)-\pi_l(0)\big]u'(z_l)=0$$

Dividendo per $\pi_l(1)\,u'(z_l)>0$ si ottiene la condizione su cui si basa tutta l'analisi:

$$\boxed{\ \frac1{u'(z_l)}=\lambda+\beta\Big[1-\frac{\pi_l(0)}{\pi_l(1)}\Big]=\lambda+\beta\,(1-r_l),\qquad l=0,1,\dots,L\ }\tag{5}$$

**Teorema** (con $e=1$, MLR e $B_0=0$): (a) $\beta>0$ e $\lambda>0$, quindi PC e IC valgono entrambi con uguaglianza; (b) $B_l-l$ è strettamente decrescente in $l$; (c) $B_l<l$ per ogni $l\ge1$: **nessuna perdita positiva è coperta per intero**. La parte della perdita a carico del cliente, $l-B_l$, è nulla per $l=0$ e cresce con $l$ (franchigia crescente).

**Interpretazione.** Se $\beta=0$ la (5) darebbe la stessa ricchezza in ogni stato (copertura piena) e il cliente sceglierebbe l'impegno basso: l'impegno alto richiede $\beta>0$. PC è attivo (altrimenti la compagnia abbassa gli indennizzi in modo uniforme senza toccare IC); IC è attivo (un incentivo più forte del necessario esporrebbe il cliente a più rischio inutile). La polizza premia le perdite che indicano più probabilmente impegno alto e penalizza quelle che indicano impegno basso: la perdita è l'unico canale osservabile attraverso cui il compenso dipende dall'impegno.

## Efficienza

Sia $e^*$ l'impegno che la compagnia sceglie con informazione simmetrica (assunto unico) e $e^{**}$ quello con informazione asimmetrica.

- Se $e^*=0$: $e^{**}=0$, stessa polizza e stesso profitto del *first best*, allocazione Pareto efficiente.
- Se $e^*=1$: l'allocazione **non** è Pareto efficiente rispetto al *first best*. O $e^{**}=0$ (impegno inferiore a quello ottimale), oppure $e^{**}=1$ e il cliente ottiene $\bar u$ come nel *first best* ma il profitto della compagnia è strettamente minore (il cliente è esposto al rischio e va compensato).

**Nella pratica.** Sconti sul premio per chi frequenta la palestra (salute) o installa la scatola nera (auto): il premio dipende da un comportamento osservabile, e ci si avvicina al benchmark solo in parte.

**Trappole.**

1. La Lagrangiana per $e=1$ usa $\pi_l(1)$ e $d(1)$ (non $\pi_l(e)$) e l'obiettivo è $p-\sum_l\pi_l(1)B_l$, non $\sum_l\pi_l(e)\,l$.
2. $B_0=0$ si impone **dopo** le FOC in $B_l$, per la traslazione.
3. «Meno di copertura piena» vale solo se si induce $e=1$.
4. «Pareto efficiente» va sempre riferito a un insieme: le allocazioni fattibili con impegno osservabile.

# Dimostrazioni da sapere

Il docente elenca queste dimostrazioni per l'esame, numerando le sue lezioni a partire dal ripasso: «Lezione 2» è l'avversione al rischio, 3 il confronto di opzioni rischiose, 4 il portafoglio ottimale, 5 il prezzo dei titoli, 6 la selezione avversa e lo screening, 7 l'azzardo morale. Le voci **Jensen e avversione al rischio** e **mean-preserving spread implica SOSD** sono **barrate** nell'elenco (tolte). Ogni scheletro dice che cosa si scrive, in ordine.

## Avversione al rischio

**(b) Trasformazione concava e avversione assoluta, (1)$\Leftrightarrow$(2).**

1. Da $u_2=\phi(u_1)$: $u_2'=\phi'(u_1)\,u_1'$, quindi $\phi'(u_1)=u_2'/u_1'$.
2. Derivando ancora: $u_2''=\phi''(u_1)(u_1')^2+\phi'(u_1)\,u_1''$.
3. Si isola $\phi''$ e si usa $u_i''/u_i'=-A_i$: $\ \phi''(u_1)=\dfrac{u_2'}{(u_1')^2}\,[A_1-A_2]$.
4. Il fattore davanti è positivo: $\phi''\le0\iff A_2\ge A_1$. Il dominio di $\phi$ è l'immagine di $u_1$, che $u_1(W)$ percorre per intero.

**(c) (1)$\Rightarrow$(3): trasformazione concava, premio maggiore.**

$$u_2(w-R_2)=E[u_2(w+X)]=E\big[\phi\big(u_1(w+X)\big)\big]\ \le\ \phi\big(E[u_1(w+X)]\big)=\phi\big(u_1(w-R_1)\big)=u_2(w-R_1)$$

Jensen interviene una sola volta, sulla $\phi$ concava. Poiché $u_2$ è crescente, $w-R_2\le w-R_1$, cioè $R_2\ge R_1$ e $CE_2\le CE_1$.

**(d) (3)$\Rightarrow$(2): dal premio all'avversione assoluta.**

1. Per $kX$ con $E[X]=0$ si definisce $R(k)$ da $E[u(w+kX)]=u(w-R(k))$.
2. Si deriva rispetto a $k$: $E[Xu'(w+kX)]+u'(w-R)R'=0$; in $k=0$ (con $E[X]=0$): $R'(0)=0$ ($R(0)=0$).
3. Si deriva ancora, in $k=0$: $E[X^2]u''(w)+u'(w)R''(0)=0$, quindi $R''(0)=A(w)\,E[X^2]$.
4. Taylor: $R(k)=\tfrac12A(w)E[X^2]k^2+o(k^2)$. Da (3), $R_2(k)\ge R_1(k)$: si divide per $k^2$ e si passa a $k\to0$, ottenendo $A_2(w)\ge A_1(w)$. Il cerchio $(3)\Rightarrow(2)\Rightarrow(1)\Rightarrow(3)$ è chiuso.

**(e) Effetto ricchezza.**

1. Si deriva $E[u(w+X)]=u(w-R)$ rispetto a $w$: $\ E[u'(w+X)]=u'(w-R)\,(1-\partial R/\partial w)$.
2. $\partial R/\partial w\le0\iff E[u'(w+X)]\ge u'(w-R)\iff E[v(w+X)]\le v(w-R)$ con $v=-u'$ (crescente perché $u''<0$). È la condizione (3) del teorema di equivalenza per la coppia $u$, $-u'$: **$-u'$ è più avversa di $u$**.
3. Per l'equivalenza (1)$\Leftrightarrow$(2): $A_{-u'}\ge A_u$. Ma $A_{-u'}=-v''/v'=-u'''/u''=P$, quindi $P\ge A$.
4. Da $A'=-u'''/u'+A^2=A(A-P)$ e $A>0$: $P\ge A\iff A'\le0$ (DARA).

## Portafoglio ottimale

**(a) Quando investire.** $V'(0)=u'(w_0)E[\tilde x]$ perché $w_0$ è certo. Se $E[\tilde x]>0$, $V'(0)>0$ e il massimo è in $\alpha^*>0$. Se $E[\tilde x]\le0$, $V'(0)\le0$ e $V'$ è non crescente ($V''<0$), quindi $V'\le0$ su $[0,W]$ e $\alpha^*=0$.

**(b) Avversione al rischio.** Sia $u_2=\phi\circ u_1$, $\phi$ strettamente concava, $\alpha_2^*\in(0,W)$.

1. Basta $V_1'(\alpha_2^*)>0$: $V_1$ è concava, cresce a destra di $\alpha_2^*$, quindi $\alpha_1^*>\alpha_2^*$.
2. FOC del secondo agente: $0=E\big[\tilde x\,\phi'\big(u_1(w_0+\alpha_2^*\tilde x)\big)\,u_1'(w_0+\alpha_2^*\tilde x)\big]$.
3. $\phi'$ è decrescente: se $x>0$, $w_0+\alpha_2^*x>w_0$ e $\phi'(u_1(w_0+\alpha_2^*x))<\phi'(u_1(w_0))$; se $x<0$ vale il verso opposto. In ogni caso $x\,\phi'(u_1(w_0+\alpha_2^*x))<x\,\phi'(u_1(w_0))$ per $x\neq0$.
4. Si moltiplica per $u_1'>0$ e si prende l'attesa: $0<\phi'(u_1(w_0))\,V_1'(\alpha_2^*)$. Se $\phi$ è solo concava la disuguaglianza è larga e si ottiene $\alpha_2^*\le\alpha_1^*$.

**(c) Ricchezza.**

1. La FOC all'ottimo vale per ogni $w_0$: $E[\tilde xu'(w_0+\alpha^*(w_0)\tilde x)]=0$; $\alpha^*$ è derivabile (teorema della funzione implicita, $V''<0$).
2. Si deriva rispetto a $w_0$: $E[\tilde xu'']+E[\tilde x^2u'']\,\partial\alpha^*/\partial w_0=0$, da cui $\partial\alpha^*/\partial w_0=-E[\tilde x\{-u''\}]/D$ con $D>0$.
3. Con $-u''=A\,u'$: $x>0\Rightarrow w_0+\alpha^*x>w_0\Rightarrow A(w_0+\alpha^*x)\le A(w_0)$ (DARA); $x<0$ al contrario. Quindi $A(w_0+\alpha^*x)\,x\,u'\le A(w_0)\,x\,u'$ per ogni $x$.
4. Attesa: $E[A(\cdot)\tilde xu']\le A(w_0)E[\tilde xu']=0$ (FOC). L'attesa di $\tilde x\{-u''\}$ è non positiva, quindi $\partial\alpha^*/\partial w_0\ge0$. Con CARA $A$ è costante e vale l'uguaglianza.

**(d) Rischio.** Si vuole $E_{F_1}[g(\tilde x)]=0\Rightarrow E_{F_2}[g(\tilde x)]\ge0$ con $g(x)=x\,u'(w_0+\alpha_1^*x)$.

1. Se $g$ è crescente e concava, per la SOSD $E_{F_2}[g]\ge E_{F_1}[g]=0$, cioè $V_2'(\alpha_1^*)\ge0$.
2. Concavità: $g''(x)=\alpha_1^*h''(\alpha_1^*x)$ con $h''(y)=2u''+y\,u'''$ (calcolati in $w_0+y$). Con $y=(w_0+y)-w_0$ e $u'''=-P\,u''$: $\ h''=u''\,[2-RP+w_0P]$.
3. Poiché $u''<0$, $h''\le0$ se $2-RP+w_0P\ge0$, vera se $RP<2$ e $P>0$ ($w_0>0$). Crescita: $h'=u'[1-RR+w_0A]>0$ se $RR<1$.
4. $V_2$ è concava e $V_2'(\alpha_1^*)\ge0$: il massimo non sta a sinistra di $\alpha_1^*$, quindi $\alpha_2^*\ge\alpha_1^*$.

## Prezzo dei titoli

**(a) Premio al rischio di mercato.**

1. Con $\alpha=1$ la FOC è $E[(\tilde y-R_fP)\,u'(\tilde y)]=0$; dividendo per $E[u'(\tilde y)]>0$: $R_fP=E[\tilde y\tilde M]$, con $E[\tilde M]=1$.
2. $\phi=\dfrac{E[\tilde y]}{P}-R_f=\dfrac{E[\tilde y]E[\tilde M]-E[\tilde y\tilde M]}{P}=-\dfrac{\mathrm{Cov}(\tilde y,\tilde M)}{P}$.
3. Segno: sia $\tilde y'$ una copia indipendente di $\tilde y$ e $g=u'$ decrescente. $E[(\tilde y-\tilde y')(g(\tilde y)-g(\tilde y'))]=2\,\mathrm{Cov}(\tilde y,g(\tilde y))$, e il prodotto dei fattori non è mai positivo (e lo è negativo con probabilità positiva se $\tilde y$ non è degenere). Quindi $\mathrm{Cov}<0$ e $\phi>0$.

**(b) Agenti eterogenei.**

1. Solo la frazione $k$ partecipa; i non partecipanti vendono la quota e consumano $R_fP(k)$. Chiusura del mercato: $k\alpha=1$, $\alpha=1/k$.
2. Ricchezza del partecipante $W_k=R_fP(k)+(\tilde y-R_fP(k))/k$; FOC in $\alpha=1/k$: $E[(\tilde y-R_fP(k))\,u'(W_k)]=0$.
3. Si divide per $E[u'(W_k)]$: $R_fP(k)=E[\tilde y\tilde M(k)]$ e, con la stessa algebra del punto (a), $\phi(k)=-\mathrm{Cov}(\tilde y,\tilde M(k))/P(k)$.
4. $\mathrm{Var}(W_k)=\mathrm{Var}(\tilde y)/k^2$: il kernel è più variabile e $\phi$ cresce al diminuire di $k$ (verifica numerica).

**(c) Titoli multipli.**

1. Con $n$ titoli e offerta 1 per ciascuno l'equilibrio è $\alpha_i=1$; la ricchezza è $\tilde y=\sum_i\tilde y_i$.
2. FOC del titolo $i$: $E[(\tilde y_i-R_fP_i)\,u'(\tilde y)]=0$; si divide per $P_iE[u'(\tilde y)]>0$: $E[\tilde R_i\tilde M]=R_f$.
3. Dalla seconda forma della covarianza e $E[\tilde M]=1$: $R_f=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i]$, quindi $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$.

## Selezione avversa e screening

**(a) Ogni consumatore acquista l'assicurazione (a prezzo equo).**

1. Senza assicurazione l'utilità attesa è $\pi u(w-L)+(1-\pi)u(w)$.
2. $u$ strettamente concava e perdita non degenere ($0<\pi<1$): Jensen stretta dà $<u(\pi(w-L)+(1-\pi)w)=u(w-\pi L)=u(w-p^*)$, l'utilità della polizza a $p^*=\pi L$.
3. Con $k$ polizze la ricchezza attesa resta $w-\pi L$: Jensen stretta preferisce la ricchezza certa, $k=1$.

**(b) Prezzo di equilibrio.**

1. Offerta: infinita se $p>\pi L$, nulla se $p<\pi L$; a prezzo equo la domanda è almeno 1: l'unico prezzo che pareggia è $p^*=\pi L$ (informazione perfetta).
2. Con informazione asimmetrica il prezzo è comune. Il consumatore $\pi$ compra se $u(w-p)\ge u(w)-\pi[u(w)-u(w-L)]$, cioè $\pi\ge h(p)$.
3. Profitto nullo sugli **acquirenti effettivi**: $p^*=E[\pi\mid\pi\ge h(p^*)]L$. Poiché $E[\pi]<E[\pi\mid\pi\ge t]$ se una parte non compra, $p^*\ge E[\pi]L=p^{**}$.

**(c) Single-crossing.**

1. Con $a=u'(w-p-L+B)>0$, $b=u'(w-p)>0$: $EU_B=\pi a$ e $EU_p=-\pi a-(1-\pi)b$.
2. Lungo la curva di indifferenza $EU_B\,dB+EU_p\,dp=0$, quindi $s=dp/dB=\pi a/[\pi a+(1-\pi)b]$.
3. A $(B,p)$ fissato, $\partial s/\partial\pi=ab/[\pi a+(1-\pi)b]^2>0$: l'alto rischio è più ripido.
4. Due incroci sono impossibili: $d=p_h-p_l$ ha $d'>0$ in ogni punto di incrocio, quindi non può tornare a zero scendendo.

## Azzardo morale

**(a) Prezzo ottimale per $e=0$ (copertura piena).**

1. Si risolve il problema con $e=0$ **senza** IC: FOC in $B_l$, $\lambda\,u'(z_l)=1$ per ogni $l$, quindi $\lambda>0$ e $z_l$ costante: $B_l-l$ costante, $B_l=l$ con $B_0=0$.
2. PC attivo (complementarità): $u(w-p)=d(0)+\bar u$.
3. Verifica di IC: con ricchezza costante diventa $u(w-p)-d(0)\ge u(w-p)-d(1)$, cioè $d(0)\le d(1)$, vera. La soluzione del problema senza IC è ammissibile con IC, quindi è ottima anche con IC (un vincolo in più non può far salire il massimo).

**(b) Prezzo ottimale per $e=1$.**

1. Si scrive $\mathcal L$ con PC ($\lambda$) e IC ($\beta$) e si deriva in $B_l$; dividendo per $\pi_l(1)u'(z_l)$: $\ 1/u'(z_l)=\lambda+\beta(1-r_l)$.
2. **$\beta>0$.** Se $\beta=0$, $u'(z_l)=1/\lambda$ costante, $z_l$ costante e IC diventa $\sum_l[\pi_l(1)-\pi_l(0)]u(z)-(d(1)-d(0))=-(d(1)-d(0))<0$: violato. (Se $\beta<0$, $r_l$ crescente renderebbe $z_l$ crescente e la MLR darebbe IC violato.)
3. **$\lambda>0$.** Se $\lambda=0$ il secondo membro $\beta(1-r_l)$ cambia segno con $l$ (positivo per $l=0$, negativo per $l=L$ perché $r_0<1<r_L$), ma il primo membro è positivo: contraddizione.
4. $\lambda,\beta>0$ implicano PC e IC con uguaglianza (complementarità).
5. $r_l$ strettamente crescente $\Rightarrow$ $\lambda+\beta(1-r_l)$ strettamente decrescente $\Rightarrow$ $1/u'(z_l)$ decrescente $\Rightarrow$ $u'(z_l)$ crescente $\Rightarrow$ $z_l$ decrescente. Poiché $z_l-(w-p)=B_l-l$: $B_l-l$ strettamente decrescente, e con $B_0=0$, $B_l<l$ per $l\ge1$.

# Prontuario

## Statica comparativa del portafoglio

| Che cosa cambia | Effetto su $\alpha^*$ | Condizione | Dove |
|---|---|---|---|
| $E[\tilde x]>0$ | $\alpha^*>0$ | $u''<0$, $E[\tilde x]>0$ | Portafoglio ottimale |
| agente più avverso ($u_2=\phi\circ u_1$, $\phi$ concava) | $\alpha_2^*\le\alpha_1^*$ ($<$ se $\phi$ strettamente concava e $\alpha_2^*<W$) | stesso $\tilde x$ e $w_0$ | Portafoglio ottimale |
| più ricchezza iniziale | cresce con DARA ($A'<0$); costante con CARA | $E[\tilde x]>0$, $\alpha^*$ interno | Portafoglio ottimale |
| CRRA | $\alpha^*=\kappa w_0$ (quota costante) | | Portafoglio ottimale |
| titolo meno rischioso ($F_2$ SOSD $F_1$) | $\alpha_2^*\ge\alpha_1^*$ | $RR<1$, $P>0$, $RP<2$ | Portafoglio ottimale |
| tassa su guadagni con sussidio delle perdite | $\alpha^*/(1-\tau)$ | base imponibile: solo il rendimento in eccesso | Portafoglio ottimale |
| $\tilde x$ sostituito da $\tilde x$ con prob. $q$ e 0 con prob. $1-q$ | invariato | $V_2'=qV_1'$ | Portafoglio ottimale |

## Prezzi e premi

| Grandezza | Formula | Quando |
|---|---|---|
| prezzo del titolo | $P=\dfrac{E[\tilde y\,u'(\tilde y)]}{R_f\,E[u'(\tilde y)]}$ | agente rappresentativo, $\alpha=1$ |
| premio al rischio di mercato | $\phi=-\dfrac{\mathrm{Cov}(\tilde y,\tilde M)}{P}$ | $u'>0$ ($>0$ se $u''<0$) |
| partecipazione limitata | $\alpha=1/k$, $W_k=R_fP(k)+(\tilde y-R_fP(k))/k$ | $\phi$ cresce al diminuire di $k$ |
| titolo $i$ fra $n$ | $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$ | rischio idiosincratico non prezzato |
| polizza a prezzo equo | $p^*=\pi L$ | informazione perfetta |
| polizza con selezione avversa | $p^*=E[\pi\mid\pi\ge h(p^*)]L\ge E[\pi]L$ | un solo prezzo |
| contratto dell'alto rischio (screening) | $(L,\overline\pi L)$ | equilibrio separante |
| polizza per l'impegno basso | $B_l=l$, $u(w-p)=d(0)+\bar u$ | azzardo morale, $e=0$ |
| polizza per l'impegno alto | $1/u'(z_l)=\lambda+\beta(1-r_l)$, $B_l<l$ | azzardo morale, $e=1$ |

# Risposte brevi per l'esame

Il Mock chiede risposte di 2 o 3 righe. Queste sono le formulazioni da avere pronte.

| Domanda | Risposta |
|---|---|
| I prezzi di acquisto e vendita sono uguali? | Con CARA sì: l'avversione assoluta è costante, non c'è effetto ricchezza e la ricchezza di partenza non conta. Con DARA l'agente che compra è più povero di quanto paga ed è più avverso: $b<s$. |
| Perché il premio per il rischio cambia fra due lotterie (stessa ricchezza)? | Cambia la dimensione e il rischio della lotteria, non la ricchezza: per rischi piccoli il premio è $\approx\tfrac12A\,\mathrm{Var}$, cresce con la varianza. |
| Due lotterie con la stessa media, $u$ solo crescente: si può dire quale è preferita? E se $u$ è anche concava? | No: a medie uguali non c'è dominanza del primo ordine (le c.d.f. si incrociano) e l'ordine dipende da $u$. Con $u$ anche concava sì, se una domina al secondo ordine (l'altra è un mean-preserving spread): si preferisce la meno rischiosa. |
| Una lotteria domina l'altra al primo ordine: la concavità cambia la risposta? | No: la FOSD implica la SOSD, ogni $u$ crescente (anche concava) preferisce la dominante. |
| Perché $\beta=0$ è impossibile se si vuole $e=1$? PC e IC sono attivi? | Con $\beta=0$ la (5) dà $1/u'=\lambda$, ricchezza uguale in ogni stato, cioè copertura piena. L'impegno costa $d(1)>d(0)$ e non porta alcun vantaggio, quindi il cliente sceglie $e=0$: IC è violato. Dunque $\beta>0$, e con $\lambda>0$ PC e IC valgono entrambi con uguaglianza: il cliente ha esattamente $\bar u$ ed è indifferente fra i due impegni. |
| Che cosa implica la MLR su $B_l-l$ al crescere di $l$? | Il rapporto $r_l$ cresce, quindi $1/u'(z_l)$ scende, $z_l$ scende e $B_l-l$ è decrescente: copertura parziale, con parte a carico del cliente crescente con la perdita. |
| L'allocazione con impegno non osservabile è efficiente? | Solo se la compagnia sceglie $e=0$. Se induce $e=1$ non è Pareto efficiente rispetto al first best (impegno osservabile): il cliente ha $\bar u$ e la compagnia meno profitto. |
| Perché investe nel titolo rischioso se è avverso? | Con $E[\tilde x]>0$ il guadagno atteso è di ordine $\varepsilon$ e il costo del rischio di ordine $\varepsilon^2$: conviene investire una piccola somma. |
| Perché la tassa con sussidio delle perdite fa investire di più? | Rende il rendimento in eccesso $(1-\tau)\tilde x$: a parità di esposizione dopo le imposte si può investire $\alpha^*/(1-\tau)$. |
| Perché il premio al rischio di mercato è positivo? | $\tilde M$ decresce in $\tilde y$: il titolo rende poco quando l'utilità marginale è alta, quindi $\mathrm{Cov}(\tilde y,\tilde M)<0$ e $\phi>0$. |
| Perché l'integrazione internazionale riduce il premio? | La diversificazione dimezza la varianza del consumo ($\mathrm{Var}(\tilde y)/2$), il kernel è meno correlato con il titolo domestico. |
| Perché il mercato assicurativo con informazione asimmetrica può scomparire? | A prezzo più alto escono i bassi rischi, il gruppo che compra è più rischioso, la perdita attesa e il prezzo di equilibrio salgono; nel caso estremo $p^*=L$ non si conclude alcuno scambio. |
| Perché nello screening il basso rischio ha copertura parziale? | Per rendere il suo contratto poco attraente per l'alto rischio, che altrimenti lo imiterebbe (compatibilità degli incentivi). Il suo contratto sta sulla curva di indifferenza dell'alto rischio. |

# Dove le slide scrivono altro

Gli errori delle slide corretti nelle note e le scelte di convenzione. Quando una domanda tocca uno di questi punti, esporre la formulazione corretta.

| Lezione | Che cosa dice la slide | Che cosa vale (come scritto nelle note) |
|---|---|---|
| Utilità attesa | una relazione «completa e transitiva» ammette una rappresentazione; $\alpha,\delta\in(0,1)$ | serve anche la continuità; $\alpha,\delta\in[0,1]$ |
| Confronto di opzioni rischiose, slide 12 | «verifica che $X_1$ SOSD $X_2$» | $X_2$ SOSD $X_1$ (la meno rischiosa domina) |
| Portafoglio ottimale, slide 19 | derivata seconda di $x\,u'(w_0+x)$ con segno sbagliato ($-u''[2-RP+w_0P]$) | $u''[2-RP+w_0P]$, concavità $\le0$; la condizione finale $RP<2$ e $P>0$ non cambia |
| Prezzo dei titoli, slide 11 | «premio del 7%» | il premio è di 6,18 punti; il 7% è il rendimento reale medio del mercato azionario |
| Prezzo dei titoli, slide 20 | $\tilde R_i=\tilde y_i/P$ | $\tilde R_i=\tilde y_i/P_i$ |
| Azzardo morale | segno di $d(e)$ nel vincolo di partecipazione; obiettivo $\sum_l\pi_l(e)\,l$; $\pi_l(e)$ e $d(e)$ nella Lagrangiana per $e=1$; $u$ «concava»; «meno della copertura piena» in generale; $B_0=0$ giustificato con $\beta,\lambda>0$ | PC con $-d(e)$; obiettivo $p-\sum_l\pi_l(e)B_l$; $\pi_l(1)$ e $d(1)$; $u$ strettamente concava; copertura parziale solo con $e=1$; $B_0=0$ per invarianza alla traslazione $(p,B_l)\mapsto(p+c,B_l+c)$ |

Altri errori trovati nelle fonti: la soluzione ufficiale del Problem Set 4, esercizio 1(c), scrive $\alpha^n=1$ ma dalla condizione di chiusura $\tfrac12\alpha^n+\tfrac12\alpha^r=1$ con $\alpha^r=0$ viene $\alpha^n=2$; nel libro di Gollier (4.4), pp. 66-67 della copia del corso, il segno della condizione integrale è rovesciato; Jehle e Reny, p. 417, stampano $d(0)\ge d(1)$.

## Scelte aperte

- **Quiz «rendimento che si annulla» (Portafoglio ottimale).** La risposta è che l'investimento non cambia, se il rendimento che si annulla è quello in eccesso; se è quello netto con $r>0$, diminuisce. Le due letture sono riportate nel capitolo.
- **Premio con media non nulla.** Le note definiscono $R=w-CE$ solo per lotterie a media nulla. Per i Mock A e B si usa $R=w+E[X]-CE$ (†): dichiararlo.
- **DARA debole o stretta.** Nelle note «decrescente» è debole ($A'\le0$) e include la CARA; dove serve la stretta (investimento che cresce con la ricchezza) è indicato.
- **Prezzi di acquisto e vendita, procedura per tre valori, caso quadratico.** Non sono nelle slide né nelle note: sono ricavati qui (†), con i numeri controllati in Python.
- **Dimostrazioni barrate.** Jensen e mean-preserving spread implica SOSD sono barrate nell'elenco del docente; sono riportate nei capitoli come risultati ma non fra le dimostrazioni da saper fare.

## Non coperto

Non sono nelle note, quindi nemmeno qui: gli esercizi dei Problem Set 1, 3 e 4, l'esempio 8.15 di Jehle e Reny, l'unicità dell'utilità a meno di trasformazione affine, il teorema di Savage, altri modelli di ambiguità, il signalling e gli equilibri pooling, HARA, il criterio dell'Hessiana. Il **compito a casa** (+2/30 al primo appello, +1/30 al secondo) non è trattato.
