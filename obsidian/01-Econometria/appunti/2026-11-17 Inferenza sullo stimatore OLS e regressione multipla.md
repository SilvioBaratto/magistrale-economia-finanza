---
corso: Econometria
data: 2026-11-17
fonte: Audio/econometria/econometria_2026-11-17.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-17
---

# Inferenza sullo stimatore OLS e regressione multipla

## Ripasso: esogeneità, consistenza e distorsione

Il modello di regressione semplice è una versione semplificata, ma studiarne bene i dettagli permette di lavorare più velocemente con modelli più complicati: molti concetti restano gli stessi e cambiano solo in alcune differenze. La lezione precedente partiva da un modello di regressione di cui si vogliono stimare i parametri. La stima ha senso solo se il termine d'errore è incorrelato con il regressore, condizione detta di esogeneità. Sotto esogeneità si può sperare che le stime dei parametri siano corrette. Quando la condizione non vale, la correlazione tra $x$ ed $\varepsilon$ si trasferisce nello stimatore e le sue proprietà non sono più accettabili: in media lo stimatore non è uguale al vero valore del parametro e, anche con un numero molto grande di osservazioni, la stima converge al vero valore più un'altra quantità.

Sotto l'ipotesi di esogeneità la lezione precedente ha dato due risultati. Il primo: in media lo stimatore è uguale al vero valore del parametro. Il secondo riguarda la varianza dello stimatore, che si scrive

$$\mathrm{Var}(\hat\beta)=\frac{\sigma^2}{\sum_{i}(x_i-\bar{x})^2},$$

dove $\sigma^2$ è la varianza del termine d'errore. Il denominatore è sostanzialmente la varianza campionaria di $x$. Se $n$ cresce, per la legge dei grandi numeri la varianza campionaria converge alla varianza di $x$ nella popolazione, che è una costante, assumendo che i momenti esistano finiti almeno fino all'ordine due. La varianza dello stimatore ha quindi la forma $1/n$ moltiplicato per una costante che dipende dalla varianza del termine d'errore, e converge a zero.

Che la varianza tenda a zero significa che, con campioni sufficientemente grandi, qualsiasi campione si ottenga non darà una stima numericamente molto diversa da $\beta$. Una varianza molto piccola indica che le osservazioni di una variabile casuale sono concentrate attorno alla media; qui la distanza media tra lo stimatore e il vero valore del parametro è un numero piccolo. Poiché lo stimatore è in media uguale a $\beta$, la stima ottenuta sarà quasi certamente vicina al vero valore di $\beta$, e la differenza tra il valore stimato e quello vero non può essere grande. Questa proprietà si chiama consistenza, cioè la convergenza dello stimatore.

> [!question] Da verificare: dopo "la varianza dello stimatore" la trascrizione riporta una frase non leggibile sulle variabili $x$ ("non posso usare le variabili x uguali a così, però posso usare le normali"); una locuzione ("il fatto della mia decisione economica") riferita al parametro da stimare non è ricostruibile e non è riportata.

### Il caso endogeno

Con endogeneità lo stimatore in media è uguale a $\beta+\delta$, dove $\delta$ è un numero, qui negativo. Il docente lo illustra su un asse che rappresenta tutte le stime ottenibili applicando i minimi quadrati o il metodo dei momenti: su di esso si segnano il vero valore del parametro e il punto $\beta+\delta$. Le stime, calcolate su campioni diversi, risultano centrate intorno a $\beta+\delta$ e non intorno a $\beta$.

Se $n$ cresce, la distribuzione dello stimatore tende a concentrarsi intorno alla propria media, ma la sua media è $\beta+\delta$. In un modello endogeno, quindi sbagliato, lo stimatore collassa su quel punto, e più osservazioni si hanno più si schiaccia esattamente lì. Per $n$ che tende all'infinito lo stimatore è una variabile casuale concentrata su quella media: molto preciso, ma nello stimare il valore sbagliato. Si tratta di una distorsione sistematica, e in questo caso si parla di non consistenza. Questo riprende quanto visto la volta precedente.

> [!question] Da verificare: nella trascrizione le espressioni "sotto ipotesi di ..." (due volte) e "eterogeneità" (nel paragrafo sulla retta stimata) sono probabilmente "endogeneità", ma il termine è lacunoso o deformato.

### Dalla retta stimata alla retta di regressione

Il docente segnala di aver messo online, tra la sera precedente e la mattina, due aggiunte in fondo ai materiali, cioè i risultati sulla legge delle aspettative iterate, da guardare se interessano, e una versione degli appunti con i grafici rifatti e alcune incoerenze di notazione sistemate. La versione è più definitiva e coerente; non cambia molto, ma alcuni punti sono spiegati in modo più chiaro.

Lo scopo finale del modello di regressione è stimare la retta di regressione, il tratteggio nel grafico, sulla base di un campione, i punti neri. Stimando il modello, la retta viene adattata ai dati e si ottiene qualcosa che non coincide necessariamente con la retta tratteggiata verde: questa è il vero modello, l'altra è quella stimata. Si cerca di stimare il modello valido per la popolazione, ma la popolazione non è disponibile e ci si basa sul campione. I parametri stimati sul campione identificano una retta con una certa pendenza e una certa intercetta, cioè l'intersezione con l'asse delle $y$. Le due rette sono diverse, e trovare il vero valore del parametro è impossibile.

Aumentando il numero di osservazioni, i pallini grigi nel grafico, l'evidenza sulla popolazione diventa più chiara. Se il modello è esatto e il regressore è esogeno, gli stimatori di $\alpha$ e di $\beta$ convergono ai veri valori dei parametri e la retta stimata converge al vero modello, che si spera sia il modello causale. Se invece il regressore è endogeno, la retta stimata non converge mai al vero modello.

## Il teorema di Gauss-Markov

Il docente premette che questo risultato non è particolarmente importante, ma compare su tutti i libri di testo. La domanda di partenza è se i minimi quadrati siano una buona strategia per stimare i parametri, cioè per sfruttare al meglio il contenuto informativo delle osservazioni. Esistono molti modi per stimare i parametri di un modello. Tutti usano i minimi quadrati perché, sotto certe condizioni, sono il modo più preciso di mettere insieme le informazioni: forniscono formule con la variabilità più piccola possibile, cioè la varianza dello stimatore più piccola. Il teorema di Gauss-Markov dà un risultato in questa direzione.

Le condizioni sono le seguenti.

- Il modello è lineare nei parametri, non nelle variabili.
- Le osservazioni sono estratte dalla popolazione con campionamento casuale semplice. Le osservazioni sono indipendenti, ma non nel senso che $X$ sia indipendente da $Y$ (altrimenti non ci sarebbe nulla da studiare): sono indipendenti tra loro le coppie $(X,Y)$ relative ai singoli individui del campione.
- Vale l'ipotesi di esogeneità.
- Vale l'ipotesi di omoschedasticità, che qui è strettamente necessaria.

Sotto queste condizioni lo stimatore dei minimi quadrati (OLS) è il migliore: ha la varianza più piccola tra tutti gli stimatori lineari e non distorti. Uno stimatore è lineare quando la sua formula si può scrivere come una sommatoria. Tra gli stimatori non distorti, cioè quelli che in media colgono il vero valore, lo stimatore OLS è quello con varianza più piccola. La formula OLS garantisce quindi l'efficienza maggiore nell'uso delle informazioni osservate.

