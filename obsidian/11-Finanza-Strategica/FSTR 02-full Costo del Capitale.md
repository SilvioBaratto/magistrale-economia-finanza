---
title: "Il costo del capitale: WACC, CAPM, rischio Paese e beta unlevered"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_02-full_Costo-del-Capitale.pdf"
text_layer: true
verified: true
generated: 2026-08-30
---

## Oggetto del capitolo

Il capitolo riguarda il tasso di sconto con cui valutare un progetto di investimento quando l'impresa si finanzia anche con debito. Il tasso si costruisce a partire dal costo del debito e dal costo del capitale proprio, stimato con il CAPM, e si sintetizza nel costo medio ponderato del capitale (WACC). Serve ad attualizzare i flussi del progetto, sia nel [[FSTR 01-full Progetti di Investimento|calcolo del valore attuale netto]] sia nei [[FSTR 03 Modelli Valutazione Finanziaria Parte1|metodi DCF di valutazione d'impresa]]. La collocazione del capitolo nel programma è descritta nell'[[FSTR 00 Intro Corso|introduzione al corso]]. Riferimento bibliografico: capitolo 7.3 del testo indicato con la sigla BBS, fino all'equazione 7.21.

## Il tasso di sconto di un progetto: Assets, Equity, Debts e WACC

L'impresa è rappresentata con tre blocchi: l'attivo (assets), finanziato dal capitale proprio (equity) e dal debito (debts). Le due fonti di finanziamento hanno rischio e rendimento richiesto diversi. Il tasso di sconto dell'attivo nel suo complesso è il WACC, il rendimento richiesto dagli azionisti è $r_E$ e quello richiesto dai finanziatori è $r_D$.

![](assets/fstr-02/fig01.png)

**Figura 1** — Struttura assets, equity e debts: l'attivo, a cui corrisponde il WACC, è finanziato dal capitale proprio, il cui costo si stima con il CAPM, e dal debito, il cui costo è il tasso sui prestiti.

> [!abstract] Definizione
> Gli **assets** sono l'insieme dei beni e delle risorse economiche dell'azienda: impianti, macchinari, immobili, brevetti, capitale circolante, competenze, tecnologia. Sono gli elementi che permettono all'azienda di produrre beni, erogare servizi e generare flussi di cassa. Il tasso con cui si attualizzano i flussi generati dagli assets è il **WACC** (Weighted Average Cost of Capital).
>
> L'**equity** è la proprietà dell'azienda e sopporta l'intero rischio residuo della gestione. Riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti e pretende un rendimento adeguato al rischio assunto, indicato con $r_E$.
>
> I **debts** comprendono tutte le forme di finanziamento ottenute da banche, obbligazionisti e altri creditori. Hanno un costo esplicito sotto forma di interessi ($r_D$), richiedono rimborsi programmati, godono di priorità rispetto agli azionisti nella distribuzione dei flussi e hanno un rischio minore dell'equity.
>
> Il WACC combina i due costi, ciascuno pesato per l'incidenza della rispettiva fonte sul totale:
>
> $$WACC = r_E\,\frac{E}{E+D} + r_D(1-t_c)\,\frac{D}{E+D}$$

Il costo del capitale proprio $r_E$ si stima con il CAPM, mentre $r_D$ è il tasso a cui l'impresa ottiene i prestiti. Il fattore $(1-t_c)$ porta il costo del debito al netto dello scudo fiscale: gli interessi passivi sono deducibili, quindi l'aliquota $t_c$ riduce l'onere effettivo del debito.

> [!lezione] Dalla lezione del 19 novembre 2026: la lettura dello schema assets, equity e debts
> Lo schema è uno stato patrimoniale riclassificato, cioè un prospetto a fonti e impieghi, e non uno stato patrimoniale civilistico. Lo mostra la voce del capitale circolante, che contiene sia attività sia passività e quindi non è né un attivo né un passivo. La riclassificazione mette in luce che a fronte di determinati impieghi ci sono determinate fonti.
>
> Tutto ciò che sta a sinistra, cioè gli assets, è di pertinenza di tutti gli stakeholders, soci o finanziatori terzi, ed è ciò che permette di produrre e di creare i flussi di cassa. Le fonti che rendono possibile l'esistenza degli assets, cioè la possibilità di far girare il capitale, arrivano dagli stakeholders e sono di due categorie: chi finanzia in qualità di socio e chi finanzia in qualità di creditore. I fornitori non rientrano tra i finanziatori, perché sono già compresi nel circolante e quindi negli assets. I creditori sono solitamente le banche.
>
> Un socio può essere anche creditore. In alcuni bilanci compare tra le voci del passivo la dicitura "soci conto finanziamento": anziché fare un conferimento di capitale in beni o in denaro, i soci fanno un prestito alla società, che è trattato come un prestito, e per quella porzione sono creditori. Sono casi un po' eccezionali, ma i finanziamenti soci si trovano di frequente, soprattutto quando l'azienda è provvisoriamente in tensione di liquidità: i soci prestano denaro in via temporanea e la somma viene poi restituita.

## L'aliquota fiscale nella valutazione

L'aliquota da impiegare dipende dall'uso che se ne fa.

| Impiego | Aliquota |
|---|---|
| Margini | IRES (24%) più IRAP (3,9%), in totale 27,9% |
| WACC | Solo IRES (24%) |

Nel WACC si usa la sola IRES perché è l'imposta che consente di dedurre gli interessi passivi, e quindi quella su cui agisce lo scudo fiscale del debito. Gli esempi del capitolo adottano queste aliquote, che restano una semplificazione del carico fiscale effettivo della società.

