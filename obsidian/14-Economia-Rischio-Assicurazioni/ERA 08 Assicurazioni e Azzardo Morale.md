---
title: "Assicurazioni e azzardo morale: polizza ottima con impegno osservabile e non osservabile"
tags:
  - corso/economia-rischio-assicurazioni
  - tipo/lezione
corso: "[[Economia del Rischio e delle Assicurazioni]]"
source: "ERA_Slide_07_Assicurazioni-e-Azzardo-Morale.pdf"
text_layer: true
verified: true
generated: 2026-11-22
---

## Oggetto del capitolo

Il capitolo studia l'azzardo morale (*moral hazard*) nel mercato assicurativo, cioè la situazione in cui la compagnia non osserva un'azione dell'assicurato che modifica la probabilità del sinistro. Si colloca dopo il capitolo su [[ERA 07 Assicurazioni e Asimmetrie Informative|assicurazioni e asimmetrie informative]], dove l'informazione nascosta riguardava il tipo del consumatore e la conseguenza era la selezione avversa. Qui la compagnia conosce il consumatore, ma non osserva l'impegno che questi mette nell'evitare l'incidente: è il caso dell'azione nascosta. Dal capitolo precedente il modello riprende la neutralità al rischio delle compagnie, la Pareto efficienza e i termini *first best* e *second best*; dal capitolo sull'[[ERA 03 Avversione al Rischio|avversione al rischio]] l'equivalenza fra avversione al rischio e concavità di $u$; dal [[ERA 01 Ripasso|ripasso di matematica]] il teorema di Kuhn-Tucker, di cui si richiamano soltanto le condizioni che servono.

Il percorso ha tre passi. Il primo definisce l'azzardo morale e costruisce il modello: una compagnia, un cliente, perdite di diverso importo e un impegno che può essere basso o alto. Il secondo risolve il benchmark con informazione simmetrica, in cui la compagnia osserva l'impegno e offre la copertura piena. Il terzo toglie l'osservabilità e aggiunge al problema un vincolo di compatibilità degli incentivi. La polizza che induce l'impegno basso resta quella del benchmark. Quella che induce l'impegno alto non copre per intero nessuna perdita positiva, e, quando la compagnia la sceglie, l'allocazione non è Pareto efficiente.

## Notazione

Il capitolo usa alcuni simboli dei capitoli precedenti con un significato diverso, che si dichiara qui. $L$ è la perdita massima, mentre nel [[ERA 07 Assicurazioni e Asimmetrie Informative|capitolo sulle asimmetrie informative]] è l'unica perdita possibile; $l\in\{0,1,\dots,L\}$ è il livello di perdita, e $l=0$ indica l'assenza di incidente. In quel capitolo il pedice $l$ indicava invece il tipo a basso rischio ($\overline B_l$, $\overline p_l$, $u_l$): qui quel tipo non compare, e $B_l$ è l'indennizzo per la perdita $l$. $\bar u$ è l'utilità di riserva del consumatore, non il livello di una curva di indifferenza. $\lambda$ è il moltiplicatore del vincolo di partecipazione, non il parametro dell'utilità CARA del capitolo sull'[[ERA 03 Avversione al Rischio|avversione al rischio]]; $\beta$ è il moltiplicatore del vincolo di compatibilità degli incentivi. La lettera $e$ indica l'impegno e mai la base dei logaritmi naturali.

Restano con lo stesso significato $w$ (ricchezza iniziale certa), $p$ (prezzo, o premio, della polizza), $B$ (indennizzo, qui uno per ogni livello di perdita), $\pi$ (sempre una probabilità, qui $\pi_l(e)$) e $u$ (funzione di utilità di Bernoulli). Per non riscrivere ogni volta l'espressione per esteso si pone
$$z_l:=w-p-l+B_l,$$
la ricchezza finale del consumatore quando la perdita è $l$ e la polizza ha premio $p$ e indennizzo $B_l$.

## L'azzardo morale

Le compagnie di assicurazione non sono ingenue. Sanno che chi ha comprato una polizza auto può guidare con meno prudenza di prima, perché una parte del costo dell'incidente passa alla compagnia. L'incentivo a guidare con prudenza diminuisce al crescere della copertura: con la copertura piena l'assicurato non ricava alcun vantaggio economico dall'evitare l'incidente, mentre la prudenza gli costa attenzione e fatica.

Nella situazione descritta la compagnia è il principale (*principal*) e l'assicurato è l'agente (*agent*).

> [!abstract] Definizione
> Si ha **azzardo morale** (*moral hazard*) quando (i) un principale ha un interesse riguardo all'azione compiuta da un agente e (ii) il principale non può osservare quell'azione.

Nel caso assicurativo l'azione è l'impegno a una guida sicura, che l'assicurato sceglie dopo la stipula del contratto. Nella selezione avversa l'informazione che la compagnia non ha riguarda invece una caratteristica del cliente già presente alla stipula. Il problema principale-agente (*principal-agent problem*) consiste, per il principale, nel progettare uno schema di incentivi che porti l'agente a compiere l'azione appropriata. Il caso assicurativo è quello che il capitolo sulle asimmetrie informative chiama azione nascosta (*hidden action*), e l'azzardo morale ne è la conseguenza tipica.

## Il modello

### Perdite, impegno e probabilità

Si considera una sola compagnia di assicurazione e un solo potenziale cliente. Il cliente può subire una perdita $l\in\{0,1,\dots,L\}$, misurata in unità monetarie: $l=0$ è l'assenza di incidente e $L\ge1$ è la perdita massima. La compagnia osserva la perdita realizzata, per cui l'indennizzo può dipendere da $l$. Non osserva invece l'impegno del cliente, e l'indennizzo non può dipendere da esso.

