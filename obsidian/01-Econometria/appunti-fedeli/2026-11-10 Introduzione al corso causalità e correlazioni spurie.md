---
corso: Econometria
data: 2026-11-10
fonte: Materiali/audio/econometria/econometria_2026-11-10.txt
tipo: appunti-fedeli
tags: [appunti-fedeli, econometria]
revisione: trascrizione gpt-transcribe ripulita, fedele al parlato
---

# Introduzione al corso: causalità e correlazioni spurie

## Obiettivo del corso: interpretare, non calcolare

L'idea è di farlo più intuitivo che tecnico. Non so benissimo qual è il vostro background; di solito una parte della classe ha già fatto i corsi di econometria, 50% ha visto magari i modelli, ma dal punto di vista solamente statistico.

> [!question] Da verificare: la trascrizione riporta "scuota percento della classe"; la percentuale non è leggibile.

Chi ha già fatto econometria? Quindi siete quasi tutti. L'idea allora è di focalizzarvi sull'interpretazione economica, sull'interpretazione. Il corso sarà di fatto cosa non fare, non come si fanno le cose, perché molto spesso l'econometria viene presentata come una disciplina tecnica. È in realtà una cosa abbastanza ibrida: già la distinzione tra econometria e economia non è così netta, e soprattutto tra econometria e statistica invece lo è. E lo è per via di un'ipotesi aggiuntiva che ha un'implicazione economica importante, che è l'ipotesi di esogeneità.

Lo scopo del corso è farvi vedere cosa succede se costruisco un modello in maniera non corretta, cioè non rispetto le regole dell'economia. Quello che succede è che tutti gli indicatori che vi ha fatto vedere il professore prima, li stimate in maniera sistematicamente distorta. Perché quello che andate a stimare non è l'effetto della vostra politica, ma l'effetto della vostra politica più un fattore di rumore che è incomprimibile. Anzi, più osservazioni avete, più siete precisi nello stimare lo sbaglio. Se vi interessa un parametro, quello che andate a stimare è il parametro più una costante, e anche quella costante non sapete neanche cos'è, quindi l'errore è che voi andate a interpretare un qualcosa come l'effetto di una politica, ma in realtà è un effetto di più effetti collaterali che potenzialmente non è quello che vi interessa. Lo scopo quindi è farvi vedere concretamente, un po' dal punto di vista teorico ma dal punto di vista anche operativo, cosa succede.

Questo è importante perché, è quello che vi diceva il professore, ==la scelta del modello, la scelta delle variabili è la cosa più importante, più che la metodologia per fare i conti veri e propri==. La scelta delle variabili mi permette di escludere il problema dell'endogeneità, che è il problema tecnico, economico.

## Relazioni logiche e non quantitative

Qual è la distinzione sottile? A me interessano relazioni logiche tra variabili, non relazioni quantitative. Vuol dire che non mi interessa che il mio modello si approssimi bene ai dati. In questo corso devo spiegarvi che ==gli indicatori tipo R quadro sono la misura peggiore per valutare il modello. Non dovete proprio utilizzarli==, perché non vi dice nulla che non misurare una correlazione. Lo vedremo adesso che le correlazioni possono raccontare delle storie che sono bizzarre, quantomeno bizzarre, perché molto spesso le correlazioni raccontano delle relazioni spurie tra variabili, non relazioni oggettive.

> [!question] Da verificare: la trascrizione riporta "la misuratura peggiore"; si legge "la misura peggiore".

E se poi, agganciandomi a quello che diceva la professoressa Biglio, andiamo a chiedere a ChatGPT o altro di spiegarmi perché ho una correlazione del 95% fra due variabili, qualcosa ChatGPT tira fuori, che abbia senso o no è irrilevante, molto spesso non ha senso. Una volta, giusto per curiosità, avevo un picco su una serie storica che avevo costruito con dei colleghi di Bologna: volevo capire se in corrispondenza di questo picco era successo qualcosa di specifico in quel mercato, in quel momento storico. E ChatGPT, non mi ricordo quale intelligenza artificiale, mi ha detto: ma certamente questo dipende dalla rivoluzione industriale che in quegli anni... Ma la rivoluzione industriale è successa 100 anni dopo, 100 anni prima, cioè la risposta che ci aveva dato era completamente sbagliata. Il fatto è che il fenomeno mi è stato spiegato in maniera non corretta.

> [!question] Da verificare: la trascrizione riporta "Il fatto è che la correlazione allignment del fenomeno mi è stato spiegato in maniera non corretta"; la frase non è leggibile per intero.

La consapevolezza di quello che si sta facendo, o di cosa non fare, è probabilmente più importante. Per affinare l'intuizione, l'intelligenza artificiale, qualsiasi strumento può essere utile per questo. Però ==il controllo, come diceva la professoressa, dovete avercelo voi==.

## I tre tipi di problema e il termine d'errore

E lo scopo del corso è darvi un po' di consapevolezza: cosa non fare, come cercare di capire quando un modello non va bene. Per capire questo bisogna capire quali sono le potenziali cause di problemi. Le potenziali cause di problemi sono tipicamente di tre tipi. Il primo tipo di problema è se considero un modello sbagliato con troppe poche informazioni. Quello che non è spiegato dal modello potrebbe avere un effetto sistematico sulla relazione tra le variabili che mi interessa.

