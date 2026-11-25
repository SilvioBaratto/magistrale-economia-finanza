---
corso: Finanza Strategica
data: 2026-11-24
fonte: Audio/finanza_strategica/finanza_strategica_2026-11-24.txt
tipo: appunti-lezione
tags: [appunti, finanza-strategica]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
---

# Metodi DCF sintetico e analitico: terminal value e sanity check

## Valutazione dell'impresa Alfa con i metodi sintetici

Si riprende l'esempio numerico delle slide dell'ultima lezione per vedere come, partendo da un conto economico, si determini il valore dell'impresa con il metodo dei flussi di cassa attualizzati (DCF). I flussi non vengono dal rendiconto finanziario ma dal conto economico. Una grandezza che il conto economico non mostra in modo isolato, ma che conviene calcolare, è il NOPAT, perché rappresenta l'equivalente dell'FCFO, cioè il flusso di cassa della gestione caratteristica.

L'esercizio riguarda l'azienda Alfa. Si chiede di calcolare enterprise value ed equity value con la formula dei DCF, sapendo che il WACC è 5,8% e il costo del capitale proprio ($r_E$) è 7,5%. Di Alfa si ha solo il conto economico: non c'è un business plan da sviluppare, quindi si usano le formule compatte, assumendo flussi costanti nel tempo. I tassi sono noti. Restano da individuare le grandezze del conto economico da usare per il valore in ottica asset e in ottica equity.

La risposta sta nella slide 6, che sembra un riepilogo ma in realtà è l'inizio dell'argomento. La terza freccia dice che, guardando l'aspetto reddituale, in ottica asset si ragiona sul NOPAT e in ottica equity sul reddito di bilancio normalizzato, cioè sull'ultima riga del conto economico. In un rendiconto finanziario le due grandezze corrisponderebbero all'FCFF (o FCFO) e all'FCFE, cioè alla remunerazione che poi diventa dividendo per gli azionisti. Le grandezze da prendere dal conto economico di Alfa sono quindi due: il NOPAT e il reddito di bilancio. Il NOPAT va calcolato a parte, perché nel conto economico civilistico non compare.

> [!question] Da verificare: nel punto in cui il docente chiede quali due grandezze si prendano dalla slide, la trascrizione riporta "il NOPAT e il reddito operativo", e più avanti "il reddito operativo di bilancio fratto l'RE". Dal contesto (ultima riga del conto economico, "utile o perdita di bilancio") la seconda grandezza è il reddito di bilancio.

Il NOPAT è la quantità di margine a conto economico prima del pagamento degli interessi ai creditori e dei dividendi agli azionisti. Poiché l'enterprise value è il valore per entrambe le categorie, il NOPAT è il numeratore della formula dell'enterprise value. Al denominatore, per omogeneità dei tassi, va il WACC e non il costo del capitale proprio: si tratta di calcolare una rendita perpetua, un NOPAT proiettato all'infinito, e il WACC è il tasso più appropriato per attualizzare un flusso destinato sia agli azionisti sia ai creditori. Il reddito di bilancio, che spetta agli azionisti, si attualizza invece al $r_E$.

Le formule usate sono quelle in ipotesi di steady state, cioè di azienda che non cresce, perché l'esempio non parla di crescita:

