---
corso: Econometria
data: 2026-11-10
fonte: Materiali/audio/econometria/econometria_2026-11-10.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-12
---

# Introduzione al corso: esogeneità, causalità e correlazioni spurie

## Impostazione del corso: interpretazione economica ed esogeneità

L'impostazione è più intuitiva che tecnica. Il docente non conosce con precisione il background dell'aula: di solito una parte della classe ha già seguito corsi di econometria e circa il 50% ha visto i modelli solo dal punto di vista statistico. Per alzata di mano risulta che quasi tutti hanno già fatto econometria.

> [!question] Da verificare: la trascrizione riporta "scuota percento della classe" per la quota di chi ha già fatto econometria; la percentuale non è ricostruibile.

Il corso si concentra sull'interpretazione economica ed è fatto soprattutto di ciò che non si deve fare, più che di come si eseguono i calcoli. L'econometria viene spesso presentata come una disciplina tecnica, ma è una disciplina ibrida: la distinzione rispetto all'economia non è netta, mentre lo è quella rispetto alla statistica. A separarla dalla statistica è un'ipotesi aggiuntiva con un'importante implicazione economica, l'ipotesi di esogeneità.

Lo scopo è mostrare che cosa accade quando un modello è costruito in modo scorretto, cioè senza rispettare le regole dell'economia. In quel caso tutti gli indicatori presentati in precedenza dal professore vengono stimati in modo sistematicamente distorto. Ciò che si stima non è l'effetto della politica considerata, ma tale effetto sommato a un fattore di rumore non eliminabile. Anzi, più osservazioni si hanno, più si è precisi nello stimare l'errore. Se interessa un parametro, si stima il parametro più una costante, e di questa costante non si sa nemmeno che cosa sia. Si interpreta quindi come effetto di una politica ciò che è la somma di più effetti collaterali, potenzialmente diversi da quello di interesse. Il corso mostra che cosa succede, sul piano teorico e su quello operativo.

Come ricordava il professore, la scelta del modello e delle variabili conta più della metodologia con cui si fanno poi i conti. Scegliere bene le variabili permette di escludere il problema dell'endogeneità, che è un problema tecnico ed economico insieme. La distinzione sottile è che interessano le relazioni logiche tra variabili, non le relazioni quantitative: non interessa che il modello si approssimi bene ai dati.

## Correlazioni spurie e uso dell'intelligenza artificiale

Il docente avverte che gli indicatori come l'$R^2$ sono la misura peggiore per valutare un modello e che in questo corso non vanno utilizzati, perché non dicono altro che una correlazione. Le correlazioni possono raccontare storie quantomeno bizzarre, perché molto spesso indicano relazioni spurie tra variabili e non relazioni oggettive.

Lo stesso vale se si chiede a ChatGPT o a uno strumento analogo perché due variabili abbiano una correlazione del 95%: una spiegazione viene sempre prodotta, e che abbia senso o no è irrilevante, perché molto spesso non ne ha. Il docente riporta un episodio. Una serie storica costruita con colleghi di Bologna presentava un picco, e si voleva capire se in quel momento fosse accaduto qualcosa di specifico in quel mercato. Un sistema di intelligenza artificiale, di cui non ricorda il nome, rispose che il picco dipendeva dalla rivoluzione industriale di quegli anni. La rivoluzione industriale era però avvenuta circa 100 anni prima o dopo, e la risposta era completamente sbagliata: il fenomeno osservato era stato spiegato in modo non corretto.

La consapevolezza di ciò che si sta facendo, e di ciò che non si deve fare, è quindi probabilmente più importante. L'intelligenza artificiale, come qualsiasi strumento, può essere utile per affinare l'intuizione, ma il controllo, come diceva la professoressa Biglio, deve restare allo studente. Lo scopo del corso è dare questa consapevolezza: che cosa non fare e come capire quando un modello non va bene. A questo fine bisogna conoscere le potenziali cause di problemi, che sono tipicamente di tre tipi.

## Il termine d'errore e i modelli con troppe poche informazioni

Il primo tipo di problema si ha quando il modello è sbagliato perché contiene troppe poche informazioni. In tal caso ciò che il modello non spiega potrebbe avere un effetto sistematico sulla relazione tra le variabili di interesse.

In statistica e in econometria occorre decidere quale sia la variabile dipendente, $y$, e quale il driver, $x$. Interessa la stima del parametro $\beta$ che lega le due variabili: se $\beta$ è positivo, all'aumento di $x$ corrisponde un aumento di $y$, se è negativo accade il contrario. Il problema è stimare $\beta$. Il modello non contiene però soltanto due variabili. Nel contesto più semplice ne contiene una terza, il termine d'errore. Dal punto di vista puramente statistico, come si vede in un corso di statistica, è una variabile casuale con media zero e varianza qualsiasi. Dal punto di vista economico raccoglie tutte le informazioni che non sono dentro il modello.

Occorre chiedersi se queste informazioni siano rilevanti e se abbiano un effetto su $x$. Se lo hanno, a una variazione di $x$ non corrisponde soltanto una variazione di $x$, ma anche una variazione di $y$, e ciò che si misura come variazione di $y$ è un misto di cose. La politica economica, che dovrebbe dipendere solo da $x$, dipende anche da $y$, ma $y$ non è osservato perché è una variabile casuale non osservabile, un errore. Di conseguenza non si è più in grado di valutare che cosa stia facendo il modello.

