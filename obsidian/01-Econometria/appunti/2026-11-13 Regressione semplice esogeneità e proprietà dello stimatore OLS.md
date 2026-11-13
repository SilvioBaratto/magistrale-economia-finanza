---
corso: Econometria
data: 2026-11-13
fonte: Materiali/audio/econometria/econometria_2026-11-13.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-13
---

# Regressione semplice: esogeneità e proprietà dello stimatore OLS

## Il modello di regressione semplice: richiamo e problema dell'identificazione

Il modello di regressione semplice è ipersemplificato, ma ciò che si vede su di esso si trasferisce direttamente ai modelli più complessi, con il vantaggio che l'algebra è più semplice. Dalla lezione precedente: il modello di regressione è il valore atteso della variabile dipendente condizionato a $X$. Il modello più semplice con un minimo di senso logico è la retta, e si ipotizza che il valore atteso condizionato abbia questa forma.

Il valore atteso condizionato va inteso sulla distribuzione di probabilità congiunta della popolazione, non sul campione. La media è calcolata su tutti i possibili lavoratori, nell'esempio di salari e livello di istruzione, e non solo su quelli osservati. È quindi il modello teorico che regola la relazione tra i dati, in generale ignoto, che si decide di approssimare con una retta. L'ipotesi che la retta sia adeguata è molto forte ed è legata all'ipotesi di esogeneità. Se l'approssimazione non è corretta si entra nell'ambito dell'endogeneità, con i problemi descritti nella lezione precedente.

Per collegare le osservazioni del campione al vero modello nella popolazione si aggiunge un termine d'errore $\varepsilon$. Esso descrive le caratteristiche individuali che differenziano persone con lo stesso valore di $X$: nel caso di istruzione e salario possono essere il genere, il tipo di studio o qualsiasi altro aspetto. Le definizioni sono quindi le seguenti: $Y$ è la variabile dipendente, $X$ il regressore, $\varepsilon$ il termine d'errore. L'errore è completamente casuale, non è osservabile e non lo sarà mai, e rappresenta tutte le caratteristiche dell'unità statistica $i$-esima del campione diverse da $X$.

### Perché serve l'incorrelazione tra X ed epsilon

Si vuole trovare una spiegazione delle variazioni della variabile dipendente: il salario rispetto agli anni di studio, il livello dei consumi rispetto a una politica economica che dà più soldi ai lavoratori, oppure, aumentando i controlli fiscali, la riduzione del sommerso in un certo paese. Il parametro $\beta$ rappresenta l'impatto della politica. Lo si identifica esattamente solo se si può escludere che a una variazione di $X$ corrisponda anche una variazione di $\varepsilon$. Altrimenti la variazione osservata della variabile dipendente dipende non solo dalla politica, ma anche da qualcosa fuori dal controllo di chi decide, perché $\varepsilon$ non è osservabile.

Per identificare l'impatto della decisione occorre quindi che la componente $\varepsilon$ resti fissa, cioè che la sua variazione sia nulla. Questo equivale a richiedere l'incorrelazione tra $X$ ed $\varepsilon$. L'ipotesi minima per identificare una relazione causa-effetto è dunque che il modello sia corretto, nel senso che la parte residuale sia completamente esogena, non collegata alla parte strutturale.

Se c'è correlazione, si osserva la variazione complessiva ma non si sa se dipenda dalla parte strutturale o da $\varepsilon$. Si può allora investire molto in una politica senza accorgersi che $\beta$ è in realtà uguale a zero e che tutta la variazione dipende dall'effetto collaterale: si spende per qualcosa che non serve, quando i fondi andrebbero usati per modificare il secondo fattore. Nel caso dei bambini a scuola, potrebbe convenire guardare al reddito delle famiglie piuttosto che alla dimensione della classe, e impiegare i due miliardi di dollari all'anno in sussidi alle persone a reddito basso. Il docente precisa di non sapere se sia la politica giusta; è solo un'illustrazione.

Una volta fissata a zero la variazione di $\varepsilon$, l'effetto marginale della politica è proporzionale al parametro $\beta$. Imporre variazione nulla di $\varepsilon$ significa assumere l'incorrelazione tra $X$ ed $\varepsilon$. Lo stimatore che sfrutta questa condizione, già visto nella lezione precedente, è la covarianza campionaria tra $X$ e $Y$ divisa per la varianza campionaria di $X$. Senza quell'ipotesi lo stimatore non è più ragionevole, perché stima sistematicamente una quantità diversa. I software si comportano come se la correlazione fosse nulla: se non lo è, il risultato differisce da quello che si vorrebbe ottenere. È il problema pratico.

### Esempio con dati simulati

Un esempio con dati simulati mostra l'effetto, perché si conoscono esattamente le variabili e la relazione tra esse. Si fissano la costante $\alpha = 3$ e il coefficiente angolare $\beta = 1{,}5$, si costruiscono $X$ e $Y$ al computer e si aggiunge un termine d'errore scelto di proposito in modo che sia correlato con $X$. In questo modello si sa quindi che la formula standard, covarianza diviso varianza, è sbagliata.

