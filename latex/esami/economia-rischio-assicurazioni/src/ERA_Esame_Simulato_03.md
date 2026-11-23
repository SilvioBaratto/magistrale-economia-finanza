---
title: "Economia del Rischio — appello simulato 03"
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
L'utilità Bernoulliana di un agente è $u(W)=-e^{-\lambda W}/\lambda$ con $\lambda=2$, definita per ogni ricchezza $W$ in euro (qui $\lambda$ è il parametro dell'utilità, non il moltiplicatore di un vincolo). Di una funzione di utilità $u$ si considerano l'avversione assoluta $A(W)=-u''(W)/u'(W)$, l'avversione relativa $RR(W)=W\,A(W)$ e la prudenza assoluta $P(W)=-u'''(W)/u''(W)$. Un'utilità è DARA (avversione assoluta decrescente) se $A'(W)\le 0$ per ogni $W$: in questa traccia «decrescente» è inteso in senso debole, quindi un'utilità con $A'=0$ è DARA. Le lotterie $X$ hanno valore atteso nullo: con ricchezza iniziale certa $w$ la ricchezza finale è $w+X$, l'equivalente certo $CE$ è la ricchezza certa tale che $E[u(w+X)]=u(CE)$ (è una ricchezza, non un guadagno) e il premio per il rischio è $R=w-CE$.
:::::

::::: {.callout kind="question" heading="A.1"}
Calcola l'avversione assoluta $A(W)$ e l'avversione relativa $RR(W)$ per un valore generico della ricchezza $W$. L'utilità è di tipo CARA? È di tipo CRRA? *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.2"}
Una lotteria $X$ fa perdere $\tfrac32\ln 2$ € con probabilità $1/4$ e guadagnare $\tfrac12\ln 2$ € con probabilità $3/4$. L'agente ha ricchezza iniziale $w=5$ €. Calcola, nell'ordine, il premio per il rischio $R$ e l'equivalente certo $CE$ (si accetta la forma chiusa con il logaritmo, non serve il decimale). (Consiglio: $e^{a\ln 2}=2^{a}$.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.3"}
Calcola la prudenza assoluta $P(W)$ e la derivata $A'(W)$ per un $W$ generico, e verifica che $A'(W)=A(W)\,[A(W)-P(W)]$. L'utilità è DARA nel senso definito nei Dati? Senza ricalcolare il premio: il premio per il rischio di una lotteria $X$ a valore atteso nullo può crescere al crescere della ricchezza iniziale $w$? *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.4"}
Un secondo agente ha utilità Bernoulliana $u_2$ due volte derivabile, con $u_2'>0$, e a ogni ricchezza iniziale $w$ paga, per ogni lotteria $X$ a valore atteso nullo, un premio per il rischio $R_2(w,X)$ maggiore o uguale al premio $R_1(w,X)$ dell'agente dei Dati. Puoi concludere che $A_2(W)\ge A_1(W)$ per ogni $W$? Perché? (Max 3 righe. Consiglio: ricorda lo sviluppo di Taylor del premio per la lotteria $kX$ in $k=0$.) *(5 punti)*
:::::

# Domanda B (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un agente valuta lotterie sui premi $x_1=1$ €, $x_2=25$ € e $x_3=81$ €, con utilità Bernoulliana $u(x)=\sqrt{x}$ e ricchezza iniziale nulla: i premi sono la sua ricchezza finale. Una lotteria $Q$ si indica con il vettore delle probabilità dei tre premi, nell'ordine, $(\pi_1,\pi_2,\pi_3)$. L'equivalente certo $CE$ di $Q$ è l'importo certo con $u(CE)=E[u(Q)]$ e, poiché il valore atteso di $Q$ non è nullo, il premio per il rischio è qui $R=E[Q]-CE$ (valore atteso meno equivalente certo).
:::::

::::: {.callout kind="question" heading="B.1"}
Una lotteria in due stadi dà, con probabilità $1/3$, la lotteria $Q_a=(0,\tfrac14,\tfrac34)$ e, con probabilità $2/3$, la lotteria $Q_b=(\tfrac34,\tfrac14,0)$; sia $Q$ la lotteria composta. Scrivi la lotteria semplice equivalente a $Q$ e il suo valore atteso. *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.2"}
Per la lotteria composta $Q$ di B.1 calcola, nell'ordine, l'utilità attesa, l'equivalente certo e il premio per il rischio $R=E[Q]-CE$. *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati dell'urna"}
Un'urna contiene 10 palline: 4 rosse e 6 che sono blu o verdi, in proporzione ignota, con almeno 2 blu; ogni pallina ha la stessa probabilità di essere estratta. Quattro scommesse pagano 81 € se la pallina estratta ha un certo colore e 1 € altrimenti: la scommessa $T_1$ paga 81 € se la pallina è rossa, $T_2$ se è blu, $T_3$ se è rossa o verde, $T_4$ se è blu o verde. L'agente ha l'utilità $u(x)=\sqrt{x}$ dei Dati e valuta ogni scommessa con l'utilità max-min: il minimo dell'utilità attesa sull'insieme dei modelli di probabilità compatibili con l'informazione,
$$\mathcal M=\Big\{\mathbb P:\ \mathbb P(\text{rossa})=\tfrac25,\ \ \mathbb P(\text{blu})\in\big[\tfrac15,\tfrac35\big],\ \ \mathbb P(\text{verde})=\tfrac35-\mathbb P(\text{blu})\Big\}.$$
Un soggetto preferisce strettamente $T_1$ a $T_2$ e strettamente $T_4$ a $T_3$.
:::::

