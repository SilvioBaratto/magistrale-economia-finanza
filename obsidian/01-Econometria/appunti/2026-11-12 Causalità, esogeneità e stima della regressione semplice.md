---
corso: Econometria
data: 2026-11-12
fonte: Materiali/audio/econometria/econometria_2026-11-12.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-12
---

# Causalità, esogeneità e stima della regressione semplice

## Le condizioni della relazione causale

La lezione procede nello specifico, mantenendo una componente di intuizione. Il docente la considera la cosa più importante da capire, perché una volta acquisita l'intuizione formalizzarla con concetti statistico-matematici è abbastanza semplice.

Nella lezione precedente sono state introdotte le relazioni causa-effetto, che devono avere tre caratteristiche sostanziali. La prima è che tra le variabili di interesse ci sia una correlazione. La correlazione però non basta: tra variabili aleatorie quantitative è un concetto simmetrico, per cui la correlazione tra Y e X è uguale a quella tra X e Y, mentre la relazione causale è unidirezionale, nel senso che una X ha un impatto su Y ma non viceversa. Il controesempio, scherzoso, era quello dei boy scout e della probabilità di avere un record giudiziario non ottimale. L'associazione tra due variabili può spiegare un fenomeno ma anche il fenomeno reciproco, e in quel caso non si può parlare di relazione causale.

### L'esempio della dimensione della classe in California

Un esempio più vicino a ciò che si farà nel corso è quello di cui sono disponibili i dati. Riguarda un problema posto in California qualche anno fa: investire in una politica pubblica per migliorare il livello scolastico dei bambini può essere utile oppure no? Definire un programma di questo tipo pone vari problemi, il primo dei quali è che cosa significhi "utile". Questo però non è un problema dell'econometrico o dello statistico, è un problema più filosofico.