Le varianze sono poste tutte uguali a 1 per comodità, per cui la covarianza è anche la correlazione, e la correlazione tra $X$ ed errore è pari a 0,6, molto alta. Il processo che genera i dati (data generating process) è dato da queste due equazioni. Il dataset contiene 200 osservazioni simulate. Si applica il modello di regressione assumendo che la covarianza tra $X$ ed errore sia nulla, cioè stimando $\beta$ come covarianza tra $X$ e $Y$ divisa per la varianza di $X$.

La tabella dei risultati è stata prodotta con Gretl, il software usato nel corso. Tutte le tabelle di questo tipo hanno la stessa struttura, con piccole differenze. Alla riga `const` compare la stima dell'intercetta, il parametro $\alpha$: 2,96, contro il vero valore 3. L'intervallo di confidenza ha limite inferiore 2,83 e limite superiore 3,08. Il valore 3 vi è contenuto, quindi è plausibile come vero valore del parametro, e la costante risulta stimata abbastanza bene.

Il coefficiente $\beta$, che nella realtà vale 1,5, è stimato con 2,1. Se 2,1 sia vicino o lontano da 1,5 dipende dalla precisione dello stimatore. Il ragionamento è lo stesso della statistica di base, con un parametro al posto della media. Il significato dei numeri della tabella sarà spiegato più avanti.

### La distorsione non scompare con più dati

L'intervallo di confidenza di $\hat\beta$ indica che il vero valore del parametro dovrebbe cadere tra 2 e 2,25. Il valore 1,5 è fuori dall'intervallo: sulla base dei risultati è molto improbabile che sia il vero valore, ma a priori si sa che lo è. Dimenticare questo pezzo nella procedura di stima produce quindi una stima abbastanza diversa da quella che dovrebbe essere.

Inoltre 2,1 è esattamente 1,5 più 0,6. La distorsione non coincide in generale con la correlazione: qui il risultato è proprio quel numero perché la varianza di $X$ è uguale a 1, altrimenti si avrebbe un altro valore, ma sempre una distorsione. Ignorare l'endogeneità significa sbagliare completamente l'impatto della politica, perché ciò che si stima non è $\beta$ ma $\beta$ più un termine aggiuntivo, di cui in generale non si conosce l'entità: può essere 0,1 oppure 0,99. Non si sa quindi quanto la stima disti da quella desiderata.

Il secondo problema è che questa distorsione non sparisce all'aumentare dei dati. Dalla statistica si sa che più dati si usano, più la stima è precisa e più preciso è il procedimento inferenziale. Qui però la parte di distorsione non è comprimibile: con più dati si converge sempre più a 2,1 e non a 1,5, perché ciò che si stima è 1,5 più 0,6. Si è molto precisi nello sbagliare. La distorsione dell'esempio non scompare aumentando il campione, e né la legge dei grandi numeri né il teorema del limite centrale servono a rimediare. L'esempio mostra che cosa succede quando l'ipotesi di incorrelazione non è valida.

### Come ragionare sull'endogeneità

Nessuno dice se l'ipotesi di covarianza nulla sia valida. Non si può dimostrare, ma occorre ragionare per capire se è ragionevole. Un modo è chiedersi quando si presenti l'endogeneità, cioè quando $X$ ed $\varepsilon$ siano correlati. Come detto nella lezione precedente, un caso è il modello con troppe poche variabili: la media condizionale dipende da una sola variabile, mentre tutte le altre stanno dentro $\varepsilon$ e potrebbero essere legate a $X$. Ciò induce correlazione, quindi endogeneità e stime sistematicamente sbagliate.

Si può allora togliere informazione a $\varepsilon$ e inserirla nel modello, aggiungendo variabili alla media condizionale. Se il parametro associato alla variabile di interesse cambia di molto aggiungendo o no una variabile, nel modello con meno variabili c'è probabilmente un problema di variabile omessa, quindi di endogeneità. In una regressione si possono avere 100 parametri, ma si guardano solo i due o tre rilevanti per il problema economico; tutto il resto sono fattori di disturbo.

Conviene perciò individuare le potenziali cause di endogeneità e costruire una serie di modelli che verifichino se quei problemi sono presenti in quello usato. Se, aggiungendo variabili, il parametro di interesse non cambia più, probabilmente le variabili importanti sono state inserite tutte, perché nessun ulteriore modo di rendere neutrale il termine d'errore produce variazioni nella stima di $\beta$. Il docente avverte che sono regole del pollice e non un teorema. Il teorema dice che, se il modello ha troppe poche variabili, le stime sono sistematicamente sbagliate; empiricamente non è facile validarlo. Si continuano ad aggiungere variabili finché si può: se a un certo punto le stime si stabilizzano, non necessariamente allo stesso numero ma con gli stessi risultati dal punto di vista qualitativo, probabilmente il problema delle variabili omesse non c'è più. A quel punto si possono usare le formule standard di stima.

Quando si ignora il problema e si stima la regressione come se non esistesse, la stima del parametro è sistematicamente sbagliata: non si stima $\beta$ ma $\beta$ più un termine legato alla correlazione tra $X$ ed errore. Più avanti lo si dimostrerà formalmente; l'idea è questa.

