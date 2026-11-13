---
corso: Econometria
data: 2026-11-10
fonte: Materiali/audio/econometria/econometria_2026-11-10.txt
tipo: appunti-sintetici
tags: [appunti-sintetici, econometria]
revisione: sintesi a punti della nota fedele della stessa lezione
---

# Introduzione al corso: causalità e correlazioni spurie

## Obiettivo del corso: interpretare, non calcolare

- L'idea è di farlo più intuitivo che tecnico; di solito una parte della classe ha già fatto econometria, ma solo dal punto di vista statistico.

> [!question] Da verificare: la trascrizione riporta "scuota percento della classe"; la percentuale non è leggibile.

- Il corso si concentra sull'interpretazione economica ed è di fatto cosa non fare, perché l'econometria viene presentata come disciplina tecnica ma è una cosa ibrida.
- La distinzione tra econometria e statistica c'è, per via di un'ipotesi aggiuntiva con implicazione economica importante: l'ipotesi di esogeneità.
- Se costruisco il modello in modo non corretto, gli indicatori sono stimati in maniera sistematicamente distorta: stimo il parametro più una costante che non so cos'è, non l'effetto della politica.
- Più osservazioni ho, più sono preciso nello stimare lo sbaglio.
- ==la scelta del modello, la scelta delle variabili è la cosa più importante, più che la metodologia per fare i conti veri e propri==.
- La scelta delle variabili permette di escludere il problema dell'endogeneità, che è il problema tecnico, economico.

## Relazioni logiche e non quantitative

- Mi interessano relazioni logiche tra variabili, non relazioni quantitative: non conta che il modello si approssimi bene ai dati.
- ==gli indicatori tipo R quadro sono la misura peggiore per valutare il modello. Non dovete proprio utilizzarli==, perché misurano solo una correlazione, e le correlazioni raccontano spesso relazioni spurie.

> [!question] Da verificare: la trascrizione riporta "la misuratura peggiore"; si legge "la misura peggiore".

- Se si chiede a ChatGPT perché c'è una correlazione del 95% tra due variabili, qualcosa tira fuori, che abbia senso o no.
- Esempio: per un picco in una serie storica costruita con colleghi di Bologna, l'IA ha risposto "la rivoluzione industriale", avvenuta 100 anni prima o dopo, quindi risposta sbagliata.

> [!question] Da verificare: la trascrizione riporta "Il fatto è che la correlazione allignment del fenomeno mi è stato spiegato in maniera non corretta"; la frase non è leggibile per intero.

- La consapevolezza di cosa non fare è più importante; l'IA può affinare l'intuizione, però ==il controllo, come diceva la professoressa, dovete avercelo voi==.

## I tre tipi di problema e il termine d'errore

- Le cause di problemi sono tipicamente di tre tipi; il primo è un modello sbagliato con troppe poche informazioni, e ciò che non è spiegato può avere un effetto sistematico sulla relazione che mi interessa.
- Servono la variabile dipendente y e il driver x; interessa la stima del parametro beta: se beta è positivo, se x aumenta aumenta y, se è negativo viceversa.
- Il modello ha anche il termine d'errore: statisticamente una variabile casuale con media zero, economicamente raccoglie le informazioni che non sono nel modello.
- Se quelle informazioni hanno un effetto sulla x, una variazione di x porta anche una variazione di y e misuro un misto di cose; la politica dipende anche dall'errore, che non osservo, e non valuto più cosa fa il modello.

> [!question] Da verificare: nel passaggio "dipende anche da Y, ma Y non lo osservo" il docente dice "Y" dove dal contesto sembra intendere l'errore; si riporta come detto.

## Previsione e comprensione dei driver