Il problema concreto riguarda i bambini della scuola prescolastica (asilo, scuola dell'infanzia): ridurre la dimensione delle classi può migliorarne l'apprendimento? È intuitivo pensare di sì, perché in classi più piccole l'insegnante riesce a dedicare più tempo a ogni singolo bambino, con miglioramenti nelle capacità pratiche e astratte. Si vuole quindi capire se la policy sia utile, cioè se riducendo la dimensione della classe i bambini vadano meglio a scuola, intendendo con questo che ottengano risultati migliori nei test di fine anno.

Attuare una policy del genere però costa molto. Occorre assumere più docenti e riorganizzare le classi: se ci sono 100 bambini e li si distribuisce in classi da 10 anziché da 20, servono più classi, più computer e più attrezzatura. L'investimento è stato quantificato, a memoria del docente, in circa 1,8 miliardi di dollari l'anno. Vale la pena farlo? Dipende dal fatto che la variabile su cui si interviene sia in relazione causale con la performance dei bambini. Serve quindi un modello causale che dica se la dimensione della classe sia un driver, non statistico ma logico, di tale performance.

### I dati e la correlazione negativa

Per l'analisi sono stati raccolti dati reali sui distretti scolastici. La California è divisa in circa 420 distretti, e ogni pallino del grafico rappresenta un distretto. Sull'asse delle x c'è la dimensione media della classe nella scuola dell'infanzia del distretto, sull'asse delle y il punteggio medio dei bambini del distretto in un test. Il test valuta competenze di matematica, logica e lingua adatte all'età dei bambini ed è standardizzato.

Facendo passare una retta che approssimi la nuvola di punti, si osserva che la pendenza è negativa: all'aumentare della dimensione media della classe la performance tende a diminuire leggermente. Se la diminuzione sia piccola o grande è una valutazione che non spetta a questa analisi. La pendenza negativa significa, come si formalizzerà più avanti, che la correlazione tra le due variabili è minore di zero. Rispetto alla ricerca di una relazione causale, questo è il primo ingrediente.

Il secondo ingrediente è una spiegazione logica per cui una classe più piccola può avere effetti benefici sulla performance dei bambini. Il docente la ritiene soddisfatta in termini generali: dal punto di vista dell'attenzione che ogni bambino riceve dal docente, in teoria le classi più piccole sono più focalizzate e si lavora meglio. Non è detto che la spiegazione sia corretta, ma è plausibile. Si è dunque trovata una correlazione e una spiegazione più o meno sensata.

### Il terzo ingrediente: escludere spiegazioni alternative

Il terzo ingrediente deve valere perché si possa parlare di relazione causale: bisogna poter escludere altre spiegazioni più convincenti. Occorre cioè chiedersi se l'effetto benefico della dimensione della classe sia la migliore spiegazione disponibile, sensata e coerente con la statistica. Per stabilirlo si devono fare altri esperimenti e provare modelli alternativi. Una spiegazione esaustiva non si troverà, perché non si possono costruire infiniti modelli che spieghino la correlazione negativa in modo alternativo. L'idea è che, avendo una teoria da verificare, si considera una serie di alternative ragionevoli per vedere se la teoria resta la strategia migliore o se c'è qualcosa di meglio.

Come già detto nella lezione precedente, non ci sarà mai una soluzione corretta in assoluto, ma una soluzione che si muove nella giusta direzione con criteri di scelta sostanzialmente razionali.

Stimando la pendenza della retta di regressione si può valutare, per esempio, se la riduzione di un'unità della dimensione della classe produca un beneficio di 10 punti al test. Il docente precisa che 10 punti possono essere molti o pochi, a seconda della scala del test. Il problema ora, però, non è quantificare gli effetti ma capire se esistano modelli migliori, e questi possono passare per l'analisi congiunta di altre variabili.

Una di queste è il reddito, che ha impatto su fondamentalmente tutte le scelte. Il reddito può spiegare in modo più convincente la relazione negativa tra dimensione della classe e performance? Dal punto di vista della catena logica può essere, perché i distretti ad alto reddito potrebbero avere performance migliori. In un distretto ad alto reddito le famiglie possono permettersi di comprare più libri ai bambini, e questo può riflettersi in una migliore performance scolastica.

Un'altra possibilità è che i distretti ad alto reddito abbiano scuole mediamente migliori. Trattandosi di dati americani, il distretto di appartenenza conta. Dove ci sono buone scuole pubbliche, la scuola privata costa moltissimo già dalle elementari, nell'ordine di decine di migliaia di dollari l'anno. Chi non può permettersi queste cifre vorrebbe una scuola pubblica, ma il livello delle scuole pubbliche è abbastanza eterogeneo. In alcuni distretti ci sono scuole pubbliche molto buone, e questo si riflette nel prezzo delle case della zona, che è estremamente più alto. La scuola pubblica buona, che costa relativamente poco, si trova quindi in un distretto ricco. Il reddito può dunque avere un effetto sulla qualità della scuola, che a sua volta incide sulla qualità dei risultati dei bambini.

Il reddito potrebbe così avere un effetto positivo sulla performance e un effetto negativo sulla dimensione della classe, perché le scuole migliori hanno già classi più piccole, magari perché hanno più insegnanti. Il docente osserva che negli Stati Uniti il concetto di dimensione della classe è un po' particolare: non ci sono necessariamente classi fisse, perché le classi si formano di volta in volta, e la dimensione viene calcolata come rapporto studenti-insegnanti. Una scuola migliore può avere più insegnanti e altre caratteristiche favorevoli.

Si vuole quindi vedere se esiste una relazione negativa tra reddito e dimensione della classe e una relazione positiva tra reddito e performance. In tal caso la relazione negativa osservata tra le due variabili iniziali potrebbe passare per l'effetto del reddito. Il reddito agisce con segno diverso sulle due variabili; se lo si omette, si vede soltanto la correlazione marginale tra dimensione e performance.

> [!question] Da verificare: la trascrizione riporta "se lo ometto vedo solo la marginale, vedo la correlazione condizionale"; probabilmente il docente intendeva che omettendo il reddito si vede la correlazione marginale e non quella condizionale al reddito.

### Come verificare il ruolo del reddito

Come stabilire quale dei due modelli sia migliore è ciò che si farà con i modelli statistici. Si vuole evitare che il reddito sia il vero driver, e quindi si controlla per il reddito. Se due distretti che non differiscono per reddito mostrano una correlazione alta o bassa tra le variabili chiave, il reddito non è un fattore determinante. Condizionandosi a distretti molto simili e studiando la correlazione tra performance e dimensione della classe, tale correlazione non può dipendere dal reddito, perché il reddito è uguale per tutti. Prendendo due distretti molto ricchi e calcolando tra loro la dipendenza tra dimensione della classe e performance, la correlazione non può dipendere dal reddito, perché le osservazioni provengono da un contesto molto omogeneo.

L'obiettivo è valutare se la correlazione stimata in precedenza, cioè la pendenza della retta rossa del grafico, sia spiegabile tramite il reddito. Il campione si divide in due sottoinsiemi, distretti ricchi e distretti poveri, e all'interno di ciascun sottocampione si studia la dipendenza tra le variabili chiave. Se la dipendenza non cambia, il reddito non è un fattore rilevante e aggiungerlo non ha alcuna utilità pratica. Se invece le correlazioni cambiano a seconda che si considerino distretti ricchi o poveri, il reddito è un fattore determinante, e per spiegare logicamente la correlazione negativa osservata tra performance e dimensione della classe bisogna passare per il reddito.

Per validare l'introduzione di una nuova variabile si controlla dunque se essa abbia un impatto sulla relazione di interesse. Quello che interessa al responsabile politico della California (provveditore, ministro o equivalente) è se i circa due miliardi di dollari l'anno da spendere servano a migliorare la performance. Se la correlazione negativa risultasse un semplice effetto collaterale del reddito, assumere nuovi docenti probabilmente non sarebbe particolarmente utile. Sarebbe forse più opportuno dare sussidi alle famiglie meno ricche, se l'obiettivo è migliorare la performance.

In pratica si prendono i 420 distretti, li si divide in ricchi e poveri e si calcola la correlazione tra performance e dimensione della classe tra i distretti ricchi e, allo stesso modo, tra i poveri. Se i due numeri sono diversi, il reddito ha potere esplicativo per il fenomeno. Se restano uguali, la relazione è la stessa indipendentemente dal reddito. Dal punto di vista operativo, se i dati dicono che un modello più complesso non vale la pena, tanto vale usare il modello logico precedente, quello senza reddito. Se invece i numeri sono diversi, aggiungere il reddito è importante, il modello precedente va scartato perché non soddisfacente e si passa al modello esteso.

L'analisi non è conclusa a questo punto, perché potrebbero esserci altri fattori da considerare. Si ha però un meccanismo di scelta: si estende il modello, si cerca di capire se migliora rispetto al precedente, si fanno valutazioni di natura logica e si traggono le conclusioni. La strategia è non fissarsi sul modello iniziale e sull'idea iniziale, ma estenderla per capire quale sia la spiegazione migliore dell'indicatore statistico visto all'inizio. Lo scopo è spiegare la correlazione negativa, cioè capire perché esista.

### Le statistiche descrittive delle tre variabili

Le statistiche descrittive riguardano le tre variabili in gioco: avg inc, il reddito medio per distretto; STR, la dimensione della classe (student teacher ratio, rapporto studenti-insegnanti); average score, il punteggio medio. Tra punteggio e dimensione della classe c'è una correlazione negativa, pari a $-0{,}22$, statisticamente significativa nel senso che, in un test di significatività, risulta diversa da zero. Il reddito medio è fortemente correlato con il punteggio: i distretti ad alto reddito tendono ad avere performance decisamente migliori, con una correlazione altissima, significativa, pari a 0,70. Tra reddito e dimensione della classe c'è una correlazione negativa: i distretti ad alto reddito tendono ad avere classi mediamente piccole.

> [!question] Da verificare: la trascrizione riporta "0,70 per cento" per la correlazione tra reddito e punteggio; poiché si tratta di un coefficiente di correlazione, il valore è presumibilmente 0,70.

I dati grezzi sono disponibili nella pagina Moodle del corso. Le analisi mostrate finora sono solo grafiche, e il grafo che segue è lo schema logico descritto fin qui a parole.

Se non si considera il reddito (ignorando la prima parte del grafo), la prima potenziale relazione causale tra le variabili è quella tra dimensione della classe e performance. La relazione è statisticamente rilevante e negativa, ha senso dal punto di vista logico e potrebbe essere un buon candidato come relazione causale. Quando si guarda l'effetto del reddito, risulta una relazione negativa con la dimensione della classe e una positiva con la performance. Aggiungendo questo fattore di controllo, ci si chiede che cosa succeda alla correlazione negativa iniziale: se essa sia una connessione diretta tra i due blocchi oppure se sia spiegata dalla terza variabile.

### Il confronto tra distretti a basso e ad alto reddito

Per verificarlo si divide il campione in due parti e si calcola la correlazione tra le due variabili in ciascuna. L'analisi mostrata è molto grossolana: si è calcolata la mediana del reddito, e i distretti sotto la mediana sono stati classificati a basso reddito, quelli sopra ad alto reddito. Come funzioni questo procedimento si vedrà meglio con il modello di regressione.

Per i distretti a basso reddito la correlazione tra dimensione della classe e performance diventa piuttosto piccola. Il punto principale non è la differenza rispetto a $-0{,}22$, ma il fatto che, in un test di significatività, il valore non risulta statisticamente significativo.

> [!question] Da verificare: la trascrizione riporta "il punto grosso non è neanche che il numero non è tanto diverso da meno 0,22"; il senso sembra essere che il valore è piccolo in assoluto, ma ciò che conta è la non significatività.

Per i distretti a basso reddito il reddito sembra dunque essere il driver principale della correlazione negativa: condizionatamente al reddito basso, la correlazione condizionale tra dimensione della classe e performance è sostanzialmente zero. Anche per i distretti ad alto reddito la correlazione è piuttosto bassa e il test di significatività la indica come non significativa. Il p-value del test è leggermente più alto, comunque non sufficiente a giustificare un livello di significatività.

Il messaggio principale è che, controllando per il reddito, la correlazione tra la variabile di interesse e quella su cui si vorrebbe investire è non significativa. Il nuovo modello, che passa per il reddito, supera quindi il precedente: contiene più informazione e le conclusioni inferenziali che ne derivano escludono il modello precedente. La correlazione tra dimensione della classe e performance non è significativa, e la correlazione marginale non è così importante perché la correlazione condizionale ai livelli di reddito non è statisticamente significativa. Il nuovo modello è anche sensato a parole, e il modello superiore esclude l'altro, per cui occorre concentrarsi su una relazione logica di questo tipo.

In caso contrario si spenderebbero circa due miliardi di dollari l'anno di denaro pubblico per intervenire su una variabile che solo apparentemente è legata alla variabile di interesse, la performance dei bambini, e da cui questa non dipende direttamente. Probabilmente non si avrebbe un effetto diretto sulla performance. Le risorse andrebbero forse usate per migliorare le condizioni delle persone meno abbienti, perché il reddito sembra la variabile chiave con un impatto sulla performance dei bambini.

### La stessa analisi con il modello di regressione

Il docente anticipa come tradurre tutto questo in un modello di regressione, che gli studenti hanno già visto in linea generale; interessa soprattutto l'intuizione, e le formule verranno spiegate meglio in seguito. Il primo modello è la relazione lineare tra il punteggio dei bambini e la dimensione della classe. La pendenza della retta di regressione stimata è $-2{,}27$. Con un test di significatività su questo coefficiente, per verificare se il parametro sia diverso da zero, il p-value risulta zero. Si può quindi affermare che esiste una pendenza negativa, quella della linea rossa dello scatter plot che descrive i dati.

Si aggiunge poi l'effetto del reddito. Nel nuovo modello di regressione l'aspettativa sulla performance dipende dalla dimensione della classe, $X_1$, e dal reddito, $X_2$. Stimando questo modello, il coefficiente che lega la performance alla dimensione della classe si più che dimezza: da circa $-2{,}2$ passa a $-0{,}64$. Il test di significatività dà un p-value maggiore del 5%, non esageratamente grande. Aggiungendo il reddito, l'impatto della dimensione della classe sulla performance si riduce di molto. In un'analisi stretta, condizionatamente al livello di reddito la dipendenza lineare tra performance e dimensione della classe è nulla, come già indicato dal p-value dell'analisi per sottocampioni.

Costruire un modello con due variabili equivale a dividere il campione in due pezzi, alto e basso reddito, e a calcolare il livello di dipendenza nei due sottoinsiemi. Questo sarà ripreso più avanti, la settimana prossima o forse già il giorno dopo.

### Estendere il modello con coerenza logica

Per capire se una relazione sia causale, uno dei problemi principali è incrementare il modello in modo logico e verificare se il nuovo modello migliora il precedente. Il modello più esteso deve mantenere sempre coerenza logica, con una spiegazione che valga la pena di usare. Non si possono inserire informazioni come il numero di persone che in California vanno a vedere il film di Nicolas Cage: potrebbero essere correlate, ma la correlazione potrebbe dipendere da qualunque cosa. Quando si inserisce una variabile nel modello serve una storia da raccontare, e non si lascia che siano i dati a dire che cosa si vuole spiegare. Il docente indica questa come la cosa più importante, e con essa conclude la lezione di due giorni prima.

## Il modello di regressione semplice e l'esogeneità

Si passa al trattamento formale del modello di regressione, che è il principale punto di riferimento per questo tipo di analisi, anche perché è estremamente semplice. Il docente si concentra sul modello di regressione semplice: se se ne capiscono le sottigliezze alla base della definizione, l'estensione ai casi più complicati è banale e cambia soltanto un po' l'algebra.

L'idea fondamentale è capire se la relazione causa-effetto sia buona. Lo è se vale una proprietà statistica del modello, accennata nella lezione precedente: l'esogeneità. Essa significa che le spiegazioni alternative non possono avere un impatto sistematico sulla relazione chiave tra le variabili che si vogliono usare. Le spiegazioni alternative si descrivono con una variabile specifica del modello, tipicamente non osservabile, che è il termine d'errore. Il termine d'errore include tutte le informazioni che potrebbero avere un impatto sulla relazione di interesse ma non vengono utilizzate: è un contenitore di elementi non osservabili, che può però avere una sua interpretazione.

### L'esempio di istruzione e salario

Il problema da cui si parte è abbastanza classico nell'economia del lavoro: la relazione tra livello di istruzione e salario.

I dati non sono particolarmente recenti ma sono abbastanza standard. I salari sull'asse delle y sono salari orari in dollari e sono numeri piccoli perché i dati risalgono agli anni Settanta; l'andamento non è molto diverso da quello che ci si aspetterebbe oggi, a parte la scala. L'esempio permette di definire alcuni concetti in modo molto intuitivo.

Sull'asse delle x c'è il livello di istruzione, chiamato educ (education) e misurato in anni. Ogni colonna di punti rappresenta la distribuzione dei salari dei lavoratori con uno specifico livello di istruzione. Per education uguale a 10, i punti della colonna sono la distribuzione dei salari dei lavoratori che hanno studiato esattamente 10 anni; un'altra colonna dà la distribuzione di quelli che hanno studiato esattamente 15 anni, e così via. Ogni fetta dello scatter rappresenta quindi una distribuzione condizionale, che dice in termini probabilistici quanto è probabile trovare, in quel sottogruppo, un lavoratore che guadagna molto o poco.

### Le medie condizionali

Al variare dell'istruzione cambia non solo la media della distribuzione. Calcolando la media per ogni colonna, ci si aspetta valori che tendono a crescere con il livello di istruzione. Per i livelli più bassi la variabilità è scarsa e il salario medio è sotto i 5 dollari l'ora. Per un livello intermedio la media sarà poco sopra i 5 dollari. Per chi ha studiato molto il centro della distribuzione è intorno ai 15 dollari. Nel grafico i quadratini rossi rappresentano queste medie condizionali: per ogni livello di education è la media della distribuzione data la colonna. Si vede una tendenza crescente, cioè a più studio corrisponde in media un salario maggiore.

Questo non significa che studiando molto si guadagni di più con certezza. In corrispondenza di uno stesso gruppo ci sono persone che guadagnano meno di chi ha studiato zero anni e persone che guadagnano estremamente di più. È ragionevole. L'eterogeneità dice come varia il salario in funzione di informazioni diverse dall'istruzione: tutte le persone di una colonna hanno lo stesso livello di istruzione ma caratteristiche individuali diverse. Il punto in alto a circa 25 dollari l'ora può essere il figlio di un dirigente che finirà a fare il dirigente. Quello più in basso può essere qualcuno che ha deciso di studiare archeologia: se gli va bene guadagna molto, se gli va male finisce a fare scavi per i cantieri. Possono esserci anche effetti più sottili, come l'effetto di genere: gli uomini tendono a guadagnare più delle donne, che sia giusto o no, è ciò che si osserva nei dati.

L'eterogeneità dei salari è quindi spiegata da fattori diversi dall'istruzione. All'interno di una colonna l'istruzione è esattamente la stessa, per cui non può essere la spiegazione dell'eterogeneità. Dipende da altro: il reddito della famiglia, il tipo di studi, l'intelligenza, il fatto di essere uomo o donna. A parità di anni di studio, chi si laurea alla Bocconi può avere aspettative diverse da chi si laurea a Cassino, anche solo perché a Milano i salari sono più alti. Questa parte dell'eterogeneità non spiegata dall'education, spiegata da qualcos'altro, viene chiamata termine d'errore e indicata con il simbolo greco $\varepsilon$.

### Perché quantificare la relazione causale

Il problema è descrivere una relazione causale tra livello salariale e livello di istruzione. Conoscendone la forma, cioè applicando il modello, si potrebbe valutare se prendere una magistrale convenga in termini di salario atteso. Per esempio, studiare due anni in più, passando da 13 a 15 (il docente precisa che i numeri non sono esatti), si può quantificare in termini di salario orario: quanto si guadagna di più, e se ne vale la pena. Si vuole quantificare una relazione causale per rispondere a domande pratiche di questo tipo: se si aumenta o si riduce la X, che cosa succede alla Y, la variabile di interesse?

Il primo problema è definire un modello coerente e logico, cioè una relazione causa-effetto. Una volta disponibile, la si può usare per analisi quantitative di vario genere: analisi di policy, di scelte, di scenario.

Un'altra rappresentazione degli stessi dati usa, per ogni sottogruppo del campione, un box plot, che mostra come cambiano l'indicatore di centralità e la dispersione del fenomeno.

### Il modello di regressione lavora sulle medie

Il modello di regressione lavora sul momento di ordine uno, cioè sulle medie. Interesseranno anche le varianze, che misurano la dispersione, ma in generale interessa capire come in media il livello di istruzione impatti sul salario. Serve un modello statistico che approssimi i quadratini rossi.

I quadratini rossi sono evidenza campionaria, non della popolazione. Quello che si vuole ottenere con il modello statistico, cioè il modello di regressione, è approssimare i quadratini rossi in modo ragionevole, non necessariamente molto preciso. Un modello statistico di interesse è dunque un modello che cerca di spiegare le medie condizionali.

In realtà l'obiettivo non è spiegare le medie condizionali nel campione, la nuvola di pallini blu del grafico, ma la popolazione. Nel campione non interessa sapere che cosa succeda: si ha un foglio Excel con tutti i numeri, e per conoscere guadagno e anni di studio dell'unità statistica numero 73 basta guardarlo, senza bisogno di prevederlo. Si vogliono usare queste informazioni per capire come si comportano le variabili nella popolazione. Non serve quindi essere troppo precisi nell'approssimare i quadratini rossi, che sono già stati calcolati. I quadratini rossi possono essere una buona approssimazione della media condizionale, ma sono solo un'approssimazione. Si cerca un modello sufficientemente robusto che approssimi l'andamento dei quadratini rossi, sapendo che ciò che interessa non è il quadratino rosso ma il quadratino verde, cioè la media nella popolazione.

Calcolare la media nella popolazione richiederebbe di intervistare tutti i lavoratori degli Stati Uniti in un certo periodo e di conoscere con esattezza il loro reddito, il che è impossibile. Il problema è quindi approssimare, soltanto approssimare, la sequenza di quadratini rossi. Questi sono le medie condizionali, e sono approssimazioni delle medie condizionali di popolazione ottenute dall'evidenza campionaria.

Per farlo in generale si usano modelli semplici. Un modello complicato che si adatti molto bene ai quadratini rossi sarebbe possibile e nemmeno difficile: basta premere un tasto sul computer per trovare funzioni molto smooth che passano esattamente sopra i quadratini rossi. Ma questo non è ciò che interessa, perché i quadratini rossi sono già noti, calcolati in una tabella a parte, e non serve una funzione complicata per approssimarli. Per sapere che cosa succede passando da 12 a 14 anni di istruzione basta fare la differenza tra le due medie condizionali. Il campione è inoltre uno specifico insieme di 500 e qualcosa lavoratori, mentre l'obiettivo è approssimare la popolazione.

Il problema non è dunque trovare una funzione molto precisa sui quadratini rossi, che sono già noti, ma una funzione sufficientemente buona per approssimarli e, allo stesso tempo, per approssimare i quadratini rossi che si otterrebbero da campioni diversi estratti dalla stessa popolazione. Un modello che si adatti perfettamente ai quadratini rossi disponibili non è particolarmente utile: oltre all'informazione già nota, significa che il modello si adatta troppo bene ai dati posseduti e non a tutti i dati possibili, che sono quelli interessanti perché ignoti. Un modello costruito sui quadratini rossi osservati e perfetto, senza errore, incorre in un problema che si chiama overfitting: si adatta troppo bene ai dati ma non necessariamente alla popolazione.

### Un esempio grafico di overfitting

Si supponga una popolazione composta da punti, alcuni blu e alcuni rossi. Tutti i punti sono persone con certe caratteristiche, appartenenti alla stessa popolazione. Il campione a disposizione è costituito dai punti blu; i rossi sono persone che potenzialmente si potrebbero avere nella popolazione ma che non sono nel campione. Si può pensare a un insieme di persone, in parte blu e in parte rosse, da cui si esegue l'analisi solo sul campione blu, lasciando fuori il rosso.

Si può costruire un modello che si adatti bene ai punti blu, che sono il campione. Rispetto ai dati usati, la funzione verde che ne risulta è perfetta, praticamente senza errore, perché approssima esattamente i punti blu. Ma l'obiettivo non è approssimare il campione, è approssimare il comportamento della popolazione, quindi anche delle persone non usate per stimare il modello. Calcolando la distanza tra ciò che il modello stima e ciò che si potrebbe avere nella popolazione, alcuni punti risultano estremamente distanti: il modello è molto distante da persone che potrebbero costituire il campione successivo, un altro campione della stessa popolazione. Il modello funziona molto bene su ciò che già si ha e molto male su ciò che si potrebbe avere.

Se si dovesse prevedere la y per un dato valore di x, si userebbe il punto sulla funzione stimata, che è la migliore approssimazione possibile con quella funzione, ma l'errore di previsione sarebbe gigantesco. Il modello va malissimo se una persona non appartiene a quel sottoinsieme della popolazione. È preferibile allora un modello che non approssimi troppo bene la linea blu ma che non vada troppo male nemmeno sulla rossa, cioè un modello che faccia da media rispetto alla curva verde che si stimerebbe con un campione diverso. Una funzione di questo tipo non è perfetta per il gruppo blu né per il gruppo rosso, ma in media non sbaglia in modo sistematico.

La linea verde è dunque un modello che fa overfitting rispetto al campione e va molto male fuori dal campione, che è ciò che interessa: il modello serve a capire che cosa succede su ciò che non si osserva, non su ciò che si è già osservato. Trovare un modello che si adatti troppo bene al campione non è necessariamente una buona notizia. Un modello di regressione con un $R^2$ del 99% non è necessariamente un buon modello, mentre uno con un $R^2$ del 20% potrebbe essere ottimo. Il docente accenna che, a chi fosse interessato, il tema si può approfondire con simulazioni più accurate e modelli più complicati; qui serviva solo dare un'idea. Stimare troppo bene un modello sui dati non è necessariamente una buona notizia, perché non c'è certezza che l'approssimazione funzioni fuori dal campione.

### Perché una retta di regressione

Tornando al problema principale, si cerca una funzione che non approssimi troppo bene le medie condizionali del campione (i quadratini rossi) ma rifletta un andamento di lungo periodo. Poiché i quadratini rossi non sono i dati che si avrebbero con altri campioni, il modello deve essere universale e non specifico del singolo dataset.

Il secondo motivo per usare una retta di regressione è che è un modello molto semplice. Una linea è facile da identificare, senza curve, polinomi o altre sofisticazioni. Una retta dipende da due soli parametri, l'intercetta e il coefficiente angolare. Stimati questi due numeri, si può caratterizzare in modo completo il comportamento dei dati su tutta la popolazione.

### Perché le medie condizionali

Il modello di regressione non approssima direttamente i dati, ma una loro caratteristica, le medie condizionali. Trovare un modello che approssimi i pallini blu è praticamente impossibile, perché non esiste una funzione che si adatti completamente ai dati. Si usano le medie condizionali perché sono indicatori di centralità sufficientemente stabili.

Esistono anche modelli statistici che, invece delle medie condizionali, considerano altri indicatori come i quantili e le mediane. Si tratta della regressione quantilica, che non fa parte del corso. Il docente la segnala perché è interessante per capire non solo come reagisce in media un fenomeno a una perturbazione, ma anche come reagiscono le code. In finanza questo può essere utile, perché interessa che cosa succede sulle code delle distribuzioni, cioè perdere o guadagnare molto, e non in media, dove non si guadagna e non si perde nulla.

I rendimenti medi di un portafoglio sono mediamente zero. A chi investe interessa coprirsi dagli eventi estremi, e quindi capire come una variazione della situazione geopolitica impatti le code del portafoglio e non la sua media. In questo corso, tuttavia, si guarderà alle medie condizionali, un indicatore di centralità tutto sommato semplice, sapendo che l'impostazione si può generalizzare.

### Notazione e definizione del modello

La media si indica con la lettera $E$, da expectation. Nella notazione $E(y \mid x)$ la prima variabile è quella su cui si calcola la media, mentre la seconda, che segue la barra verticale, è la variabile di condizionamento. I quadratini rossi rappresentano quindi il valore atteso condizionale dei salari rispetto all'istruzione: wage è la variabile $y$ ed education la variabile $x$. In questo momento le variabili sono soltanto due.

Il modello di regressione è la formula che definisce la media di $y$ dato $x$ come il modello più semplice, cioè una retta: $E(y \mid x) = \alpha + \beta x$. Conosciuti i parametri $\alpha$ e $\beta$, tutto è identificato.

Dal punto di vista della stima e dell'inferenza, interessa però legare le osservazioni individuali alla media condizionale. Si considerano le coppie di osservazioni $(y_i, x_i)$, dove $i$ indica l'individuo, cioè l'unità statistica (un lavoratore nell'esempio precedente), $x_i$ è l'istruzione del lavoratore $i$-esimo e $y_i$ il suo livello di salario. Il legame tra le osservazioni grezze, i puntini blu del grafico, e la media condizionale è

