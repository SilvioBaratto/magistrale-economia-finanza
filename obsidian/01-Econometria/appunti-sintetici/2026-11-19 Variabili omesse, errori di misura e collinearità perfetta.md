---
corso: Econometria
data: 2026-11-19
fonte: Materiali/audio/econometria/econometria_2026-11-19.txt
tipo: appunti-sintetici
tags: [appunti-sintetici, econometria]
revisione: sintesi a punti della nota fedele della stessa lezione
---

# Variabili omesse, errori di misura e collinearità perfetta

## Le cause dell'endogeneità

- L'endogeneità non è verificabile direttamente, quindi riconoscerla è un task abbastanza complicato.
- Conoscendone le possibili cause, si può lavorare a priori dal punto di vista logico per capire se c'è un problema.

> [!question] Da verificare: "in maniera di direzione multipla" e "endogenità"; si adottano "regressione multipla" e "endogeneità" delle slide 1 e 12 di ECON 03.

## I distretti californiani divisi in ricchi e poveri

- Esempio dei bambini californiani: performance scolastica, dimensione della classe, effetto reddito.
- Si dividono i distretti in ricchi e poveri e in ciascun gruppo si stima punteggio uguale ad alfa più beta per size più un termine d'errore (beta A per i distretti ad alto reddito, alfa B e beta B per i poveri). I termini d'errore sono diversi perché le sottopopolazioni sono diverse.
- In ogni sottogruppo le stime non dipendono dal reddito, perché è omogeneo: si elimina l'effetto della variabile confondente.
- Si suppone che epsilon non abbia un effetto sistematico. Se beta nei due sottocampioni non cambia, il reddito non ha impatto sulla correlazione tra le variabili chiave; se cambia, il reddito ha importanza.
- Beta è una misura di correlazione: covarianza fratto varianza, cioè la correlazione tra X e Y.

> [!question] Da verificare: "dello storno"; probabilmente "dello score".

## Dal campione diviso al modello unico

- La stima sui due sottocampioni si può fare in un'unica operazione con un modello di regressione multipla.

## Domande sui test

- I dubbi sui test vanno chiariti subito (a lezione, a ricevimento, per email, su Zoom): ==perché poi si userà molto nel compito quella statistica di base==.

> [!tip] Esame: la statistica di base si userà molto nel compito; i dubbi sui test vanno chiariti subito.

## Il modello con più variabili

- Per scrivere la struttura logica come regressione multipla si aggiungono variabili alla media condizionale: il valore atteso condizionale della Y dato X dipende da più di un fattore.
- X1 è la dimensione della classe, X2 il fattore confondente, il reddito.

## Variabili di interesse e variabili di controllo

- Le variabili del valore atteso condizionale sono di interesse (di policy) o di controllo.
- Al responsabile della didattica in California interessa beta1, la dimensione della classe. Il reddito, beta 2, serve solo per stimare bene beta 1: senza reddito potrebbe sbagliare a prevedere l'impatto di una riduzione della classe.
- Le variabili di controllo servono a ripulire il termine d'errore da effetti collaterali. A parte le variabili in più, il modello è definito come la regressione semplice.

## Il termine d'errore nel modello multiplo

- Il termine d'errore rappresenta tutte le caratteristiche dell'unità i-esima (per esempio il distretto 57, Orange County) che non sono né reddito né dimensione della classe, come la percentuale di non madrelingua o la qualità delle scuole.
- Nel modello semplice y aveva dentro anche questo fattore, perché non era nella media condizionale. È un bidone della spazzatura.

> [!question] Da verificare: "pidone alla spazzatura"; probabilmente "bidone della spazzatura".

*(slide 8, regressione multipla)*

## Che cosa sono beta1 e beta2

- Beta non è più la correlazione marginale ma una correlazione condizionale: la dipendenza tra due variabili al netto di una terza.
- Si vuole prevedere la performance attesa di un distretto con caratteristiche x1 e x2, con la barra a indicare un valore generico.

> [!question] Da verificare: "la performance a tela di un distretto"; probabilmente "la performance attesa di un distretto".