- Non è un problema se lo scopo è la previsione: se la x assume questo livello, la y assumerà questo livello.
- Esempio Nutella: per la catena di produzione basta sapere che servono 7 tonnellate di noccioline in un certo momento dell'anno, come con una scatola nera; per capire perché la gente compra la Nutella (gusto, ricetta, packaging) serve la relazione logica.
- Lo scopo del corso è soprattutto la seconda parte, capire i driver; la previsione con un modellino banale è quasi automatica.
- Chi faceva le previsioni per le noccioline guadagnava sull'ordine del milione di euro l'anno, 15-20 anni fa.

> [!question] Da verificare: la trascrizione riporta "Pensa per fare le previsioni per la Ferrari non è... non c'è nemmeno il tedesco per farlo" e "trent'anni da quando mi dicevano queste cifre"; il passaggio sulla Ferrari e l'epoca delle cifre (15-20 o trent'anni fa) non sono leggibili.

## Esogeneità ed endogeneità

- La differenza tra statistica ed econometria è la relazione logica tra le variabili, tecnicamente esogeneità, formalizzata con un indicatore di correlazione tra un qualcosa che non osservo e un qualcosa che osservo.
- Vedremo come capire se un modello è affetto da endogeneità e come risolverlo.
- Primo caso: troppe poche variabili nel modello, e le altre finiscono nel termine d'errore epsilon.
- La variazione della variabile dipendente è una combinazione di due oggetti che non so misurare separatamente: misuro solo il totale.
- Si risolve togliendo variabili dal termine d'errore con ragionamenti logici, non numerici: cerco di capire quali variabili contano veramente.
- ==C'è la teoria economica che mi deve guidare nella definizione del modello, non sono i dati.==

## Causalità circolare

- Altro problema: non è chiaro se la x influenza la y o viceversa; introduco un riferimento circolare e non capisco quanto una variazione di x impatta sulla y.
- Questo crea una correlazione tra la x e l'errore, e la stima dei coefficienti diventa problematica.

## Errore di misura

- Ultimo problema, più sottile: dati approssimativi inducono una distorsione nella stima dei parametri anche se il modello è perfetto, tanto più grande quanto è grande l'errore di misura.
- Esempio Istat: si chiede quanto si è speso al supermercato nell'ultima settimana; chi ha speso 190 o 205 riporta 200. Anche se la spesa media nel campione è corretta, c'è rumore che distorce la stima del parametro.
- Non si parla di gente che sistematicamente sottoriporta o sovrariporta, ma di gente imprecisa perché non ricorda.
- Esempio dell'aeroporto di Venezia: dopo sette mesi negli Stati Uniti ha detto circa 10.000 euro, poteva essere 15.000 o 5.000, un numero a caso; per una settimana di viaggio si sa quanto si è speso.

> [!question] Da verificare: la trascrizione riporta "se uno sta via una settimana più o meno mi dà di quanto ha speso"; si legge "sa quanto ha speso".

- Diverso il caso delle evasioni fiscali: lì c'è una distorsione sistematica, che si controlla più facilmente.
- Qui si parla di gente onesta ma imprecisa; si vedrà con dati simulati, quindi controllabili.

## Come si svolgerà il corso

- Un po' di teoria, perché la formula fa capire, e un po' di empirica, perché vedere le conseguenze è utile, senza algebra complicata e senza algebra matriciale.
- Serviranno algoritmi, derivate; la rappresentazione matriciale sarà solo per far vedere che non cambia nulla: la matrice rende le formule piccole e compatte, come le sommatorie.

> [!question] Da verificare: la trascrizione riporta "algoritmi, derivate"; forse "logaritmi", le slide non lo stabiliscono.

> [!question] Da verificare: la trascrizione riporta "come sottopo o per meno"; probabilmente "sommatorie", non determinabile con certezza.

- Prima parte: una survey del modello di regressione, focalizzata su quando non va bene.
- Seconda parte: dati in serie storica, in cui i modelli di regressione, sempre la stessa strategia, cambiano a seconda del tipo di dati.

## Dati indipendenti e dati dinamici