- enterprise value = NOPAT / WACC;
- equity value = reddito di bilancio (l'ultima riga del conto economico) / $r_E$.

Applicandole all'esercizio, l'enterprise value risulta di circa 1.031.000 e l'equity value di 586.000. L'enterprise value è il valore di tutta l'azienda, l'equity value la parte degli azionisti. Si potrebbe anche ipotizzare, ma non faceva parte dell'esempio, che Alfa abbia una PFN di 445.000, cioè la porzione di valore in capo ai creditori. L'esempio chiedeva solo enterprise value ed equity value.

### Il caso con crescita

Si riprende lo stesso esempio, con WACC al 5,8% e $r_E$ al 7,5%, per un'azienda che presenta un capitale investito netto operativo di 760.000 e un capitale proprio di 302.000 e che prevede di crescere del 2% l'anno a tasso costante. È l'ipotesi del $g$ già visto: l'azienda cresce all'infinito del 2%. Si è quindi in ipotesi di steady growth e si applicano le due formule, quella di sinistra per l'enterprise value e quella di destra per l'equity value, che contengono tutte le grandezze dell'esercizio.

Come detto nella lezione precedente, il NOPAT cresce al tasso $1 + g$, cioè del 2% ogni anno nella formula di sinistra. L'azienda però si irrobustisce: anche il capitale investito netto operativo cresce al tasso $g$ del 2%. È una semplificazione molto forte della realtà, che cerca di approssimarla. Non è detto che un'azienda il cui utile cresce del 2% l'anno abbia anche una struttura che cresce del 2%, e spesso i dati lo smentiscono. Si applica comunque questa correzione, perché altrimenti un'azienda che cresce del 2% all'infinito vedrebbe esplodere il proprio valore. È un accorgimento prudenziale: il valore del NOPAT cresciuto viene ridotto dall'aumento del capitale investito, di pari crescita.

I risultati sono i seguenti. Un'impresa che non cresce ha un enterprise value di circa 1.031.000. Un'azienda con lo stesso WACC e lo stesso $r_E$ che cresce del 2% ha un enterprise value di circa 1.206.000. Vale quindi di più l'azienda che cresce di quella che non cresce, e la differenza è l'effetto di $g$. Le slide con i numeri vengono messe a disposizione dopo la lezione.

### Collocazione nel programma

Oggi si prosegue con i metodi DCF. I multipli si vedranno nelle lezioni successive.

> [!question] Da verificare: la trascrizione riporta "da domani vediamo i multipli, da dopodomani vediamo i multipli, da giovedì". Il giorno di inizio dei multipli non è chiaro, probabilmente giovedì.

Riprendendo il concetto: il metodo sintetico è quello in cui si ipotizzano flussi costanti e un tasso di crescita costante, indicato con $g$. Si è all'interno dei DCF, che si basano sui numeri dell'azienda, cioè sui suoi bilanci.

I DCF si distinguono dai multipli, che prendono anche valori di mercato. All'interno dei DCF i metodi sono due: il sintetico e l'analitico.

### Il metodo sintetico

Il metodo sintetico prevede flussi costanti e tassi di crescita costanti. È una forte semplificazione della realtà, ma permette di usare formule compatte e di calcolare il valore dell'azienda partendo dal solo bilancio, scaricabile dalla Camera di Commercio. Non servono dati gestionali: la formula compatta si calcola rapidamente. Il procedimento è simile a quello dei multipli, dove si parte da un EBITDA, cioè da un conto economico riclassificato a cui si applicano i multipli.

Il DCF sintetico si usa, ad esempio, per valutare la target di un'acquisizione quando chi valuta non è interno all'azienda e quindi non dispone di tutti i numeri, come in un'autovalutazione. Il bilancio si scarica da AIDA o da Orbis e si calcolano i flussi di cassa, oppure grandezze economiche equiparabili, come il NOPAT. Dell'azienda non si sa altro, e per questo i flussi sono costanti. Il tasso di crescita non è noto, ma si può assumere quello del mercato. Un advisor che deve valutare una target di cui non ha altre informazioni dispone solo dei bilanci e può prendere come $g$ la crescita prevista per il settore, ricavandola da ricerche di mercato. Le associazioni di categoria (moda, gioielleria, lusso, acciaio) pubblicano ogni anno studi di settore con previsioni sulla crescita del mercato, e un valutatore può assumere quel tasso.

Il tasso di crescita costante va preso con grande cautela, come già detto nella lezione precedente ("con una maxi pinza"), perché viene applicato in una formula di rendita perpetua e quindi proiettato all'infinito. Questa assunzione, di per sé piuttosto forte, viene attenuata dai modelli multi-step, che si vedranno verso la fine del modulo e che si trovano anche nel libro.

### Il metodo analitico

Il metodo analitico sarebbe preferibile, ma richiede, oltre al bilancio (che si scarica dalla Camera di Commercio o da AIDA), un documento che non si ha e che deve essere fornito: il business plan. Senza business plan il metodo analitico non si può applicare. Ne derivano due casi: o si valuta la propria azienda e il business plan è a disposizione, oppure qualcuno consegna quello dell'azienda target. In caso contrario non si può fare nulla. Il metodo analitico è più rigoroso proprio perché poggia sul business plan.

Il business plan, o piano industriale, è tradotto in italiano il piano economico-finanziario. Contiene una serie di descrizioni del business e ha un orizzonte, cioè il punto fin dove chi lo ha scritto si è spinto con le previsioni: tre, cinque o sette anni. Giovedì il docente mostrerà un business plan completo di un'operazione conclusa.

### I limiti del business plan

Negli ultimi anni le previsioni sono state sconvolte da una serie di eventi. Nel 2020-21 la pandemia ha fatto saltare le previsioni sulla crescita delle aziende. Dal 2022 c'è la guerra in Ucraina, che a febbraio compie cinque anni. Nel frattempo i dazi decisi da Trump e ulteriori guerre hanno sconvolto il mercato. Quasi tutte le aziende lavorano o esportano su tutti i paesi del mondo, a meno che non siano realtà artigianali locali, e anche queste spesso esportano. Il conto economico di un'azienda e i suoi flussi sono quindi esposti a una moltitudine di fattori mondiali, che ormai cambiano di settimana in settimana. Per questo è difficile fare un business plan e persino una previsione a tre anni: i mercati e le economie salgono e scendono, e gli analisti si accorgono che alcuni business hanno economie diverse man mano che nascono e si sviluppano.

Il settore dell'intelligenza artificiale ne è un esempio: quasi tutte le aziende sono ampiamente in perdita, quindi il loro sviluppo è una scommessa. Scrivere il business plan di Anthropic, o dell'intero settore dell'intelligenza artificiale e del calcolo, significherebbe prevedere conti profondamente in rosso. Lo stesso vale per altri settori, come quelli legati all'informatica, e per quelli colpiti dalle guerre.

Un altro esempio è lo stretto di Hormuz, che ha inciso sul costo dei combustibili. Un'azienda esposta ai trasporti che avesse scritto il business plan prima che fossero posizionate le mine nello stretto avrebbe sbagliato completamente la previsione del costo dei trasporti, perché nessuno poteva prevederlo. Un anno fa un business plan proiettava costi di trasporto in condizioni del tutto normali. Oggi il costo del gasolio, compreso quello delle navi portacontainer e degli aerei cargo, è praticamente raddoppiato. Un'azienda che esporta in tutto il mondo a proprie spese, o che importa dalla Cina via nave, deve fare adesso tre o quattro volte la strada di prima. Confrontando il business plan di un'azienda scritto un anno fa con il suo conto economico a consuntivo, si troverebbe una differenza enorme.

Il metodo analitico si basa sul business plan, ma il business plan non è opera di un mago: lo ha scritto un analista dell'azienda con le informazioni disponibili in quel momento.

### Le analisi di scenario

Il business plan contiene spesso analisi di scenario, forse già viste. Oggi di solito se ne costruiscono almeno due o tre. Il primo descrive come stanno le cose da qui a tre anni. Lo scenario ottimistico prevede che Hormuz riapra e che il gasolio torni a costare un euro e sessanta anziché due euro e venti. Lo scenario pessimistico prevede un peggioramento del quadro economico, con costi in aumento, più dazi, un aumento del costo delle materie prime o la loro scarsità perché alcuni paesi falliscono, e così via.

### Business plan e terminal value

Nel business plan si fanno solitamente tre scenari: normal, best e worst. Disponendo di un business plan si ha la previsione dei flussi di cassa dei prossimi tre, cinque, sei o sette anni. Come nella prima lezione con il VAN, i flussi visibili nel fascicolo del business plan si portano al tempo zero: è il metodo analitico. Superato il periodo del business plan, l'altro elemento che concorre alla valutazione dell'azienda è il terminal value.

Il terminal value, o valore terminale, è una formula che approssima una serie di flussi illimitati, dall'ultimo anno dell'orizzonte del business plan fino all'anno n all'infinito. Si assume che l'impresa sia equiparabile a una rendita perpetua, una macchina di flussi di cassa, e il terminal value è una sorta di rendita posticipata.

### Aziende a durata limitata

L'ipotesi del terminal value presuppone una durata illimitata dell'azienda. Esistono però casi di aziende a durata limitata, in cui qualcosa limita la vita dell'impresa a dispetto dei principi di going concern e di continuità aziendale, secondo cui l'azienda prospererà all'infinito. A un certo punto l'azienda finisce, viene messa in liquidazione, e applicare una rendita perpetua non ha senso. I casi sono tre.

1. Vincoli di natura normativa, nei business in regime di autorizzazione o concessione. Le concessioni di beni del demanio durano 20 o 30 anni e non è detto che vengano rinnovate: è il caso dei balneari, delle autostrade, della gestione di una diga o dello sfruttamento di una falda acquifera per erogare e vendere acqua, cioè di attività legate al pubblico servizio.
2. Limiti ambientali. Una società che gestisce una miniera non continua a scavare fino al centro della Terra: quando la risorsa finisce, finisce. Nel DCF di una miniera si deve fare attenzione a usare il terminal value, perché lo sfruttamento del giacimento può essere limitato.
3. Joint venture, reti di imprese, consorzi o associazioni in partecipazione. Queste realtà hanno spesso uno scopo e una durata, e anche qui non si assume una rendita perpetua illimitata.

Il docente porta alcuni esempi. Mercatone Uno è entrata in amministrazione straordinaria, come risulta dal comunicato dei commissari straordinari: il brand termina e non può essere una rendita illimitata. La società Expo 2015 è chiusa. L'area dell'Expo, con l'albero della vita, i raccordi, la fermata della metropolitana, i parcheggi e il polo fieristico di Rho, esisteva già in parte (la fiera), ma è stata ampiamente ingrandita per l'Expo, mentre prima del 2015 c'era una spianata di campi. Per l'evento è stata creata una società che oggi non esiste più.

> [!question] Da verificare: il docente introduce l'esempio con "se voi siete stati a Roma", ma i luoghi citati (polo fieristico di Rho) sono a Milano.

Una joint venture tra GAC e Fiat Chrysler è un esempio di joint venture costituita per lanciare progetti: in questo caso non è andata bene ed è finita in liquidazione. Un altro esempio è Ship Recycling S.c.a.r.l., descritta dal docente come "società consortile in accomandita a responsabilità limitata" (i corsi di diritto commerciale ne trattano la forma). È stata costituita per smaltire la Costa Concordia: una volta raddrizzata la nave, restavano da smaltire 23.000 tonnellate di acciaio. Con un accordo tra Saipem e Fonderie San Giorgio è nata una società la cui durata era il tempo necessario a recuperare, vendere e smaltire tutto il ferro, e così è stato. Dall'estratto dei bilanci risulta che la società è stata posta in liquidazione il 4 ottobre 2017 per avvenuto conseguimento dell'oggetto sociale. La colonna del 2025 è vuota: la società ha chiuso i conti nel 2024 e nel 2025 tutte le voci sono a zero.

Altre aziende chiudono perché sopraggiungono certe condizioni o perché vengono assorbite da un gruppo. Se la target da valutare viene acquisita e dopo tre anni chiusa, il tempo è quello necessario a rilevarla, trasferire asset e personale, prendere ciò che serve e metterla in liquidazione. In questo caso non si può applicare il terminal value, perché dopo tre anni l'azienda chiude. Tutti questi esempi di aziende che chiudono sono contrari all'ipotesi di durata illimitata, quindi il terminal value come rendita perpetua non è applicabile.

### Le due componenti del metodo analitico

Nel modello analitico del DCF il valore dell'impresa è determinato in base alla capacità di generare flussi di cassa futuri, che si articola in due componenti: il business plan e il terminal value.

La prima è il periodo di previsione analitica, un orizzonte temporale generalmente tra i tre e i cinque anni. Una volta si scriveva sette, ma oggi nessuno si azzarda a fare un business plan a sette anni, perché nessuno è in grado di stimare i ricavi e i costi delle materie prime nel 2033 circa. La seconda è il periodo successivo alla previsione analitica, che si estende oltre l'ultimo anno del business plan: si assume (è un'informazione che il valutatore deve avere) che l'impresa continui a svolgere la propria attività e a generare flussi di cassa. Questa parte è espressa dal terminal value.

