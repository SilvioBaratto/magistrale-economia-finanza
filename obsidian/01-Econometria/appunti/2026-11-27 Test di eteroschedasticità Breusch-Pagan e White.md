---
corso: Econometria
data: 2026-11-27
fonte: Audio/econometria/econometria_2026-11-27.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe ripulita, fedele al parlato
integrato: 2026-11-28
---

# Test di eteroschedasticità: Breusch-Pagan e White

## Gli esercizi di oggi

Quindi velocemente, ma volevo fare un po' di esercizi che di fatto sono vecchi esami che avevo messo a disposizione. In particolare sono gli esami che stanno nella parte, qui, uno e due, guardiamo insieme.

> [!tip] Esame
> Non ci sono le soluzioni online, così più o meno dovreste capire che tipo di risposta mi aspetto alle domande.

## Ripasso degli standard error robusti

Allora, quello che abbiamo fatto ieri è, in pratica, cercare di capire come costruire questo standard error per i coefficienti che siano insensibili all'ipotesi che faccio sulla varianza condizionata. Questo dal punto di vista operativo semplifica molto la vita, perché di fatto io posso non pensare più al problema dell'eteroschedasticità o dell'omoschedasticità, perché il modo robusto con cui io calcolo la seconda colonna dell'output, il modello di regressione, va comunque sempre bene, indipendentemente dall'ipotesi che posso fare sui dati. Quindi dal punto di vista operativo è sempre conveniente utilizzare questa formula, questo modello di regressione semplice, quindi la formula è facile da scrivere. Nel modello di regressione multipla c'è la formula dei lucidi, ma è semplicemente un po' più complicata, è la stessa roba. È sempre conveniente utilizzare questa formula anziché quella che in pratica mi elimina questa componente, mi elimina il quadrato.

Per dimostrare che questa formula funziona, l'abbiamo visto ieri, mi basta avere dei coefficienti alfa e beta del modello di regressione che siano stimati in maniera consistente, cioè il mio stimatore deve convergere al vero valore del parametro, l'unica ipotesi che ho. In pratica sto dicendo che basta che valga l'esogenità. Questa roba, per n sufficientemente grande, funziona e quindi sono a posto.

Quindi una volta che ho uno stimatore di questo tipo, e in realtà il software li calcola in maniera automatizzata, non so se l'avete già visto nelle esercitazioni o lo vedrete la prossima volta, quando voi andrete a stimare con Gretl o con qualsiasi altro software un modello, dovete semplicemente aggiungere l'opzione usa standard error robusti. ==Il mio consiglio: usateli sempre.== In Gretl, quando avete la finestra del modello di regressione, sotto c'è un quadratino con scritto standard error robusti, spuntate e automaticamente viene fatta questa formula anziché l'altra. Quindi risolto il problema.

Una volta che abbiamo risolto il problema, vuol dire che, ovviamente questa roba funziona solo se avete abbastanza dati, per n sufficientemente grande potete calcolare i test, l'inferenza quindi, in maniera molto standard. Se voleste calcolare una statistica t, semplicemente avrete un numeratore che è il solito numeratore della statistica t e un denominatore che è lo standard error robusto calcolato con la formula che vi ho appena fatto vedere. Quindi anziché prendere lo standard error incerto, prende lo standard error robusto.

> [!question] Da verificare: la trascrizione riporta "standard error incerto"; probabilmente "naïve" (così la slide 10 chiama gli standard error non robusti), ma la slide non conferma la parola detta.

Quindi il test F funziona uguale. Una volta che ho utilizzato standard error robusti, il calcolo del test F è leggermente diverso, però una volta che dico al computer stimami il modello con standard error robusti, automaticamente verrà costruita una versione del test F che è coerente con questi standard error nuovi. Lo fa in automatico il computer, quindi non è un problema che avrete in cavo.

> [!question] Da verificare: la trascrizione riporta "in cavo"; probabilmente "in capo".

Quindi una volta che voi decidete di stimare un modello con standard error robusti, automaticamente tutta l'inferenza che rende diversa l'ipotesi di omoschedasticità rispetto all'eteroschedasticità dal punto di vista pratico viene gestita da qualsiasi software di benchmarking. Quindi se stimate il modello con standard error robusti, andate a calcolare la statistica t, verrà calcolata in maniera robusta e la statistica F verrà calcolata in maniera robusta. Quindi non ci sono più problemi, eteroschedasticità e omoschedasticità non sono più un problema. E questo è per concludere quello che vi volevo dire.

> [!question] Da verificare: la trascrizione riporta "software di benchmarking"; il termine non è chiaro (forse software di statistica o di econometria).

## A che cosa servono i test di eteroschedasticità