> [!question] Da verificare: nel passaggio la trascrizione riporta "Y" dove, per il senso (variabile casuale non osservabile, errore), si tratta probabilmente del termine d'errore.

## Previsione e spiegazione: l'esempio della Nutella

Quanto detto non è un problema se lo scopo del modello è fare previsioni. La previsione è un gioco semplicemente statistico: se $x$ assume un certo livello, $y$ assumerà un certo livello. Per preparare la catena di produzione della Nutella non interessa sapere perché la gente la mangia, se sia buona, se costi poco o tanto. Interessa sapere che a un certo momento dell'anno bisogna comprare 7 tonnellate di nocciole. Capire se ci sia una relazione logica tra variabili non è particolarmente rilevante: il problema pratico è rifornire la catena di montaggio. Se una scatola nera indica di comprare 7 tonnellate in quel periodo, si comprano e non serve sapere altro.

Se invece si vuole capire perché la gente compra la Nutella, non basta sapere che la comprava anche ieri. Occorre sapere, per esempio, che il gusto non piace, perché allora bisogna cambiare la ricetta, il packaging e così via.

Il corso presenta esempi della distinzione tra l'analisi statistica, cioè la previsione, e la ricerca dei driver che muovono la variabile. Lo scopo è soprattutto il secondo: il primo, con un modello banale, si realizza in modo quasi automatico. Il docente aggiunge che chi faceva le previsioni sulle nocciole della Nutella guadagnava dell'ordine di un milione di euro l'anno, cifra riferita a 15-20 anni fa, quindi sono lavori di un certo interesse.

> [!question] Da verificare: l'inciso sui compensi è in parte illeggibile (un riferimento alla Ferrari non è ricostruibile) e poi si parla di "trent'anni" fa, in contrasto con i 15-20 anni.

Il corso mostra soprattutto la distinzione tra statistica ed econometria, che sta nella relazione logica tra le variabili. Dal punto di vista puramente tecnico questa relazione si chiama esogeneità, e viene formalizzata con un indicatore di correlazione tra qualcosa che non si osserva e qualcosa che si osserva. Il docente mostrerà come capire se un modello è affetto da endogeneità e, su quella base, come risolvere il problema. Il primo caso di endogeneità si ha quando nel modello si mettono troppe poche variabili: tutte le altre variabili che non vengono inserite finiscono nel termine d'errore.

Quando una variabile omessa finisce nel termine d'errore, una variazione di $x$ causa una variazione di $y$ e, insieme, una variazione del termine d'errore, che si indica con $\varepsilon$. La variazione della variabile dipendente è allora una combinazione di due componenti, e se ne misura solo il totale senza sapere quanto conti ciascuna.

> [!question] Da verificare: l'inizio del segmento è garbato ("di Y il termine d'errore chiama epsilon"); la ricostruzione sopra è la più probabile.

Se si capisce che l'imprecisione del modello deriva dal fatto di essere troppo piccolo, la soluzione è togliere variabili dal termine d'errore, cioè inserirle nel modello, usando ragionamenti logici e non numerici. Non si usa una procedura puramente statistica per selezionare l'errore: il problema è economico, e si tratta di capire quali siano le variabili che contano davvero. A guidare la definizione del modello è la teoria economica, non i dati. Il docente tornerà più avanti su come risolvere il problema.

## Causalità non chiara tra le variabili

Un secondo problema si ha quando la relazione di causa ed effetto non è chiara: è $x$ che influenza $y$ o $y$ che influenza $x$? In questo contesto si può dimostrare che non si sa più se, muovendo una variabile, si muove l'altra. Si introduce di fatto un riferimento circolare, e non si capisce più quanto una variazione di $x$ incida su $y$. Il cortocircuito crea una correlazione tra $x$ e l'errore, e la stima dei coefficienti diventa problematica.

## Errori di misura nei dati

L'ultimo problema è più tecnico e più sottile e riguarda la qualità dei dati. Si può dimostrare con facilità che, anche se il modello è perfetto, dati approssimativi e poveri di informazione inducono una distorsione nella stima dei parametri a causa dell'errore di misura delle osservazioni. La distorsione è tanto più grande quanto più è grande l'errore di misura.

Il docente propone un esempio. L'Istat, o un'agenzia che conduce analisi simili, intervista migliaia di persone per capire le loro preferenze di spesa e chiede, per esempio, quanto hanno speso al supermercato nell'ultima settimana. Il docente stesso non ricorderebbe con esattezza la cifra. Se ha speso 190 euro, gli è più facile ricordare 200 e scrivere 200 sul modulo; chi spende 205 riporta ugualmente 200. Quasi tutti fanno un'approssimazione di questo tipo. L'errore di riporto, anche se non è sistematico e la spesa media nel campione è corretta, introduce rumore nella procedura di stima, e questo a sua volta distorce la stima del parametro. Non si sta dicendo che la gente sottoriporti o sovrariporti sistematicamente ciò che ha fatto: è semplicemente imprecisa, perché non ricorda, magari perché la domanda si riferisce a qualcosa accaduto molto tempo prima.