In statistica e in econometria devo decidere qual è la variabile dipendente, la y, e qual è il driver, quella variabile. Quello che mi interessa è la stima del parametro che lega quei due concetti. Se beta è positivo vuol dire che se aumenta x aumenta y, se beta è negativo viceversa. Il problema è stimare beta. In realtà il modello in un contesto molto semplice è composto anche da una terza variabile, che è il termine d'errore. Dal punto di vista puramente statistico è semplicemente una variabile casuale con media zero e varianza quello che volete. Dal punto di vista economico il termine d'errore raccoglie tutte le informazioni che non sono dentro il modello. Mi chiedo: le informazioni che costruiscono il termine d'errore sono rilevanti? Hanno un effetto sulla x oppure no? Perché se ce l'hanno, in corrispondenza di una variazione di x non ho solo una variazione di x, ma anche una variazione di y, quindi quello che vado a misurare in termini di variazione di y è un misto di cose. Vuol dire che la mia politica economica, che dovrebbe essere dipendente solo da x, dipende anche da y, ma y non lo osservo perché è una variabile casuale, non osservabile, un errore, e di conseguenza non sono più in grado di valutare cosa sta facendo il mio modello.

> [!question] Da verificare: nel passaggio "dipende anche da Y, ma Y non lo osservo" il docente dice "Y" dove dal contesto sembra intendere l'errore; si riporta come detto.

## Previsione e comprensione dei driver

Questo non è un problema se lo scopo del mio modello è fare delle previsioni, che è un giochino semplicemente statistico: se la x assume questo livello, la y assumerà questo livello. Se devo preparare la catena di produzione della Nutella, non mi interessa sapere perché la gente mangia la Nutella, se è buona, costa poco, costa tanto. Mi interessa sapere che devo comprare 7 tonnellate di noccioline a un certo momento dell'anno. Capire se c'è una relazione logica tra variabili non è particolarmente rilevante: se ho una scatola nera che mi dice di comprare 7 tonnellate, io compro 7 tonnellate, non voglio sapere altro. Se invece voglio capire perché la gente compra la Nutella, non mi interessa sapere che la gente compra la Nutella perché ieri la gente comprava la Nutella. Voglio sapere che non gli piace il gusto, devo cambiare la ricetta, il packaging, tutto questo.

Vedremo esempi in cui c'è questa distinzione tra l'obiettivo di fare un'analisi statistica, quindi la previsione, e l'obiettivo di capire quali sono i driver che muovono la variabile. Lo scopo del corso è soprattutto la seconda parte. La prima, una volta che uno sa avere un modellino banale, la può fare in maniera quasi automatica, non è una cosa particolarmente complicata. Per quanto chi faceva le previsioni per le noccioline della Nutella guadagnava sull'ordine del milione di euro l'anno, si parla di 15-20 anni fa, quindi sono lavori che hanno un certo interesse.

> [!question] Da verificare: la trascrizione riporta "Pensa per fare le previsioni per la Ferrari non è... non c'è nemmeno il tedesco per farlo" e "trent'anni da quando mi dicevano queste cifre"; il passaggio sulla Ferrari e l'epoca delle cifre (15-20 o trent'anni fa) non sono leggibili.

## Esogeneità ed endogeneità

Vi farò vedere soprattutto la distinzione tra statistica ed econometria: la differenza è la relazione logica tra le variabili, che dal punto di vista puramente tecnico si chiama esogeneità. La formalizzeremo con un indicatore di correlazione tra un qualcosa che non osservo e un qualcosa che osservo. Vi farò vedere come si può capire se un modello è affetto da endogeneità oppure no, e sulla base di questo cercheremo di capire come si può risolvere il problema. Il primo caso di endogeneità è se io metto nel modello troppe poche variabili: tutte le altre variabili che non metto nel modello finiscono nel termine d'errore.

Vuol dire che una variazione di x causa una variazione di y e, di y, il termine d'errore, che chiamo epsilon. La variazione della mia variabile dipendente è una combinazione di due oggetti che io non so misurare separatamente: misuro solo il totale, non so quanto conta il singolo fattore. Come posso risolvere il problema, se capisco che questa imprecisione è data da un modello troppo piccolo? L'idea è di togliere variabili dal termine d'errore utilizzando dei ragionamenti logici, non numerici: non uso una procedura puramente statistica, c'è un problema economico, cerco di capire quali sono le variabili che veramente contano. ==C'è la teoria economica che mi deve guidare nella definizione del modello, non sono i dati.==

## Causalità circolare

Un altro problema si verifica quando la relazione causa-effetto non è chiara. È la x che influenza la y o la y che influenza la x? In questo contesto si può dimostrare che non so più se muovo una variabile muovo l'altra, ma di fatto introduco un riferimento circolare che non mi fa più capire quanto una variazione di x impatta sulla y. Questo mi crea un cortocircuito, una correlazione tra la x e l'errore, e a questo punto la stima dei coefficienti diventa problematica.

## Errore di misura

L'ultimo problema, un po' più sottile, riguarda la qualità dei dati. Se utilizzo dei dati approssimativi, si può dimostrare in maniera molto facile che, anche se il modello è perfetto, questo errore di misura delle osservazioni induce una distorsione nella stima dei parametri. E questa distorsione è tanto più grande quanto è grande l'errore di misura.

Faccio un esempio stupido: l'Istat o qualsiasi agenzia che fa un'indagine sulle preferenze di spesa intervista n mila persone e chiede: nell'ultima settimana quanto hai speso al supermercato? Io non ho una memoria di quanto ho speso esattamente. Se ho speso 200 euro magari me lo ricordo, ma se ho speso 190 mi è più facile ricordare 200, quindi nel foglietto scrivo 200. E tutti più o meno fanno un'approssimazione di questo tipo: anche uno che spende 205 riporta 200. Questo errore di riporto, anche se la spesa media nel campione è corretta, mi induce un livello di rumore nella procedura di stima che a sua volta distorce la stima del parametro.