Esistono però in letteratura dei test che servono in qualche modo a validare l'ipotesi di eteroschedasticità. Da un punto di vista operativo non è particolarmente utile fare un test per sapere se è più probabile l'omoschedasticità o l'eteroschedasticità, anche perché, vedremo fra un attimo, l'omoschedasticità non è dimostrabile sulla base di test standard. Però potrebbe essere utile fare i test di eteroschedasticità perché potrebbero raccontarci qualcosa su come sono fatti i dati. Ci potrebbero spiegare perché la varianza cambia con x e questo potrebbe aiutarci a specificare un modello di regressione in maniera migliore, sia in termini di capacità del modello di fare previsioni, sia magari per spiegare dei fattori, delle caratteristiche che sono nei dati e che potrebbero essere interessanti dal punto di vista economico.

## Un esempio: prezzi delle case e dimensione

L'esempietto che volevo proporvi è un qualcosa del genere. Supponiamo di essere interessati a vedere se i prezzi delle case dipendono dalla dimensione della casa stessa. Per esempio, sul diagramma di regressione: posso stimarlo, posso vedere come i residui, come la capacità previsiva del modello, cambia a seconda che prendo case piccole o case grandi. Tipicamente con una regressione di questo tipo, quello che mi aspetto è che l'errore di previsione, il residuo associato alle case piccole, è tendenzialmente piccolo. Il residuo associato alle case grandi è tendenzialmente grande. Cosa vuol dire? Le case piccole più o meno hanno tutte lo stesso prezzo. Le case grandi possono variare per un sacco di altre caratteristiche in più. Tipicamente le case piccole sono considerate anche meno prestigiose, quindi magari hanno finiture diverse, hanno meno stanze, queste cose qua. Quindi i prezzi sono più o meno tutti uguali, perché sotto una certa soglia magari non si scende. Le case grandi possono anche essere state costruite volutamente in zone più pregiate. Siccome sono grandi, magari si è messa la finestra migliore, ci potrebbero essere caratteristiche di questo tipo.

> [!question] Da verificare: la trascrizione riporta "la finestra migliore"; il termine non è chiaro (forse finitura o vista).

Quindi dal momento che mi aspetto un beta positivo, mi chiedo se le caratteristiche omesse da questa regressione magari non creano problemi di endogeneità, perché magari quelle caratteristiche non sono legate alla dimensione, per esempio, è contrario a quello che ho fatto. Però magari potrebbero in qualche modo spiegarmi la dispersione dei dati.

> [!question] Da verificare: la trascrizione riporta "è contrario a quello che ho fatto"; il senso non è chiaro.

È un po' come l'esempio che avevo fatto, il primo esempio del modello di regressione semplice, in cui il reddito, il livello di istruzione, sul salario. Lavoratori con un livello basso di education più o meno guadagnano tutti uguali dai dati che avevamo visto. Lavoratori con un alto livello di istruzione tendono ad essere molto dispersi in termini di salario. Questa dispersione può essere spiegata e di fatto è eteroschedasticità, se la chiamo con un nome statistico. Magari il modello potrebbe beneficiare dall'aggiunta di alcune caratteristiche che mi spieghino anche quella dispersione, che potrebbe essere un sintomo di variabili mancanti all'interno del modello. Questa è un po' l'idea.

Quindi quello che vorrei poter fare è vedere se la variabilità dell'errore dipende dal regressore stesso. Se c'è questo effetto, vuol dire che, per qualche ragione, altre caratteristiche in qualche modo non osservate dentro il modello potrebbero essere importanti per spiegare il mio problema economico, per dirla in maniera molto generale, molto astratta, se volete. Quindi potrebbe essere interessante capire perché la varianza dipende dalla x, perché potrebbe darmi informazioni in più. Non è detto che siano interessanti, detto che comunque il problema statistico di calcolare gli standard error l'ho risolto a prescindere, una volta che il mio modello è ben specificato.

> [!question] Da verificare: la trascrizione riporta "detto che comunque"; probabilmente "dato che comunque".

Quindi quello che potrei fare per capire se effettivamente la variabilità dei miei dati dipende dal regressore è prendere un'approssimazione, come abbiamo fatto ieri, della varianza condizionale con il sigma quadro U. Abbiamo visto che per certi versi lo posso approssimare come un residuo al quadrato, e costruisco una regressione ausiliaria in cui questa roba qua mi rappresenta la varianza condizionale, e vedo se dipende da x.