$$y_i = \alpha + \beta x_i + \varepsilon_i .$$

Il salario esatto dell'individuo, che non è il salario medio, dipende da due fattori. Il primo è una componente media: per il fatto di appartenere a una categoria, cioè a un certo livello di istruzione, il salario atteso è il valore $\alpha + \beta x_i$. Il secondo è una componente idiosincratica, individuale, che rappresenta tutte le caratteristiche del lavoratore diverse dall'istruzione: il genere, la famiglia, se è sveglio o no, se ha fatto un master in finanza o in storia dell'arte, e così via. Il salario di una persona è quindi un salario medio, dovuto all'appartenenza a un gruppo, più una componente individuale con tutte le altre caratteristiche.

### Esogeneità ed endogeneità

Le caratteristiche del termine $\varepsilon$ determinano se il modello statistico così definito sia una relazione causale oppure no. Nel corso di statistica non sono così importanti, lo sono invece in econometria e in economia, perché la relazione tra $\varepsilon$ e la variabile $x$ è la ragione pratica e teorica che permette di dire se il modello è ben specificato, cioè se è una relazione causale. Si assumerà che la correlazione tra questo fattore e il fattore presente nel modello sia zero. Questa condizione si chiama esogeneità. Se non vale si parla di endogeneità, che ha conseguenze pesanti sulla stima del modello, come si vedrà in vari esempi.