Non sto parlando di gente che sistematicamente sottoriporta o sovrariporta. Sto dicendo che è un po' imprecisa, perché non si ricorda, magari perché la domanda fa riferimento a qualcosa che è successo abbastanza tempo prima. Una volta, tornando dagli Stati Uniti, all'aeroporto a Venezia c'erano quelli dell'Istat che facevano domande su quanto hai speso nell'ultimo viaggio. Io ero via da sette mesi circa, ho fatto una stima a spanna: avrò speso 10.000 euro, poteva essere 15.000, poteva essere 5.000, non mi ricordo assolutamente, gli ho dato un numero completamente a caso. Chiaro che se uno sta via una settimana più o meno sa quanto ha speso.

> [!question] Da verificare: la trascrizione riporta "se uno sta via una settimana più o meno mi dà di quanto ha speso"; si legge "sa quanto ha speso".

Diverso è il caso delle evasioni fiscali: se faccio un'analisi fiscale, tutti tenderanno a sottostimare o sovrastimare, quindi là ci potrebbe essere una distorsione sistematica. È quasi preferibile avere un campione di quel tipo, perché quella distorsione può essere controllata più facilmente. Qui sto parlando di gente onesta ma un po' imprecisa. Questo potrebbe creare dei grossi problemi, e vi farò vedere con dei dati simulati, quindi controllabili, cosa succede.

## Come si svolgerà il corso

Analizzeremo tutto questo un po' dal punto di vista teorico, perché la formula fa capire meglio che cosa sta succedendo, un po' dal punto di vista empirico, perché vedere effettivamente le conseguenze delle azioni è probabilmente la cosa più utile. L'idea è di fare un po' di teoria senza un'algebra complicata: cercherò di non utilizzare algebra matriciale: tutto quello che mi serve sono algoritmi, derivate, queste cose relativamente semplici. Farò anche una rappresentazione dei sistemi dal punto di vista matriciale, ma solo per far vedere che non c'è nessuna differenza. La matrice è solo una strategia per rendere le formule piccole e compatte, non serve a nulla di più e nulla di meno rispetto a scrivere le cose come sommatorie.

> [!question] Da verificare: la trascrizione riporta "algoritmi, derivate"; forse "logaritmi", le slide non lo stabiliscono.

> [!question] Da verificare: la trascrizione riporta "come sottopo o per meno"; probabilmente "sommatorie", non determinabile con certezza.

Questa riguarda la prima parte, in cui farò una survey del modello di regressione focalizzandomi su quando il modello non va bene. Nella seconda parte analizzeremo i dati in serie storica e cercheremo di capire come i modelli, sempre di regressione, che è la strategia sempre la stessa, cambiano a seconda del tipo di dati che ho a disposizione.

## Dati indipendenti e dati dinamici

Nell'analisi del modello di regressione si fa sempre l'ipotesi che le osservazioni siano pescate in maniera indipendente dalla popolazione: ho un campione di persone, le pesco a caso, tutte le osservazioni sono indipendenti tra di loro. Le unità statistiche che mi danno le informazioni sono indipendenti tra di loro. Se le osservazioni fossero indipendenti, avrei tutti i coefficienti di legame tra le variabili uguali a zero. Il problema è che nei sistemi dinamici, tipici della finanza, dell'economia, delle serie storiche, le variabili hanno una loro inerzia e non sono osservate in maniera indipendente: se il tasso di interesse oggi è il 5%, domani non sarà lo 0% e neanche il 10%, sarà 5% più o meno una piccola variazione. E questo mi crea un problema di stabilità delle traiettorie dei miei dati. ==Il problema è che la statistica funziona bene se i dati sono stabili nel tempo.==

Il motivo è abbastanza intuitivo. Faccio il grafico alla lavagna, ma poi lo vedremo. Supponiamo che i dati abbiano un andamento di questo tipo, il tipico andamento del prezzo di un asset finanziario, per esempio i prezzi giornalieri dello Standard & Poor's. Posso descrivere con degli indicatori sintetici un fenomeno che ha una dinamica di quel tipo? Tecnicamente sì: prendo i prezzi giorno per giorno e ci faccio la media, e qualche software mi dà quel numero. Ma la media è un indicatore di centralità, sarà un punto più o meno qua, una riga orizzontale in mezzo ai dati. È un buon indicatore per rappresentare il comportamento di un fenomeno dinamico di questo tipo? No: va bene per questo intervallo temporale, per puro caso, ma non è un buon indicatore né per questa informazione né per questa informazione.

Se i dati non sono stabili, la statistica descrittiva mi rappresenta caratteristiche di una popolazione troppo eterogenea nel tempo. Faccio una media che prende in considerazione magari i prezzi tipici degli ultimi cinque anni e i prezzi tipici di trent'anni fa: ottengo un numero che non è utile né per descrivere quello che succede oggi né quello che succedeva ieri. Di fatto io sto utilizzando dei dati che provengono da popolazioni statistiche diverse, tutti con media diversa. Se mischio insieme tutte queste informazioni, la mia stima è una stima di medie. Faccio un esempio più semplice. Supponiamo di avere una popolazione in cui il 50% è alto due metri e il 50% è alto un metro. Ne pesco a caso, quindi nel campione avrò metà della popolazione molto alta e metà molto bassa: due medie che rappresentano la popolazione, la distribuzione condizionale, i bassi e gli alti, un metro e due metri.

Se calcolo una media aritmetica sulla base di quel campione, ottengo come stima più o meno un metro e mezzo, che non è un indicatore utile né per il gruppo dei bassi né per il gruppo degli alti. Il problema della stabilità della serie è esattamente questo: tutte le statistiche descrittive, tutti i parametri che posso stimare dal modello, se i dati non sono sufficientemente regolari non hanno nessun significato logico. Numericamente posso calcolare tutto, ma dal punto di vista operativo i numeri non hanno nessun significato. ==Una delle ipotesi che bisognerà fare quando si utilizzano i dati in serie storica è richiedere che la serie sia stabile nel tempo, quantomeno che abbia una media comune.==

