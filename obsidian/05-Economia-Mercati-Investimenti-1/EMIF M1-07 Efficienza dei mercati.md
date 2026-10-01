---
title: "Efficienza dei mercati"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-07_Efficienza-dei-mercati.pdf"
pages: 61
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: le prime evidenze e il random walk

**Kendall (1953)** analizza le variazioni del prezzo delle azioni. Principali risultati:
- I prezzi hanno la stessa probabilità di aumentare o diminuire.
- I movimenti passati dei prezzi non predicono le variazioni future.

**Interpretazione**: i prezzi delle azioni seguono un *random walk* (passeggiata aleatoria); le variazioni dei prezzi sono indipendenti e imprevedibili.

**Questione chiave**: perché i prezzi si comportano in modo apparentemente casuale?

### Processo random walk

Sia $p_{it+1} = \ln P_{it+1}$ il logaritmo del prezzo del titolo $i$. Nel caso più semplice, i prezzi evolvono secondo

$$p_{it+1} = p_{it} + e_{it+1}$$

dove $e_{it+1}$ rappresenta le nuove informazioni (innovazione), con $E(e_{it+1}\mid I_t) = 0$.

**Implicazione**: le variazioni del logaritmo del prezzo (rendimenti) sono imprevedibili; la migliore previsione del logaritmo del prezzo domani è il logaritmo del prezzo oggi:

$$E(p_{it+1}\mid I_t) = p_{it}$$

### Random walk con drift

Più in generale, i prezzi possono avere un rendimento atteso costante (drift, o deriva):

$$p_{it+1} = p_{it} + \mu_i + e_{it+1}$$

dove $\mu_i$ è il rendimento atteso (drift nei prezzi in logaritmo) ed $e_{it+1}$ è il rendimento inatteso (nuova informazione), con $E(e_{it+1}\mid I_t)=0$.

**Interpretazione economica**: $\mu_i$ riflette la remunerazione del rischio, tipicamente determinata da modelli di asset pricing di equilibrio (per esempio, il CAPM).

**Implicazione**: i rendimenti sono prevedibili solo nella misura in cui riflettono il rischio a cui è esposto il titolo (termine di drift); la componente restante dei rendimenti rimane imprevedibile:

$$E(p_{it+1}\mid I_t) = p_{it} + \mu_i$$

*(slide 3–5)*

## L'ipotesi del mercato efficiente (EMH)

> [!abstract] Definizione
> Le nuove informazioni sono intrinsecamente imprevedibili e i prezzi reagiscono rapidamente alle nuove informazioni.
>
> **Ipotesi del mercato efficiente (EMH)**
> - **Definizione**: i prezzi riflettono in modo completo e immediato tutte le informazioni disponibili.
> - **Implicazione**: i rendimenti attesi sono determinati solo dal rischio (modelli di equilibrio) $\Rightarrow$ impossibile "battere il mercato" al netto di aggiustamenti per il rischio.
>
> **Una precisazione**: la raccolta e l'elaborazione di informazioni non è gratuita; gli investitori raccolgono informazioni solo se i benefici superano i costi.
>
> ### Informazione, concorrenza e prezzi
>
> L'informazione è l'input chiave nei mercati finanziari, poiché determina le aspettative degli investitori sui rendimenti futuri e i rischi. La concorrenza tra investitori implica che qualsiasi informazione utile venga rapidamente sfruttata attraverso il trading, e dunque rapidamente incorporata nei prezzi.
>
> Man mano che più investitori agiscono sulla base della stessa informazione, le opportunità di profitto vengono eliminate dalla concorrenza, per cui il *mispricing* non può persistere sistematicamente.
>
> La prospettiva di rendimenti più elevati motiva l'acquisizione di informazioni, ma i rendimenti decrescenti e la concorrenza limitano la redditività di tale attività (**paradosso di Grossman-Stiglitz**).
>
> ### EMH e aggiustamenti dei prezzi
>
> L'EMH può essere vista come una semplice sequenza: nuove informazioni arrivano in modo imprevedibile, gli investitori rispondono ad esse e i prezzi si aggiustano di conseguenza. Poiché questo aggiustamento è rapido, i prezzi riflettono quasi immediatamente le nuove informazioni, impedendone lo sfruttamento sistematico.
>
> Dopo l'aggiustamento, i rendimenti attesi sono nuovamente allineati al rischio, come determinato dalle relazioni di equilibrio. L'implicazione chiave è che opportunità di profitto possono emergere momentaneamente quando arrivano nuove informazioni, ma scompaiono rapidamente a causa della concorrenza.

*(slide 6–8)*

## Il gioco equo, martingalità e la distinzione dal random walk