L'impegno a una guida sicura si indica con $e$ e si semplifica a due livelli, $e\in\{0,1\}$: $e=0$ è l'impegno basso e $e=1$ quello alto. La probabilità della perdita $l$ dato l'impegno $e$ è $\pi_l(e)$, con
$$\sum_{l=0}^L\pi_l(e)=1\qquad\text{per ogni }e\in\{0,1\}.$$
Si assume $\pi_l(e)>0$ per ogni $l$ e per ogni $e$. Le due distribuzioni hanno lo stesso supporto: nessuna perdita rivela con certezza l'impegno, e il rapporto fra le due probabilità della stessa perdita, che serve nel passo seguente, è sempre definito.

### La proprietà del rapporto di verosimiglianza monotono

L'idea è che un impegno maggiore renda meno probabili le perdite grandi. La si formalizza con una condizione sul rapporto fra le probabilità di una stessa perdita nei due livelli di impegno.

> [!abstract] Definizione
> Le distribuzioni delle perdite $\pi(0)$ e $\pi(1)$ hanno la proprietà del **rapporto di verosimiglianza monotono** (MLR, *monotone likelihood ratio*) se il rapporto
>
> $$r_l:=\frac{\pi_l(0)}{\pi_l(1)}$$
>
> è strettamente crescente in $l\in\{0,1,\dots,L\}$.

Il significato si legge con la regola di Bayes. Si attribuiscano a priori ai due livelli di impegno le probabilità $\mathbb P(e=0)>0$ e $\mathbb P(e=1)>0$. La probabilità a posteriori dell'impegno $e$ dopo aver osservato la perdita $l$ è $\mathbb P(e\mid l)=\pi_l(e)\,\mathbb P(e)/\mathbb P(l)$, dove il denominatore non dipende da $e$. Il rapporto fra le due probabilità a posteriori è quindi
$$\frac{\mathbb P(e=0\mid l)}{\mathbb P(e=1\mid l)}=\frac{\pi_l(0)}{\pi_l(1)}\cdot\frac{\mathbb P(e=0)}{\mathbb P(e=1)}.$$
Il secondo fattore non dipende da $l$. Il rapporto fra le probabilità a posteriori cresce con $l$ qualunque sia l'opinione di partenza, purché dia probabilità positiva a entrambi i livelli: più la perdita osservata è grande, più è probabile che derivi da scarso impegno. Si usa la versione stretta della crescita. Esclude il caso in cui il rapporto è costante in $l$: poiché le probabilità sommano a 1 in entrambi i casi, la costante sarebbe 1 e l'impegno non cambierebbe la distribuzione delle perdite. Serve inoltre al risultato sulla copertura parziale: due perdite con lo stesso rapporto riceverebbero la stessa ricchezza finale nella polizza ottima che induce l'impegno alto, e con $r_1=r_0$ la perdita 1 sarebbe coperta per intero.

Dalla proprietà MLR discendono due fatti che il capitolo usa più volte.

> [!tip] Teorema
> Sia $L\ge1$ e valga la proprietà MLR. Allora:
>
> (a) $r_0<1<r_L$. In particolare esistono un livello di perdita $l'$ con $\pi_{l'}(0)>\pi_{l'}(1)$ e un livello $l''$ con $\pi_{l''}(0)<\pi_{l''}(1)$.
>
> (b) Per ogni successione strettamente crescente $x_0<x_1<\dots<x_L$,
>
> $$\sum_{l=0}^L\pi_l(0)\,x_l\ >\ \sum_{l=0}^L\pi_l(1)\,x_l.$$
>
> In particolare, con $x_l=l$, la perdita attesa con l'impegno basso supera quella con l'impegno alto.

> [!note] Dimostrazione
> (a) Poiché $\sum_l\pi_l(0)=\sum_l\pi_l(1)=1$, si ha $\sum_l\pi_l(1)\,r_l=\sum_l\pi_l(0)=1$, quindi
>
> $$\sum_{l=0}^L\pi_l(1)\,(r_l-1)=0.$$
>
> I pesi $\pi_l(1)$ sono positivi. Se fosse $r_0\ge1$, per la stretta crescita sarebbe $r_l>1$ per ogni $l\ge1$, e la somma sarebbe strettamente positiva perché esiste almeno un $l\ge1$. Se fosse $r_L\le1$, sarebbe $r_l<1$ per ogni $l<L$ e la somma sarebbe strettamente negativa. Entrambe le ipotesi contraddicono la somma nulla, quindi $r_0<1<r_L$. Si può prendere $l'=L$ e $l''=0$.
>
> (b) Sia $j$ il più grande $l$ con $r_l\le1$. Per (a) vale $0\le j<L$. Poiché $\pi_l(0)=\pi_l(1)\,r_l$,
>
> $$\sum_l\pi_l(0)\,x_l-\sum_l\pi_l(1)\,x_l=\sum_l\pi_l(1)\,(r_l-1)\,x_l=\sum_l\pi_l(1)\,(r_l-1)\,(x_l-x_j),$$
>
> dove l'ultima uguaglianza sottrae $x_j\sum_l\pi_l(1)(r_l-1)=0$. Per $l\le j$ i fattori $r_l-1$ e $x_l-x_j$ sono entrambi non positivi, per $l>j$ sono entrambi positivi. Ogni addendo è non negativo, e quello con $l=L$ è strettamente positivo perché $L>j$. La somma è positiva.

Il punto (b) si collega a un fatto più generale, espresso con la dominanza del primo ordine definita nel capitolo sul [[ERA 04 Confronto di Opzioni Rischiose|confronto di opzioni rischiose]]: con la proprietà MLR la ricchezza $w-l$ con l'impegno alto domina al primo ordine quella con l'impegno basso, cioè la perdita è stocasticamente più grande con l'impegno basso.

### Consumatore e compagnia

Il consumatore ha una funzione di utilità di Bernoulli $u$ strettamente crescente e strettamente concava, cioè è strettamente avverso al rischio, come nel capitolo sulle asimmetrie informative. La stretta concavità rende $u'$ strettamente decrescente, e una funzione strettamente decrescente è iniettiva: ciò permette di concludere $z=z'$ da un'uguaglianza $u'(z)=u'(z')$, e le dimostrazioni seguenti lo usano più volte. La ricchezza iniziale è $w>L$, in modo che la ricchezza resti positiva anche con la perdita massima e senza assicurazione.

