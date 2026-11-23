---
title: "Economia del Rischio — appello simulato 02"
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
Due agenti hanno funzione di utilità Bernoulliana $u_1(W)=\sqrt{W}$ (agente 1) e $u_2(W)=\ln W$ (agente 2), definite per $W>0$, dove $W$ è la ricchezza in euro. Di una funzione di utilità $u$ si considerano l'avversione assoluta $A(W)=-u''(W)/u'(W)$, l'avversione relativa $RR(W)=W\,A(W)$ e la prudenza assoluta $P(W)=-u'''(W)/u''(W)$. L'agente 2 è più avverso al rischio dell'agente 1 se $A_2(W)\ge A_1(W)$ per ogni $W>0$; un agente è DARA (avversione assoluta decrescente) se $A'(W)\le 0$ per ogni $W>0$. Le lotterie $X$ hanno valore atteso nullo: con ricchezza iniziale certa $w$ la ricchezza finale è $w+X$, l'equivalente certo $CE$ è il livello di ricchezza certa tale che $E[u(w+X)]=u(CE)$ (è una ricchezza, non un guadagno) e il premio per il rischio è $R=w-CE$.
:::::

::::: {.callout kind="question" heading="A.1"}
Per l'agente 1 e poi per l'agente 2 calcola, nell'ordine, $A(W)$, $RR(W)$ e $P(W)$ a un livello arbitrario di ricchezza $W>0$. Quale dei due agenti è più avverso al rischio? Ciascuno dei due è DARA (prima l'agente 1, poi l'agente 2)? (Per rispondere all'ultima domanda confronta $P(W)$ con $A(W)$.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.2"}
Una lotteria $X$ fa guadagnare 20 € o perdere 20 €, ciascuno con probabilità $1/2$. I due agenti hanno la stessa ricchezza iniziale $w=29$ €. Calcola, nell'ordine, l'equivalente certo $CE_1$ e il premio per il rischio $R_1$ dell'agente 1, poi $CE_2$ e $R_2$ dell'agente 2. *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.3"}
Esiste una funzione $\phi$, definita per $x>0$, tale che $u_2(W)=\phi\big(u_1(W)\big)$ per ogni $W>0$. Trovala e calcola $\phi''$. Verifica poi, usando le misure di A.1, che
$$\phi''\big(u_1(W)\big)=\frac{u_2'(W)}{\big(u_1'(W)\big)^2}\,\big[A_1(W)-A_2(W)\big].$$
(In questa domanda $\phi$ è la funzione che lega le due utilità; in B indicherà un'altra grandezza.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.4"}
Confronta i premi per il rischio $R_1$ e $R_2$ dei due agenti. L'ordine $R_2\ge R_1$ vale per ogni ricchezza iniziale $w>0$ e per ogni lotteria $X$ con $E[X]=0$ e $w+X>0$? Perché? (Max 3 righe. Consiglio: che relazione lega $u_1$ e $u_2$?) *(5 punti)*
:::::

# Domanda B (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un agente rappresentativo con utilità Bernoulliana $u(W)=\ln W$ parte con una quota di un titolo rischioso e sceglie la quota $\alpha$ da tenere, senza vincoli, vendendo o comprando le altre quote al prezzo $P$. Il titolo non paga dividendi: domani vale $\tilde y=2$ € nello stato 1 e $\tilde y=3$ € nello stato 2, due stati equiprobabili. Il titolo privo di rischio ha rendimento lordo $R_f=1$ (un euro oggi rende un euro domani) ed è in offerta netta nulla. Con la quota $\alpha$ la ricchezza finale è $W=\alpha\tilde y+(1-\alpha)R_fP$ e il mercato è in equilibrio se la quota ottima è $\alpha=1$. In questo esercizio $P$ è il prezzo del titolo (non la prudenza), $R=E[\tilde y]/P$ è il rendimento lordo atteso (non un premio per il rischio) e $\phi=R-R_f$ è il premio al rischio di mercato (non una trasformazione concava). In B.2 «$a$» e «$b$» sono solo etichette dei due titoli.
:::::

::::: {.callout kind="question" heading="B.1"}
Calcola, nell'ordine, il prezzo di equilibrio $P$, il rendimento lordo atteso $R$ e il premio al rischio di mercato $\phi$. *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.2"}
Il valore del titolo è la somma dei valori di due titoli, $\tilde y=\tilde y_a+\tilde y_b$, ciascuno con quota totale pari a 1: il titolo $a$ vale 1,5 € nello stato 1 e 2 € nello stato 2, il titolo $b$ vale 0,5 € nello stato 1 e 1 € nello stato 2. In equilibrio l'agente tiene tutte le quote dei due titoli. Sia $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$ il pricing kernel. Calcola, nell'ordine, il valore di $\tilde M$ nello stato 1 e nello stato 2, il prezzo $P_b$ del titolo $b$, il suo premio al rischio di mercato $E[\tilde R_b]-R_f$ con $\tilde R_b=\tilde y_b/P_b$ e la covarianza $\mathrm{Cov}(\tilde R_b,\tilde M)$. Verifica che il premio è uguale a $-\mathrm{Cov}(\tilde R_b,\tilde M)$. *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.3"}
Solo una frazione $k=1/3$ degli agenti, tutti identici, può detenere il titolo rischioso di B.1; gli altri vendono la propria quota e investono nel titolo privo di rischio. Il mercato si chiude se i partecipanti, tutti insieme, tengono tutte le quote: ciascuno ne tiene $\alpha=1/k$, prendendo a prestito al tasso $R_f$. Indica con $P(k)$ il prezzo di equilibrio e con $W_k$ la ricchezza finale di un partecipante. Scrivi, nell'ordine, $W_k$ in funzione di $\tilde y$ e $P(k)$, la condizione del primo ordine che determina $P(k)$, il prezzo $P(k)$ (risolvendo l'equazione di secondo grado che ne segue) e il premio al rischio di mercato $\phi(k)=E[\tilde y]/P(k)-R_f$. Fra le due radici dell'equazione, $P(k)$ è la minore (con l'altra la ricchezza di un partecipante sarebbe negativa in uno stato e $\ln$ non sarebbe definito). *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.4"}
Perché $\phi(k)$ è maggiore di $\phi$? E perché la partecipazione limitata è proposta come spiegazione dell'*equity premium puzzle*? (Max 3 righe. Consiglio: chi sopporta il rischio del titolo?) *(5 punti)*
:::::