> [!tip] Teorema
> ### Un gioco equo
>
> I prezzi al tempo $t$ riflettono completamente l'insieme informativo $I_t$, dunque le componenti prevedibili dei rendimenti sono già incorporate nei prezzi. I rendimenti attesi sono quindi determinati dal rischio, non da flussi informativi sfruttabili. Gli investitori vengono compensati solo per aver assunto rischio, senza la possibilità di ottenere sistematicamente rendimenti aggiuntivi.
>
> **Un gioco equo**:
>
> $$E\big(r_{it+1} - E(r_{it+1}\mid I_t)\big) = 0$$
>
> **Perché "equo"?**
> - Dato $I_t$, nessuna strategia produce extrarendimenti attesi positivi.
> - Il rendimento atteso dal trading è pari al suo costo, quindi il "gioco" ha valore netto medio pari a zero.
> - I guadagni/perdite realizzati riflettono solo notizie imprevedibili, non un vantaggio informativo sistematico.
>
> ### Random walk vs. gioco equo
>
> Il random walk è un caso speciale all'interno della EMH:
>
> $$\text{Random walk} \Rightarrow \text{Gioco equo (EMH)}$$
>
> Tuttavia il viceversa non è vero:
>
> $$\text{Gioco equo (EMH)} \not\Rightarrow \text{Random walk}$$
>
> **Distinzione fondamentale**
> - *Random walk*: le variazioni del prezzo sono i.i.d., quindi i rendimenti attesi sono costanti e i rendimenti sono completamente imprevedibili.
> - *Gioco equo*: condizionatamente a $I_t$, i rendimenti anomali hanno aspettativa nulla, ma i rendimenti attesi possono variare nel tempo.
>
> Il random walk impone quindi restrizioni più stringenti, escludendo ogni variazione prevedibile nei rendimenti attesi.
>
> ### Un gioco equo che non è un random walk
>
> Si consideri la scomposizione
>
> $$r_{it+1} = E(r_{it+1}\mid I_t) + e_{it+1}, \qquad E(e_{it+1}\mid I_t) = 0$$
>
> Se i rendimenti attesi variano nel tempo in funzione del rischio, allora:
> - i rendimenti possono essere prevedibili tramite $E(r_{it+1}\mid I_t)$, riflettendo premi per il rischio variabili nel tempo;
> - ma $e_{it+1}$ rimane imprevedibile.
>
> **Implicazione**: il processo dei rendimenti può corrispondere a un gioco equo anche se non segue un random walk. La prevedibilità dei rendimenti riflette premi per il rischio variabili nel tempo, non extraprofitti sistematici.
>
> **Conclusione**: l'EMH consente rendimenti attesi prevedibili, ma esclude profitti extra prevedibili basati sulle informazioni disponibili.
>
> ### Martingalità
>
> Si ricordi la rappresentazione del gioco equo
>
> $$r_{it+1} = E(r_{it+1}\mid I_t) + e_{it+1}, \qquad E(e_{it+1}\mid I_t) = 0$$
>
> che mostra come solo i rendimenti residui siano imprevedibili. Secondo l'EMH, i prezzi riflettono tutte le informazioni disponibili e si aggiustano immediatamente alle ultime notizie.
>
> In assenza di arbitraggio, esiste un fattore di sconto stocastico $m_{t+1}$ (o una misura martingala-equivalente $E^{\hat\pi}[\cdot]$) tale che:
> - il prezzo scontato è una martingala;
> - i guadagni attesi corretti per il rischio sono zero.
>
> Questo fornisce un benchmark più generale rispetto al random walk:
> - i rendimenti attesi $E(r_{it+1}\mid I_t)$ possono variare nel tempo;
> - i rendimenti possono quindi essere prevedibili attraverso $E(r_{it+1}\mid I_t)$;
> - ma i rendimenti extra (corretti per il rischio) restano imprevedibili.
>
> La prevedibilità dovuta a premi per il rischio variabili nel tempo è pienamente coerente con l'EMH.
>
> ### Implicazioni economiche
>
> **Intuizione economica**: i prezzi reagiscono immediatamente alle notizie; se ci si aspetta che un prezzo aumenti domani, aumenterà già oggi; dopo aver aggiustato per il rischio, gli aumenti e le diminuzioni di prezzo sono ugualmente probabili.
>
> Qualsiasi componente prevedibile nei rendimenti, cioè $E(r_{it+1}\mid I_t)$, riflette premi per il rischio variabili nel tempo piuttosto che inefficienza. Il random walk è un caso speciale ottenuto quando i rendimenti attesi sono costanti.

*(slide 9–13)*

## Efficienza allocativa vs. informativa, e le tre forme di efficienza