- Si fissa il reddito e si confrontano due distretti identici per reddito, ricco con ricco, modificando leggermente la dimensione della classe in uno solo.
- Delta Y, con i tre segnetti a indicare una definizione, è la differenza di valori attesi nei due scenari: dipende dalla variazione della X, che si decide, non da X2 che è costante, e dall'impatto di epsilon nei due scenari.
- Con incorrelazione tra X1, X2 ed epsilon, la parte condizionale è nulla e la variazione attesa di Y dipende solo dal pezzo legato a beta1. È una variazione attesa, non numerica.
- Ipotizzare che in media epsilon non conti niente si dice ipotizzare l'esogeneità: i fattori non messi nel modello non hanno un impatto sistematico sulle relazioni tra variabili.

## Correlazione parziale ed effetto marginale

- Beta1 dice quanto una variazione di X ha impatto in media sulla Y, ma non è la correlazione del modello semplice: qui si controlla per il reddito, ipotizzato costante.
- Beta uno è la correlazione tra y e x1 al netto di x2, una correlazione condizionale, parziale: dice quanto aumenta la performance con una riduzione della classe in distretti con lo stesso reddito.
- Ipotizzando che la media di y, fissati gli x, sia uguale a zero, quegli y non hanno effetto sistematico e si possono buttare via.

> [!question] Da verificare: "la media di y, fissati gli x" e "quegli y"; sembra epsilon (slide 23 di ECON 03: $E[\epsilon \mid X] = 0$), ma si lascia aperto.

- Primo punto: ==beta uno non è più una correlazione, ma una correlazione al netto dell'altra variabile, quindi una correlazione parziale==.
- Secondo punto: lo schema replica il ragionamento grafico, più grezzo, con distretti sopra e sotto la mediana. Per qualsiasi livello di x due si calcola la correlazione parziale: ==un modello di regressione multipla mi replica questo schema intuitivo==.
- Si isolano gli effetti controllando per i fattori confondenti, purché siano dentro il modello in modo esplicito e non in epsilon: ==ricordatevi che epsilon non è osservabile==.
- Lo scopo è sempre beta uno; beta due non è rilevante.
- ==il parametro beta uno viene chiamato effetto marginale, cioè effetto di una variabile sulla y al netto di tutte le altre==: qui, fissato il reddito, integrato via l'effetto di x due.

## La regressione sui dati californiani, senza e con il reddito

- Senza controllare per il reddito il coefficiente beta è circa meno 2,27, con p-value zero: statisticamente significativo, candidato a una relazione causa-effetto.

*(slide 4, regressione multipla)*

- Con il reddito la regressione ha tre parametri: str, la dimensione della classe (student-teacher ratio), e average income, il reddito medio.

> [!question] Da verificare: "R-squared" e "staff-student teacher ratio"; la slide 11 riporta "str" e si adotta; "student-teacher ratio" è solo probabile (la slide 3 dice "rapporto studenti-insegnanti").

- Il coefficiente della classe non è più meno 2,2 ma meno 0,64, meno di un terzo. È debolmente significativo: p-value 6,8%, a un livello del 5% non si rifiuta l'ipotesi nulla. Nell'intervallo di confidenza il limite inferiore è negativo e il superiore positivo, quindi zero è un valore possibile.
- L'effetto reddito è 1,8, significativo, con intervallo di confidenza solo positivo; ci si aspetta un parametro positivo.

*(slide 11, regressione multipla)*

- Si sommano in valore assoluto beta 1 e beta 2, che hanno effetti diversi (ridurre di un'unità la classe, aumentare di un'unità il reddito): 0,64 più 1,83 è più o meno il 2,2 stimato prima, al netto del segno. Il docente non sa se è un caso.

> [!question] Da verificare: "0,64 più 1,83 è più o meno il 2,2"; con le slide 11 e 4 la somma è circa 2,49 e il coefficiente semplice 2,2798. Si riporta quanto detto.

- Il modello semplice stima la combinazione dell'effetto classe e dell'effetto reddito; senza reddito nel modello, tutto il peso di meno 2,2 è assegnato alla classe.

## Perché il modello più complicato è preferibile

- Aggiungere un regressore scompone gli effetti in modo esplicito: il modello ha senso logico, si stima sui dati e migliora il precedente.
- Se il coefficiente del reddito fosse non significativo si resterebbe nel modello semplice (rasoio di Occam: tra due spiegazioni che funzionano si preferisce la semplice). Qui il modello complicato cambia le conclusioni e fa rifiutare il precedente: si è obbligati ad andarci, la stima è più precisa.
- Non è detto che sia una relazione causale: si continuerebbe aggiungendo fattori, togliendoli dal termine d'errore e mettendoli nella media condizionale, in coerenza con un'idea teorica, economica, sociologica, pedagogica.

