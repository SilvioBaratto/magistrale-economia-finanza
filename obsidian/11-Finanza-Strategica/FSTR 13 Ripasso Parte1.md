---
title: "Riepilogo I: flussi di cassa, costo del capitale e multipli"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_13_Ripasso-Parte1.pdf"
text_layer: true
verified: true
generated: 2026-08-30
---

## Inquadramento

Il capitolo riepiloga i concetti e le formule della prima parte del corso: i flussi di cassa e i soggetti a cui spettano, i criteri di valutazione degli investimenti, il costo del capitale e il Beta, il capitale investito netto e il capitale circolante netto, la valutazione assoluta e i multipli di mercato. Le definizioni sono richiamate in forma sintetica e rinviano ai capitoli in cui gli argomenti sono sviluppati.

## I flussi di cassa e i loro beneficiari

### Beneficiari e tassi di sconto

Il **FCFO** è il flusso di cassa della gestione operativa. Nella forma usata per la valutazione, al netto degli investimenti in capitale fisso, è indicato anche come FCFF. Si ottiene dal margine operativo lordo sottraendo la variazione del capitale circolante netto operativo, il flusso fiscale operativo e gli investimenti, e si colloca prima degli oneri finanziari: non dipende da come l'attività è finanziata. Spetta perciò a tutti i finanziatori dell'impresa, creditori e azionisti.

Il **FCFE** è il flusso che resta dopo la gestione straordinaria, gli oneri finanziari al netto dello scudo fiscale e la variazione dei debiti finanziari. Spetta ai soli azionisti.

| Flusso | A chi spetta | Tasso di attualizzazione | Valore che ne risulta |
|---|---|---|---|
| FCFO (FCFF) | creditori e azionisti | WACC | enterprise value, $V$ |
| FCFE | azionisti | costo dell'equity, $r_E$ | equity value, $E$ |

$$V = \sum_{t=1}^{\infty} \frac{FCFF_t}{(1+WACC)^t} \qquad E = \sum_{t=1}^{\infty} \frac{FCFE_t}{(1+r_E)^t} \qquad E = V - PFN$$

La costruzione dei due flussi a partire dal margine operativo lordo è trattata in [[FSTR 01-full Progetti di Investimento|i flussi FCFO e FCFE nei progetti di investimento]]; le formule generali dei metodi DCF sono in [[FSTR 03 Modelli Valutazione Finanziaria Parte1|i modelli di valutazione finanziaria]].

### Il flusso adatto all'enterprise value

Per calcolare l'enterprise value è appropriato il FCFO. L'enterprise value è il valore del capitale investito nell'attività operativa, indipendente dal modo in cui questa è finanziata, e il FCFO è il flusso calcolato prima della remunerazione dei finanziatori, che il WACC sconta tenendo conto del costo sia del debito sia del capitale proprio. Il FCFE è invece già al netto degli oneri verso i creditori: scontato al costo dell'equity restituisce direttamente il valore del capitale proprio, non l'enterprise value. Il passaggio tra le due grandezze è $EV = MK\,CAP + PFN$, cioè $MK\,CAP = EV - PFN$.

### La remunerazione dei creditori

I creditori sono remunerati con gli interessi, cioè gli oneri finanziari, e con il rimborso del capitale prestato. Nello schema dei flussi queste voci formano l'area del capitale di terzi: oneri finanziari netti e variazione dei debiti finanziari.

I flussi verso i creditori si attualizzano al costo del debito $r_D$, il tasso di interesse effettivo del prestito, che compensa il creditore per il valore del tempo e per il rischio di mancato rimborso. Con più finanziamenti $r_D$ è la media dei tassi ponderata per il valore di ciascun debito:

$$r_D = \frac{\sum_i \text{Debito}_i \times \text{tasso}_i}{\sum_i \text{Debito}_i}$$

Il tasso $r_D$ è al lordo delle imposte, perché il creditore incassa interessi lordi. L'effetto fiscale entra nel calcolo del WACC attraverso il fattore $(1-t_c)$, cioè attraverso lo scudo fiscale. Per un debito $D$ costante e perpetuo gli interessi annui sono $D \cdot r_D$ e il loro valore attuale al tasso $r_D$ è $D \cdot r_D / r_D = D$, pari al valore del debito.

