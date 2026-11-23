---
title: "Economia del Rischio — appello simulato 05"
subtitle: "Traccia simulata, con la struttura dell'appello del 13 giugno 2025"
stats: "5 domande · 100 punti · 90 minuti"
disclaimer: "Appello simulato costruito a fini di studio sul modello dei veri appelli e sui contenuti del corso (EM2080, prof. Valerio Dotti). Non è una traccia ufficiale del docente."
---

# Istruzioni (leggere attentamente)

Nome e cognome: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Matricola: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Scrivi le risposte sul foglio protocollo con una penna blu o nera. L'esame si svolge in presenza e a libro chiuso e dura 1 ora e 30 minuti (90 minuti). Riceverai un avviso a 10 minuti e a 1 minuto dalla fine; quando verrà annunciata la fine, posa la penna SUBITO. Scrivi nome, cognome e matricola nello spazio qui sopra e in testa a OGNI foglio protocollo che usi: un elaborato privo di questi dati NON verrà valutato. Rispondi in modo SINTETICO e non superare MAI il numero di righe indicato, pena una penalizzazione nel punteggio. Ogni domanda riporta il punteggio massimo a fianco del titolo (per esempio 3 punti). Il punteggio massimo dell'esame è 100. Buona fortuna!

# Domanda A (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Si considerano due agenti: l'agente 1 ha utilità Bernoulliana $u_1(W)=\ln W$, definita per $W>0$, e l'agente 2 ha $u_2(W)=-e^{-\lambda W}/\lambda$ con $\lambda=1/20$; $W$ è la ricchezza espressa in euro. (In A ed E $\lambda$ è il parametro dell'utilità CARA; in D indicherà un moltiplicatore.) Di una funzione di utilità $u$ si considerano l'avversione assoluta $A(W)=-u''(W)/u'(W)$ e l'avversione relativa $RR(W)=W\,A(W)$: l'utilità è CARA se $A$ non dipende da $W$ ed è CRRA se $RR$ non dipende da $W$. L'agente $j$ è più avverso al rischio dell'agente $i$ se $A_j(W)\ge A_i(W)$ per ogni $W>0$. Le lotterie $X$ hanno valore atteso nullo: con ricchezza iniziale certa $w$ la ricchezza finale è $w+X$, l'equivalente certo $CE$ è il livello di ricchezza certa tale che $E[u(w+X)]=u(CE)$ (è una ricchezza, non un guadagno) e il premio per il rischio è $R=w-CE$.
:::::

::::: {.callout kind="question" heading="A.1"}
Per l'agente 1 e poi per l'agente 2 calcola, nell'ordine, l'avversione assoluta $A(W)$ e l'avversione relativa $RR(W)$ a un livello arbitrario di ricchezza $W>0$. Classifica poi ciascuna utilità come CARA o CRRA (prima l'agente 1, poi l'agente 2). *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.2"}
Una lotteria $X$ fa guadagnare 15 € o perdere 15 €, ciascuno con probabilità $1/2$. L'agente 1 ha ricchezza iniziale $w=25$ €. Calcola, nell'ordine, l'equivalente certo $CE$ e il premio per il rischio $R$. *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.3"}
Per l'agente 1 il premio $R(w,X)$ dipende dalla ricchezza iniziale $w$ attraverso l'uguaglianza $E[u_1(w+X)]=u_1\big(w-R(w,X)\big)$. Derivandola rispetto a $w$, ricava $\partial R/\partial w$ in funzione di $E[u_1'(w+X)]$ e di $u_1'(w-R)$. Calcola poi $\partial R/\partial w$ per $w=25$ € e per la lotteria $X=\pm15$ € di A.2, e di' se il premio cresce o decresce con la ricchezza (in quest'ordine: formula, valore, verdetto). *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.4"}
Uno dei due agenti è più avverso al rischio dell'altro? Considera poi una lotteria $X$ a valore atteso nullo e piccola (per esempio $\pm1$ €): a ricchezza iniziale $w=10$ € quale dei due agenti paga il premio per il rischio maggiore? E a $w=40$ €? (Max 3 righe. Consiglio: confronta le due avversioni assolute a ciascun livello di ricchezza.) *(5 punti)*
:::::