Se questo coefficiente b è positivo vuol dire che l'aumentare della dimensione della casa aumenta anche l'eterogeneità delle case che sto considerando. Se invece b è uguale a zero, vuol dire che la varianza condizionale approssimata, che posso misurare, non dipende dalla dimensione e quindi probabilmente, diciamo che non c'è eterogeneità aggiuntiva che devo spiegare, sono in un contesto più semplice. Quindi potrei decidere di fare una regressione di questo tipo, giusto per capire perché la varianza cambia, perché capire come funziona la varianza può darmi idee su come migliorare il mio modello iniziale, tutto qua. Quindi i test di eteroschedasticità non vengono fatti per capire se siamo in un contesto omoschedastico o eteroschedastico, perché tanto il problema dell'omoschedasticità versus eteroschedasticità l'abbiamo risolto con gli standard error robusti. Questi test mi servono per in qualche modo capire se c'è un effetto, quali sono le variabili che potrebbero effettivamente avere un impatto sulla varianza condizionale.

Vi propongo un paio di test, velocemente, giusto per farvi vedere la filosofia e come si possono interpretare. Quindi questa roba qua mi serve per capire se sono in un contesto o nell'altro, perché tanto indipendentemente dal contesto l'abbiamo risolto il problema della varianza condizionale, per fare inferenza. Questi test che vi propongo servono proprio per vedere se si può specificare in maniera migliore il modello, perché può essere di interesse economico più che statistico.

> [!question] Da verificare: la trascrizione riporta "questa roba qua mi serve per capire se sono in un contesto o nell'altro"; dal seguito ("tanto indipendentemente dal contesto l'abbiamo risolto il problema") sembra mancare un "non", ma l'audio trascritto non lo dice.

## Il test di Breusch-Pagan

Allora, supponiamo di avere un modello, primo test, test di Breusch-Pagan. Supponiamo di avere un modello di regressione a disposizione, una regressione multipla, e sulla base di quello che vi ho detto prima sui prezzi delle case e la dimensione vorrei capire se la varianza condizionale, quindi questo è il modello, dipende dalle x, dove le x sono potenzialmente tutti i fattori che ho incluso nel modello stesso.

### Una regressione sulla varianza condizionale

Ora, la varianza condizionale non è altro che questo oggetto e se ci pensate questo potenzialmente è un modello di regressione, perché cosa fa un modello di regressione? Mi modella la media condizionale di una variabile fissata la X. Di solito qua ci mettiamo la Y come primo argomento delle variabili attese. Però, in linea di principio, questo è un modello di regressione, una media condizionale, una combinazione lineare di variabili e quindi vorrei stimare questo modello, esattamente come vorrei farlo con l'esempio di prima della dimensione della casa e il prezzo della casa, e la varianza dei prezzi delle case.

*(slide 29)*

Qual è il problema di questo modello? Che dal punto di vista teorico è un modello di regressione ben specificato, ma dal punto di vista pratico è un po' complicato da stimare. Qualcuno ha un'idea del perché? Cioè, alla fine questa definizione di regressione mi porta a questo modello empirico. Perché questo modello non è stimabile? Uno studente risponde: "Non siamo certi se le variabili X sono condizionate...". Può essere, però il problema è più pratico, molto più semplice. Il problema che starò io non osservo e in una regressione la variabile dipendente io la devo osservare assieme ai regressori. Poi ci può anche essere, in aggiunta, un problema di come si rapportano tra loro i coefficienti. Quindi dal punto di vista operativo questa regressione non è calcolabile, perché manca la Y, manca quello a sinistra dell'uguale, cioè su Gretl o qualsiasi software io non ho dei numeri qua, ho solo un concetto astratto legato alla varianza condizionale.

> [!question] Da verificare: la trascrizione riporta "Non siamo certi se le variabili X sono condizionate..." subito dopo la domanda del docente; sembra la risposta di uno studente, ma la frase è interrotta e l'attribuzione è dedotta.

> [!question] Da verificare: la trascrizione riporta "Il problema che starò io non osservo"; la parola "starò" non è chiara (il docente intende forse la varianza condizionale, che non è osservata).

### Che cosa dice l'ipotesi nulla

Però dal punto di vista concettuale quello che potrei dire è che, ipotizzando che la varianza condizionale sia in qualche modo rappresentabile da questa funzione, che è molto specifica, un test per l'omoschedasticità contro l'eteroschedasticità potrebbe essere costruito in questo modo. Se tutti quei coefficienti che ho qua, da $\delta_1$ a $\delta_k$, da $\delta_0$ no, perché mi serve, sono tutti nulli, vuol dire che la varianza condizionale qua non dipende dalla x, perché se tutti i coefficienti sono nulli, pensate alla ... di esclusione, tutta sta roba sparisce, la varianza condizionale sarebbe una costante che coincide con questo parametrino. Se almeno uno dei coefficienti è diverso da zero, vuol dire che la varianza condizionale dipende da almeno una x, vuol dire che c'è eteroschedasticità e dipende proprio da quel fattore specifico.

