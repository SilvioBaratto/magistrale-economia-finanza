---
title: "I metodi DCF: modelli sintetici asset side ed equity side"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_03_Modelli-Valutazione-Finanziaria-Parte1.pdf"
text_layer: true
verified: true
generated: 2026-08-30
---

## Inquadramento

Questo capitolo presenta i metodi **DCF** (Discounted Cash Flow) come passaggio dal valore dei singoli investimenti al valore dell'intera impresa. Al centro stanno i **modelli sintetici**, in entrambe le ottiche di valutazione, asset side ed equity side. Il testo di riferimento è il capitolo 8 del testo BBS, fino al paragrafo 8.4.

I tassi di sconto usati in questi modelli, il WACC per l'ottica assets e il costo dell'equity per l'ottica equity, derivano dalle decisioni di investimento dell'impresa indebitata ([[FSTR 02-full Costo del Capitale|il costo del capitale]]). Dopo i metodi DCF la sequenza degli argomenti passa ai multipli di borsa ([[FSTR 06 Multipli di Borsa lez01|i multipli di borsa]]), alla crescita esterna con la valutazione delle operazioni di integrazione e alla due diligence. I modelli DCF analitici e il terminal value sono sviluppati in [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|i metodi DCF analitici e il VAM]].

## Le grandezze di riferimento per la valutazione dell'impresa

> [!abstract] Definizione
> La valutazione d'impresa si conduce in due ottiche, **assets** ed **equity**. In ciascuna si individuano grandezze di riferimento sul piano del valore stimato, patrimoniale, reddituale, finanziario e del costo del capitale.
>
> | Dimensione | Ottica assets | Ottica equity |
> |---|---|---|
> | Valore stimato | Asset value (enterprise value, EV) | Equity value (capitalizzazione di mercato, MK CAP) |
> | Patrimoniale | CIN rettificato | Capitale proprio rettificato |
> | Reddituale | NOPAT normalizzato | Reddito di bilancio normalizzato |
> | Finanziario | FCFF (indicato anche come FCFO) | FCFE |
> | Costo del capitale | WACC | Costo dell'equity |

L'**enterprise value** è il valore del capitale investito nell'attività operativa. Si scompone nel valore del capitale di rischio, cioè l'**equity value** o capitalizzazione di mercato (MK CAP), e nel valore del debito netto, la **posizione finanziaria netta** (PFN, in inglese net financial position, NFP), che è il debito finanziario al netto della cassa:

$$EV = MK\,CAP + PFN$$

L'equity value è dunque la parte dell'EV di pertinenza degli azionisti: $MK\,CAP = EV - PFN$.

> [!lezione] Dalla lezione del 19 novembre 2026: le grandezze reddituali normalizzate
> Nella riga reddituale della tabella il reddito di bilancio dell'ottica equity è l'ultima riga del conto economico. In entrambe le ottiche la grandezza è normalizzata: la normalizzazione è il lavoro di aggiustamento svolto con la due diligence.

> [!lezione] Dalla lezione del 20 novembre 2026: ottica asset, ottica equity e interessi in gioco
> I dati contabili aiutano fino a un certo punto e non bastano a determinare il valore effettivo dell'impresa, che spesso dipende da aspetti prospettici non riflessi nei bilanci, i quali guardano fondamentalmente al passato. Tutta la reportistica consuntiva guarda indietro, mentre in un'operazione di M&A si guarda in maniera prospettica. Per farlo si devono scegliere grandezze e tassi, e il prospetto di riepilogo serve a orientarsi in questa scelta.
>
> In ottica asset l'azienda è osservata nella sua interezza e nel suo valore complessivo, in ottica equity dal punto di vista di azionisti e soci, e quindi non anche dei creditori. A grandi linee si possono immaginare tre macro grandezze, ciascuna rappresentativa degli interessi dei rispettivi stakeholder: il valore complessivo dell'azienda, che convenzionalmente si chiama enterprise value, è bilanciato dalla somma di due interessi contrapposti, l'equity value, di competenza degli azionisti, e la parte di competenza dei creditori.
>
> Non si tratta di uno stato patrimoniale contabile diviso in tre: il docente richiama l'articolo 2423 del Codice Civile per ricordare che lo stato patrimoniale è a valori di costo, quindi contabili, e non a valori di transazione. L'art. 2423 disciplina la redazione del bilancio; l'iscrizione delle immobilizzazioni al costo di acquisto o di produzione è prevista dall'art. 2426, n. 1, sui criteri di valutazione. In un'ottica di fonti e impieghi il concetto è però assimilabile, perché l'azienda ha un valore nel suo complesso e gli impieghi sono sostenuti da fonti messe dai soci o dai creditori. In un deal siedono di solito al tavolo compratori e venditori, che ragionano sulla parte equity; ci sono poi i creditori, come la banca e gli altri soggetti che hanno pretese di remunerazione.

## Relazione tra enterprise value ed equity value: esempi numerici

Gli esempi seguenti applicano la relazione $EV = MK\,CAP + PFN$ ai tre casi possibili per il segno della PFN. I valori sono in milioni di euro.

> [!lezione] Dalla lezione del 20 novembre 2026: la PFN come variabile di negoziazione, la casa e il mutuo
> Nelle transazioni la parte di debito, cioè la PFN, gioca spesso un ruolo: nel perimetro dell'operazione viene inclusa o esclusa ed è oggetto di negoziazione. Si sente dire "la PFN la teniamo fuori" oppure "la mettiamo dentro", "te la tengo nel prezzo" oppure "te la escludo dal prezzo": questa è la prassi.
>
> L'esempio del docente paragona l'azienda a una casa e la PFN a un mutuo. Il valore della casa raffigurata è sempre lo stesso, ed è il valore concordato per quella transazione, cioè l'enterprise value. Tutto ciò che succede dopo in termini di PFN è un meccanismo di aggiustamento che non riguarda il valore dell'azienda: che la casa abbia pesi, ipoteche, debiti oppure un tesoro all'interno non ne cambia il valore, e l'enterprise value non cambia al variare della PFN.
>
> I casi sono tre. Nel caso A l'azienda è indebitata, cioè ha una PFN positiva e dei creditori. Nel caso B non ha né cassa né debiti, come se avesse un euro in conto: è un caso raro, mostrato solo per completare l'esempio. Nel caso C ha cassa. Di solito ci si trova nel caso A o nel caso C.

### Impresa indebitata (PFN > 0)

> [!example] Esempio
> | Impresa | Enterprise value (EV) | Equity value (MK CAP) | Debito (PFN) |
> |---|---|---|---|
> | Alfa | 60 | 15 | 45 |
> | Beta | 70 | 15 | 55 |
>
> Verifica: per Alfa 15 + 45 = 60, per Beta 15 + 55 = 70. Le due imprese hanno lo stesso equity value. Beta ha una PFN superiore di 10 e un EV superiore di 10: a parità di equity value, l'EV varia in misura pari alla PFN.

> [!lezione] Dalla lezione del 20 novembre 2026: caso A, azienda indebitata
> Si acquista una casa che ha un mutuo sopra. Se l'azienda è valorizzata 100, il prezzo deve tenere conto del fatto che ci si porta dietro un debito: dal giorno dopo occorre iniziare a pagare il mutuo, che nell'esempio ha un capitale residuo di 45. Quando si acquista un'azienda con una PFN positiva, stimata e calcolata dalla due diligence, il debito si scala dal prezzo: l'azienda vale 100, contiene 45 milioni di debiti e il prezzo pagato è quindi 55.
>
> Nello schema compare anche il plusvalore rispetto agli asset contabili, cioè all'attivo di stato patrimoniale. Nell'esempio gli asset contabili sono 60, il totale attivo del bilancio civilistico, che comprende per esempio i cespiti, come un robot ammortizzato al 100% e quindi iscritto a zero. Si parte comunque dal bilancio; poi si fa la valutazione svolta nel corso, con i DCF e i multipli, e si porta il valore della casa a 100. Il fatto che valga 100 non significa però che l'acquirente faccia un bonifico da 100: il meccanismo di aggiustamento si basa sempre sulla PFN, e nel caso A il bonifico è di 55.

### Impresa non indebitata (PFN = 0)

> [!example] Esempio
> | Impresa | Enterprise value (EV) | Equity value (MK CAP) |
> |---|---|---|
> | Gamma | 95 | 95 |
> | Delta | 74 | 74 |
>
> Senza debito, enterprise value ed equity value coincidono.