## Fino a che punto aggiungere variabili

- Si inseriscono variabili finché il parametro di interesse non si stabilizza: quando beta 1 è insensibile a nuove variabili, ciò che non si mette non conta più. È un'idea di lavoro.
- Beta 2, beta 3 e beta 4 non interessano; interessa se vale la pena investire 2 miliardi di dollari l'anno per quell'idea pedagogica.

> [!question] Da verificare: "beta 2 e beta 3 da 4"; probabilmente "beta 2, beta 3 e beta 4".

## La distorsione da variabile omessa

- Il vero processo è: la media di Y dato X1, X2 ed eventualmente altre variabili è uguale ad alfa più beta1 X1 più beta2 X2; in generale non è noto.
- Il modello statistico semplice è alfa tilde più beta tilde più epsilon tilde (il segnetto indica parametri ed errori diversi da quelli del processo). Il modello di regressione corretto ha in più beta due x due i e il termine d'errore, per il matching tra osservazioni e valore atteso condizionato.
- Lo stimatore di beta tilde è la covarianza tra y e x uno fratto la varianza di x uno. Riscrivendo y secondo il vero modello: covarianza tra alfa più beta uno x uno più beta due x due più epsilon, e x uno, diviso la varianza di x uno.

> [!question] Da verificare: "più y, e x uno"; la covarianza con epsilon dopo fa pensare a "più epsilon", ma si lascia aperto.

- Scomposta in somma: alfa e x uno zero perché costante; beta uno per la varianza di x uno; beta due per la covarianza tra x uno e x due; la covarianza tra epsilon e x1.
- Risultato: beta1 più beta2 per la covarianza tra x1 e x2 fratto la varianza di x1, più la covarianza tra epsilon e x1, che è zero perché nel vero modello vale l'esogeneità.
- Lo stimatore non è legato solo a beta1: è il vero segnale più un effetto che dipende dalla correlazione con la variabile tolta dal modello. Si ottiene la somma di due numeri, per esempio meno 2,2 uguale a meno 0,5 più 1, meno 1,8, "adesso una roba così".

> [!question] Da verificare: "meno 0,5 più 1, meno 1,8, adesso una roba così"; i numeri sono detti per esempio e non tornano con meno 2,2.

- ==Se prendo un modello e ci metto troppe poche variabili, quello che stimo è una combinazione di effetti==: beta 1 e la struttura di correlazione tra la variabile omessa e la variabile inclusa.
- È endogeneità, perché ==nel modello piccolo, epsilon tilde è dato dal vero epsilon, quello del modello vero, più beta 2 x2==: ciò che non si mette resta nell'errore, e x2 e x1 potrebbero essere correlati.

> [!question] Da verificare: "se lo metto qualcosa vuol dire che resta qua dentro"; probabilmente "se non lo metto".

- Se x1 e x2 hanno covarianza zero, o se beta2 è zero, l'effetto distorsivo è zero: escludere una variabile inutile o incorrelata non cambia nulla. Se è molto piccolo, il problema è trascurabile.
- Una delle cause più importanti di endogeneità è un modello statistico non coerente con il modello teorico che non conosciamo.

## Come accorgersi della distorsione da variabili omesse

- Si parte da un modello semplice e si aggiungono regressori un po' alla volta, togliendo i fattori confondenti: semplificando il termine d'errore, la probabilità di endogeneità è più bassa.
- Con un modello troppo piccolo, escludendo variabili rilevanti, si stima beta più qualcosa: nei testi è la distorsione da variabili omesse.
- L'endogeneità non si valuta a priori, non si può verificare se l'errore è correlato con le X, ma se ne vedono le conseguenze: se la stima di un parametro oscilla molto al variare del modello, probabilmente c'è endogeneità.
- Se il parametro resta stabile dopo tanti esperimenti si va nella direzione giusta: è un metodo di lavoro più robusto.

## Il campione grande non risolve il problema

- Stimando il modello sbagliato si stima beta più la correlazione tra x inclusa e x esclusa, che non sparisce con n: con 10.000, 100.000, un milione di osservazioni non tende a zero.
- Asintoticamente lo stimatore converge al vero parametro più una costante non calcolabile ma esistente. L'unica speranza è un modello con covarianza tra x ed epsilon uguale a zero.
- ==La dimensione del campione non aiuta==. È il primo caso di endogeneità.