Negli esempi visti, dopo il business plan il secondo elemento, se la durata è limitata, cioè se si sa già che l'azienda chiuderà dopo tre, cinque o sette anni, non sarà una rendita perpetua.

> [!question] Da verificare: la trascrizione riporta "sarà una rendita perpetua", ma il seguito ("non prenderò il terminal value come rendita perpetua") indica che il docente intendeva "non sarà".

Per valutare con il DCF la società che ha smaltito il ferro della Costa Concordia, si ha un business plan a tre, cinque o sette anni e dopo non si prende il terminal value come rendita perpetua, ma un valore terminale contabile, cioè una sorta di valore contabile o di liquidazione. Al quinto anno l'azienda non proietta flussi di cassa illimitatamente: si dismettono le macchine, ad esempio le gru ragno che staccavano il ferro dalla nave e lo posavano sul piazzale. Resta da stabilire quanto valgano quei beni.

Il valore terminale sarà un valore contabile di liquidazione. Lo stesso vale per la società nata per costruire il passante di Mestre, cioè la variante da Mestre a raccordo con l'altra tratta: quella società come tale non c'è più, ha magari cambiato oggetto sociale e ora si occupa di manutenzione. Ha venduto o comprato ruspe e mezzi, e il valore contabile finale è quello che conta.

