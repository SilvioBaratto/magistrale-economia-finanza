---
title: "Economia del Rischio — appello simulato 01"
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
La ricchezza $W$ di un agente, in euro, gli dà l'utilità Bernoulliana $u(W)=-1/W$, definita per $W>0$. Una lotteria $X$ fa perdere 2 € con probabilità $2/3$ e fa guadagnare 4 € con probabilità $1/3$: ha valore atteso nullo. Se l'agente ha ricchezza iniziale certa $w$, la sua ricchezza finale è $w+X$. L'equivalente certo $CE$ è il livello di ricchezza certa tale che $E[u(w+X)]=u(CE)$ (è una ricchezza, non un guadagno) e il premio per il rischio è $R=w-CE$.
:::::

::::: {.callout kind="question" heading="A.1"}
Determina l'avversione assoluta $A(W)$ e quella relativa $RR(W)$ al rischio per un generico $W>0$. L'utilità è di tipo CARA o CRRA? *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.2"}
L'agente ha ricchezza iniziale $w_1=4$ €. Calcola l'equivalente certo della ricchezza aleatoria $w_1+X$ e il premio per il rischio $R_1$. *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.3"}
Ora l'agente ha ricchezza iniziale $w_2=6$ €. Calcola il premio per il rischio $R_2$ della stessa lotteria $X$. Calcola poi il coefficiente di prudenza assoluta $P(W)=-u'''(W)/u''(W)$ e, confrontandolo con $A(W)$, spiega perché il premio per il rischio a $w_2$ deve essere minore o maggiore di quello a $w_1=4$ €. (Nota: un'utilità ha avversione assoluta al rischio decrescente, DARA, se $A'(W)\le 0$ per ogni $W$, in senso stretto se $A'(W)<0$.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.4"}
Sia $kX$ la lotteria $X$ moltiplicata per un fattore $k>0$ piccolo, a ricchezza iniziale $w_1=4$ €, e sia $R(k)$ il suo premio per il rischio. Per quale fattore si moltiplica, circa, il premio per il rischio se $k$ raddoppia? Perché? Si chiede l'approssimazione per $k$ piccolo, non il valore esatto. (Max 3 righe. Consiglio: pensa allo sviluppo di Taylor di $R(k)$ in $k=0$.) *(5 punti)*
:::::

# Domanda B (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un consumatore ha ricchezza iniziale $w=36$ € e utilità Bernoulliana $u(W)=\sqrt{W}$. Con probabilità $\pi$ subisce una perdita $L=20$ €, per cui la sua ricchezza finale è $w-L$; con probabilità $1-\pi$ non perde nulla. Una compagnia di assicurazione, neutrale al rischio e senza costi, vende una polizza a copertura piena: paga $L$ in caso di perdita, a fronte di un prezzo $p$ (premio) pagato in ogni caso. Il consumatore che compra la polizza ha ricchezza certa $w-p$. A parità di utilità il consumatore compra.
:::::

::::: {.callout kind="question" heading="B.1"}
Sia $\pi=1/4$. Calcola il premio equo della polizza, cioè quello per cui il profitto atteso della compagnia è nullo, e confronta l'utilità attesa del consumatore con e senza copertura piena a quel premio. Quale situazione preferisce? Perché? *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.2"}
Sia ancora $\pi=1/4$. Calcola l'equivalente certo della posizione senza assicurazione, il premio massimo che il consumatore pagherebbe per la copertura piena e il premio per il rischio. (Nota: qui il premio per il rischio è la ricchezza attesa meno l'equivalente certo, perché il valore atteso della perdita non è zero.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.3"}
Considera ora una popolazione di consumatori, tutti con gli stessi $w$, $L$ e $u$ di sopra, in cui la probabilità di perdita $\pi$ è uniforme su $[0,1]$ e non è osservata dalle compagnie. Le compagnie offrono la stessa polizza a un prezzo unico $p$. Indica con $h(p)$ la soglia di probabilità di perdita sopra la quale il consumatore compra. Un prezzo è di equilibrio se il profitto atteso per polizza venduta, calcolato sugli acquirenti effettivi, è nullo. Per $p=11$ €, calcola $h(p)$, la probabilità media di perdita fra gli acquirenti e il profitto atteso per polizza venduta: il prezzo $p=11$ € è di equilibrio?

Verifica poi che $p=L$ è un prezzo di equilibrio. (Nota: per $p=L$ la soglia vale 1 e la probabilità media fra gli acquirenti si intende come limite di $E[\pi\mid\pi\ge t]$ per $t\to 1$.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.4"}
Ammetti ora due soli tipi di consumatore, a basso rischio ($\pi_l$) e ad alto rischio ($\pi_h$), con $\pi_l<\pi_h$, con gli stessi $w$, $L$ e $u$. Le compagnie, concorrenti e neutrali al rischio, possono offrire contratti $(B,p)$ con $0\le B\le L$: l'indennizzo $B$ è pagato in caso di perdita, anche con copertura parziale ($B<L$), e il premio $p$ è pagato in ogni caso. In un equilibrio separante i due tipi scelgono contratti diversi, ciascuno con profitto atteso nullo, e l'alto rischio sceglie la copertura piena al prezzo equo, $(L,\pi_hL)$. Perché il contratto scelto dal basso rischio prevede una copertura parziale, $B<L$? (Max 3 righe. Consiglio: nel piano $(B,p)$ confronta le pendenze delle curve di indifferenza dei due tipi nello stesso contratto.) *(5 punti)*
:::::

# Domanda C (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
I premi possibili sono 20, 30 e 40 €. Una lotteria si indica con le probabilità dei tre premi, nell'ordine. Un agente con utilità crescente deve scegliere fra le lotterie
$$p=(1/10;\,7/10;\,2/10)\qquad\text{e}\qquad q=(2/10;\,5/10;\,3/10).$$
:::::

::::: {.callout kind="question" heading="C.1"}
Puoi stabilire senza ambiguità quale lotteria, fra $p$ e $q$, preferisce l'agente? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.2"}
Se l'agente è anche strettamente avverso al rischio ($u$ strettamente concava), quale lotteria preferisce fra $p$ e $q$? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda coppia"}
Siano $\alpha=1/2$ e $L_c=(0;\,1;\,0)$ la lotteria che dà 30 € con certezza. Si considerano le lotterie composte sugli stessi tre premi
$$p'=\alpha\,p+(1-\alpha)\,L_c\qquad\text{e}\qquad q'=\alpha\,q+(1-\alpha)\,L_c,$$
con $p$ e $q$ definite sopra.
:::::

::::: {.callout kind="question" heading="C.3"}
Un agente che massimizza l'utilità attesa, non necessariamente avverso al rischio, preferisce $p$ a $q$. Quale lotteria sceglie fra $p'$ e $q'$? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.4"}
Un soggetto preferisce strettamente $q$ a $p$ e strettamente $p'$ a $q'$. Queste preferenze sono compatibili con la teoria dell'utilità attesa? Perché, nel triangolo di Machina? (Max 2 righe) *(5 punti)*
:::::

# Domanda D (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Nel modello di azzardo morale sul mercato assicurativo visto a lezione, un assicurato con ricchezza iniziale $w$ è esposto a una perdita $l\in\{0,1,\dots,L\}$, dove $l=0$ indica che non c'è sinistro, e decide quanto impegno $e\in\{0,1\}$ dedicare a prevenirla; l'impegno ha una disutilità $d(e)$, con $d(1)>d(0)$. Dato $e$, la perdita $l$ si verifica con probabilità $\pi_l(e)>0$. L'assicurato ha utilità Bernoulliana $u$ derivabile, strettamente crescente e strettamente concava. Con una polizza che prevede il premio $p$, dovuto in ogni caso, e l'indennizzo $B_l$ se la perdita è $l$, la sua utilità è
$$\sum_{l=0}^{L}\pi_l(e)\,u(w-p-l+B_l)-d(e).$$
La compagnia è neutrale al rischio: incassa $p$ e paga $B_l$ se la perdita è $l$. Il valore $\bar u$ è l'utilità che l'assicurato ottiene se rifiuta la polizza.
:::::

::::: {.callout kind="question" heading="D.1"}
Supponi che la compagnia possa osservare l'impegno, che è quindi un dato $e$. Il problema della compagnia è
$$\max_{p,\,B_0,\dots,B_L}\ p-\sum_{l=0}^{L}\pi_l(e)\,B_l\qquad\text{s.t.}\qquad \sum_{l=0}^{L}\pi_l(e)\,u(w-p-l+B_l)-d(e)\ \ge\ \bar u.$$
Costruisci la Lagrangiana, indicando con $\lambda$ il moltiplicatore del vincolo, e scrivi le condizioni del primo ordine in $p$ e in ciascun $B_l$. Mostra che da esse segue la copertura piena, $B_l=l$ per ogni $l$, con la normalizzazione $B_0=0$ (senza questa normalizzazione la soluzione è unica solo a meno di una traslazione di $p$ e di tutti i $B_l$). *(6 punti)*
:::::

::::: {.callout kind="question" heading="D.2"}
Supponi ora che la compagnia NON possa osservare $e$. Al vincolo precedente si aggiunge il constraint di compatibilità con gli incentivi: fra i due livelli, il cliente deve scegliere proprio l'impegno $e$ che la compagnia vuole indurre:
$$\sum_{l=0}^{L}\pi_l(e)\,u(w-p-l+B_l)-d(e)\ \ge\ \sum_{l=0}^{L}\pi_l(e')\,u(w-p-l+B_l)-d(e'),\qquad e'\neq e.$$
Se il cliente è indifferente, sceglie l'impegno voluto dalla compagnia. Spiega perché, se la compagnia vuole indurre $e=0$, la polizza ottima è la stessa del punto D.1, a copertura piena. (Max 3 righe. Consiglio: la polizza deve rispettare entrambi i vincoli.) *(8 punti)*
:::::

::::: {.callout kind="question" heading="D.3"}
Con l'impegno osservabile, la compagnia sceglie l'impegno che massimizza il suo profitto con la polizza di D.1, e il massimo è raggiunto in un solo livello, $e^*=0$. L'impossibilità di osservare l'impegno crea inefficienza, cioè un'allocazione che non è Pareto efficiente rispetto alle allocazioni fattibili quando l'impegno è osservabile? Perché? (Max 3 righe) *(6 punti)*
:::::

# Domanda E (20 punti)

::::: {.callout kind="abstract" heading="Il problema"}
Nel problema di portafoglio visto a lezione un investitore con ricchezza iniziale $W>0$ ha utilità Bernoulliana $u$ tre volte derivabile, con $u'>0$ e $u''<0$. Destina l'importo $\alpha\in[0,W]$ a un titolo rischioso, il cui rendimento netto $\tilde x_0$ è aleatorio, e il resto a un titolo sicuro di rendimento netto $r$. Posti $w_0=W(1+r)>0$ e $\tilde x=\tilde x_0-r$, il rendimento in eccesso, che assume un numero finito di valori con $\mathbb P(\tilde x\neq 0)>0$ e $E[\tilde x]>0$, la sua scelta è la soluzione di
$$\max_{\alpha\in[0,W]}\ V(\alpha)=E\big[u(w_0+\alpha\tilde x)\big].$$
:::::

::::: {.callout kind="question" heading="E.1"}
Calcola $V'(\alpha)$ e $V''(\alpha)$ e scrivi la condizione del primo ordine che caratterizza un ottimo interno, $0<\alpha^*<W$. Per un tale ottimo, applica il teorema della funzione implicita alla condizione del primo ordine: scrivi $d\alpha^*/dw_0$ e di' di quale valore atteso, scritto con $u''$, ha lo stesso segno. *(8 punti)*
:::::

::::: {.callout kind="question" heading="E.2"}
Il rendimento in eccesso ha due possibili distribuzioni, con funzioni di ripartizione $F_1$ e $F_2$, e $F_2$ è preferita a $F_1$ nel senso della dominanza stocastica del secondo ordine (il titolo con $F_2$ è il meno rischioso). Per $i=1,2$ sia $V_i(\alpha)=E_{F_i}\big[u(w_0+\alpha\tilde x)\big]$ e sia $\alpha_i^*$ il suo massimo su $[0,W]$, unico perché $V_i$ è strettamente concava (si assume $\mathbb P_{F_i}(\tilde x\neq 0)>0$). Supponi $\alpha_1^*$ interno e $g(x)=x\,u'(w_0+\alpha_1^*x)$ concava in $x$ su tutti i valori di $x$ per cui $w_0+\alpha_1^*x$ è una ricchezza ammissibile. Siano $A(w)=-u''(w)/u'(w)$ e $RR(w)=w\,A(w)$ le misure di avversione assoluta e relativa al rischio. Mostra che, se $RR(w)<1$ per ogni ricchezza finale ammissibile $w$, allora $\alpha_2^*\ge\alpha_1^*$: passando a un titolo meno rischioso l'investimento ottimo non scende. (Consiglio: ricorda che in $\alpha_1^*$ vale la FOC sotto $F_1$, quindi basta verificare che sotto $F_2$ la derivata della funzione obiettivo in $\alpha_1^*$ non sia negativa. La dominanza del secondo ordine garantisce $E_{F_2}[G(\tilde x)]\ge E_{F_1}[G(\tilde x)]$ per ogni $G$ crescente e concava: poiché la concavità di $g$ è assegnata, resta da provare che $g$ cresce. Con $h(y)=y\,u'(w_0+y)$ si ha $g(x)=h(\alpha_1^*x)/\alpha_1^*$: esprimi $h'(y)$ tramite $A$ e $RR$ valutati in $w_0+y$ e mostra che è positiva quando $RR<1$.) *(12 punti)*
:::::
