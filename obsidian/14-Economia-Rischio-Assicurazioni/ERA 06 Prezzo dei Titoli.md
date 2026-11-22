---
title: "Prezzo dei titoli: agente rappresentativo, pricing kernel, premio al rischio di mercato ed equity premium puzzle"
tags:
  - corso/economia-rischio-assicurazioni
  - tipo/lezione
corso: "[[Economia del Rischio e delle Assicurazioni]]"
source: "ERA_Slide_05_Prezzo-dei-Titoli.pdf"
text_layer: true
verified: true
generated: 2026-11-22
---

## Oggetto del capitolo

Il capitolo determina il prezzo di un titolo rischioso come equilibrio fra domanda e offerta. Nel [[ERA 05 Portafoglio Ottimale|portafoglio ottimale]] il rendimento atteso del titolo rischioso era un dato e l'agente sceglieva quanto investire. Qui il rendimento atteso è un risultato del modello, e si studia come dipende dalle condizioni di mercato.

Il modello base ha un agente rappresentativo e porta a una formula per il premio al rischio di mercato (*equity premium*), cioè la differenza fra il rendimento atteso del titolo rischioso e quello del titolo privo di rischio. Calibrata sui dati, la formula dà un valore molto più basso di quello osservato: è l'*equity premium puzzle*. Il resto del capitolo rilassa l'ipotesi di agente rappresentativo con la partecipazione limitata al mercato dei titoli e con l'apertura al mercato internazionale dei capitali, e poi estende il modello a più titoli.

Il capitolo segue il portafoglio ottimale e precede le [[ERA 07 Assicurazioni e Asimmetrie Informative|assicurazioni e le asimmetrie informative]]. Dall'[[ERA 02 Teoria dell'Utilità Attesa|utilità attesa]] riprende il criterio di scelta, dall'[[ERA 03 Avversione al Rischio|avversione al rischio]] la concavità di $u$ e la funzione CRRA, dal [[ERA 01 Ripasso|ripasso]] la covarianza.

## Richiamo sulla covarianza

La covarianza $\mathrm{Cov}(X,Y)=E\big[(X-E[X])(Y-E[Y])\big]=E[XY]-E[X]\,E[Y]$, la cui seconda forma è quella usata nel capitolo, e il segno della correlazione sono definiti nel [[ERA 01 Ripasso|ripasso]]. Il capitolo usa anche alcune proprietà che seguono dalla definizione: $\mathrm{Cov}(X,X)=\mathrm{Var}(X)$, la simmetria $\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)$ e $\mathrm{Cov}(X,c)=0$ per una costante $c$, perché $c-E[c]=0$. C'è poi la linearità, $\mathrm{Cov}(aX,Y)=a\,\mathrm{Cov}(X,Y)$ e $\mathrm{Cov}(X+Z,Y)=\mathrm{Cov}(X,Y)+\mathrm{Cov}(Z,Y)$ per $a$ reale, che per la simmetria vale anche nel secondo argomento: $\mathrm{Cov}(X,aY)=a\,\mathrm{Cov}(X,Y)$.

## Il modello

### Ipotesi e variabili

Il modello ha un solo periodo. Oggi l'agente decide, domani consuma, e la sua utilità dipende dalla ricchezza finale. Un titolo rischioso vale $P$ oggi e $\tilde y$ domani; la tilde segnala una variabile casuale. Poiché il titolo non paga dividendi, $\tilde y$ è tutto ciò che il titolo rende. Esiste anche un titolo privo di rischio, con rendimento lordo $R_f$ noto e costante: un euro investito oggi ne rende $R_f$ domani. I rendimenti del capitolo sono lordi, cioè uguali a uno più il rendimento netto del [[ERA 05 Portafoglio Ottimale|portafoglio ottimale]]. Il titolo privo di rischio è in offerta netta nulla: ogni euro che qualcuno vi investe è preso a prestito da qualcun altro.

Il titolo è posseduto da un agente rappresentativo, che non incontra vincoli nel prendere o dare a prestito. L'agente è avverso al rischio: ha una funzione di utilità di Bernoulli $u$ con $u'>0$ e $u''<0$. Parte con una quota del titolo e sceglie la quota $\alpha$ da tenere, senza vincoli. Con $\alpha<1$ vende $1-\alpha$ quote e investe il ricavato nel titolo privo di rischio. Con $\alpha>1$ compra altre quote e prende a prestito per pagarle, con $\alpha<0$ vende allo scoperto.

L'agente rappresentativo si può sostituire con molti agenti identici, ciascuno con una quota del titolo, in una popolazione di dimensione uno. La quota individuale per la dimensione della popolazione dà il totale delle quote: $1\cdot1=1$. L'ipotesi è comune in macroeconomia. Le sezioni sugli agenti eterogenei e sul mercato internazionale la rilassano.

Se l'agente tiene $\alpha$ quote, la somma $(1-\alpha)P$ ricavata dalla vendita delle altre rende $R_f$ per euro, e la ricchezza finale è

$$W=\alpha\tilde y+(1-\alpha)R_fP=R_fP+\alpha\,(\tilde y-R_fP).$$

È il problema di portafoglio del capitolo precedente, senza il vincolo $\alpha\in[0,W]$ di quel capitolo, in cui $W$ è la ricchezza iniziale, e con $\alpha$ misurato in quote. La ricchezza certa è $w_0=R_fP$ e il guadagno in eccesso di una quota, rispetto alla stessa somma $P$ investita nel titolo privo di rischio, è $\tilde x=\tilde y-R_fP$. Il rendimento lordo atteso del titolo è $R=E[\tilde y]/P$. Il **premio al rischio di mercato** (*equity premium*) è la differenza