> [!lezione] Dalla lezione del 20 novembre 2026: caso B, né debiti né liquidità
> Nell'esempio il patrimonio contabile è di nuovo 60 e l'azienda è valorizzata 100. Non ci sono debiti né liquidità, e 100 è quanto concordato. Per avere il 100% delle quote il prezzo è un bonifico di 100: il prezzo pagato corrisponde all'enterprise value quando la PFN non c'è. Il caso è raro.

### Impresa non indebitata con liquidità netta (PFN < 0)

Le imprese Gamma e Delta hanno la stessa attività operativa del caso precedente (immobilizzazioni per 95 e 74) e in più una cassa di 10. La PFN è quindi pari a $-10$.

> [!example] Esempio
> | Impresa | Immobilizzazioni (attivo operativo) | Cassa | PFN | Equity value (MK CAP) | EV = MK CAP + PFN |
> |---|---|---|---|---|---|
> | Gamma | 95 | 10 | -10 | 105 | 95 |
> | Delta | 74 | 10 | -10 | 84 | 74 |
>
> Per Gamma 105 - 10 = 95, per Delta 84 - 10 = 74.

La cassa aumenta di 10 il valore per gli azionisti e lascia invariato l'EV, perché non fa parte del capitale investito nell'attività operativa. Con liquidità netta il passaggio dal valore dell'attivo operativo al valore per gli azionisti somma la cassa anziché sottrarre il debito. Se si chiamasse enterprise value l'intero attivo, cassa compresa (105 per Gamma, 84 per Delta), l'EV coinciderebbe con l'equity value e non rispetterebbe più la relazione $EV = MK\,CAP + PFN$.

> [!lezione] Dalla lezione del 20 novembre 2026: caso C, azienda con liquidità e perimetro della PFN
> Chi acquista una catena di supermercati della grande distribuzione, come Aliper, PAM o Esselunga, trova liquidità, cioè una PFN negativa, se non altro perché queste imprese hanno il ciclo inverso del circolante e quindi un circolante negativo. Il tema sarà ripreso nella parte sul circolante. Chi compra un vasetto di yogurt paga subito, mentre Esselunga paga Danone a 60 giorni: incassa un euro oggi, non ha crediti perché ha incassato dal cliente, e fa il bonifico a Danone dopo 60 giorni. Chi compra Esselunga si trova quindi un'azienda piena di cassa per effetto del business stesso, con conti correnti in attivo e, per esempio, 10 milioni all'interno.
>
> Esselunga vale comunque 100. Chi cede le chiavi di un'azienda in cui c'è un forziere con 10 milioni di euro può però dire: "ti do le chiavi, tu mi dai 100 per l'azienda e poi mi paghi i soldi che ci sono dentro", oppure "li scorporiamo". È il tema che si ritrova sempre nelle negoziazioni: c'è una separazione tra il valore dell'equity e l'enterprise value, e le grandezze si aggiustano tra loro. Se si compra una casa che vale 100 con un forziere da 10 milioni all'interno, il bonifico è di 110, perché i soldi che restano dentro vanno pagati. Entrando nel 100% dell'azienda si ricevono le password dell'home banking e quel denaro diventa a tutti gli effetti proprio, perché si è diventati soci, a meno che il venditore dica "quelli li tiro fuori".
>
> Quando la PFN viene negoziata ed esclusa dal deal ci si trova nel caso B. Il giorno prima di andare dal notaio si lascia di solito una piccola provvista. Se la liquidità è molta, perché l'azienda non ha solo il ciclo inverso del circolante ma fa soldi da vent'anni e ha il bilancio pieno di disponibilità liquide e, come contropartita contabile, di riserve di capitale e di patrimonio, i soci prima di vendere svuotano i due contenitori: fanno una maxi distribuzione di dividendi, svuotano le casse e abbattono la voce riserve, che è in un certo senso fittizia, perché il patrimonio netto non esiste nella realtà. Tengono il minimo necessario per alzare la serranda il giorno dopo e consegnano quello. Il grosso della PFN viene così portato fuori e ci si avvicina molto al caso B.

![](assets/fstr-03/fig01.png)

**Figura 1** — Scomposizione dell'enterprise value in equity value (MK CAP) e posizione finanziaria netta (PFN), con blocchi di altezza proporzionale ai valori in milioni di euro. Con PFN positiva l'EV supera l'equity value della PFN, con PFN nulla i due valori coincidono, con PFN negativa l'EV corrisponde alle sole immobilizzazioni (95 e 74) e l'equity value (105 e 84) lo supera della liquidità netta (10).

> [!lezione] Dalla lezione del 20 novembre 2026: le due domande a cui rispondono enterprise value ed equity value
> L'enterprise value risponde alla domanda su quanto vale il business di quell'azienda a prescindere da come viene finanziato. Ragionando in logica di enterprise value si valuta l'azienda nel suo complesso, senza guardare se dentro ci sia un mutuo o un forziere con i soldi: ci si chiede quanto vale quell'edificio, quella casa rossa. L'equity value risponde a un'altra domanda ed è più un discorso di cash e di regolamento: per diventare azionisti al 100% di quell'azienda, quanto si deve pagare agli attuali soci per acquistare il 100% delle quote, cioè per entrare in possesso dell'equity? Il prezzo da pagare per prendere il 100% delle quote non coincide con il valore dell'azienda.
>
> Il debito rappresenta altre persone, i creditori. Quando c'è la PFN non ci sono solo i soci: gli altri stakeholder determinano l'ammontare della PFN, anche quando questa è una disponibilità presso una banca.
>
> Se si dice che Riello vale 20 milioni, senza chiedersi quanti debiti o quanto equity abbia, quella cifra è il suo enterprise value: l'azienda vale 20 milioni, punto. Se invece si vuole prendere il 100% delle quote, ci si chiede quanto occorre corrispondere per essere azionisti e far parte dell'equity, e si ragiona nella logica dell'equity value.

## Richiami: EBIT, EBITDA e NOPAT

> [!abstract] Definizione
> Il **NOPAT** (Net Operating Profit After Taxes) è l'utile netto operativo, cioè l'EBIT al netto delle imposte. Misura il profitto netto generato dalle attività caratteristiche. Poiché parte dall'EBIT, prima degli oneri finanziari, non dipende dalla struttura finanziaria dell'impresa:
> $$NOPAT = EBIT \times (1 - t_c)$$

L'EBITDA coincide con il margine operativo lordo (MOL). Il conto economico seguente mostra la sequenza dall'EBITDA al reddito netto e il calcolo del NOPAT.

> [!example] Esempio
> | Voce | Valore |
> |---|---|
> | Ricavi | 150.000 |
> | Costo del venduto | -70.000 |
> | **EBITDA** | **80.000** |
> | Ammortamenti | -25.000 |
> | **EBIT** | **55.000** |
> | Oneri finanziari | -10.000 |
> | **EBT** (risultato prima delle imposte) | **45.000** |
> | Imposte (20%) | -9.000 |
> | **Reddito netto** | **36.000** |
>
> $$NOPAT = EBIT \times (1-t_c) = 55.000 \times (1-20\%) = 44.000$$

Il NOPAT (44.000) supera il reddito netto (36.000) di 8.000, pari agli oneri finanziari al netto del risparmio d'imposta: $10.000 \times (1 - 20\%)$.

> [!lezione] Dalla lezione del 20 novembre 2026: dal bilancio al NOPAT
> Per ragionare sulle grandezze dell'azienda si parte dai bilanci, soprattutto se non si lavora in quell'azienda. Se un CFO o un manager di private equity chiede quanto può valere un gruppo, si scarica il bilancio e, prima di tutto, lo si riclassifica. La riclassificazione, con EBIT ed EBITDA, è già stata vista in altri corsi, e dell'EBITDA va ricordato sempre che cos'è, perché è una grandezza chiave.
>
> Associando le grandezze economiche ai vari stakeholder, si vede che i costi remunerano una serie di soggetti. Dopo l'EBIT i creditori vengono remunerati con gli oneri finanziari, perché l'azienda paga gli interessi sul debito, e poi viene pagato lo Stato. L'obiettivo è arrivare a un livello di marginalità da cui si veda in modo molto pulito la redditività di un'azienda che ha già pagato tutti, compreso lo Stato, a esclusione dei soci e dei creditori. Per ottenere una grandezza di flusso assimilabile a cassa occorre un risultato intermedio che non esiste nel conto economico civilistico e di solito nemmeno in quello riclassificato, dove si vedono l'EBIT e, come ultima riga, l'utile o la perdita d'esercizio. Il NOPAT non si legge nel conto economico riclassificato ma va costruito con la formula.
>
> Nella logica reddituale il NOPAT è l'analogo dell'FCFO. In un rendiconto finanziario in ottica asset si arriva a un livello di flussi di cassa subito prima di remunerare, nell'area dei finanziamenti, prima i creditori e poi i soci con i dividendi, e la stessa cosa si vuole riprodurre in un conto economico. Dopo aver pagato i costi operativi e gli ammortamenti si arriva all'EBIT, a 55.000 nell'esempio. Restano da pagare tre soggetti: i creditori con gli oneri finanziari, lo Stato con le imposte e i soci con i dividendi. Si paga lo Stato, così che ne restino due, e ciò che rimane è il NOPAT, che si divide tra creditori e azionisti.
>
> Le imposte del NOPAT sono calcolate sull'EBIT, prima di pagare gli oneri finanziari, e non sono i 9.000 che compaiono nel conto economico dell'esempio. Il NOPAT misura il profitto netto generato dalle attività caratteristiche: pagare gli interessi ai creditori non è un'attività caratteristica, e nemmeno pagare i dividendi, mentre le imposte sul reddito d'esercizio lo sono, perché sono reddito scaturito dall'attività. Il flusso disponibile in un conto economico dopo aver pagato tutti, compreso lo Stato come se fosse un qualsiasi fornitore o dipendente che manda la fattura, è il NOPAT, cioè la versione da conto economico dell'FCFO.