> [!abstract] Definizione
> ### Efficienza allocativa vs. informativa
>
> **Efficienza allocativa**: le risorse vengono allocate in modo ottimale tra gli agenti; in finanza $\Rightarrow$ condivisione efficiente del rischio (*risk sharing*).
>
> **Efficienza informativa**: i prezzi riflettono le informazioni disponibili; EMH $\Rightarrow$ "il prezzo è corretto" per date informazioni.
>
> **"Il prezzo è corretto"**: il prezzo coincide con la migliore stima del valore fondamentale data $I_t$. Vi può essere un errore di prezzo, ma non può essere sfruttato sistematicamente; gli errori sono imprevedibili, non persistenti.
>
> ### Forme di efficienza informativa (Fama, 1970, 1991)
>
> - **Forma debole**: i prezzi riflettono le informazioni di mercato passate.
> - **Forma semi-forte**: i prezzi riflettono tutte le informazioni pubbliche.
> - **Forma forte**: i prezzi riflettono tutte le informazioni, comprese quelle riservate.
>
> **Figura (diagramma di Venn, p. 15)** — Tre insiemi annidati: "Past market info" (il più piccolo) $\subset$ "All public info" $\subset$ "All public & private info" (il più grande). Mostra come ciascuna forma di efficienza informativa incorpori un insieme di informazioni via via più ampio, dalle sole quotazioni passate fino a tutte le informazioni pubbliche e private.
>
> ### Implicazioni dell'efficienza informativa
>
> Quale informazione non può essere utilizzata per guadagnare profitti anomali?
>
> - **Forma debole**: i prezzi passati non possono generare profitti $\Rightarrow$ l'analisi tecnica è inefficace.
> - **Forma semi-forte**: le informazioni pubbliche non possono generare profitti $\Rightarrow$ l'analisi fondamentale è inefficace.
> - **Forma forte**: anche le informazioni private non possono generare profitti $\Rightarrow$ l'insider trading non produce rendimenti anomali.
>
> Ciascuna di queste forme di efficienza definisce un diverso punto di riferimento per l'efficienza informativa del mercato.
>
> ### Forme di analisi finanziaria
>
> - **Analisi tecnica**: usa prezzi passati e schemi di trading; si basa sulla prevedibilità dei rendimenti $\Rightarrow$ richiede la violazione dell'efficienza in forma debole.
> - **Analisi fondamentale**: usa informazioni specifiche dell'azienda e macroeconomiche; cerca deviazioni di prezzo rispetto ai fondamentali $\Rightarrow$ richiede la violazione dell'efficienza semi-forte.
>
> Entrambi gli approcci assumono che i prezzi devino dal valore fondamentale in modo prevedibile.
>
> ### Cosa rende i mercati informativamente efficienti?
>
> Gli investitori scambiano titoli sulla base dell'informazione disponibile per sfruttare mispricing percepito. I loro scambi generano una pressione sui prezzi che elimina il mispricing. Le informazioni pubbliche sono rapidamente incorporate nei prezzi. Le informazioni private creano incentivi all'analisi finanziaria e al trading.
>
> $\Rightarrow$ La concorrenza tra investitori informati crea efficienza informativa.
>
> ### Il paradosso di Grossman-Stiglitz
>
> Le informazioni sono costose da acquisire ed analizzare.
>
> In presenza di mercati perfettamente efficienti:
> - i prezzi riflettono pienamente tutte le informazioni disponibili;
> - nessun investitore potrebbe ottenere rendimenti extra dalle informazioni a disposizione;
> - $\Rightarrow$ nessun incentivo a raccogliere informazioni costose.
>
> Se nessuno raccoglie informazioni: i prezzi non possono riflettere completamente i fondamentali e il mispricing persiste.
>
> **Implicazione di equilibrio**: i mercati potranno essere solo parzialmente efficienti; i prezzi riflettono le informazioni, ma non perfettamente; gli investitori informati guadagnano a sufficienza per coprire il costo della raccolta ed analisi delle informazioni.
>
> $\Rightarrow$ Una piccola quantità di inefficienza è necessaria per sostenere la produzione di informazioni (Grossman e Stiglitz, 1980).
>
> ### Chi ha incentivi a raccogliere informazioni?
>
> L'acquisizione di informazioni comporta per lo più costi fissi.
>
> **Economie di scala**: i costi di dati e analisi non crescono proporzionalmente con i titoli; i portafogli più grandi possono distribuire questi costi su più capitale.
>
> $\Rightarrow$ Gli incentivi a raccogliere informazioni differiscono tra gli investitori: i piccoli investitori si affidano soprattutto a informazioni pubbliche; gli investitori grandi e istituzionali investono nella produzione di informazioni.
>
> **Ruolo dei gestori professionali**: specializzati nella raccolta e nell'elaborazione delle informazioni, fanno trading sulla base del mispricing percepito e contribuiscono a incorporare le informazioni nei prezzi.
>
> L'efficienza del mercato dipende dalla presenza di operatori informati.

*(slide 14–20)*

## I tre approcci per testare l'EMH

L'EMH fornisce un insieme di vincoli teorici sui prezzi e i rendimenti dei titoli. Questi vincoli possono essere testati empiricamente:
- I rendimenti sono prevedibili usando le informazioni disponibili?
- I prezzi si aggiustano immediatamente alle nuove informazioni?
- Gli investitori possono guadagnare sistematicamente rendimenti extra?

**Tre approcci principali**
1. **Studi su prevedibilità**: i rendimenti sono prevedibili usando informazioni passate o pubbliche?
2. **Studi di eventi**: con quale rapidità e accuratezza i prezzi reagiscono alle nuove informazioni?
3. **Studi su extrarendimenti**: gli investitori possono battere il mercato sistematicamente?

Questi test colgono diversi aspetti dell'efficienza informativa.

*(slide 21)*

## 1) Studi su prevedibilità — impostazione e origini della prevedibilità

Un modo naturale per valutare l'EMH è testare se i rendimenti siano prevedibili sulla base delle informazioni disponibili al tempo $t$, ossia $I_t$. L'EMH implica che le variabili in $I_t$ non dovrebbero generare rendimenti anomali prevedibili.

**Domanda**: in presenza di prevedibilità, si tratta di inefficienza o di variazione temporale razionale dei rendimenti attesi?

### Origini della prevedibilità

Le variazioni nei prezzi dei titoli possono riflettere:
- notizie sui flussi di cassa futuri;
- variazioni nei tassi di sconto o nei premi per il rischio;
- cambiamenti nel sentiment degli investitori o bias comportamentali.

La prevedibilità quindi non implica automaticamente inefficienza del mercato. Il punto fondamentale è distinguere tra variazioni razionali nei rendimenti attesi e deviazioni dall'efficienza.

### Verifica della prevedibilità

I test empirici di prevedibilità si dividono in:
- **Prevedibilità su serie storiche**: i rendimenti variano in modo prevedibile nel tempo sulla base delle informazioni disponibili in $t$?
- **Prevedibilità sezionale**: alcuni titoli riportano sistematicamente rendimenti più elevati di altri in base a caratteristiche osservabili?

I test su serie storiche studiano la variazione dei rendimenti attesi nel tempo; i test sezionali (*cross-sectional*) studiano la variazione dei rendimenti medi tra asset. Entrambi sono rilevanti per l'EMH, poiché rendimenti anomali prevedibili possono emergere sia nel tempo sia tra i titoli.

### Prevedibilità su serie storiche a breve e lungo termine