$$\phi=R-R_f.$$

La stessa grandezza si chiama anche premio per il capitale di rischio.

### Notazione

Quattro simboli hanno qui un significato diverso da quello dei capitoli sull'[[ERA 03 Avversione al Rischio|avversione al rischio]] e sul [[ERA 05 Portafoglio Ottimale|portafoglio ottimale]]. $P$ è il prezzo del titolo e non la prudenza assoluta, $R$ è il rendimento lordo atteso e non il premio per il rischio, $\phi$ è il premio al rischio di mercato e non una trasformazione concava, $k$ è la frazione dei partecipanti al mercato e non la scala di una lotteria. La lettera $W$ indica la ricchezza finale, argomento di $u$ come nell'avversione al rischio; nel portafoglio ottimale indicava la ricchezza iniziale. Il capitolo non usa prudenza né trasformazioni concave, e il premio per il rischio $R$ del capitolo sull'avversione al rischio si scrive a parole o con l'equivalente certo $CE$. Il simbolo $\alpha$, che è un peso di miscela nella teoria dell'utilità attesa e un ammontare in euro nel portafoglio ottimale, è qui una quota del titolo. Le lettere $A$ e $B$ sono le etichette dei due paesi nella sezione sul mercato internazionale dei capitali, non l'avversione assoluta né un importo. L'attesa si scrive sempre $E[\cdot]$, e l'agente è avverso al rischio salvo dove si dice il contrario.

## La domanda dell'agente rappresentativo

L'agente sceglie la quota $\alpha$ che massimizza l'utilità attesa della ricchezza finale:

$$\max_{\alpha}\ V(\alpha)=E\big[u\big(\alpha\tilde y+(1-\alpha)R_fP\big)\big].$$

La derivata della ricchezza finale rispetto ad $\alpha$ è $\tilde y-R_fP$, e la derivata passa sotto il segno di attesa. La condizione del primo ordine (FOC) è quindi

$$V'(\alpha)=E\Big[(\tilde y-R_fP)\,u'\big(\alpha\tilde y+(1-\alpha)R_fP\big)\Big]=0.$$

È la FOC del problema di portafoglio, $E[\tilde x\,u'(w_0+\alpha\tilde x)]=0$, con $w_0=R_fP$ e $\tilde x=\tilde y-R_fP$: all'ottimo il guadagno in eccesso di una quota, pesato con l'utilità marginale dello stato in cui si realizza, ha valore atteso nullo. La FOC è anche sufficiente. La derivata seconda è $V''(\alpha)=E\big[(\tilde y-R_fP)^2\,u''(W)\big]$, negativa perché $u''<0$ e, poiché il titolo è rischioso, $\tilde y$ non è degenere e $\tilde y\neq R_fP$ con probabilità positiva. La funzione obiettivo è strettamente concava in $\alpha$: la FOC è necessaria e sufficiente e la quota ottima, se esiste, è unica.

Il segno della domanda si legge in $\alpha=0$. Allora la ricchezza finale $R_fP$ è certa, e

$$V'(0)=u'(R_fP)\,E[\tilde y-R_fP]=u'(R_fP)\,P\,(R-R_f).$$

Poiché $V'$ è decrescente, la quota ottima, se esiste, è positiva se e solo se $R>R_f$. Come nel [[ERA 05 Portafoglio Ottimale|portafoglio ottimale]], il titolo rischioso è domandato solo se rende in media più del titolo privo di rischio.

## L'offerta e il prezzo di equilibrio

Poiché non c'è una controparte con cui commerciare, il mercato si chiude se la quota ottima è $\alpha=1$: l'agente non vuole né comprare né vendere. Con molti agenti identici la conclusione è la stessa. Se uno vuole comprare altre quote lo vogliono tutti, e lo stesso vale per la vendita: il mercato si chiude solo se ciascuno vuole tenere la propria quota. Con $\alpha=1$ l'agente non detiene titoli privi di rischio, $(1-\alpha)P=0$, e anche il mercato del titolo privo di rischio, in offerta netta nulla, è in equilibrio. Il prezzo di equilibrio è il prezzo $P$ al quale la domanda ottima è $\alpha=1$.

Con $\alpha=1$ la ricchezza finale è $\tilde y$ e la FOC diventa $E[(\tilde y-R_fP)\,u'(\tilde y)]=0$, che equivale a $E[\tilde y\,u'(\tilde y)]=R_fP\,E[u'(\tilde y)]$. Poiché $E[u'(\tilde y)]>0$, si può dividere:

$$R_fP=E\Big[\tilde y\,\frac{u'(\tilde y)}{E[u'(\tilde y)]}\Big],\qquad\text{ossia}\qquad P=\frac{E[\tilde y\,u'(\tilde y)]}{R_f\,E[u'(\tilde y)]}.$$

Il prezzo è il valore atteso di $\tilde y$ pesato con l'utilità marginale normalizzata e scontato al tasso privo di rischio. Il secondo membro non dipende da $P$, perché il consumo di equilibrio è $\tilde y$ qualunque sia il prezzo: $P$ si calcola direttamente da $u$, dalla distribuzione di $\tilde y$ e da $R_f$.

## Il pricing kernel

> [!abstract] Definizione
> Si chiama ***pricing kernel*** l'utilità marginale normalizzata
>
> $$\tilde M=\frac{u'(\tilde y)}{E[u'(\tilde y)]}.$$
>
> In generale, per un agente il cui consumo è la variabile casuale $\tilde c$, $\tilde M=u'(\tilde c)/E[u'(\tilde c)]$.