L'impegno costa al consumatore una disutilità $d(e)$, con $d(1)>d(0)$: guidare con prudenza è faticoso. Le preferenze sono additive: con l'impegno $e$ e la ricchezza finale $z$ l'utilità è $u(z)-d(e)$. Una polizza è un vettore $(p,B_0,B_1,\dots,B_L)$, dove $p$ è il premio, pagato in ogni caso, e $B_l$ è l'indennizzo se la perdita è $l$. Con questa polizza e l'impegno $e$ l'utilità attesa del consumatore è
$$\sum_{l=0}^L\pi_l(e)\,u(w-p-l+B_l)-d(e)=\sum_{l=0}^L\pi_l(e)\,u(z_l)-d(e).$$

La compagnia è neutrale al rischio e massimizza il profitto atteso. Incassa $p$ e paga $B_l$ con probabilità $\pi_l(e)$, per cui il profitto atteso è
$$p-\sum_{l=0}^L\pi_l(e)\,B_l.$$
A differenza del capitolo precedente, la compagnia è una sola e non c'è una concorrenza che azzeri il profitto: sceglie la polizza che massimizza il profitto fra quelle che il cliente accetta. Il cliente accetta una polizza solo se gli dà almeno la sua utilità di riserva $\bar u$, cioè l'utilità che ottiene non acquistando. Poiché può sempre non comprare, vale $\bar u\ge\max_{e\in\{0,1\}}\{\sum_l\pi_l(e)\,u(w-l)-d(e)\}$, l'utilità senza assicurazione con l'impegno migliore. Se non ci sono altre offerte vale l'uguaglianza; $\bar u$ può essere maggiore se altre compagnie offrono polizze che il cliente preferisce.

### Le domande del modello

Il modello risponde a due domande: che tipo di polizza viene offerta al consumatore, e se l'allocazione che ne risulta è efficiente. Le risposte si danno prima nel caso in cui la compagnia osserva l'impegno, che fa da benchmark, poi nel caso in cui non lo osserva.

## Il benchmark: informazione simmetrica

### Il problema della compagnia

Il benchmark è l'allocazione che la compagnia otterrebbe se l'impegno fosse osservabile: il confronto con il caso in cui non lo è misura quanto costa l'asimmetria informativa. Si supponga che la compagnia osservi il livello di impegno $e$. È lo stesso benchmark che il capitolo sulle asimmetrie informative chiama informazione perfetta. La compagnia può allora offrire una polizza che versa l'indennizzo solo se è stato profuso un certo impegno: poiché può verificare il rispetto della clausola, il cliente che vuole l'indennizzo si attiene all'impegno richiesto, e in pratica la compagnia sceglie l'impegno del cliente. Il suo problema è
$$\max_{e,\,p,\,B_0,\dots,B_L}\ p-\sum_{l=0}^L\pi_l(e)\,B_l\qquad\text{sotto}\qquad \sum_{l=0}^L\pi_l(e)\,u(w-p-l+B_l)-d(e)\ \ge\ \bar u.$$
Il vincolo è il **vincolo di partecipazione** (PC, *participation constraint*): il cliente accetta la polizza solo se ne ricava almeno l'utilità di riserva $\bar u$.

Si procede in due tempi. Si fissa $e$ e si cerca la polizza ottima per quell'impegno; poi si confrontano i profitti ottenuti con $e=0$ e con $e=1$.

### La polizza ottima per un impegno fissato

Il problema con $e$ fissato è un problema di massimo con un vincolo. Per il teorema di Kuhn-Tucker, se si scrive il vincolo come $g\ge0$ la Lagrangiana è $\mathcal L=f+\lambda g$, e in un punto di ottimo si annullano le derivate di $\mathcal L$ rispetto alle variabili di scelta e valgono
$$\lambda\ge0,\qquad g\ge0,\qquad \lambda\,g=0.$$
L'ultima è la condizione di complementarità: se il vincolo è lasco, $g>0$, il moltiplicatore è nullo; se il moltiplicatore è positivo, il vincolo vale con uguaglianza. Si assume che nel punto di ottimo valgano le condizioni di qualificazione dei vincoli, così che queste condizioni siano necessarie. Con più vincoli si ha un moltiplicatore per ciascuno. Lo stesso problema si può scrivere con il vincolo nella forma $h:=-g\le0$ e il termine $-\lambda h$ nella Lagrangiana: la Lagrangiana è la stessa, e cambia solo il modo di scrivere la condizione sul vincolo, $h\le0$.

Qui $f=p-\sum_l\pi_l(e)B_l$ e $g=\sum_l\pi_l(e)u(z_l)-d(e)-\bar u$, per cui
$$\mathcal L=p-\sum_{l=0}^L\pi_l(e)\,B_l+\lambda\Big[\sum_{l=0}^L\pi_l(e)\,u(w-p-l+B_l)-d(e)-\bar u\Big].$$
Per la regola della catena $u(z_l)$ ha derivata $-u'(z_l)$ rispetto a $p$, perché $\partial z_l/\partial p=-1$, e $u'(z_l)$ rispetto a $B_l$, perché $\partial z_l/\partial B_l=1$. Nelle due somme che compongono $\mathcal L$ contiene $B_l$ solo l'addendo di indice $l$, perché gli altri contengono $B_k$ con $k\neq l$. Le condizioni del primo ordine sono
$$\frac{\partial\mathcal L}{\partial p}=1-\lambda\sum_{l=0}^L\pi_l(e)\,u'(z_l)=0,\tag{1}$$
$$\frac{\partial\mathcal L}{\partial B_l}=-\pi_l(e)+\lambda\,\pi_l(e)\,u'(z_l)=0\qquad l=0,1,\dots,L,\tag{2}$$
e, per il vincolo, $\lambda\ge0$, $g\ge0$, $\lambda g=0$.