## I criteri di valutazione degli investimenti: il tempo di recupero

I cinque criteri di valutazione di un progetto con investimento iniziale $I_0$ sono riassunti nella tabella; pregi, limiti e campi di applicazione di ciascuno sono trattati in [[FSTR 01-full Progetti di Investimento|i criteri di valutazione dei progetti di investimento]].

| Criterio | Formula | Regola di decisione |
|---|---|---|
| Valore attuale netto (VAN) | $-I_0 + \sum_{t=1}^{N} \dfrac{FCFO_t}{(1+WACC)^t}$ | $VAN > 0$ |
| Tasso interno di rendimento (TIR) | tasso $r$ tale che $VAN(r) = 0$ | $TIR > WACC$ |
| Indice di redditività (IR) | $\dfrac{VA}{I_0}$ | $IR > 1$ |
| Tempo di recupero (TR) | minimo $t$ tale che $\sum_{i=1}^{t} FCFO_i \geq I_0$ | $t \leq$ cut-off |
| Tempo di recupero attualizzato (TRA) | minimo $t$ tale che $\sum_{i=1}^{t} \dfrac{FCFO_i}{(1+WACC)^i} \geq I_0$ | $t \leq$ cut-off |

Il tempo di recupero è legato a un cut-off arbitrario. Il TR misura gli anni necessari perché i flussi cumulati coprano l'investimento iniziale, ma per decidere se il progetto sia accettabile occorre confrontarlo con un tempo limite fissato dall'impresa, che non discende da alcuna grandezza economica. La stessa arbitrarietà vale per il TRA. Le soglie degli altri criteri hanno invece un significato economico: il VAN positivo, il TIR superiore al WACC e l'IR superiore a 1 esprimono tutti un rendimento maggiore del costo-opportunità del capitale. Il TR presenta inoltre due limiti: nella forma non attualizzata ignora il valore del tempo e il rischio, e in entrambe le forme ignora i flussi successivi al recupero.

> [!example] Esempio
> Un progetto richiede un esborso iniziale di 152.000 e genera un flusso costante di 65.000 in ciascuno dei quattro anni successivi. Il WACC è il 9%.
>
> | Anno | Flusso | Flusso cumulato | Flusso attualizzato | Attualizzato cumulato |
> |---|---|---|---|---|
> | 1 | 65.000 | 65.000 | 59.633 | 59.633 |
> | 2 | 65.000 | 130.000 | 54.709 | 114.342 |
> | 3 | 65.000 | 195.000 | 50.192 | 164.534 |
> | 4 | 65.000 | 260.000 | 46.048 | 210.582 |
>
> Alla fine del secondo anno il flusso cumulato (130.000) è inferiore a 152.000; alla fine del terzo lo supera (195.000). Il tempo di recupero è quindi di 3 anni. Il cumulato attualizzato supera 152.000 solo nel terzo anno (164.534), per cui anche il tempo di recupero attualizzato è di 3 anni.
>
> Il VAN del progetto è $210.582 - 152.000 = 58.582$, positivo. Con un cut-off di due anni il progetto sarebbe respinto da entrambi i criteri di recupero, con un cut-off di tre anni accettato: la conclusione dipende dalla soglia scelta e non da una proprietà del progetto.

## Il costo del capitale: premio per il rischio e Beta

### Le componenti del premio per il rischio

Il costo del capitale proprio si determina con il CAPM:

$$r_E = r_f + \beta\,(R_m - r_f)$$

Il termine $\beta\,(R_m - r_f)$ è il **premio per il rischio** richiesto all'azionista. È il prodotto di due fattori: il Beta, che misura la quantità di rischio sistematico, e il premio per il rischio di mercato $(R_m - r_f)$, che ne esprime il prezzo.