La prevedibilità delle serie storiche viene studiata utilizzando una gamma di metodi:
- regressioni predittive (ad esempio, $r_{it+1} = \alpha + \beta z_t + e_{it+1}$);
- test statistici di casualità (ad esempio, *run test*, regole di filtro).

**Orizzonti brevi (settimane o mesi)**: i test verificano se i rendimenti siano prevedibili tramite informazioni ad alta frequenza; sia test basati su regressioni che test statistici di dipendenza seriale.

**Orizzonti lunghi (anni)**: i test verificano se variabili che si muovono gradualmente prevedano i rendimenti su periodi più lunghi; tipicamente implementati utilizzando regressioni predittive.

Questi approcci valutano se i rendimenti attesi variano sistematicamente nel tempo $\to$ l'interpretazione varia a seconda che la prevedibilità rifletta inefficienza o premi per il rischio variabili.

*(slide 23–26)*

## Il rapporto dividendo/prezzo e la prevedibilità di lungo periodo

> [!example] Esempio
> Le evidenze da regressione suggeriscono che gli indici di valutazione (come il BtM, book-to-market) aiutano a prevedere i rendimenti.
>
> **Esempio**: il rapporto dividendo-prezzo (D/P) predice la crescita futura del prezzo delle azioni (Campbell e Shiller, 2001).
>
> Più in generale, esiste un'ampia letteratura sulla prevedibilità basata su relazioni di valore attuale, tra cui il modello dinamico di Gordon linearizzato in logaritmi.
>
> **Figura (p. 27)** — "PRICE GROWTH till the next time D/P crosses its mean", scatterplot del D/P (asse x) contro la crescita successiva del prezzo (asse y) con retta di regressione crescente. Mostra la relazione positiva stimata tra il rapporto dividendo/prezzo e la successiva crescita dei prezzi azionari: un D/P più alto (titoli relativamente sottovalutati) è associato a una crescita di prezzo futura maggiore, coerente con la prevedibilità di lungo periodo basata su indici di valutazione.

*(slide 27)*

## Test di dipendenza lineare e non lineare sui rendimenti (forma debole)

### Test sulla correlazione seriale

Test per la dipendenza lineare tra rendimenti attuali e passati:

$$r_{it} = a + b r_{it-1} + \varepsilon_t$$

**Interpretazione**: $a$ è l'intercetta, contribuisce alla media incondizionata; $b$ misura la prevedibilità sulla base dei rendimenti passati.

**Evidenze**: per i principali indici, la correlazione seriale è debole; esistono evidenze di momentum per alcuni titoli; in generale, le evidenze suggeriscono che la performance di un singolo titolo non è prevedibile — a sostegno dell'efficienza in forma debole.

**Limiti di questi test**: trading nonsincrono; effetti di liquidità e microstruttura.

### Run tests

Test basati sul segno dei rendimenti piuttosto che sulla loro entità. Si definisca "+" se il rendimento $> 0$, "-" se $< 0$, "0" altrimenti. Si studiano le sequenze di segni identici (*run*):

$$[+][----][+++][0]$$

Il *run test* confronta le sequenze identiche osservate con quelle attese nell'ipotesi di indipendenza. Coglie dipendenze non lineari non rilevabili con test di correlazione.

I test empirici mostrano una debole relazione positiva, che scompare aumentando l'intervallo di osservazione (da un giorno a 15 giorni) — a sostegno dell'efficienza debole.

### Regole del filtro

Test su dipendenza non lineare basati su strategie di trading implementabili.

**Esempio**: regola del filtro X% (*market timing*) — acquistare quando il prezzo sale di X%, vendere quando il prezzo scende di X%. Progettate per sfruttare potenziali trend o inversioni.

Fama e Blume (1966) mostrano che le regole filtro (0,5%–4%) raramente battono le strategie passive: al netto dei costi di transazione, nessuna strategia basata su simili regole di trading è profittevole — a sostegno dell'efficienza in forma debole.

*(slide 28–30)*

## Effetti di calendario

Test su variazioni prevedibili dei rendimenti legate al calendario. Esempi:
- **Effetto gennaio**: rendimenti insolitamente alti a gennaio (specialmente per i titoli *small caps*).
- **Effetti giorno della settimana**: rendimenti più bassi il lunedì, più alti verso la fine della settimana.
- **Effetti infragiornalieri**: rendimenti concentrati in orari specifici (ad esempio alla fine della giornata di contrattazione).

**Implicazioni per l'EMH**: questi pattern sistematici mettono in discussione l'EMH, anche nella sua forma debole. La rilevanza economica dipende dai costi di transazione e dagli aggiustamenti per il rischio.

*(slide 31)*

## Prevedibilità sezionale: momentum e reversal