## Stabilizzare le serie: rendimenti e modelli ARCH e GARCH

Per fortuna esistono delle trasformazioni delle serie storiche originali, che sono uno a uno, quindi non mi fanno perdere informazione, e che tendono a stabilizzare la serie. Anziché usare i prezzi, uso le variazioni di prezzo, che sono i rendimenti. I rendimenti tipicamente hanno una media stabile, tipicamente zero, quello che si osserva nei dati, mentre la variabilità cambia nel tempo, ma quello si può gestire in maniera un po' più naturale. Sono i modelli che si usano in finanza, la classe ARCH o GARCH, che ha fatto vincere il premio Nobel nel 2000 e qualcosa. Il problema è capire perché la varianza, che è un indicatore di rischio di un investimento, cambia nel tempo e in che modo cambia: questo mi permette di costruire misure di rischio utili dal punto di vista operativo. È quello che si fa nei corsi di risk management.

Quando i dati sono osservati nel tempo non sono indipendenti. Devo controllare che la dipendenza sia sotto controllo. Se ho una dipendenza che mi crea una componente di trend, la statistica descrittiva standard non funziona più. Posso dimostrare anche analiticamente che il teorema del limite centrale e la legge dei grandi numeri non valgono più, tutte le proprietà statistiche degli indicatori vanno a farsi benedire. Ma il problema è sostanzialmente logico: mischio dati che non sono coerenti tra di loro, e ottengo una mistura di indicatori di centralità, un misto di cose che non hanno interpretazione.

## Regressione spuria e cointegrazione

Quando lavoreremo con le serie storiche dovremo stare attenti a questo fenomeno, perché se non lo consideriamo, quello che otterremo, erroneamente, anche da analisi fatte con modelli semplici e facilmente controllabili, è che sembrerà che qualsiasi cosa non statisticamente significativa poi automaticamente diventa...

> [!question] Da verificare: la trascrizione riporta "sembrerà che qualsiasi cosa non statisticamente significativa poi automaticamente diventa..."; la frase resta interrotta.

Se faccio un test classico, mi assegnerà un p-value estremamente piccolo, che è il contrario di quello che mi aspetto. Si chiama regressione spuria. Prendo due cose che sono per costruzione indipendenti, ma se faccio un test di significatività del coefficiente che lega le due cose viene sempre diverso da zero. Il motivo è che il test lo calcolo sulla base di una distribuzione normale, ma la distribuzione degli stimatori dei parametri, quando i dati hanno quelle caratteristiche, non è più normale. Il software non lo sa e mi spara fuori un numero che non ha senso. In generale, quando avete dati non stabili non si può facilmente utilizzare la regressione, a meno che non stabilizziate i dati prima. C'è un'eccezione che si chiama cointegrazione, estremamente importante soprattutto in ambito finanziario ma anche economico: se le caratteristiche di regolarità sono più o meno stabili, allora si può sperare che la relazione tra le variabili sia stabile, che il parametro che lega le variabili sia identificabile.

## Schema del corso

La prima parte del corso riguarda cosa non guardare in un output di un modello di regressione, cosa non fare quando i dati sono sostanzialmente indipendenti. Poi cosa cambia quando entro in un contesto di dipendenza e che tipi di modelli posso implementare per sfruttare la irregolarità nel tempo delle serie. È un po' una seccatura dal punto di vista concettuale, ma una volta che so che un sistema dinamico ha una sua inerzia, posso usare l'inerzia sia per fare previsioni, sia per trovare dei modelli migliori, dal punto di vista statistico e dal punto di vista economico. Sono i modelli a correzione di equilibrio, sarà l'ultima cosa che faremo. Più che dirvi cosa fare, sarà più cosa non fare; la parte di interpretazione secondo me è particolarmente importante: capire perché utilizzo un modello, come posso interpretare i risultati di quello specifico modello.

## Materiale, Moodle e Gretl

Tutto il materiale lo potete trovare nella pagina Moodle del corso, Econometria 2026-2027. Ho già fatto l'upload di un po' di materiale, tipicamente prima delle lezioni cerco di aggiornarlo. A parte i primi due set di slide che utilizzeremo, gli altri sono la versione dell'anno prima. Un po' li cambio, ma non più di tanto. Sappiate che tutto il materiale prima della lezione potete trovarlo là, magari nella versione penultima, però comunque poi la aggiorno regolarmente. Qua dentro trovate sia i lucidi sia i dataset, perché una parte del corso sarà anche applicata. Cercherò di farvi vedere soprattutto nella parte delle esercitazioni come si possono analizzare i dati e scovare i problemi di un modello, che certe volte non sono facili da scovare, e lo farete più con il dottor Peruzzi, che farà le esercitazioni.

> [!question] Da verificare: il docente indica "dottor Peruzzi" per le esercitazioni; la slide 3 riporta "Marco Bidoia". Si riporta il nome detto dal docente.

Il software che utilizzerò è Gretl *(slide 3)*. L'ho scelto semplicemente perché è molto semplice da utilizzare, quindi vi potete concentrare sulla parte econometrica più che sul comando. È immediato ed è gratuito, potete scaricarlo su qualsiasi piattaforma. In più, il libro di testo mette a disposizione tutti i dati degli esempi, scaricabili anche in formato Excel: se volete replicare gli esercizi del libro per fare pratica, potete farlo. Gretl va a tasti; c'è anche un linguaggio in background, che però non è necessariamente la cosa più importante. Alla fine il problema in econometria non è stimare il modello, è capire cosa state facendo, capire se il modello che state stimando va bene oppure va male. Questa è la teoria: almeno mi dà una casistica da controllare quando mi approccio all'analisi empirica di un modello economico.

> [!question] Da verificare: la trascrizione riporta "Questa è la teoria, mi dice alla fine questo, ma almeno mi dà una casistica da controllare quando faccio questo tutorial"; l'inizio della frase non è leggibile.