> [!lezione] Dalla lezione del 19 novembre 2026: l'aliquota come semplificazione
> Indicare l'aliquota con $t_c$ è una semplificazione, perché il reddito d'esercizio di una SRL o di una SPA è tassato con l'IRES e con l'IRAP, che hanno basi imponibili diverse. Per questo negli esercizi e nelle semplificazioni si usa un carico fiscale del 28 o del 30% sull'utile ante imposte: nei business plan e nel conto economico la proiezione del carico fiscale su più anni è stimata tra il 27, il 28 e il 30%. Il calcolo effettivo dell'imponibile spetta al commercialista, ma a volte la realtà va semplificata: se viene chiesto di costruire un business plan e di proiettare in avanti il carico fiscale, si può assumere il 28 o il 30%.
>
> Per gli interessi passivi vale invece una regola specifica: sono deducibili dall'imponibile IRES, la cui aliquota è il 24%. Dal monte imponibile su cui si calcola l'IRES si possono togliere gli interessi passivi pagati sui finanziamenti, e l'imponibile si abbassa. Lo scudo fiscale è dunque legato agli interessi passivi e, tramite questi, all'IRES. Per questo negli esempi del libro e negli esercizi, nel calcolo dello scudo fiscale, si usa il risparmio del 24%.

## Il costo del debito

> [!abstract] Definizione
> Il **costo del debito** $r_D$ è il rendimento richiesto dai finanziatori che prestano denaro all'impresa: banche, obbligazionisti, istituzioni finanziarie. Il creditore si aspetta un rendimento che compensi il valore del tempo e il rischio che l'impresa non rimborsi il finanziamento. Tale rendimento è il tasso di interesse effettivo del prestito.

> [!lezione] Dalla lezione del 19 novembre 2026: chi presta e che cosa remunera il costo del debito
> Prestano denaro all'impresa le banche, gli obbligazionisti se l'azienda ha emesso obbligazioni, altre istituzioni finanziarie e anche enti statali o parastatali che finanziano la crescita e gli investimenti a un costo del denaro agevolato, come Invitalia e Simest. Il socio può a sua volta fare un finanziamento alla società, fruttifero o infruttifero: se è fruttifero, rientra nel costo del debito.
>
> Che cosa viene ricompensato con $r_D$? Prestare denaro implica in ogni caso tempo e rischio. Poiché il prestito è fatto a un'azienda e non, per esempio, al governo tedesco, l'azienda può avere vicende diverse, e quindi $r_D$ incorpora di per sé un fattore rischio e un fattore tempo.

> [!example] Esempio
> Un'azienda ottiene un finanziamento di 1 milione di euro al 5% annuo, quindi $r_D = 5\%$. Gli interessi annui sono 50.000 euro. Poiché sono deducibili, con IRES al 24% l'imposta si riduce di 12.000 euro e l'onere netto è 38.000 euro, pari al 3,8% del finanziamento. Con l'effetto fiscale l'onere effettivo diventa
>
> $$r_D^{\,\text{post-tax}} = 5\% \times (1-24\%) = 3{,}8\%$$

Quando l'azienda ha più finanziamenti contemporanei, $r_D$ è la media ponderata del costo di tutti i debiti, con pesi pari al valore di ciascun finanziamento. Occorre quindi considerare sia il tasso sia il peso di ogni debito nella struttura complessiva:

$$r_D = \frac{\sum_i (\text{Debito}_i \times \text{tasso}_i)}{\sum_i \text{Debito}_i}$$

$$r_D^{\,\text{post-tax}} = r_D \times (1-t_c)$$

> [!lezione] Dalla lezione del 19 novembre 2026: come si determina il costo del debito con più finanziamenti
> Nel bilancio o nella situazione contabile di un'azienda compaiono più finanziamenti, ciascuno con il proprio tasso: per esempio un anticipo export, un mutuo a 5 anni con la banca, un mutuo a 30 anni, il debito verso Simest per l'acquisto di un macchinario. Resta da stabilire quale valore di $r_D$ usare. Con una semplificazione si assume la media ponderata dei tassi di debito, in cui ogni finanziamento pesa in rapporto al totale dei finanziamenti.
>
> Se un'azienda ha un mutuo da 20 milioni di euro al 5% e un finanziamento da 500.000 euro all'1%, è molto più probabile che $r_D$ sia vicino al 5% che non alla semplice media tra i due tassi. Per debiti si intendono sempre i debiti finanziari, cioè quelli che maturano interessi, e non i debiti verso i fornitori. Con tre mutui a tre tassi diversi il calcolo si sviluppa allo stesso modo. Nell'esempio considerato a lezione, che comprende anche lo scudo fiscale, un tasso medio del 4,70% corrisponde a un costo effettivo dopo lo scudo fiscale del 3,57%.

## Il costo del capitale proprio

> [!abstract] Definizione
> Il **costo del capitale proprio** $r_E$ è il rendimento che l'azionista si aspetta dall'investimento nell'impresa. L'azionista si espone al rischio dell'azienda e pretende un compenso adeguato: $r_E$ è l'obiettivo di rendimento che l'impresa deve garantire ai suoi proprietari affinché accettino di investire capitale rischioso.

Il capitale proprio non ha garanzie. Assorbe i rischi operativi, finanziari e di mercato e riceve i flussi solo dopo che tutti i creditori sono stati soddisfatti. Nella pratica $r_E$ risulta quasi sempre più elevato del costo del debito.