> [!example] Esempio
> ### Prevedibilità sezionale
>
> Gli studi sulla prevedibilità sezionale (*cross-sectional*) verificano se le differenze nei rendimenti medi tra titoli siano sistematicamente correlate a caratteristiche osservabili $\to$ **anomalie**.
>
> Esempi classici comprendono gli effetti dimensione, valore, momentum, redditività e investimento.
>
> **Metodo**:
> - ordinare i titoli in portafogli basandosi sulle caratteristiche in $I_t$;
> - confrontare i rendimenti medi tra i portafogli;
> - verificare se i modelli fattoriali possono spiegare i differenziali risultanti.
>
> La prevedibilità sezionale è particolarmente importante perché collega la EMH al più ampio tema della determinazione del prezzo dei titoli, ovvero se i premi di rendimento riflettano rischio o mispricing.
>
> ### Anomalie basate sulla performance passata: momentum e reversal
>
> Due fenomeni principali:
> - **Momentum**: continuità della performance relativa su orizzonti intermedi.
> - **Reversal**: tendenza alla inversione della performance relativa passata su orizzonti più lunghi.
>
> La domanda chiave è se tali regolarità riflettano remunerazione del rischio oppure deviazioni dall'efficienza in forma debole.
>
> **Momentum** (Jegadeesh e Titman, 1993, 2001): differenza mensile tra portafogli vincenti e perdenti, basata sulla performance recente. Evidenza di persistenza a breve termine nella performance relativa; i periodi successivi mostrano evidenza di inversione.
>
> **Figura 1 (p. 34)** — "Cumulative momentum profits": rendimenti cumulati di un portafoglio momentum (long-short vincenti/perdenti) su titoli NYSE, AMEX e Nasdaq, per diversi sottoperiodi campionari (1965-1987, 1965-1981, 1982-1987). Mostra una crescita cumulata dei profitti nei mesi immediatamente successivi alla formazione del portafoglio, seguita da un appiattimento/inversione nei mesi più lontani, coerente con momentum a breve e reversal successivo.
>
> **Reversal** (De Bondt e Thaler, 1985): inversione a lungo termine; rendimenti (corretti per il rischio) dei titoli vincenti-perdenti nei cinque anni precedenti.
>
> **Figura 1 (p. 35)** — "Cumulative Average Residuals for Winner and Loser Portfolios of 35 Stocks (1–36 months into the test period)": il portafoglio *Loser* mostra residui medi cumulati (CAR) crescenti fino a circa +0,30, mentre il portafoglio *Winner* mostra CAR negativi fino a circa −0,10. Mostra che, su orizzonti lunghi (fino a 36 mesi), i titoli precedentemente perdenti sovraperformano quelli precedentemente vincenti: un'inversione (reversal) della performance relativa passata.

*(slide 32–35)*

## Anomalie basate sui fondamentali: effetto dimensione ed effetto valore

> [!example] Esempio
> Momentum e inversione indicano che i rendimenti possono essere previsti nella sezione trasversale utilizzando i rendimenti passati $\to$ efficienza in forma debole?
>
> Estendendo l'analisi alle caratteristiche fondamentali: le caratteristiche delle imprese spiegano le differenze nei rendimenti tra titoli; prevedibilità basata su variabili contabili e di mercato.
>
> **Due principali evidenze empiriche**:
> - **Effetto dimensione** $\Rightarrow$ le imprese più piccole tendono a ottenere rendimenti medi più elevati (Banz, 1981).
> - **Effetto valore** $\Rightarrow$ le imprese con alto rapporto book-to-market (o basso P/E) tendono a ottenere rendimenti più elevati (Basu, 1977; Fama e French, 1993).
>
> Le differenze nei rendimenti sono associate ai fondamentali osservabili delle imprese $\to$ efficienza in forma semi-forte?
>
> ### Effetto dimensione
>
> Titoli ordinati per dimensione delle società (1 = piccolo; 10 = grande). Le aziende piccole ottengono rendimenti medi superiori rispetto a quelle grandi.
>
> **Possibili meccanismi**:
> - frizioni informative (minore copertura degli analisti, maggiore incertezza sui fondamentali);
> - frizioni di liquidità (minore volume di scambi, costi di transazione più elevati).
>
> **Figura 11.3 (p. 37)** — "Average annual return for 10 size-based portfolios, 1926–2015": rendimento medio annuo (%) per decile di dimensione (1 = più piccolo, 10 = più grande). Valori decrescenti da 18,7% (decile 1) a 11,1% (decile 10), con valori intermedi 16,8 / 15,1 / 15,4 / 14,9 / 15,0 / 16,7 / 13,6 / 12,8. Mostra la relazione inversa tra dimensione dell'impresa e rendimento medio: le imprese più piccole hanno ottenuto rendimenti storicamente più alti.
>
> ### Effetto valore
>
> Rendimenti ordinati per rapporto book-to-market (1 = basso; 10 = alto). Le aziende con book-to-market elevato ottengono rendimenti medi più alti.
>
> **Meccanismi possibili**:
> - rischio di dissesto finanziario (le aziende con book-to-market elevato tendono a essere in crisi);
> - spiegazioni comportamentali (per esempio, estrapolazione eccessiva dei rendimenti passati).
>
> **Figura 11.4 (p. 38)** — "Average return as a function of book-to-market ratio, 1926–2015": rendimento medio annuo (%) per decile di book-to-market (1 = più basso, 10 = più alto). Valori crescenti da 11,1% (decile 1) a 17,2% (decile 10), con valori intermedi 12,0 / 11,7 / 12,1 / 12,9 / 13,1 / 13,2 / 15,3 / 16,1. Mostra la relazione diretta tra book-to-market e rendimento medio: le imprese "value" (alto book-to-market) hanno ottenuto rendimenti storicamente più alti delle imprese "growth".

*(slide 36–38)*

## Dai modelli a fattore singolo ai modelli multifattoriali; interpretazione delle anomalie

### Dalle anomalie ai modelli fattoriali

I modelli a singolo fattore come il CAPM non possono spiegare queste anomalie $\Rightarrow$ modelli multifattoriali.

**Fama & French (1993)**:
- fattore di mercato;
- fattore dimensione (SMB: *small minus big*);
- fattore valore (HML: *high minus low* book-to-market).

**Carhart (1997)**: introduce un fattore momentum (UMD: *winners minus losers*), che rappresenta la persistenza dei rendimenti documentata in precedenza.

Le differenze sezionali nei rendimenti possono essere riassunte da un piccolo insieme di fattori di rischio.

### Interpretare le anomalie