Le definizioni sono queste. $y$ è la variabile dipendente. $x$ è il regressore o predittore: predittore se si segue una letteratura più statistica, regressore se più economica. $\varepsilon$ è il termine d'errore. Il termine d'errore non è osservabile sulla base dei dati, quindi per capire se il modello sia corretto bisogna calcolare le proprietà di qualcosa che non si può misurare direttamente, e occorre aggirare il problema per stabilire se il modello sia ragionevole.

### Perché serve una condizione su $\varepsilon$: un esempio operativo

Si consideri il modello $y = \alpha + \beta x + \varepsilon$ e si supponga di voler prevedere, con esso, il salario atteso di chi studia esattamente $x_1$ anni (per esempio dieci). Il salario di un individuo che ha studiato $x_1$ anni è $\alpha + \beta x_1 + \varepsilon$. Il termine $\varepsilon$ contiene altri fattori, diversi dall'istruzione, che in linea di principio potrebbero essere collegati al livello di istruzione: più si studia, più si impara, e le competenze possono aumentare. Si fa quindi dipendere $\varepsilon$ anche da $x_1$, scrivendo $\varepsilon(x_1)$. Se $\varepsilon$ rappresenta il livello di abilità conseguita, questo può dipendere da altre cose ma anche dall'istruzione. In questo modo si lega direttamente l'abilità di una persona al livello di istruzione.