# Domanda B (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un solo periodo. Un agente rappresentativo con utilità Bernoulliana $u$ possiede un titolo rischioso che non paga dividendi: oggi vale $P$ (il prezzo di equilibrio), domani rende la variabile casuale $\tilde y$. Il titolo privo di rischio ha rendimento lordo $R_f=1$ (un euro oggi rende un euro domani) ed è in offerta netta nulla. Nel modello base, all'equilibrio, l'agente tiene tutte le quote del titolo e la sua ricchezza finale è $\tilde y$. In questo esercizio $P$ è il prezzo del titolo (non la prudenza), $R=E[\tilde y]/P$ è il rendimento lordo atteso (non un premio per il rischio) e $\phi=R-R_f$ è il premio al rischio di mercato (non una trasformazione concava). In B.2 $A$ e $B$ sono solo etichette dei due paesi (non l'avversione assoluta). Il *pricing kernel* è $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$.
:::::

::::: {.callout kind="question" heading="B.1"}
Con utilità CRRA $u(W)=W^{1-\gamma}/(1-\gamma)$, $\gamma>0$, e $\tilde y$ poco disperso attorno al suo valore atteso, si usa l'approssimazione $\phi\approx\gamma\,\mathrm{Var}(\tilde y)/E[\tilde y]^2$ (è un'approssimazione, non un'uguaglianza). Il rapporto $\mathrm{Var}(\tilde y)/E[\tilde y]^2$ vale $0{,}0009$: $\tilde y$ ha una deviazione standard pari al 3% del suo valore atteso. Calcola, nell'ordine, il premio al rischio di mercato del modello con $\gamma=5$, in punti percentuali, e, con questa approssimazione, il valore di $\gamma$ necessario per riprodurre un premio osservato del 4,5%. *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.2"}
Due paesi, $A$ e $B$, hanno ciascuno un agente rappresentativo con $u(W)=\ln W$ e un titolo domestico: i valori $\tilde y^A$ e $\tilde y^B$ sono indipendenti e identicamente distribuiti, e valgono 1 € o 3 € con probabilità $1/2$. I due titoli hanno lo stesso prezzo $P$. Calcola, nell'ordine, il premio al rischio di mercato $\phi$ del titolo del paese $A$ (i) in autarchia, quando ciascun agente tiene solo il titolo del proprio paese, e (ii) con l'integrazione dei mercati dei capitali, quando per simmetria ciascun agente tiene la quota $\alpha^A=\alpha^B=1/2$ di ciascun titolo (nessun titolo privo di rischio) e ha ricchezza finale $W=(\tilde y^A+\tilde y^B)/2$ (quattro stati equiprobabili). *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.3"}
Il mercato ha tre stati equiprobabili e due titoli, $a$ e $b$ (etichette), con quota totale 1 ciascuno. Il valore domani del portafoglio di mercato, $\tilde y=\tilde y_a+\tilde y_b$, è $(1;\,3;\,6)$ € nei tre stati; il titolo $a$ paga $(1;\,0;\,1)$ € e il titolo $b$ paga il resto. L'agente rappresentativo ha $u(W)=\ln W$ e tiene tutte le quote dei due titoli. Il rendimento lordo del titolo $a$ è $\tilde R_a=\tilde y_a/P_a$. Calcola, nell'ordine, l'espressione del kernel $\tilde M$ in funzione di $\tilde y$, il prezzo $P_a$ e il premio $E[\tilde R_a]-R_f$ del titolo $a$. Il rendimento $\tilde R_a$ è correlato positivamente con $\tilde y$: il premio del titolo $a$ è positivo, nullo o negativo? *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.4"}
Perché l'integrazione dei mercati dei capitali di B.2 abbassa il premio al rischio di mercato del titolo del paese $A$? Che cosa cambia nel kernel e nella sua covarianza con $\tilde y^A$? (Max 3 righe. Consiglio: confronta la variabilità della ricchezza di un agente nei due casi.) *(5 punti)*
:::::