Per un'impresa localizzata in un Paese con rischio superiore al minimo, il premio per il rischio di mercato ha a sua volta due componenti. La prima è il **MRP** (*Market Risk Premium*), il premio richiesto per investire nel mercato azionario anziché in un titolo privo di rischio: si calcola sui mercati con rischio Paese molto contenuto, tipicamente gli Stati Uniti, riflette il rischio sistematico globale e viene aggiornato ogni anno da Damodaran (4,12% nel 2024). La seconda è il **Country Risk Premium** (CRP), il premio specifico per il rischio del Paese, ricavato dal CDS sul debito sovrano (1,08% per l'Italia, nel 2024). Il premio di mercato complessivo è $4{,}12\% + 1{,}08\% = 5{,}20\%$ e il costo del capitale proprio diventa

$$r_E = r_f + \beta\,(MRP + CRP)$$

dove per le imprese italiane $r_f$ è il rendimento del Bund tedesco a 10 anni. In alternativa il rischio Paese si include nel tasso privo di rischio, usando il rendimento del titolo di Stato del Paese di riferimento, e il premio per il rischio coincide con il solo MRP. Le due impostazioni sono equivalenti se applicate in modo coerente. Il calcolo con i valori numerici è sviluppato in [[FSTR 02-full Costo del Capitale|il costo del capitale e il rischio Paese]].

### Il Beta e la sua interpretazione

Il **Beta** misura quanto varia il rendimento di un titolo al variare del rendimento di mercato:

$$\beta = \frac{COV(R_i; R_m)}{VAR(R_m)}$$

dove $R_i$ è il rendimento del titolo e $R_m$ quello del mercato. Dipende dal rischio operativo, legato al rapporto tra costi fissi e variabili, e dal rischio finanziario, legato alla leva. I valori considerati nel corso si interpretano come segue.

| Valore | Interpretazione | Settori tipici |
|---|---|---|
| $\beta > 1$ | il titolo varia più che proporzionalmente al mercato | settori fortemente ciclici: automotive, costruzioni, lusso e alta moda, turismo, compagnie aeree, high-tech |
| $\beta = 1$ | il titolo varia in proporzione al mercato | settori ciclici come l'economia: trasporti, assicurazioni |
| $0 < \beta < 1$ | il titolo varia meno che proporzionalmente al mercato e assorbe il ciclo economico | settori non ciclici con contratti pluriennali, tariffe regolate o abbonamenti: utilities, energie rinnovabili, farmaceutico, healthcare, gestione rifiuti, telecomunicazioni, beni di consumo primari |

In teoria il Beta può essere anche negativo, se il titolo tende a muoversi in senso opposto al mercato; è un caso eccezionale e non compare negli schemi settoriali.

## La valutazione assoluta

La **valutazione assoluta** si concentra sull'impresa e non sul confronto con altre. Si fonda sull'analisi delle sue caratteristiche (modello di business, strategie, management, patrimonio) e sulla previsione delle performance economico-finanziarie future. Considera le politiche finanziarie, di finanziamento e di dividendo e misura il rischio operativo e finanziario. Procede con un criterio analitico di stima e fornisce **valori intrinseci**, detti anche valori finanziari o fondamentali, il cui significato economico poggia sul principio di convenienza economica dell'investimento in capitale di rischio aziendale. Lo strumento tipico è il DCF, che attualizza i flussi attesi a un tasso coerente con il loro rischio.

La valutazione relativa, al contrario, esprime il valore dell'impresa per confronto con imprese simili e conduce a valori di mercato, detti prezzi probabili. Sul piano professionale le due valutazioni si associano in modo complementare; le formule dei modelli sono in [[FSTR 03 Modelli Valutazione Finanziaria Parte1|i metodi DCF]].

## Capitale investito netto e capitale circolante netto

### Definizioni

Il **capitale circolante netto** (CCN) è il capitale impegnato nella gestione corrente. Aumenta con i crediti commerciali e con le rimanenze di magazzino e diminuisce con i debiti verso fornitori, che sono le sue grandezze principali:

$$CCN = \text{crediti commerciali} + \text{rimanenze} - \text{debiti verso fornitori}$$

Il **capitale investito netto** (CIN) comprende il CCN e anche il capitale immobilizzato:

$$CIN = CCN + \text{immobilizzazioni caratteristiche nette}$$