Che cosa succede se si decide di studiare di più, aumentando la dotazione di istruzione di $\Delta x$, per esempio due anni? Si passa da $x_1$ a $x_1 + \Delta x$. Il salario della stessa persona diventa $\alpha + \beta (x_1 + \Delta x) + \varepsilon(x_1 + \Delta x)$. Il beneficio stimato dal modello per i due anni in più di studio è la differenza tra le due quantità. Indicata con $\Delta y$ la variazione di $y$:

$$\Delta y = \alpha + \beta x_1 + \beta \Delta x + \varepsilon(x_1 + \Delta x) - \alpha - \beta x_1 - \varepsilon(x_1) .$$

Semplificando i termini uguali si ottiene

$$\Delta y = \beta \Delta x + \Delta\varepsilon ,$$

dove $\Delta\varepsilon$ è la differenza tra $\varepsilon(x_1 + \Delta x)$ ed $\varepsilon(x_1)$. Questo termine non è calcolabile, perché non è noto, ma teoricamente esiste. La variazione di salario dipende quindi in parte dal fatto di aver studiato due anni in più e in parte da effetti collaterali della scelta.

La variazione complessiva si può calcolare: prendendo la differenza dei quadratini rossi si trova, per esempio, 3 dollari. Sulla base del modello però non si sa se questi 3 dollari in più dipendano dalla scelta di studiare o da altro. Non si riesce a separare quanto vale $\beta \Delta x$ e quanto vale il resto: si conosce soltanto la somma. I 3 dollari potrebbero essere 1 più 2, oppure 0 più 3, oppure $-3$ più 6. L'effetto non è identificabile.