> [!question] Da verificare: la trascrizione riporta "pensate alla ... di esclusione"; manca una parola, probabilmente "restrizione".

Ora, questa è un'ipotesi molto restrittiva su come può essere la varianza condizionale. In linea di principio io non so come è fatta la varianza condizionale. So solo che cambia con x se c'è eteroschedasticità, so che è costante se non c'è eteroschedasticità, ma non so qual è la funzione che mi dice come cambia l'eteroschedasticità. Dipende dalla dimensione della casa, dipende da quante finestre ci sono, dipende dall'area in cui è costruita la casa. Io non lo so qual è il modello che influenza la variabilità dei prezzi. Ed è molto difficile, perché già è complicato costruire un modello per la media condizionale che è osservata, i prezzi sono osservati, figurarsi costruire un modello su qualcosa che non è neanche osservabile direttamente, ma lo posso solo approssimare. Però posso fare un'ipotesi. La varianza è fatta così. È più probabile l'omoschedasticità rispetto all'eteroschedasticità però fatta così, se e solo se tutti i coefficienti da $\delta_1$ a $\delta_k$ sono identicamente nulli.

Quindi come posso validare l'ipotesi di omoschedasticità contro eteroschedasticità in questo contesto? Posso fare un test tipo F in cui pongo a zero tutti i coefficienti da 1 a k. Se tutti i coefficienti sono uguali a zero, allora vuol dire che il modello ridotto è questo qua, cioè almeno uno diverso da zero vuol dire che c'è eteroschedasticità.

*(slide 30)*

### Non rifiutare l'ipotesi nulla

Domanda, secondo voi, se io non rifiuto l'ipotesi nulla, cioè non rifiuto l'ipotesi che $\delta_1$ e $\delta_k$ sono tutti uguali a zero, quindi non rifiuto l'ipotesi, vuol dire che sono nell'ambito dell'omoschedasticità secondo voi? Chi vota per il sì e chi vota per il no?

In realtà quello è il problema, che un test fatto così non è un test del tipo omoschedasticità contro eteroschedasticità, è un test del tipo eteroschedasticità più un tipo specifico, che non so se è corretto, contro non quel tipo di eteroschedasticità. La nulla non è omoschedasticità, mi dice semplicemente che è più probabile l'omoschedasticità contro un'alternativa che è fatta così, ma io non so se l'eteroschedasticità è fatta così, è solo un'ipotesi che sto facendo da statistico. Quindi ==non rifiutare nulla, non vuol dire omoschedasticità==, anche se software quando fate questi test vi dicono H0 omoschedasticità, H1 eteroschedasticità. In realtà H0 è: non c'è questa forma di eteroschedasticità, l'ipotesi di principio potrebbe essere ci sia qualche altro modello che mi descrive la varianza condizionale. Però, vabbè, questo è un test abbastanza popolare, può essere fatto. E mi può essere utile più che altro per capire non tanto se c'è omoschedasticità o eteroschedasticità, ma per capire se questi coefficienti sono positivi o negativi, come varia la varianza condizionale al variare di x. Perché, come vi ho detto prima, può aiutare a costruire un modello statistico migliore. Mi può aiutare a ridurre il problema delle variabili mancanti.

### Come stimare la regressione sulla varianza

Ora rimane il problema: come faccio a stimare questa regressione dove la variabile dipendente non ce l'ho? Ieri però abbiamo visto che, su un campione sufficientemente grande, l'errore al quadrato può essere approssimato dal residuo al quadrato, che approssima anche $\sigma_i^2$, che è la varianza condizionale al quadrato. Quindi la regressione calcolabile può essere un qualcosa in cui, anziché considerare questa sequenza di variabili casuali, metto i residui al quadrato, tanto sono tutti più o meno la stessa quantità asintoticamente. Quindi quello che potrei fare è stimare questa regressione dove anziché mettere $\epsilon^2$ metto il residuo alla seconda, quello con il cappellino.

E a quel punto ho una regressione qualsiasi, faccio un test tipo F, non è che lo faccio proprio F, però faccio praticamente quella roba là. Quindi calcolo la statistica, vedo se è più probabile H0 o H1 e prendo una decisione, sapendo che se rifiuto la nulla vuol dire che almeno quella forma di eteroschedasticità ce l'ho, perché vuol dire che la varianza dipende da quei regressori e quindi dipende da X. Se non rifiuto la nulla, non posso dire che c'è omoschedasticità, posso solo dire che non c'è l'eteroschedasticità del tipo di Breusch-Pagan, ma potrebbe esserci un'altra forma di eteroschedasticità che il modello non comprende.