Nel modello a un periodo il consumo è la ricchezza finale, che in equilibrio è $\tilde y$. Il kernel è una variabile casuale con $E[\tilde M]=E[u'(\tilde y)]/E[u'(\tilde y)]=1$ per costruzione. La condizione di equilibrio dell'offerta si scrive

$$R_fP=E[\tilde y\,\tilde M].$$

Poiché $u'$ è decrescente, $\tilde M$ è grande negli stati in cui $\tilde y$ è basso, dove l'utilità marginale è alta. Un titolo che paga di più proprio in quegli stati ha perciò un prezzo più alto. Per la seconda forma della covarianza e con $E[\tilde M]=1$, la condizione di equilibrio equivale a

$$P=\frac{E[\tilde y]+\mathrm{Cov}(\tilde y,\tilde M)}{R_f}.$$

Il prezzo è il valore atteso di $\tilde y$ scontato al tasso privo di rischio, più un aggiustamento per il rischio, $\mathrm{Cov}(\tilde y,\tilde M)/R_f$, negativo per un titolo che rende poco quando l'utilità marginale è alta.

Nei testi di finanza il fattore di sconto stocastico $m$ è definito dalla condizione $P=E[m\,\tilde y]$ e ha media $1/R_f$. Il kernel di questo capitolo è la versione normalizzata a media uno, $\tilde M=R_fm$, e per $R_f=1$ le due definizioni coincidono.

## Il premio al rischio di mercato

> [!tip] Teorema
> Sia $u'>0$ e sia $P>0$ il prezzo di equilibrio. Il premio al rischio di mercato è
>
> $$\phi=-\frac{\mathrm{Cov}(\tilde y,\tilde M)}{P}=-\frac{\mathrm{Cov}\big(\tilde y,u'(\tilde y)\big)}{P\,E[u'(\tilde y)]}.$$
>
> Se inoltre $u''<0$ e $\tilde y$ non è degenere, allora $\phi>0$.

> [!note] Dimostrazione
> *Identità.* Per definizione $\phi=E[\tilde y]/P-R_f$. Si usa $E[\tilde M]=1$ al numeratore e la condizione di equilibrio $R_fP=E[\tilde y\tilde M]$:
>
> $$\phi=\frac{E[\tilde y]\,E[\tilde M]-R_fP}{P}=\frac{E[\tilde y]\,E[\tilde M]-E[\tilde y\tilde M]}{P}=-\frac{\mathrm{Cov}(\tilde y,\tilde M)}{P}.$$
>
> L'ultimo passaggio è la seconda forma della covarianza. Poi $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$ e $E[u'(\tilde y)]$ è un numero, quindi per la linearità della covarianza nel secondo argomento $\mathrm{Cov}(\tilde y,\tilde M)=\mathrm{Cov}(\tilde y,u'(\tilde y))/E[u'(\tilde y)]$. Questo dà la seconda espressione.
>
> *Segno.* Sia $\tilde y'$ una copia di $\tilde y$ indipendente da $\tilde y$ e con la stessa distribuzione, e sia $g=u'$. Per l'indipendenza e l'uguaglianza delle distribuzioni, $E[\tilde y\,g(\tilde y')]=E[\tilde y]\,E[g(\tilde y)]=E[\tilde y'\,g(\tilde y)]$ e $E[\tilde y'g(\tilde y')]=E[\tilde y\,g(\tilde y)]$. Sviluppando il prodotto,
>
> $$E\big[(\tilde y-\tilde y')\big(g(\tilde y)-g(\tilde y')\big)\big]=2E[\tilde y\,g(\tilde y)]-2E[\tilde y]\,E[g(\tilde y)]=2\,\mathrm{Cov}\big(\tilde y,g(\tilde y)\big).$$
>
> Poiché $u''<0$, la funzione $g=u'$ è decrescente: i fattori $\tilde y-\tilde y'$ e $g(\tilde y)-g(\tilde y')$ hanno segni opposti oppure sono nulli, e il prodotto non è mai positivo. È negativo con probabilità positiva se $\tilde y$ non è degenere, perché allora $\tilde y\neq\tilde y'$ con probabilità positiva. Quindi $\mathrm{Cov}(\tilde y,u'(\tilde y))<0$. Con $P>0$ e $E[u'(\tilde y)]>0$ la formula dà $\phi>0$.

Il premio al rischio di mercato è positivo perché $\tilde y$ e $u'(\tilde y)$ sono correlati negativamente: l'utilità marginale è alta proprio dove il titolo rende poco. Il prezzo $P=(E[\tilde y]+\mathrm{Cov}(\tilde y,\tilde M))/R_f$ è perciò inferiore a $E[\tilde y]/R_f$ e il rendimento atteso supera $R_f$. Se $u''\le0$, cioè per un agente avverso o neutrale al rischio, la dimostrazione dà di più: il premio al rischio di mercato è nullo se e solo se $u'$ è costante sull'insieme dei valori di $\tilde y$. Con $u''<0$ questo accade solo se $\tilde y$ è degenere; per l'agente neutrale al rischio del quiz seguente accade sempre. Più l'agente è avverso al rischio, più alto è $\phi$: la calibrazione della sezione successiva illustra che $\phi$ cresce con il coefficiente $\gamma$ della CRRA.

> [!example] Esempio
> Quiz. Se l'agente rappresentativo è neutrale al rischio, il premio al rischio di mercato è (1) positivo, (2) zero, (3) negativo?
>
> *Risposta: (2), zero.* L'agente neutrale al rischio ha $u$ lineare: $u'$ è una costante positiva e $\tilde M=u'/E[u']\equiv1$. La covarianza di $\tilde y$ con una costante è nulla, quindi $\phi=-\mathrm{Cov}(\tilde y,\tilde M)/P=0$. Il prezzo è $P=E[\tilde y]/R_f$: un agente neutrale non chiede compenso per detenere il titolo rischioso. L'identità del teorema richiede solo $u'>0$ e vale anche con $u''=0$.