> [!lezione] Dalla lezione del 19 novembre 2026: perché il costo del capitale proprio supera il costo del debito
> $r_E$ è quanto l'azienda deve remunerare un socio che mette 100 euro non come creditore ma come azionista, cioè il rendimento che deve ricevere per rischiare quei 100 euro nel capitale di rischio. Se l'azienda chiude o fallisce, i 100 euro sono persi. Gli azionisti vengono inoltre dopo tutti: se viene nominato un liquidatore, sono pagati prima il personale e i dipendenti, poi lo Stato, poi le banche e tutti gli altri creditori, e solo se avanza qualcosa la somma va agli azionisti che hanno messo il capitale. Essendo ultimi nella gerarchia di restituzione, gli azionisti assorbono tutti i rischi rispetto agli altri soggetti, e per questo $r_E$ è solitamente più alto di $r_D$.
>
> A grandi linee $r_E$ si può immaginare come la somma di un elemento certo, garantito, e di un elemento di rischiosità: l'azienda è infatti esposta ogni giorno al mercato, alle decisioni aziendali, alla concorrenza, alle vicende interne e allo sviluppo dei prodotti. Il primo elemento è il tasso privo di rischio, che non dipende dal fatto di essere un'azienda ma dal fatto che delle somme sono vincolate per un determinato periodo: è ciò che dà valore al tempo. Richiama le prime slide, in cui si diceva che 100 euro oggi valgono più di 100 euro tra un anno e che 100 euro tra un anno oggi ne valgono 98: spostare il denaro nel tempo prevede già di per sé una remunerazione, data dal tasso fisso.
>
> Al tasso privo di rischio si aggiunge un premio per il rischio, che ha due elementi. Il primo è il rischio sistematico, misurato dal beta. Il secondo è il Paese: non è indifferente che l'azienda sia in Italia, in Paraguay, in Germania o in America. La condizione di rischio dipende quindi da due cose: dal settore, per esempio le ciminiere piuttosto che le telecomunicazioni o l'aerospaziale, e dal luogo in cui si esercita il business.

## Il CAPM

> [!abstract] Definizione
> Il **Capital Asset Pricing Model** (CAPM) determina il costo del capitale proprio come somma di un tasso privo di rischio e di un compenso per il rischio:
>
> $$r_E = r_f + \beta\,(R_m - r_f)$$
>
> | Componente | Nome | Interpretazione |
> |---|---|---|
> | $r_E$ | Costo del capitale proprio | Rendimento richiesto dagli investitori |
> | $r_f$ | Tasso privo di rischio | «Valore del tempo» |
> | $\beta$ | Moltiplicatore del rischio sistematico | «Quantità di rischio» |
> | $(R_m - r_f)$ | Premio per il rischio di mercato | «Prezzo del rischio» |
>
> Il termine $\beta\,(R_m - r_f)$ nel suo insieme è il **premio per il rischio**.

Il beta è una caratteristica dell'impresa o del settore, mentre il premio per il rischio di mercato dipende dal mercato, cioè dal Paese a cui l'investimento si riferisce. Resta da stabilire come tenere conto del rischio Paese quando si fissano $r_f$ e il premio.

## Il rischio Paese nel CAPM

Il **rischio Paese** è la componente di rischiosità del Paese a cui l'investimento si riferisce. Se l'azienda o il progetto valutato sono situati in Italia, si ragiona sulla rischiosità dell'Italia. Dipende dalla solidità dei conti pubblici, dal livello del debito sovrano, dall'affidabilità delle istituzioni, dalla stabilità politica, dall'efficienza del sistema giudiziario, dalla qualità delle infrastrutture, dal rating del Paese, dallo spread sovrano e dai CDS.

> [!lezione] Dalla lezione del 19 novembre 2026: perché conta il Paese in cui si svolge il business
> Dove si esercita il business è rilevante, e il rischio Paese va misurato accanto al premio per il rischio di mercato, sia per un progetto di investimento sia per il business di un'azienda, come aprire una filiale o acquisire un'azienda in quel Paese. Il docente porta l'esempio della Fairplast di Castelfranco Veneto (Vicenza), leader nei prodotti per animali: PET, acquari, gabbiette e accessori. Secondo il docente la società ha uno stabilimento in Ucraina e un mese prima della lezione è stato lanciato un missile sul capannone adiacente al suo, che sarebbe stato raso al suolo; la Fairplast ha ancora in Ucraina una controllata, dove svolge il business, a tre o quattro metri di distanza. Mettere 100 euro in un'azienda nella zona industriale di Kiev, o in Angola dove passano le jeep dei ribelli armati, non è come metterli nella periferia di Bonn o di Berlino, o in America.
>
> Fa fede il Paese in cui si trova il business e non la sede legale. Se una società ha la sede a Milano, dove c'è un ufficio con una segretaria, ma tutti gli impianti produttivi sono in Congo, la sede legale è italiana ma il business, cioè il luogo in cui si manifesta il rischio, è probabilmente in Africa. Il ragionamento non si fa quindi sulla sede legale della società o dell'investimento, che può non coincidere con il luogo del core business: occorre considerare il Paese in cui si svolgono effettivamente le operations.
>
> Tra i fattori che determinano il livello di rischio attribuito a ogni Paese il docente cita, oltre a guerre civili come in Congo e a bombe come in Ucraina, i fenomeni di corruzione e un governo che cambia ogni due mesi. Sono questi, con molti altri, gli indicatori usati dalle società di rating quando annunciano, per esempio, che il rating dell'Italia è confermato: valutano più o meno questi aspetti per dire quanto sia rischioso mettere i soldi in quel Paese. Più è rischioso, più va chiesto un rendimento alto.