- Nel modello di regressione si assume che le osservazioni siano pescate in maniera indipendente dalla popolazione.
- Nei sistemi dinamici (finanza, economia, serie storiche) le variabili hanno inerzia: se il tasso di interesse oggi è il 5%, domani non sarà lo 0% né il 10%, ma 5% più o meno una piccola variazione. Questo crea un problema di stabilità delle traiettorie.
- ==Il problema è che la statistica funziona bene se i dati sono stabili nel tempo.==
- Esempio dei prezzi giornalieri dello Standard & Poor's: la media è un indicatore di centralità che va bene per un intervallo solo per caso, non per gli altri.
- Se i dati non sono stabili, la statistica descrittiva rappresenta una popolazione troppo eterogenea nel tempo, con medie diverse.
- Esempio: popolazione con 50% alto due metri e 50% alto un metro; la media è un metro e mezzo, utile né per i bassi né per gli alti.
- Numericamente posso calcolare tutto, ma senza regolarità i numeri non hanno significato logico.
- ==Una delle ipotesi che bisognerà fare quando si utilizzano i dati in serie storica è richiedere che la serie sia stabile nel tempo, quantomeno che abbia una media comune.==

## Stabilizzare le serie: rendimenti e modelli ARCH e GARCH

- Esistono trasformazioni uno a uno, che non fanno perdere informazione: anziché i prezzi si usano le variazioni di prezzo, cioè i rendimenti, con media stabile, tipicamente zero, mentre la variabilità cambia nel tempo.
- I modelli della classe ARCH o GARCH, che ha fatto vincere il premio Nobel nel 2000 e qualcosa, studiano come cambia la varianza, indicatore di rischio, e servono per misure di rischio operative (corsi di risk management).
- I dati osservati nel tempo non sono indipendenti; con una componente di trend la statistica descrittiva standard non funziona più.
- Il teorema del limite centrale e la legge dei grandi numeri non valgono più, ma il problema è logico: mischio dati non coerenti e ottengo una mistura di indicatori di centralità senza interpretazione.

## Regressione spuria e cointegrazione

- Senza attenzione a questo fenomeno, anche con modelli semplici sembrerà che qualsiasi cosa non statisticamente significativa poi automaticamente diventa...

> [!question] Da verificare: la trascrizione riporta "sembrerà che qualsiasi cosa non statisticamente significativa poi automaticamente diventa..."; la frase resta interrotta.

- Un test classico dà un p-value estremamente piccolo, il contrario di quello che mi aspetto: si chiama regressione spuria. Due cose indipendenti per costruzione hanno un coefficiente sempre diverso da zero.
- Il motivo è che il test usa la distribuzione normale, ma la distribuzione degli stimatori con quei dati non è più normale; il software non lo sa.
- Con dati non stabili non si può usare la regressione, a meno di stabilizzarli prima.
- Eccezione: la cointegrazione, importante in ambito finanziario ed economico; se le caratteristiche di regolarità sono più o meno stabili, il parametro che lega le variabili è identificabile.

## Schema del corso

- Prima parte: cosa non guardare in un output di regressione e cosa non fare con dati sostanzialmente indipendenti.
- Poi cosa cambia nel contesto di dipendenza e quali modelli sfruttano l'irregolarità nel tempo; l'inerzia serve per fare previsioni e per trovare modelli migliori.
- Ultima cosa: i modelli a correzione di equilibrio.
- Più che cosa fare, sarà cosa non fare; conta l'interpretazione: perché uso un modello e come interpreto i risultati.

## Materiale, Moodle e Gretl

- Tutto il materiale è sulla pagina Moodle, Econometria 2026-2027, aggiornato prima delle lezioni; a parte i primi due set di slide, gli altri sono la versione dell'anno prima. Ci sono lucidi e dataset.
- Le esercitazioni, in cui si scovano i problemi di un modello, le fa il dottor Peruzzi.