L'applicazione del terminal value dipende quindi dalla durata. Se la durata è illimitata si usa una rendita perpetua. Se è limitata si usa un valore residuo, che si recupera liquidando il patrimonio aziendale, cioè vendendo gru, ruspe, macchine, automezzi e così via.

### La formula dell'enterprise value con il terminal value

Occorre usare i flussi di cassa corretti. In ottica asset, dove si calcola $W$, cioè l'enterprise value di tutta l'azienda, il valore è la somma di due termini: il valore attualizzato dei flussi di cassa del business plan e il terminal value attualizzato.

La parte a sinistra del segno più nella formula, con l'FCFF diviso per $1 + \text{WACC}$, è la stessa operazione degli esercizi svolti in precedenza: un progetto genera i flussi di cassa degli anni 1, 2, 3, 4, ciascuno con il proprio indice, e ciascuno viene attualizzato. Qui l'attualizzazione avviene al WACC perché si valuta tutta l'azienda. Se al numeratore ci fosse l'FCFE, il flusso per gli azionisti, l'attualizzazione avverrebbe al tasso $r_E$, relativo alle aspettative degli azionisti.

> [!question] Da verificare: la trascrizione riporta "come quello che facevate sugli esercizi delle opzioni"; dal seguito ("ho un progetto che genera i seguenti flussi di cassa", "come facevamo negli esercizi del progetto") si tratta degli esercizi sui flussi di un progetto di investimento.