Adesso vi faccio un secondo test per farvi capire meglio cosa voglio dire. Ricordandovi però che ==a me non interessa sapere se c'è omoschedasticità, perché non lo saprò mai==. Mi interessa sapere perché c'è eteroschedasticità e quindi capire come sono fatti i coefficienti di questi modelli.

### Il test di Breusch-Pagan in Gretl

Dal punto di vista operativo, lo vedremo anche magari con un esempio un po' più pratico. Se voi andate nell'output standard di Gretl e calcolate la regressione, andate nel menu test, andate nel sottomenu test di eteroschedasticità, scegliete Breusch-Pagan e automaticamente vi verrà fuori il valore della statistica test. Quindi dovrebbe essere nel menu test, andate nella sottosezione LM test eteroschedasticità. LM test è solo il modo con cui il test viene calcolato operativamente dal software. LM sta per moltiplicatore di Lagrange, che è la tecnica statistica che viene utilizzata per calcolarlo. Dopodiché andate nell'opzione eteroschedasticità. Scegliete Breusch-Pagan, e automaticamente vi viene fuori l'output del test. C'è anche qualcosa di più, credo che il software vi fa anche vedere i parametri, le stime dei parametri, giusto perché vi ho appena detto che è quella forse la parte più interessante.

> [!question] Da verificare: la trascrizione riporta "Scegliete Browse, paga"; la slide 32 riporta "Breush-Pagan" nel menu di Gretl e si adotta "Breusch-Pagan".

Dopodiché qua, in questo esempio che vi faccio, la statistica test è 30, è tipo una statistica F, vi calcola il p-value del test che è circa zero, quindi automaticamente in questo esempio specifico rifiutate l'ipotesi nulla. Quello che potete dire è che escludo l'omoschedasticità. A questo punto, se aveste avuto il dubbio di non usare standard error robusti, qua avete almeno un controesempio che vi diagnostica eteroschedasticità. Se c'è questa forma di eteroschedasticità vuol dire che almeno un controesempio l'avete trovato, quindi l'omoschedasticità è impossibile, più o meno. Quindi qua il test mi dice: schiacciate il bottone, fammi il test di Breusch-Pagan, non dovete fare niente, il residuo al quadrato se li calcola automaticamente il software, si fa la regressione, ve la fa vedere e poi vi fa una piccola sintesi del risultato. Il p-value vi dice che è zero, è un test tipo F, quindi è unilaterale a destra, vuol dire che siete nella zona di rifiuto. Rifiutate l'ipotesi di omoschedasticità. E questo è un po' il primo test. È abbastanza semplice, una volta che avete capito che l'errore al quadrato è approssimabile con il residuo al quadrato, dopodiché è una regressione normale.

*(slide 32)*

> [!question] Da verificare: la trascrizione riporta "un'illaterale a destra"; probabilmente "unilaterale a destra" (la slide 32 riporta P(Chi-quadro(3) > 30,0227), una coda destra). Inoltre il docente dice "è tipo una statistica F" e "è un test tipo F", mentre la slide 32 riporta una statistica LM con p-value calcolato da una Chi-quadro(3); si riporta ciò che ha detto il docente.

## Il test di White

Il problema è che questo modello forse è troppo semplice, perché? Perché sto dicendo che la varianza dipende dalla x. La varianza potrebbe dipendere da qualcos'altro, qualcosa di più. Per esempio, la varianza potrebbe dipendere dal quadrato delle x. La varianza a un momento secondo, e magari può dipendere dalla varianza della y, potrebbe dipendere dalla varianza della x. E quindi potrebbe essere sensato aggiungere a questa regressione le variabili al quadrato. Come dire, più la x è variabile, più la y è variabile. Ma potrebbe anche aver senso considerare i prodotti incrociati, il prodotto tra x e y.

> [!question] Da verificare: la trascrizione riporta "La varianza a un momento secondo"; probabilmente "la varianza è un momento secondo" (più avanti il docente dice "con le varianze che sono momenti secondi").

> [!question] Da verificare: la trascrizione riporta "il prodotto tra x e y"; dal seguito (il prodotto tra $x_1$ e $x_2$) probabilmente il docente intende il prodotto tra due regressori, ma non è certo.

### L'intuizione sulla varianza di una combinazione lineare