## Più regressori del necessario

- È un secondo caso di endogeneità, più sottile, non presente nei lucidi.

> [!question] Da verificare: "non c'è nelle luci"; probabilmente "non c'è nei lucidi".

- Con tre regressori anziché due il problema non si pone: il terzo avrà stima circa zero e beta 1 e beta 2 non cambiano. Al più gli standard error diventano un po' più grandi, perché lo si fissa alla covarianza campionaria anziché a zero.
- ==Mettere più regressori del necessario non è un problema, metterne meno del necessario è un problema==. Metterne troppi pochi è un problema sostanziale.

## Errori di misura

- È un'altra causa di endogeneità, più sottile: il modello è perfetto sulla carta, con tutte le variabili necessarie.

> [!question] Da verificare: "Non solo il problema di stimarlo"; senso non chiaro, forse "resta solo il problema di stimarlo".

- Il regressore però non si osserva con precisione, se ne ha solo un'approssimazione. Esempio: il consumo delle famiglie italiane da sondaggi (Istat). Chi ha speso 160 euro ricorda 150; la volta dopo spende 140 e riporta 150. L'approssimazione è onesta: a volte sovrastima, a volte sottostima.
- Setup: la y è legata alla x dal modello economico corretto, quindi la correlazione tra y e x è zero. Si osserva x con l'asterisco, uguale al vero x più il coefficiente di distrazione, una variabile casuale con media zero e varianza qualcosa.
- Il coefficiente di distrazione non dipende da epsilon né da quanto si spende (se sono scemo al 10% lo sarò sempre): la covarianza tra x e u è zero, la covarianza tra u e epsilon è zero.

*(slide 17, regressione multipla)*

## Il modello calcolabile e il parametro gamma uno

- Si stima con i dati che si hanno al posto di x, quelli del foglio Excel, con parametri gamma zero e gamma uno del modello statistico, distinti da alfa e beta del processo che genera i dati.

> [!question] Da verificare: "Questo è il modello calcolabile, è quello del vero processo generatore"; probabilmente "non è quello".

- La domanda è se gamma uno sia legato a beta. Si stima $Y = \gamma_0 + \gamma_1 X^* + \epsilon$: gamma uno è la covarianza tra y e x con la stellina, diviso la varianza di x con la stellina, dove x con la stellina è il vero x più il coefficiente di distrazione.

> [!warning] Correzione: il docente ha usato u per due quantità e correggerà i lucidi; la slide 17 usa u per l'errore di misura e ε* per l'errore della regressione calcolabile.

- Si riscrive y in funzione del vero x e del vero beta: covarianza tra y e x star, che è x più u, diviso la varianza di x più u.

> [!question] Da verificare: "Sì, posso farlo il trappassaggio in meno, quindi"; probabilmente "posso fare un passaggio in meno".

- Rispetto al processo che genera i dati è la covarianza tra y e x più la covarianza tra y e u, diviso la varianza di x più u. Sviluppando: beta per la varianza di x fratto la varianza di x più u, più la covarianza tra x e y fratto la varianza di x, più la covarianza yu fratto la varianza di x.

> [!question] Da verificare: "la covarianza tra x e y" come secondo termine; dal seguito ("x è esogeno rispetto ad epsilon") sembra x ed epsilon, ma si lascia aperto.