# Domanda C (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
I valori delle lotterie di questa domanda sono ricchezze finali in euro. L'agente massimizza l'utilità attesa; la sua utilità Bernoulliana è definita su tutti i valori possibili e le utilità attese esistono. Con $F$ si indica la funzione di ripartizione (c.d.f.) di una lotteria. La prima coppia è formata da due uniformi continue sugli intervalli indicati,
$$X_1\sim U[2,6]\qquad\text{e}\qquad X_2\sim U[4,7].$$
:::::

::::: {.callout kind="question" heading="C.1"}
Un agente con utilità strettamente crescente sceglie fra $X_1$ e $X_2$. Quale delle due lotterie preferisce? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.2"}
Un agente con utilità strettamente crescente e strettamente convessa (amante del rischio) sceglie fra $X_1$ e $X_2$. Quale delle due lotterie preferisce? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda coppia"}
La seconda coppia è formata da due normali, con la convenzione $\mathcal N(\mu,\sigma^2)$ in cui il secondo parametro è la varianza:
$$Z_1\sim\mathcal N(10,\,4)\qquad\text{e}\qquad Z_2\sim\mathcal N(10,\,9).$$
:::::

::::: {.callout kind="question" heading="C.3"}
Un agente con utilità strettamente crescente e strettamente concava sceglie fra $Z_1$ e $Z_2$. Quale delle due lotterie preferisce? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.4"}
Un agente ha utilità strettamente crescente, ma non si sa se concava. Puoi stabilire senza ambiguità quale fra $Z_1$ e $Z_2$ preferisce? Perché? (Max 2 righe) *(5 punti)*
:::::

# Domanda D (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Nel modello di azzardo morale sul mercato assicurativo visto a lezione un assicurato con ricchezza iniziale $w$ può subire una perdita $l\in\{0,1,\dots,L\}$, dove $l=0$ è l'assenza di sinistro. Sceglie un impegno di prevenzione $e\in\{0,1\}$, che gli costa la disutilità $d(e)$ con $d(1)>d(0)$; dato $e$, la perdita $l$ ha probabilità $\pi_l(e)>0$. L'assicurato ha utilità Bernoulliana $u$ derivabile, strettamente crescente e strettamente concava e, con impegno $e$ e ricchezza finale $z$, ottiene l'utilità $u(z)-d(e)$. Una polizza è un vettore $(p,B_0,\dots,B_L)$: il premio $p$ è dovuto in ogni caso e l'indennizzo $B_l$ è pagato se la perdita è $l$, per cui la ricchezza finale è $z_l=w-p-l+B_l$. La compagnia è una sola, neutrale al rischio; il suo profitto atteso è il premio incassato meno gli indennizzi attesi. Non osserva l'impegno, e gli indennizzi non possono dipendere da $e$. Se rifiuta la polizza, il cliente ottiene l'utilità $\bar u$. Si pone $r_l=\pi_l(0)/\pi_l(1)$, che è debolmente crescente in $l$ (MLR).
:::::

::::: {.callout kind="question" heading="D.1"}
Scrivi il problema di massimo della compagnia che vuole indurre l'impegno alto, $e=1$: la funzione obiettivo e i due vincoli, il vincolo di partecipazione (PC) e il vincolo di compatibilità degli incentivi (IC), ciascuno nella forma $g\ge0$. (A parità di utilità il cliente sceglie l'impegno voluto dalla compagnia.) *(6 punti)*
:::::

::::: {.callout kind="question" heading="D.2"}
Si sa che, per $e=1$, nella polizza ottima PC e IC valgono entrambi con uguaglianza. Spiega perché la compagnia non lascia al cliente più di $\bar u$ e perché non gli dà un incentivo più forte del necessario. (Max 3 righe. Consiglio: pensa a che cosa potrebbe fare la compagnia se un vincolo fosse lasco.) *(8 punti)*
:::::