> [!question] Da verificare: il docente indica "dottor Peruzzi" per le esercitazioni; la slide 3 riporta "Marco Bidoia". Si riporta il nome detto dal docente.

- Il software è Gretl *(slide 3)*, scelto perché è semplice, gratuito e su ogni piattaforma, così ci si concentra sulla parte econometrica; il libro di testo dà i dati degli esempi, anche in formato Excel.
- Gretl va a tasti, con un linguaggio in background non essenziale; il problema in econometria non è stimare il modello ma capire se va bene o male.

> [!question] Da verificare: la trascrizione riporta "Questa è la teoria, mi dice alla fine questo, ma almeno mi dà una casistica da controllare quando faccio questo tutorial"; l'inizio della frase non è leggibile.

> [!tip] Esame: sulla pagina Moodle ci sono esami vecchi e prima dell'esame finale si fanno esercitazioni stile mock exam, con il docente, il dottor Peruzzi o il tutor.

- La lezione si può recuperare; il docente incoraggia il ricevimento: ==spiegare dove sono gli errori è troppo tardi, ormai il compito è fatto.==

> [!question] Da verificare: la trascrizione riporta "per mettervi di risolvere i problemi pre-esame non posto. Il coraggio di un esame, spiegare dove sono gli errori, è troppo tardi"; non si legge a quale momento si riferisca.

## Iscrizione a Moodle, ricevimento ed esame

- Ci si deve iscrivere manualmente a Moodle, così il docente può contattare tutti in blocco.
- Si può scrivere per un altro orario di ricevimento, anche online.
- ==L'unica cosa che non si può fare online è la visione dell'esame. Chi vuole vedere l'esame esposto dovrà venire.== Non c'è tempo per la scansione di cento compiti.

> [!question] Da verificare: la trascrizione riporta "Ok, quindi a parte quello, però ricevimenti standard non possiamo fare"; non si capisce se il docente escluda o ammetta i ricevimenti standard online.

- Per chi ha diritto, le registrazioni delle lezioni saranno scaricabili dalla pagina, se funziona.

> [!tip] Esame: l'esame è scritto, di una decina di domande (numero non fissato), e si chiede di interpretare risultati, non di fare le stime.

- La stima con un software è per chi vuole diventare operativo, ma si consigliano le lezioni empiriche, che spiegano come interpretare i modelli.
- La prima lezione empirica, probabilmente la settimana prossima: riscalare le variabili con trasformazioni tipo logaritmo, interpretare gli effetti marginali in scala diversa, approssimata o esatta, e diagnosticare la quasi collinearità; la collinearità esatta è facile.
- Il variation factor serve a diagnosticare la quasi collinearità, normalmente un problema perché, se non me ne accorgo, penso che il modello mi dia risultati non corretti.

> [!question] Da verificare: la trascrizione riporta "la collinearità esatta è facile, con due si pianta"; che cosa si pianti non è determinabile.

> [!question] Da verificare: la trascrizione riporta "variation factor"; probabilmente il variance inflation factor, ma nelle slide non compare.

> [!question] Da verificare: la trascrizione riporta "se non me ne accorgo, penso che il modello mi dia dei risultati che non sono corretti"; dal contesto il senso sembra l'opposto (li penso corretti e non lo sono), si riporta come detto.

- Le lezioni empiriche con il dottor Peruzzi legano teoria e pratica; il compito chiede di interpretare risultati, capire se il modello ha un problema, analizzando grafici e tabelle, e nelle serie storiche interpretare i risultati dinamici e statici di un modello dinamico. Ci sono già esempi.

## Feedback e libro di testo

- Si può interrompere in qualsiasi momento: il corso è per gli studenti; al docente non piace correggere compiti.

> [!question] Da verificare: la trascrizione riporta "doppi altissimi, che mi appello"; il senso probabile è "voti altissimi al primo appello".