> [!tip] Esame: ci sono anche degli esami vecchi sulla pagina Moodle. Prima dell'esame finale faremo delle esercitazioni stile esame, dei mock exam: vi do il testo un po' prima e poi, con me, con il dottor Peruzzi o con il tutor, farete esercizi in questa direzione.

Quindi tutto il materiale ce l'avete qua. Ci sono anche degli esami vecchi, e prima dell'esame finale faremo delle esercitazioni stile esame, tipo mock exam, in cui magari vi do il testo un po' prima e poi o con me o con il dottor Peruzzi o con il tutor farete esercizi in questa direzione. Anche questa lezione la potete recuperare. Vi incoraggio a venire a ricevimento. Di solito non c'è molta gente, però serve per risolvere i problemi prima dell'esame: ==spiegare dove sono gli errori è troppo tardi, ormai il compito è fatto.== Quindi cerchiamo di risolvere i problemi prima, in modo che poi arrivati all'esame tranquilli passate con voti alti e siamo tutti contenti.

> [!question] Da verificare: la trascrizione riporta "per mettervi di risolvere i problemi pre-esame non posto. Il coraggio di un esame, spiegare dove sono gli errori, è troppo tardi"; non si legge a quale momento si riferisca.

## Iscrizione a Moodle, ricevimento ed esame

Quando avete l'esame nel piano di studio, siete iscritti automaticamente alla pagina Moodle del corso, oppure dovete iscrivervi manualmente? Dovete iscrivervi. Vi consiglio di iscrivervi, se non l'avete già fatto, anche perché se devo mandarvi un'informazione, una lezione che cambia d'orario, un materiale extra, vi posso contattare tutti in blocco. Scrivetemi pure email se non vi va bene l'orario di ricevimento ufficiale: se sono disponibile possiamo trovare un altro momento, anche online. ==L'unica cosa che non si può fare online è la visione dell'esame. Chi vuole vedere l'esame esposto dovrà venire.== Non ho tempo di fare la scansione di cento compiti.

> [!question] Da verificare: la trascrizione riporta "Ok, quindi a parte quello, però ricevimenti standard non possiamo fare"; non si capisce se il docente escluda o ammetta i ricevimenti standard online.

Per chi ha diritto, le registrazioni delle lezioni verranno scaricabili da questa pagina, se funziona.

> [!tip] Esame: l'esame è scritto. Potete guardare gli esempi dei compiti vecchi: tipicamente è organizzato in una decina di domande, ma il numero non è fissato, e vi chiedo sostanzialmente di interpretare dei risultati, non di fare le stime.

Poi l'esame è scritto: potete guardare gli esempi dei compiti vecchi, ma tipicamente l'esame è organizzato in una decina di domande, poi il numero di domande non è fissato, e sostanzialmente vi chiedo di interpretare dei risultati, quindi non vi chiederò di fare le stime. La parte di spiegarmi come si fa la stima con un software o con un altro software sarà più per voi, se volete diventare più operativi, ma per l'esame non è particolarmente necessario. Vi consiglio comunque di partecipare alle lezioni più empiriche, perché dentro ci sono anche delle spiegazioni su come interpretare i modelli. La prima lezione, probabilmente non oggi ma la settimana prossima, è cosa succede quando riscalate le variabili con trasformazioni tipo logaritmo, come si interpretano gli effetti marginali quando le variabili sono in una scala diversa, approssimata o esatta, e come si diagnostica un problema patologico del modello, la quasi collinearità: la collinearità esatta è facile, con due si pianta, ma la quasi collinearità non è così facile. Questi casi sono trattati empiricamente, ma servono anche nel compito. Approfittate della parte empirica perché è più intuitivo, per esempio come utilizzare il variation factor, che serve per diagnosticare la quasi collinearità, normalmente un problema perché, se non me ne accorgo, penso che il modello mi dia dei risultati che non sono corretti. Lo vedrete.

> [!question] Da verificare: la trascrizione riporta "la collinearità esatta è facile, con due si pianta"; che cosa si pianti non è determinabile.

> [!question] Da verificare: la trascrizione riporta "variation factor"; probabilmente il variance inflation factor, ma nelle slide non compare.

> [!question] Da verificare: la trascrizione riporta "se non me ne accorgo, penso che il modello mi dia dei risultati che non sono corretti"; dal contesto il senso sembra l'opposto (li penso corretti e non lo sono), si riporta come detto.

Le lezioni empiriche con il dottor Peruzzi sono importanti perché, assieme alla parte meccanica, c'è una componente di interpretazione legata a quello che facciamo dal punto di vista teorico: l'idea è di trovare un legame tra teoria e pratica. Il compito sarà fatto di domande in cui vi chiedo di interpretare dei risultati, capire se il modello ha un problema o non ce l'ha, analizzando sia grafici sia tabelle. Soprattutto sulla serie storica, un'altra cosa è capire se un modello è corretto dal punto di vista metodologico, come interpretare i risultati dinamici e statici di un modello dinamico e avanti. Ci sono già degli esempi e prima dell'esame vedremo esercizi di questo tipo.

## Feedback e libro di testo

Potete interrompermi in qualsiasi momento, anzi mi fa piacere avere dei feedback sul momento. Il corso è per voi, non è per me. Una delle cose che odio di più in assoluto è correggere compiti, quindi se passaste tutti con voti altissimi al primo appello sarei la persona più felice del mondo.

> [!question] Da verificare: la trascrizione riporta "doppi altissimi, che mi appello"; il senso probabile è "voti altissimi al primo appello".