::::: {.callout kind="question" heading="B.3"}
Calcola, nell'ordine, l'utilità max-min delle scommesse $T_1$, $T_2$, $T_3$ e $T_4$, con utilità non normalizzata $u(x)=\sqrt{x}$. Le preferenze del soggetto sono spiegate da un agente max-min? *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.4"}
Perché nessuna probabilità soggettiva attribuita al colore blu rende le preferenze del soggetto compatibili con l'utilità attesa? Quale presupposto sulle probabilità, richiesto dal teorema dell'utilità attesa, viene a mancare? (Max 3 righe. Consiglio: dai al colore blu una probabilità soggettiva e vedi che cosa implica ciascuna preferenza.) *(5 punti)*
:::::

# Domanda C (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Una comunità di agenti si divide in parti uguali le perdite di reddito dei suoi membri. Ogni perdita vale 400 € e si verifica con probabilità $1/5$; i valori in gioco sono variazioni di reddito, nulle o negative. Gli agenti hanno utilità Bernoulliana $u$ strettamente crescente. Qui solo l'agente 1 può subire la perdita; l'agente 2 non ha alcun rischio. Se i due formano una comunità (situazione G) ciascuno sopporta metà dell'eventuale perdita; altrimenti ciascuno resta solo (situazione S).
:::::

::::: {.callout kind="question" heading="C.1"}
Puoi stabilire senza ambiguità se l'agente 1 preferisce S o G? Se sì, indicala. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.2"}
Puoi stabilire senza ambiguità se l'agente 2 preferisce S o G? Se sì, indicala. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda coppia"}
Ora ciascuno dei due agenti può subire la perdita di 400 € con probabilità $1/5$, indipendentemente dall'altro. Con $N=1$ un agente è solo e sopporta la propria perdita; con $N=2$ i due formano una comunità e dividono a metà la somma delle perdite.
:::::

::::: {.callout kind="question" heading="C.3"}
Un agente con utilità strettamente crescente: puoi stabilire senza ambiguità se preferisce $N=1$ o $N=2$? Se sì, indica quale. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.4"}
Se $u$ è anche strettamente concava (agente strettamente avverso al rischio), quale situazione preferisce, $N=1$ o $N=2$? Perché? (Max 2 righe) *(5 punti)*
:::::

# Domanda D (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Nel modello di screening visto a lezione i consumatori hanno ricchezza iniziale $w$, possono subire un incidente che causa la perdita $L$ (con $0<L<w$) e hanno utilità Bernoulliana $u$ derivabile, strettamente crescente e strettamente concava. Ci sono due tipi di consumatori, a basso rischio e ad alto rischio, con probabilità di incidente $0<\underline\pi<\overline\pi<1$ (la lettera $\pi$ indica sempre una probabilità, la lettera $p$ un premio). Due compagnie concorrenti, neutrali al rischio e senza costi, non osservano il tipo e offrono contratti $(B,p)$: l'indennizzo $B$ è pagato in caso di incidente (anche con copertura parziale, $B\neq L$) e il premio $p$ è pagato in ogni caso. Un consumatore di probabilità $\pi$ che sceglie $(B,p)$ ha ricchezza $w-p-L+B$ se subisce l'incidente e $w-p$ altrimenti, e utilità attesa
$$EU(B,p;\pi)=\pi\,u(w-p-L+B)+(1-\pi)\,u(w-p).$$
Nel piano $(B,p)$, con $B$ sull'asse orizzontale e $p$ su quello verticale, una curva di indifferenza è l'insieme dei contratti con $EU$ costante. Un contratto venduto a un consumatore di probabilità $\pi$ dà alla compagnia il profitto atteso $p-\pi B$; la retta di profitto nullo di quel tipo è $p=\pi B$.
:::::

::::: {.callout kind="question" heading="D.1"}
Ricava la pendenza $s=dp/dB$ della curva di indifferenza di un consumatore di probabilità $\pi$ nel contratto $(B,p)$ e mostra che, a $(B,p)$ fissato, $\partial s/\partial\pi>0$. Che cosa ne segue per le curve di indifferenza dei due tipi nello stesso contratto? *(6 punti)*
:::::

