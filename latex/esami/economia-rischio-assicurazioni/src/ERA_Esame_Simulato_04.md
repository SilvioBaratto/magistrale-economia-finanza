---
title: "Economia del Rischio — appello simulato 04"
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
Le preferenze di un agente sono rappresentate da una utilità di Bernoulli quadratica
$$u(W)=W-\frac{W^2}{2c},\qquad c=100,$$
dove $W$ è la ricchezza in euro. Poiché $u'(W)=1-W/c$ è positiva solo per $W<c$, la funzione si considera per $W<c$ e tutte le ricchezze finali delle domande stanno sotto $c$. Di una utilità $u$ si considerano l'avversione assoluta $A(W)=-u''(W)/u'(W)$, l'avversione relativa $RR(W)=W\,A(W)$ e la prudenza assoluta $P(W)=-u'''(W)/u''(W)$; $u$ è DARA (avversione assoluta decrescente) se $A'(W)\le 0$ per ogni $W$. Le lotterie $X$ hanno valore atteso nullo: con ricchezza iniziale certa $w$ la ricchezza finale è $w+X$, l'equivalente certo $CE$ è la ricchezza certa tale che $E[u(w+X)]=u(CE)$ (è una ricchezza, non un guadagno) e il premio per il rischio è $R=w-CE$.
:::::

::::: {.callout kind="question" heading="A.1"}
Calcola $A(W)$ e $RR(W)$, valide per ogni $W<100$. L'utilità ha avversione assoluta costante (CARA)? Ha avversione relativa costante (CRRA)? Rispondi sì o no a ciascuna delle due domande, nell'ordine, e motiva con le misure calcolate. *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.2"}
Una lotteria $X$ fa guadagnare 12 € o perdere 12 €, ciascuno con probabilità $1/2$. L'agente ha ricchezza iniziale $w_1=65$ €. Calcola, nell'ordine, l'equivalente certo $CE_1$ e il premio per il rischio $R_1$ di $X$. (Consiglio: scrivi $u(W)$ come una costante meno un quadrato.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.3"}
Ora l'agente ha ricchezza iniziale $w_2=84$ € e fronteggia la stessa lotteria $X$. Calcola, nell'ordine, il premio per il rischio $R_2$, la prudenza assoluta $P(W)$ e la derivata $A'(W)$, valide per ogni $W<100$. Il premio $R_2$ è maggiore di $R_1$? Rispondi sì o no e motiva con il teorema che lega il DARA all'andamento del premio con la ricchezza. *(5 punti)*
:::::

::::: {.callout kind="question" heading="A.4"}
Un agente avverso al rischio ha utilità $u$ concava e strettamente crescente. Perché il suo premio per il rischio $R$ è non negativo per ogni lotteria $X$ a valore atteso nullo, qualunque sia la ricchezza iniziale $w$? (Max 3 righe. Consiglio: ricorda la disuguaglianza di Jensen.) *(5 punti)*
:::::

# Domanda B (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un consumatore ha ricchezza iniziale $w=18$ € e utilità Bernoulliana $u(W)=\ln W$. Con probabilità $\pi$ subisce una perdita $L=10$ €. Le compagnie di assicurazione, neutrali al rischio e senza costi, vendono una polizza a copertura piena (paga $L$ in caso di perdita) a un prezzo $p$, dovuto in ogni caso: chi la compra ha ricchezza certa $w-p$. Le compagnie non osservano $\pi$, che varia da consumatore a consumatore ed è distribuita in modo uniforme su $[0{,}4;\,0{,}8]$; $w$, $L$ e $u$ sono uguali per tutti e, a parità di utilità, il consumatore compra. Si indica con $h(p)$ la probabilità di perdita sopra la quale un consumatore compra la polizza al prezzo $p$. In questa domanda $p$ è un prezzo, non una probabilità né una lotteria. Le domande B.1 e B.2 usano questi dati.
:::::

::::: {.callout kind="question" heading="B.1"}
Per $p=6$ € calcola $h(p)$: compra chi ha $\pi\ge h(p)$. Confrontala con $p/L$: fra chi compra ci sono anche consumatori la cui polizza equa, $\pi L$, costerebbe meno di $p$? (Sì o no.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.2"}
Tutte le compagnie offrono lo stesso prezzo e si congettura il prezzo $p^{**}=E[\pi]\,L$. Il profitto atteso per polizza venduta è $p-E[\pi\mid\text{acquirenti}]\,L$, e un prezzo è di equilibrio se questo profitto, calcolato sugli acquirenti effettivi, è nullo. Calcola, nell'ordine, $p^{**}$, la probabilità media di perdita fra gli acquirenti e il profitto atteso per polizza venduta a $p^{**}$. Il prezzo $p^{**}$ è di equilibrio? (Sì o no.) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda parte"}
Ora il mercato ha due tipi di consumatore, con la stessa utilità $u(W)=\ln W$ ma con ricchezza iniziale $w=27$ € e perdita $L=24$ €: il tipo a basso rischio ha probabilità di perdita $\pi_l=1/4$ e il tipo ad alto rischio $\pi_h=1/2$. Le compagnie conoscono la quota $\alpha$ di consumatori a basso rischio, ma non il tipo del singolo consumatore. Un contratto è una coppia $(B,p)$, dove $B\le L$ è l'indennizzo pagato in caso di perdita e $p$ è il premio, dovuto in ogni caso: un consumatore che sceglie $(B,p)$ ha ricchezza $w-p-L+B$ con probabilità pari alla sua probabilità di perdita e $w-p$ altrimenti. Un contratto dà alla compagnia il profitto atteso $p-\pi B$ se è scelto da un consumatore di probabilità $\pi$. In un equilibrio separante l'alto rischio sceglie un contratto $\psi_h^c$ a copertura piena e prezzo equo, e il basso rischio sceglie un contratto $\overline\psi_l$ a profitto atteso nullo che l'alto rischio non preferisce a $\psi_h^c$.
:::::

::::: {.callout kind="question" heading="B.3"}
Scrivi, nell'ordine, l'indennizzo e il premio del contratto $\psi_h^c$ e l'utilità $u_h^c$ che l'alto rischio ne ricava. Il contratto del basso rischio è $\overline\psi_l=(B,p)=(8;\,2)$: verifica che sta sulla retta di profitto nullo del tipo a basso rischio e che l'alto rischio, con $\overline\psi_l$, ottiene la stessa utilità $u_h^c$. *(5 punti)*
:::::

::::: {.callout kind="question" heading="B.4"}
Perché, se la quota $\alpha$ di consumatori a basso rischio è alta, l'equilibrio separante può non esistere? (Max 3 righe. Consiglio: cerca una deviazione profittevole per una compagnia.) *(5 punti)*
:::::

# Domanda C (20 punti)

::::: {.callout kind="abstract" heading="Dati"}
Un agente sceglie fra due lotterie sui premi 10 €, 50 € e 90 €. Una lotteria si indica con le probabilità dei tre premi, nell'ordine:
$$p=(1/8;\,6/8;\,1/8)\qquad\text{e}\qquad q=(3/8;\,1/8;\,4/8).$$
In questa domanda $p$ e $q$ sono lotterie, non prezzi né premi di una polizza.
:::::

::::: {.callout kind="question" heading="C.1"}
Un agente la cui utilità è soltanto crescente deve scegliere fra $p$ e $q$: la sua scelta è determinata senza ambiguità dai dati? Se sì, indica la lotteria che sceglie. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.2"}
La scelta è determinata senza ambiguità se l'agente ha utilità crescente e anche concava (è avverso al rischio)? Se sì, indica la lotteria che sceglie. Perché? (Max 2 righe) *(5 punti)*
:::::

::::: {.callout kind="abstract" heading="Dati della seconda coppia"}
Il rendimento in eccesso $\tilde x$ di un titolo rischioso (il suo rendimento netto meno quello del titolo privo di rischio) assume i valori $\{-60\%;\ 20\%;\ 60\%\}$. Due titoli hanno rendimenti in eccesso $\tilde x_1$ e $\tilde x_2$, con distribuzioni date dalle probabilità dei tre valori, nell'ordine ($F_i$ indica qui il vettore delle probabilità, non la funzione di ripartizione):
$$F_1=(3/8;\,1/8;\,4/8)\qquad\text{e}\qquad F_2=(1/4;\,1/2;\,1/4).$$
:::::

::::: {.callout kind="question" heading="C.3"}
Le due distribuzioni hanno la stessa media. Esibisci un rumore $\tilde\varepsilon$, con $E[\tilde\varepsilon\mid x_2]=0$ per ogni valore $x_2$ di $\tilde x_2$, tale che $\tilde x_2+\tilde\varepsilon$ abbia distribuzione $F_1$: cioè mostra che $F_1$ è un *mean-preserving spread* di $F_2$. (Max 2 righe, oppure una piccola tabella con i valori di $\tilde\varepsilon$ e le loro probabilità condizionate, per ciascun $x_2$.) *(5 punti)*
:::::

::::: {.callout kind="question" heading="C.4"}
Un investitore ha ricchezza iniziale $W=100$ €, utilità Bernoulliana $u(z)=\sqrt z$ della ricchezza finale $z$ e un titolo privo di rischio con rendimento netto $r=0$. Destina al titolo rischioso un ammontare $\alpha\in[0,W]$ (senza vendite allo scoperto) e ottiene la ricchezza finale $W+\alpha\tilde x$. Sia $\alpha_1^*$ l'ammontare ottimo se il titolo ha distribuzione $F_1$ e $\alpha_2^*$ quello se ha distribuzione $F_2$. Vale $\alpha_2^*\ge\alpha_1^*$? Perché? (Max 2 righe) *(5 punti)*
:::::

# Domanda D (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Nel modello di azzardo morale visto a lezione un assicurato con ricchezza iniziale $w$ può subire una perdita $l\in\{0,1,2\}$ (in migliaia di euro; $l=0$ vuol dire che non c'è sinistro) e sceglie l'impegno di prevenzione $e\in\{0,1\}$, con disutilità $d(e)$ e $d(1)>d(0)$. Dato $e$, la perdita $l$ ha probabilità $\pi_l(e)>0$. L'assicurato ha utilità Bernoulliana $u$ strettamente crescente e strettamente concava. Una polizza ha premio $p$, dovuto in ogni caso, e indennizzo $B_l$ se la perdita è $l$: la ricchezza finale è $z_l=w-p-l+B_l$ e l'utilità è $\sum_l\pi_l(e)\,u(z_l)-d(e)$. La compagnia è neutrale al rischio e ha profitto atteso $p-\sum_l\pi_l(e)\,B_l$; $\bar u$ è l'utilità di riserva dell'assicurato: nessuna polizza che gliene dia meno viene accettata, e $\bar u$ non è inferiore all'utilità che l'assicurato ha senza polizza. In questa domanda $p$ e $p(e)$ sono premi, non probabilità né lotterie. Dati (in migliaia di euro): $w=3$, $u(z)=-1/z$ per $z>0$ (quindi $u^{-1}(v)=-1/v$ per $v<0$), $\bar u=-0{,}5$, $d(0)=0$, $d(1)=0{,}1$ e

| | $l=0$ | $l=1$ | $l=2$ |
|---|---|---|---|
| $\pi_l(0)$ | 0,5 | 0,1 | 0,4 |
| $\pi_l(1)$ | 0,8 | 0,1 | 0,1 |

:::::

::::: {.callout kind="question" heading="D.1"}
Con impegno osservabile la polizza ottima per ogni $e$ ha copertura piena, $B_l=l$, e il vincolo di partecipazione vale con uguaglianza: $u(w-p(e))=d(e)+\bar u$. Mostra, per una qualunque $u$ strettamente crescente, che $p(0)>p(1)$. Poi, con i dati, calcola nell'ordine: $p(0)$ e $p(1)$; i profitti $\Pi^{FB}(e)=p(e)-\sum_l\pi_l(e)\,l$ per $e=0$ e $e=1$; l'impegno $e^*$ che la compagnia sceglie. *(6 punti)*
:::::

::::: {.callout kind="question" heading="D.2"}
Supponi ora che la compagnia non osservi $e$ e offra la polizza a copertura piena del caso $e=1$, cioè $B_l=l$ con premio $p(1)$. Quale impegno sceglie il cliente? Perché? La compagnia ottiene il profitto $\Pi^{FB}(1)$? (Max 3 righe) *(8 punti)*
:::::

::::: {.callout kind="question" heading="D.3"}
Alcune compagnie auto offrono uno sconto sul premio a chi accetta di installare una scatola nera, e alcune assicurazioni sanitarie a chi frequenta regolarmente una palestra. Perché uno sconto di questo tipo avvicina la polizza al benchmark con impegno osservabile? E perché solo in parte? (Max 3 righe) *(6 punti)*
:::::

# Domanda E (20 punti)

::::: {.callout kind="abstract" heading="Il modello"}
Un agente rappresentativo ha utilità Bernoulliana $u$ con $u'>0$ e $u''<0$. Parte con una quota di un titolo rischioso e sceglie la quota $\alpha$ da tenere, senza vincoli: con $\alpha<1$ vende quote, con $\alpha>1$ ne compra prendendo a prestito, con $\alpha<0$ vende allo scoperto. Oggi il titolo vale $P$ e domani $\tilde y$ (non paga dividendi); il titolo privo di rischio ha rendimento lordo $R_f$ (un euro oggi ne rende $R_f$ domani) ed è in offerta netta nulla. In questa domanda $P$ è il prezzo del titolo (non la prudenza) e $R=E[\tilde y]/P$ è il suo rendimento lordo atteso (non un premio per il rischio). Il mercato del titolo è in equilibrio se l'agente vuole tenere esattamente le quote in offerta.
:::::

::::: {.callout kind="question" heading="E.1"}
Scrivi la funzione obiettivo $V(\alpha)$ dell'agente e la sua condizione del primo ordine. Mostra poi che $V'(0)=u'(R_fP)\,P\,(R-R_f)$ e spiega perché la condizione del primo ordine è anche sufficiente per l'ottimo. *(8 punti)*
:::::

::::: {.callout kind="abstract" heading="Il modello con più titoli"}
Ora l'agente rappresentativo può scegliere fra $n$ titoli rischiosi, ciascuno con quota totale pari a 1, prezzi $P_i>0$ e valori domani $\tilde y_i$ ($i=1,\dots,n$; nessun dividendo). Il valore del portafoglio di mercato è $\tilde y=\sum_i\tilde y_i$. L'agente parte con una quota di ciascun titolo e sceglie le quote $\alpha_i$ da tenere, senza vincoli: vendendo le quote $1-\alpha_i$ ricava $(1-\alpha_i)P_i$, che investe al rendimento lordo $R_f$. Il rendimento lordo del titolo $i$ è $\tilde R_i=\tilde y_i/P_i$ (non un premio per il rischio) e il pricing kernel è $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$. In equilibrio l'agente tiene tutte le quote di tutti i titoli, $\alpha_i=1$ per ogni $i$.
:::::

::::: {.callout kind="question" heading="E.2"}
Dimostra che, in equilibrio, per ogni titolo $i$ valgono: (a) $R_f=E[\tilde R_i\tilde M]$, a partire dalla condizione del primo ordine in $\alpha_i$; (b) $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$; (c) per un titolo il cui valore $\tilde y_i$ è indipendente dal valore $\tilde y$ del portafoglio di mercato, di cui il titolo $i$ fa parte, il premio $E[\tilde R_i]-R_f$ è nullo. (Consiglio: ricorda che $E[\tilde M]=1$ e che $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$.) *(12 punti)*
:::::