> [!tip] Esame
> Il docente raccomanda di ricordare questa tabella dell'esempio, perché è più importante della derivazione teorica.

### Qualità del risultato ed endogeneità come problema economico

Per giudicare se un modello sia buono nella qualità dei risultati, e non nella parte statistica, la parte statistica è corretta: lo stimatore dei minimi quadrati, o del metodo dei momenti descritto nella lezione precedente, è la covarianza tra $X$ e $Y$ divisa per la varianza di $X$. Con endogeneità la qualità del risultato è bassissima. Con esogeneità la formula dà esattamente ciò che serve, cioè un effetto marginale, il parametro $\beta$. Se non ci fosse esogeneità, tutti i modelli stimati sarebbero da buttare.

Esogeneità ed endogeneità sono quindi un'ipotesi da fare: il modello considerato deve essere corretto dal punto di vista logico, cioè deve rappresentare una relazione causa-effetto. Ogni deviazione da questa condizione porta a risultati sistematicamente sbagliati, nel senso che $\beta$ non è più stimato correttamente. Occorre convincersi che il modello non sia influenzato dall'endogeneità. Se lo è, le soluzioni sono due: specificare diversamente il modello, oppure usare stimatori non standard, come le variabili strumentali, che non saranno trattate nel corso per mancanza di tempo.

Non si è mai sicuri della presenza o dell'assenza di endogeneità. Insieme al modello di interesse si stima una batteria di altri modelli e si fanno altri esercizi che permettano di escludere alcuni tipi di endogeneità. Una risposta definitiva non si avrà mai. Non basta stimare la regressione tra $X$ e $Y$: servono, per esempio, altre 50 regressioni per convincersi che non manchino variabili e che quelle usate siano misurate con una certa precisione. L'endogeneità non si può mai escludere, ma si lavora per ridurne la probabilità. Generalmente si valutano molti modelli per convincersi che quello adottato sia relativamente corretto.

Il docente ribadisce che l'endogeneità è un problema economico, non statistico. In un corso di statistica generalmente non interessa molto, e probabilmente non è stata vista nel modello di regressione, perché se l'obiettivo è prevedere $Y$ qualsiasi modello che funzioni va bene. In ambito economico interessa invece la misura del parametro, che in queste condizioni non funziona. La misura è interessante perché dice quanto vale la politica; altrimenti si rischia di prendere decisioni costose e sbagliate.

## Previsione, residuo e modello teorico contro modello statistico

L'esempio con dati simulati, in cui i parametri sono noti, mostra gli effetti dell'endogeneità. Si lascia ora da parte il problema e si assume di usare lo stimatore corretto di $\beta$, dato dalla formula già vista. Non ci si sofferma sulla stima di $\alpha$: l'intercetta non è un parametro particolarmente interessante, salvo applicazioni specifiche, e in generale si include nel modello a meno di ragioni molto forti per escluderla. Prima di chiedersi se la strategia di stima sia ragionevole, servono alcune definizioni.

### Valore predetto e residuo

Una volta stimati i parametri, il modello si usa per la previsione. Il valore predetto si calcola approssimando il valore atteso condizionale con i parametri stimati al posto di quelli veri, $\hat\alpha + \hat\beta x$, dove $x$ è un valore prefissato scelto da chi fa la previsione. Esso indica che cosa ci si aspetta dalla variabile dipendente quando $X$ assume quel valore. Per brevità lo si indica con $\hat y$ ed è la stima di un valore atteso condizionale. È una variabile casuale, perché $\alpha$ e $\beta$ sono incerti: si conoscono solo approssimazioni calcolate sul campione, non i veri parametri della popolazione.

Può essere utile anche misurare quanto la previsione si discosta dal valore effettivamente osservato, se noto. Questa differenza è il residuo, ossia il termine d'errore valutato per l'individuo $i$ osservato: la differenza tra il salario osservato e il salario previsto per un dato valore di $x$.

Il residuo è diverso dal termine d'errore. Il residuo è la distanza tra un'osservazione e la sua previsione, un'evidenza campionaria riferita a una persona specifica, ed è un numero. Il termine d'errore $\varepsilon$ è un concetto più astratto: è la distanza tra ogni individuo della popolazione, e non del campione, e il vero modello nella popolazione, ed è una variabile casuale. Il residuo non è un'approssimazione di $\varepsilon$; sono due concetti distinti, anche se il residuo ha una sua utilità. Nel grafico con la retta di regressione stimata e un'osservazione, il valore predetto è una distanza e la componente residuale è l'altra.

### Quando la strategia dei minimi quadrati funziona

Assumendo che il modello sia ragionevole, in condizioni di esogeneità, ci si chiede se usare covarianza divisa per varianza dia in media risultati corretti e che cosa accada quando il campione cresce. Si vuole sapere se la strategia statistica funziona, quando funziona e quando no, e soprattutto qual è il fattore che definisce l'endogeneità.