## Esercizio svolto: EBIT e NOPAT dell'azienda Alfa

L'azienda Alfa di questo esercizio è distinta dall'impresa Alfa dell'esempio sull'enterprise value.

> [!example] Esempio
> **Dati.** Fatturato di € 568.000; acquisto di materie prime € 372.000; costo del lavoro € 58.000; affitto dell'immobile produttivo € 43.000; ammortamenti € 12.000; oneri finanziari € 22.000. Il carico fiscale stimato è il 27,9%.
>
> **Richieste.** Calcolare EBITDA e NOPAT, e il reddito netto d'esercizio.
>
> **Conto economico**
>
> | Voce | Valore |
> |---|---|
> | Fatturato | 568.000 |
> | Acquisto materie prime | -372.000 |
> | Costo del lavoro | -58.000 |
> | Affitti | -43.000 |
> | **EBITDA** | **95.000** |
> | Ammortamenti | -12.000 |
> | **EBIT** | **83.000** |
> | Oneri finanziari | -22.000 |
> | **EBT** | **61.000** |
> | Imposte d'esercizio | -17.019 |
> | **Reddito netto** | **43.981** |
>
> **Calcolo del NOPAT**
>
> | Voce | Valore |
> |---|---|
> | EBIT | 83.000 |
> | Imposte sull'EBIT | -23.157 |
> | **NOPAT** | **59.843** |

Le imposte sull'EBIT (23.157, cioè $83.000 \times 27{,}9\%$) differiscono dalle imposte d'esercizio (17.019, cioè $61.000 \times 27{,}9\%$) perché è diversa la base imponibile a cui si applica l'aliquota: l'EBIT nel primo caso, l'EBT nel secondo. La differenza, 6.138, è il risparmio d'imposta sugli oneri finanziari ($22.000 \times 27{,}9\%$), detto scudo fiscale. Ne segue il raccordo tra NOPAT e reddito netto: $59.843 - 22.000 + 6.138 = 43.981$.