La differenza tra i due aggregati è quindi il capitale fisso: il CCN è una componente del CIN. Dal lato delle fonti il CIN è uguale a patrimonio netto più PFN.

### L'effetto del CCN sulla liquidità

Una variazione del CCN modifica la liquidità generata dalla gestione con segno opposto. Indicando con $\Delta CCN$ la differenza tra il CCN di fine e di inizio esercizio, il flusso di cassa della gestione corrente, prima delle imposte operative, è

$$\text{Cash flow gestionale lordo} = MOL - \Delta CCN$$

Se il CCN aumenta, a parità del resto, la liquidità generata diminuisce: l'impresa ha più crediti da incassare o più scorte da finanziare e il cash flow gestionale si riduce dell'importo dell'aumento. Una riduzione del CCN libera invece liquidità, con effetto uguale e contrario.

Se aumentano i debiti verso fornitori, a parità di crediti commerciali e rimanenze, il CCN diminuisce: i fornitori finanziano una parte dell'attività e la liquidità generata aumenta. Se aumentano le rimanenze, a parità di crediti commerciali e debiti verso fornitori, il CCN aumenta: le scorte assorbono liquidità e la liquidità generata diminuisce.

### Esempi svolti

> [!example] Esempio
> **Primo caso.** L'EBITDA è 1.000 e il CCN nell'anno è aumentato di 300. Il flusso di cassa operativo è
>
> $$1.000 - 300 = 700$$
>
> **Secondo caso.** L'EBITDA è $-200$ e il CCN nell'anno è diminuito di 700, quindi $\Delta CCN = -700$. Il flusso di cassa operativo è
>
> $$-200 - (-700) = 500$$
>
> Nel secondo caso il flusso è positivo nonostante l'EBITDA negativo, perché la riduzione del CCN libera 700 di liquidità: per esempio perché si incassano crediti, si smobilizzano scorte o aumentano i debiti verso fornitori. Nei dati non figurano imposte operative, per cui i risultati corrispondono al cash flow gestionale lordo.

Il capitale circolante è oggetto di verifica anche nelle imprese da acquisire, dove si controllano l'andamento e la stagionalità del suo livello ([[FSTR 08 Financial Due Diligence|il CCN nella financial due diligence]]).

## I multipli di mercato

Un multiplo è il rapporto tra un valore osservato, di assets o di equity, e una grandezza economica o patrimoniale di riferimento. I multipli appartengono alla valutazione relativa e si dividono in base all'aggregato di valore posto al numeratore: nell'ottica assets il valore d'impresa (EV/Sales, EV/EBITDA, EV/EBIT, EV/CIN), nell'ottica equity il prezzo o la capitalizzazione (P/E, P/cash flow reddituale, P/E adjusted, P/BV).

### Multipli di borsa e multipli delle transazioni concluse

I multipli di borsa non coincidono con quelli delle transazioni concluse: le due categorie hanno fonti diverse.

| Multipli di borsa | Multipli delle transazioni concluse |
|---|---|
| ricavati dai prezzi di borsa | ricavati da compravendite di aziende |
| riferiti a transazioni di minoranza | riferiti a pacchetti di maggioranza o di minoranza qualificata |
| risultato di numerose transazioni | risultato di una singola transazione specifica |

I prezzi dei pacchetti di controllo incorporano i benefici del controllo (si veda [[FSTR 11 Le Sinergie|il premio di controllo e i benefici privati]]), per cui le due categorie non sono intercambiabili nella valutazione di un'impresa. Il procedimento di applicazione ai casi di imprese non quotate è descritto in [[FSTR 06 Multipli di Borsa lez01|il funzionamento dei multipli di borsa]].

### Le versioni del denominatore

Il denominatore del multiplo può essere una grandezza storica, detta versione *current*, una grandezza previsionale, detta *leading*, oppure una grandezza cumulata dei dodici mesi precedenti, detta *trailing* o LTM (*last twelve months*). La versione *trailing* si riferisce quindi a una grandezza cumulata, consuntiva, e non previsionale: ha senso solo per i dati economici, che sono flussi, e si ottiene per esempio sommando i risultati dei quattro trimestri più recenti.