Il premio per il rischio Paese può essere considerato in due modi. Con l'Alternativa 1 si carica il rischio Paese nel tasso privo di rischio, con l'Alternativa 2 lo si carica nel premio per il rischio. Entrambe sono corrette: l'importante è la coerenza, cioè applicarne una sola lungo tutta la stima.

Una misura del rischio Paese è il Country Risk Assessment di Coface, che classifica 160 Paesi su una scala di otto classi, con l'indicazione dei declassamenti (downgrade) e dei miglioramenti (upgrade) più recenti. La metodologia combina la competenza macroeconomica nella valutazione del rischio Paese, la comprensione del contesto di business e dati microeconomici raccolti in 70 anni di esperienza di pagamento. Coface valuta il rischio di credito medio delle imprese di un Paese a partire da dati macroeconomici, finanziari e politici.

| Classe | Giudizio (Coface) | Rischio Paese |
|---|---|---|
| A1 | Very low | Molto basso |
| A2 | Low | Basso |
| A3 | Satisfactory | Soddisfacente |
| A4 | Reasonable | Ragionevole |
| B | Fairly high | Abbastanza alto |
| C | High | Alto |
| D | Very high | Molto alto |
| E | Extreme | Estremo |

La mappa di Coface mostra che il rischio Paese varia sensibilmente da un'area all'altra: Nord America, Europa occidentale e settentrionale e Australia rientrano per lo più nelle classi più basse, mentre Africa, ampie aree dell'Asia, parte dell'Europa orientale e parte dell'America meridionale sono in classi più alte. Per questo il premio per il rischio Paese va considerato nella stima del costo del capitale.

> [!lezione] Dalla lezione del 19 novembre 2026: Coface, Allianz e la lettura delle cartine del rischio Paese
> La cartina è pubblicata ogni anno da Coface, un'azienda di intermediazione creditizia: una multinazionale che svolge in gran parte l'attività di assicurazione dei crediti. Coface è una specie di broker che assicura i crediti delle aziende. L'azienda ha dei crediti, ne presenta il monte alla società e questa glieli assicura, come si assicura un'automobile: l'azienda paga il premio e, se per determinati motivi non incassa il credito, la società la rimborsa. Più il credito è rischioso, più alto è il premio. Lo stesso accade nei preventivi delle assicurazioni auto, dove viene chiesto dove si tiene la macchina, perché se sta in strada è più rischiosa e il premio è più alto.
>
> Nella cartina la scala dei colori parte dal verde scuro, che corrisponde al livello 1 (very low); il livello 2 è low, e la categoria E è il viola più scuro. Conviene osservare dove si trovano i verdi nel mondo e dove si trova la categoria E: i Paesi in verde scuro sono pochi, e la cartina è una spiegazione abbastanza pratica del rischio Paese, che esiste perché il mondo è effettivamente distribuito così. L'Italia compare in un rosa chiaro, che per Coface indica un rischio moderatamente alto (fairly high). Questo valore è legato al rischio delle aziende di quel Paese.
>
> Quella di Coface non è l'unica cartina e non è il riferimento mondiale. Un'altra è stata fatta da Allianz, con altri colori e altri parametri, ed è mostrata solo per far vedere come funziona il rischio Paese. Anche in questa i verdi sono molto simili a quelli del grafico Coface, quindi le conclusioni sono più o meno le stesse. I colori sono quattro (verde, giallo, arancio e viola) e in questo grafico l'Italia è verde.

## Il tasso privo di rischio

> [!abstract] Definizione
> Come riferimento per il **tasso privo di rischio** $r_f$ si usa il rendimento dei bond governativi a rischio minimo nel Paese o nell'area di riferimento dell'impresa da valutare, il più prossimo in termini geografici. Per la valutazione delle imprese italiane si usa il **Bund tedesco a 10 anni** (esempio: 2,20%).
>
> I BTP italiani non sono privi di rischio: il loro rendimento incorpora già il rischio Paese dell'Italia.

La tabella riporta il rendimento dei titoli di Stato decennali di venti Paesi e lo spread rispetto al Bund, in punti percentuali (dati ritardati di almeno 15 minuti, al 10 novembre 2025, ore 13:21 GMT). Lo spread del Bund è nullo per definizione. Il BTP italiano rende il 3,45% contro il 2,71% del Bund, con uno spread di +0,74 punti percentuali: sul titolo italiano il mercato richiede un rendimento superiore a quello del Bund. Gli spread sono riportati come nella fonte e in alcuni casi differiscono di un centesimo dalla differenza tra i rendimenti arrotondati.

| Paese | Rendimento | Spread vs Bund |
|---|---|---|
| Australia | 4,43% | +1,73 |
| Austria | 2,99% | +0,29 |
| Belgio | 3,25% | +0,54 |
| Canada | 3,26% | +0,55 |
| Danimarca | 2,60% | -0,11 |
| Finlandia | 3,06% | +0,36 |
| Francia | 3,45% | +0,75 |
| Germania | 2,71% | (riferimento) |
| Grecia | 3,35% | +0,64 |
| Irlanda | 2,91% | +0,20 |
| Italia | 3,45% | +0,74 |
| Giappone | 1,77% | -0,93 |
| Paesi Bassi | 2,86% | +0,15 |
| Nuova Zelanda | 4,25% | +1,54 |
| Portogallo | 3,04% | +0,34 |
| Spagna | 3,21% | +0,50 |
| Svezia | 2,66% | -0,04 |
| Svizzera | 0,17% | -2,54 |
| Regno Unito | 4,57% | +1,87 |
| Stati Uniti | 4,13% | +1,42 |