- La covarianza tra x ed epsilon è zero perché il modello con il vero x è perfetto. Si ipotizza che l'imprecisione non dipenda dalla y, quindi anche la covarianza tra y e u è zero: gamma uno è uguale a beta per la varianza di X.
- Il denominatore è la varianza di X più la varianza di U più due volte la covarianza, zero perché X e U sono incorrelati (l'imprecisione è sempre 10%).

## Il rapporto minore di uno

- ==Stimando il modello di regressione con errore di misura, non vado a stimare beta, ma vado a stimare beta che moltiplica un rapporto minore di uno==.
- È minore di uno per costruzione, perché il denominatore è sempre più grande del numeratore.
- Se la varianza di U è piccola il rapporto tende a uno e gamma e beta coincidono; se è uguale alla varianza di X il rapporto è uno fratto due, un mezzo, e si stima beta per un mezzo.

## Un esempio con dati simulati

- Dati simulati dal modello semplice: duecento osservazioni, epsilon e x normali N(0,1). Il coefficiente di x è 1,42 e la costante 3,07; i veri valori, 1,5 e 3, stanno negli intervalli di confidenza: il modello funziona.

> [!question] Da verificare: "la normale 0,1"; la slide 20 riporta ε ∼ N(0, 1) e u ∼ N(0, 1), e si adotta N(0,1).

*(slide 19, regressione multipla)*

- Con il regressore perturbato, x con la stellina uguale a x più un errore u normale con media zero e varianza uno (la varianza di x è uno): intercetta stimata 3,13, intervallo tra 2,93 e 3,33, che contiene l'errore del parametro. Beta stimato 0,7, l'errore del parametro 1,5.

> [!question] Da verificare: "l'errore del parametro" (due volte); probabilmente "il valore del parametro" (3 e 1,5).

- Con stima poco precisa un test potrebbe non rifiutare, ma l'intervallo di confidenza va da 0,55 a 0,85 più o meno: 1,5 non ci sta dentro neanche da vicino. Il risultato è sistematicamente diverso dalla verità e il campione non è troppo piccolo, perché il modello precedente ha funzionato.

*(slide 20, regressione multipla)*

## L'attenuation bias

- Lo 0,7 è 1,5 per un mezzo: la varianza di x è 1, la varianza di u è 1, quindi si stima beta che moltiplica un mezzo.
- Con beta positivo le stime sono sistematicamente più basse, circa la metà: si chiama attenuation bias, sottostima regolare del parametro di interesse.
- La distorsione è la differenza tra beta e un mezzo beta; è circa 0,75, la metà di un mezzo. L'esempio ha bias e coefficiente un mezzo uguali; si rifarà con la varianza di u diversa da quella di x.
- Con dati imprecisi, da campionamento fatto male, la stima è cattiva anche con il modello perfetto.

> [!question] Da verificare: "la distorsione è circa 0,75, la metà di un mezzo"; la slide 21 riporta la metà del vero valore, circa 0.75. Si riporta quanto detto.

*(slide 21, regressione multipla)*

## Gli errori di misura in finanza

- Sono frequenti perché ci sono procedure di stime ripetute: i coefficienti di una prima regressione sono usati come regressori in una seconda, per esempio per validare il CAPM. Sono variabili approssimate, il vero valore al netto di un errore campionario, e possono creare endogeneità.
- Esempio: la volatilità di un investimento come regressore della performance non è osservabile, si stima: è la migliore approssimazione, non un indicatore esatto. Crea endogeneità, con stimatori che tipicamente sottostimano il vero valore del parametro.

## Ridurre l'errore di misura con la media di più osservazioni

- Istituti seri (Istat, Banca d'Italia, istituti di ricerca) cercano di correggere il problema; con dati cattivi la stima è cattiva anche con il modello migliore.
- Si osserva la famiglia i-esima per un periodo lungo, per esempio dieci settimane: x1, x2, x10, ciascuna con varianza uguale alla varianza di u, l'imprecisione fisiologica.
- Si usa come regressore la media aritmetica: uno fratto dieci, in generale uno fratto n, per la sommatoria degli xj della famiglia i per j da uno a dieci, o a n.
- La varianza della media è uno fratto n per la varianza di u, con osservazioni indipendenti (passaggi nei lucidi dei richiami di statistica).
- Con dieci informazioni e precisione 10%, la varianza della media è uno fratto 10 per 10%, circa l'1%: il rapporto varianza di x fratto varianza di x più varianza di u diventa praticamente uno. Più grande n, più piccolo l'effetto dell'imprecisione.
- Al volo: chiedere quattro o cinque volte e fare la media. Ci sono tecniche più sofisticate, perché chiedere dieci volte è costoso. Il problema va risolto a monte.

## Errori di misura ed endogeneità

- Con dati da una survey su internet fatta al volo gli errori di misura rischiano di non essere considerati e le stime sono pesantemente distorte anche con il modello corretto: è il secondo caso di endogeneità.
- ==se sapete a monte che i vostri dati potrebbero avere un errore di misura, allora automaticamente dovreste pensare al concetto di endogeneità==. Se c'è endogeneità c'è distorsione.
- Nella regressione stimata la covarianza tra regressore e termine d'errore è proporzionale alla varianza dell'errore di misura, non comprimibile: lo stesso risultato visto da un altro punto di vista.

> [!tip] Esame: la formalizzazione dell'endogeneità da errore di misura sui lucidi non è così importante.

*(slide 18, regressione multipla)*

## La volatilità stimata e i dati ad alta frequenza

- La volatilità nel modello è uno stimatore, quindi un errore di misura, lo standard error della stima: attenzione alla distorsione delle stime.
- Nelle applicazioni recenti si usano dati ad alta frequenza, osservati ogni tot secondi (in un giorno 100.000 osservazioni sulle variazioni di prezzo di Standard & Poor's), per stimare la volatilità del giorno mediando 4-500 osservazioni: precisione estremamente alta.

> [!question] Da verificare: "sto vediando 4-500 osservazioni"; probabilmente "sto mediando", e il numero non coincide con le 100.000 dette prima.

- Con un modello di tipo ARCH la stima si basa su un'unica osservazione, il rendimento del giorno: in media buona ma non molto precisa.
- L'idea è usare più dati; i dati intragiornalieri possono essere utili con accorgimenti, perché troppi dati potrebbero essere problematici (più avanti).

## I due casi di endogeneità visti finora

- Ci sono due concetti di endogeneità. "Finisco il quarto oggi."

> [!question] Da verificare: "Finisco il quarto oggi"; senso non chiaro.

- È una covarianza, un concetto astratto: il problema è capire quando è diversa da zero.
- Primo caso, troppe poche variabili: se ne aggiungono di più, in modo sensato, preservando la logica del modello, per vedere se l'effetto distorsivo c'è o sparisce. Il secondo problema, concettualmente più semplice: si aggiunge informazione finché la stima del parametro di interesse non si stabilizza.

> [!question] Da verificare: "Il secondo problema, quindi, è più semplice"; dal seguito sembra il primo caso (variabili omesse).

- L'errore di misura è più sottile perché non dipende da chi modella: con dati poveri le stime sono sbagliate anche con il modello migliore. Ci si affida a dataset affidabili e standardizzati, sapendo che il problema c'è.

## L'errore di misura sulla y

- Non è sui lucidi: ci si aspetta ancora peggio, invece ==se ce l'ho sulla y non cambia niente==.
- Aumentano solo gli standard error di tutti i coefficienti, perché l'errore di misura entra nel termine d'errore. Con y più u il gamma stimato è uguale a beta: cambia la varianza di epsilon, non la distorsione. È la seconda casistica.

> [!warning] Correzione: il docente corregge l'aspettativa che l'errore sulla y sia ancora peggio: non cambia niente, aumentano solo gli standard error.

> [!question] Da verificare: "siccome ancora è correlato con x, è correlato con qualsiasi cosa"; dal senso probabilmente "non è correlato", ma si lascia aperto.

> [!question] Da verificare: "la varianza di e, del termine d'errore"; probabilmente "la varianza di epsilon".

## Una domanda sul segno meno

- Uno studente fa una domanda interrotta su gamma. Il docente: c'è un meno che si trasferisce quando calcola la varianza; ha saltato i passaggi perché gli sembra più intuitivo così, con l'algebra più lineare.
- Il meno viene dal fatto che la distorsione è beta meno questa roba, che è più piccola: la distorsione è nel senso negativo.

> [!question] Da verificare: domanda incompleta; la slide 18 riporta $\mathrm{Cov}(X^*, \varepsilon^*) = \gamma \,\mathrm{Var}(u)$ senza segno meno, ma non si sa se la risposta si riferisca a quella riga.

## Altri casi di endogeneità

- La regressione multipla è la regressione semplice con più variabili; visti due casi di endogeneità, ne verrà almeno un altro prima della fine del corso, solo nell'ambito delle serie storiche.
- Altri casi, quando non si sa se è la X che causa la Y o viceversa, non si trattano in questi modelli: capita nei modelli macro.

## Le ipotesi per stimare il modello

- Il modello deve essere lineare nei parametri; può essere non lineare nelle variabili (logaritmo, polinomio).
- ==la covarianza tra X ed epsilon, qualsiasi X nel modello, deve essere uguale a zero, quindi esogeneità, quella è la cosa importante==.
- I dati sono campionati in maniera indipendente dalla popolazione, almeno in questa parte del corso.
- C'è un'ipotesi tecnica per applicare il teorema del limite centrale e la legge dei grandi numeri e fare inferenza asintotica.

> [!question] Da verificare: "teorema del limite centrale alla legge dei grandi numeri" e "inferenza sintotica"; si adottano "e la legge" e "asintotica" (slide 45 di regressione semplice).

*(slide 25, regressione multipla)*

## I momenti fino al quarto ordine

- Servono momenti fino al quarto ordine finiti per X e Y: la dispersione non può essere troppo grande, le code non troppo pesanti, e la media teorica deve essere calcolabile. Con una Cauchy, o una t-Student con tre gradi di libertà, non si hanno i momenti.
- Esempio: la media del reddito in Texas. Pescare un Elon Musk, con miliardi di dollari, distorce tutto al rialzo: reddito medio 60 milioni di dollari. Non si vogliono troppi outlier né varianze esplosive.
- Per ora si ipotizza l'omoschedasticità; poi si vedrà l'eteroschedasticità.

## La perfetta collinearità

- Nella regressione multipla serve un'ipotesi in più: evitare la perfetta collinearità tra i regressori. Le X sono correlate tra loro (reddito e classe), ma il problema è la correlazione uguale a uno: conoscendo una variabile si prevede esattamente l'altra.
- Esempio: il salario rispetto a istruzione e genere, per capire se a parità di genere ci sono distorsioni salariali tra uomini e donne, cioè un effetto sistematicamente distorsivo indipendente da istruzione e capacità. È un problema gravissimo.

> [!question] Da verificare: "a parità di genere" con il confronto tra uomini e donne; probabilmente "a parità di istruzione", ma si lascia aperto.

- Modello: salario uguale ad alfa più beta uno istruzione più beta due m più beta tre f più epsilon. M è uguale a uno se il lavoratore è maschio; F è zero se è di genere maschile e uno se femminile.

> [!question] Da verificare: "che la sovradefinisco"; probabilmente "che adesso definisco".

> [!question] Da verificare: "Cioè genere maschile è zero, femmina,"; frase lasciata a metà che contraddice le definizioni, si omette.

- M e F sono correlatissime, correlazione esattamente uno: se M è uno F è zero, e se M è zero F è uno.
- Beta 2 è l'effetto di essere maschio al netto delle altre variabili. Per l'effetto marginale si modifica M tenendo fisse le altre, ma modificando M cambia anche F. Non è un problema di campione, è sistematico, deterministico.
- M e F sono perfettamente collineari: il modello statistico non è correttamente specificato. Si dovrebbero stimare quattro parametri, alfa, beta 1, beta 2, beta 3, ma non si identificano gli effetti marginali.

## Il modello riscritto e il problema di identificazione

- Con M uguale a 1 meno F: salario uguale ad alfa più beta 1 education, più beta due per uno meno F, più beta tre F, più epsilon. I due modelli sono equivalenti. Riordinato: intercetta alfa più beta due, beta uno per education, beta due più beta tre per F.
- Il modello sopra ha quattro parametri; stimando l'altro (costante, education, F) se ne ottengono tre (visto con Peruzzi), perché i parametri stimati sono tanti quanti i regressori.
- Nel secondo si stima un alfa cappellino uguale ad alfa più beta due, un beta uno cappellino uguale a beta uno, un beta due cappellino uguale a beta due più beta tre (improprio, non formalmente corretto).
- Sono tre equazioni con quattro incognite, con infinite soluzioni: un problema di identificazione. Aggiungere F o M aggiunge un parametro ma non informazione per la stima.

## Fissare beta tre a zero

- Si fissa beta 3 uguale a 0, la soluzione più semplice: la stima coincide con beta 2 e l'alfa con l'alfa.
- Non crea problemi di interpretabilità: non si tolgono le donne dal campione, si toglie un regressore ridondante. Come si interpreta il modello, domani.
- ==non posso più fissare tutte le variabili e muoverne una per calcolare l'effetto marginale==. Matematicamente è un sistema di tre equazioni e quattro incognite, impossibile: si fissa un parametro a zero, si toglie il regressore e si vede cosa succede alle altre variabili dipendenti.

> [!question] Da verificare: "alle altre variabili dipendenti"; probabilmente "indipendenti" (slide 25), ma si lascia aperto.

## Una domanda sul coefficiente di F

- Lo studente chiede della riga con il coefficiente di F beta due più beta tre. Il docente: ha ragione, beta due va con il segno meno; raccogliendo F ottiene beta tre meno beta due. Domani si continua.

> [!warning] Correzione: il coefficiente di F nel modello riscritto è beta tre meno beta due e non beta due più beta tre.