- Senza feedback può esserci un mismatch notato troppo tardi; il programma si può modificare, se c'è tempo, in base agli interessi.
- L'acquisto del libro non è obbligatorio, ma è utile: discorsivo, con molti esempi, soprattutto sulle serie storiche e la regressione, e argomenti in più *(slide 4)*; è in biblioteca.
- I lucidi sono solo uno schema per appunti o scaletta del docente, messa a punto in trent'anni di insegnamento; il libro dà di più.

## Materiale di statistica di base

- Il primo set di lucidi è l'introduzione; ci sono anche appunti di un corso di statistica di base per richiamare i concetti essenziali, come medie e varianze e la notazione (per esempio E per la media), all'inizio della pagina Moodle.

## Che cos'è l'econometria

- L'econometria ha tre scopi, ma in generale è un'analisi quantitativa di modelli economici *(slide 5)*; non esiste una definizione chiara.
- Il primo scopo è la misura delle relazioni causa-effetto tra variabili.
- Il secondo è fare previsioni, che è più statistica che econometria.
- Il terzo è usare metodologie anche avanzate per valutare teorie economiche, per esempio il CAPM: due pagine di algebra che danno l'equazione per cui gli extra rendimenti di un investimento sono proporzionali agli extra rendimenti del portafoglio di mercato.
- Il CAPM richiede molte ipotesi: mercato dei capitali e dei tassi di interesse in equilibrio, portafogli costruiti con l'algoritmo di Markowitz.

## Validare un modello economico: il CAPM

- Domanda: la relazione è credibile e i dati la supportano? Se il modello fosse vero, un rendimento in media non dovrebbe garantire un premio extra per il rischio, quindi la regressione non può avere l'intercetta.
- Possibile test: una regressione semplice con intercetta, e valutare se è uguale a zero o diversa da zero.
- Se il modello non passa il test, non basta aggiungere l'intercetta: cambierebbero tutte le equazioni e ipotesi precedenti, e va rispecificato il modello economico.
- La validazione è la parte preferita del docente: ho una teoria, ho dei dati, voglio vedere se la teoria spiega i dati.

## Relazioni causa-effetto e criteri di causalità

- Una relazione causale si rappresenta con un grafo asimmetrico: la x ha un impatto sulla y ma non viceversa, la x è un driver per la y; il problema è capire se x è una causa per y *(slide 6)*.
- Devono valere tre criteri. Il primo è statistico: serve almeno una relazione statistica; se le variabili sono quantitative, una correlazione statisticamente significativa tra x e y.
- La correlazione è simmetrica, quindi non dice nulla sul nesso causale, solo che c'è un legame di qualche natura.
- Serve anche un legame logico, una variabile che anticipi l'altra non solo temporalmente, con una storia che spieghi il legame statistico. E quella storia deve essere unica.

> [!question] Da verificare: la trascrizione riporta "So più storie che coerentemente mi descrivono quella forma di dipendenza statistica, lo troverò migliore"; la frase non è leggibile, il senso probabile è che con più storie coerenti il legame non è stabilito.

- Il legame logico deve essere unico. ==La cosa importante da capire è che il legame statistico non è sufficiente.==

## Correlazioni spurie: gli esempi del sito

- Una pagina web di uno statistico buontempone *(slide 13)*: un programma cerca le coppie più correlate in un database di 10.000 variabili, senza pensare a che variabili sono.
- Primo esempio: gente che ha guardato Big Bang Theory contro ricerche Google che cominciano con "how to make"; nessun legame logico, ma si potrebbe prevedere l'una con l'altra. L'R quadro è 96,5%.
- ==Questo 96,5% mi spiega solo il legame statistico==: dice che le serie si muovono insieme, non perché, e non che il modello è corretto dal punto di vista logico.
- Sul sito ci sono a volte spiegazioni fatte con l'IA della correlazione alta.
- Secondo esempio: partite di lacrosse contro biglietti venduti al cinema, correlazione intorno al 74%, senza legame sostanziale.