La parte a destra del segno più è il terminal value, indicato con TV. TV è un valore collocato nel tempo futuro. Il valutatore si trova sempre al tempo zero, come negli esercizi sul progetto, quindi anche TV va portato indietro fino a zero. Come si portano a oggi i flussi del business plan, così si porta a oggi il terminal value, con lo stesso tasso usato nella parte di sinistra.

### Che cos'è il terminal value

Il termine "terminal value" non compare in un business plan né in un bilancio: è un'etichetta creata per indicare un insieme infinito di flussi di cassa nel tempo, cioè una rendita perpetua. Nella formula (il quadrato azzurro della slide) la sigla TV si può quindi sostituire con una formula. Nel mondo dell'enterprise value, il terminal value è il NOPAT, il flusso di cassa a beneficio di tutti, attualizzato come rendita perpetua al WACC. Il fattore $1/(1 + \text{WACC})^n$, contrassegnato nella slide con un asterisco, serve solo a portare il valore al tempo zero. Il terminal value è quindi il flusso proiettato all'infinito a partire dall'ultimo anno del business plan, e va riportato indietro per tutta la durata del piano.

In un business plan quadriennale, i flussi del periodo uno vengono portati indietro di un periodo, quelli del periodo due di due, del tre di tre e del quattro di quattro. Al quinto anno si colloca il terminal value, che viene portato indietro anch'esso. Se il flusso è proiettato all'infinito dall'anno cinque, il terminal value va riportato indietro di cinque periodi. L'enterprise value è la somma di questi termini, come negli esercizi di una o due settimane prima: è il valore, oggi, di un'azienda che opererà all'infinito.