I valori numerici degli esempi di questo capitolo (BTP al 4,40%, Bund al 2,20%) sono indicativi e non coincidono con quelli della tabella.

> [!lezione] Dalla lezione del 19 novembre 2026: perché il Bund e non il BTP, e che cosa misura lo spread
> Partendo dall'Italia e guardando ai Paesi limitrofi, la cosa più vicina a un tasso privo di rischio è un Bund tedesco, cioè un titolo di debito emesso dalla Germania. Il primo riferimento utile per $r_f$ è quindi il Bund tedesco a dieci anni, il cui rendimento è pubblicato dalla banca centrale tedesca e riportato nelle slide. La probabilità che la Germania fallisca e non restituisca il Bund fra dieci anni è verosimilmente quasi nulla.
>
> Il BTP, come mostrano anche le cartine, non è privo di rischio. Il BTP e il BTP Valore compaiono nelle pubblicità delle Poste e in televisione e sono proposti agli italiani come qualcosa con un rendimento certo, ma di fatto non lo è: è comunque meno certo di un titolo tedesco. Per questo si parla di spread, il differenziale rispetto al Bund. Nella tabella la Germania è il benchmark e il suo spread è indicato con un trattino, cioè è zero. Lo spread dell'Italia dimostra che il BTP non è privo di rischio: incorpora una quantità di rischio, seppur minima, che dipende dal fatto di essere in Italia.
>
> Nella tabella commentata a lezione il Bund a dieci anni rende circa 3,37-3,38% e lo spread dell'Italia verso il Bund è 1,05 punti percentuali; la tabella della nota riporta per il Bund il 2,71% e per l'Italia uno spread di +0,74.

## Alternativa 1: il rischio Paese nel tasso privo di rischio

Con l'Alternativa 1 il rischio Paese è caricato nel tasso privo di rischio. Il CAPM usa quindi come tasso privo di rischio il rendimento dei bond governativi del Paese di riferimento dell'impresa da valutare, comprensivo del rischio Paese (esempio: BTP italiano a 10 anni, 4,40%), e come premio per il rischio di mercato il premio base, cioè quello dei Paesi con rischio Paese minimo (esempio: Stati Uniti, 4,12%).

## Alternativa 2: il rischio Paese nel premio per il rischio

Con l'Alternativa 2 il tasso privo di rischio è quello puro (il Bund) e il premio per il rischio di mercato è formato da due componenti.

> [!abstract] Definizione
> Il **Market Risk Premium** (MRP), o premio per il rischio «base», è il premio che un investitore richiede per investire nel mercato azionario invece che in un titolo privo di rischio. Si calcola sui mercati con rischio Paese molto contenuto, tipicamente gli Stati Uniti, e riflette il rischio sistematico globale, non specifico del Paese. Deriva da serie storiche di rendimenti azionari e obbligazionari e viene aggiornato annualmente da Damodaran.
>
> Il **Country Risk Premium** (CRP), o spread di rischio specifico del Paese, è il premio richiesto per investire in un Paese con rischiosità superiore a quella dei Paesi di riferimento. Si ricava dal CDS (Credit Default Swap sul debito sovrano), che misura il rischio percepito dagli investitori che lo Stato non onori i suoi impegni finanziari, ad esempio il CDS Italia. Riflette la percezione sul debito pubblico e le condizioni politiche ed economiche ed è comparabile a uno spread. Il CDS, o lo spread legato al rating del Paese, viene «azionarizzato», cioè trasformato in CRP moltiplicandolo per un coefficiente che corregge la volatilità relativa.

Nella formulazione di Damodaran il coefficiente è il rapporto tra la volatilità del mercato azionario del Paese e quella dei suoi titoli di Stato:

$$CRP = \text{spread sovrano} \times \frac{\sigma_{\text{azioni}}}{\sigma_{\text{obbligazioni}}}$$

I valori di riferimento sono quelli di Damodaran (2024). L'Equity Risk Premium degli Stati Uniti, che costituisce l'MRP, è il 4,12%. Il Country Risk Premium dell'Italia, ricavato dal CDS, è l'1,08%. Il premio per il rischio di mercato applicabile all'Italia è la loro somma:

$$4{,}12\% + 1{,}08\% = 5{,}20\%$$

## Esempio: il costo del capitale proprio per un'impresa italiana

> [!example] Esempio
> Il CAPM $r_E = r_f + \beta\,(R_m - r_f)$ si applica a un'impresa italiana con i due metodi corrispondenti alle due alternative.
>
> **Metodo 1** (Alternativa 1, rischio Paese nel tasso privo di rischio). Il tasso privo di rischio è il rendimento del BTP, che include il rischio Paese, e il premio è quello di un mercato a rischio minimo (Stati Uniti):
>
> $$r_E = \underbrace{r_{BTP}}_{4{,}40\%} + \beta\,\underbrace{MRP_{USA}}_{4{,}12\%} = 4{,}40\% + 4{,}12\%\,\beta$$
>
> **Metodo 2** (Alternativa 2, rischio Paese nel premio per il rischio). Il tasso privo di rischio è il Bund, risk free «puro», e il premio è quello del mercato a rischio minimo più il premio specifico dell'Italia:
>
> $$r_E = \underbrace{r_{Bund}}_{2{,}20\%} + \beta\,(\underbrace{MRP_{USA}}_{4{,}12\%} + \underbrace{CRP_{Italia}}_{1{,}08\%}) = 2{,}20\% + 5{,}20\%\,\beta$$