A titolo di aneddoto, il docente racconta che, tornando dagli Stati Uniti dopo circa sette mesi, fu fermato nell'aeroporto di Venezia da addetti dell'Istat che chiedevano quanto avesse speso nell'ultimo viaggio. Diede una stima a spanne, dicendo 10.000 euro, che poteva essere 15.000 o 5.000: non lo ricordava affatto, e il numero era del tutto casuale. Chi invece è stato via una settimana sa indicare con una certa precisione quanto ha speso. Il punto è che la gente non sbaglia a riportare la spesa effettiva se non perché non ricorda.

Il caso è diverso per le evasioni fiscali. In un'analisi fiscale tutti tenderebbero a sottostimare o a sovrastimare, e in quel caso potrebbe esserci una distorsione sistematica. Un campione di quel tipo è quasi preferibile, perché una distorsione di quel tipo si può controllare più facilmente. Qui si parla invece di persone oneste ma un po' imprecise, e questo può creare grossi problemi. Il docente mostrerà con dati simulati, quindi controllabili, che cosa succede in questi casi.

## Struttura del corso

Tutte queste questioni saranno analizzate in parte dal punto di vista teorico, perché la formula aiuta a capire meglio che cosa sta accadendo, e in parte dal punto di vista empirico, perché vedere le conseguenze delle azioni è probabilmente la cosa più utile. La teoria sarà svolta senza un'algebra complicata: il docente cercherà di non usare l'algebra matriciale e di ricorrere a strumenti relativamente semplici, come algoritmi e derivate. I sistemi studiati saranno rappresentati anche in forma matriciale, ma solo per mostrare che non c'è differenza rispetto alla notazione abituale. La matrice è soltanto una strategia per rendere le formule piccole e compatte, né più né meno.

> [!question] Da verificare: la trascrizione riporta un confronto illeggibile ("rispetto a scrivere le cose come sottopo o per meno"), omesso qui.

La prima parte del corso è una rassegna del modello di regressione, concentrata sui casi in cui il modello non va bene. Nella seconda parte si analizzano i dati in serie storica: la strategia resta sempre la regressione, ma il modello cambia a seconda del tipo di dati disponibili.

## Dati dinamici e stabilità: il limite della media

Nell'analisi del modello di regressione si assume di solito che le osservazioni siano pescate in modo indipendente dalla popolazione: si ha un campione di persone scelte a caso, e le unità statistiche che forniscono le informazioni sono indipendenti tra loro. Se le osservazioni fossero indipendenti, i coefficienti di legame tra di esse sarebbero uguali a zero.

> [!question] Da verificare: la frase originale ("avrei tutti i coefficienti di legame tra la variabile sarebbe uguale a zero") è garbata; si intende probabilmente il legame tra le osservazioni della stessa variabile.

Nei sistemi dinamici, tipici della finanza, dell'economia e delle serie storiche, le variabili hanno una loro inerzia e non sono osservate in modo indipendente. Se il tasso di interesse oggi è il 5%, domani non sarà 0% né 10%, ma 5% con una piccola variazione. Questo crea un problema di stabilità delle traiettorie dei dati, e la statistica funziona bene se i dati sono stabili nel tempo. Il motivo è intuitivo.

Il docente lo illustra alla lavagna. Si supponga che i dati abbiano un andamento come quello disegnato, tipico del prezzo di un asset finanziario, per esempio i prezzi giornalieri dello Standard & Poor's. Ci si chiede se un fenomeno con una dinamica di questo tipo si possa descrivere con indicatori sintetici. Tecnicamente sì: si può calcolare la media dei prezzi giorno per giorno, e un software restituisce il numero. La media è però un indicatore di centralità, e cade in un punto intermedio rispetto ai dati, rappresentato da una riga orizzontale. Questo indicatore descrive bene il comportamento del fenomeno solo in un intervallo temporale, per puro caso, e non negli intervalli che lo precedono e lo seguono nel grafico.

Se i dati non sono stabili, la statistica descrittiva rappresenta caratteristiche di una popolazione troppo eterogenea nel tempo. Una media che mette insieme i prezzi tipici degli ultimi cinque anni e quelli di trent'anni fa è un numero utile né per descrivere ciò che accade oggi né per descrivere ciò che accadeva allora. Si stanno usando dati che provengono da popolazioni statistiche diverse, ciascuna con una media diversa; mescolandoli, la stima è una stima di medie.

Un esempio più semplice: una popolazione in cui il 50% è alto due metri e il 50% è alto un metro. Pescando a caso, nel campione metà della popolazione avrà altezza molto alta e metà molto bassa. Le medie che rappresentano la popolazione sono quindi due, quelle delle distribuzioni condizionali dei bassi e degli alti, un metro e due metri.

Calcolando però una media aritmetica sul campione, si ottiene una stima di circa un metro e mezzo, che non è un indicatore utile né per il gruppo dei bassi né per quello degli alti. Il problema della stabilità della serie è esattamente questo: se i dati non sono sufficientemente regolari, tutte le statistiche descrittive e tutti i parametri stimati dal modello non hanno alcun significato logico. Numericamente si può calcolare tutto, ma dal punto di vista operativo i numeri non significano nulla. Una delle ipotesi da fare quando si usano dati in serie storica è quindi che la serie sia stabile nel tempo, quantomeno che abbia una media comune.