L'unico modo per identificare l'effetto della scelta, cioè $\beta \Delta x$, è fissare il valore di $\Delta\varepsilon$. Fissandolo, la variazione di $y$ dipende semplicemente dalla scelta. Il valore più comodo da fissare è 0: se si assume che la variazione di $\varepsilon$ sia uguale a zero, tutta la variazione di $y$ dipende da $\beta \Delta x$. Per identificare l'effetto di un fattore su cui si sceglie bisogna quindi essere sicuri che gli effetti collaterali siano nulli.

> [!question] Da verificare: la frase finale della trascrizione ("Se delta y non è uguale a zero, vuol dire che delta x non è uguale a beta delta x") è confusa; il senso probabile è che, se $\Delta\varepsilon$ non è nulla, la variazione di $y$ non coincide con $\beta \Delta x$.

### La condizione statistica per $\Delta\varepsilon = 0$

Resta da stabilire quale sia la condizione statistica per cui la variazione di tutto il resto è nulla in corrispondenza di una variazione di $x$. Qui tutto è lineare, quindi basta poco. La variazione di $\varepsilon$ rappresenta quanto cambiano tutte le altre variabili che non sono nel modello quando varia $x$, dato che nel modello $y$ dipende da $x$ in modo diretto ed esplicito. Tale variazione è nulla quando la correlazione tra $x$ ed $\varepsilon$ è uguale a zero, e questa implica quella.

> [!question] Da verificare: la trascrizione riporta "quando la correlazione tra x e y è uguale a zero"; dal contesto (la variazione che riguarda "tutte le altre variabili che non sono nel modello") si tratta probabilmente della correlazione tra $x$ e il termine d'errore $\varepsilon$.

Si ha così un concetto statistico che permette di identificare gli effetti delle proprie scelte sulla variabile dipendente: una struttura di dipendenza, una correlazione, che deve essere uguale a zero. Concettualmente è difficile verificarla, perché $x$ si può misurare ma $\varepsilon$ no. Se però si può fare questa ipotesi aggiuntiva, si può affermare che l'unica spiegazione plausibile per una variazione di $y$ è la variazione di $x$ pesata dal coefficiente $\beta$, la pendenza della retta di regressione.

Questa ipotesi si chiama esogeneità, e in questo caso esogeneità stretta. Esistono vari concetti di esogeneità; nei modelli di regressione classici si usa quella stretta. Nella seconda parte del corso verrà abbandonata a favore dell'esogeneità debole, che è più che sufficiente. Se invece la correlazione fosse diversa da zero, la variazione di $\varepsilon$ non potrebbe essere nulla in corrispondenza di una variazione di $x$, e non si saprebbe valutare perché si osservino variazioni di $y$.

### Interpretabilità dei risultati e scopo dell'analisi

Il problema posto non è un problema generale del modello di regressione, ma di interpretabilità dei risultati. In un corso di statistica il problema dell'eterogeneità nel modello di regressione non viene praticamente considerato, perché lo scopo è trovare un modello da usare per fare previsioni sui dati successivi, e va benissimo. Qui invece interessa valutare con precisione il parametro $\beta$, perché esso dice, per esempio, quanto denaro si sta spendendo per l'istruzione dei bambini e se la scelta fatta è corretta.

### Esempio: il bonus fiscale e i consumi

Un esempio più semplice. Uno dei problemi dell'Italia è che i consumi sono molto bassi. Per dare impulso ai consumi si danno tipicamente dei bonus; il docente richiama la riforma di Matteo Renzi dei mille euro, introdotta prima come sconto fiscale e destinata a una certa fascia di lavoratori. La misura è costosa, perché a ogni lavoratore di una fascia di reddito media si dà una somma, non grande ma significativa. Il costo si può valutare in modo abbastanza preciso, perché è una minore entrata per lo Stato, trattandosi di sconto fiscale. Lo scopo era stimolare i consumi, e ci si chiede se i consumi siano effettivamente migliorati in conseguenza della policy.

Per rispondere si può calcolare la relazione tra redditi e consumi, con i consumi come $y$ e i redditi come $x$, entrambi pro capite. La policy varia $x$ di 1.000 euro, e ci si chiede come siano variati i consumi in corrispondenza di tale variazione. Il docente precisa di non aver svolto questa analisi, che gli interessa poco. In generale, se il parametro che lega consumi e redditi è grande, 1.000 euro in più alle famiglie avranno un impatto sui consumi, e la policy, giusta o sbagliata che sia, avrà ottenuto il risultato voluto.

Il problema è se il modello considerato sia corretto. La variazione dei consumi osservata potrebbe dipendere dai 1.000 euro in più, oppure da altro: le condizioni economiche di quel periodo, o qualsiasi altro fattore. Si vuole valutare se spendere molto denaro abbia un impatto al netto degli altri effetti collaterali della manovra. Se l'effetto collaterale fosse più importante, probabilmente sarebbe stato più efficiente usare quei soldi per altro. Il docente precisa che non sta valutando se la scelta sia stata giusta o sbagliata: pone un problema statistico.

Si può investire molto denaro in una policy e stimare un parametro grande tra le due variabili, da cui ci si aspetterebbe un impatto devastante. Tale impatto vale solo se si ipotizza che $\Delta\varepsilon$ sia zero. Altrimenti non si può dire che la policy abbia avuto un impatto, perché occorre considerare una combinazione di eventi e non solo uno o l'altro: la variazione si può calcolare ma non si sa da che cosa dipenda.

L'unico modo per essere sicuri che la policy, cioè l'investimento, abbia un impatto è fissare ciò che non si conosce, e ciò che non si conosce si fissa tipicamente a zero. Se $\Delta\varepsilon$ è zero, l'unica spiegazione della variazione di $y$ è $x$, pesata da $\beta$, che è il moltiplicatore. Il solo problema diventa allora stimare $\beta$.

### Stimare β, non prevedere

Lo scopo dell'analisi con i modelli di regressione in economia è capire quanto una policy abbia impatto, cioè valutare correttamente il parametro $\beta$. Non interessa un modello che si adatti ai dati o che serva per le previsioni, ma un modello che stimi $\beta$ in modo corretto, e per farlo occorre fissare $\Delta\varepsilon$ a zero. In questo corso lo scopo è stimare $\beta$, non trovare un modello che faccia previsioni decenti. In un corso orientato alle previsioni, invece, che $\beta$ sia calcolato bene o male non importa, purché la previsione sia corretta.