La condizione (1) è ridondante: è implicata dalle $L+1$ condizioni (2). Sommando le (2) su $l$ e ricordando che $\sum_l\pi_l(e)=1$ si ottiene $-1+\lambda\sum_l\pi_l(e)\,u'(z_l)$, che è l'opposto del primo membro di (1). Se le (2) valgono, vale anche (1).

> [!tip] Teorema
> Con informazione simmetrica e impegno $e$ fissato, la polizza ottima ha copertura piena (*full insurance*): $B_l=l$ per ogni $l$, con la normalizzazione $B_0=0$. Il premio $p(e)$ è definito da
>
> $$u\big(w-p(e)\big)=d(e)+\bar u,\qquad\text{cioè}\qquad p(e)=w-u^{-1}\big(d(e)+\bar u\big),$$
>
> e il vincolo di partecipazione vale con uguaglianza.

> [!note] Dimostrazione
> *Ipotesi.* La funzione $u$ è strettamente crescente e strettamente concava, $\pi_l(e)>0$ per ogni $l$, e nel punto di ottimo valgono le condizioni di Kuhn-Tucker.
>
> *Passo 1: $\lambda>0$ e la ricchezza finale è la stessa in ogni stato.* Dividendo la (2) per $\pi_l(e)>0$ si ottiene
>
> $$\lambda\,u'(z_l)=1\qquad\text{per ogni }l.$$
>
> Poiché $u'(z_l)>0$ è finita, $\lambda\neq0$, e poiché $\lambda\ge0$ vale $\lambda>0$. Allora $u'(z_l)=1/\lambda$ per ogni $l$. La funzione $u'$ è iniettiva perché $u$ è strettamente concava, quindi $z_l$ è lo stesso per ogni $l$: la differenza $-l+B_l$ è costante in $l$.
>
> *Passo 2: il vincolo vale con uguaglianza.* Poiché $\lambda>0$, la complementarità $\lambda g=0$ impone $g=0$. Sia $z$ il valore comune di $z_l$. Poiché $\sum_l\pi_l(e)=1$, il vincolo diventa $u(z)-d(e)=\bar u$, cioè $u(z)=d(e)+\bar u$.
>
> *Passo 3: normalizzazione.* Le incognite sono $p,B_0,\dots,B_L,\lambda$, in numero di $L+3$. Le equazioni indipendenti sono le $L+1$ condizioni (2) e l'uguaglianza del vincolo, cioè $L+2$; la (1) è ridondante. Resta un grado di libertà, che corrisponde a una trasformazione che non cambia nulla: per ogni costante $c$, la sostituzione $(p,B_l)\mapsto(p+c,B_l+c)$ lascia invariata la ricchezza finale $z_l$, e con essa l'utilità, e lascia invariato il profitto, perché
>
> $$(p+c)-\sum_l\pi_l(e)\,(B_l+c)=p-\sum_l\pi_l(e)\,B_l\qquad\text{essendo }\textstyle\sum_l\pi_l(e)=1.$$
>
> Si può porre $B_0=0$ senza perdita di generalità: il cliente non riceve nulla se non c'è incidente.
>
> *Passo 4: la soluzione.* Con $B_0=0$ la costanza di $-l+B_l$ dà $B_l-l=B_0-0=0$, cioè $B_l=l$ per ogni $l$. Per $l=0$ si ha $z_0=w-p$, quindi $u(w-p)=d(e)+\bar u$.
>
> *Passo 5: è un massimo.* La polizza trovata soddisfa le condizioni di Kuhn-Tucker con $\lambda=1/u'(w-p(e))>0$. L'obiettivo $f$ è lineare in $(p,B_0,\dots,B_L)$ e il vincolo $g$ è concavo, perché $u$ è concava, ogni $z_l$ è una funzione affine di $(p,B_l)$ e i pesi $\pi_l(e)$ sono positivi. Per il teorema sulle condizioni sufficienti del [[ERA 01 Ripasso|ripasso di matematica]] la polizza è un massimo globale; per i passi 1-3 ogni altro massimo differisce da essa soltanto per la traslazione $(p,B_l)\mapsto(p+c,B_l+c)$.

Con $B_l=l$ la ricchezza finale è $w-p(e)$ in ogni stato: il consumatore non è esposto ad alcun rischio. Il risultato è la condivisione efficiente del rischio fra un consumatore strettamente avverso al rischio e una compagnia neutrale: tutto il rischio passa a chi è neutrale. Il premio è fissato in modo da lasciare al cliente soltanto l'utilità di riserva.

La stretta concavità di $u$ è essenziale per questo risultato. Se $u$ fosse lineare, $u'$ sarebbe costante e la (2) darebbe soltanto $\lambda u'=1$, senza alcun vincolo sui $z_l$: ogni polizza che rispetta il vincolo di partecipazione con l'uguaglianza darebbe lo stesso profitto, e la copertura piena sarebbe una soluzione fra infinite. Un consumatore neutrale al rischio è indifferente a chi sopporta il rischio; uno strettamente avverso non lo è.

### La scelta dell'impegno

Con la polizza a copertura piena il profitto della compagnia è $p(e)-\sum_l\pi_l(e)\,l$, perché $B_l=l$. Lo si indica con $\Pi^{FB}(e)$, dove $FB$ sta per *first best*, il nome dell'allocazione ottenuta con informazione simmetrica. L'impegno che la compagnia desidera, indicato con $e^*$, massimizza questo profitto:
$$\max_{e\in\{0,1\}}\ \Pi^{FB}(e)=p(e)-\sum_{l=0}^L\pi_l(e)\,l.$$
Si assume che il massimo sia raggiunto in un solo livello di impegno, che è $e^*$.