E questo perché? Perché supponiamo di avere, giusto per darvi un'intuizione, poi formalmente si può essere più precisi, supponiamo di voler calcolare la varianza. Più o meno ho che $y = \alpha + \beta_1 x_1 + \beta_2 x_2 + \epsilon$. Se devo calcolare la varianza di y in funzione di x, la varianza di y dato x, supponiamo che la y non sia così importante, beh questa roba è la varianza di $\alpha + \beta_1 x_1 + \beta_2 x_2$ più qualcos'altro, supponiamo che sia irrilevante. A questo punto, se calcolo questa roba, devo calcolare $\beta_1^2$, la varianza di $x_1$, più $\beta_2^2$, la varianza di $x_2$, più $\beta_1$ per $\beta_2$ due volte la covarianza tra $x_1$ e $x_2$.

> [!question] Da verificare: la trascrizione riporta "supponiamo che la y non sia così importante"; dal seguito ("più qualcos'altro, supponiamo che sia irrilevante") il docente si riferisce probabilmente al termine d'errore, ma non è certo.

Quindi, che cos'è la varianza di $x_1$? È in qualche modo qualcosa che fa riferimento ai quadrati di $x_1$. Cos'è la varianza di $x_2$? È qualcosa che fa riferimento ai quadrati di $x_2$. Che cos'è la covarianza? È qualcosa che fa riferimento a $x_1$ e $x_2$, al prodotto incrociato tra di loro. Quindi se ho in mente una varianza di una combinazione lineare di roba, potrebbe aver senso mettere le variabili al quadrato nella regressione ausiliaria, ma anche il prodotto incrociato.

### La regressione ausiliaria di White

A questo punto cosa ha pensato White? White ha pensato che anziché prendere la regressione di Breusch-Pagan, ci aggiunge tutte le variabili al quadrato più tutti i prodotti incrociati possibili tra le variabili. Quindi diventa un modello molto più complicato del precedente. E questa roba qua in teoria dovrebbe essere sufficiente per descrivere praticamente tutti i tipi di eteroschedasticità che mi vengono in mente. Quindi è un modello molto più generale e dovrebbe andar bene per descrivere tutte le forme di eteroschedasticità in un modello lineare.

*(slide 33)*

Quindi l'idea è: regredisco la mia proxy della varianza condizionale rispetto a tutto sto bidone di roba e il test sarà sempre lo stesso. Se tutti questi coefficienti sono congiuntamente nulli, allora vuol dire che è più probabile l'omoschedasticità, ma se almeno uno di questi coefficienti è diverso da zero, vuol dire che la varianza condizionale dipende almeno da una x e quindi c'è eteroschedasticità. Il test sembra perfetto perché in pratica è comprensivo di tutte le forme di eteroschedasticità possibili. I momenti di ordine superiore, tipo x alla terza e x alla quarta, non dovrebbero servire perché sto lavorando con le variabili al massimo, con le varianze che sono momenti secondi.

### Il problema dei troppi regressori

Qual è il problema? Che questa regressione la calcolo quando nel modello originale ho tre regressori, ma se comincio ad avere un modello con dieci regressori, il numero di regressori da mettere in questa regressione ausiliare è enorme, perché devo fare non solo dieci più dieci, ma c'ho anche tutti i prodotti incrociati. Quindi si fa presto ad arrivare a una regressione con quaranta, cinquanta possibili regressori. Qual è il problema quando costruisco un sacco di regressioni, la maggior parte dei quali non spiega nulla, è zero, è che in realtà il test diventa estremamente impreciso. Non tanto per quanto riguarda l'errore del primo tipo. Ricordate che il test che devo fare è tipo un test F. L'errore del primo tipo è sempre l'alfa percento, quindi la probabilità di decidere che è vera l'alternativa quando in realtà vera è nulla. Ma in realtà questo tipo di regressioni enormi mi crea grossi problemi per quanto riguarda la potenza del test, che mi indica qual è la probabilità di non rifiutare. L'errore del primo tipo è non rifiuto la nulla quando la nulla è vera. L'errore del secondo tipo è non rifiuto l'alternativa quando l'alternativa è vera. Non rifiuto la nulla quando l'alternativa è vera, scusate, sono sempre un po' confuso.

> [!question] Da verificare: la trascrizione riporta "costruisco un sacco di regressioni, la maggior parte dei quali non spiega nulla"; dal contesto probabilmente "regressori".

Quindi ho un altro errore che di solito spero sia piccolo. Ecco, in questi modelli quell'errore tipicamente è molto grande. Quindi non sbaglio dalla una parte, cioè l'errore del primo tipo, ma sbaglio dall'altra parte. Quindi potrei non rifiutare la nulla troppo spesso rispetto a quello che vorrei. Quindi il test è impreciso. Però dal punto di vista metodologico sarebbe più corretto perché in qualche modo mi descrive tantissime forme di eteroschedasticità. Quindi ho due test. Uno è conservativo e non ha problemi di potenza del test. Non sbaglia troppo quando parlo, penso, agli errori del secondo tipo, però potrebbe non descrivere la varianza condizionale correttamente, perché ho troppi pochi regressori nel modello ausiliario.