Il docente dichiara che questo risultato non gli piace molto, pur avendo una sua importanza. Le ragioni sono due. Le ipotesi richieste nella realtà non sono quasi mai verificate. Inoltre, in statistica non è detto che gli stimatori non distorti siano i più interessanti. Se si sa quanto vale la distorsione, per esempio 0,5, si può sottrarla allo stimatore distorto e ottenere uno stimatore alternativo del parametro. In generale, se si può ritenere che la distorsione sia abbastanza piccola e che il guadagno in precisione sia molto più grande, si può decidere di usare uno stimatore con caratteristiche diverse. Il docente non sostiene che sia la scelta migliore, ma osserva che la non distorsione è comunque una costrizione, un vincolo.

Considerati tutti gli stimatori scrivibili come sommatoria (lo stimatore dei minimi quadrati è un rapporto di sommatorie) e, tra questi, i non distorti, il più preciso, cioè quello con la varianza più piccola, è lo stimatore dei minimi quadrati. Per questo teorema è chiave, oltre all'esogeneità, l'ipotesi di omoschedasticità: la varianza condizionale del termine d'errore è costante rispetto a $x$.

> [!question] Da verificare: la trascrizione riporta "omogeneità" accanto a "omoschedasticità"; probabilmente "esogeneità".

Il docente enuncia il risultato senza dimostrarlo, perché la dimostrazione è piuttosto complicata. Il meccanismo è però lo stesso della media aritmetica in statistica.

## Distribuzione dello stimatore in campioni finiti e asintotica

Oltre alla media e alla varianza dello stimatore, interessa conoscerne la distribuzione di probabilità. Lo stimatore è una variabile casuale che raccoglie tutte le stime ottenibili da campioni diversi, quindi una sequenza di numeri, ciascuno con una sua probabilità. Se si potessero avere tutti i campioni, si calcolerebbe lo stimatore per ciascuno e se ne costruirebbe l'istogramma, cioè la distribuzione di probabilità.

Si distinguono due approcci. Nel primo si studia la distribuzione dello stimatore con il numero di osservazioni fissato: 20, 35, 47, 100, 10.000. Nel secondo si studia che cosa succede allo stimatore se il numero di osservazioni diverge, cioè se i campioni sono abbastanza grandi da approssimare bene la popolazione. Al docente interessa di più il secondo aspetto. Il primo non è particolarmente interessante, anche perché la maggior parte dei risultati dimostrabili in campioni finiti richiede ipotesi aggiuntive, tra cui che il termine d'errore non sia solo incorrelato con $X$, ma anche gaussiano.

> [!question] Da verificare: la trascrizione dice "il campione infinito non è particolarmente interessante"; dal contesto (il motivo addotto riguarda i campioni finiti) si legge "campione finito".

### Campione finito con errore gaussiano

Con $n$ fissato, per dimostrare le proprietà della distribuzione dello stimatore $\hat\beta$ si assume che il termine d'errore sia gaussiano con media zero e varianza $\sigma^2$, dove $\sigma^2$ è un parametro che per ora si suppone noto. Sotto queste ipotesi si dimostra analiticamente che il rapporto

$$\frac{\hat\beta-\beta}{\sqrt{\mathrm{Var}(\hat\beta)}}$$

ha media zero e varianza uno. Riscalando per la media e per la varianza, lo stimatore si distribuisce come una normale con media pari al vero valore del parametro (lo stimatore è non distorto) e con una varianza che si può calcolare.

Le ipotesi importanti sono due: la varianza $\sigma^2$ è nota, ed $\varepsilon$ è gaussiano oltre che incorrelato con $x$. Nessuna delle due è facile da soddisfare. La prima difficoltà è che $\varepsilon$ non è osservato, quindi non si può dire che sia gaussiano: è un'ipotesi di convenienza, che non è detto valga. Ogni ipotesi andrebbe in teoria validata, ma validarla senza avere le osservazioni è difficile, ed è per questo che il docente preferisce in generale non farla. Anche sapere che $\sigma^2$ sia noto è difficile. Tipicamente lo è in applicazioni di fisica o chimica, dove $\sigma^2$ rappresenta il livello di precisione dello strumento di misura: se il macchinario è preciso a $10^{-5}$ millimetri (il valore è fatto a titolo di esempio), questo descrive come i dati si distribuiscono intorno alla media. Nelle scienze sociali l'ipotesi non è proponibile: non si può dire quale sia la dispersione delle osservazioni rispetto alla media quando le osservazioni sono salari, età e simili.

Il risultato è quindi gradevole, perché permette di costruire l'istogramma degli stimatori con la forma a campana, ma nella vita reale l'ipotesi è insostenibile per i due motivi detti: non si sa se $\varepsilon$ sia gaussiano e non si conosce $\sigma^2$.

> [!question] Da verificare: la trascrizione dice "non so qual è la media", ma nel contesto si tratta probabilmente di $\sigma^2$.

### Varianza stimata e distribuzione t di Student

Se si indeboliscono le condizioni, mantenendo $\varepsilon$ gaussiano ma stimando $\sigma^2$ (cosa che si fa facilmente), il rapporto si distribuisce come una variabile casuale t di Student con $n-2$ gradi di libertà, dove $n$ è il numero di osservazioni. Con 635 osservazioni si ha una t di Student con 633 gradi di libertà. I gradi di libertà controllano la varianza della distribuzione.

L'unica differenza rispetto al caso precedente è che il denominatore va stimato. Nel caso a $\sigma^2$ noto il denominatore usa la varianza campionaria di $x$; se $\sigma^2$ va stimato, la distribuzione non è più normale ma t di Student. Il problema non è serio, perché la t di Student è di fatto sovrapponibile alla gaussiana per un numero di gradi di libertà superiore a circa 30. Se $n-2$ è maggiore di 30, le due distribuzioni sono indistinguibili.

Dal punto di vista operativo, con un campione più grande di 30-35 osservazioni si può usare l'approssimazione normale. Con meno di 30 osservazioni i risultati non sono comunque affidabili, perché tra un campione piccolo e l'altro la variabilità campionaria è troppo alta: tanto vale far finta che la distribuzione sia normale, scegliendo la strada facile. L'approssimazione normale è inoltre giustificata dalla teoria asintotica, che studia che cosa succede quando il numero di osservazioni cresce anziché essere fissato.

### Distribuzione asintotica

Se $n$ tende all'infinito, si dimostra che la deviazione dello stimatore dal vero valore del parametro, moltiplicata per $\sqrt{n}$, converge a una normale con media zero e una varianza detta varianza asintotica. La sua formula si può calcolare ed è funzione di $x$ e di $\sigma^2$. Se $n$ è sufficientemente grande, quindi, lo stimatore si distribuisce come una normale con media $\beta$ e con quella varianza.

> [!question] Da verificare: la trascrizione dice "moltiplicata per il numero di unità campionarie"; il fattore standard è $\sqrt{n}$, ma il testo non lo dice.

In un campione reale il numero di osservazioni è noto, quindi la teoria asintotica si usa come approssimazione con $n$ finito. Con 100 osservazioni, per esempio, si calcola il numeratore della varianza asintotica, lo si divide per 100 e si ottiene un'approssimazione della distribuzione dello stimatore, basata sulla teoria asintotica: una normale con media $\beta$ e un certo numero come varianza. Se il campione è molto grande, quel numero è molto piccolo e lo stimatore converge al vero valore del parametro. Lo si sapeva già, perché valgono i risultati sulla varianza che collassa a zero.