La scelta mette in gioco due effetti opposti, come mostra la differenza fra i profitti dei due livelli:
$$\Pi^{FB}(0)-\Pi^{FB}(1)=\big[p(0)-p(1)\big]-\Big[\sum_l\pi_l(0)\,l-\sum_l\pi_l(1)\,l\Big].$$
Il primo effetto riguarda il premio: vale $p(0)>p(1)$. Infatti da $u(w-p(e))=d(e)+\bar u$ e da $d(1)>d(0)$ segue $u(w-p(1))>u(w-p(0))$, e poiché $u$ è crescente $w-p(1)>w-p(0)$, cioè $p(1)<p(0)$. Un cliente che deve sostenere un impegno più costoso, a parità di ricchezza certa, è disposto a pagare un premio più basso. Il secondo effetto riguarda la perdita attesa: per il punto (b) del teorema sulla proprietà MLR con $x_l=l$, la perdita attesa è minore con $e=1$ che con $e=0$, e la seconda parentesi è positiva. Con $e=0$ la compagnia incassa di più ma paga di più. Quale dei due effetti prevalga dipende da $u$, da $\pi_l(\cdot)$ per ogni $l$, da $d(\cdot)$ e da $\bar u$.

### Efficienza del benchmark

Un'allocazione è qui una polizza con l'impegno, $(e,p,B_0,\dots,B_L)$. Dà al cliente l'utilità $U=\sum_l\pi_l(e)\,u(z_l)-d(e)$ e alla compagnia il profitto $\Pi=p-\sum_l\pi_l(e)B_l$. L'allocazione è Pareto efficiente se, fra le allocazioni fattibili quando l'impegno è osservabile, nessuna dà a uno dei due almeno quanto ha e all'altro strettamente di più.

> [!tip] Teorema
> Con informazione simmetrica l'allocazione che la compagnia sceglie, cioè la polizza a copertura piena con l'impegno $e^*$, è Pareto efficiente.

> [!note] Dimostrazione
> Per ogni livello $v$ di utilità richiesto al cliente, sia $\Pi^*(v)$ il massimo profitto che la compagnia ottiene sotto il vincolo $\sum_l\pi_l(e)\,u(z_l)-d(e)\ge v$. Per il teorema sulla polizza ottima, applicato con $v$ al posto di $\bar u$, per ogni $e$ il massimo è $p(e;v)-\sum_l\pi_l(e)\,l$ con $p(e;v)=w-u^{-1}(d(e)+v)$, strettamente decrescente in $v$ perché $u^{-1}$ è strettamente crescente. Il massimo su $e\in\{0,1\}$ di due funzioni strettamente decrescenti è strettamente decrescente: $\Pi^*(v)$ è strettamente decrescente in $v$. L'allocazione scelta dalla compagnia dà $U=\bar u$ e $\Pi=\Pi^*(\bar u)$.
>
> Si supponga che esista un'allocazione fattibile con utilità $\hat U\ge\bar u$ e profitto $\hat\Pi\ge\Pi^*(\bar u)$, con almeno una delle due disuguaglianze stretta. Questa allocazione è fattibile nel problema con utilità richiesta $v=\hat U$, per cui $\hat\Pi\le\Pi^*(\hat U)\le\Pi^*(\bar u)$. Se $\hat U>\bar u$ l'ultima disuguaglianza è stretta e contraddice $\hat\Pi\ge\Pi^*(\bar u)$. Se $\hat U=\bar u$ deve essere $\hat\Pi>\Pi^*(\bar u)$, che contraddice la definizione di massimo. Nessun miglioramento paretiano esiste.

## Informazione asimmetrica

Si supponga ora che la compagnia non osservi $e$. La compagnia vuole proporre una polizza associata a un certo livello di impegno del cliente, ma non può imporlo: deve fare in modo che la polizza stessa induca il cliente a scegliere volontariamente l'impegno desiderato. La polizza deve soddisfare due requisiti. Il primo è il vincolo di partecipazione: dare al cliente un'utilità almeno pari a $\bar u$, altrimenti il cliente preferisce non comprare. Il secondo è il **vincolo di compatibilità degli incentivi** (IC, *incentive compatibility constraint*): fra i due livelli di impegno, quello che il cliente sceglie, una volta ottenuta la polizza, deve essere quello che la compagnia desidera. Se il cliente è indifferente, si assume che scelga l'impegno desiderato dalla compagnia.

Il problema della compagnia diventa
$$\max_{e,\,p,\,B_0,\dots,B_L}\ p-\sum_{l=0}^L\pi_l(e)\,B_l$$
sotto i vincoli
$$\text{(PC)}\qquad\sum_{l=0}^L\pi_l(e)\,u(z_l)-d(e)\ \ge\ \bar u,$$
$$\text{(IC)}\qquad\sum_{l=0}^L\pi_l(e)\,u(z_l)-d(e)\ \ge\ \sum_{l=0}^L\pi_l(e')\,u(z_l)-d(e')\qquad e,e'\in\{0,1\},\ e'\neq e.$$
Gli indennizzi possono dipendere dalla perdita ma non da $e$, che la compagnia non osserva. Nell'obiettivo compare il premio $p$, variabile di scelta insieme ai $B_l$, e non il premio $p(e)$ del benchmark, che era il valore ottimo di $p$ con copertura piena. Anche $e$ è una variabile di scelta della compagnia, benché sia il cliente a scegliere l'impegno: la compagnia decide quale impegno indurre, il vincolo IC fa sì che il cliente scelga proprio quell'$e$, ed $e$ entra nel profitto attraverso le probabilità $\pi_l(e)$.

La strategia di soluzione è quella del benchmark: si fissa $e$, si trova la polizza ottima fra quelle che inducono $e$ e poi si confrontano i profitti ottenuti per $e=0$ e per $e=1$.

## La polizza ottima per l'impegno basso

> [!tip] Teorema
> Se la compagnia vuole indurre l'impegno basso, la polizza ottima con informazione asimmetrica è la stessa del benchmark: $B_l=l$ per ogni $l$, con la normalizzazione $B_0=0$, e il premio $p$ è definito da $u(w-p)=d(0)+\bar u$.