L'endogeneità nasce tipicamente perché il modello statistico stimato non corrisponde al modello che descrive i dati nella popolazione. In ogni analisi empirica si hanno in mente due concetti: ciò che si fa, cioè una scelta individuale, e il processo generatore dei dati, un concetto astratto per cui i dati sono legati ad altre variabili in modo predeterminato. C'è quindi un modello teorico che descrive la realtà e un modello empirico che è il modo in cui la si vede. Se i due modelli coincidono non c'è endogeneità; se divergono, può esserci. Il modello teorico spiega la relazione tra le variabili nella popolazione e non è noto. Il modello statistico è quello scelto da chi analizza, il comando da dare al software. Se il modello stimato è sbagliato rispetto al processo generatore dei dati si ricade nell'endogeneità, con problemi nella stima dei parametri di interesse.

Il problema chiave dell'econometria è capire se le formule usate per approssimare i parametri vadano bene. A questo scopo occorre conoscere le caratteristiche del termine d'errore, in particolare i suoi momenti condizionali rispetto a $X$.

### Il momento condizionale dell'errore

Il modello statistico è $Y = \alpha + \beta X + \varepsilon$, e si ipotizza che la media condizionale di $Y$ sia il modello di regressione, $\alpha + \beta X$. Si calcola il valore atteso condizionale di $Y$ dato $X$ sulla base di questo modello: fissato $X$, la media di $\alpha + \beta X + \varepsilon$ è $\alpha + \beta X + E[\varepsilon \mid X]$. Questa è la media condizionale rispetto alla distribuzione di probabilità nella popolazione, calcolata però a partire dal modello empirico. Essa coincide con $\alpha + \beta X$ se il modello è correttamente specificato, cioè se il modello statistico approssima correttamente la media condizionale. Ne segue che, se il modello teorico coincide con quello statistico, deve valere

$$E[\varepsilon \mid X] = 0.$$

> [!question] Da verificare: nella trascrizione il termine che si annulla compare come "y" ("la media condizionale di Y dato X deve essere uguale a zero"); dal ragionamento si tratta dell'errore $\varepsilon$, qui riportato di conseguenza.

Questo momento condizionale di una variabile casuale è legato all'esogeneità, presentata come covarianza nulla tra $X$ ed errore, ma è una condizione leggermente più forte. Una volta assunto che sia uguale a zero, si dimostra facilmente che la covarianza tra $X$ ed errore è nulla.

La covarianza si può sempre scrivere come la media del prodotto incrociato meno il prodotto delle medie: $\mathrm{Cov}(X,\varepsilon) = E[X\varepsilon] - E[X]E[\varepsilon]$. Si assume che la media di $\varepsilon$ sia uguale a zero. Se non lo fosse, si può riscrivere il modello in modo che lo sia, riscalando e modificando l'intercetta, senza cambiare nulla. Il secondo termine sparisce allora per definizione.

> [!question] Da verificare: anche qui la trascrizione dice "media di y uguale a zero", ma il contesto riguarda la media dell'errore $\varepsilon$.

Dunque la covarianza tra $X$ ed errore è uguale alla media del prodotto incrociato $E[X\varepsilon]$. Non è ovvio che questo termine sia nullo, ma lo si dimostra con una proprietà della statistica di base: la media di una variabile si può scrivere come la media delle medie condizionali.

> [!question] Da verificare: nella trascrizione l'errore è spesso chiamato "y" ("covarianza tra X ed Y", "media di Y dato X"). Per coerenza con il ragionamento qui e di seguito si riporta $\varepsilon$.

### La legge delle aspettative iterate