::::: {.callout kind="question" heading="D.3"}
Con $\lambda$ e $\beta$ moltiplicatori di PC e IC (in D $\lambda$ non è il parametro di A ed E), per $e=1$ la polizza ottima soddisfa, per ogni $l$, la condizione del primo ordine
$$\frac{1}{u'(z_l)}=\lambda+\beta\,(1-r_l),\qquad\lambda>0,\ \beta>0,$$
con la normalizzazione $B_0=0$ (che non cambia né $z_l$ né il profitto). Supponi che per le perdite 0 e 1 valga $r_1=r_0$, cioè che la crescita di $r_l$ non sia stretta fra le prime due perdite. Quanto vale $B_1$? La perdita $l=1$ è coperta per intero o in parte? (Max 3 righe) *(6 punti)*
:::::

# Domanda E (20 punti)

::::: {.callout kind="abstract" heading="Il problema"}
Nel problema di portafoglio visto a lezione un investitore con ricchezza iniziale $W>0$ ha utilità Bernoulliana $u$ tre volte derivabile, con $u'>0$ e $u''<0$. Investe $\alpha\in[0,W]$ in un titolo rischioso, il cui rendimento netto $\tilde x_0$ assume un numero finito di valori, e il resto in un titolo privo di rischio con rendimento netto $r$. Posti $w_0=W(1+r)>0$ e $\tilde x=\tilde x_0-r$, il rendimento in eccesso, con $\mathbb P(\tilde x\neq 0)>0$, la ricchezza finale è $w_0+\alpha\tilde x$ e l'investitore sceglie la soluzione $\alpha^*$ di $\max_{\alpha\in[0,W]}V(\alpha)=E\big[u(w_0+\alpha\tilde x)\big]$. Si indica con $A(w)=-u''(w)/u'(w)$ l'avversione assoluta.
:::::

::::: {.callout kind="question" heading="E.1"}
Due investitori hanno $W=100$ €, $r=5\%$ e lo stesso titolo rischioso, con $\tilde x_0=-15\%$ o $+35\%$, ciascuno con probabilità $1/2$. Le loro utilità sono CARA, $u_i(w)=-e^{-\lambda_iw}/\lambda_i$, con $\lambda_1=0{,}02$ e $\lambda_2=0{,}04$ (in questa domanda $\lambda_i$ è il parametro CARA e $\phi$ è la trasformazione concava, non il premio al rischio di mercato di B); usa $\ln(3/2)\approx0{,}405$. Scrivi la condizione del primo ordine di un investitore con utilità CARA di parametro $\lambda$ e ricavane $\alpha^*$ in forma chiusa. Calcola poi $\alpha_1^*$ e $\alpha_2^*$ e verifica che siano interni, $0<\alpha_i^*<W$. Trova infine la funzione $\phi$ tale che $u_2=\phi\circ u_1$ e di' che cosa afferma il teorema sull'agente più avverso al rischio riguardo a $\alpha_2^*$ rispetto a $\alpha_1^*$ (maggiore o minore): è coerente con i tuoi numeri? *(8 punti)*
:::::

::::: {.callout kind="question" heading="E.2"}
Sia $E[\tilde x]>0$ e sia $\alpha^*\in(0,W)$ l'ottimo interno. Come funzione della ricchezza certa $w_0$, $\alpha^*(w_0)$ soddisfa la condizione del primo ordine $E\big[\tilde x\,u'(w_0+\alpha^*\tilde x)\big]=0$ e, per il teorema della funzione implicita,
$$\frac{\partial\alpha^*}{\partial w_0}=-\frac{E\big[\tilde x\,\{-u''(w_0+\alpha^*\tilde x)\}\big]}{D},\qquad D=-E\big[\tilde x^2\,u''(w_0+\alpha^*\tilde x)\big]>0.$$
Dimostra che, se $u$ ha avversione assoluta decrescente (DARA), cioè $A'(w)\le0$ per ogni $w$, allora $\partial\alpha^*/\partial w_0\ge0$, e che, se $A'(w)<0$ per ogni $w$ (DARA stretta), allora $\partial\alpha^*/\partial w_0>0$. (Consiglio: ricorda che $-u''=A\,u'$, quindi l'attesa al numeratore è $E[A(w_0+\alpha^*\tilde x)\,\tilde x\,u'(w_0+\alpha^*\tilde x)]$; ricorda anche che in $\alpha^*$ vale la condizione del primo ordine.) *(12 punti)*
:::::