### Esempio: piano industriale a cinque anni

Oggi, 24 novembre 2026, un advisor si fa consegnare il business plan a cinque anni, ad esempio il piano industriale di Adora, per il periodo 2027-2031. Nel piano c'è una pagina con il rendiconto finanziario previsionale: il rendiconto del 2026 è praticamente chiuso, seguono quelli del 2027, 2028, 2029, 2030 e 2031. I flussi di cassa si attualizzano a oggi e il risultato si mette da parte. Poi si calcola il terminal value e lo si porta a oggi.

Il docente anticipa la domanda su quale flusso di cassa usare nel terminal value per proiettarlo dal 2032 in poi. Il flusso migliore disponibile è l'ultimo del business plan, FC5: si vede fino al 2031, e l'orizzonte più lontano visibile diventa il flusso da cui parte il terminal value, proiettato dal 2031 all'infinito.

> [!question] Da verificare: la trascrizione riporta "dal 2031 al 2801", forse "dal 2031 all'infinito".

Un altro esempio, se ci si trovasse nel 2025: si prendono i flussi del 2026, 2027 e 2028, cioè un business plan a tre anni. Si calcola il NOPAT dell'ultimo anno, oppure si prende il flusso di cassa dell'ultimo anno, e lo si usa da quel momento all'infinito: è il terminal value.

### Terminal value con crescita

Se si vuole inserire anche il tasso di crescita $g$, si usano le formule con $g$. La formula risulta arricchita ma ha sempre la stessa struttura, la somma di una previsione esplicita e del terminal value attualizzato. A sinistra del segno più c'è la previsione esplicita, cioè il business plan, con i flussi (i termini in verde della slide) portati indietro uno per uno. A destra c'è il terminal value, con al numeratore il NOPAT che cresce al netto della crescita del capitale investito netto, al denominatore il WACC nella versione con $g$ e infine il fattore di attualizzazione. Si porta indietro una rendita perpetua dall'ultimo punto, il 2031, a oggi, per cinque periodi: il terminal value viene riportato in $t = 0$.

> [!question] Da verificare: la formula del terminal value con crescita è letta a voce ("NOPAT che cresce meno il capitale investito netto che cresce fratto il WACC che cresce per il fattore di attualizzazione") e non è determinabile dal parlato; va controllata sulla slide.

### I sanity check

Per stabilire se il procedimento ha senso, occorre guardare alcune grandezze. Nel libro c'è un paragrafo sui sanity check, che mettono in relazione ciò che risulta a sinistra del segno più con ciò che risulta a destra: il valore che emerge dalla previsione esplicita, cioè dal business plan, e quello ottenuto con la stima della proiezione all'infinito.

Un esempio grafico: se l'enterprise value risulta di 10 milioni ed è distribuito in modo che i quattro anni di business plan valgano un milione di flussi di cassa e il terminal value attualizzato ne valga 9, tanto valeva usare direttamente una rendita perpetua. Ci sono due letture possibili. Il business plan pesa pochissimo, oppure la maggior parte dei flussi si manifesta nella zona arancione della slide, cioè dal 2031 in poi. In questo secondo caso nei primi anni non succede quasi nulla, perché ad esempio il progetto deve ancora partire: il business plan mostra per i primi tre, quattro o cinque anni flussi di cassa vicini a zero, gli FCFF sono scarsi perché l'attività è appena avviata. Il grosso arriva quando, per esempio, un'app raggiunge un milione di utenti, mentre nei primi anni si regala il prodotto o si fanno promozioni, e questa parte del business plan rende poco.