Questa regressione potrebbe andar bene, però poi la statistica non mi viene in aiuto perché non è abbastanza precisa, quello sto dicendo. Uno potrebbe dire: però guardandoli tutti e due insieme mi posso fare un'idea precisa. Ricordatevi poi che ==a me non interessa neanche tanto sapere se vale più l'omoschedasticità contro l'eteroschedasticità, ma sapere eventualmente perché c'è eteroschedasticità==, perché poi mi può aiutare a specificare il modello sulla media condizionale, cioè il modello di regressione originale.

### Il test di White in Gretl

Detto questo, anche qua, quando voi avete stimato una regressione, calcolare il test di White è estremamente semplice. È un test in linea di massima di tipo F con restrizioni lineari. Cercate dal menu test della regressione il test di White, automaticamente il software si calcola tutto e vi fornisce questo tipo di informazione. Anche qua avete un p-value circa zero, vuol dire che confermate l'eteroschedasticità.

*(slide 35)*

## Che cosa si può dire dopo i test

In generale, se almeno uno di questi test vi conferma l'ipotesi di eteroschedasticità, vuol dire che almeno quella forma di eteroschedasticità c'è. Ma siccome non mi interessa sapere com'è fatta l'eteroschedasticità, vuol dire che siamo in un contesto omoschedastico, eteroschedastico.

> [!question] Da verificare: la trascrizione riporta "Ma siccome non mi interessa sapere com'è fatta l'eteroschedasticità, vuol dire che siamo in un contesto omoschedastico, eteroschedastico"; la frase è incoerente e il senso non è determinabile dall'audio.

Quando anche tutti i test che fate non rifiutano la nulla, quindi i test di Breusch-Pagan hanno un p-value grande, 25%, il test di White ha un p-value grande, ancora non vuol dire che siete nell'ambito dell'omoschedasticità, questo sto dicendo. Perché? Perché il primo test di Breusch-Pagan potrebbe non dare una descrizione corretta della varianza condizionale. Magari la varianza condizionale dipende da $x^2$ e non dipende da $x$, e quindi il Breusch-Pagan non ha $x^2$ nel modello e quindi non dirà contagio. Il test di White ha le variabili al quadrato. Il problema è che, siccome per costruire il test di White devo mettere troppi regressori, la capacità del test di essere preciso, soprattutto per quanto riguarda l'errore del secondo tipo, diventa scarsa. Quindi il test non è troppo preciso se avete troppi regressori. Quindi se avete il modello sufficientemente ragionevole per descrivere i dati, non funziona tanto bene. Quindi doveste avere, a livello grande, qualsiasi test di omoschedasticità di questo tipo vogliate fare, non potete comunque affermare che c'è omoschedasticità.

> [!question] Da verificare: la trascrizione riporta "non dirà contagio"; il termine non è chiaro.

> [!question] Da verificare: la trascrizione riporta "se avete il modello sufficientemente ragionevole per descrivere i dati, non funziona tanto bene" e "Quindi doveste avere, a livello grande, qualsiasi test"; le due frasi non sono chiare (forse "complicato" al posto di "ragionevole" e "a livello generale") e si lasciano come dette.

In realtà questo dovrebbe venire anche dalla statistica. ==Voi quando fate un test non accettate mai l'ipotesi nulla, la rifiutate o non la rifiutate.== In pratica, in questi test è ancora più chiaro il concetto di perché dico non rifiuto, perché il fatto che non posso accettare qualsiasi test, non mi permette di accettare l'omoschedasticità, mi permette di dire i dati sono abbastanza coerenti con l'omoschedasticità o non abbastanza coerenti con l'omoschedasticità, ma non mi danno una risposta definitiva. Non possono darmi una risposta definitiva, perché io non so qual è il vero modello che descrive la varianza condizionale. E questo dovrebbe essere ancora più chiaro perché non dico mai accetto, perché quando anche il p-value di questi test è grande per qualche motivo, non posso dire che sono nel caso dell'omoschedasticità, perché potrebbe esserci un'altra forma di eteroschedasticità plausibile, oppure il test non è abbastanza preciso. Per quello si dice: si rifiuta oppure non si rifiuta, ma non si accetta, perché in questo caso l'omoschedasticità non è veramente nulla. So qual è l'alternativa, ma la nulla. Il software mi dice: eteroschedasticità non presente oppure omoschedasticità, ma in realtà non è vero. Mi dice che quel tipo di eteroschedasticità non è presente, sotto la nulla, non l'omoschedasticità in generale. Questo era quello che vi volevo raccontare, per chiudere l'argomento.