Con $n$ sufficientemente grande si applicano la legge dei grandi numeri e il teorema centrale del limite, e si dimostra che la distanza tra lo stimatore e il vero parametro è gaussiana. Per ottenere una distribuzione di probabilità non degenere occorre però moltiplicare per $\sqrt{n}$. Senza questo fattore, poiché la varianza dello stimatore collassa a zero, lo stimatore converge a una variabile casuale degenere: per $n$ che tende all'infinito, $\hat\beta$ è uguale a $\beta$ con probabilità 1 e diverso da $\beta$ con probabilità 0. Il risultato è interessante, ma non permette di fare inferenza né di condurre test. Per i test occorre dare più peso al numeratore moltiplicandolo per $\sqrt{n}$, e questo è il teorema centrale del limite.

L'analisi della media aritmetica nel corso di statistica è esattamente la stessa cosa. Lo stimatore di $\beta$, e allo stesso modo quello di $\alpha$, si può scrivere come un rapporto di medie.

## Perché la distribuzione asintotica è normale

Il docente premette che la spiegazione è un po' all'acqua di rose. Data una sequenza di osservazioni indipendenti, si calcola la media aritmetica, si individua la media della popolazione e la varianza della media aritmetica; il teorema centrale del limite dice che la media standardizzata converge a una normale standard.

Nel modello di regressione si ha un numeratore e un denominatore. Il numeratore è composto da prodotti incrociati, cioè dalle osservazioni meno la loro media aritmetica, di $x$ e di $y$. Questi prodotti si possono indicare con $z_i$. Sono indipendenti tra loro, perché $x$ e $y$ sono pescati in modo indipendente rispetto all'individuo $i$ e il prodotto di quantità indipendenti resta indipendente. Il numeratore è quindi $1/n$ per la somma di questi oggetti, cioè la loro media, e vale il teorema del limite centrale. Perché valga, la varianza dei $z_i$ deve essere finita, quindi i momenti quarti di $x$ e di $y$ devono esistere. Non si può quindi usare una t di Student con tre gradi di libertà, ma una con cinque va già bene.

Il numeratore è dunque una media aritmetica e, opportunamente standardizzato, converge a una normale con media zero e varianza uno. Il denominatore converge in probabilità alla varianza di $x$, quindi a una costante. Se il numeratore converge a una normale e il denominatore a una costante, il rapporto è normale. Calcolando $\hat\beta$ meno il suo valore atteso, diviso per la sua variabilità, si ottiene un oggetto gaussiano con media zero e varianza uno, e di qui il risultato asintotico visto prima.

> [!question] Da verificare: la trascrizione motiva la varianza uno con "la variabilità di questo oggetto è compensata dalla variabilità del denominatore, uguali"; il passaggio non è ricostruibile dal parlato e si riporta solo la conclusione.

In sintesi: la formula dei minimi quadrati si scompone in numeratore e denominatore; si applica la legge dei grandi numeri al denominatore, che diventa una costante, e il teorema del limite centrale al numeratore, che diventa gaussiano. Riscalando e aggiungendo il fattore appropriato, $\hat\beta$ si distribuisce asintoticamente come una normale. Il docente non va oltre, perché il risultato dovrebbe essere già noto dal corso di statistica. Lo stimatore di $\beta$ si comporta come una media aritmetica, con la differenza che qui le medie sono due: la covarianza al numeratore e la varianza al denominatore. Per le ragioni dette convergono senza particolari problemi, almeno nel caso di un campione indipendente e identicamente distribuito. Di conseguenza, per $n$ sufficientemente grande, l'istogramma ottenuto da, per esempio, 10.000 campioni si approssima bene con una curva a campana con una certa media e una certa varianza.

### Il grafico delle distribuzioni al crescere di $n$

Il risultato è quello mostrato nel grafico visto in precedenza. Con poche osservazioni la distribuzione è irregolare, con code anche asimmetriche. Al crescere delle osservazioni si schiaccia intorno al vero valore del parametro, che è 3,2, e la forma è approssimata sempre meglio da una campana, cioè dalla distribuzione normale. Questi sono dati reali, frutto di calcoli su un campione estratto da una popolazione a disposizione del docente. Un secondo grafico è invece astratto: se $n$ è grande lo stimatore è ben approssimato da una curva gaussiana, se $n$ è piccolo l'approssimazione gaussiana non è garantita e la distribuzione può essere asimmetrica.

Ognuna delle curve disegnate ha sempre la stessa media $\beta$, ma non è necessariamente simmetrica. Media e moda possono essere diverse: nel grafico la moda è un punto e la media un altro. Più osservazioni si hanno, migliore è l'approssimazione data da una curva simmetrica a campana. È questa l'intuizione alla base della teoria asintotica.

Il docente non entra nelle derivazioni analitiche, perché sarebbe noioso e richiederebbe di definire altri concetti. Chi ha già visto questi risultati per la media riconosce la stessa cosa: nel modello di regressione la notazione è più complicata, ma il procedimento è identico.

## Dall'approssimazione normale al test di ipotesi

Conoscere la distribuzione di tutti i risultati ottenibili da un campione di dimensione sufficientemente grande permette di fare inferenza, cioè un test di ipotesi. Si può, per esempio, verificare se un valore di interesse per il parametro è coerente con le stime oppure no.