> [!example] Esempio
> Sia $u=\ln$, $R_f=1$, e sia $\tilde y$ uguale a $1$ o $2$ con probabilità $\tfrac12$. Allora $u'(\tilde y)=1/\tilde y$ e $E[u'(\tilde y)]=\tfrac12\big(1+\tfrac12\big)=\tfrac34$. Poiché $\tilde y\,u'(\tilde y)=1$, il prezzo di equilibrio è $P=1/E[u'(\tilde y)]=4/3$. Il kernel vale $\tilde M=(1/\tilde y)/(3/4)$, cioè $4/3$ se $\tilde y=1$ e $2/3$ se $\tilde y=2$, con media $1$. Si ha $E[\tilde y\tilde M]=\tfrac12\big(\tfrac43+\tfrac43\big)=\tfrac43=R_fP$, come richiesto dall'equilibrio, e $E[\tilde y]=\tfrac32$. La covarianza vale
>
> $$\mathrm{Cov}(\tilde y,\tilde M)=\tfrac43-\tfrac32=-\tfrac16.$$
>
> Il rendimento atteso è $R=E[\tilde y]/P=\tfrac32\cdot\tfrac34=\tfrac98$ e il premio al rischio di mercato è $\phi=\tfrac98-1=\tfrac18$, uguale a $-\mathrm{Cov}(\tilde y,\tilde M)/P=\tfrac16\big/\tfrac43=\tfrac18$.

## L'equity premium puzzle

### Dati osservati e calibrazione del modello

Mehra e Prescott hanno posto il puzzle a partire dal premio al rischio di mercato osservato negli Stati Uniti nel periodo 1889-1978, di circa il 6%. Il rendimento reale medio dell'indice S&P 500 è 6,98%, circa il 7%, mentre il tasso reale privo di rischio è 0,80%. In termini di rendimenti lordi, $1{,}0698-1{,}008=0{,}0618$: il premio al rischio di mercato osservato è del 6,18%.