# Domanda C (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Il rendimento in eccesso $\tilde x$ di un titolo rischioso (il suo rendimento netto meno quello del titolo privo di rischio) assume i valori $\{-20\%;\ 10\%;\ 40\%\}$. Un agente con ricchezza finale certa $w_0$ senza investimento destina al titolo un ammontare $\alpha\in[0,W]$ ($W$ è la ricchezza iniziale e $w_0=W(1+r)$, con $r$ il rendimento netto del titolo privo di rischio), senza vendite allo scoperto, e ottiene la ricchezza finale $w_0+\alpha\tilde x$. L'agente ha utilità Bernoulliana $u$ derivabile con $u'>0$ (e $u''<0$ dove si dice). Una distribuzione di $\tilde x$ si indica con le probabilità dei tre valori, nell'ordine: $F_i$ indica qui il vettore delle probabilità dei tre valori, non la funzione di ripartizione. La prima coppia di distribuzioni è
$$F_1=(4/10;\,4/10;\,2/10)\qquad\text{e}\qquad F_2=(3/10;\,3/10;\,4/10).$$
:::::

::::: {.callout kind="question" heading="C.1"}
Puoi stabilire senza ambiguità quale delle due distribuzioni preferisce un agente con utilità crescente che investe lo stesso ammontare $\alpha>0$ nel titolo? Se sì, indicala. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.2"}
Puoi dire quale delle due distribuzioni ha il rendimento atteso maggiore? Perché? Una media maggiore basterebbe, da sola, perché una distribuzione domini l'altra al primo ordine? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda coppia"}
Sugli stessi tre valori di $\tilde x$ si considera una seconda coppia di distribuzioni,
$$F_3=(2/6;\,1/6;\,3/6)\qquad\text{e}\qquad F_4=(1/6;\,3/6;\,2/6).$$
:::::