### Il punto di vista del decisore e quello del genitore

Un economista vuole sapere se spendere 2 miliardi di dollari l'anno per ridurre la dimensione della classe sia utile dal punto di vista sistemico, a grande scala, che è un problema politico o economico. Si può però assumere il punto di vista di un genitore che deve iscrivere un figlio a scuola. Il criterio potrebbe essere scegliere la scuola in cui il voto finale del figlio sarà più alto, così da entrare l'anno dopo in una buona scuola con una borsa di studio e poter sopravvivere a un sistema di istruzione estremamente costoso.

Per il genitore lo scopo non è migliorare il mondo, ma trovare la scuola più adatta al proprio figlio. Il problema diventa allora di forecast. Se la variabile che prevede meglio la performance del figlio risultasse la dimensione del parcheggio della scuola, il genitore misurerebbe il parcheggio di tutte le scuole degli Stati Uniti e sceglierebbe in base a quello: non importa se logicamente non ha senso, funziona. È una black box.

Il docente paragona la previsione a una catena di produzione: non interessa sapere perché la gente compra un certo prodotto, né quanti componenti servano per la manutenzione, ma sapere che quel giorno bisogna avere sette tonnellate in magazzino, cioè che la catena di produzione funzioni.

> [!question] Da verificare: la trascrizione riporta "mozzoline di ferro" e una frase confusa sull'esempio del magazzino; il senso è che in un problema di previsione conta la correttezza della previsione e non la comprensione delle cause.

Dal punto di vista dello statistico che fa previsione, quindi, non interessa calcolare esattamente il parametro che lega le variabili, perché non è necessariamente legato alla capacità previsiva del modello. Se invece si usa il modello per valutare politiche, o per confermare congetture economiche e finanziarie di qualsiasi tipo, interessa conoscere il parametro. L'unico modo per stimarlo correttamente è essere sicuri che la variazione di $\varepsilon$ sia nulla.

> [!question] Da verificare: la trascrizione riporta "essere sicuri che la varianza di Y sia uguale a zero"; per coerenza con la discussione precedente si intende probabilmente la variazione (o la correlazione con $x$) del termine d'errore $\varepsilon$, non la varianza di $y$.

Il docente precisa che non sta dicendo che un approccio sia migliore dell'altro: lo stesso strumento risponde a criteri diversi perché i problemi sono diversi.

## Stima dei parametri del modello di regressione

Come si stima il parametro del modello di regressione? In generale tutti i libri indicano come modo corretto il metodo dei minimi quadrati. Si prendono le osservazioni su $y$ e il modello, e si trovano $\alpha$ e $\beta$ tali che la distanza media tra $y$ e la trasformazione lineare di $x$ sia la più piccola possibile. La distanza si calcola con il quadrato, per evitare che gli scarti positivi e negativi si compensino. Per risolvere il problema si derivano rispetto ad $\alpha$ e $\beta$, si pongono le derivate uguali a zero e si risolve il sistema di due equazioni in due incognite. La soluzione per $\beta$ è un rapporto tra quantità, quella per $\alpha$ una differenza di medie.

Il docente considera questa la via più noiosa, e dato che gli studenti l'avranno già vista molte volte ne presenta una leggermente diversa, con un'algebra più breve e a suo parere più intuitiva.

### Ricavare β dai momenti della popolazione

Si considera il modello di regressione e si ipotizza che sia corretto, cioè che valga l'esogeneità. Il docente non considera che cosa succeda stimando un modello logicamente sbagliato. L'ipotesi è che la covarianza tra $x$ ed $\varepsilon$ sia zero.

> [!question] Da verificare: più volte nel passaggio la trascrizione dice "la covarianza tra X e Y è uguale a zero" a proposito dell'ipotesi di esogeneità; subito dopo, nel calcolo, il docente usa l'ipotesi che la covarianza tra $x$ ed $\varepsilon$ sia zero, ed è quella riportata qui.

Si chiede come $\beta$ si leghi alle caratteristiche dei dati, e lo si ricava dai momenti delle variabili. Supponendo che il modello sia corretto, si calcola la covarianza tra $x$ e $y$ nella popolazione. Scritta così non è molto informativa, ma si può sviluppare: si sa (come se si fosse una divinità) che $y$ è data dalla combinazione $\alpha + \beta x + \varepsilon$, quindi

$$\operatorname{Cov}(x, y) = \operatorname{Cov}(x, \alpha + \beta x + \varepsilon).$$

Si usa una proprietà semplice della covarianza: la covarianza di una variabile rispetto a una combinazione lineare è la combinazione lineare delle covarianze. Si può pensare alla covarianza come a una media, a una sommatoria, o anche a un integrale; sommatorie e integrali sono operatori lineari, per cui la sommatoria di una somma è la somma delle sommatorie. Chi non si fida può verificare con un esempio con $x$, $y$ e $z$, calcolando la covarianza di $x$ rispetto a $y + z$ dalle definizioni. Si ottiene

$$\operatorname{Cov}(x, y) = \operatorname{Cov}(x, \alpha) + \operatorname{Cov}(x, \beta x) + \operatorname{Cov}(x, \varepsilon).$$

Il primo termine è zero, perché la covarianza tra una costante e una variabile casuale è nulla: al variare di $x$, $\alpha$ resta costante. Il terzo termine è zero per ipotesi. Il docente sottolinea che è una scelta, un'ipotesi non necessariamente corretta. Nel secondo termine la costante $\beta$ si porta fuori dalla covarianza e resta la covarianza di $x$ con se stessa, cioè la varianza di $x$. Quindi

$$\operatorname{Cov}(x, y) = \beta \operatorname{Var}(x),$$

da cui $\beta$ si ricava in funzione dei momenti delle variabili:

$$\beta = \frac{\operatorname{Cov}(x, y)}{\operatorname{Var}(x)}.$$

Questa relazione vale nella popolazione: il vero $\beta$, quello che si otterrebbe considerando tutti i lavoratori degli Stati Uniti, è la covarianza tra livello di istruzione e salario divisa per la varianza del livello di istruzione.

### Lo stimatore campionario e il metodo dei momenti

Se la formula vale nella popolazione, si può applicarla in ambito campionario. Il vero $\beta$ è una covarianza divisa per una varianza; con un campione si possono stimare numeratore e denominatore. Per la legge dei grandi numeri, il numeratore converge alla vera covarianza e il denominatore alla vera varianza, per cui lo stimatore converge al vero $\beta$. Uno stimatore di $\beta$ è quindi