::::: {.callout kind="question" heading="D.2"}
In un equilibrio separante ciascun contratto scelto sta sulla retta di profitto nullo del proprio tipo: $p=\underline\pi B$ per il basso rischio e $p=\overline\pi B$ per l'alto rischio. Perché il contratto scelto dall'alto rischio prevede la copertura piena, $B=L$? (Max 3 righe. Consiglio: confronta, nel contratto dell'alto rischio, la curva di indifferenza con la retta di profitto nullo.) *(8 punti)*
:::::

::::: {.callout kind="question" heading="D.3"}
Un mercato con un solo prezzo può fallire del tutto: con $\pi$ uniforme su $[0,1]$ l'equilibrio $p^*=L$ non porta a nessuna transazione utile. Si supponga che con lo screening esista un equilibrio separante, con un contratto per tipo, profitto nullo per le compagnie e un indennizzo $\overline B_l>0$ per il basso rischio. Rispetto all'esito in cui nessuno dei due tipi si assicura, l'equilibrio separante è un miglioramento paretiano? È Pareto efficiente rispetto alle allocazioni fattibili quando le compagnie osservano il tipo? Perché? (Max 3 righe) *(6 punti)*
:::::

# Domanda E (20 punti)

::::: {.callout kind="abstract" heading="Il problema"}
Nel problema di portafoglio visto a lezione un investitore con ricchezza iniziale $W>0$ ha utilità Bernoulliana $u$ tre volte derivabile, con $u'>0$ e $u''<0$; l'argomento di $u$ è una ricchezza $c$, mentre $W$ indica solo la ricchezza iniziale. Investe $\alpha\in[0,W]$ in un titolo rischioso, il cui rendimento netto $\tilde x_0$ vale $-30\%$ oppure $+100\%$, ciascuno con probabilità $1/2$, e il resto in un titolo senza rischio, il cui rendimento netto è $r=10\%$. Quindi $w_0=W(1+r)=1{,}1\,W$ e il rendimento in eccesso è $\tilde x=\tilde x_0-r$. La ricchezza finale è $w_0+\alpha\tilde x$ e la scelta dell'investitore è la soluzione di
$$\max_{\alpha\in[0,W]}\ V(\alpha)=E\big[u(w_0+\alpha\tilde x)\big].$$
:::::

::::: {.callout kind="question" heading="E.1"}
Scrivi la condizione del primo ordine. Ricava poi $\alpha^*$ in funzione di $w_0$ per $u(c)=\ln c$ e per $v(c)=-1/c$, controllando che sia $\alpha^*\le W$. Come variano con $w_0$ l'ammontare investito e la quota $\alpha^*/w_0$? Quale dei due agenti investe di più? Spiega, con il teorema sull'agente più avverso al rischio, perché l'ordine non dipende da $w_0$ né dalla distribuzione di $\tilde x$ (purché $E[\tilde x]>0$ e l'ottimo con $v$ sia interno). (Consiglio: con $v'(c)=c^{-2}$ conviene prendere la radice quadrata della condizione.) *(8 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati di E.2"}
Siano $A(c)=-u''(c)/u'(c)$ l'avversione assoluta, $RR(c)=c\,A(c)$ l'avversione relativa, $P(c)=-u'''(c)/u''(c)$ la prudenza assoluta e $RP(c)=c\,P(c)$ la prudenza relativa. Sia $w_0>0$ e sia $h(y)=y\,u'(w_0+y)$, definita per i valori di $y$ per cui $w_0+y$ è una ricchezza ammissibile: la funzione $h$ governa il confronto fra la domanda di titoli di rischiosità diversa.
:::::

::::: {.callout kind="question" heading="E.2"}
(i) Calcola $h''(y)$ e scrivila in funzione di $u''(w_0+y)$, di $RP$ e $P$ valutate in $w_0+y$ e di $w_0$. (ii) Mostra che $h$ è concava se $RP(c)<2$ e $P(c)>0$ per ogni ricchezza ammissibile $c$. (iii) Per quali valori di $\gamma$ l'utilità $u(c)=c^{1-\gamma}/(1-\gamma)$, con $\gamma>0$ e $\gamma\neq 1$, soddisfa $RR<1$, $P>0$ e $RP<2$ per ogni $c>0$? (iv) Il logaritmo ($\gamma=1$) ha $RR=1$ e $RP=2$, quindi non le soddisfa: mostra tuttavia che, con $u=\ln$, la funzione $h$ è crescente e concava. (Consiglio: derivando due volte il prodotto $y\,u'(w_0+y)$ compaiono $u''$ e $u'''$ calcolate in $w_0+y$; $P$ e $RP$ sono definite alla ricchezza finale $w_0+y$, non in $y$; per il segno ricorda che $u''<0$; per (iii) calcola $RR$, $P$ e $RP$ dalle derivate di $u$ e imponi le tre disuguaglianze.) *(12 punti)*
:::::