## Trasformazioni che stabilizzano la serie

Esistono trasformazioni delle serie storiche originali che tendono a stabilizzarle. Sono trasformazioni uno a uno, quindi non fanno perdere informazione, o ne fanno perdere zero. Tipicamente, anziché i prezzi si usano le variazioni di prezzo, cioè i rendimenti. I rendimenti hanno di solito una media stabile, tipicamente zero, come si osserva nei dati. Ciò che cambia nel tempo è invece la variabilità della serie, ma questo si può gestire in modo più naturale.

A questo è dedicata la classe di modelli ARCH e GARCH, usati in finanza, per i quali è stato assegnato il premio Nobel nel 2000 e qualcosa. Il problema diventa capire, per esempio in ambito finanziario, perché la varianza, che è un indicatore di rischio di un investimento, cambia nel tempo e in che modo cambia. Ciò permette di costruire misure di rischio utili dal punto di vista operativo, ed è quello che si fa tipicamente nei corsi di analisi del rischio e di risk management.

Quando i dati sono dinamici e osservati nel tempo, non sono indipendenti. Occorre controllare che la dipendenza sia sotto controllo. Se la dipendenza genera una componente di trend, la statistica descrittiva standard non funziona più. Si può dimostrare anche analiticamente che il teorema del limite centrale e la legge dei grandi numeri non valgono più, e che tutte le proprietà statistiche degli indicatori vengono meno. Il problema è però sostanzialmente logico: si mescolano dati non coerenti tra loro, e il risultato è una mistura di indicatori di centralità di cose estremamente diverse, un numero privo di interpretazione.

## Regressione spuria e cointegrazione

Con le serie storiche bisogna prestare attenzione a questo fenomeno. Se non lo si considera, anche con modelli semplici e facilmente controllabili un test classico assegna un p-value estremamente piccolo, che è il contrario di ciò che ci si aspetta. Il fenomeno si chiama regressione spuria. Si prendono due serie indipendenti per costruzione, ma il test di significatività del coefficiente che le lega risulta sempre diverso da zero. Il motivo è che il test è calcolato sulla base di una distribuzione normale, mentre la distribuzione degli stimatori dei parametri, quando i dati hanno queste caratteristiche, non è più normale. Il software non lo sa e restituisce un numero privo di senso.

In generale, con dati non stabili non si può usare facilmente la regressione, a meno che i dati non siano stabilizzati prima. Fa eccezione la cointegrazione, estremamente importante soprattutto in ambito finanziario ma anche economico. Nonostante i dati abbiano le caratteristiche descritte, se le caratteristiche di regolarità sono più o meno stabili si può sperare che anche la relazione tra le variabili sia stabile, e che il parametro che lega le variabili sia sostanzialmente identificabile.

## Percorso del corso

La prima parte del corso riguarda ciò che non va guardato in un output di regressione e ciò che non va fatto in un modello di regressione quando i dati sono indipendenti. La seconda mostra che cosa cambia in un contesto di dipendenza e quali modelli si possono usare per sfruttare la regolarità nel tempo delle serie. Dal punto di vista concettuale è una seccatura, ma una volta che si sa che un sistema dinamico ha una sua inerzia, la si può usare sia per fare previsioni, sia per cercare modelli migliori dal punto di vista statistico ed economico. I modelli a correzione d'equilibrio saranno l'ultimo argomento.

Lo scopo del corso è quindi dire più che cosa non fare che cosa fare. La parte di interpretazione è particolarmente importante: capire perché si usa un modello e come si interpretano i risultati di quello specifico modello.

## Materiali, software ed esami

Tutto il materiale si trova nella pagina Moodle del corso, Econometria 2026-2027. Il docente carica il materiale prima delle lezioni e lo aggiorna di volta in volta. A parte i primi due set di slide che verranno utilizzati, gli altri sono la versione dell'anno precedente, cambiata solo in parte; quella presente può essere la penultima versione, aggiornata poi con regolarità. La pagina contiene sia i lucidi sia i dataset, perché una parte del corso è applicata. Nelle esercitazioni si vedrà come analizzare i dati e come scovare i problemi di un modello, che certe volte non sono facili da individuare. Le esercitazioni sono tenute dal dottor Peruzzi.

Il software utilizzato è Gretl. Il docente lo ha scelto perché è molto semplice da usare, e permette di concentrarsi sulla parte econometrica più che sui comandi. È immediato, gratuito, disponibile su qualsiasi piattaforma e in certi aspetti migliore di molti altri. Si usa a tasti, e c'è anche un linguaggio in background, che però non è la cosa più importante. In più, il libro di testo mette a disposizione tutti i dati degli esempi, scaricabili anche in formato Excel: chi è interessato alla materia può riprendere gli esercizi del libro e replicare i calcoli per fare pratica. Il docente osserva che tutti i libri di testo che conosce mettono a disposizione i dati.

In econometria il problema non è stimare il modello, ma capire che cosa si sta facendo e se il modello stimato va bene oppure no. La teoria fornisce una casistica di problemi da controllare quando ci si approccia all'analisi empirica di un modello economico.