## Come usare davvero i test di eteroschedasticità

Quindi, in sostanza, quando avete un modello di regressione usate sempre gli standard error robusti. Gli standard error usateli sempre, quelli robusti, perché così vi risolvete il problema. La speranza è che il campione sia sufficientemente grande per far sì che l'approssimazione robusta funzioni correttamente. Se avete pochi dati, comunque il modello è impreciso abbastanza, i risultati sono comunque imprecisi. Dopodiché i test di eteroschedasticità li posso fare per capire perché c'è eteroschedasticità eventualmente, perché questo mi può essere utile per costruire un modello migliore, niente di più. Non mi servono mai, in pratica, per decidere se sono nell'ambito dell'omoschedasticità o dell'eteroschedasticità, perché i test non sono abbastanza precisi per poterlo fare. In più, in teoria dovrei fare infiniti test con tutte le forme di eteroschedasticità possibili e immaginabili; se rifiuto sempre l'alternativa, allora in quel caso posso dire che c'è omoschedasticità, ma è impossibile, perché dovrei ottimare infiniti modelli.

> [!question] Da verificare: la trascrizione riporta "dovrei ottimare infiniti modelli"; il verbo non è chiaro (forse "stimare").

E quindi l'utilità di questi test è, primo, storica; secondo, da un certo punto di vista metodologica, perché dimostrare le proprietà di quei test è interessante anche dal punto di vista statistico, proprio come meccanismo scientifico, tra virgolette. Ma soprattutto mi serve per capire come la varianza può dipendere dai regressori stessi. Mi serve più per capire se queste informazioni possono essere utili per descrivere meglio il sistema economico. E questo è chiuso. Quindi nella vita reale, se ho fatto una regressione, usate sempre gli standard error robusti. Tutto il resto è ausiliario. Questo è quello che vi volevo raccontare.

## Gli esercizi di riepilogo

A questo punto penso che possiamo passare a una parte un po' più pratica e volevo farvi vedere questi esercizi di riepilogo. Sono compiti vecchi, e quindi cominciamo con questo.

> [!tip] Esame
> Questo è un compito che ho dato nel 2023, ma sono più o meno tutti uguali, quindi una volta che avete capito la filosofia degli esercizi cambia pochissimo da uno all'altro. Tipicamente un esame è organizzato così, ma forse l'avete già visto: un esercizio che tipicamente vi dà un output di una regressione. Dopodiché, sulla base dell'output della regressione vi chiedo di ottenere dei risultati.

### L'appello del 2023: i dati e il modello

Anche la soluzione, che ho qua, così so i numeri, senza doverli calcolare a mano. Giugno 2023.

> [!question] Da verificare: la trascrizione riporta "Giugno 2013"; il testo dell'appello riporta 15 giugno 2023 (e il docente ha detto "2023" poco prima), e si adotta "giugno 2023".

Allora, qua abbiamo l'output della regressione. La regressione descrive i prezzi delle case, in alcuni casi, in una certa zona degli Stati Uniti, in scala logaritmica, come funzione di una variabile. NOX è un fattore inquinante, è un'approssimazione della qualità dell'aria in quella zona, in scala logaritmica anche lui. Poi il tasso di criminalità, il livello, quindi è un indice che più grande è, peggio è. Numero di stanze della casa, numero di stanze al quadrato. ddist è la variabile dummy che è uguale a uno se la casa è lontana dai centri di interesse definiti in qualche modo, tipo dove la gente va a lavorare, dove ci sono i monumenti, dove ci sono i bar, praticamente, e zero altrimenti. Quindi zero è una zona comoda e uno è una zona scomoda. Questa è un'approssimazione, c'era nel dataset questo lavoro fatto da questi autori, pubblicato parecchi anni fa, ma per dare un esempio.

> [!question] Da verificare: la trascrizione riporta "DIST"; il testo dell'appello del 15/06/2023 riporta `ddist` (dummy uguale a 1 se il distretto è lontano dai centri lavorativi principali) e si adotta questa forma.

Dopodiché ho incluso una variabile che è il prodotto incrociato, come avete visto a lezione con Antonio, che è il prodotto tra una variabile dummy e un fattore inquinante, riscalato rispetto a uno per evitare qualche problema di collinearità, per esattezza. Quindi ricordate quella roba che avevate, il genre per il livello di istruzione che non funzionava perché vi dava qualche linearità e sceglievate la media.

> [!question] Da verificare: la trascrizione riporta "il genre per il livello di istruzione" e "qualche linearità"; probabilmente "gender" e "collinearità", ma non confermati dalle slide né dal testo dell'appello.