> [!lezione] Dalla lezione del 20 novembre 2026: perché il NOPAT interessa nei DCF
> Ci si può chiedere perché si spieghi il NOPAT se la valutazione è fatta con i multipli dell'EBITDA. Questo modulo riguarda i DCF e non i multipli: con il NOPAT non si calcola il multiplo di qualcosa, si sta capendo come funzionano i flussi di cassa attualizzati. Il NOPAT è un'approssimazione di un flusso di cassa ricavata dal conto economico. Il conto economico non sempre dà un flusso di cassa affidabile e il NOPAT è una grossa approssimazione, ma è la grandezza più simile a un flusso di cassa che il conto economico offra.
>
> Con il metodo dei multipli dell'EBITDA ci si può fermare tranquillamente all'EBITDA. L'EBITDA invece non si prende come flusso di cassa, perché il metodo DCF muove nel tempo flussi di cassa e non avrebbe senso muovere nel tempo l'EBITDA: mancano ancora gli ammortamenti e le imposte, quindi non è rappresentativo. Ciò che idealmente si può chiamare flusso di cassa è il NOPAT.
>
> Il docente avverte che negli esercizi del compito su questo tema capita che chi va di fretta calcoli il NOPAT usando le imposte del conto economico (17.019 nell'esercizio svolto). Le imposte vanno sempre calcolate sull'EBIT, non prese dal conto economico, perché la base imponibile non è la stessa.

## Richiami: capitale investito netto e capitale circolante netto

Lo stato patrimoniale riclassificato in ottica finanziaria contrappone al capitale investito netto le fonti di finanziamento:

| Capitale investito netto | Fonti di finanziamento |
|---|---|
| Capitale circolante netto (CCN) | Patrimonio netto (equity) |
| Capitale immobilizzato netto | Posizione finanziaria netta (PFN, debt) |

> [!abstract] Definizione
> Il **capitale investito netto operativo** (CIN) è la somma del capitale circolante commerciale (CCN) e delle immobilizzazioni caratteristiche nette:
> $$CIN = CCN + \text{Immobilizzazioni caratteristiche nette}$$

Le due colonne hanno per costruzione lo stesso totale, quindi $CIN = \text{Patrimonio netto} + PFN$. Nelle formule successive il capitale investito netto operativo è indicato con CINO, il capitale circolante netto operativo con CCNO e il patrimonio netto (capitale proprio) con C.P.

> [!lezione] Dalla lezione del 20 novembre 2026: capitale circolante commerciale e capitale circolante netto
> Per calcolare il CCN occorre stabilire quali voci contiene. Le prime sono le rimanenze, poi i crediti e i debiti operativi, quindi praticamente tutti, compresi i crediti tributari e i ratei e risconti, che devono comunque essere collocati da qualche parte nel patrimonio.
>
> Del capitale circolante esistono due versioni, il CCC e il CCN: a volte si trova scritto capitale circolante commerciale, a volte capitale circolante netto. Il capitale circolante commerciale comprende crediti verso clienti, debiti verso fornitori e rimanenze. Restano però altre poste dello stato patrimoniale: il TFR, i ratei e risconti, i crediti e debiti tributari, i debiti previdenziali, gli altri crediti, gli acconti. Non sono immobilizzazioni, non sono equity e non sono PFN, quindi per differenza vanno nel capitale circolante, che a quel punto si chiama CCN, cioè netto anche di tutte queste altre voci.

## La valutazione assoluta (DCF)

La **valutazione assoluta** si concentra sull'impresa. Poggia sull'analisi delle sue caratteristiche (modello di business, strategie, management, patrimonio e così via) e sulla previsione delle performance economico-finanziarie future. Considera le sue politiche finanziarie, di finanziamento e di dividendo, e misura il suo rischio operativo e finanziario. Si basa su un criterio analitico di stima.

Il risultato è un insieme di **valori finanziari**, detti anche valori fondamentali o **valori intrinseci**. Hanno significato economico perché fondati sul principio di convenienza economica dell'investimento in capitale di rischio aziendale.

Per rischio operativo si intende il rischio di perdite derivanti da fallimenti o inadeguatezza dei processi interni, delle risorse umane e dei sistemi tecnologici, oppure da eventi esterni. Il rischio finanziario incide sulla liquidità aziendale ed è legato all'equilibrio tra flussi monetari in entrata e in uscita.

> [!lezione] Dalla lezione del 19 novembre 2026: punti di forza e limiti del DCF
> Nei DCF il valore dell'azienda dipende dalla sua capacità di generare flussi di cassa in futuro, attualizzati a un certo tasso. Per questo sono stati svolti tutti gli esercizi sul VAN: il principio è identico. Il VAN si usa per un investimento e lo stesso concetto si usa per un'azienda, immaginando che il progetto sia l'azienda stessa. I punti di forza sono due: il metodo permette di ragionare sulla capacità prospettica di generare risorse e di stimare sia i flussi di cassa attesi sia il rischio associato.
>
> Se il DCF fosse il metodo perfetto sarebbe l'unico usato per valutare le aziende. Ha invece controindicazioni, la prima delle quali è che occorre prevedere il futuro, una forte assunzione: il metodo valuta i flussi di cassa prospettici e li attualizza a oggi, ma nessuno garantisce che i flussi saranno quelli. I flussi sono inoltre specifici di quell'azienda, ed è un'altra caratteristica dei DCF: guardano l'azienda e non il settore.
>
> Se i flussi di cassa stimati non sono attendibili si costruisce un castello di carte. Se si sbaglia la previsione e si usano formule di matematica finanziaria come la rendita perpetua, la valutazione che ne risulta, portata a una trattativa con un dealer, non è credibile, perché proietta per milioni di euro flussi di cassa che non lo sono. Alla base dei DCF c'è quindi un ragionamento molto delicato: i flussi di cassa devono essere sostenibili e credibili.

Un esempio di rendiconto finanziario di un'impresa reale è quello consolidato di Brembo, in migliaia di euro, per gli esercizi chiusi al 31 dicembre 2020 e 2019.

| Voce | 31.12.2020 | 31.12.2019 |
|---|---|---|
| **Disponibilità liquide e mezzi equivalenti all'inizio del periodo** | **168.559** | **195.871** |
| Risultato prima delle imposte | 156.044 | 307.691 |
| Ammortamenti/Svalutazioni | 207.550 | 196.630 |
| Plusvalenze/Minusvalenze | -1.695 | -2.157 |
| Proventi e oneri da partecipazioni al netto dei dividendi ricevuti | -413 | -3.984 |
| Componente finanziaria dei fondi a benefici definiti e debiti per il personale | 407 | 577 |
| Accantonamenti a fondi relativi al personale | 2.423 | 2.502 |
| Altri accantonamenti ai fondi al netto degli utilizzi | 48.618 | -52 |
| Risultato derivante da attività operative cessate | -304 | -6.422 |
| **Flusso monetario generato dalla gestione reddituale** | **412.630** | **494.785** |
| Imposte correnti pagate | -48.873 | -65.961 |
| Utilizzi dei fondi relativi al personale | -4.580 | -4.813 |
| *(Aumento) diminuzione delle attività a breve:* | | |
| rimanenze | -23.913 | -7.604 |
| attività finanziarie | 136 | -5 |
| crediti commerciali | 4.387 | 14.558 |
| crediti verso altri e altre attività | -9.175 | -6.306 |
| *Aumento (diminuzione) delle passività a breve:* | | |
| debiti commerciali | 910 | -90.846 |
| debiti verso altri e altre passività | 18.382 | -26.374 |
| Effetto delle variazioni dei cambi sul capitale circolante | -16.503 | -814 |
| **Flusso monetario netto generato/(assorbito) da attività operativa** | **333.401** | **306.620** |
| *Investimenti in immobilizzazioni:* | | |
| materiali | -162.052 | -213.657 |
| di cui diritto di utilizzo beni in leasing | -37.755 | -38.165 |
| immateriali | -28.273 | -38.111 |
| finanziarie | -182.862 | -131 |
| Prezzo di realizzo, o valore di rimborso, di immobilizzazioni | 4.205 | 6.589 |
| **Flusso monetario netto generato/(assorbito) da attività di investimento** | **-368.982** | **-245.310** |
| Dividendi pagati nel periodo | 0 | -71.541 |
| Acquisto azioni proprie | 0 | -11.329 |
| Dividendi pagati nel periodo ad azionisti di minoranza | -640 | -800 |
| Variazione di fair value di strumenti derivati | 648 | -1.920 |
| Nuovi contratti per beni in leasing | 35.616 | 38.167 |
| Rimborso passività per beni in leasing | -24.826 | -24.436 |
| Mutui e finanziamenti assunti nel periodo da banche e altri finanziatori | 425.000 | 103.518 |
| Rimborso di mutui e finanziamenti a lungo termine | -122.492 | -120.205 |
| **Flusso monetario netto generato/(assorbito) da attività di finanziamento** | **313.306** | **-88.546** |
| **Flusso monetario complessivo** | **277.725** | **-27.236** |
| Effetto delle variazioni dei cambi sulle disponibilità liquide e mezzi equivalenti | -1.054 | -76 |
| **Disponibilità liquide e mezzi equivalenti alla fine del periodo** | **445.230** | **168.559** |

Il flusso monetario complessivo è la somma dei flussi dell'attività operativa, di investimento e di finanziamento: nel 2020, $333.401 - 368.982 + 313.306 = 277.725$. Aggiungendo questo flusso e l'effetto dei cambi (-1.054) alla liquidità iniziale (168.559) si ottiene la liquidità finale di 445.230.

## La valutazione relativa (multipli)

> [!abstract] Definizione
> La valutazione relativa esprime un **valore relativo** dell'impresa, fondato sul confronto con imprese simili (*comparables*). Richiede l'applicazione di moltiplicatori, i **multipli di mercato**, ricavati dai prezzi che il mercato segna per i comparables, e conduce a **valori di mercato**, detti anche **prezzi probabili**.
>
> I multipli di mercato sono rapporti tra il prezzo di mercato (quotazione) di uno strumento azionario e una data grandezza di bilancio.

> [!lezione] Dalla lezione del 20 novembre 2026: valutazione assoluta e valutazione relativa a confronto
> La valutazione con i DCF si chiama assoluta per distinguersi da quella con i multipli, che si chiama relativa. Il DCF è assoluto perché ci si focalizza in modo assoluto su quella sola azienda, con un criterio analitico di stima: si va dentro l'azienda, senza prendere parametri esterni o indicatori, partendo dai bilanci e dai business plan. Il metodo dei multipli è relativo perché mette in relazione: i multipli sono multipli di altre aziende, quindi l'azienda da valutare viene messa in relazione con altre. Cambia il sistema di osservazione, ed è per questo che i due metodi si usano insieme. Con i multipli si apre la finestra e si guarda fuori, ai multipli che ci sono in giro; con il DCF si resta dentro e si guarda quanta cassa sta facendo l'azienda, o quanta ne farà.
>
> Per sapere quanto vale Brembo con i DCF si prende ciò che l'azienda pubblica, cioè il rendiconto finanziario consolidato, come per De'Longhi e per Enel. Per valutare Brembo con i multipli non si guarda invece il rendiconto finanziario di Brembo S.p.A.: si compara l'azienda con aziende simili, i comparables, e si applicano i multipli di mercato, che sono rapporti e fanno riferimento alle quotazioni in borsa. La valutazione che ne risulta è a valori di mercato, detti anche prezzi probabili. Il DCF porta invece a valori finanziari, detti fondamentali o intrinseci.
>
> Il docente indica come possibile domanda a risposta multipla "il metodo DCF porta a valori di mercato, vero o falso?". La risposta è falso: il DCF porta a valori finanziari, detti anche fondamentali, mentre il metodo dei multipli porta a valori di mercato.

### Esempio: individuazione dei comparables nel settore automotive

Il primo passo è scegliere le imprese confrontabili. Partendo da Brembo, si considerano quattro imprese del settore automotive e se ne confrontano sede, dimensione e valutazione.

> [!example] Esempio
> | Azienda | Attività | Sede principale | Dipendenti | Valutazione (USD) |
> |---|---|---|---|---|
> | Brembo | Tecnologie di freni a disco per veicoli | Stezzano (IT) | 10.868 (+3%) | 3,5 miliardi |
> | Kongsberg Automotive | Sviluppo, produzione e vendita di prodotti per l'industria automotive | Zurigo (CH) | 11.234 (+3%) | 265,9 milioni |
> | Ford Otosan | Produzione, assemblaggio, importazione, esportazione e vendita di veicoli a motore e ricambi in Turchia | Istanbul (TR) | 14.145 | n.d. |
> | Subaru | Gruppo con attività automotive e aerospaziali (già Fuji Heavy Industries) | Tokyo (JP) | 36.910 | 13,2 miliardi |
> | BorgWarner | Soluzioni tecnologiche per veicoli a combustione, ibridi ed elettrici | Auburn Hills (US) | 49.300 (-1%) | 9,2 miliardi |

### Esempio: P/E e P/BV di Brembo, Sogefi e Valeo

Si considerano poi come comparables di Brembo due società della componentistica automotive, Sogefi e Valeo, e si confrontano due multipli: il P/E (prezzo su utili) e il P/BV (prezzo su valore contabile del patrimonio netto).

> [!example] Esempio
> | Azienda | P/E | P/BV |
> |---|---|---|
> | Brembo | 16,48 | 2,02 |
> | Sogefi | 51,53 | 0,54 |
> | Valeo | 22,99 | 1,09 |

Brembo ha il P/E più basso del gruppo (16,48 contro 51,53 e 22,99) e il P/BV più alto (2,02 contro 0,54 e 1,09). I multipli di imprese dello stesso settore possono quindi differire molto, e in senso opposto a seconda del multiplo considerato.

### Esempio: multiplo dell'EBITDA nel settore alimentare

> [!example] Esempio
> Il multiplo dell'EBITDA è il rapporto tra capitalizzazione ed EBITDA. Importi in migliaia di euro.
>
> | Azienda | Capitalizzazione | EBITDA | Multiplo EBITDA |
> |---|---|---|---|
> | Conagra Foods Inc. | 17.383.003 | 1.391.339 | 12,49 |
> | General Mills Inc. | 35.364.038 | 2.999.013 | 11,79 |
> | Kellogg Co. | 24.665.300 | 2.319.281 | 10,63 |
> | Marr S.p.A. | 1.269.299 | 105.674 | 12,01 |
> | Tyson Foods Inc. | 19.542.863 | 2.479.693 | 7,88 |
>
> Il valore medio del multiplo nel gruppo è $(12{,}49 + 11{,}79 + 10{,}63 + 12{,}01 + 7{,}88)/5 = 10{,}96$.

![](assets/fstr-03/fig02.png)

**Figura 2** — Multiplo EBITDA nel settore alimentare: i valori vanno da 7,88 (Tyson Foods) a 12,49 (Conagra Foods), con media semplice 10,96. Kellogg e Tyson Foods si collocano sotto la media, le altre tre società sopra.

Moltiplicando il multiplo (per esempio la media del gruppo) per l'EBITDA dell'impresa da valutare si ottiene una stima del suo valore per analogia con i comparables. In senso stretto, il numeratore dei multipli della tabella è la capitalizzazione di mercato, mentre l'EBITDA è un margine calcolato prima degli oneri finanziari: un rapporto coerente con l'EBITDA avrebbe al numeratore l'enterprise value (multiplo EV/EBITDA). Il tema è ripreso in [[FSTR 06 Multipli di Borsa lez01|l'ottica assets e l'ottica equity nei multipli]].

> [!lezione] Dalla lezione del 20 novembre 2026: il multiplo dell'EBITDA, un calcolo semplice con un lavoro difficile a monte
> L'applicazione del metodo del multiplo è un'operazione matematica elementare: moltiplicare un EBITDA per 3,2 lo sa fare anche un bambino. La difficoltà non sta nella formula, ma nel trovare un multiplo rappresentativo e un EBITDA da moltiplicare altrettanto rappresentativo. Per questo ci si impegna sull'EBITDA, facendo la due diligence e lavorandolo fino a normalizzarlo: è il primo elemento del prodotto. Il secondo è il multiplo, che va trovato giusto, il più appropriato.
>
> Il docente fa un inciso fuori dal libro: il multiplo dell'EBITDA è il più in voga, ma è molto approssimativo e non viene mai usato da solo. Se si chiede agli advisor quanto vale un'azienda con un EBITDA di un milione, la risposta può essere che nel fashion il multiplo è 8, quindi 8 milioni. Non è così: quando con l'avvocato si scrive il contratto di compravendita dell'azienda non si moltiplica l'EBITDA per 8. Questa è la narrazione da bar o da convegno M&A. Nelle valutazioni effettive ci si impegna a fondo su quanto sia l'EBITDA e su quanto sia il multiplo, e il metodo è sempre accompagnato da altri metodi: non c'è una trattativa siglata e firmata sul solo multiplo dell'EBITDA, perché è rappresentativo ma troppo approssimativo e non abbastanza dettagliato.
>
> Il multiplo dà comunque un'idea in chiave prospettica. Se Brembo ha un EBITDA di 10 milioni e le imprese comparabili, che operano nella stessa arena competitiva sui sistemi frenanti, hanno prospettive di sviluppo pari a 4,5 volte, allora, essendo allineata ai suoi comparables, anche Brembo potrebbe avere una prospettiva di 4,5.

> [!lezione] Dalla lezione del 20 novembre 2026: altri multipli oltre all'EBITDA
> Ai multipli saranno dedicate un paio di lezioni, perché quello dell'EBITDA è uno tra moltissimi e si prendono sempre i comparables con alcuni multipli. Per aziende molto pesanti dal punto di vista dei costi fissi l'EBITDA può non essere il multiplo più appropriato, dato che non tiene conto degli ammortamenti. Un'azienda come Ilva, che vive di altiforni, se usa un multiplo senza ammortamenti non rappresenta il capitale investito dell'azienda e si perde un grosso pezzo. Il multiplo dell'EBITDA si può usare per un'azienda che non si basa tutta su un altoforno o sullo sfruttamento di una miniera.
>
> Per un'azienda come Zara, che macina fatturato sui volumi di vendita, il focus dovrebbe andare più sulle vendite che sulla redditività netta dell'EBITDA, cioè sulla capacità potenziale di sviluppare vendite. Servono quindi multipli ancorati alle sales e non agli ammortamenti: Zara ha i negozi in affitto e quindi, secondo il docente, ammortamenti quasi nulli, mentre ha personale, magazzino, utenze e pubblicità. Gli ammortamenti non sono rilevanti se la rete è in affitto. Il multiplo dell'EBITDA è quello di cui si parla di più, ma non è l'unico né l'unico usato.

> [!lezione] Dalla lezione del 20 novembre 2026: la comparabilità, l'esempio dei cinque operatori del food
> Si compara sempre. Nelle tavole di confronto compaiono spesso aziende quotate, per le quali c'è molto più materiale disponibile, e sono sempre messe in relazione: per questo si parla di valutazione relativa. Nella tavola dei cinque operatori del food occorre decidere quale multiplo prendere, per esempio quello di Kellogg's o quello di General Mills, e c'è un lavoro da fare sul multiplo, perché non se ne trova uno solo: scavando si trova una valanga di comparables, tutti diversi.
>
> Sono aziende americane. Se l'azienda da valutare produce cereali ed è di Padova, il docente richiama Cereal Docks, azienda veneta, grande operatore dei derivati dei cereali, le cui performance in termini di EBITDA sono influenzate dal sistema Italia. Cinque aziende americane sono comparables perché fanno cereali, ma occorre chiedersi come li fanno: negli Stati Uniti il costo del personale può essere totalmente diverso, e anche il mercato finale è diverso, perché Cereal Docks esporta tutto mentre lì c'è consumo interno. Ha senso proiettare le stesse prospettive di crescita di cinque aziende americane su un'azienda padovana? Significherebbe prendere il multiplo di Kellogg's e applicarlo a quell'azienda. Questi ragionamenti si faranno nella parte sui multipli.

## Valutazione assoluta e valutazione relativa: un approccio complementare

Sul piano professionale si ritiene oggi più corretto associare le valutazioni assolute e relative. Il ricorso ai multipli in senso **complementare** serve a individuare le **leve del valore** e le **leve di prezzo** (variabili di contesto) che guidano i prezzi del mercato finanziario, e a coprire meglio lo spettro delle informazioni rilevanti per la valutazione.

> [!lezione] Dalla lezione del 19 novembre 2026: il patrimonio netto rettificato come terzo metodo
> I metodi per valutare un'azienda trattati nel corso sono due: i DCF e i multipli dell'EBITDA. Un terzo metodo, che il libro non riporta e che nella prassi alcuni usano, talvolta come confronto, è il patrimonio netto rettificato; ne parlerà anche il team di KPMG. Può essere utile a chi lavora nella consulenza o si cimenta in un deal.
>
> I multipli dell'EBITDA e i DCF si basano sulle prospettive di guadagno e di reddito dell'azienda: o su dati esterni, cioè i multipli, o sui flussi di cassa generati dall'azienda. In entrambi i casi non si guarda il patrimonio, cioè non si guarda dentro il capannone. Non ci si accorge, per esempio, se un'azienda taglia la lamiera di acciaio con una taglierina azionata da un operaio oppure con un robot laser di ultima generazione, pagato un milione di euro e con intelligenza artificiale integrata, che taglia cento sagome al minuto. Nei DCF e nei multipli non ci si rende conto di questo aspetto e del valore di mercato di alcuni asset importanti. Il bilancio dice ancora meno: il braccio robotizzato viene probabilmente ammortizzato secondo le tabelle fiscali con un'aliquota del 25%, quindi in quattro anni il robot da un milione di euro arriva a zero, mentre può tagliare per altri dieci anni. Dire all'imprenditore che ha speso un milione per quel robot che dopo quattro anni gli si dà zero, perché a bilancio c'è scritto zero e tutto è ammortizzato, non è accettabile.
>
> Si tratta del disallineamento tra il valore netto contabile, calcolato con i principi contabili, e un valore di mercato, di recupero o di realizzo. Per questo un aspetto della valutazione d'azienda consiste nel rettificare il patrimonio, cioè ricondurlo a valori di mercato, soprattutto per le immobilizzazioni. Un fabbricato iscritto a bilancio al costo storico, cioè al costo di acquisto, vale poco ma potrebbe essersi apprezzato nel tempo. Lo stesso accade con le location dei negozi, con le aree rivalutate col tempo, con le città turistiche, con le zone dove c'è stata una riqualificazione residenziale o dove ora passa la metropolitana e prima non passava.
>
> Il docente porta l'esempio della zona di Milano intorno a Porta Garibaldi e a piazza Gae Aulenti, dove si trovano la Torre Unicredit e il Bosco Verticale. Di fianco ci sono le case ringhiera, casette milanesi di mattoni con il cortile interno e il ballatoio con la ringhiera, che prima della costruzione di quei palazzi, in una zona malfamata, non valevano niente. Oggi un appartamento in affitto al Bosco Verticale costa circa 15.000 euro al mese, e le case ringhiera accanto potrebbero essersi apprezzate un poco. Si supponga che la sede legale di un'azienda e i suoi uffici siano in una casa ringhiera di Milano: a bilancio quell'edificio oggi probabilmente non vale quasi niente: se è stato ammortizzato al 3%, in dieci anni si è ridotto del 30%. Chi compra da un'azienda che vende un fabbricato accanto al Bosco Verticale non se lo vedrà vendere al costo d'acquisto. Nei multipli dell'EBITDA e nei DCF non si considera quanto può valere la sede accanto al Bosco Verticale, in un edificio comprato vent'anni prima a 300.000 euro e che ora vale 3 milioni: nessuno lo venderebbe a 300.000 euro, al valore di libro del bilancio.
>
> Il terzo metodo consiste nel fare una ricognizione degli asset aziendali e nello stimare, tramite perizie giurate di periti, quanto valgono i beni dell'azienda a valore commerciale, soprattutto gli immobili.

## I metodi DCF: formule generali

> [!abstract] Definizione
> Le formule generali dei metodi DCF dipendono dall'ottica di valutazione.
>
> Ottica assets (il valore dell'attività operativa è la somma dei FCFF attualizzati al WACC):
> $$V = \sum_{t=1}^{\infty} \frac{FCFF_t}{(1 + WACC)^t}$$
>
> Ottica equity (il valore del capitale proprio è la somma dei FCFE attualizzati al costo dell'equity):
> $$E = \sum_{t=1}^{\infty} \frac{FCFE_t}{(1 + r_E)^t}$$
>
> I due valori sono legati da
> $$E = V - D$$
> dove $D$ è il valore del debito finanziario netto (PFN).

Per poter usare tassi di sconto stabili, WACC e $r_E$ costanti nel tempo, i metodi assumono la costanza nel tempo del rischio operativo e del rischio finanziario.

> [!lezione] Dalla lezione del 20 novembre 2026: quale flusso e quale tasso per la valutazione assoluta
> Il costo del capitale è stato oggetto dell'intera lezione precedente e serve perché nelle formule dei DCF va inserito un tasso: il WACC oppure $r_E$.
>
> Per trovare il valore complessivo dell'azienda si possono prendere i flussi di cassa che residuano immediatamente prima di remunerare creditori e soci. Nel rendiconto finanziario l'FCFF, o FCFO, è il flusso dopo aver remunerato tutti, compresi gli investimenti e l'area tributaria: resta solo l'area finanziaria, cioè rimborso e accensione di finanziamenti, interessi e dividendi, quindi creditori e soci. L'FCFF è il flusso adatto, perché idealmente è quello che interessa a creditori e azionisti. Se si chiedesse a un potenziale creditore o a un potenziale azionista quale flusso guarderebbe per proiettarlo negli anni, risponderebbe che guarderebbe il flusso che l'azienda sarebbe disposta a dare a lui; chiesto congiuntamente a un azionista e a un creditore, direbbero all'unisono: il flusso per noi.
>
> Il tasso più appropriato per attualizzare un flusso di pertinenza sia dei creditori sia degli azionisti, cioè sia del debito sia dell'equity, è il WACC. La formula è compatta: non c'è uno sviluppo di flussi, è una sorta di rendita perpetua che va da uno all'infinito, molto veloce da applicare. Ci si chiede quanto vale l'azienda in base a quanto è in grado di dare ai creditori e agli azionisti nel loro complesso: l'FCFF, attualizzato al tasso che rappresenta le aspettative di entrambi e proiettato nel tempo, dà l'enterprise value, cioè il valore dell'azienda a beneficio di tutti.
>
> Se si restringe il focus agli azionisti, ci si chiede che cosa arrivi a loro nel rendiconto finanziario, cioè l'FCFE. I creditori vengono pagati prima, nell'area finanziaria, e l'FCFE è l'ultima riga del rendiconto finanziario, l'ultima fettina di flusso di cassa che residua per gli azionisti, la cui aspettativa è il tasso $r_E$. Il valore dell'equity per i soci si ottiene applicando una formula di rendita perpetua che proietta all'infinito il loro flusso.
>
> Il limite di questo approccio è che si scontra con la realtà: chi ha detto che l'FCF sarà lo stesso per i prossimi mille anni? Si prende l'FCF del 2025 dal bilancio depositato, si prende il tasso $r_E$ e si afferma che quell'azienda vale tanto, ma non c'è alcuna ragione per ritenere che il flusso resti uguale. Si scoprono così le carte anche sui DCF: non sono un metodo attendibile solo perché usano i flussi di cassa.

## I flussi finanziari di riferimento: dal MOL a FCFF e FCFE

Il flusso di cassa rilevante per le valutazioni aziendali si costruisce a cascata a partire dal MOL e attraversa cinque aree: gestione corrente, investimenti, straordinaria, capitale di terzi e capitale proprio.

> [!abstract] Definizione
> | Area | Voce | Flusso intermedio |
> |---|---|---|
> | Gestione corrente | MOL | |
> | | - Variazione CCNO | |
> | | | **Cash flow gestionale lordo** |
> | | - Flusso fiscale operativo (imposte + scudi - variazione dei debiti per imposte) | |
> | | | **Cash flow gestionale netto** |
> | Investimenti | -/+ Investimenti/disinvestimenti in capitale fisso | |
> | | | **Free cash flow to the firm (FCFF)** |
> | Straordinaria | +/- Proventi/oneri straordinari | |
> | Capitale di terzi | - Oneri finanziari netti | |
> | | + Scudo fiscale sugli oneri finanziari | |
> | | +/- Aumento/riduzione dei debiti finanziari | |
> | Capitale proprio | | **Free cash flow to equity (FCFE)** |

Il FCFF è il flusso disponibile per tutti i finanziatori, equity e debito. Il FCFE è il flusso residuo che spetta ai soli azionisti, dopo la gestione straordinaria, gli oneri finanziari al netto dello scudo fiscale e la variazione dei debiti finanziari.

> [!lezione] Dalla lezione del 20 novembre 2026: i nomi dei flussi nei rendiconti finanziari
> Nel libro si parla di FCGC, flusso di cassa della gestione caratteristica. Il docente non si focalizza sulle lettere e non ha corretto la slide volutamente, per creare un po' di confusione: scaricando dieci bilanci di società quotate con dieci rendiconti finanziari si trovano dieci nomi diversi di questi flussi, tra cui flusso di cassa delle attività operative, flusso di cassa della gestione caratteristica e free cash flow operativo. Il motivo è che il legislatore, nell'OIC sul rendiconto finanziario, ha dato indicazioni di massima sullo schema ma non i nomi, a differenza dello stato patrimoniale civilistico, con le lettere maiuscole e i numeri romani. Nel rendiconto finanziario ognuno lo compila come gli piace.
>
> Al di là del nome, il flusso di interesse è quello prima di remunerare il capitale di terzi e il capitale proprio. Possono esserci oneri straordinari, che qui si trascurano; con i nuovi principi contabili è una voce diventata residuale. In qualsiasi rendiconto, scaricato da AIDA o di una quotata, occorre prendere ciò che residua e dargli un nome qualsiasi, FCF, FCFO, FCGC, chiedendosi che cosa manchi da togliere: l'area del capitale di terzi e l'area dei soci, cioè i dividendi.
>
> L'FCFE è sempre il flusso che residua dopo tutti, perché gli azionisti si prendono i soldi dopo che tutti gli altri sono stati pagati. L'FCFF, o FCFO, è il flusso prima di remunerare i creditori. Nell'area dei finanziamenti ci sono l'aumento o la diminuzione dei debiti finanziari e gli interessi pagati: se si rimborsano finanziamenti e si pagano interessi i debiti finanziari si riducono, se ci si indebita entrano soldi, e trattandosi di flussi possono essere entrate o uscite. Nelle formule interessa poi un elemento con segno più, lo scudo fiscale, che non si trova nei rendiconti finanziari perché non è una voce da valorizzare ma che in ottica M&A conta: rappresenta un risparmio di denaro ed è legato all'area dell'indebitamento.

## I metodi DCF: modelli sintetici e modelli analitici

> [!abstract] Definizione
> | Modello sintetico | Modello analitico |
> |---|---|
> | Il valore degli assets o dell'equity si ottiene con **formule compatte**, che prevedono per esempio flussi costanti oppure flussi che crescono a un tasso costante. | Il valore degli assets o dell'equity si ottiene come somma di un **valore frutto di un piano esplicito** (3-7 anni) e di un **terminal value** attualizzato, calcolato con un metodo sintetico. |

Di norma si utilizza il metodo analitico. Il suo vantaggio rispetto ai metodi sintetici emerge nei periodi di discontinuità, per esempio grandi investimenti pluriennali o abbattimento del debito: in queste fasi i flussi non sono né costanti né crescenti a tasso costante, e solo un piano esplicito può rappresentarli. Il terminal value del metodo analitico è a sua volta ottenuto con un modello sintetico, come quelli illustrati di seguito. Il metodo analitico è trattato in [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|i metodi DCF analitici]] e il terminal value in [[FSTR 05 Annotazioni sul Terminal Value|le annotazioni sul terminal value]].

> [!lezione] Dalla lezione del 19 novembre 2026: il business plan nei DCF e i due modi di applicarli
> Come suggerisce la slide, per stimare i flussi ci si aiuta con un business plan: si incarica un esperto che guardi avanti, come minimo, per tre o quattro anni, cioè che navighi a vista per quel periodo. Chi applica i DCF attualizza a oggi tutti i flussi di cassa che l'azienda farà da qui alla fine dei tempi, per comprarla: almeno si verifichi quanta cassa farà nei prossimi quattro anni. In questo modo non serve forzare le formule, perché ci si arriva costruendo con un business plan uno sviluppo di crescita del business.
>
> Dove possibile si usa un business plan ottenuto con una simulazione informatica o chiedendo a tutte le aree aziendali di proiettare ricavi, costi e così via, per proiettare il business in modo abbastanza certo. Dal quinto anno in poi ci si deve affidare a conteggi che derivano dai bilanci, con tutte le incertezze del caso.
>
> Uno dei due modi di maneggiare il metodo dei DCF è spacchettare in due il valore futuro dell'azienda: fin dove si riesce a navigare a vista con un business plan si attualizzano quei flussi, poi si usa una formula perpetua. L'alternativa è partire da oggi e assumere che l'azienda faccia da oggi all'infinito lo stesso cash flow, attualizzare tutto a oggi e dire che l'azienda vale quella cifra.

> [!lezione] Dalla lezione del 20 novembre 2026: modello sintetico e modello analitico, il piano e il terminal value
> Con il metodo DCF si maneggiano flussi di cassa e le strade sono due. La prima usa formule compatte come quelle viste, un po' approssimative perché hanno la forma della rendita perpetua: è il modello sintetico. Il valore degli asset o dell'equity si ottiene con una formula compatta che ipotizza tendenzialmente flussi costanti. Se si inserisce un tasso di crescita il margine di manovra è limitato, perché la formula è una sola e la crescita viene ipotizzata sempre in avanti.
>
> Il metodo analitico contiene due formule: il valore dell'azienda è dato da due addendi, il valore frutto di un piano e il terminal value. È più analitico perché ci si immagina di avere un cannocchiale per prevedere il futuro con i flussi di cassa; in pratica non viene dato un cannocchiale ma un business plan, e un business plan a sette anni ha poco valore, perché con l'incertezza geopolitica è molto azzardato. Con un business plan sotto mano si può però fotografare il rendiconto finanziario previsionale: per esempio, se si ricevesse il business plan di Brembo e il rendiconto dell'ultimo bilancio fosse quello del 2025, ci sarebbero le colonne 2026, 2027, 2028 e 2029 o 2030. Si hanno così cinque flussi di cassa, cinque FCFO da usare, come negli esercizi sui progetti di investimento in cui venivano forniti quattro o cinque anni di flusso. Questi flussi sono ragionevolmente certi, perché stimati all'euro dagli analisti o dall'azienda.
>
> Il valore totale è la somma di due componenti, la prima delle quali è il frutto del piano. Al quinto o sesto anno il business plan finisce e non si hanno più dati, quindi si ipotizza una proiezione fino alla fine della vita dell'azienda, che si chiama terminal value: è il pezzo che lancia dalla fine del business plan verso il futuro. Tutto ciò che viene dopo, insieme al business plan, va riportato al tempo zero, come negli esercizi sui progetti di investimento. Le formule della settimana precedente servono a dare familiarità nel prendere i valori di un business plan e del terminal value e ricondurli tutti al momento zero.

## FCFF e FCFE in steady state e in steady growth

Le formule generali del flusso di cassa si semplificano sotto due ipotesi limite: i flussi costanti nel tempo (steady state) e i flussi che crescono a un tasso costante $g$ (steady growth).

### Steady state

> [!abstract] Definizione
> | Formula generale | Steady state |
> |---|---|
> | MOL | MOL |
> | - Variazione CCNO | 0 (variazione nulla) |
> | Cash flow gestionale lordo | → MOL |
> | - Flusso fiscale operativo | - Imposte operative |
> | Cash flow gestionale netto | → MOL netto |
> | -/+ Investimenti/disinvestimenti in capitale fisso | -/+ Ammortamenti |
> | Free cash flow to the firm (FCFF) | → **NOPAT** |
> | +/- Proventi/oneri straordinari | +/- Proventi/oneri straordinari |
> | - Oneri finanziari netti | - Oneri finanziari netti |
> | + Scudo fiscale sugli oneri finanziari | + Scudo fiscale sugli oneri finanziari |
> | +/- Aumento/riduzione dei debiti finanziari | 0 (nessuna variazione) |
> | Free cash flow to equity (FCFE) | → **Reddito di bilancio** |

In steady state il capitale circolante non varia, gli investimenti in capitale fisso si limitano a reintegrare gli ammortamenti e il debito finanziario resta costante. Il MOL al netto delle imposte operative e degli ammortamenti è il NOPAT, quindi il **FCFF coincide con il NOPAT**. Aggiungendo oneri finanziari, scudo fiscale e componenti straordinarie si arriva al reddito di bilancio, quindi il **FCFE coincide con il reddito di bilancio**.

### Steady growth

> [!abstract] Definizione
> | Formula generale | Steady growth |
> |---|---|
> | MOL | MOL × (1+g) |
> | - Variazione CCNO | - g × CCNO |
> | Cash flow gestionale lordo | → MOL × (1+g) - g × CCNO |
> | - Flusso fiscale operativo | - Imposte operative × (1+g) |
> | Cash flow gestionale netto | → MOL netto × (1+g) - g × CCNO |
> | -/+ Investimenti/disinvestimenti in capitale fisso | - (g × C.F. + Amm. × (1+g)) |
> | Free cash flow to the firm (FCFF) | → **NOPAT × (1+g) - g × CINO** |
> | +/- Proventi/oneri straordinari | +/- Proventi/oneri straordinari × (1+g) |
> | - Oneri finanziari netti | - Oneri finanziari netti × (1+g) |
> | + Scudo fiscale sugli oneri finanziari | + Scudo fiscale × (1+g) |
> | +/- Aumento/riduzione dei debiti finanziari | + g × Debiti finanziari |
> | Free cash flow to equity (FCFE) | → **Reddito di bilancio × (1+g) - g × C.P.** |

Le grandezze economiche (MOL, imposte operative, ammortamenti, oneri finanziari, scudo fiscale) e quelle patrimoniali (CCNO, capitale fisso C.F., debiti finanziari) sono riferite all'ultimo esercizio e crescono al tasso $g$. Gli ammortamenti moltiplicati per $(1+g)$ si sottraggono al MOL netto $\times (1+g)$ e lasciano il $NOPAT \times (1+g)$. Restano da sottrarre l'aumento del CCNO ($g \times CCNO$) e la crescita del capitale fisso ($g \times C.F.$), che insieme valgono $g \times CINO$, perché $CINO = CCNO + C.F.$ Ne risulta $FCFF = NOPAT \times (1+g) - g \times CINO$.

Per il FCFE si aggiunge che il debito finanziario cresce anch'esso al tasso $g$ e produce una nuova raccolta di $g \times D$. Poiché $CINO - D = C.P.$, il FCFE diventa:

$$FCFE = \text{Reddito di bilancio} \times (1+g) - g \times CINO + g \times D = \text{Reddito di bilancio} \times (1+g) - g \times C.P.$$

> [!lezione] Dalla lezione del 20 novembre 2026: steady state, crescita al tasso g e semplificazioni del modello
> Si parla di steady state perché si ipotizza che l'azienda, quando si proiettano i flussi nel futuro, replichi se stessa a vita, cosa abbastanza improbabile. Se l'azienda crescesse dell'1% ogni anno, questo 1% diventerebbe il tasso di crescita $g$: ogni anno l'azienda fa $1 + g$, cioè la dimensione di un anno più 1%, più 1%, più 1%, in un percorso di crescita dell'1% annuo. È un'ipotesi più attinente alla realtà, ma con un effetto importante, perché $g$ diventa rilevante col passare del tempo.
>
> Il docente richiama il video in cui si piega un foglio di carta in quattro, poi in otto, in sedici e così via: dopo quaranta piegature il foglio diventa il diametro della Terra, una progressione a cui di solito non si pensa. L'effetto di $g$ è analogo: occorre fare attenzione a inserirlo, perché si ipotizza una crescita dell'1% sull'1% dell'anno precedente, e quando la formula viene proiettata all'infinito il valore cambia molto. Mettere 1% oppure 1,8% cambia molto, perché il tasso viene moltiplicato ogni anno.
>
> Il modello contiene semplificazioni. Se l'azienda cresce dell'1%, si ipotizza che anche il MOL cresca dell'1% ogni anno. Per crescere però serve probabilmente più magazzino, più crediti, più denaro immobilizzato, quindi il MOL cresciuto di $1 + g$ viene in parte eroso dalla crescita del circolante: si assume che a una performance di $1 + g$ corrispondano rimanenze e crediti di $1 + g$, con liquidità che si blocca e un po' di MOL che viene mangiato. La formula, che si trova anche nel libro, esprime questo: il MOL che cresce, meno la quota di CCN assorbita dal MOL cresciuto, pari a $g$.
>
> Si ipotizza inoltre che non si possa crescere dell'1% ogni anno senza ingrandirsi e senza investire in nuovi impianti: anche gli ammortamenti salgono dell'1% e salgono dell'1% anche gli investimenti in capex, in asset. Il modello amplifica così anche la parte patrimoniale con questi aggiustamenti, e tutto diventa funzione di $g$. Non è detto che un'azienda come l'acqua San Benedetto, perché cresce dell'1%, amplii dell'1% i suoi investimenti in linea produttiva e quindi anche gli ammortamenti: magari per i prossimi due o tre anni non servono altri investimenti. La valutazione inizia a stare stretta: anche applicando i flussi di cassa dell'azienda si fanno forzature nel ragionamento.

## Le formule dei modelli sintetici

Le formule compatte si ottengono sostituendo i flussi appena descritti nelle formule generali e sommando la serie. Per un flusso costante $F$ scontato al tasso $i$, la somma dei valori attuali è $F/i$. Per un flusso che cresce ogni anno al tasso $g$, con primo flusso $F_1$, è $F_1/(i-g)$, purché $g < i$.

> [!abstract] Definizione
> **Steady state**
> $$V = \frac{NOPAT}{WACC}$$
> $$E = \frac{R.BILANCIO}{r_E}$$
>
> **Steady growth**
> $$V = \frac{NOPAT(1+g) - CINO \cdot g}{WACC - g}$$
> $$E = \frac{R.BILANCIO(1+g) - C.P. \cdot g}{r_E - g}$$
>
> Nelle formule $V$ è il valore in ottica assets (enterprise value), $E$ il valore in ottica equity (equity value), $g$ il tasso di crescita costante, $CINO$ il capitale investito netto operativo, $C.P.$ il capitale proprio, $WACC$ il costo medio ponderato del capitale e $r_E$ il costo dell'equity, cioè il rendimento atteso dagli azionisti.

> [!lezione] Dalla lezione del 20 novembre 2026: le formule a partire dal conto economico
> Il ragionamento è lo stesso di prima, ma serve quando non si hanno i flussi di cassa del rendiconto finanziario. In ipotesi steady state si applica una sorta di rendita perpetua in cui, al posto dei flussi di cassa, si mette l'FCFO, che dal conto economico si assimila al NOPAT. Per l'equity si mette l'FCFE, il cui fratello nel conto economico è l'utile d'esercizio, cioè l'ultima riga. I valori sono attualizzati con una formula tipo rendita perpetua: se l'azienda sta ferma e replica se stessa ogni anno, la formula è questa; se cresce, si inseriscono tutti gli aggiustamenti di $g$, con le semplificazioni indicate.
>
> Nel caso dell'equity si ha un utile d'esercizio molto semplificato, il reddito di bilancio, che se l'azienda cresce di $g$ cresce dell'1% anche a fine anno; il capitale proprio però è influenzato dalla crescita di $g$. Anche nel caso dell'asset il reddito operativo cresce dell'1%, ma viene ridotto dal capitale investito, cioè dagli asset che si sono gonfiati e hanno eroso margine, deprimendo così il NOPAT. Il ragionamento vale sia che l'azienda cresca a un tasso fisso $g$ sia che replichi se stessa.

## Esempio steady state: valutazione dell'impresa Alfa

> [!example] Esempio
> **Dati.** Si riprendono i risultati dell'esercizio sull'azienda Alfa: NOPAT 59.843 e reddito netto 43.981. Il WACC stimato è il 5,8% e il rendimento atteso per gli azionisti ($r_E$) è il 7,5%. Si vuole il valore dell'impresa in ottica assets e in ottica equity.
>
> **Ottica assets.**
>
> $$EV = \frac{NOPAT}{WACC} = \frac{59.843}{5{,}8\%} = 1.031.776$$
>
> **Ottica equity.**
>
> $$E = \frac{R.BILANCIO}{r_E} = \frac{43.981}{7{,}5\%} = 586.413$$
>
> **Posizione finanziaria netta implicita.** Dalla relazione $E = EV - PFN$:
>
> $$PFN = EV - E = 1.031.776 - 586.413 = 445.363$$
>
> | Grandezza | Valore |
> |---|---|
> | Enterprise value (ottica assets) | 1.031.776 |
> | Equity value (ottica equity) | 586.413 |
> | PFN implicita | 445.363 |

In steady state il FCFE coincide con il reddito netto. Il passaggio dal NOPAT al reddito netto si verifica con i dati dell'esercizio: $59.843 - 22.000 + 6.138 = 43.981$, cioè NOPAT, meno oneri finanziari, più scudo fiscale ($22.000 \times 27{,}9\%$).

> [!lezione] Dalla lezione del 20 novembre 2026: compito per la lezione successiva
> Il docente chiede di riprendere l'azienda per cui è stato calcolato il NOPAT, di applicare le formule in ottica asset ed equity e di vedere quanto può valere. Gli esempi delle pagine di slide verranno caricati fino a questo punto. La lezione successiva è martedì.

## Esempio steady growth: valutazione dell'impresa Alfa

> [!example] Esempio
> **Dati.** Stessi NOPAT (59.843), reddito netto (43.981), WACC (5,8%) e $r_E$ (7,5%) dell'esempio precedente. L'azienda ha un capitale investito netto operativo di € 760.000, un capitale proprio di € 302.000 e prevede di crescere a un tasso costante $g$ del 2,0%.
>
> **Ottica assets.**
>
> $$EV = \frac{NOPAT(1+g) - CINO \cdot g}{WACC - g}$$
>
> Numeratore: $59.843 \times 1{,}02 - 760.000 \times 0{,}02 = 61.039{,}86 - 15.200 = 45.839{,}86 \approx 45.840$.
>
> Denominatore: $5{,}8\% - 2{,}0\% = 3{,}8\%$.
>
> $$EV = \frac{45.839{,}86}{3{,}8\%} = 1.206.312$$
>
> **Ottica equity.**
>
> $$E = \frac{R.BILANCIO(1+g) - C.P. \cdot g}{r_E - g}$$
>
> Numeratore: $43.981 \times 1{,}02 - 302.000 \times 0{,}02 = 44.860{,}62 - 6.040 = 38.820{,}62 \approx 38.821$.
>
> Denominatore: $7{,}5\% - 2{,}0\% = 5{,}5\%$.
>
> $$E = \frac{38.820{,}62}{5{,}5\%} = 705.829$$
>
> **Posizione finanziaria netta implicita.**
>
> $$PFN = EV - E = 1.206.312 - 705.829 = 500.483$$
>
> | Grandezza | Valore |
> |---|---|
> | Enterprise value (ottica assets) | 1.206.312 |
> | Equity value (ottica equity) | 705.829 |
> | PFN implicita | 500.483 |