Sulla pagina Moodle sono presenti anche i vecchi esami. Prima dell'esame finale si faranno esercitazioni in stile esame, mock exam, per cui il docente potrà distribuire il testo con un certo anticipo; gli esercizi si svolgeranno con lui, con il dottor Peruzzi o con il tutor. Anche questa lezione si può recuperare.

> [!tip] Esame: il docente incoraggia a venire a ricevimento, anche se di solito ci va poca gente. Conviene risolvere i problemi prima dell'esame, perché dopo l'esame spiegare dove sono gli errori è troppo tardi: il compito è ormai fatto.

## Iscrizione a Moodle, ricevimento e modalità d'esame

Il docente chiede se gli studenti siano iscritti automaticamente alla pagina Moodle del corso quando l'esame è nel piano di studio. Gli studenti rispondono che devono iscriversi manualmente. Il docente consiglia di farlo, se non lo si è già fatto: in questo modo può contattare tutti insieme per comunicare un cambio d'orario di una lezione o l'invio di materiale extra, altrimenti non saprebbe come raggiungerli.

Gli studenti possono scrivere email al docente se l'orario di ricevimento ufficiale non va bene: se il docente è disponibile si può trovare un altro momento, anche online. L'unica cosa che non si può fare online è la visione dell'esame: chi vuole vedere il proprio compito deve andare di persona, perché il docente non ha tempo di scansionare cento compiti. Ricevimenti standard a parte questo non sono possibili. Per chi ne ha diritto, le registrazioni delle lezioni saranno scaricabili dalla pagina Moodle, se la funzione è attiva.

> [!tip] Esame: l'esame è scritto. Il docente rimanda agli esempi dei compiti vecchi. Tipicamente è organizzato in una decina di domande, ma il numero non è fissato, e si chiede di interpretare dei risultati: non si chiede di eseguire le stime. Spiegare come si fa una stima con un software o con un altro è utile a chi vuole diventare più operativo, ma per l'esame non è particolarmente necessario.

## Le lezioni empiriche con il dottor Peruzzi

Il docente consiglia comunque di frequentare le lezioni della parte empirica, perché contengono anche spiegazioni su come interpretare i modelli. La prima di queste lezioni, probabilmente non oggi ma la settimana prossima, tratta che cosa succede quando si riscalano le variabili con trasformazioni come il logaritmo, e come si interpretano gli effetti marginali quando le variabili sono in una scala diversa, approssimata o esatta. Tratta anche come diagnosticare un problema patologico del modello, la quasi collinearità: la collinearità esatta è facile, perché con due variabili esattamente collineari il software si blocca, mentre la quasi collinearità non è altrettanto facile da riconoscere. Questi casi sono trattati in modo empirico, ma servono anche nel compito. La parte empirica è più intuitiva per spiegare alcuni strumenti, come il variation factor, che serve a diagnosticare un problema di quasi collinearità. Se non ci si accorge del problema, si crede che il modello dia risultati corretti, mentre non lo sono.

> [!question] Da verificare: la trascrizione riporta "variation factor"; probabilmente il variance inflation factor (VIF), che non compare nelle note del corso.

Le lezioni empiriche sono importanti perché, insieme alla parte meccanica (come si stima il modello, come si fanno le cose), contengono una componente di interpretazione legata a ciò che si fa dal punto di vista teorico. L'idea è creare un legame tra teoria e pratica.

Il compito conterrà dunque domande in cui si chiede di interpretare risultati, analizzando grafici e tabelle, e di capire se il modello ha un problema oppure no. Per la parte di serie storica si chiede inoltre di capire se un modello è corretto dal punto di vista metodologico, di interpretare i risultati dinamici e statici di un modello dinamico, e così via. Ci sono già esempi, e prima dell'esame si vedranno esercizi di questo tipo.

## Feedback e libro di testo

Il docente invita a interromperlo in qualsiasi momento, perché il feedback sul momento gli fa piacere: il corso è per gli studenti, non per lui, e più ne beneficiano meglio è. Aggiunge che una delle cose che odia di più è correggere i compiti, quindi se tutti passassero con voti altissimi sarebbe la persona più felice del mondo. Se nessuno dà feedback, va avanti per la propria strada e potrebbe esserci uno scarto tra lui e gli studenti; se se ne accorge alle ultime tre lezioni, c'è poco da fare. Si possono dare feedback di qualsiasi natura, e il docente precisa di non essere vendicativo. Se ci sono interessi specifici da esplorare, il programma può essere modificato volentieri, se c'è tempo. Si può intervenire durante il corso, a fine lezione o a ricevimento.

L'acquisto del libro non è obbligatorio, perché non si può obbligare ad acquistarlo, ma è un supporto utile. Il docente lo segue abbastanza ed è molto discorsivo: contiene la parte tecnica ma anche molti esempi che portano a capire la tecnica, soprattutto nei capitoli sulle serie storiche e sulla regressione. Ci sono poi argomenti in più che non c'è il tempo di trattare. Il libro è disponibile in biblioteca. Il docente consiglia di leggerlo, perché aiuta a capire i dettagli che a lezione non fa in tempo a raccontare, e di non limitarsi ai lucidi pubblicati online: sono uno schema per prendere appunti, o una scaletta per il docente, messa a punto in circa trent'anni di insegnamento. Il libro dà di più, e in particolare contiene molti esempi che spiegano bene il perché delle cose.