Il docente propone un esempio: la decisione di iscriversi alla magistrale, cioè di studiare due anni in più. Una persona potrebbe decidere di farlo se il guadagno atteso in termini di paga oraria è di almeno un euro in più (numeri a caso, precisa, sperando in un po' di più). La decisione è quindi: se studio due anni in più mi aspetto di guadagnare almeno un euro in più, altrimenti non vale la pena. Per validare un'ipotesi di questo tipo si deve fare un test di ipotesi.

Si lavora con un modello di regressione semplice, $y=\alpha+\beta x+\varepsilon$, e si suppone che la covarianza tra $x$ ed $\varepsilon$ sia zero, quindi che il modello si comporti bene e non ci siano problemi. Il modello permette di quantificare la variazione attesa di $y$ in corrispondenza di due anni di studio in più con la quantità mostrata nella slide. Questa è l'idea di "studio due anni in più": è $\beta$, il moltiplicatore della scelta economica.

> [!question] Da verificare: la trascrizione riporta "la covarianza tra x ed y sia uguale a zero", probabilmente la covarianza tra $x$ ed $\varepsilon$. La quantità che misura la variazione attesa di $y$ per due anni in più non è leggibile dal parlato, che la collega solo a $\beta$.

Si assume che non ci siano effetti collaterali.

> [!question] Da verificare: la trascrizione completa la frase con "cioè variazioni di y non abbiano nessuna rilevanza in media", che non è interpretabile con certezza.

Il problema è decidere, in modo coerente dal punto di vista statistico, se il guadagno salariale sia maggiore di un euro, che è quanto ci si aspetta di guadagnare in più studiando due anni in più. Un euro è la soglia minima per fare la magistrale: guadagnare dieci euro in più sarebbe ancora meglio. La condizione si verifica se $\beta$ è maggiore di un mezzo.

### Perché non basta confrontare la stima con la soglia

Una strategia sarebbe prendere un campione di dati, stimare $\beta$ e vedere se la stima è maggiore o minore di un mezzo. Potrebbe sembrare ragionevole, ma funziona poco, perché il $\beta$ stimato non è il vero valore della popolazione: è l'evidenza campionaria, cioè la pendenza della retta stimata, non quella della retta della popolazione, mentre la decisione va presa sul $\beta$ della popolazione. La stima può essere influenzata da una differenza campionaria, da un errore campionario che si spera piccolo ma che non si può quantificare. Non ci si può quindi basare sulla pendenza stimata: occorre tener conto che ciò che si stima è il vero valore più una componente di variabilità che dipende dai dati osservati, e che un campione diverso potrebbe dare un risultato diverso. Si vuole una decisione corretta dal punto di vista probabilistico, che tenga conto dell'incertezza con cui i parametri sono stimati. L'incertezza deriva dal fatto che si misura solo una parte della popolazione, il campione. Serve quindi un test.

## Il test di ipotesi

Il docente chiede se i test di ipotesi siano chiari o se serva un ripasso. Uno studente risponde che serve un ripasso.

Un test serve a decidere tra due ipotesi o condizioni. Una è l'ipotesi nulla, indicata di solito con $H_0$; l'altra è l'ipotesi alternativa, indicata con $H_1$ oppure $H_a$. Il docente non ricorda quale notazione abbia usato nelle slide, forse entrambe, ma è la stessa cosa.

> [!question] Da verificare: il docente aggiunge un richiamo alla logica formale (algebra di Boole, interruttori 0 e 1) per spiegare la numerazione delle ipotesi; la trascrizione è confusa e il passaggio non è riportato.

### Costruzione del sistema di ipotesi

Si vuole capire se i dati sono coerenti con l'ipotesi nulla. Si può porre sotto l'alternativa la condizione che interessa, cioè $\beta>1/2$: se i dati sono più coerenti con questa ipotesi, si farà la magistrale; se sono più coerenti con l'altra, si potrebbe scegliere di non farla. Definita l'alternativa, la nulla è la sua opposta: $\beta\le 1/2$. La nulla comprende quindi qualsiasi numero da un mezzo in giù.

Il caso più difficile da decidere è $\beta$ uguale a un mezzo contro $\beta$ maggiore di un mezzo, perché lì la distinzione è minima: un mezzo è il punto dell'insieme sotto la nulla più vicino all'alternativa. In generale, invece di scrivere la nulla come $\beta\le 1/2$, è equivalente scrivere $\beta=1/2$. Se si rifiutasse la nulla in questo caso, in cui i dati non sono coerenti con il $\beta$ più vicino all'alternativa, lo sarebbero ancora meno con un $\beta$ più piccolo. Un test di $\beta=1/4$ contro $\beta>1/2$, per esempio, rifiuterebbe la nulla ancora più nettamente. Si prende dunque il caso più complicato e si fissa $\beta$ a un mezzo: se la nulla è rifiutata in questo caso, lo è per qualsiasi $\beta$ minore di un mezzo. Anziché l'ipotesi composta, si usa la condizione più sfavorevole rispetto all'alternativa. Lo studente conferma che il passaggio è chiaro.

### La procedura di Neyman e Pearson

Nella procedura di Neyman e Pearson si ipotizza di credere ciecamente all'ipotesi nulla, e quindi che il vero valore del parametro sia un mezzo. Se allora si sottrae un mezzo allo stimatore e si divide per il livello di precisione della stima, cioè lo standard error di $\hat\beta$ (la radice quadrata della varianza), per la teoria asintotica il risultato deve essere una normale con media zero e varianza uno. Questa quantità si chiama $t$. Usando la teoria asintotica si potrebbe chiamare $z$, ma, osserva il docente, la lettera non è importante.

Sull'asse si riportano tutti i valori che la statistica $t$ può assumere se l'ipotesi nulla è corretta. Se si calcolassero 100.000 stimatori su 100.000 campioni diversi, togliendo un mezzo e dividendo per lo standard error, l'istogramma sarebbe ben approssimato dalla normale standard. Questa è la distribuzione della statistica $t$ sotto l'ipotesi nulla, centrata in zero.

Se invece fosse vera l'alternativa, $\beta$ sarebbe in media maggiore di un mezzo e la media del numeratore maggiore di zero. Se il vero $\beta$ fosse 5, la media del numeratore sarebbe 5 meno un mezzo. La distribuzione di probabilità sotto l'alternativa è quindi ancora normale, ma spostata a destra rispetto a quella sotto $H_0$.

### La regola decisionale

Le due curve rappresentano tutti i campioni ottenibili dalla popolazione, ma si dispone di un solo campione, usato per i calcoli. Si guarda dove cade sull'asse la statistica $t$ osservata, calcolata sui dati. Se cade nella parte dell'asse dove una delle due curve è più probabile, i dati sono più coerenti con l'ipotesi nulla; se cade nella parte in cui è più probabile l'altra curva, sono più coerenti con l'alternativa. Si può quindi definire una soglia, una barra verticale che divide l'asse in due parti: da un lato i dati sono coerenti con la nulla, dall'altro lo sono di più con l'alternativa.

Questa soglia non è ancora disponibile e va calcolata in modo razionale. Se la statistica osservata è molto lontana da un lato o dall'altro, la decisione è facile.

Se la statistica $t$ osservata cade in una zona in cui la curva sotto la nulla assegna probabilità zero, la decisione non si discute: vale l'alternativa. Se cade dalla parte opposta, la nulla è molto più probabile dell'alternativa, perché la probabilità assegnata dalla curva della nulla è molto più grande di quella dell'alternativa, anche se in assoluto resta piccola. La difficoltà è nella zona intermedia: tutto quel segmento è coerente sia con la nulla sia con l'alternativa, e lì la decisione diventa più difficile.

### Errore del primo tipo e livello di significatività

L'idea di Neyman e Pearson per costruire un test parte dal fatto che, prendendo una decisione statistica, un errore si può sempre fare. L'obiettivo è non sbagliare troppo spesso, cioè controllare la probabilità di sbagliare. Si costruisce quindi la soglia in modo che la probabilità di uno specifico errore sia fissata a un livello $\alpha$. Tipicamente $\alpha$ vale 1%, 5% o 10%; nelle applicazioni macroeconomiche anche di più, perché i dati sono pochi.

Si fissa la soglia in modo che la probabilità, sotto la curva della nulla, di superarla sia uguale ad $\alpha$. Questa probabilità è l'area evidenziata in giallo nel grafico. Se la statistica $t$ cade oltre la soglia, si rifiuta la nulla e si dice che è più probabile l'alternativa, ma la curva della nulla potrebbe essere comunque quella corretta. L'errore consiste quindi nel decidere a favore dell'alternativa quando i dati potrebbero essere coerenti con la nulla. Si chiama errore del primo tipo.

Si fissa comunque una soglia sapendo di poter sbagliare, perché un errore è inevitabile e perché, scegliendo la soglia in modo che l'area gialla valga $\alpha$, la probabilità di sbagliare in questo modo non può mai superare $\alpha$. Se $\alpha$ è abbastanza piccolo, questo tipo di errore non si commette di fatto.

Fissato $\alpha$, la soglia si legge sulla tavola della normale. Con $\alpha=2{,}5\%$ la soglia è 1,96: se la statistica $t$ è inferiore a 1,96 si decide per la nulla, altrimenti per l'alternativa. Con $\alpha=5\%$ la soglia è 1,64: sotto 1,64 la nulla, altrimenti l'alternativa. Si tratta, ovviamente, di un test unilaterale a destra.

### Errore del secondo tipo

Si possono fare due errori. L'errore del primo tipo è scegliere l'alternativa quando è vera la nulla. L'errore del secondo tipo è scegliere la nulla quando è vera l'alternativa. In statistica si fissa la probabilità del primo e di solito non si guarda il secondo, sperando che sia piccolo. La giustificazione "filosofica" di questa asimmetria è che gli errori hanno conseguenze diverse: alcuni sono gravi e altri meno. Il secondo tipo è considerato meno grave, il primo più grave.

Il docente ricorda l'esempio che gli fu fatto nel corso di statistica, l'incidente dello space shuttle esploso in volo subito dopo il lancio. Si sapeva che potevano esserci problemi, perché le condizioni climatiche potevano danneggiare le guarnizioni dei serbatoi. Col freddo le guarnizioni si ruppero e non isolarono più il serbatoio dal motore; il carburante finì sul motore, troppo caldo, e tutto esplose. La NASA doveva decidere se lanciare sapendo che c'era un problema o non lanciare e perdere i diritti televisivi. Se lancia e non succede nulla, la decisione è giusta. Gli errori sono due: lanciare e avere l'incidente, oppure non lanciare quando l'incidente non ci sarebbe stato e perdere la diretta televisiva, cioè i soldi. Quale sia l'errore grave si può discutere (il docente osserva di non sapere che cosa sia più importante, la vita umana o i soldi), ma in generale l'errore grave è l'esplosione e quello non grave la perdita dei diritti televisivi.

Con questo esempio si possono interpretare i due errori. L'errore del primo tipo è quello che si fissa, perché non si vuole sbagliare più di tanto in ciò che si considera più grave. L'errore del secondo tipo si può commettere, e si spera che sia il più piccolo possibile. Per chi vuole fare la statistica in modo rigoroso, la probabilità dell'errore del secondo tipo si chiama potenza. La potenza del test misura quanto la procedura sbaglia nell'altra direzione. Il docente dice di non averla mai capita bene e salta l'argomento.

> [!question] Da verificare: il docente identifica la potenza con la probabilità di errore del secondo tipo; di norma la potenza è il complemento a uno di tale probabilità.

Il richiamo ai test di ipotesi è così concluso. Si ha una regola, cioè una soglia che indica dove finisce la nulla e dove comincia l'alternativa, e resta solo da decidere la probabilità di errore. Una volta calcolata la statistica $t$ dalle stime del modello, si può prendere la decisione, sapendo che resta incerta.

### Il p-value

Esiste un altro modo per decidere se la statistica si trova a sinistra o a destra della soglia, il p-value. Che si sia molto lontani dalla soglia o molto vicini, purché dalla stessa parte, la decisione è sempre la stessa. Si vuole però anche un'idea di quanto si è vicini alla soglia, cioè una misura di quanto si è lontani dalla coda della distribuzione.

Se la statistica $t$ osservata è un certo valore, il p-value è la probabilità, sotto l'ipotesi nulla, di osservare una statistica $t$ che vada nella direzione dell'alternativa, cioè di osservare qualcosa che sia peggio, rispetto all'idea di ipotesi nulla, di quanto osservato. Nel grafico è l'area nera, calcolata sotto la curva della nulla. Poiché l'area gialla è fissata al 5%, se l'area nera è maggiore di $\alpha$ la statistica è automaticamente a sinistra della soglia; se è inferiore al 5%, è a destra. I due modi sono equivalenti.

Il p-value dice però quanto si è vicini alla soglia. Con $\alpha=5\%$ e un p-value del 5,1%, si è molto vicini al bordo e la decisione è incerta, perché basta osservare un numero un po' diverso nel calcolare le stime per cambiarla del tutto; in un caso simile occorre più cautela nelle affermazioni. Con un p-value del 75% ci si sente più tranquilli nel prendere la decisione. Il p-value dà quindi un'informazione in più.

Permette inoltre di fissare la probabilità a posteriori e non a priori. Per trovare la soglia occorre definire subito $\alpha$: con $\alpha=5\%$ la soglia è 1,64, con $\alpha=2{,}5\%$ è 1,96, e così via, e solo dopo si decide. Calcolando invece la probabilità di osservare qualcosa di più grande della statistica $t$ osservata, non occorre definire $\alpha$ in anticipo e si può scegliere dopo. La procedura è quindi piuttosto comoda. Per decidere se è più plausibile la nulla o l'alternativa si può usare la soglia oppure il p-value.

Il p-value è la probabilità, ipotizzando che la nulla sia vera, che la statistica $t$ sia maggiore o uguale alla statistica $t$ osservata, cioè quella calcolata sul campione. Se è maggiore di $\alpha$, non si rifiuta la nulla; se è minore di $\alpha$, la si rifiuta.

### Rifiutare e non rifiutare, mai accettare

In statistica le ipotesi si rifiutano o non si rifiutano, ma non si accettano mai. Accettare significherebbe dire che l'ipotesi è vera, mentre la decisione è presa sotto incertezza. Se il p-value è maggiore di $\alpha$, non si può essere sicuri che $\beta$ sia effettivamente minore o uguale al valore soglia; è più probabile che lo sia piuttosto che no, ma non si può affermare con certezza che sia quel valore. Una statistica osservata nella zona in cui il p-value è alto indica che i dati non permettono di rifiutare l'ipotesi nulla. Una statistica con p-value pari a zero indica che l'evidenza empirica permette di rifiutarla. Ma osservare una statistica nella prima zona non permette di accettare, cioè di dire che il parametro sia esattamente quel valore: questo non si sa mai. Si rifiuta o non si rifiuta.

> [!question] Da verificare: nel passaggio la trascrizione dice "minore o uguale di 1,5", mentre la soglia dell'esempio è un mezzo.

Questo è il test unilaterale a destra. Per decidere se un parametro soddisfa una condizione di questo tipo si può usare questa struttura.

### Test unilaterale a sinistra

Nel test unilaterale a sinistra si girano le distribuzioni e il p-value non si calcola più con $t$ maggiore o uguale alla $t$ osservata, ma con $t$ minore o uguale, perché si guarda la coda sinistra. Il docente osserva che questo test non è particolarmente interessante e che i richiami di statistica sulla pagina Moodle contengono tutti i casi.

Per un test di $H_0:\ \beta\ge 1/2$ contro $H_1:\ \beta<1/2$, il p-value è la probabilità, sotto la nulla, che la statistica $t$ sia minore o uguale alla $t$ osservata. Si guarda la coda sinistra perché la nulla ha media zero e l'alternativa si trova dalla parte sinistra, non da quella destra: basta girare tutto il resto.

## Test bilaterale

Il caso più standard in statistica è quello in cui non ci sono alternative unilaterali e si guardano entrambe le code contemporaneamente. Per esempio, $H_0:\ \beta=1/2$ contro $H_1:\ \beta\ne 1/2$. La nulla è sempre centrata in zero, mentre l'alternativa non si sa dove sia: si sa solo che non è centrata in zero, quindi può stare a sinistra o a destra: nel grafico ci sono due curve per l'alternativa, una a sinistra e una a destra, e una curva per la nulla, sempre sull'asse della statistica $t$. Se la statistica $t$ cade nelle code è più probabile l'alternativa; se cade al centro è più probabile la nulla.

Si definiscono due soglie, perché si può sbagliare da due parti, in modo che la probabilità complessiva di sbagliare sia $\alpha$. Poiché la distribuzione è simmetrica, si può dividere $\alpha$ a metà: due soglie tali che la probabilità di sbagliare a sinistra sia $\alpha/2$ e quella di sbagliare a destra sia $\alpha/2$. La somma è $\alpha$. Si divide così perché a priori non si sa da quale parte si possa sbagliare. Con $\alpha=5\%$ e la normale, le due soglie sono, dalle tavole, circa $-1{,}96$ e $+1{,}96$. Se la statistica $t$ cade tra le due soglie, la nulla è più probabile e i dati non sono in grado di rifiutarla. Se cade nelle code, i dati non sono coerenti con la nulla e quest'ultima si rifiuta.

### Il p-value bilaterale

Calcolare il p-value è più complicato, perché nel caso unilaterale era la probabilità di osservare qualcosa di più grande (o di più piccolo), mentre ora si deve considerare la probabilità di sbagliare da entrambi i lati. Aiuta il valore assoluto, familiare dalla matematica delle scuole medie, il cui grafico il docente affianca a quello di $t$. Si rifiuta la nulla per valori della statistica $t$ molto piccoli o molto grandi. Fissata, per esempio, una soglia superiore pari al valore assoluto della statistica osservata, i valori di $|t|$ oltre la soglia sono quelli per cui $t$ è molto grande oppure molto piccola. Guardando $|t|$ si considerano quindi le due code contemporaneamente, con un'unica operazione: se $|t|$ supera una soglia, si è in una delle due code.

Il p-value è la probabilità, sotto la nulla, che $|t|$ sia maggiore o uguale a $|t_{\text{oss}}|$, dove $t_{\text{oss}}$ è la statistica calcolata sul campione, cioè il parametro riscalato. Si conosce la distribuzione gaussiana di $t$ ma non quella di $|t|$; non serve, perché l'evento si scompone in due eventi disgiunti, uno per ciascuna coda:

$$P_{H_0}\big(t\le -|t_{\text{oss}}|\big)+P_{H_0}\big(t\ge |t_{\text{oss}}|\big).$$

Poiché gli eventi sono disgiunti, la probabilità della loro unione è la somma delle due probabilità. Poiché la normale è simmetrica rispetto a zero, i due addendi sono lo stesso numero, e il p-value è

$$2\,P_{H_0}\big(t\ge |t_{\text{oss}}|\big).$$

Nella scrittura alla lavagna il docente aveva dimenticato i valori assoluti e li ripristina: se la statistica osservata è $-3{,}5$, diventa $3{,}5$ e il segno meno si mette davanti, il che porta nel lato sinistro della distribuzione; l'altro termine descrive il lato destro. Il p-value si può calcolare in entrambi i modi. I pacchetti statistici lo calcolano in automatico, quindi non è un problema. Questo valore si chiama tipicamente p-value a due code.

Il docente conclude che questo era un richiamo del concetto di test di ipotesi.

Il docente chiede se il test di ipotesi sia ora più chiaro e ricordato meglio: è la stessa cosa vista in statistica, cioè una regola di decisione sotto incertezza. Si fissa la probabilità di sbagliare, si fissano le soglie e si decide se la statistica cade a sinistra o a destra. Si può evitare questa procedura con il p-value, oppure con uno strumento ancora più intuitivo, l'intervallo di confidenza.

## L'intervallo di confidenza

Lo scopo della statistica è stimare qualcosa. La stima è solo un'approssimazione di ciò che si vorrebbe conoscere, perché c'è incertezza dovuta all'uso di un campione al posto della popolazione. Insieme alla stima c'è quindi un grado di incertezza, che è la varianza dello stimatore. La stima da sola è troppo poco: si spera che l'errore sia piccolo, ma il numero ottenuto non sarà mai uguale al vero valore del parametro. Si costruisce allora un indicatore che tenga insieme la stima, cioè la migliore scommessa sul parametro di interesse, e il grado di incertezza.

L'intervallo di confidenza, senza entrare nel dettaglio, si costruisce così. La stima è il centro dell'intervallo, a cui si aggiunge e da cui si sottrae un margine d'errore che riflette l'incertezza sulla stima del parametro. Anziché riportare una stima si riporta un intervallo, con la migliore scommessa al centro. Il limite inferiore è il parametro stimato meno il margine d'errore, il limite superiore il parametro stimato più il margine d'errore. Il margine d'errore si ottiene dal percentile di livello $\alpha/2$ della distribuzione di interesse, che in questo corso è la normale, moltiplicato per il livello di imprecisione, cioè lo standard error.

> [!question] Da verificare: la trascrizione dice "più il livello di imprecisione"; la costruzione usuale è il prodotto tra il percentile e lo standard error.

Questo modo di procedere garantisce che il vero valore del parametro, che non si conosce, cada in un intervallo così costruito con probabilità pari a $1-\alpha$ e non ad $\alpha$ (il docente si corregge sul momento): una probabilità tipicamente alta. Se l'intervallo ha copertura del 95% e risulta, per esempio, tra 1 e 3,5, il vero valore del parametro cade con alta probabilità tra 1 e 3,5. Più piccolo è l'intervallo di confidenza, meglio è, perché il vero valore cade con alta probabilità in un intervallo sufficientemente piccolo.

### Che cosa significa "con alta probabilità"

Anche l'intervallo di confidenza è una specie di stimatore: definisce un limite inferiore e uno superiore, ciascuno dei quali è una variabile casuale, perché lo stimatore è una variabile casuale ed entra in entrambi i limiti. Si supponga di avere 100 campioni diversi, con dati diversi, e di calcolare per ciascuno l'intervallo di confidenza con la formula, che mette insieme la migliore scommessa sulla stima e il margine d'errore. Con un intervallo a livello 95% ci si aspetta che il vero valore del parametro cada nell'intervallo circa 95 volte e non vi cada circa 5 volte. Non significa che il vero valore cada sempre nell'intervallo, ma che cade con probabilità molto alta in un intervallo costruito in questo modo. Su 100 intervalli costruiti, 95 sono soddisfacenti; quando si calcola l'intervallo sui dati, cioè la realizzazione campionaria dell'intervallo, ci si aspetta che sia uno dei 95 piuttosto che uno dei 5. È quindi molto probabile che il vero parametro cada in un intervallo fatto così.

L'ampiezza dell'intervallo dipende dal valore di $z$ scelto. Un intervallo al 95% è quello che tutti guardano, ma se ne può considerare uno più stretto al 90% o uno più ampio al 99%. È un po' come per i test di ipotesi: l'intervallo di confidenza serve anche a decidere se un'ipotesi nulla o un'ipotesi alternativa siano credibili.

## Lettura di un output di regressione

Si considera l'output di un modello di regressione che mette in relazione i salari con il livello di istruzione. Una tabella di questo tipo riporta due numeri, la stima del coefficiente $\beta$, 0,54, espressa in centesimi perché il salario è misurato in centesimi di euro, e la costante. Lo standard error è la stima della varianza dello stimatore sotto radice quadrata: si prende la formula della varianza per un certo $n$ fissato, si stima $\sigma^2$ e si ottengono questi numeri. La stima è quindi accompagnata dal livello di precisione della stima.

Tipicamente tutti i software eseguono un test di ipotesi, con nulla "il parametro è uguale a zero" e alternativa "diverso da zero". Il motivo è che se il parametro è zero non c'è correlazione tra $x$ e $y$: $\beta$ misura la covarianza tra $x$ e $y$ divisa per la varianza di $x$, che è sempre positiva (strettamente positiva), quindi ciò che conta è la covarianza. Un coefficiente nullo significa che $x$ non permette di prevedere $y$. Anche in un modello causale la prima condizione è che le variabili siano correlate tra loro.

Viene quindi calcolata la statistica $t$ per verificare l'ipotesi nulla che il parametro sia zero e, automaticamente, il p-value sulle due code, quindi bilaterale, in cui si usa il valore assoluto. Nell'esempio il p-value del coefficiente è zero: l'ipotesi nulla è rifiutata, cioè il coefficiente è statisticamente diverso da zero. Il test e il p-value si ottengono direttamente dall'output.

Per la costante la statistica è molto piccola e lo standard error molto grande. Il p-value è circa il 18,7%, maggiore del 5%. Il numero non è quindi molto distante da zero dal punto di vista probabilistico: numericamente può esserlo, ma statisticamente è indistinguibile dallo zero. Non si riesce a rifiutare l'ipotesi che il parametro $\alpha$ sia uguale a zero, perché i dati non sono abbastanza informativi.

### Intervallo di confidenza nell'esempio

L'intervallo di confidenza è una formula che dà un limite inferiore e uno superiore, e indica approssimativamente dove ci si aspetta che cada il vero valore del parametro. Lo si calcola sia per $\beta$ sia per $\alpha$. Per $\beta$ l'intervallo va da 0,43 a 0,64: il vero valore del parametro è incluso con alta probabilità tra questi due numeri. In 95 casi su 100 ci si aspetta che il vero $\beta$ cada in un intervallo costruito così. Questo è l'unico intervallo disponibile e si spera sia uno dei 95 buoni e non di quelli che sbagliano. La migliore scommessa su $\beta$ è 0,54, ma siccome è fatta con un margine d'errore, il vero valore del parametro può ragionevolmente trovarsi tra 0,43 e 0,64.

Il docente pone infine la domanda: se si volesse verificare l'ipotesi che 0,5 sia il vero valore del parametro, cioè $\beta=0{,}5$, che cosa si potrebbe fare?

### Intervallo di confidenza e test sono equivalenti

Per verificare $\beta=0{,}5$ si può fare un test cambiando la statistica: non più $\hat\beta$ meno zero diviso lo standard error, ma $\hat\beta$ meno 0,5 diviso lo standard error. Oppure si guarda l'intervallo di confidenza e ci si chiede se 0,5 cada al suo interno. Se cade dentro, non si può escludere che sia il vero valore; se cade fuori, probabilmente 0,5 non è il vero valore del parametro.

Si dimostra (il docente salta la dimostrazione) che decidere con l'intervallo di confidenza è sostanzialmente equivalente a decidere con il sistema di ipotesi. L'intervallo dice dove deve stare il vero valore del parametro, il test guarda se la statistica sta fuori dall'intervallo. Con una distribuzione normale, l'intervallo di confidenza guarda il 95% centrale (la pancia) della distribuzione, il test di ipotesi guarda il 5% sulle code. Chi è sulle code non è sulla pancia e viceversa: se il vero valore cade dentro l'intervallo, non è di certo sulle code. In termini statistici, l'intervallo di confidenza e il test di ipotesi sono problemi duali l'uno dell'altro, e la decisione deve essere assolutamente la stessa, almeno per il test bilaterale.

Per verificare se il parametro è uguale a 0,5 o diverso da 0,5, senza usare il test classico, si calcola quindi l'intervallo di confidenza e si guarda se 0,5 ci cade dentro. Se ci cade, l'ipotesi nulla è credibile; se non ci cade, con alta probabilità non lo è. Ci sono dunque tre modi per decidere se un parametro è uguale a una certa costante: il test con le soglie, il p-value e l'intervallo di confidenza.

### Intervallo di confidenza e ipotesi con disuguaglianza

L'intervallo di confidenza serve anche per test con disuguaglianza. Si voglia verificare $H_0:\ \beta\le 0{,}5$. Se l'intervallo sta interamente sopra 0,5, tutti i valori plausibili del parametro sono maggiori di 0,5 e il vero valore non può essere minore, quindi l'ipotesi nulla è rifiutata. Se l'intervallo sta interamente sotto 0,5, il vero valore sarà sempre inferiore a 0,5, quale che sia la sua posizione precisa nell'intervallo. Il caso più scomodo è quello in cui 0,5 cade dentro l'intervallo: allora la nulla non può essere rifiutata, perché non si può escludere che il vero valore sia 0,5.

Al docente non dispiace usare gli intervalli di confidenza, perché rispetto al test danno un'intuizione geometrica di ciò che si sta facendo. Al computer ognuno può procedere come preferisce: il metodo che fa sbagliare di meno è quello giusto, e non ce n'è uno migliore o peggiore. Le decisioni sono equivalenti perché si basano sullo stesso problema: se si rifiuta la nulla non si rifiuta l'alternativa e viceversa. O si sta sulle code o si sta sulla fascia centrale della distribuzione, non su entrambe contemporaneamente.

> [!tip] Esame
> Un esercizio di questo tipo compare nel compito, quindi conviene prenderci mano. Per dubbi se ne può parlare con più calma in ufficio, durante l'esercitazione.

Il docente chiede se ci siano domande; non ne arrivano.

## L'R² come misura di bontà di adattamento

Il docente introduce un argomento che aveva detto non servire a niente, ma che gli serve per spiegare altri concetti in modo collaterale. Spesso, lavorando con modelli statistici, interessa sapere se il modello si adatta bene ai dati. Come visto la volta precedente, un modello che si adatta troppo bene al campione può essere un sintomo di overfitting, e non è necessariamente una cosa positiva. Può tuttavia essere utile capire il grado di bontà di adattamento della retta di regressione stimata alle osservazioni. L'indicatore usato di solito nel modello lineare è l'$R^2$.

I libri lo spiegano scomponendo la variabilità di $y$ in una parte di varianza spiegata dal modello e in una parte non spiegata; dopo una paginata di algebra noiosissima si ottiene un numero compreso tra 0 e 1. L'$R^2$ non è altro che la correlazione tra i valori predetti dal modello e i valori osservati, cioè quanto la previsione del modello è correlata con le osservazioni vere. Per costruzione è compreso tra 0 e 1; svolgendo i calcoli si ottiene la formula dei libri, che richiede appunto una lunga derivazione algebrica. Servirà in seguito per costruire test più complicati.

> [!question] Da verificare: il docente identifica l'$R^2$ con "la correlazione" tra valori predetti e osservati; poiché l'indicatore sta tra 0 e 1, si tratta presumibilmente del quadrato di tale correlazione.

### Perché l'R² non dice se un modello è corretto

Il docente non userebbe mai l'$R^2$ per dire se un modello sia corretto. L'indicatore dice soltanto come il modello si adatta ai dati; non dice come l'output del modello sia correlato con la realtà, di cui ciò che si osserva è solo una piccola parte, il campione. Non dice nulla neppure sulla relazione causa-effetto.

Lo mostra l'output del modello di regressione discusso come caso di endogeneità, in cui c'era una correlazione di 0,6 tra $X$ ed $Y$. Il modello di base non è sbagliato in sé, ma viene stimato in modo sbagliato, perché si finge di non vedere quel 0,6. Lo stimatore del coefficiente di interesse, il parametro di policy, è nettamente sbagliato: ciò che si stima non è 1,5, il vero valore, ma 1,5 più 0,6. L'$R^2$ di questo modello è tuttavia l'85%, altissimo. Il coefficiente di bontà di adattamento di un modello sbagliato è dunque grande: l'$R^2$ non dice se c'è endogeneità, che è lo scopo del corso.

> [!question] Da verificare: la trascrizione riporta "una correlazione pari a 0,6 tra X ed Y"; nel contesto dell'endogeneità è probabilmente la correlazione tra $X$ ed $\varepsilon$.

Il secondo modello, quello che lega salari e istruzione, non è detto che sia corretto né il migliore possibile, perché si potrebbero aggiungere altre informazioni, ma ha un senso logico, a differenza del precedente. Il suo $R^2$ è il 16%: la correlazione tra modello e dati è relativamente bassa. L'$R^2$ non dice quindi se un modello va bene o male: dice come il modello si adatta ai dati, e un buon adattamento non implica una relazione causale. È soltanto la correlazione tra i valori predetti dal modello nel campione e i valori osservati nel campione. Basta una varianza del termine d'errore molto piccola, con dati molto concentrati, per avere un $R^2$ molto grande, perché la retta si adatta, ma nulla di più.

> [!tip] Esame
> Se nel compito si scrive che un modello è migliore di un altro perché ha un $R^2$ più grande, la risposta non va bene. Il docente dichiara che non la prende bene e la prende "proprio sul personale".

## Legge delle aspettative iterate

Nei nuovi lucidi, come promesso, compare un risultato che non occorre sapere, ma che si usa spesso in econometria: la legge delle aspettative totali (detta poi, più in breve, legge delle aspettative). Afferma che la media delle medie condizionali è la media marginale. Se si calcola la media condizionale rispetto a un insieme informativo molto grande e poi la si media rispetto a un insieme molto piccolo, l'informazione aggiuntiva sparisce. La dimostrazione è in fondo ai lucidi e non serve guardarla: il risultato è presentato perché il docente lo cita ogni tanto.

> [!question] Da verificare: la trascrizione contiene una frase poco leggibile sull'origine dei lucidi ("è stato fatto proprio in sala da lucidi di un altro corso"), non riportata.

Con questo si chiude quanto il docente voleva dire sul modello di regressione semplice. Nella lezione precedente aveva finito dieci minuti prima, avendo letto male l'ora senza che gli studenti glielo dicessero; ora restano sei minuti e vengono usati. Non ci sono domande.

## Dal modello semplice alla regressione multipla

Poiché il modello di regressione semplice è stato sviluppato in modo abbastanza dettagliato, la regressione multipla si affronta più velocemente, per differenze. Anche per questa parte i lucidi sono stati modificati in mattinata: chi li ha scaricati il giorno prima può trovarli un po' diversi. Il docente ci sta ancora lavorando; la base è la stessa e alcuni punti sono migliorati.

Un modello con due variabili è troppo piccolo per ricavarne molto. Lo ha mostrato l'esempio della prima lezione, i bambini che vanno a scuola, con la performance in funzione della dimensione della classe: guardare solo due variabili era troppo poco. Aggiungendo il reddito, le conclusioni, ragionando logicamente, risultavano completamente diverse. Si vuole quindi costruire un modello con più informazioni disponibili, cioè più variabili, il che aiuta anche a specificare meglio un potenziale nesso causale tra le variabili.

### Dal modello semplice all'esempio con tre variabili

Nell'esempio le variabili in gioco sono tre: il reddito, la dimensione della classe e la performance. Il modello di regressione semplice, di cui si mostra l'output, dà la stima per una variazione unitaria della dimensione della classe: se la classe diminuisce di un'unità, il punteggio al test attitudinale aumenta in media di due punti. Il numero è statisticamente significativo, perché il p-value del test di significatività è diverso da zero, quindi c'è un miglioramento sistematico. L'intervallo di confidenza non include lo zero, e perciò il parametro è statisticamente diverso da zero; è sistematicamente negativo, perché l'intervallo assume solo valori negativi.

Il problema è che non si è sicuri che la relazione sia causale. La storia raccontata può avere senso, ma si vorrebbe includere nel modello l'effetto del reddito che, per quanto detto nelle lezioni precedenti, è legato sia alla dimensione della classe sia alla performance, in senso diverso. Occorre quindi un modello di regressione che incorpori questa informazione.

Per capire se il reddito fosse importante, nelle lezioni precedenti il campione era stato diviso in due gruppi, distretti ricchi e distretti poveri. Si calcolava la correlazione condizionale tra performance e dimensione della classe nei due sottocampioni, per vedere se la stima restasse più o meno stabile rispetto alla stima marginale. Uno schema di questo tipo, in cui il campione è diviso in sottostrati, si può incorporare facilmente in un modello di regressione con più variabili. Questo è il modello di regressione multipla.

## Il modello con due regressori

Si considera il caso con due regressori, quello dell'esempio. $Y$ è la performance, $X_1$ la dimensione della classe, $X_2$ il secondo regressore. Si ipotizza che il valore atteso condizionale, cioè il vero modello nella popolazione, dipenda da $\alpha$, $\beta_1$, $\beta_2$, $X_1$ e $X_2$. I parametri sono $\alpha$, l'intercetta, e $\beta_1$ e $\beta_2$, che misurano quanto conta $X_1$ e quanto conta $X_2$. Come nel modello semplice, per collegare l'osservazione del singolo distretto alla media condizionale si aggiunge un termine d'errore, che descrive come differiscono tra loro distretti con le stesse caratteristiche: caratteristiche dei distretti diverse dalla dimensione della classe e dal livello di reddito.

> [!question] Da verificare: la trascrizione dice "X2 è l'effetto rete", ma l'esempio prevede il reddito come secondo regressore.

### Che cosa sono $\beta_1$ e $\beta_2$

Nel modello di regressione semplice $\beta_1$ è una correlazione marginale tra $x$ e $y$, cioè la covarianza tra $x$ e $y$ divisa per la varianza di $x$. Nel modello con più variabili $\beta_1$ e $\beta_2$ sono ancora correlazioni, ma non marginali: sono correlazioni condizionali.

Il docente ripete l'esercizio già fatto: stabilire la performance attesa di $Y$ per due livelli della dimensione della classe, con il reddito fissato. Si tiene fisso il reddito, cioè si prendono distretti con lo stesso reddito, e si vede che cosa succede alla performance modificando una sola delle due variabili, la dimensione della classe. Se si riduce di un'unità la dimensione della classe, ma i distretti sono identici dal punto di vista del reddito, sostituendo nel modello di regressione i due valori e facendo la differenza, la variazione della performance attesa è data da una quantità semplice. Se si ipotizza che la componente residuale sia nulla, la variazione di performance è uguale a $\beta_1$ per la variazione della policy, cioè la riduzione di un'unità della dimensione della classe.

> [!question] Da verificare: la condizione sul residuo è resa nella trascrizione con "cioè varianza e eterogeneità", non interpretabile con certezza.

$\beta_1$ non dice quanto conti in generale ridurre di un'unità la dimensione della classe, ma quanto conti farlo in contesti in cui i distretti hanno lo stesso reddito. Non è più una correlazione tra $X$ e $Y$, ma una correlazione tra $X_1$ e $Y$ con $X_2$ fissato. Si confrontano distretti uguali, quindi la variazione di $Y$ non può dipendere dall'effetto reddito, perché quella quantità è fissa. L'esperimento consiste nel modificare la dimensione della classe solo tra distretti uguali. In un contesto in cui il modello è depurato dall'effetto reddito, la variazione in termini di performance è data dalla formula. A parità di reddito, una variazione $dx$ della dimensione avrà un impatto proporzionale a $\beta_1$.

La formula è la stessa del modello semplice, ma il concetto è diverso. Qui si ha una correlazione condizionale, tra $Y$ e $X_1$ con $X_2$ fissato; nel modello di regressione semplice $X_2$ non è fissato, perché non compare nel modello, e la correlazione è marginale. È esattamente ciò che si faceva nelle lezioni precedenti dividendo un campione grande in due parti, distretti ricchi e distretti poveri, e calcolando la correlazione nelle due parti: è questo che si fa nel modello di regressione.

La lezione continua con l'analisi di questo modello alla prossima lezione, mercoledì.