**Regolarità empiriche**: effetti di dimensione, valore, momentum, inversione, ecc. (il cosiddetto "zoo dei fattori").

**Interpretazioni concorrenti**:
- **Visione basata sul rischio**: le caratteristiche sono proxy per il rischio sottostante.
- **Visione di mispricing / comportamentale**: deviazioni sistematiche dal valore fondamentale, generate da bias degli investitori e limiti all'arbitraggio.

**Problema dell'ipotesi congiunta** (Fama, 1970): i test di EMH testano anche il modello di pricing dei titoli; un rifiuto può riflettere un errore di specificazione del modello piuttosto che un'inefficienza.

### Persistenza delle anomalie

Molte anomalie sono documentate su campioni lunghi: size, value, momentum e altri premi di fattore; differenze sistematiche nei rendimenti tra portafogli. La loro persistenza nel tempo è meno chiara.

Possibili considerazioni: data mining e sovrastima della significatività statistica, pubblicazione dei risultati, costi di transazione. (Si veda il codice Python associato al corso.)

**Figura (p. 41)** — "Cumulative Factor Returns": rendimenti cumulati (Growth of $1) di diversi fattori (Mkt-RF, SMB, HML, RMW, CMA) dal 1970 circa fino a oggi. Mostra che il fattore di mercato (Mkt-RF) cresce nettamente più degli altri fattori nel lungo periodo, mentre i premi di fattore dimensione/valore/qualità/investimento (SMB, HML, RMW, CMA) mostrano andamenti più piatti o meno persistenti negli anni recenti.

*(slide 39–41)*

## Test di efficienza in forma forte e conclusioni sulla prevedibilità

### Test di efficienza in forma forte

È possibile per agenti con informazioni privilegiate o superiori ottenere rendimenti extra?

**Insider trading**: dirigenti, amministratori, grandi azionisti sono obbligati a divulgare le loro transazioni alle autorità di mercato (ad esempio, Jaffe, 1974; Seyhun, 1986, 1988, 1992; Givoly e Palmon, 1985). Le operazioni degli insider sono seguite da movimenti di prezzo; emerge una capacità di ottenere extrarendimenti.

**Analisti**: usano sia informazioni pubbliche che non; alcune evidenze di extra rendimenti (Dimson e Marsh, 1984), ma la capacità predittiva rimane limitata.

Le evidenze sono contrastanti, ma coerenti con limiti all'efficienza in forma forte.

### Conclusioni sull'EMH e la prevedibilità

La distinzione rilevante non è tra efficienza e prevedibilità, ma tra **efficienza** e **rendimenti extra prevedibili**.

Secondo l'EMH:
- i rendimenti inattesi non sono prevedibili sulla base di $I_t$;
- i rendimenti attesi possono variare nel tempo a causa di premi per il rischio variabili;
- le differenze sezionali di rendimento possono riflettere premi per il rischio diversi.

I modelli mostrati sopra non contraddicono l'EMH se riflettono: remunerazione per il rischio di equilibrio variabile nel tempo; limiti all'arbitraggio.

**Conclusione**: l'EMH esclude i guadagni facili, non la variazione prevedibile dei rendimenti attesi nel tempo o tra titoli.

*(slide 42–43)*

## 2) Studi di eventi: definizione e metodo

> [!abstract] Definizione
> Test dell'EMH basati sulla reazione dei prezzi a nuove informazioni $\to$ **studi di eventi**.
>
> Si identificano eventi (annunci di utili, fusioni, shock macroeconomici) e si definiscono i **rendimenti anomali** come la differenza tra i rendimenti realizzati e quelli che si sarebbero osservati in assenza dell'evento (controfattuale non osservabile che deve essere stimato).
>
> Secondo l'EMH, i rendimenti anomali dovrebbero essere circoscritti al momento degli annunci.
>
> ### Metodo
>
> Si definisce il tempo relativo all'evento $\tau = 0$ e la finestra dell'evento $\tau \in [\tau_1, \tau_2]$. (Opzionale) finestra di stima $\tau \in [\tau_a, \tau_b]$, con $\tau_b < \tau_1$.
>
> Si calcolano i rendimenti:
> - rendimenti azionari: $r_{i\tau}$;
> - rendimenti attesi (controfattuali): $E(r_{i\tau}\mid I_{\text{no-event}})$ da un modello benchmark.
>
> **Rendimenti anomali**:
>
> $$AR_{i\tau} = r_{i\tau} - E(r_{i\tau}\mid I_{\text{no-event}})$$
>
> Benchmark tipici: rendimento medio costante, rendimento di mercato, modello di mercato, modelli multifattoriali (es. Fama–French, Carhart).
>
> **Media su $N$ eventi**:
>
> $$AAR_\tau = \frac{1}{N}\sum_{i=1}^{N} AR_{i\tau}$$
>
> ### Interpretazione
>
> I **rendimenti anomali medi cumulati** nella finestra dell'evento sono:
>
> $$CAAR(\tau_1, \tau_2) = \sum_{\tau=\tau_1}^{\tau_2} AAR_\tau$$
>
> **Benchmark secondo EMH**: i prezzi si aggiustano in $\tau = 0$; nessuna persistenza nei rendimenti anomali oltre l'evento.

*(slide 45–47)*

## Interpretazione degli studi di eventi: reazione efficiente, sotto-reazione, sovra-reazione

Oltre alla reazione istantanea attesa sotto EMH, sono possibili altri scenari:
- **Variazione pre-evento** $\Rightarrow$ fuga di informazioni.
- **Variazione graduale** $\Rightarrow$ sotto-reazione.
- **Inversione** $\Rightarrow$ sovra-reazione.