Il modello predice un valore molto più basso. La formula del teorema si può approssimare quando $\tilde y$ è poco disperso attorno al suo valore atteso $\mu=E[\tilde y]$. Si sostituisce $u'(\tilde y)$ con l'approssimazione lineare $u'(\mu)+u''(\mu)(\tilde y-\mu)$ e si ottiene $\mathrm{Cov}(\tilde y,u'(\tilde y))\approx u''(\mu)\,\mathrm{Var}(\tilde y)$ e $E[u'(\tilde y)]\approx u'(\mu)$. Con $R_f=1$, come nella calibrazione, $P=\mu+\mathrm{Cov}(\tilde y,\tilde M)$ differisce da $\mu$ per un termine dell'ordine di $\mathrm{Var}(\tilde y)$, quindi $P\approx\mu$. Ne segue

$$\phi\approx-\frac{u''(\mu)}{u'(\mu)}\,\frac{\mathrm{Var}(\tilde y)}{P}\approx-\mu\,\frac{u''(\mu)}{u'(\mu)}\,\frac{\mathrm{Var}(\tilde y)}{\mu^2}=RR(\mu)\,\frac{\mathrm{Var}(\tilde y)}{\mu^2},$$

dove $RR$ è l'avversione relativa al rischio del capitolo sull'[[ERA 03 Avversione al Rischio|avversione al rischio]]. Per un'utilità con avversione relativa al rischio costante (CRRA) $u(W)=W^{1-\gamma}/(1-\gamma)$ si ha $RR=\gamma$ e l'approssimazione diventa

$$\phi\approx\gamma\,\frac{\mathrm{Var}(\tilde y)}{E[\tilde y]^2}.$$

Il premio al rischio di mercato del modello è proporzionale al coefficiente di avversione $\gamma$ e al quadrato del coefficiente di variazione di $\tilde y$. Calibrando il modello sulla crescita del PIL reale pro capite degli Stati Uniti nel periodo 1963-92, $\tilde y$ è il fattore lordo di crescita e $\mathrm{Var}(\tilde y)/E[\tilde y]^2=0{,}056\%$, una deviazione standard di circa il 2,4% del valore atteso. Il consumo varia poco, e serve un'avversione molto alta per ottenere un $\phi$ sensibile. Con $\gamma=2$ il modello dà $\phi\approx2\cdot0{,}056\%=0{,}11\%$, lo stesso valore del calcolo con i dati, contro il 6% osservato. Per $\gamma$ grande l'approssimazione si allontana dal calcolo: per $\gamma=40$ la formula dà $2{,}24\%$, il calcolo con i dati $2{,}86\%$. Il valore osservato e quello del modello vengono da campioni diversi, il 1889-1978 per il primo e il 1963-92 per la calibrazione, ma lo scarto di quasi due ordini di grandezza non dipende da questa differenza.

Per riprodurre il valore osservato servirebbe $\gamma>40$. Se il modello è corretto, l'agente rappresentativo deve essere estremamente avverso al rischio. L'esempio seguente dà la misura di questa avversione.

> [!example] Esempio
> Sia $\gamma=40$ e sia $w$ la ricchezza di un agente che accetta o rifiuta una scommessa: con probabilità $\tfrac12$ guadagna il 30% di $w$ e con probabilità $\tfrac12$ lo perde. L'equivalente certo $CE$ soddisfa $u(CE)=\tfrac12u(0{,}7w)+\tfrac12u(1{,}3w)$, cioè
>
> $$CE^{-39}=\tfrac12\Big[(0{,}7w)^{-39}+(1{,}3w)^{-39}\Big],\qquad CE=0{,}7126\,w.$$
>
> L'agente è indifferente fra la scommessa e una ricchezza certa pari al 71,26% di $w$: pagherebbe il 28,7%, circa il 29% della ricchezza, per evitare di perdere o guadagnare il 30% con uguale probabilità.

### Le spiegazioni proposte

Il divario fra il premio al rischio di mercato osservato e quello del modello si può cercare in quattro direzioni. La prima è il campione: si controlla se il puzzle dipende dagli anni scelti, per esempio con i dati più recenti del 1979-2009. Con altri campioni il valore osservato resta molto più alto di quello del modello: 6,9% nel 1889-2000 e 4,5% nel 1963-95, contro lo 0,11% del modello.

La seconda è l'eterogeneità degli agenti: l'agente rappresentativo è un'ipotesi forte, e agenti diversi possono avere rischi di reddito non assicurabili o un accesso limitato al mercato dei titoli. Questa è la direzione sviluppata nella sezione seguente. La terza è l'uso di preferenze diverse dall'utilità attesa, per esempio l'avversione alle perdite con valutazione frequente del portafoglio (Benartzi e Thaler) e l'ambiguità. La quarta è l'effetto delle politiche pubbliche, come le tasse sulle rendite da capitale e sulle imprese e la regolamentazione dei fondi pensione (McGrattan e Prescott).

## Agenti eterogenei: la partecipazione limitata

### Il modello con partecipazione $k$

Si supponga che solo una frazione $k\in(0,1]$ della popolazione possa tenere il titolo rischioso fino a domani, per ragioni di abilità o per imperfezioni del mercato dei capitali che il modello non descrive: la frazione $k$ è un dato esogeno. I partecipanti prendono a prestito al tasso $R_f$, come si vede più sotto: l'esclusione riguarda solo il titolo rischioso, e i non partecipanti investono comunque nel titolo privo di rischio.

I non partecipanti vendono la propria quota al prezzo di equilibrio, che dipende da $k$ e si scrive $P(k)$, la investono al tasso $R_f$ e consumano $R_fP(k)$ con certezza: sono completamente assicurati contro il rischio aggregato. I partecipanti, che sono una frazione $k$ della popolazione, comprano le quote cedute. In equilibrio l'offerta di quote è 1 e la domanda è $k\alpha$: la condizione di chiusura del mercato diventa $k\alpha=1$, ossia

$$\alpha=\frac1k,$$

che supera 1 per $k<1$. Ciascun partecipante detiene $1/k$ quote e prende a prestito $\frac{1-k}{k}P(k)$ per pagare le quote in più. La sua ricchezza finale è

$$W_k=\frac{\tilde y}{k}+\frac{k-1}{k}R_fP(k)=R_fP(k)+\frac{\tilde y-R_fP(k)}{k}.$$

L'eccesso del valore del titolo su $R_fP(k)$ è moltiplicato per $1/k$. Per $k<1$ la ricchezza del partecipante è più rischiosa di $\tilde y$, perché $\mathrm{Var}(W_k)=\mathrm{Var}(\tilde y)/k^2>\mathrm{Var}(\tilde y)$. Con $R_f=1$ si ha $W_k=\tilde y/k+\frac{k-1}{k}P(k)$. La FOC dell'agente, valutata in $\alpha=1/k$, è

$$E\Big[\big(\tilde y-R_fP(k)\big)\,u'(W_k)\Big]=0,$$

che determina il prezzo di equilibrio. Per $k=1$ si ritrova il modello base. In generale $P(k)$ non ha una forma chiusa e si calcola numericamente. Il pricing kernel diventa

$$\tilde M(k)=\frac{u'(W_k)}{E[u'(W_k)]}.$$

### Il premio al rischio di mercato con partecipazione limitata

> [!tip] Teorema
> Sia $u'>0$, sia $k\in(0,1]$ e sia $P(k)>0$ il prezzo al quale la quota ottima del partecipante è $\alpha=1/k$. Allora valgono $R_fP(k)=E[\tilde y\,\tilde M(k)]$ e
>
> $$\phi(k)=\frac{E[\tilde y]}{P(k)}-R_f=-\frac{\mathrm{Cov}\big(\tilde y,\tilde M(k)\big)}{P(k)}.$$

> [!note] Dimostrazione
> La FOC $E[(\tilde y-R_fP(k))\,u'(W_k)]=0$ equivale a $E[\tilde y\,u'(W_k)]=R_fP(k)\,E[u'(W_k)]$. Si divide per $E[u'(W_k)]>0$ e si ottiene $E[\tilde y\,\tilde M(k)]=R_fP(k)$. È la condizione di equilibrio del modello base con $\tilde M(k)$ al posto di $\tilde M$, e $E[\tilde M(k)]=1$ per costruzione. La catena di passaggi della dimostrazione del teorema sul premio al rischio di mercato vale invariata:
>
> $$\phi(k)=\frac{E[\tilde y]\,E[\tilde M(k)]-R_fP(k)}{P(k)}=\frac{E[\tilde y]\,E[\tilde M(k)]-E[\tilde y\,\tilde M(k)]}{P(k)}=-\frac{\mathrm{Cov}\big(\tilde y,\tilde M(k)\big)}{P(k)}.$$

I partecipanti detengono $1/k$ quote e la loro ricchezza è più variabile di $\tilde y$: chiedono un compenso maggiore, perché l'argomento di $u'$ nel kernel contiene $\tilde y/k$, più volatile di $\tilde y$. Il calcolo numerico conferma che il premio al rischio di mercato è maggiore quando $k$ è piccolo. Il risultato è numerico e non si dimostra in generale.

> [!example] Esempio
> Siano $u=\ln$, $R_f=1$ e $\tilde y$ uguale a $1$ o $2$ con probabilità $\tfrac12$, come nell'esempio svolto sul premio al rischio di mercato. Scritto $P$ per $P(k)$, la FOC è $E\big[(\tilde y-P)/(P+(\tilde y-P)/k)\big]=0$. Moltiplicando numeratore e denominatore di ciascun termine per $k$ e dividendo per $k/2$ si ottiene
>
> $$\frac{1-P}{kP+1-P}+\frac{2-P}{kP+2-P}=0\quad\Longrightarrow\quad(2-2k)P^2-(6-3k)P+4=0.$$
>
> Per $k=1$ l'equazione si riduce a $-3P+4=0$. Per $k<1$ ha due radici e $P(k)$ è la minore: l'altra supera $E[\tilde y]=\tfrac32$ e darebbe ricchezza negativa al partecipante. Il premio al rischio di mercato è $\phi(k)=\tfrac32/P(k)-1$:
>
> | $k$ | $P(k)$ | $\phi(k)$ |
> |---|---|---|
> | $1$ | $1{,}3333$ | $0{,}1250$ |
> | $1/2$ | $1{,}2192$ | $0{,}2303$ |
> | $1/3$ | $1{,}1569$ | $0{,}2965$ |
> | $1/4$ | $1{,}1208$ | $0{,}3383$ |
> | $1/5$ | $1{,}0979$ | $0{,}3663$ |
>
> Il premio al rischio di mercato cresce al diminuire di $k$, e per $k\to0$ tende a $\tfrac12$ mentre $P(k)\to1$. Per $k=1/5$ la ricchezza del partecipante vale $0{,}6085$ se $\tilde y=1$ e $5{,}6085$ se $\tilde y=2$.

Con la calibrazione della sezione precedente ($\gamma=2$, crescita del PIL reale pro capite degli Stati Uniti nel 1963-92) il calcolo numerico mostra che la partecipazione limitata non sposta in modo apprezzabile il premio al rischio di mercato finché $k$ supera circa il 30%. Sotto questa soglia l'effetto cresce abbastanza da avvicinare il valore osservato.

## Il mercato internazionale dei capitali

### Due paesi

Ci sono due paesi, $A$ e $B$. Ciascuno ha un agente rappresentativo che possiede una quota del titolo domestico. I valori dei titoli domani, $\tilde y^A$ e $\tilde y^B$, sono variabili casuali indipendenti e identicamente distribuite (i.i.d.), e i prezzi oggi dei due titoli sono uguali a $P$. I due agenti hanno preferenze identiche e commerciano titoli domestici e stranieri sul mercato finanziario internazionale. Ci si chiede come l'accesso a questo mercato influenzi il premio al rischio di mercato di ciascun titolo.

L'agente del paese $A$ parte con una quota del titolo $A$, che vale $P$. Detiene $\alpha^A$ del titolo $A$, $\alpha^B$ del titolo $B$ e $P(1-\alpha^A-\alpha^B)$ in titoli privi di rischio. La sua ricchezza finale è

$$W=\alpha^A\tilde y^A+\alpha^B\tilde y^B+R_fP\,(1-\alpha^A-\alpha^B),$$

e per $i\in\{A,B\}$ la FOC è $E[(\tilde y^i-R_fP)\,u'(W)]=0$.

Le preferenze sono identiche, il mercato non ha frizioni e la situazione iniziale è simmetrica: ciascun agente parte con una quota di un titolo che è, ex ante, identico a quello dell'altro paese. Alla fine i due agenti hanno quindi lo stesso portafoglio. L'offerta di ciascun titolo è 1 e gli agenti sono due: l'equilibrio è

$$\alpha^A(1+1)=1,\qquad\alpha^B(1+1)=1\qquad\Longrightarrow\qquad\alpha^A=\alpha^B=\tfrac12.$$

Ciascun agente diversifica perfettamente. Le quote dei titoli privi di rischio sono nulle e la ricchezza finale è la media dei due valori, $W=(\tilde y^A+\tilde y^B)/2$. Il prezzo $P$ è lo stesso per i due titoli, per la simmetria, ma non è quello che si avrebbe senza integrazione: dipende dal mercato integrato.

### Il premio al rischio di mercato con integrazione

Il pricing kernel diventa

$$\tilde M=\frac{u'\Big(\dfrac{\tilde y^A+\tilde y^B}{2}\Big)}{E\Big[u'\Big(\dfrac{\tilde y^A+\tilde y^B}{2}\Big)\Big]}.$$

Per la FOC del titolo $A$ vale ancora $E[\tilde y^A\tilde M]=R_fP$, e la catena di passaggi del teorema sul premio al rischio di mercato dà $\phi=-\mathrm{Cov}(\tilde y^A,\tilde M)/P$. Il kernel dipende ora dalla media dei due valori e non da $\tilde y^A$ soltanto, e ha con il valore del titolo domestico una covarianza minore, in valore assoluto, di quella senza integrazione. La diversificazione rende il consumo meno variabile: poiché i due valori sono i.i.d., $\mathrm{Var}\big((\tilde y^A+\tilde y^B)/2\big)=\mathrm{Var}(\tilde y)/2$. L'integrazione dei mercati dei capitali riduce il premio al rischio di mercato. La minore covarianza e la riduzione del premio al rischio di mercato non hanno una dimostrazione generale: si verificano con un calcolo esatto per un'utilità quadratica e, per la CRRA, con il calcolo numerico.

Per un'utilità quadratica, $u'(W)=a-bW$ con $b>0$ e $a-bW>0$ sui valori possibili della ricchezza, la riduzione della covarianza è esatta. Senza integrazione la covarianza di $\tilde y$ con il kernel del modello base vale $-b\,\mathrm{Var}(\tilde y)/E[u'(\tilde y)]$. Con integrazione, e con il kernel $\tilde M$ appena definito, $\mathrm{Cov}(\tilde y^A,W)=\mathrm{Var}(\tilde y)/2$ per l'indipendenza, e $E[u'(W)]=a-bE[W]=E[u'(\tilde y)]$ perché $W$ e $\tilde y$ hanno lo stesso valore atteso. Ne segue

$$\mathrm{Cov}(\tilde y^A,\tilde M)=-\frac{b\,\mathrm{Var}(\tilde y)}{2\,E[u'(\tilde y)]}.$$

La covarianza si dimezza. Con l'utilità quadratica il premio al rischio di mercato scende a meno della metà, perché il prezzo sale con l'integrazione. Con utilità CRRA il calcolo numerico mostra, nei casi considerati, una riduzione del premio al rischio di mercato a circa la metà: con $\gamma=2$ da $0{,}11\%$ a $0{,}06\%$ e con $\gamma=40$ da $2{,}86\%$ a $1{,}42\%$.

> [!example] Esempio
> Sia $u=\ln$, $R_f=1$, e siano $\tilde y^A$ e $\tilde y^B$ i.i.d., uguali a $1$ o $2$ con probabilità $\tfrac12$. La ricchezza $W=(\tilde y^A+\tilde y^B)/2$ vale $1$, $1{,}5$, $1{,}5$, $2$ con probabilità $\tfrac14$ ciascuno, e $E[1/W]=\tfrac14\big(1+\tfrac23+\tfrac23+\tfrac12\big)=\tfrac{17}{24}$. La FOC del titolo $A$, $E[(\tilde y^A-P)/W]=0$, dà
>
> $$P=\frac{E[\tilde y^A/W]}{E[1/W]}=\frac{1}{17/24}=\frac{24}{17}\approx1{,}4118,$$
>
> perché $E[\tilde y^A/W]=\tfrac14\big(1+\tfrac23+\tfrac43+1\big)=1$. Il prezzo sale da $\tfrac43$ a $\tfrac{24}{17}$. Il premio al rischio di mercato è
>
> $$\phi=\frac{E[\tilde y^A]}{P}-1=\frac32\cdot\frac{17}{24}-1=\frac1{16}=0{,}0625,$$
>
> la metà di quello senza integrazione, $\tfrac18$. La covarianza con il kernel passa da $-\tfrac16\approx-0{,}1667$ senza integrazione a $\mathrm{Cov}(\tilde y^A,\tilde M)=-\tfrac3{34}\approx-0{,}0882$ con il kernel dell'integrazione. Le due FOC sono nulle in $\alpha^A=\alpha^B=\tfrac12$.

## Titoli multipli

### Il modello con $n$ titoli

Si torna a un solo agente rappresentativo e si suppone che ci siano $n$ titoli rischiosi, ciascuno con quota totale pari a 1. I prezzi oggi e i valori domani sono $P_i$ e $\tilde y_i$, per $i=1,\dots,n$. Il prezzo corrente e il valore futuro del portafoglio di mercato, cioè dell'insieme di tutti i titoli, sono

$$P=\sum_{i=1}^nP_i,\qquad\tilde y=\sum_{i=1}^n\tilde y_i.$$

Le lettere $P$ e $\tilde y$ sono quelle del titolo singolo, e il caso $n=1$ è il modello base.

L'agente parte con una quota di ciascun titolo, per una ricchezza iniziale $P$, e sceglie le quote $\alpha_i$ da tenere. Per ogni titolo, la somma $(1-\alpha_i)P_i$ ricavata dalla vendita delle quote cedute rende $R_f$ per euro. Il problema è

$$\max_{\{\alpha_i\}}\ E\Big[u\Big(\sum_{i=1}^n\big[\alpha_i\tilde y_i+(1-\alpha_i)R_fP_i\big]\Big)\Big].$$

Ogni $\alpha_i$ compare linearmente nella ricchezza finale con coefficiente $\tilde y_i-R_fP_i$. Le $n$ FOC valgono insieme, e per ogni $i$

$$E\Big[(\tilde y_i-R_fP_i)\,u'\Big(\sum_{j=1}^n\big[\alpha_j\tilde y_j+(1-\alpha_j)R_fP_j\big]\Big)\Big]=0,$$

con la stessa $u'$, valutata sulla ricchezza totale, in tutte le equazioni.

Per la stessa ragione del titolo singolo ($u''<0$ e argomento lineare nelle quote) l'obiettivo è concavo nel vettore $(\alpha_i)$. Per ogni vettore $z=(z_1,\dots,z_n)\neq0$ la forma quadratica delle derivate seconde è $E\big[\big(\sum_iz_i(\tilde y_i-R_fP_i)\big)^2u''(W)\big]$, dove $W$ è la ricchezza finale. È negativa se la combinazione $\sum_iz_i(\tilde y_i-R_fP_i)$ non è quasi certamente nulla. Basta che nessuna combinazione non nulla dei valori, $\sum_iz_i\tilde y_i$, sia quasi certamente costante, cioè che la matrice delle covarianze dei $\tilde y_i$ sia invertibile: è il senso in cui i titoli non sono perfettamente collineari, e non basta che non lo sia nessuna coppia. Per la concavità le $n$ FOC sono già sufficienti; sotto questa ipotesi la soluzione, se esiste, è anche unica. L'offerta di ciascun titolo è 1: l'equilibrio di mercato implica $\alpha_i=1$ per ogni $i$. La ricchezza dell'agente è allora il valore del portafoglio di mercato, $\tilde y=\sum_i\tilde y_i$, ed è questo il consumo di cui il kernel misura l'utilità marginale.

### Il premio al rischio di mercato di ciascun titolo

Il rendimento lordo stocastico del titolo $i$ è $\tilde R_i=\tilde y_i/P_i$.

> [!tip] Teorema
> Sia $u'>0$ e siano $P_i>0$ i prezzi di equilibrio con $n$ titoli, ai quali la quota ottima è $\alpha_i=1$ per ogni $i$. Con $\tilde M=u'(\tilde y)/E[u'(\tilde y)]$ e $\tilde y=\sum_i\tilde y_i$ valgono, per ogni $i$,
>
> $$R_f=E\big[\tilde R_i\,\tilde M\big],\qquad E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M).$$

> [!note] Dimostrazione
> Con $\alpha_i=1$ per ogni $i$ la FOC del titolo $i$ è $E[(\tilde y_i-R_fP_i)\,u'(\tilde y)]=0$, che equivale a $E[\tilde y_i\,u'(\tilde y)]=R_fP_i\,E[u'(\tilde y)]$. Si divide per $P_i\,E[u'(\tilde y)]>0$:
>
> $$E\Big[\frac{\tilde y_i}{P_i}\,\frac{u'(\tilde y)}{E[u'(\tilde y)]}\Big]=R_f,\qquad\text{ossia}\qquad E[\tilde R_i\,\tilde M]=R_f.$$
>
> Poi, per la seconda forma della covarianza e con $E[\tilde M]=1$,
>
> $$R_f=E[\tilde R_i\tilde M]=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i]\,E[\tilde M]=\mathrm{Cov}(\tilde R_i,\tilde M)+E[\tilde R_i],$$
>
> da cui $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)$.

Per $n=1$ la prima relazione è la condizione di equilibrio dell'offerta nel caso del titolo singolo. Il premio al rischio di mercato del titolo $i$, $E[\tilde R_i]-R_f$, è positivo se e solo se il rendimento del titolo è correlato negativamente con il pricing kernel. Ci si può chiedere se, in modo equivalente, il premio al rischio di mercato sia positivo quando il rendimento è correlato positivamente con il valore $\tilde y$ del portafoglio di mercato.

L'equivalenza non vale in generale. Se $\tilde R_i$ è una funzione non decrescente di $\tilde y$, allora $\mathrm{Cov}(\tilde R_i,\tilde y)\ge0$ e, poiché $\tilde M$ è una funzione decrescente di $\tilde y$, $\mathrm{Cov}(\tilde R_i,\tilde M)\le0$: è il ragionamento che dà il segno di $\phi$, con la copia indipendente $\tilde y'$ e due funzioni di $\tilde y$ di monotonia opposta. Per un'utilità quadratica $\tilde M$ è lineare e decrescente in $\tilde y$: le due covarianze hanno segno opposto, o sono entrambe nulle. Negli altri casi il segno che conta è quello della covarianza con $\tilde M$, come mostra l'esempio seguente.

> [!example] Esempio
> Sia $R_f=1$, sia $\tilde y$ uguale a $1$, $2$, $3$ con probabilità $\tfrac13$ ciascuno, e sia $u'(W)=W^{-2}$, la CRRA con $\gamma=2$. Il kernel è $\tilde M=(108;27;12)/49$ nei tre stati. Un titolo del mercato ha valore domani proporzionale a $(2;0;3)$, con una costante di proporzionalità non superiore a $\tfrac12$ perché gli altri titoli abbiano valore non negativo. Il suo prezzo è $P_i=E[\tilde y_i\tilde M]/R_f$ e il rendimento lordo è $\tilde R_i=(\tfrac76;0;\tfrac74)$ nei tre stati, con $E[\tilde R_i]=\tfrac{35}{36}$, qualunque sia la costante. Si ha $\mathrm{Cov}(\tilde R_i,\tilde y)=\tfrac7{36}>0$, mentre $\mathrm{Cov}(\tilde R_i,\tilde M)=\tfrac1{36}>0$. Il titolo è correlato positivamente con $\tilde y$ ma anche con il kernel, e il suo premio al rischio di mercato è $E[\tilde R_i]-R_f=-\mathrm{Cov}(\tilde R_i,\tilde M)=-\tfrac1{36}$, negativo.

Un titolo il cui rendimento non è correlato con il kernel ha $E[\tilde R_i]=R_f$: anche se è rischioso, non paga un premio al rischio di mercato. È il caso di un titolo il cui valore è indipendente da $\tilde y$, perché $\tilde M$ è funzione di $\tilde y$: il rischio idiosincratico non è prezzato.