## Materiale introduttivo e definizione di econometria

Questo è il primo set di lucidi, di introduzione al corso. Il docente ha inserito nella pagina Moodle anche informazioni tratte da appunti usati qualche anno fa per un corso di statistica di base, per richiamare i concetti essenziali e gli strumenti che servono per dimostrare i risultati. Il materiale è molto semplice, ma una volta capito come funzionano varianze e medie, il resto è abbastanza semplice. Chi vuole richiamare la statistica per fissare la notazione, per esempio perché la media si indica con $E$, trova tutto all'inizio della pagina Moodle.

L'econometria ha tre scopi, che in generale si possono racchiudere nell'analisi quantitativa di modelli economici. Non esiste nemmeno una definizione chiara di che cosa sia: il docente dice di non averla ancora capita alla sua età, ma c'è abbastanza consenso su tre aspetti. Il primo è la misura delle relazioni di causa ed effetto tra variabili. Il secondo è fare previsioni, che è però più statistica che econometria; il docente osserva che gli econometrici sono "una famiglia accogliente" e prendono dentro anche gli statistici. Il terzo, che gli piace particolarmente, è usare metodologie anche avanzate per valutare teorie economiche.

Si parta da un modello economico astratto, per esempio il CAPM, che si vede spesso nelle applicazioni finanziarie. Il CAPM non è un'equazione: sono due pagine di algebra che portano a un'equazione secondo cui gli extra-rendimenti di un investimento sono proporzionali agli extra-rendimenti di un portafoglio di mercato, qualsiasi esso sia. Il problema è che quella è un'equazione. Per arrivare al modello occorrono molte ipotesi: che il mercato dei capitali sia in equilibrio, che il mercato dei tassi di interesse sia in equilibrio, che gli investitori costruiscano portafogli con l'algoritmo di Markowitz, ipotizzando che funzioni. Si fanno i conti e si ottiene quella relazione.

Il punto è se quella relazione sia credibile e se i dati la supportino. Come si può validare il modello? Se il modello fosse vero, un rendimento in media non dovrebbe garantire un premio extra per il rischio, e dal punto di vista operativo ciò si traduce nel fatto che il modello di regressione non può avere l'intercetta. Per validare un modello banale come il CAPM, dimenticando tutto ciò che porta all'equazione finale, si può costruire una regressione semplice che include l'intercetta e valutare se l'intercetta è uguale a zero oppure diversa da zero. Questo potrebbe essere un possibile test; non è detto che poi funzioni, ma è un'idea. L'idea è usare una metodologia econometrica per verificare se un modello economico è coerente con i dati, perché un modello economico incoerente con ciò che si osserva ha pochissima utilità.

Se il modello economico non supera il test econometrico, non si può semplicemente aggiungere un'intercetta al modello. Aggiungerla significherebbe cambiare tutte le equazioni e tutte le ipotesi fatte prima, cioè le due pagine di algebra precedenti. Se il test econometrico non supporta il modello economico, bisogna rispecificare il modello economico in modo che il modello statistico accetti quelle variazioni. La validazione di un modello è quindi un'altra funzione importante: si ha una teoria, si hanno dei dati, e si vuole vedere se la teoria è coerente nello spiegarli. Il docente dice che questa è la parte per lui particolarmente importante, la sua preferita.

## Relazioni di causa ed effetto e criteri di causalità

La prima parte del corso riguarda le relazioni di causa ed effetto. Il docente vuole spiegare brevemente che cosa sono e qual è il pericolo nell'usare i metodi statistici senza aver pensato prima, a monte dell'analisi empirica, a quali siano le potenziali relazioni logiche tra le variabili.

Dal punto di vista grafico, una relazione causale si rappresenta con due variabili, $x$ e $y$, e una relazione asimmetrica: $x$ ha un impatto su $y$ ma non viceversa. $x$ è un driver per $y$, e il viceversa non vale. Il problema tipico è capire se $x$ sia una causa di $y$ oppure no. Perché la relazione tra due variabili sia di causa ed effetto, devono valere sostanzialmente tre criteri.

Il primo è un criterio puramente statistico. Il docente precisa che con ciò ritira quanto detto poco prima: la parte statistica è diversa dalla parte economica, ma in realtà è l'inizio. Per vedere se esiste una relazione causale tra due variabili occorre prima stabilire che esista almeno una relazione statistica. Senza relazione statistica, anche se ci fosse una relazione causale, una variazione di $x$ non avrebbe impatto su $y$ e l'interesse per il problema verrebbe meno. Se le variabili sono quantitative, ci deve essere una correlazione statisticamente significativa tra $x$ e $y$.