Un grafico mostra i salari di 526 lavoratori. I lavoratori sono divisi in sottogruppi disgiunti, e per ciascun sottogruppo la media aritmetica è rappresentata da un quadratino rosso. Per calcolare la media marginale dei salari ci sono due strade. La prima: prendere tutti i pallini blu, considerarne la seconda coordinata (l'altezza) e farne la media aritmetica, cioè $1/526$ per la somma dei salari. La seconda: poiché si conosce il salario medio di ogni sottogruppo, si fa la media dei quadratini rossi, pesata per il numero di osservazioni di ciascun gruppo. Un quadratino con due persone vale due, uno con una persona vale uno, uno con 60 persone vale 60. Si ottiene esattamente lo stesso numero.

La media delle medie condizionali è quindi uguale alla media marginale. È un risultato generale della statistica, valido anche nella popolazione e non solo nel campione: la media marginale si calcola come valore atteso iterato del valore atteso condizionato. Il docente metterà nei lucidi entro la sera la dimostrazione almeno per il caso discreto. Il risultato è importante in statistica e molto usato in econometria, anche in applicazioni più avanzate.

Applicato al prodotto incrociato: si calcola prima la media rispetto a $\varepsilon$ del prodotto $X\varepsilon$ fissato $X$, che corrisponde ai quadratini rossi, cioè alle medie condizionali; poi si fa la media rispetto a tutti i possibili valori di $X$, cioè la media dei quadratini rossi:

$$E[X\varepsilon] = E\big[\,E[X\varepsilon \mid X]\,\big].$$

Una volta fissato $X$, esso è una costante e si può portare fuori dalla media condizionale:

$$E\big[\,E[X\varepsilon \mid X]\,\big] = E\big[\,X \, E[\varepsilon \mid X]\,\big].$$

Se il modello è corretto, cioè se il modello statistico coincide con quello teorico, $E[\varepsilon \mid X] = 0$. Qualunque sia il valore di $X$, l'argomento della media è sempre zero, quindi la media è zero. Il docente aggiunge che si tratta della media rispetto a $X$ di una quantità identicamente nulla, e che gli eventuali passaggi formali con l'integrale rispetto alla densità di $X$ non cambiano il risultato. Il docente segnala inoltre di aver dimenticato un termine alla lavagna e invita gli studenti a segnalare le imprecisioni.

Dunque $E[\varepsilon \mid X] = 0$, che è la definizione corretta di esogeneità, implica $\mathrm{Cov}(X,\varepsilon) = 0$. Il viceversa non vale necessariamente, ma l'implicazione è appena stata dimostrata.

### Esogeneità e covarianza nulla

La condizione sul momento condizionale è un concetto complesso da ricordare dal punto di vista statistico e logico, mentre la covarianza e la correlazione sono più naturali. Nel corso i due concetti si possono considerare sostanzialmente equivalenti. È vero che dalla covarianza nulla non si dimostra il viceversa, ma esistono controesempi solo in casi patologici; in generale i due concetti sono strettamente legati. Chi preferisce può quindi pensare l'esogeneità così: $X$ non deve essere correlato con l'errore. Come si misura la correlazione, in un modo o nell'altro, cambia poco dal punto di vista intuitivo.

Si è dimostrato che un primo criterio per capire se si sta lavorando bene è stabilire se il modello stimato sia ragionevole per descrivere la relazione causa-effetto, cioè il processo che genera i dati. Operativamente è solo un'idea generale, ma ora è formalizzata. Occorre capire se il modello statistico sia una buona approssimazione di qualcosa che purtroppo non è noto. Per stabilire se ci siano problemi nel modello di regressione servono ipotesi sul termine d'errore, perché da come è fatto dipende la qualità della stima di $\beta$. Il docente chiede se ci siano domande.

### Omoschedasticità ed eteroschedasticità

Non interessa solo la media di $\varepsilon$. Porre la media condizionale a zero dice che il modello va bene, ma si possono fare ipotesi anche su altri momenti. Un'altra ipotesi riguarda la varianza di $\varepsilon$ per ogni valore fissato di $X$. È un'ipotesi più semplice di quella sull'esogeneità. Qualunque sia l'ipotesi sulla varianza di $\varepsilon$, le stime dei minimi quadrati restano valide: non è quello il problema. Tuttavia l'ipotesi sulla varianza condizionale ha conseguenze sulla capacità di fare test sui parametri, quindi sull'inferenza.

Le ipotesi principali sono due. L'omoschedasticità vale quando la varianza di $\varepsilon$ dato $X$ è costante, cioè la varianza della componente residuale è sempre la stessa al variare di $X$. Si parla di eteroschedasticità quando la varianza dell'errore varia in qualsiasi modo al variare di $X$.

Parlare della varianza di $\varepsilon$ dato $X$ e della varianza di $Y$ dato $X$ è esattamente la stessa cosa. Nel modello di regressione la varianza di $Y$ per un livello fissato di $X$, qualunque esso sia, è

$$\mathrm{Var}(Y \mid X) = \mathrm{Var}(\alpha + \beta X + \varepsilon \mid X).$$

Nella formula va precisato che la varianza è condizionata a $X$. Fissato $X$, il termine $\alpha + \beta X$ è una costante: se il livello di istruzione è 5, $\alpha$ e $\beta$ sono numeri ignoti ma pur sempre numeri, quindi $\alpha + \beta \cdot 5$ è un valore esatto.

### Varianza condizionale dell'errore e varianza di Y

La varianza di una variabile casuale a cui si somma una costante non dipende dalla costante. Una variabile casuale è una collezione di valori, ciascuno con una probabilità; nel caso di un dado, sei facce con la loro probabilità. La varianza misura la dispersione del fenomeno, cioè indicativamente l'ampiezza dell'intervallo tra il valore più piccolo e il più grande: piccola se le osservazioni stanno in un intervallo ristretto, grande se stanno in uno ampio. Se a ogni faccia del dado si aggiunge 3, il fenomeno si sposta di 3 unità, ma la variabilità tra il valore minimo e quello massimo non cambia: invece della differenza tra 6 e 1 si ha quella tra 9 e 4, sempre 5. Traslare una variabile casuale per una costante lascia invariata la varianza.

Fissato $X$, quindi, la varianza di una costante più una variabile casuale è la varianza della variabile casuale:

$$\mathrm{Var}(Y \mid X) = \mathrm{Var}(\varepsilon \mid X).$$

L'eterogeneità dei salari corrisponde così all'eterogeneità della componente individuale del salario che non dipende dal livello di istruzione. Nella lezione precedente, guardando il grafico dei dati sui salari, si era osservato che la dispersione in ogni sottogruppo non dipende dal livello di istruzione, comune a tutti i membri del sottogruppo, ma da altro, che si era chiamato $\varepsilon$. La variabilità all'interno di ciascun sottogruppo è quindi la variabilità di tutto ciò che non è nel modello, cioè del termine d'errore. La varianza condizionale di $\varepsilon$ è il coefficiente di eterogeneità dei lavoratori in ciascun sottogruppo.

Una nota tecnica del docente: la registrazione della lezione non sarà disponibile, perché il sistema è andato in crash.

### Riconoscere omoschedasticità ed eteroschedasticità dai grafici

Sul grafico dei salari, la varianza condizionale di $\varepsilon$ è più vicina all'omoschedasticità o all'eteroschedasticità? È eteroschedasticità: al variare di $X$ la dispersione delle osservazioni tende ad aumentare, con un gruppo di lavoratori a varianza piccola e un altro, a livelli di istruzione maggiori, a varianza grande. In questo modello l'ipotesi di omoschedasticità non sembra sensata. In ogni caso non si può mai escludere una qualche forma di eteroschedasticità; sarà trattata più avanti in dettaglio. La varianza non deve necessariamente crescere con $X$: può diminuire, o essere grande, piccola, piccola, grande. Basta che non sia costante.

Due grafici illustrano la differenza. Il primo è costruito con dati simulati in ambito omoschedastico: i soggetti si dispongono intorno a una retta di regressione e la dispersione di ogni sottogruppo è più o meno costante. Nelle code ci sono meno osservazioni e la variabilità può essere qualsiasi, ma dove c'è il corpo della distribuzione la variabilità è sempre circa la stessa. Nel secondo, eteroschedastico, la dispersione è grande, poi piccola, poi di nuovo grande, e così via. Per giudicare bisogna guardare le oscillazioni di $Y$ a ogni livello fissato di $X$: nel secondo caso non sono costanti.

Per il termine d'errore si fanno quindi due ipotesi. La prima è che la media condizionale sia zero: serve a definire un modello corretto dal punto di vista logico, legato a una relazione causale, a cui non manca nulla. La seconda riguarda la varianza condizionale, che può essere costante o no. Questa seconda ipotesi è di comodo, si gestisce in modo abbastanza semplice e non è così importante, anche se richiede qualche attenzione.

## Proprietà dello stimatore OLS di beta

Si ritorna al problema principale: uno stimatore è una strategia statistica che crea un legame tra dati e parametro. Ci si chiede se lo stimatore dei minimi quadrati, cioè il rapporto covarianza su varianza, sia una buona strategia per stimare $\beta$. Una buona strategia dovrebbe, indipendentemente dal campione estratto, essere legata al vero valore del parametro, e dovrebbe essere tanto più precisa quanto più dati si hanno. Si vuole quindi capire se covarianza fratto varianza sia legata al vero $\beta$ e che cosa succeda quando il campione cresce.

Il docente avverte che la lezione prosegue con un po' di algebra, la più semplice possibile e senza matematica complicata, e che risulta un po' noiosa.

La lezione precedente ha derivato lo stimatore con il metodo dei momenti anziché con i minimi quadrati, ma i due coincidono. Si assume che i dati siano campionati dalla popolazione in modo indipendente, ipotesi importante. Con $n$ numero di osservazioni e $\bar x$, $\bar y$ medie campionarie, lo stimatore è

$$\hat\beta = \frac{\sum_{i=1}^{n}(x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^{n}(x_i - \bar x)^2}.$$

> [!question] Da verificare: nella trascrizione il denominatore è detto "sommatoria della varianza della x"; si riporta la somma dei quadrati degli scarti di $x_i$ dalla media, coerente con "covarianza su varianza". Si potrebbe anche dividere numeratore e denominatore per $n$, senza differenza.

La formula da sola non lega il vero $\beta$ al $\beta$ stimato, che è l'approssimazione statistica. Per costruire il legame si applica la formula al vero modello, sostituendo a $y_i$ la sua rappresentazione $\alpha + \beta x_i + \varepsilon_i$. Prima, però, conviene semplificare il numeratore, perché gli econometrici sono pigri e semplificano quando possono. Si sviluppa il prodotto come prodotto di $(x_i - \bar x)$ per $y_i$ meno il prodotto di $(x_i - \bar x)$ per $\bar y$.

### Semplificazione del numeratore

Il docente avverte che, volendo semplificare, ha in realtà reso l'espressione più lunga, ma che il vantaggio si vede subito. Il numeratore diventa

$$\sum_i (x_i - \bar x)\,y_i \;-\; \sum_i (x_i - \bar x)\,\bar y.$$

Il secondo termine è nullo: $\bar y$ è una costante, quindi si porta fuori dalla sommatoria, e la somma degli scarti di una variabile dalla propria media è zero. Uno studente chiede perché il secondo termine sia zero. Il docente risponde che la proprietà fondamentale della media aritmetica è proprio questa: gli scostamenti delle osservazioni dalla media sommano a zero. Il termine riguarda solo il numeratore e deve essere esattamente zero. Resta

$$\hat\beta = \frac{\sum_i (x_i - \bar x)\,y_i}{\sum_i (x_i - \bar x)^2}.$$

### Legame tra lo stimatore e il vero beta

Si sostituisce $y_i = \alpha + \beta x_i + \varepsilon_i$ nella formula. Il numeratore si scompone in tre somme:

$$\sum_i (x_i - \bar x)\,\alpha \;+\; \sum_i (x_i - \bar x)\,\beta x_i \;+\; \sum_i (x_i - \bar x)\,\varepsilon_i,$$

il tutto diviso per $\sum_i (x_i - \bar x)^2$.

La prima somma è nulla: $\alpha$ è una costante che si porta fuori, e resta la somma degli scarti dalla media, uguale a zero. È lo stesso ragionamento di prima, con il parametro costante al posto della media di $y$.

Nella seconda somma $\beta$ è una costante e si porta fuori. Si sa che la somma degli scarti $(x_i - \bar x)$ moltiplicata per una costante è zero, quindi si può sottrarre zero, nella forma $\beta \sum_i (x_i - \bar x)\bar x$, senza cambiare il valore. Il numeratore di questo termine diventa $\beta \sum_i (x_i - \bar x)(x_i - \bar x) = \beta \sum_i (x_i - \bar x)^2$. Diviso per il denominatore, che è la stessa quantità, dà $\beta$.

Per concludere si raccolgono i primi due addendi, che hanno la stessa struttura, e si nota che numeratore e denominatore del termine in $\beta$ coincidono, dato che $(x_i - \bar x)$ moltiplicato per sé stesso è il quadrato dello scarto, quindi si semplificano. Il terzo termine resta. Si ottiene

$$\hat\beta = \beta + \frac{\sum_i (x_i - \bar x)\,\varepsilon_i}{\sum_i (x_i - \bar x)^2}.$$

Quindi, rispetto al vero modello, in cui la media condizionale di $Y$ dato $X$ è $\alpha + \beta X$, lo stimatore è uguale al vero parametro più una componente di rumore che dipende dall'eterogeneità degli individui.

### Valore atteso dello stimatore

Ci si chiede quali siano le proprietà dello stimatore rispetto al vero $\beta$: se la sua media sia legata a $\beta$ e quale sia la sua varianza. Lo stimatore è una variabile casuale perché dipende dai dati: cambiando il campione cambia la stima. È la collezione delle stime ottenibili da campioni diversi, ciascuna con la probabilità di estrarre quel campione, e quindi se ne possono calcolare valore atteso e varianza.

Si calcola il valore atteso condizionale ai valori di $x$ del campione. Equivale a considerare campioni omogenei tra loro, che condividono gli stessi $x$ ma non le stesse persone, perché ciò che cambia sono gli $\varepsilon$. Per capire il senso di campioni omogenei tra loro, il docente porta l'esempio dei colleghi che hanno fatto il dottorato con lui: persone con le stesse caratteristiche osservabili, ma che hanno fatto scelte diverse e hanno salari diversi. Sono uguali nelle $x$ e diversi in $\varepsilon$.

Fissati tutti gli $x$ del campione, $\beta$ è una costante e il termine di rumore è una variabile casuale, perché $\varepsilon$ non è fissato. La media di una costante più una variabile casuale è la costante più la media della variabile casuale. Il denominatore dipende solo da $x$, quindi è una costante e si porta fuori dalla media, dato che la media di una costante per una variabile casuale è la costante per la media. Inoltre la media di una somma è la somma delle medie, come quando si calcola il reddito medio familiare di una famiglia con due lavoratori sommando le medie dei due. L'operatore di media si porta quindi dentro la sommatoria. Infine, fissati gli $x$, anche $(x_i - \bar x)$ è una costante e si porta fuori:

$$E[\hat\beta \mid x] = \beta + \frac{1}{\sum_i (x_i - \bar x)^2}\sum_i (x_i - \bar x)\,E[\varepsilon_i \mid x].$$

Se il modello è corretto, $E[\varepsilon_i \mid x]$ è zero, quindi la somma è zero e

$$E[\hat\beta \mid x] = \beta.$$

In media lo stimatore è uguale a $\beta$.

### Non distorsione e varianza dello stimatore

Se si prendono campioni con caratteristiche simili e si calcola $\hat\beta$ moltissime volte, la media di tutte queste stime deve essere il vero $\beta$, che per fortuna non è noto: se lo fosse, la statistica non servirebbe. Con un primo campione si ottiene $\hat\beta_1$, con un secondo $\hat\beta_2$, e così via. La teoria dice che la media di tutte queste stime è esattamente il vero valore. Si dice allora che lo stimatore è non distorto: non devia sistematicamente dal vero valore del parametro.

Finora si è guardata solo la media, non la distribuzione. La distribuzione si può calcolare in due modi: in modo esatto, oppure in modo asintotico, cioè approssimato, per campioni abbastanza grandi. Per calcolarla servono ipotesi più forti sul termine d'errore, sulla sua distribuzione di probabilità. Il docente non la affronta, perché non serve realmente, e dichiara di essere contrario alla distribuzione per campioni infiniti.

Il problema è che si ha un solo campione e non si sa se dia una stima vicina o lontana dalla media. La distanza dal vero valore dipende solo da $\varepsilon$, cioè dall'eterogeneità delle osservazioni in quel dataset specifico. Non dipende dal fatto che il modello sia sbagliato o che si usino formule sbagliate. Non si può valutare a monte, perché il vero valore non è noto. Serve quindi la distanza media tra lo stimatore, inteso come tutti i valori che può assumere su campioni diversi, e il vero parametro. La misura di distanza media in statistica è la varianza.

### Varianza dello stimatore sotto omoschedasticità

Si calcola

$$\mathrm{Var}(\hat\beta \mid x) = \mathrm{Var}\!\left(\beta + \frac{\sum_i (x_i - \bar x)\varepsilon_i}{\sum_i (x_i - \bar x)^2} \,\Big|\, x\right).$$

Come visto, $\beta$ è una costante e la varianza è insensibile alla traslazione, quindi conta solo il secondo termine. Per semplificare i calcoli si assume omoschedasticità, rimandando il caso generale a dopo. Il docente salta alcuni passaggi, solo noiosi. Fissato $x$, il denominatore è una costante, che uscendo dalla varianza va elevata al quadrato. Le osservazioni sono indipendenti, quindi la varianza della somma è la somma delle varianze. Anche $(x_i - \bar x)$ è costante e, portato fuori, va al quadrato:

$$\mathrm{Var}(\hat\beta \mid x) = \frac{\sum_i (x_i - \bar x)^2\,\mathrm{Var}(\varepsilon_i \mid x)}{\left(\sum_i (x_i - \bar x)^2\right)^2}.$$

Se la varianza condizionale di $\varepsilon$ è costante, la si chiama $\sigma^2$: non dipende da $x$ e si porta fuori dalla sommatoria. Il numeratore si semplifica con uno dei due fattori del quadrato al denominatore:

$$\mathrm{Var}(\hat\beta \mid x) = \frac{\sigma^2}{\sum_i (x_i - \bar x)^2}.$$

Dividendo numeratore e denominatore per $n$ si ottiene una formula più intuitiva: il denominatore diventa la varianza campionaria di $X$, che per $n$ abbastanza grande converge alla varianza di $X$ nella popolazione, mentre il numeratore è $\sigma^2/n$. Il denominatore converge quindi a una costante, mentre il numeratore tende a zero al crescere di $n$. All'aumentare delle osservazioni l'incertezza dello stimatore tende a zero.

Ne segue che lo stimatore è consistente: con molti dati, la stima ottenuta da qualsiasi campione non si discosta dalla media. Il numero nella tabella di output, in un modello corretto e con abbastanza dati, collassa sul vero valore del parametro.

### Illustrazione con campioni simulati

Il grafico mostra stime di $\beta$ ottenute da campioni di numerosità diversa. Con campioni di dimensione 2, simulando col computer circa 10.000 campioni dalla stessa popolazione, si costruisce l'istogramma delle stime (blu). Con campioni di dimensione 10, sempre 10.000, la distribuzione è più concentrata: stime lontane, che con dimensione 2 compaiono, con dimensione 10 non capitano mai. Con dimensione 100 la distribuzione è molto più schiacciata attorno al vero parametro, il valore della popolazione.

> [!question] Da verificare: la trascrizione riporta "campioni di dimensione n2" e "circa 10.000" ("mi sembra"); le dimensioni 2, 10 e 100 sono ricostruite dal contesto.

Se $n$ tende all'infinito, si osservano tutte le persone della popolazione, tutti i campioni coincidono e lo stimatore dà sempre lo stesso numero: una variabile con media $\beta$ e varianza zero. Osservando l'intera popolazione si trova il vero $\beta$. È un risultato teorico asintotico, ma l'intuizione è che più $n$ è grande, più la varianza è piccola e più i valori ottenibili dalla procedura di stima sono concentrati intorno alla media, che si è dimostrato essere il vero valore. Con 100 osservazioni una stima molto distante dal vero $\beta$ non capita praticamente mai.

### Risultati fondamentali

Sotto l'ipotesi di esogeneità lo stimatore è non distorto. Sotto indipendenza delle osservazioni e varianza costante, cioè omoschedasticità, tende a essere consistente. Il secondo risultato si può dimostrare anche con dati dipendenti ed eteroschedasticità, ma la formula presentata è più semplice, a parte la noia della dimostrazione.

> [!question] Da verificare: il docente afferma che la consistenza vale anche con dati dipendenti; la dipendenza delle osservazioni richiede in generale condizioni aggiuntive, non discusse nella lezione.

> [!tip] Esame
> Per il modello di regressione semplice, l'esogeneità è l'ipotesi cruciale: senza di essa non funziona niente. Le altre, come l'indipendenza delle osservazioni e l'omoschedasticità, sono tipicamente ipotesi di comodo e discutibili; saranno riprese più avanti.

Il docente chiede se ci siano domande, poi rimanda alla settimana successiva, quando proseguirà la teoria aggiungendo altri ingredienti.