Se nessuno mi dà feedback, io vado avanti per la mia strada e magari c'è un mismatch tra me e voi, e se mi accorgo di un problema alle ultime tre lezioni c'è poco che posso fare. Non sono vendicativo, potete parlarmi apertamente. Se può essere utile modificare un po' il programma sulla base di quello che vi interessa, si può fare, se c'è tempo, più che volentieri. Interrompetemi, oppure a fine lezione o a ricevimento, come volete.

L'acquisto del libro è obbligatorio? No, non vi posso obbligare ad acquistarlo. Il libro però è un supporto piuttosto utile, perché io lo seguo abbastanza ed è molto discorsivo: c'è la parte tecnica ma ci sono un sacco di esempi che portano a capire la tecnica, soprattutto nei capitoli che riguardano le serie storiche e la regressione, poi ci sono argomenti in più che non c'è tempo di trattare *(slide 4)*. C'è in biblioteca. Consiglierei di leggerlo, perché è utile per capire i dettagli che non faccio in tempo a raccontare. Non vincolatevi solo ai lucidi che metto online, perché quello è uno schema per voi per prendere appunti, o per me per avere una scaletta, che mi sono ordinato in trent'anni più o meno che insegno. Però in generale il libro dà di più, soprattutto quel libro là in particolare ha un sacco di esempi che descrivono abbastanza bene il perché delle cose.

## Materiale di statistica di base

Questo è il primo set di lucidi di introduzione al corso. Ho anche messo degli appunti che avevo utilizzato qualche anno fa per un corso di statistica di base, per richiamare i concetti essenziali che mi servono per dimostrare le cose. Quando avete capito come funzionano le varianze, le medie, il resto è abbastanza semplice. Se volete fare dei richiami di statistica per fissare la notazione, per esempio perché per calcolare una media uso E, è tutto là, all'inizio della pagina Moodle.

## Che cos'è l'econometria

L'econometria, ve l'ho già detto, ha tre scopi, ma in generale si può racchiudere come un'analisi quantitativa di modelli economici *(slide 5)*. Non esiste neanche una definizione chiara, io non l'ho ancora capita alla mia età, però c'è abbastanza consenso su questi tre aspetti. Uno è la misura delle relazioni causa-effetto tra variabili. Un altro è fare le previsioni, ma quello è più statistica che econometria. Però siamo una famiglia accogliente, quindi prendiamo dentro anche gli statistici.

Un'altra cosa che mi piace particolarmente è usare metodologie anche avanzate per valutare delle teorie economiche. Ho un modello economico astratto, per esempio il modello CAPM. Il modello CAPM non è un'equazione: sono due pagine di algebra che alla fine mi danno l'equazione che dice che gli extra rendimenti di un investimento sono proporzionali agli extra rendimenti di un portafoglio di mercato, qualsiasi esso sia. Per arrivare a quel modello ho un sacco di ipotesi da fare, tipo che il mercato dei capitali sia in equilibrio, che il mercato dei tassi di interesse sia in equilibrio, la gente costruisce dei portafogli utilizzando l'algoritmo di Markowitz, ipotizzando che funzioni. Con tutta quella roba, uno fa i conti e si accorge che esiste quella relazione.

## Validare un modello economico: il CAPM

Il mio punto è: quella relazione è credibile oppure no? I dati supportano questa evidenza oppure no? Come posso validare il modello? Se il modello fosse vero, un rendimento in media non dovrebbe garantire un premio extra per il rischio, il che dal punto di vista operativo si quantifica nel fatto che il mio modello di regressione non può avere l'intercetta. Dimentichiamoci tutto il pregresso che mi porta all'equazione finale. Costruiamo una regressione semplice in cui metto l'intercetta, valuto se l'intercetta è uguale a zero o diversa da zero, e quello potrebbe essere un possibile test. Non è detto che poi funzioni, però potrebbe essere un'idea: utilizzare una metodologia econometrica per validare un modello economico, perché se un modello economico non è coerente con quello che osservo ha pochissima utilità.

Ma se il modello economico non passa il test econometrico, cosa devo fare? Non è che posso aggiungere nel modello un'intercetta e via così, perché aggiungere un'intercetta vuol dire che devo cambiare tutte le equazioni, tutte le ipotesi che ho fatto prima, le due pagine precedenti. Devo rispecificare il modello economico in modo che il modello statistico poi accetti quelle variazioni. La validazione di un modello è un'altra cosa importante: ho una teoria, ho dei dati, voglio vedere se la teoria è coerente nello spiegare i dati. Questa secondo me è una parte particolarmente importante, è la mia preferita, se devo essere onesto.

## Relazioni causa-effetto e criteri di causalità

La prima parte del corso sarà sulle relazioni causa-effetto. Prima di tutto vorrei spiegare che cosa sono e qual è il pericolo nell'utilizzare i metodi statistici senza pensare a monte, prima di cominciare l'analisi empirica, quali sono le potenziali relazioni logiche tra variabili. Dal punto di vista grafico, una relazione causale si rappresenta con un grafo: ho due variabili, la x e la y, ed è una relazione asimmetrica, perché la x ha un impatto sulla y ma non viceversa. La x è un driver per la y. Il mio problema è tipicamente capire se x è una causa per y oppure no *(slide 6)*.

Se è una relazione causa-effetto, devono valere sostanzialmente tre criteri. Il primo è un criterio puramente statistico, quindi mi rimangio quello che vi ho detto prima, che la parte statistica è diversa dalla parte economica: in realtà è l'inizio. Per vedere se c'è una relazione causale tra due variabili ho bisogno di capire se c'è almeno una relazione statistica. Se non c'è, quand'anche ci fosse una relazione causale, una variazione della x non avrà impatto sulla y e cade l'interesse per il problema. Se le variabili sono quantitative, ci deve essere una correlazione statisticamente significativa tra x e y.