> [!question] Da verificare: la trascrizione riporta "la cross"; si interpreta come lacrosse, ma le slide non lo confermano.

> [!question] Da verificare: la trascrizione riporta "il 74% o più del 50%"; il valore non è del tutto leggibile.

- L'IA una storia la trova, ma non ha necessariamente senso; il legame statistico è solo il primo pezzo.
- Un R quadro grande non vuol dire che il modello vada bene.

> [!question] Da verificare: la trascrizione riporta "se il primo modello di regressione, quando è grande"; dal seguito ("i modelli buoni non hanno R quadro così grande") si legge "R quadro".

- Tipicamente i modelli buoni non hanno R quadro molto grande; un R quadro troppo grande porta problemi di collinearità.
- Variabili legate statisticamente ma senza motivo logico non spiegano perché una si muova e non permettono analisi di scenario; quello che si trova è casuale e non replicabile.

## Nessun modello è definitivo, ma si lavora con regole precise

- Quasi mai si ha una risposta definitiva, perché è quasi impossibile escludere tutte le altre spiegazioni logiche; la distinzione causale dà però una regola su come lavorare.

> [!question] Da verificare: la trascrizione riporta "relazioni casuali" e "distinzione casuale"; la slide 11 tratta lo stesso passaggio come "relazione causale" e si adotta "causale".

- Ogni volta devo capire perché costruisco il modello e perché scelgo certe variabili; poi vedo se i coefficienti hanno il segno atteso, perché un segno sbagliato può indicare una stima non corretta.
- Lavorando in modo coerente il mio modello contribuisce al lavoro degli altri, finché si trova un consenso: provati 10.000 modelli, esclusi tutti gli altri.
- Un modello perfetto con le tre caratteristiche è troppo ambizioso, soprattutto la terza parte.
- ==la relazione statistica non è abbastanza==: serve un legame logico che resista a spiegazioni alternative; provare modelli buttando dentro dati sperando nei segni giusti non basta.

## Fumo e malattie dei polmoni

- Sintesi della letteratura epidemiologica sull'associazione tra fumo e malattie gravi ai polmoni *(slide 12)*: la correlazione c'è ma non basta per la relazione causa-effetto.
- Per decine di anni sono state testate ipotesi e trovati meccanismi biologici; ora c'è l'idea di una relazione causa-effetto, probabilmente definitiva, ma da ripensare se un biologo trovasse un'alternativa più convincente.
- ==quello che state facendo non deve essere un tentativo, ma deve essere un tentativo fatto con un background==.
- Prima dei dati si capiscono i potenziali driver e poi si inseriscono nel modello; non si mette tutto dentro per selezionare finché non si trova qualcosa. La teoria definisce i legami logici a priori, non la correlazione.

> [!question] Da verificare: la trascrizione riporta "Ho fatto il contrario, che è tutta la roba dentro modello"; si riporta in forma negativa, coerente con il contesto.

## Boy scout e criminalità: causalità inversa

- Dati inventati da un libro di statistica, per capire da dove nascono le correlazioni spurie *(slide 9)*: tabella a doppia entrata tra chi ha fatto il boy scout e chi ha avuto problemi con la giustizia.
- Tra chi ha fatto il boy scout l'incidenza è più bassa: sembra una relazione negativa. Spiegazione logica: regole e principi insegnati, relazione boy scout verso delinquency *(slide 10)*.
- Spiegazione alternativa: chi è avverso alle regole non si iscrive ai boy scout, quindi la direzione è opposta.
- ==Il legame statistico, che è simmetrico, non mi dice nulla su qual è la direzionalità tra le variabili.== Si chiama reverse causality.

## Prossima lezione

- Oggi era una chiacchierata; giovedì si ragiona su come definire un modello statistico che descriva una relazione causale e su come capire quando lo supporta o no.