I due metodi allocano la stessa componente di rischio Paese in punti diversi della formula e danno stime che tendono a convergere, senza coincidere in generale. La differenza tra i due risultati è

$$(4{,}40\% - 2{,}20\%) - 1{,}08\%\,\beta = 2{,}20\% - 1{,}08\%\,\beta$$

perché nel primo metodo lo spread tra BTP e Bund (2,20 punti percentuali) entra per intero nel tasso privo di rischio, mentre nel secondo il rischio Paese (1,08%) è moltiplicato per il beta. Le due stime coincidono solo per $\beta = 2{,}20/1{,}08 \approx 2{,}037$; per beta inferiori il primo metodo dà il valore più alto. La tabella confronta i risultati per alcuni valori del beta, scelti a titolo illustrativo.

| $\beta$ | Metodo 1 | Metodo 2 | Differenza (punti percentuali) |
|---|---|---|---|
| 0,50 | 6,46% | 4,80% | 1,66 |
| 1,00 | 8,52% | 7,40% | 1,12 |
| 1,50 | 10,58% | 10,00% | 0,58 |
| 2,037 | 12,79% | 12,79% | 0,00 |

> [!lezione] Dalla lezione del 19 novembre 2026: le due alternative a confronto
> Nell'alternativa 1 il rischio Paese dell'Italia è già incluso nel BTP, che diventa quindi il tasso privo di rischio. Manca soltanto il rischio generico di mercato, quello di base, che non dipende dall'essere in Italia ma solo dall'essere sul mercato: si immagina un portafoglio infinito di tutte le aziende e si prende il premio per il rischio degli Stati Uniti, un Paese a rischio minimo. Il beta resta invariato.
>
> Nell'alternativa 2 il tasso privo di rischio resta il Bund e non lo si maggiora. L'essere in Italia entra nella seconda parte dell'espressione, nel premio per il rischio di mercato, che si può pensare come composto da due componenti: l'MRP, cioè il rischio di un portafoglio di aziende, e un rischio specifico dell'Italia, il country risk premium, che si può rappresentare con il CDS. È come sommare la rischiosità dell'Italia a quella degli Stati Uniti.
>
> Nell'esempio numerico svolto a lezione la prima alternativa usa il rendimento del bond italiano, circa 4,42% secondo la tavola del Financial Times, abbinato al premio di mercato degli Stati Uniti; la seconda usa il Bund al 3,38%, il premio di mercato degli Stati Uniti e il CDS dell'Italia, poco più dell'1%. Le due alternative portano a quantità abbastanza simili, e il docente le considera equivalenti e sensate. Si guardano entrambe perché si possono avere a disposizione dati diversi, e sono entrambe valide perché i risultati convergono.

## Il coefficiente beta

> [!abstract] Definizione
> Il **beta** misura quanto varia il rendimento di un titolo al variare del rendimento di mercato:
>
> $$\beta = \frac{COV(R_t;\,R_m)}{VAR(R_m)}$$
>
> dove $R_t$ è il rendimento del titolo valutato e $R_m$ quello del mercato.

La covarianza misura quanto i rendimenti del titolo si muovono insieme a quelli del mercato (è una misura affine alla correlazione), mentre la varianza esprime la variabilità dei rendimenti di mercato. Per il calcolo si usano i rendimenti di un indice di mercato (ad esempio FTSE MIB o S&P) e quelli del titolo, su base giornaliera o settimanale, relativi agli ultimi due o cinque anni.

> [!lezione] Dalla lezione del 19 novembre 2026: origine del beta e fonti dei dati
> Questi concetti sono ereditati da Damodaran, che secondo il docente nel 1999 ha condotto le analisi sulle società quotate americane; per questo si parla sempre di rendimento del titolo. In Italia il ragionamento si presta meno, perché le società con titoli quotati sono una manciata, a fronte di quasi un milione di sole SRL. Per l'applicazione, al posto del singolo titolo si può assumere il settore a cui appartiene.
>
> I dati sono pubblici: le quotazioni dei tassi dei bond, cioè dei BTP, e le tavole di Damodaran sul premio per il rischio. Per il beta si usano sempre le tavole di Damodaran o simili, che riportano sia il beta del settore, dato dai beta delle singole aziende, sia quello della singola azienda. I due non coincidono, perché il beta della singola azienda è influenzato da fattori più specifici rispetto a quello del settore: esistono per esempio il beta dell'ILVA e il beta del settore metallurgia. Entrambi risentono del diverso grado di indebitamento delle aziende, quindi sono beta levered.

Il beta dipende dal livello di rischio operativo, legato al rapporto tra costi fissi e costi variabili, e dal livello di rischio finanziario, cioè dalla leva. La ciclicità dei ricavi e il rischio operativo possono differire poco tra imprese dello stesso settore, mentre il rischio finanziario può essere molto diverso: è il caso tipico della sottocapitalizzazione delle PMI italiane. Per questo, nel confronto tra imprese con leve diverse, il beta osservato richiede una rettifica per la leva finanziaria, che si ottiene con il beta unlevered descritto più avanti.