> [!note] Dimostrazione
> Si consideri il problema con $e=0$ senza il vincolo IC. È il problema del benchmark, la cui soluzione è la polizza a copertura piena con $u(w-p)=d(0)+\bar u$. Si verifica che questa polizza soddisfa IC. Con $B_l=l$ la ricchezza finale è $w-p$ in ogni stato, e poiché $\sum_l\pi_l(0)=\sum_l\pi_l(1)=1$, il vincolo IC con $e=0$ diventa
>
> $$\sum_l\pi_l(0)\,u(w-p)-d(0)\ \ge\ \sum_l\pi_l(1)\,u(w-p)-d(1)\qquad\Longleftrightarrow\qquad u(w-p)-d(0)\ \ge\ u(w-p)-d(1),$$
>
> cioè $d(0)\le d(1)$, che è vera perché l'impegno è faticoso. Aggiungere un vincolo a un problema di massimo non può far aumentare il massimo. La soluzione del problema senza IC soddisfa IC, quindi è ottima anche nel problema con IC.

Con la copertura piena il cliente ha la stessa ricchezza in ogni stato, e l'impegno non migliora in alcun modo la sua sorte. Poiché l'impegno è costoso, sceglie volontariamente quello basso: la compagnia ottiene l'impegno che desidera senza dover dare incentivi.

## La polizza ottima per l'impegno alto

### Lagrangiana e condizioni del primo ordine

Con $e=1$ la polizza del benchmark non basta. Con la copertura piena il cliente, che ha la stessa ricchezza in ogni stato, sceglierebbe l'impegno basso perché $d(0)<d(1)$. La compagnia deve imporre il vincolo IC. Poiché $e=1$ e ci sono solo due livelli di impegno, IC contiene una sola deviazione possibile, $e'=0$. I due vincoli, scritti nella forma $g\ge0$, sono
$$g_{PC}:=\sum_{l=0}^L\pi_l(1)\,u(z_l)-d(1)-\bar u\ \ge\ 0,$$
$$g_{IC}:=\sum_{l=0}^L\pi_l(1)\,u(z_l)-d(1)-\Big[\sum_{l=0}^L\pi_l(0)\,u(z_l)-d(0)\Big]\ \ge\ 0.$$
Il moltiplicatore di PC è $\lambda$, quello di IC è $\beta$. La Lagrangiana è
$$\mathcal L=p-\sum_{l=0}^L\pi_l(1)\,B_l+\lambda\Big[\sum_{l=0}^L\pi_l(1)\,u(z_l)-d(1)-\bar u\Big]+\beta\Big[\sum_{l=0}^L\pi_l(1)\,u(z_l)-d(1)-\sum_{l=0}^L\pi_l(0)\,u(z_l)+d(0)\Big].$$
Le condizioni del primo ordine, con la regola della catena usata come nel benchmark, sono
$$\frac{\partial\mathcal L}{\partial p}=1-\lambda\sum_{l=0}^L\pi_l(1)\,u'(z_l)-\beta\sum_{l=0}^L\big[\pi_l(1)-\pi_l(0)\big]u'(z_l)=0,\tag{3}$$
$$\frac{\partial\mathcal L}{\partial B_l}=-\pi_l(1)+\lambda\,\pi_l(1)\,u'(z_l)+\beta\,\big[\pi_l(1)-\pi_l(0)\big]u'(z_l)=0\qquad l=0,1,\dots,L,\tag{4}$$
con $\lambda\ge0$, $g_{PC}\ge0$, $\lambda g_{PC}=0$ e $\beta\ge0$, $g_{IC}\ge0$, $\beta g_{IC}=0$.

Come nel benchmark, la (3) è ridondante: la somma delle (4) su $l$ è $-1+\lambda\sum_l\pi_l(1)u'(z_l)+\beta\sum_l[\pi_l(1)-\pi_l(0)]u'(z_l)$, l'opposto del primo membro della (3). Anche la normalizzazione $B_0=0$ resta lecita: la sostituzione $(p,B_l)\mapsto(p+c,B_l+c)$ lascia invariati $z_l$ e il profitto, e con essi PC e IC, che dipendono dalla polizza solo attraverso i $z_l$. Lo stesso risultato si ottiene contando le equazioni: le incognite sono $p,B_0,\dots,B_L,\lambda,\beta$, cioè $L+4$, e con i due vincoli attivi, come mostra il teorema seguente, le equazioni indipendenti sono le $L+1$ condizioni (4) e le due uguaglianze dei vincoli, cioè $L+3$.