::::: {.callout kind="question" heading="C.3"}
Un agente con utilità crescente e strettamente concava sceglie l'ammontare $\alpha\in[0,W]$ che massimizza la sua utilità attesa, prima quando il titolo ha la distribuzione $F_3$ e poi quando ha la $F_4$. Quale dei due portafogli ottimi preferisce? Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.4"}
In generale, siano $G$ e $H$ le distribuzioni del rendimento in eccesso di due titoli, con $G$ che domina $H$ al secondo ordine. Un agente con utilità crescente e strettamente concava sceglie l'ammontare $\alpha_G^*\in[0,W]$ che massimizza la sua utilità attesa se può investire solo in $G$ (oltre che nel titolo privo di rischio), e l'ammontare $\alpha_H^*\in[0,W]$ se può investire solo in $H$. Dalla sola dominanza del secondo ordine segue che ogni agente di questo tipo investe in $G$ almeno quanto investe in $H$? Perché? (Max 2 righe) *(5 punti)*
:::::

# Domanda D (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Nel modello di azzardo morale sul mercato assicurativo visto a lezione un assicurato con ricchezza iniziale $w$ può subire una perdita $l\in\{0,1,\dots,L\}$, dove $l=0$ è l'assenza di sinistro, e sceglie l'impegno $e\in\{0,1\}$ da dedicare alla prevenzione, con disutilità $d(e)$ e $d(1)>d(0)$. Dato $e$, la perdita $l$ ha probabilità $\pi_l(e)>0$. L'assicurato ha utilità Bernoulliana $u$ derivabile, strettamente crescente e strettamente concava. Con una polizza di premio $p$, dovuto in ogni caso, e indennizzo $B_l$ se la perdita è $l$, la sua ricchezza finale è $z_l=w-p-l+B_l$ e la sua utilità è $\sum_{l=0}^{L}\pi_l(e)\,u(z_l)-d(e)$. La compagnia è neutrale al rischio e non osserva $e$; $\bar u$ è l'utilità che l'assicurato ottiene senza polizza. La compagnia vuole indurre l'impegno alto, $e=1$, e risolve
$$\max_{p,\,B_0,\dots,B_L}\ p-\sum_{l=0}^{L}\pi_l(1)\,B_l\quad\text{s.t.}\quad
\begin{cases}
\text{(PC)}\quad \sum_{l}\pi_l(1)\,u(z_l)-d(1)\ \ge\ \bar u,\\[2pt]
\text{(IC)}\quad \sum_{l}\pi_l(1)\,u(z_l)-d(1)\ \ge\ \sum_{l}\pi_l(0)\,u(z_l)-d(0).
\end{cases}$$
Con il moltiplicatore $\lambda$ per PC e $\beta$ per IC, la Lagrangiana è
$$\mathcal L=p-\sum_{l}\pi_l(1)B_l+\lambda\Big[\sum_{l}\pi_l(1)u(z_l)-d(1)-\bar u\Big]+\beta\Big[\sum_{l}\pi_l(1)u(z_l)-d(1)-\sum_{l}\pi_l(0)u(z_l)+d(0)\Big].$$
Si pone $r_l=\pi_l(0)/\pi_l(1)$; la normalizzazione $B_0=0$ si impone dopo la derivazione, perché la traslazione $(p,B_l)\to(p+c,B_l+c)$ non cambia né $z_l$ né il profitto.
:::::