> [!lezione] Dalla lezione del 19 novembre 2026: le tre grandezze da cui dipende il beta
> Il docente indica tre grandezze da cui dipende il beta.
>
> La prima è la ciclicità dei ricavi: alcuni settori, e di conseguenza le aziende che vi appartengono, hanno ricavi ciclici. L'esempio è più forte nei sottosegmenti che nelle categorie generali come food and beverage: le aziende che fanno gelati hanno una stagionalità annuale dei ricavi molto simile tra loro, diversa da quella di un'azienda di abbigliamento o di un'azienda automobilistica. Alcune aziende sono inoltre più esposte di altre alla ciclicità. Un'azienda che vende sciroppi per la tosse ha le pubblicità in autunno e nessuna a luglio, mentre quelle per il mal di testa si trovano a giugno-luglio o a gennaio-marzo, per chi deve chiudere i bilanci o sostenere gli esami. Ogni azienda e ogni settore ha le sue ciclicità.
>
> La seconda è la leva operativa, o rischio operativo, cioè la proporzione tra costi fissi e costi variabili. Un call center vive di personale e ha quasi tutti costi variabili: se chiude, i costi fissi sono al massimo un centinaio di cuffie e di computer. Un'azienda siderurgica ha quasi tutti costi fissi: se chiude l'ILVA, i costi fissi sono molti di più, perché chiudere un altoforno non è come chiudere un call center.
>
> La terza è l'indebitamento, che nelle aziende italiane sposta il peso sul beta e distorce un po' il ragionamento. Le aziende italiane sono spesso sottocapitalizzate in termini di capitale proprio: se ogni volta che servono soldi li si fa dare dalla banca, il passivo si gonfia di debiti verso terzi e c'è poco capitale di rischio. L'indebitamento ha come conseguenza lo scudo fiscale. Si prenda un'azienda con 100 euro di capitale: se ha il 60% di debito bancario e il 40% di equity, rispetto a una che ha tutto equity, quella indebitata ha lo scudo fiscale su quei 60 euro. Le due aziende non giocano la stessa partita, perché quella indebitata può sfruttare il risparmio fiscale.
>
> Il docente non è molto convinto del terzo elemento: l'appartenenza a un settore dovrebbe determinare quanti costi fissi o variabili si hanno e se i ricavi sono ciclici, ma non se l'azienda è molto o poco indebitata. L'indebitamento ha però un impatto sul beta. Alla conclusione del modulo sul costo del capitale si arriverà a un ragionamento secondo cui avrebbe senso togliere l'effetto dell'indebitamento dal calcolo del beta, tanto più in Italia, dove le aziende sono molto indebitate.

La tabella associa i valori del beta ai settori tipici.