Il problema è che la correlazione è una relazione simmetrica tra le variabili, mentre nel grafo sto definendo che x ha un impatto su y ma non viceversa. La correlazione tra x e y o tra y e x è lo stesso numero, quindi una correlazione non mi dice nulla sul nesso causale, mi dice solo che c'è un legame di qualche natura, che non è necessariamente un legame logico. Per definire una relazione causale bisogna aggiungere l'ipotesi che ci sia un legame logico tra le variabili, non solo statistico: una variabile che da un punto di vista logico anticipi l'altra, non solo dal punto di vista temporale. Ho bisogno che ci sia una storia che mi spieghi perché c'è un legame statistico. E quella storia deve essere unica.

> [!question] Da verificare: la trascrizione riporta "So più storie che coerentemente mi descrivono quella forma di dipendenza statistica, lo troverò migliore"; la frase non è leggibile, il senso probabile è che con più storie coerenti il legame non è stabilito.

Vi farò degli esempi per legare questo ragionamento astratto alla pratica economica, magari più la prossima lezione, quando guardiamo un po' di dati. In generale non mi basta sapere che ci sia un legame logico, ho bisogno che quel legame logico sia unico. ==La cosa importante da capire è che il legame statistico non è sufficiente.==

## Correlazioni spurie: gli esempi del sito

Per farvi capire che non è sufficiente, vi propongo una pagina web che potete consultare online *(slide 13)*. È di uno statistico buontempone che ha chiesto a un programmino di cercare le variabili più correlate possibili tra di loro: ha un database di, non so, 10.000 variabili, e il programmino trova le coppie più collegate, senza pensare a che variabili sta considerando.

Il primo esempio: la serie nera è quanta gente ha guardato la serie TV Big Bang Theory, la serie rossa è il numero di ricerche su Google che cominciano con "how to make". Da un punto di vista logico non c'è un legame, però se guardate il grafico sono variabili estremamente vicine una all'altra. Paradossalmente, se so che nel 2016 Big Bang Theory ha un certo livello di visibilità, posso usare questa informazione per prevedere il livello dell'altra variabile, perché c'è una correlazione forte. Da un punto di vista puramente predittivo potrei usarle per prevedere una o l'altra. Il punto è che questa relazione non ha una spiegazione logica. Però l'R quadro della relazione è 96,5%. ==Questo 96,5% mi spiega solo il legame statistico==, non mi spiega null'altro, ed è un numero molto fuorviante, perché mi dice solo che le due serie si muovono insieme, non mi dice perché. Se guardo l'R quadro come indicatore di bontà del modello, mi dice che i dati sono approssimati bene, non che il modello è corretto dal punto di vista logico, che è quello che sto cercando.

Sul sito ci sono in alcuni casi delle spiegazioni fatte tramite intelligenza artificiale del perché c'è una correlazione così alta.

Un altro dataset: la serie nera mi dice come sono andate le partite di lacrosse, lo sport molto popolare negli Stati Uniti, e la linea rossa sono i biglietti venduti al cinema.

> [!question] Da verificare: la trascrizione riporta "la cross"; si interpreta come lacrosse, ma le slide non lo confermano.

Non c'è nessun legame sostanziale tra le serie, ma anche qua c'è un livello di correlazione, intorno al 74%.

> [!question] Da verificare: la trascrizione riporta "il 74% o più del 50%"; il valore non è del tutto leggibile.

Se chiedete all'intelligenza artificiale di spiegare questa associazione, qualcosa viene fuori, e una storia uno la può anche trovare, il punto è che non è una storia che necessariamente ha senso. Dateci un'occhiata, per vedere che il legame statistico non ha niente a che fare con il legame logico. È solo uno dei prerequisiti, è solo il primo pezzo.

Cosa vuol dire? Se l'R quadro del modello di regressione è grande, non vuol dire che il modello vada bene.

> [!question] Da verificare: la trascrizione riporta "se il primo modello di regressione, quando è grande"; dal seguito ("i modelli buoni non hanno R quadro così grande") si legge "R quadro".

Anzi, tipicamente i modelli buoni non hanno R quadro molto grande. Un R quadro troppo grande porta anche dei problemi statistici non banali, i problemi di collinearità. Qua avete variabili molto legate dal punto di vista statistico, ma non c'è nessun motivo logico che le lega: combinarle non mi dà nessuna spiegazione del perché una delle variabili si muova, e quindi nessuna capacità di fare analisi di scenario.

Sono anche variabili abbastanza inutili, se volete, ma immaginate di trovare una correlazione tra due variabili economiche che non c'entrano niente una con l'altra e di voler fare un'analisi di scenario come quelle che vi diceva il professore prima. Qualsiasi cosa che trovate è completamente casuale, non è qualcosa che potete replicare, perché non c'è un legame.

## Nessun modello è definitivo, ma si lavora con regole precise

Per quanto io mi sforzi di trovare delle relazioni causali, alla fine non sarò quasi mai in grado di avere una risposta definitiva, perché posso anche spiegare logicamente il legame statistico tra due variabili, ma è quasi impossibile escludere tutte le altre spiegazioni che dal punto di vista logico stanno in piedi. Però nulla è perduto. La distinzione causale mi dà una chiave di lettura su come devo lavorare, una regola su come devo lavorare.

> [!question] Da verificare: la trascrizione riporta "relazioni casuali" e "distinzione casuale"; la slide 11 tratta lo stesso passaggio come "relazione causale" e si adotta "causale".

Ogni volta che costruisco un modello devo capire perché lo sto facendo, perché sto selezionando certi tipi di variabili. Poi cercherò di vedere se il modello descrive le mie aspettative, se i coefficienti hanno il segno corretto, perché se il segno è sbagliato può essere un indicatore che non sto stimando le correlazioni che mi aspetto in maniera corretta, e lo vedremo formalmente.