::::: {.callout kind="question" heading="D.1"}
Scrivi la condizione del primo ordine della Lagrangiana rispetto a $B_l$, per $l=0,1,\dots,L$ (prima di imporre $B_0=0$), e mostra che equivale a
$$\frac{1}{u'(z_l)}=\lambda+\beta\,(1-r_l).$$
*(6 punti)*
:::::

::::: {.callout kind="question" heading="D.2"}
Supponi che $r_l$ sia strettamente crescente in $l$ (proprietà del rapporto di verosimiglianza monotono, MLR), che nell'ottimo valga $\beta>0$ e che valga la condizione di D.1. Spiega perché $\lambda>0$. (Max 3 righe. Consiglio: confronta il segno dei due membri della condizione di D.1.) *(8 punti)*
:::::

::::: {.callout kind="question" heading="D.3"}
Supponi che, con impegno osservabile (benchmark o *first best*), il massimo del profitto della compagnia sia raggiunto in un solo livello di impegno, $e^*=1$. L'esito che si ottiene con impegno non osservabile (*second best*) è Pareto efficiente rispetto alle allocazioni fattibili quando l'impegno è osservabile? Chi perde rispetto al benchmark? (Max 3 righe) *(6 punti)*
:::::

# Domanda E (20 punti)

::::: {.callout kind="abstract" heading="Il problema"}
Nel problema di portafoglio visto a lezione un investitore con ricchezza iniziale $W>0$ ha utilità Bernoulliana $u$ derivabile con $u'>0$ e $u''<0$. Investe $\alpha\in[0,W]$ in un titolo rischioso, il cui rendimento netto $\tilde x_0$ assume un numero finito di valori, e il resto in un titolo privo di rischio con rendimento netto $r$. Posti $w_0=W(1+r)>0$ e $\tilde x=\tilde x_0-r$, il rendimento in eccesso, con $\mathbb P(\tilde x\neq 0)>0$, la ricchezza finale è $w_0+\alpha\tilde x$ e la scelta dell'investitore è la soluzione $\alpha^*$ di
$$\max_{\alpha\in[0,W]}\ V(\alpha)=E\big[u(w_0+\alpha\tilde x)\big].$$
La funzione $V$ è strettamente concava, quindi la soluzione è unica.
:::::

::::: {.callout kind="question" heading="E.1"}
Calcola $V'(0)$. Dimostra che $\alpha^*>0$ se e solo se $E[\tilde x]>0$, cioè se e solo se $E[\tilde x_0]>r$. Spiega poi perché basta anche un rendimento atteso positivo molto piccolo perché l'investitore investa qualcosa nel titolo rischioso. (Consiglio: considera un piccolo importo $\varepsilon$ investito nel titolo rischioso.) *(8 punti)*
:::::

::::: {.callout kind="question" heading="E.2"}
Due agenti hanno la stessa ricchezza $w_0$ e fronteggiano lo stesso rendimento in eccesso $\tilde x$, con $E[\tilde x]>0$. L'agente 1 ha utilità $u_1$, con $u_1'>0$ e $u_1''<0$; l'agente 2 ha utilità $u_2=\phi\circ u_1$, con $\phi$ due volte derivabile, $\phi'>0$ e $\phi''<0$. Per $i=1,2$ sia $V_i(\alpha)=E\big[u_i(w_0+\alpha\tilde x)\big]$ e sia $\alpha_i^*$ il suo massimo su $[0,W]$; si assume $0<\alpha_2^*<W$. Dimostra che $\alpha_2^*<\alpha_1^*$. (Consiglio: poiché $V_1$ è strettamente concava, basta mostrare che $V_1'(\alpha_2^*)>0$. Scrivi la condizione del primo ordine dell'agente 2 e, con la regola della catena $u_2'=\phi'(u_1)\,u_1'$, riconducila a $V_1'(\alpha_2^*)$.) *(12 punti)*
:::::