$$\hat\beta = \frac{\sum_{i=1}^{n} (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^{n} (x_i - \bar x)^2},$$

dove $\bar x$ e $\bar y$ sono le medie campionarie e $n$ è il numero di osservazioni del campione, cioè di lavoratori, che nel caso specifico sono 526.

La teoria dice dunque che, se il modello è corretto, il vero $\beta$ è dato da questo rapporto. Non si dispone di tutta la popolazione ma solo di un campione, che si suppone abbastanza rappresentativo, e il concetto astratto si calcola con le statistiche descrittive. Numeratore e denominatore convergono ai due momenti di popolazione, per cui per $n$ sufficientemente grande lo stimatore approssima bene $\beta$. Questo procedimento si chiama metodo dei momenti.

Il docente si chiede perché questo approccio gli piaccia più della costruzione delle derivate rispetto ad $\alpha$ e $\beta$.

Il motivo è che con il metodo dei momenti l'ipotesi viene formulata in modo specifico: nelle condizioni usate per la stima si impone direttamente, in modo brutale, la condizione di esogeneità. La formula funziona solo se la covarianza tra $x$ ed $\varepsilon$ è uguale a zero; in quel caso il termine corrispondente sparisce per ipotesi e si ottiene lo stimatore visto sopra. Si usa dunque il metodo dei momenti anziché i minimi quadrati.

Nella slide successiva si minimizza la distanza tra $y$ e il modello di regressione, e si trova che lo stimatore dei minimi quadrati coincide esattamente con quello appena ricavato.

> [!question] Da verificare: la trascrizione riporta "se minimizzo la varianza di y, cioè se calcolo la distanza minima tra y e il modello di regressione"; il criterio dei minimi quadrati minimizza la distanza tra $y$ e il modello, e il riferimento alla "varianza di y" sembra un lapsus.

In questo caso i due approcci coincidono, cosa che non sempre accade. Ci sono motivi profondi per cui succede, ma in generale quello che si è fatto prima non è molto diverso da quello che si fa ora, con la differenza che nel metodo dei momenti le ipotesi economiche specifiche, cioè l'esogeneità, sono imposte direttamente.

### Che cosa succede se l'esogeneità non vale

Si supponga che la covarianza tra $x$ ed $\varepsilon$ sia diversa da zero e la si indichi con $\rho_{x\varepsilon}$, un numero diverso da zero.

> [!question] Da verificare: la trascrizione parla di "covarianza tra x e y" e di "rho xy"; dal calcolo che segue si tratta della covarianza tra $x$ e il termine d'errore, qui indicata con $\rho_{x\varepsilon}$.

Ripetendo il calcolo di prima, la covarianza tra $x$ e $y$ è uguale a $\beta \operatorname{Var}(x) + \rho_{x\varepsilon}$. Se questa condizione valesse e il numero fosse noto, $\beta$ andrebbe calcolato come

$$\beta = \frac{\operatorname{Cov}(x, y) - \rho_{x\varepsilon}}{\operatorname{Var}(x)}.$$

Per ottenere $\beta$ correttamente occorrerebbe dunque stimare anche $\rho_{x\varepsilon}$, cosa che non si sa fare. Un software non lo fa, anche perché quel numero non è noto. La formula però mostra una cosa più sottile: il software fa finta che $\rho_{x\varepsilon}$ sia uguale a zero. La stima del parametro non è quindi fatta bene, perché manca un pezzo, e la stima di $\beta$ sarà sistematicamente diversa dal vero $\beta$ nella popolazione.

Uno studente chiede se l'endogeneità indichi l'assenza di esogeneità. Il docente conferma: si ha endogeneità quando la correlazione tra $x$ ed $\varepsilon$ è diversa da zero, cioè quando vale il contrario dell'esogeneità.

In presenza di endogeneità il software non lo sa, a meno che non gli venga detto, e tratta $\rho_{x\varepsilon}$ come se fosse zero. La stima di $\beta$ basata sul rapporto tra covarianza e varianza è alterata, perché il numeratore dovrebbe essere ripulito dall'effetto di $\rho_{x\varepsilon}$. Applicando la formula sbagliata quando l'esogeneità non vale, lo stimatore di $\beta$ non risulta collegato a $\beta$, ma a $\beta$ più un termine ulteriore. Si ha quindi una distorsione sistematica tra ciò che si vuole stimare e ciò che si stima effettivamente dai dati. Con endogeneità, gli stimatori che si vedranno nel corso sono distorti, e la distorsione non sparisce nemmeno aumentando il numero di osservazioni: è sistematica. L'implicazione di policy che si vuole valutare con il modello sarà sistematicamente sbagliata.

Riassumendo: se si fa finta di essere in un contesto corretto, in cui $x$ è esogena rispetto a $\varepsilon$, si assume che questa covarianza sia zero. Se il modello è invece sbagliato perché l'errore è correlato con $x$, andrebbe usata la formula corretta. Poiché il software non lo fa, dato che non gli viene detto, la stima di $\beta$ cambia in modo sostanziale.

### Il caso della dimensione della classe

Nell'esempio dei bambini a scuola c'è un problema di endogeneità. La prima regressione lega la performance dei bambini alla dimensione della classe più un termine d'errore, e nel termine d'errore c'è l'effetto del reddito, perché non è nel modello: $\varepsilon$ raccoglie tutto ciò che non è dimensione della classe, e qui lo si può identificare con il reddito. Si è visto che la correlazione tra reddito e dimensione della classe è significativamente diversa da zero. Stimando quel modello si ipotizza di fatto che tale correlazione sia zero, e si ottiene una stima di $\beta$ pari a $-2{,}27$.

Come anticipazione di ciò che si farà più avanti, si toglie dal termine d'errore il reddito, che è la variabile problematica, e lo si inserisce nel modello. L'errore del modello con il regressore in più non è più caratterizzato dall'effetto del reddito, perché questo è ora parte della media condizionale e non della parte residuale. Ristimando il modello si elimina una delle possibili cause di endogeneità, cioè una delle cause che creano relazione tra $\varepsilon$ e la dimensione della classe. Il parametro passa da $-2{,}2$ a $-0{,}64$.

Probabilmente nel modello precedente c'era un problema di endogeneità che si era fatto finta di non vedere. I parametri sono cambiati molto, quindi per stimare $\beta$ nella prima regressione si è probabilmente usata la formula sbagliata, perché si è supposto nulla la correlazione tra reddito e dimensione della classe, che invece non lo è. Scorporando questo effetto, $-2{,}2$ diventa $-0{,}64$: il livello di correlazione tra reddito e dimensione della classe ha un impatto notevole.

> [!question] Da verificare: la trascrizione riporta "ha un impatto tra note"; il senso sembra essere che l'impatto è rilevante.

La distorsione non è piccola e il parametro cambia molto. Queste sono le conseguenze di stimare un modello facendo finta che $\Delta\varepsilon$ sia uguale a zero quando in realtà non lo è.

Tutto il gioco dell'econometria, almeno a questo livello, consiste nel capire quando si può dire che la variazione di $\varepsilon$ è uguale a zero in corrispondenza della variazione di $x$. Tutto il resto è algebra banale: la difficoltà è economica più che tecnica. Nelle prossime lezioni si introdurrà gradualmente la parte tecnica, per mostrare che quanto detto qualitativamente ha un corrispettivo formale.