Lavorare in modo logicamente coerente mi permette di far andare avanti lo studio su un certo fenomeno. Magari il mio modello non sarà quello definitivo, ma contribuirà al lavoro degli altri, che proveranno altri modelli e valuteranno se il loro è migliore del mio, e si andrà avanti finché non si troverà un equilibrio in cui ci sarà un consenso: abbiamo provato 10.000 modelli su un fenomeno specifico, siamo convinti che la relazione causale è esattamente questa, perché abbiamo escluso tutti gli altri.

La speranza di trovare un modello perfetto, che rispecchi quelle tre caratteristiche, è troppo ambiziosa. Soprattutto la terza parte richiederebbe troppo tempo. Quello che secondo me è importante è capire che ==la relazione statistica non è abbastanza==, ogni volta devo ragionare in termini di legame logico tra variabili, e una volta che ho pensato a un legame logico devo vedere se resiste a spiegazioni alternative logicamente ben strutturate. Un po' alla volta, nel tempo, ci si fa un'idea. Quello che si sta facendo non sarà definitivo, ma deve essere fatto con regole sostanzialmente precise. Provare dei modelli buttando dentro dati, sperando di trovare qualcosa che ci piace in termini di segni, non è sufficiente. In generale è difficilissimo trovare delle relazioni causali, ma con un po' di pazienza qualcosa si trova.

## Fumo e malattie dei polmoni

Qua non ho i dati reali, ma vi faccio una sintesi di quello che è stato trovato nella letteratura epidemiologica negli ultimi centinaia d'anni: l'associazione tra fumo e malattie gravi ai polmoni *(slide 12)*. La correlazione c'è. È sufficiente per dire che ci sia una relazione causa-effetto? No. Però negli anni sono state testate varie ipotesi, per decine di anni, non sto parlando di settimane. Un po' alla volta hanno trovato che il legame è logico, c'è un motivo biologico per cui il consumo di sigarette può aumentare l'incidenza di certe malattie. Hanno trovato dei meccanismi. È sufficiente? No, potrebbero esserci altri meccanismi non ancora visti. Il punto è che questo screening tra varie opzioni è stato raffinato e adesso c'è più o meno l'idea che ci sia una relazione causa-effetto. È definitiva? Probabilmente sì, però se qualche biologo trovasse un'alternativa più convincente, bisognerebbe ripensare a tutto. È una procedura che va avanti in maniera progressiva, quindi trovare un modello che risolva tutti i problemi in maniera definitiva è praticamente impossibile.

L'importante però è che ogni volta che proponete un modello, che lavorate su un modello, dovete avere una certa convinzione che ==quello che state facendo non deve essere un tentativo, ma deve essere un tentativo fatto con un background==. Quindi prima di affrontare un problema economico, prima di arrivare ai dati, dovete cercare di capire quali sono i potenziali driver che vi possono interessare, dopodiché li inserite nel modello. Non devo fare il contrario, cioè mettere tutta la roba dentro il modello e poi selezionare le variabili finché non trovo qualcosa. La teoria mi deve definire i legami logici a priori, e non posso farmi raccontare dalla correlazione.

> [!question] Da verificare: la trascrizione riporta "Ho fatto il contrario, che è tutta la roba dentro modello"; si riporta in forma negativa, coerente con il contesto.

## Boy scout e criminalità: causalità inversa

Per farvi capire un altro tipo di problematica: questi sono dati inventati che ho trovato su un libro di statistica e che mi fanno capire da dove nascono le correlazioni spurie tra variabili *(slide 9)*. È una tabella a doppia entrata in cui vengono osservati dei ragazzini: alcuni hanno fatto il boy scout da piccoli e poi, dopo anni, è stato guardato il loro record criminale. I dati non sono reali, potrebbero esserlo, li ho presi da un libro di testo che ho utilizzato per un corso di statistica anni fa.

La variabile qua è chi ha fatto il boy scout, sì o no, e qua chi ha avuto problemi con la giustizia. Quello che osservo è che tra il gruppo di persone che ha fatto il boy scout c'è un'incidenza più bassa rispetto a quelli che hanno avuto problemi con la giustizia. Quindi sembrerebbe che ci sia una relazione negativa tra l'essere boy scout ed essere un criminale. La tabella è abbastanza chiara: questa è una percentuale bassa, questa è una percentuale alta, questa è alta, questa è alta. Dal punto di vista logico mi chiedo: questa correlazione è supportata da un'intuizione logica? Uno che ha fatto il boy scout magari viene insegnato a comportarsi bene. Ti danno delle regole, dei principi, ti aiutano a capire che aiutare un'anziana ad attraversare la strada è una cosa positiva. Chi ha fatto il boy scout ha avuto degli input diversi, è una persona migliore, tra virgolette, e ha una probabilità di essere arrestato più bassa. È una relazione del tipo boy scout verso delinquency *(slide 10)*.

Un'altra persona potrebbe dirmi: se una persona è interamente cattiva, probabilmente non si sarebbe mai iscritta ai boy scout. Se sono avverso a rispettare le regole, non vado in un posto dove mi riempiono di regole. E quindi potrei avere che il fatto che sono una persona avversa alle regole mi fa sì che io non mi iscriva ai boy scout, quindi la correlazione può anche essere spiegata dall'altra direzione. ==Il legame statistico, che è simmetrico, non mi dice nulla su qual è la direzionalità tra le variabili.== Questa si chiama reverse causality e crea problemi nello stimare una relazione causa-effetto. Prima ancora di arrivare al modello, devo ragionare su quali sono i potenziali legami logici tra le variabili.

## Prossima lezione

Oggi era una chiacchierata. Dalla prossima volta, che è giovedì, ragioneremo su come definire un modello statistico che cerchi di descrivere una relazione causale, e su come capire quando il modello statistico supporta o non supporta una relazione di questo genere.