| Valore | Interpretazione | Settori tipici |
|---|---|---|
| $\beta > 1$ | Il titolo (l'azienda) varia più che proporzionalmente al variare del mercato | Settori fortemente ciclici: automotive, costruzioni, lusso e alta moda, turismo, compagnie aeree, high-tech |
| $\beta = 1$ | Il titolo (l'azienda) varia proporzionalmente al variare del mercato | Settori ciclici al pari dell'economia: trasporti, assicurazioni |
| $0 < \beta < 1$ | Il titolo (l'azienda) varia meno che proporzionalmente al variare del mercato e assorbe il ciclo economico | Settori non ciclici: energie rinnovabili, utilities, farmaceutico, healthcare, gestione rifiuti, telecomunicazioni, beni di consumo primari |

Le aziende dei settori non ciclici hanno in comune contratti pluriennali, tariffe regolate (nelle utilities) e abbonamenti periodici.

> [!lezione] Dalla lezione del 19 novembre 2026: come si leggono i tre comportamenti del beta
> Con $\beta > 1$ il beta amplifica le variazioni del mercato: con $\beta = 1{,}5$, se il mercato sale dell'1% il titolo sale dell'1,5%, cioè più del mercato. Il docente cita come esempi l'automotive, le compagnie aeree e le aziende di costruzioni e materiali edili. In un momento di crescita economica e di prosperità le persone cambiano la macchina, fanno più viaggi o comprano casa, ed è comprensibile che quando cresce l'economia questi settori abbiano comportamenti amplificati rispetto all'andamento del mercato.
>
> Con $\beta = 1$, o molto vicino a uno, il titolo, cioè l'azienda, varia in misura proporzionale al mercato, sale e scende come il mercato ed è ciclico al pari dell'economia. Il docente cita come settori i trasporti e la logistica, le assicurazioni e tutta la GDO.
>
> Con $0 < \beta < 1$ i titoli si muovono in modo più tiepido del mercato e lo seguono in maniera meno amplificata: utilities, farmaceutici e beni essenziali. Non sono settori in cui si acquista per impulso, per euforia o per un picco di disponibilità di reddito: non si accendono tutte le luci di casa insieme né si fa scorta di medicine perché si potrebbe comprare tutto l'outlet. È prevedibile che questi settori siano più indifferenti al mercato quando sale e scende.
>
> Il beta minore di zero non compare tra i casi. Sarebbe paradossale: un titolo che va nella direzione opposta rispetto al mercato, per cui il mercato sale e il titolo scende, o il titolo sale e il mercato scende. Sono casi talmente eccezionali da non essere inseriti nelle casistiche, per cui tecnicamente il beta si considera quasi sempre maggiore di zero.

## Il beta unlevered e il tasso di sconto di un progetto

Usare un tasso di sconto per valutare un progetto pone tre criticità:

1. la struttura finanziaria del progetto non è nota al momento della valutazione (quanto equity e quanto debito);
2. l'impresa può non essere quotata, e quindi difficilmente confrontabile;
3. il progetto può essere realizzato in un settore diverso da quello in cui l'impresa opera abitualmente.

La soluzione è usare il **beta unlevered** dell'impresa, o del settore, in cui il progetto viene lanciato. Si ipotizza cioè che il progetto sia finanziato interamente con equity: il costo del capitale proprio in assenza di debito, $r_{E,D=0} = r_0$, si ottiene con il beta unlevered:

$$r_0 = r_f + \beta_U\,(R_m - r_f)$$

dove $r_f$ e il premio per il rischio di mercato sono determinati secondo una delle due alternative di trattamento del rischio Paese. La scelta si giustifica anche perché un progetto dovrebbe essere accettato o respinto a prescindere dai benefici derivanti dalla politica finanziaria: il debito riduce il costo delle fonti di finanziamento, ma è un effetto della struttura finanziaria e non del progetto.

> [!lezione] Dalla lezione del 19 novembre 2026: perché il beta levered pone problemi
> Il beta incorpora per definizione la leva finanziaria, e questo crea due problemi. Il primo è che al momento della valutazione di un progetto non si sa quanto sia indebitata l'azienda e in che misura il progetto sarà finanziato, con soldi propri o con soldi dei creditori: occorre valutare la remunerazione del progetto e il suo beta, ma nel beta c'è già la leva finanziaria.
>
> Il secondo è che i beta si prendono dalle tavole disponibili su internet, che arrivano dall'America, dove la maggior parte delle aziende è quotata, ha molto capitale proprio e poco capitale di terzi. Per calcolare il beta della Diadora in Italia, per esempio, azienda con un passivo e un capitale di terzi enormi rispetto all'equity, si andrebbe a prendere il beta del settore shoes o sportswear americano, che è un beta di aziende quasi prive di debito perché sono in borsa e hanno tutto capitale proprio. Anche questo punto indica perplessità nell'uso del beta così com'è, cioè del beta levered.
>
> A questi due problemi si aggiunge un possibile disallineamento tra il progetto da valutare, che può trovarsi in un settore diverso da quello dell'azienda, e il tipo di beta disponibile. La soluzione è il beta unlevered $\beta_U$ al posto del $\beta_L$: se si toglie l'effetto del debito dal beta, si può applicare un beta che rappresenta la ciclicità di quel settore, a prescindere dal fatto che l'investimento, il progetto o l'azienda siano molto o poco indebitati.

Il beta osservato sul titolo di un'impresa comparabile, che riflette la sua struttura finanziaria, è il beta levered $\beta_L$. Il beta unlevered $\beta_U$ è quello depurato dall'effetto della leva. Il calcolo dipende dal segno della posizione finanziaria netta (PFN), cioè del debito finanziario al netto della cassa, dell'impresa comparabile; $E$ è il valore di mercato del capitale proprio.

> [!abstract] Definizione
> Se la PFN è **positiva**, l'attivo è finanziato da equity e debito (Assets = Equity + Debts):
>
> $$\beta_U = \frac{\beta_L}{1 + \dfrac{PFN}{E}(1-t_c)}$$
>
> Se la PFN è **negativa**, la cassa supera il debito e l'attivo, sommato alla cassa, è finanziato interamente dal capitale proprio (Assets + Cash = Equity):
>
> $$\beta_U = \beta_L\,\frac{E}{E+PFN}$$
>
> In entrambe le formule il beta del debito è implicitamente considerato pari a zero.

![](assets/fstr-02/fig02.png)

**Figura 2** — Struttura finanziaria e beta unlevered: con PFN positiva l'attivo è finanziato da equity e debito, con PFN negativa l'attivo sommato alla cassa coincide con l'equity. A ciascun caso corrisponde la propria formula del beta unlevered, con beta del debito nullo.

Le due formule si raccordano in corrispondenza di PFN nulla, dove entrambe danno $\beta_U = \beta_L$. Con PFN positiva $\beta_U < \beta_L$: il debito accresce il beta dell'equity rispetto a quello delle attività. Con PFN negativa il fattore $E/(E+PFN)$ supera 1 e quindi $\beta_U > \beta_L$: la cassa, trattata come debito negativo con beta nullo, riduce il beta dell'equity, per cui il beta delle sole attività operative è più alto di quello osservato.

> [!lezione] Dalla lezione del 19 novembre 2026: la formula con PFN negativa e l'uso negli esercizi
> Le formule del beta unlevered sono la 7.19 bis e la 7.20 del libro, riportate nelle slide. Per convenzione un'azienda con debito ha una PFN positiva e un'azienda con cassa ha una PFN negativa.
>
> Nella formula con PFN negativa il cambiamento principale è che non compare il fattore $(1 - t_c)$, cioè lo scudo fiscale: chi ha cassa e non ha debito non ha neanche lo scudo fiscale sugli interessi, perché non paga interessi se ha soldi in tasca invece di debiti bancari. Per coerenza il beta si pulisce anche in caso di cassa. L'obiettivo è ragionare sul beta senza l'effetto del debito e anche senza l'effetto della cassa, perché il progetto va accettato o respinto a prescindere dal fatto che si abbia debito o cassa.
>
> Il docente avverte che negli esercizi l'effetto del debito si toglie con le due formule del beta unlevered: se l'azienda è indebitata, cioè ha una PFN positiva, si usa la prima formula; se la PFN di bilancio è negativa, cioè c'è cassa, si usa l'altra.