Il problema è che la correlazione è una relazione simmetrica tra le variabili, mentre nel grafo si è definito che $x$ ha un impatto su $y$ e non viceversa. La correlazione tra $x$ e $y$ e quella tra $y$ e $x$ sono lo stesso numero, quindi una correlazione non dice nulla sulla direzione. Indica solo un legame di qualche natura, non necessariamente logico. Per definire una relazione causale bisogna aggiungere ipotesi: ci deve essere un legame logico tra le variabili, non solo statistico, con una variabile che ne anticipi l'altra non solo dal punto di vista temporale ma dal punto di vista puramente logico. Non basta un legame statistico tra due quantità: serve una storia che spieghi perché esiste quel legame statistico, e quella storia deve essere unica. Non basta sapere che c'è un legame logico, occorre che sia unico. Il docente mostrerà esempi per legare questo ragionamento astratto alla pratica economica, probabilmente nella lezione successiva, guardando alcuni dati.

> [!question] Da verificare: il docente annuncia tre criteri ma ne enumera esplicitamente solo il primo; gli altri due (legame logico con precedenza logica, storia unica) sono ricostruiti dal seguito. Il passaggio sul caso di più storie coerenti con la stessa dipendenza statistica ("lo troverò migliore") è garbato e non è riportato.

## Correlazioni spurie: Big Bang Theory e lacrosse

La cosa importante è che il legame statistico non è sufficiente. Per mostrarlo, il docente propone un esempio scaricabile online da una pagina web di uno statistico buontempone. Lo statistico ha un database di circa 10.000 variabili e ha chiesto a un programma di cercare le coppie di variabili più correlate possibili, senza considerare quali variabili fossero.

Nel primo esempio la serie storica nera è il numero di persone che hanno guardato la serie televisiva Big Bang Theory, e la serie rossa è il numero di ricerche su Google che cominciano con "how to make". Dal punto di vista logico non c'è alcun legame tra le variabili, ma il grafico mostra due serie estremamente vicine. Paradossalmente, sapendo che nel 2016 Big Bang Theory ha avuto un certo livello di visibilità, si potrebbe usare questa informazione per prevedere il livello dell'altra variabile, perché la correlazione è forte. Dal punto di vista puramente predittivo le due serie sono correlate e si potrebbe usare l'una per prevedere l'altra. Ma questa correlazione non ha una spiegazione logica, e tipicamente le relazioni di questo tipo non ce l'hanno.

L'$R^2$ della relazione è 96,5%. Questo valore spiega solo il legame statistico, non altro, ed è un numero molto fuorviante: dice soltanto che le due serie si muovono insieme, non perché. Considerando un modello di regressione e usando l'$R^2$ come indicatore di bontà del modello, esso indica che i dati sono ben approssimati, non che il modello è corretto dal punto di vista logico, che è ciò che si cerca.

Sul sito, in alcuni casi, sono presenti spiegazioni prodotte con intelligenza artificiale del motivo di una correlazione così alta.

Un secondo esempio mette in relazione l'esito delle partite finali di lacrosse, sport molto popolare negli Stati Uniti (serie nera), con i biglietti venduti al cinema (serie rossa). Non c'è alcun legame sostanziale tra le serie, ma anche qui la correlazione è alta: intorno al 74%, in ogni caso oltre il 50%. Se si chiede all'intelligenza artificiale di spiegare l'associazione, qualcosa viene fuori, e una storia si può sempre trovare. Il punto è che non è una storia che abbia necessariamente senso.

> [!question] Da verificare: "la cross" è ricostruito come lacrosse; la correlazione è riportata come "il 74% o più del 50%", valore non univoco.

Il docente invita a guardare questi esempi per vedere che il legame statistico non ha niente a che fare con il legame logico. È solo uno dei prerequisiti, il primo pezzo. Un $R^2$ grande non vuol dire che il modello vada bene. Anzi, tipicamente i modelli buoni non hanno un $R^2$ molto grande, e un $R^2$ troppo grande porta con sé problemi statistici non banali, noti come problema di collinearità.

Nelle serie mostrate le variabili sono molto legate dal punto di vista statistico, ma nessun motivo logico le lega. Combinarle non spiega perché una delle due si muova, e quindi non dà alcuna capacità di fare analisi di scenario.

Le variabili degli esempi sono piuttosto inutili, ma si immagini di trovare una correlazione tra due variabili economiche che non c'entrano niente l'una con l'altra e di voler fare un'analisi di scenario, come quelle citate dal professore. Qualsiasi risultato sarebbe del tutto casuale e non replicabile, perché non c'è un legame.

## Come lavorare quando non esiste una risposta definitiva

Per quanto ci si sforzi di trovare relazioni causali, non si sarà quasi mai in grado di avere una risposta definitiva. Si può spiegare logicamente il legame statistico tra due variabili, ma è quasi impossibile escludere tutte le altre spiegazioni logicamente valide della correlazione. Nulla è però perduto: la distinzione causale fornisce una chiave di lettura e una regola di lavoro.

Ogni volta che si costruisce un modello bisogna capire perché lo si fa e perché si selezionano certi tipi di variabili. Si verifica poi se il modello descrive le aspettative, per esempio se i coefficienti hanno il segno corretto. Un segno sbagliato può indicare che le correlazioni attese non sono stimate in modo corretto, come si vedrà formalmente. Lavorare in modo logicamente coerente permette alla disciplina di avanzare, cioè di far progredire lo studio di un certo fenomeno. Il proprio modello può non essere quello definitivo, ma contribuisce al lavoro degli altri che cercano di risolvere lo stesso problema, provano altri modelli e valutano se il loro è migliore. Si va avanti finché non si trova un equilibrio in cui c'è consenso: si è provato con 10.000 modelli su un fenomeno specifico, si è convinti che la relazione causale sia esattamente questa e tutte le altre sono state escluse.