Questi test richiedono una tempistica dell'evento ben definita: l'informazione deve diventare di pubblico dominio in un unico momento.

**Figura (p. 48)** — Grafico schematico del rendimento anomalo cumulato attorno a $\tau=0$ per tre scenari: *Over-reaction* (curva che sale oltre il livello finale e poi scende, in rosso), *Efficient Reaction* (salita immediata a un plateau stabile, in blu), *Under-reaction* (salita graduale nel tempo, in arancione). Mostra visivamente come distinguere una reazione di mercato efficiente da una sovra- o sotto-reazione osservando la forma del rendimento anomalo cumulato dopo l'evento.

*(slide 48)*

## Applicazioni degli studi di eventi

> [!example] Esempio
> ### Annunci di utili
>
> Drift pre-annunci di utili, forse dovuto ad insider trading. I rendimenti anomali persistono dopo l'annuncio; i rendimenti anomali cumulati crescono per più mesi. Va contro l'efficienza in forma semi-forte.
>
> **Figura 11.5 (p. 49)** — "Cumulative abnormal returns in response to earnings announcements" (Rendelman, Jones e Latané, 1982): rendimenti anomali cumulati (%) per decili di *earnings surprise* (dal decile 1 al decile 10), nei giorni da −20 a +90 rispetto all'annuncio. Il decile 10 (sorprese più positive) sale fino a circa +6%, il decile 1 (sorprese più negative) scende fino a circa −9%, con drift continuo anche nei mesi successivi all'annuncio. Mostra un drift post-annuncio persistente e graduale — coerente con una sotto-reazione del mercato, in contrasto con l'efficienza semi-forte.
>
> ### Frazionamenti (stock split)
>
> I frazionamenti sono interpretati come segnali positivi.
>
> **Drift pre-annuncio**: dovuto ad autoselezione di imprese con alta redditività e possibile insider trading.
>
> **Assenza di drift post-annuncio**: i prezzi si aggiustano all'annuncio — a sostegno dell'efficienza in forma semi-forte (Fama, Fisher, Jensen, Roll, 1969).
>
> **Figura 2a/2b (p. 50)** — "Average residuals — all splits" e "Cumulative average residual — all splits": il residuo medio cumulato cresce gradualmente da circa 29 mesi prima dello split fino a raggiungere circa 0,24-0,26 al momento dello split (mese 0), per poi restare stabile nei mesi successivi. Mostra un drift positivo pre-annuncio seguito da un plateau post-annuncio, coerente con l'assenza di sfruttabilità sistematica dopo la data dello split.
>
> ### Acquisizioni
>
> Annunci di acquisizioni: i prezzi aumentano bruscamente vicino alla data dell'evento e poi si stabilizzano. Rapida incorporazione delle informazioni $\to$ evidenza a favore dell'efficienza in forma semi-forte.
>
> **Figura 11.1 (p. 51)** — "Cumulative abnormal returns before takeover attempts: target companies" (Keown e Pinkerton, 1981): il rendimento anomalo cumulato (%) per le società target resta vicino a zero da −135 a circa −20 giorni, poi sale bruscamente da circa −15 giorni fino a +15 giorni (raggiungendo circa +30%), per poi stabilizzarsi. Mostra un pattern di drift pre-annuncio (possibile fuga di informazioni) seguito da un rapido aggiustamento intorno alla data di annuncio.
>
> ### Notizie sui media
>
> Caso studio: CNBC "Midday Call". Reazione immediata dopo la menzione all'interno del programma televisivo, distinta tra notizie positive vs. negative. Complessivamente a sostegno dell'efficienza in forma semi-forte.
>
> **Figura 11.2 (p. 52)** — "Stock Price Reaction to CNBC Reports" (Busse e Green, 2002): rendimento cumulato (%) nei minuti da −15 a +15 rispetto alla menzione, separato per report "Midday-Positive" (che sale fino a circa +0,6%) e "Midday-Negative" (che scende fino a circa −1,3%), con la maggior parte della reazione concentrata nei primi minuti dopo la menzione. Mostra una reazione di prezzo molto rapida (nell'ordine dei minuti) alla diffusione della notizia in TV, coerente con una rapida incorporazione dell'informazione nei prezzi.

*(slide 49–52)*

## 3) Studi su extrarendimenti: l'alfa e la sua misurazione

> [!abstract] Definizione
> Test della EMH basati sulla performance degli investitori professionali. Oggetto di interesse: l'extra rendimento (**alpha**):
>
> $$\alpha = r_{t+1} - E(r_{t+1}\mid I_t)$$
>
> **Metodo**: confrontare i rendimenti di portafoglio con un benchmark o modello di pricing dei titoli; stimare alpha come intercetta nelle regressioni sui fattori.
>
> **Benchmark EMH**: nessun alpha positivo persistente dopo la correzione per rischio e costi.
>
> **Aspetti cruciali**: abilità vs. fortuna; dipendenza dal modello dei rendimenti attesi; problema dell'ipotesi congiunta.
>
> ### Alfa di Jensen
>
> Jensen (1968) valuta la performance del fondo usando il CAPM:
>
> $$r_{fund,t} - r_{f,t} = \alpha_{fund} + \beta_{fund}\big(r_{m,t+1} - r_{f,t}\big) + e_{fund,t}$$
>
> Si stima $\alpha_{fund}$ — la performance corretta per il rischio — al lordo e al netto delle commissioni.
>
> **Figura (p. 55)** — Due istogrammi "Frequency distribution" delle intercette stimate $\hat\alpha_i$ (in %) per un campione di fondi comuni, per il periodo disponibile per ciascun fondo. Il primo istogramma (rendimenti lordi) mostra una distribuzione centrata vicino allo zero leggermente a sinistra; il secondo (rendimenti al netto delle commissioni) è spostato ulteriormente verso valori negativi. Mostra che, al netto delle commissioni di gestione, la distribuzione degli alfa stimati si sposta verso sinistra, indicando una performance mediamente peggiore per gli investitori dopo i costi.
>
> ### Dal CAPM ai modelli multifattoriali
>
> L'alfa di Jensen utilizza il CAPM come benchmark. Approccio moderno $\to$ modelli multifattoriali: fattori di Fama-French (mercato, dimensione SMB, value HML); Carhart (1997) aggiunge il momentum (UMD).
>
> L'alfa misura la performance dopo aver tenuto conto di molteplici fonti di rischio sistematico.

*(slide 54–56)*

## Evidenze empiriche sulla performance dei fondi

> [!example] Esempio
> Il modello a tre fattori calcola l'alfa di ciascun fondo come intercetta della seguente regressione:
>
> $$r - r_f = \alpha + \beta_1(r_m - r_f) + \beta_2 r_s + \beta_3 r_p + \varepsilon$$
>
> dove $r$ è il rendimento del fondo, $r_f$ è il tasso privo di rischio, $r_{s0}$ è il rendimento sul S&P 500 index, $r_s$ è il rendimento su un portafoglio non-S&P di titoli small-stock, $r_p$ è il rendimento su un bond portfolio, ed $\varepsilon$ è la misura di sensibilità del rendimento residuo del fondo alle diverse variabili.
>
> **Tabella — Alfa stimato per categoria di fondo (Elton, Gruber, Das e Hlavka, "Efficiency with Costly Information", *Review of Financial Studies*, 6, 1993, pp. 1–22)**
>
> | Type of Fund (Wiesenberger Classification) | Number of Funds | Alpha (%) | t-Statistic for Alpha |
> |---|---|---|---|
> | Maximum capital gain | 12 | −4,59 | −1,87 |
> | Growth | 33 | −1,55 | −1,23 |
> | Growth and income | 40 | −0,68 | −1,65 |
> | Balanced funds | 31 | −1,27 | −2,73 |
>
> **Figura 11.7 (p. 57)** — "Mutual fund alphas computed using a four-factor model of expected return, 1993–2007": istogramma di frequenza degli alfa a quattro fattori (%/mese) per un campione di fondi comuni (esclusi il 2,5% migliore e peggiore delle osservazioni). Mostra una distribuzione approssimativamente centrata poco sotto lo zero, con la maggior parte dei fondi che presenta alfa vicini a zero o leggermente negativi, coerente con l'assenza di extra-performance sistematica al netto del rischio.

*(slide 57)*

## Bias di sopravvivenza e persistenza della performance dei fondi

### Bias di sopravvivenza

I dati sui rendimenti dei fondi possono essere distorti dalla selezione del campione.

**Bias di sopravvivenza**: i dataset includono tipicamente solo i fondi che rimangono attivi; i fondi con performance scarsa tendono a scomparire più facilmente; la performance media risulta sovrastimata.

**Pratiche correlate**: fondi con performance scarsa fusi in fondi migliori; fondi incubatori portati selettivamente sul mercato.

### Persistenza della performance dei fondi (breve termine)

Esiste persistenza a breve termine? I fondi vengono classificati in base alla performance passata. Il decile superiore mostra performance elevata nel periodo di classificazione, ma persistenza limitata nel periodo successivo.

**Figura 11.8 (p. 59)** — "Risk-adjusted performance in ranking quarter and following quarter": rendimento trimestrale (%) per decile di performance (1–10), confrontando il "Ranking Quarter" (curva blu, fortemente decrescente da circa +4% a circa −5% dal decile 1 al 10) con il "Post-Ranking Quarter" (curva grigia, quasi piatta, leggermente decrescente attorno a 0-1%). Mostra che la forte differenziazione di performance osservata nel trimestre di classificazione (ranking) si dissolve quasi completamente nel trimestre successivo, indicando persistenza limitata a breve termine.

### Persistenza della performance dei fondi (medio termine)

Esiste persistenza a medio termine? Si confronta il ranking dei fondi in periodi diversi (Carhart, 1997): la persistenza risulta debole.

**Figura 1 (p. 60)** — "Contingency table of initial and subsequent one-year performance rankings": grafico a barre 3D che incrocia il decile iniziale ("Subsequent Ranking") con il decile finale ("Initial Ranking"), mostrando la probabilità condizionata di un fondo di trovarsi in un dato decile di rendimento lordo l'anno successivo, dato il ranking iniziale. Mostra che la massa di probabilità è solo debolmente concentrata sulla diagonale (permanenza nello stesso decile), a indicare una persistenza di performance debole da un anno all'altro.

*(slide 58–60)*

## Gestione attiva vs. passiva e implicazioni per la scelta di portafoglio

**Evidenze sulla gestione attiva**: capacità limitata di sovraperformare costantemente i benchmark; performance spesso penalizzate da commissioni e costi di transazione.

**Strategie attive vs. passive**:
- Gestione attiva: selezione dei titoli e market timing, costi più elevati.
- Gestione passiva: esposizione diversificata tramite fondi indicizzati ed ETF, basso costo.

**Implicazioni secondo l'EMH**: i fondi passivi sono la scelta razionale; l'attenzione si sposta dall'alfa al controllo dei costi.

**Ruolo ancora importante per la gestione del portafoglio**:
- allocazione del rischio e diversificazione;
- orizzonte temporale e considerazioni fiscali;
- preferenze eterogenee degli investitori.

*(slide 61)*