Dividendo la (4) per $\pi_l(1)\,u'(z_l)>0$ si ottiene
$$-\frac1{u'(z_l)}+\lambda+\beta\Big[1-\frac{\pi_l(0)}{\pi_l(1)}\Big]=0,$$
cioè la condizione su cui si basa tutta l'analisi:
$$\frac1{u'(z_l)}=\lambda+\beta\Big[1-\frac{\pi_l(0)}{\pi_l(1)}\Big]=\lambda+\beta\,(1-r_l)\qquad l=0,1,\dots,L.\tag{5}$$
Se $\beta=0$ resta $1/u'(z_l)=\lambda$, la condizione di condivisione del rischio del benchmark: la derivata $u'(z_l)$ è la stessa in ogni stato. Il termine con $\beta$ è la correzione che il vincolo IC impone, e dipende da $l$ attraverso il rapporto $r_l$.

Il teorema seguente stabilisce le proprietà della polizza ottima per $e=1$. La dimostrazione procede così: si mostra che i due moltiplicatori sono positivi, poi che i due vincoli sono attivi, e da $\beta>0$ e dalla proprietà MLR si ricava come la ricchezza finale varia con la perdita.

> [!tip] Teorema
> Sia $e=1$ il livello di impegno che la compagnia vuole indurre, valga la proprietà MLR e sia $B_0=0$. Allora:
>
> (a) $\beta>0$ e $\lambda>0$, quindi PC e IC valgono entrambi con uguaglianza;
>
> (b) $B_l-l$ è strettamente decrescente in $l\in\{0,1,\dots,L\}$;
>
> (c) $B_l<l$ per ogni $l\ge1$: la polizza non dà copertura piena per nessuna perdita positiva.

> [!note] Dimostrazione
> *Ipotesi.* Valgono quelle del benchmark ($u$ strettamente crescente e strettamente concava, $\pi_l(e)>0$, condizioni di Kuhn-Tucker nel punto di ottimo), la proprietà MLR con crescita stretta e $d(1)>d(0)$. Si ricorda che $u'$ è strettamente decrescente: $u'(z)<u'(z')$ se e solo se $z>z'$.
>
> *Passo 1: $\beta>0$.* Si supponga per assurdo $\beta\le0$. Le condizioni di Kuhn-Tucker danno già $\beta\ge0$, per cui basterebbe escludere $\beta=0$; l'argomento esclude anche $\beta<0$ senza usare questo segno: con $\beta<0$ la (5) renderebbe impossibile soddisfare IC.
>
> Se $\beta=0$, la (5) dà $1/u'(z_l)=\lambda$ per ogni $l$: $u'(z_l)$ è costante e, per l'iniettività di $u'$, anche $z_l=z$ è costante. Poiché $\sum_l[\pi_l(1)-\pi_l(0)]=1-1=0$, il vincolo IC diventa
>
> $$g_{IC}=\sum_l\big[\pi_l(1)-\pi_l(0)\big]u(z)-\big(d(1)-d(0)\big)=-\big(d(1)-d(0)\big)<0,$$
>
> che viola $g_{IC}\ge0$.
>
> Se $\beta<0$, il termine $-\beta\,r_l$ è strettamente crescente in $l$ perché $r_l$ lo è. Il secondo membro della (5) è strettamente crescente in $l$: lo è allora $1/u'(z_l)$, e $u'(z_l)$ è strettamente decrescente in $l$. Poiché $u'$ è strettamente decrescente, $z_l$ è strettamente crescente in $l$, e lo è anche $u(z_l)$. Per il punto (b) del teorema sulla proprietà MLR con $x_l=u(z_l)$ vale $\sum_l[\pi_l(0)-\pi_l(1)]\,u(z_l)>0$, cioè $\sum_l[\pi_l(1)-\pi_l(0)]\,u(z_l)<0$, e allora
>
> $$g_{IC}=\sum_l\big[\pi_l(1)-\pi_l(0)\big]u(z_l)-\big(d(1)-d(0)\big)<0,$$
>
> di nuovo una violazione di IC. Dunque $\beta>0$.
>
> *Passo 2: $\lambda>0$.* Si supponga $\lambda=0$. La (5) diventa $1/u'(z_l)=\beta\,(1-r_l)$. Il primo membro è positivo per ogni $l$. Per il punto (a) del teorema sulla proprietà MLR, $1-r_l$ è positivo per $l=0$ e negativo per $l=L$, e poiché $\beta>0$ il secondo membro cambia segno al variare di $l$. Per qualche $l$ la (5) non vale: contraddizione. Dunque $\lambda>0$.
>
> *Passo 3: i vincoli sono attivi.* Poiché $\lambda>0$ e $\beta>0$, la complementarità impone $g_{PC}=0$ e $g_{IC}=0$. Il cliente ottiene esattamente l'utilità $\bar u$ ed è indifferente fra impegno alto e impegno basso. Questo prova il punto (a).
>
> *Passo 4: monotonia.* Poiché $\beta>0$ e $r_l$ è strettamente crescente, il secondo membro della (5), $\lambda+\beta(1-r_l)$, è strettamente decrescente in $l$. Quindi $1/u'(z_l)$ è strettamente decrescente, $u'(z_l)$ è strettamente crescente e, per la stretta decrescenza di $u'$, $z_l$ è strettamente decrescente in $l$. Poiché $z_l-(w-p)=B_l-l$ e $w-p$ non dipende da $l$, la differenza $B_l-l$ è strettamente decrescente.
>
> *Passo 5: copertura parziale.* Con $B_0=0$ si ha $B_0-0=0$, e per la stretta decrescenza $B_l-l<0$ per ogni $l\ge1$, cioè $B_l<l$.

### Che cosa significa il risultato

Che entrambi i vincoli siano attivi ha una lettura economica. PC è attivo: se il cliente ricevesse più di $\bar u$, la compagnia potrebbe abbassare gli indennizzi in modo da ridurre della stessa quantità l'utilità $u(z_l)$ in ogni stato; IC non cambierebbe, perché $\sum_l[\pi_l(1)-\pi_l(0)]=0$, e il profitto salirebbe. IC è attivo: la polizza rende il cliente indifferente fra i due livelli di impegno, perché un incentivo più forte del necessario esporrebbe il cliente a più rischio, e la compagnia, che deve comunque garantirgli $\bar u$, dovrebbe compensarlo e guadagnerebbe meno.

La differenza $l-B_l$ è la parte della perdita che resta a carico del consumatore. È nulla per $l=0$ e strettamente crescente in $l$: il consumatore sopporta una franchigia che aumenta con l'importo della perdita.

Il rapporto $r_l$ misura quanto la perdita $l$ è più probabile con l'impegno basso che con l'impegno alto, e dice in quale direzione, e con quale forza, quella perdita sposta la valutazione dell'impegno: verso l'impegno basso se $r_l>1$, verso quello alto se $r_l<1$. La (5) lega la ricchezza finale a $r_l$: dove $r_l$ è più alto, $1/u'(z_l)$ è più basso, $u'(z_l)$ più alto e $z_l$ più basso. La polizza premia l'assicurato nelle perdite che indicano più probabilmente un impegno alto e lo penalizza in quelle che indicano più probabilmente un impegno basso. La compagnia osserva soltanto la perdita, e la perdita è il solo canale attraverso cui il compenso può dipendere, indirettamente, dall'impegno. La lettura è statistica: in equilibrio la compagnia sa che il cliente sceglie $e=1$, e legare la ricchezza a $r_l$ serve a togliere ogni vantaggio alla deviazione a $e=0$, che all'ottimo dà al cliente la stessa utilità dell'impegno alto.

Con la copertura piena l'impegno non darebbe al consumatore alcun vantaggio e IC non sarebbe soddisfatto: per questo $\beta=0$ è impossibile, perché la (5) darebbe la stessa ricchezza in ogni stato, cioè la copertura piena, e il cliente sceglierebbe l'impegno basso. L'impegno alto può essere indotto solo con $\beta>0$. Poiché IC è attivo, il vantaggio atteso in utilità dell'impegno alto, $\sum_l[\pi_l(1)-\pi_l(0)]\,u(z_l)$, deve uguagliare il costo $d(1)-d(0)$, e perciò deve essere positivo. La polizza ottima lo rende positivo facendo scendere la ricchezza finale al crescere della perdita: per il punto (b) del teorema sulla polizza per l'impegno alto, $B_l-l$ è strettamente decrescente in $l$, e con esso $z_l$ e $u(z_l)$; il punto (b) del teorema sulla proprietà MLR con $x_l=-u(z_l)$ dà $\sum_l[\pi_l(1)-\pi_l(0)]\,u(z_l)>0$. Con una ricchezza costante in $l$ il vantaggio sarebbe nullo, con una ricchezza strettamente crescente sarebbe negativo. La polizza ottiene questo risultato lasciando il consumatore esposto al rischio, e l'esposizione costa: il consumatore è avverso al rischio e la compagnia deve comunque garantirgli $\bar u$, perché PC è attivo.

## Polizza ottima ed efficienza

Sia $e^{**}$ il livello di impegno che la compagnia induce con la polizza ottima quando $e$ non è osservabile: è il livello, fra 0 e 1, a cui corrisponde il profitto maggiore fra quelli delle due polizze ottime trovate nelle sezioni precedenti (se i due profitti coincidono, il teorema seguente vale per entrambe le scelte). L'allocazione con $e$ osservabile è il *first best*; quella con $e$ non osservabile è il *second best*. Come nel capitolo sulle asimmetrie informative, il second best è il meglio raggiungibile dato il vincolo informativo.

> [!tip] Teorema
> Si assuma che con informazione simmetrica il massimo del profitto sia raggiunto in un solo livello di impegno $e^*$.
>
> (a) Se $e^*=0$, anche con informazione asimmetrica $e^{**}=0$, con la stessa polizza e lo stesso profitto del *first best*, e l'allocazione è Pareto efficiente.
>
> (b) Se $e^*=1$, l'allocazione non è Pareto efficiente: il *first best* la migliora in senso paretiano. O $e^{**}=0$, e allora l'impegno è inferiore a quello ottimale; oppure $e^{**}=1$, e allora il consumatore ottiene la stessa utilità del *first best*, $\bar u$, ma il profitto della compagnia è strettamente inferiore.

> [!note] Dimostrazione
> *Caso (a).* La polizza a copertura piena con $e=0$ soddisfa IC, per il teorema sulla polizza per l'impegno basso, ed è ammissibile con informazione asimmetrica: dà il profitto $\Pi^{FB}(0)$. Con $e=1$ il problema con informazione asimmetrica ha un vincolo in più rispetto a quello con informazione simmetrica, quindi il suo massimo non supera $\Pi^{FB}(1)$, che è minore di $\Pi^{FB}(0)$ perché $e^*=0$ è l'unico massimo. Ne segue $e^{**}=0$, con la stessa polizza e lo stesso profitto del *first best*. L'allocazione coincide con quella del *first best*, che è Pareto efficiente per il teorema sull'efficienza del benchmark.
>
> *Caso (b).* La polizza ottima del *first best* con $e=1$ è a copertura piena, $B_l=l$. Con $B_l=l$ il vincolo IC con $e=1$ diventa $u(w-p)-d(1)\ge u(w-p)-d(0)$, cioè $d(1)\le d(0)$, che è falsa. La polizza del *first best* viola IC e non è ammissibile. La polizza ottima per $e=1$ con informazione asimmetrica ha $B_l<l$ per $l\ge1$ e ricchezza finale $z_l$ non costante. Per il teorema sul benchmark ogni soluzione del problema con informazione simmetrica ha $z_l$ costante, quindi la polizza con $B_l<l$ è ammissibile in quel problema ma non ne è una soluzione, e il suo profitto è strettamente inferiore a $\Pi^{FB}(1)$. Poiché PC è attivo, l'utilità del consumatore è $\bar u$, come nel *first best*.
>
> Se invece la compagnia induce $e=0$, la polizza è a copertura piena, l'utilità del consumatore è $\bar u$ e il profitto è $\Pi^{FB}(0)$, strettamente minore di $\Pi^{FB}(1)$ perché $e^*=1$ è l'unico massimo.
>
> In entrambi i casi il consumatore ottiene $\bar u$ e la compagnia meno che nel *first best*. L'allocazione del *first best* sarebbe un miglioramento paretiano, ma non è ammissibile se la compagnia non osserva $e$.

L'inefficienza di cui parla il teorema è relativa al *first best*, che si può realizzare soltanto se l'impegno è osservabile. Indurre l'impegno alto in presenza di asimmetrie informative è costoso: la compagnia non può fare a meno di esporre il cliente al rischio, e ne ricava un profitto minore, mentre l'utilità del cliente resta $\bar u$.

## Incentivi nella pratica

L'azzardo morale è un problema serio per il mercato assicurativo, perché può produrre un'allocazione inefficiente. Se la compagnia induce l'impegno alto, la polizza ottima lascia a carico del cliente una parte di ogni perdita positiva; con l'impegno basso resta a copertura piena.

Nella pratica le compagnie ricorrono a incentivi specifici. Nell'assicurazione sanitaria offrono sconti sul premio a chi frequenta con regolarità una palestra; nell'assicurazione auto offrono sconti a chi accetta di installare una scatola nera. In entrambi i casi il premio dipende da un comportamento che la compagnia riesce a osservare, e questo avvicina la situazione al benchmark con impegno osservabile, ma solo in parte, perché il comportamento è soltanto un indizio dell'impegno.