La speranza di trovare un modello perfetto, che rispecchi le tre caratteristiche viste, è quindi troppo ambiziosa; soprattutto la terza richiederebbe troppo tempo. Secondo il docente è importante capire che la relazione statistica non basta e che occorre ragionare ogni volta in termini di legame logico tra le variabili. Una volta pensato un legame logico, si prova a vedere se resiste a spiegazioni alternative logicamente ben strutturate. Un po' alla volta, nel tempo, ci si fa un'idea. Bisogna lavorare sempre in questa dimensione, pensando che ciò che si fa non sarà definitivo ma che va fatto con regole sostanzialmente precise. Provare regressioni e modelli buttando dentro i dati, nella speranza di trovare qualcosa che piaccia in termini di segni, non è sufficiente. È difficilissimo trovare relazioni causali, ma con un po' di pazienza qualcosa si trova.

## Esempio: fumo e malattie ai polmoni

Il docente non ha con sé i dati reali, ma riassume quanto emerso nella letteratura epidemiologica nel corso di molti anni. L'associazione tra fumo e gravi malattie ai polmoni c'è, la correlazione c'è. È sufficiente per dire che esista una relazione di causa ed effetto? No. Negli anni sono state testate varie ipotesi e varie teorie, per decine di anni e non per settimane. Un po' alla volta si è trovato che il legame è logico, cioè c'è un motivo biologico per cui il consumo di sigarette può aumentare l'incidenza di certi tipi di malattie: sono stati individuati dei meccanismi. Basta? No, potrebbero esserci altri meccanismi non ancora visti. Questo screening tra le varie opzioni è però stato raffinato, e oggi si ritiene più o meno che esista una relazione di causa ed effetto. È definitiva? Probabilmente sì, ma se qualche biologo trovasse un'alternativa più convincente di quelle attuali, bisognerebbe ripensare tutto. La procedura va dunque avanti in modo progressivo, e trovare un modello che risolva tutti i problemi in modo definitivo è praticamente impossibile.

> [!question] Da verificare: la trascrizione riporta "negli ultimi centinaia d'anni" per l'arco della letteratura epidemiologica; poco dopo il docente parla di "decine di anni".

Ciò che conta è che, ogni volta che si propone o si lavora su un modello, ci sia la convinzione che non sia un semplice tentativo, ma un tentativo fatto con un background. Prima di affrontare un problema economico e prima di arrivare ai dati, bisogna capire quali siano i potenziali driver di interesse, e solo dopo inserirli nel modello. Non si deve fare il contrario, cioè mettere tutto nel modello e poi selezionare le variabili finché non si trova qualcosa. La teoria deve definire a priori i legami logici, e non ci si può far raccontare la storia dalla correlazione.

## Esempio: boy scout e criminalità, la causalità inversa

Un altro tipo di problema si vede con un esempio di dati inventati, tratti da un libro di statistica, che mostra da dove possono nascere le correlazioni spurie tra variabili. È una tabella a doppia entrata in cui si osservano dei ragazzini: alcuni hanno fatto i boy scout da piccoli, e anni dopo è stato guardato il loro record criminale. I dati non sono reali, potrebbero esserlo; il docente li ha ricopiati da un libro di testo usato per un corso di statistica anni fa.

Una variabile indica se si è stati boy scout, sì o no; l'altra se si sono avuti problemi con la giustizia. Si osserva che tra chi ha fatto il boy scout l'incidenza di problemi con la giustizia è più bassa, mentre nelle altre celle della tabella le percentuali sono alte. Sembra quindi che ci sia una relazione negativa tra l'essere stati boy scout e l'essere un criminale.

Ci si chiede se questa correlazione sia supportata da un'intuizione logica. Chi ha fatto il boy scout viene magari educato a comportarsi bene: gli vengono date regole e principi, e gli si fa capire che aiutare un'anziana ad attraversare la strada è positivo. Chi ha fatto il boy scout avrebbe quindi ricevuto input diversi dagli altri, sarebbe una persona migliore, tra virgolette, e avrebbe una probabilità più bassa di essere arrestato. È una relazione del tipo boy scout, delinquenza.

Un'altra persona potrebbe obiettare che chi è totalmente cattivo probabilmente non si sarebbe mai iscritto ai boy scout: chi è avverso al rispetto delle regole non va in un posto dove ne trova molte. Essere una persona avversa alle regole farebbe quindi sì che non ci si iscriva ai boy scout, e la correlazione si spiegherebbe nella direzione opposta. Il legame statistico, che è simmetrico, non dice nulla sulla direzione tra le variabili. Questo si chiama reverse causality, ed è un problema per la stima di una relazione di causa ed effetto. Prima ancora di arrivare al modello bisogna quindi ragionare su quali siano i potenziali legami logici tra le variabili.

## Prossima lezione

La lezione di oggi era una chiacchierata. A partire dalla prossima, giovedì, si ragionerà su come definire un modello statistico che cerchi di descrivere una relazione causale e su come capire quando il modello statistico supporta o non supporta una relazione di questo genere.