A quel punto si potrebbe obiettare che non vale la pena guardare il business plan. Se i flussi dei primi anni sono scarsi e il valore è concentrato in un terminal value molto grande, tanto vale usare subito la formula compatta, con un flusso a regime attualizzato, senza scomporre i primi anni del piano. I sanity check dicono questo: se risulta che il 90% del valore dell'impresa dipende dalle ipotesi formulate sul periodo successivo al business plan, o ci sono errori di previsione nel business plan (le entrate sono sottostimate), o l'orizzonte è troppo breve e il business plan avrebbe dovuto essere più lungo, oppure si lascia perdere il metodo analitico. Il metodo analitico non serve a niente se i flussi del business plan non sono apprezzabili.

Questi indicatori sono quozienti da calcolare dopo aver applicato il metodo analitico con il terminal value. Se i pesi risultano molto elevati e non congruenti, mostrano che non ha senso usare il metodo analitico.

> [!question] Da verificare: la trascrizione riporta "chiudiamo l'argomento switch exit come gli interpreto", probabilmente "chiudiamo l'argomento dei sanity check, come interpretarli".

In sintesi, quanto maggiore è il peso del terminal value rispetto al resto, tanto più la valutazione dipende dalle ipotesi formulate sul lungo periodo dell'impresa, cioè dalla parte ipotizzata per la crescita perpetua. Quando il terminal value è l'85-90% di tutto il valore dell'impresa, ci si deve porre domande sul business plan e sul tipo di previsioni fatte sui flussi dei primi tre, quattro o cinque anni.

### I modelli multi-step

Un modo per attenuare il problema sono i modelli multi-step, che si vedranno rapidamente. Partono dall'idea che i business non crescano sempre allo stesso modo, con lo stesso flusso, ma possano avere velocità diverse: i modelli multi-step ipotizzano che la crescita si muova a velocità diverse in periodi diversi.

Un primo caso è il lancio di un'azienda con un'app nuova a diffusione progressiva: nei primi anni ci sono molti investimenti, quindi molto rosso nel business plan e pochi flussi in entrata. Il caso opposto è il lancio di un gadget o di un prodotto di moda con un fenomeno di massa immediato: c'è una fiammata iniziale, anche più alta rispetto al settore, poi l'effetto moda si raffredda e i flussi di cassa rallentano, per poi magari stabilizzarsi. Si può quindi avere un modello a due o a tre stadi, per semplificare la realtà.

Un modello a due fasi corrisponde a un'azienda che lancia un prodotto con una fiammata iniziale e poi si stabilizza nel lungo periodo. Ad esempio una nuova console o un nuovo dispositivo: all'inizio lo vogliono tutti, poi le persone che continuano a comprarlo e a sostituirlo si stabilizzano. Un altro caso è l'azienda che ha un brevetto e lo sfrutta nella fase iniziale, come nel settore farmaceutico o nel design.

Secondo il docente, Ikea, come Zara, copia: molti suoi prodotti sono di design e il brevetto non c'è più, come per chaise longue, lampade e pezzi vintage. I designer possono aver registrato il brevetto per un periodo e poi liberarlo, oppure il brevetto decade dopo un certo numero di anni. L'azienda che detiene il brevetto nel momento del lancio ha una posizione diversa. L'esempio è Kartell, con la lampada di Castiglioni dagli anni Sessanta, quella con il cubo di marmo, lo stelo e la campana, che si vede nei negozi di arredamento ed è piena di imitazioni. Oggi si trova ovunque, anche da "Ovio" al centro commerciale a un prezzo molto basso, ma l'originale aveva un brevetto: chi voleva quella lampada poteva comprarla solo da quell'azienda. Scaduto il brevetto, l'azienda ha continuato a venderla, ma ora la vendono tutti.

> [!question] Da verificare: la trascrizione riporta "Kartell" per l'azienda della lampada di Castiglioni e "Ovio" per il negozio del centro commerciale; entrambi i nomi non sono verificabili dal parlato.

Esiste anche un modello a tre stadi: una crescita molto veloce, una riduzione e poi una stabilizzazione. Sono, osserva il docente, semplificazioni della realtà.

La lezione si interrompe qui; la prossima riprende da questa slide.
