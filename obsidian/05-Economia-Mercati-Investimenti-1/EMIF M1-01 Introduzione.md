---
title: "Economia dei mercati ed investimenti finanziari (EM5002) — Introduzione"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-01_Introduzione.pdf"
pages: 92
text_layer: true
verified: true
generated: 2026-07-10
---

## Presentazione del corso

**Corso:** Economia dei mercati ed investimenti finanziari (EM5002) — lezione introduttiva.

**Docente:** Stefano Colonnello — Università Ca' Foscari Venezia.

La lezione è organizzata in cinque parti, che costituiscono anche la struttura del resto del materiale:

1. Organizzazione del corso
2. Una panoramica dei mercati finanziari
3. Margin trading
4. Un modello base a un periodo
5. Ulteriori osservazioni

*(slide 1–2)*

## Contatti e organizzazione delle lezioni

- **Docente:** Stefano Colonnello, Dipartimento di Economia
- **Ricevimento:** mercoledì, 9:00–11:00, in presenza o da remoto (si prega di inviare email il giorno precedente con gli argomenti da discutere)
- **Lezioni:** mercoledì, giovedì, venerdì
- All'interno delle lezioni si svolgeranno anche esercizi utili ai fini della comprensione e dell'esame
- È previsto un servizio di tutorato per eventuali dubbi nello svolgimento dei lavori di gruppo

*(slide 3–4)*

## Materiale didattico

- Lucidi delle lezioni pubblicati sulla pagina Moodle del corso (parte del materiale è basato sul corso "Asset Pricing I" di Markus Brunnermeier, disponibile online)
- **Libro di testo:** Zvi Bodie, Alex Kane, Alan J. Markus (2023), *Investments*, McGraw-Hill Education
  - I capitoli rilevanti sono elencati nel syllabus su Moodle
  - Possono essere utilizzate anche edizioni precedenti
- **Altri riferimenti bibliografici utili:**
  - John H. Cochrane (2005), *Asset Pricing*, Princeton University Press
  - Roy E. Bailey (2005), *The Economics of Financial Markets*, Cambridge University Press
  - Ulteriori fonti indicate nei lucidi delle singole lezioni

*(slide 5)*

## Modalità di valutazione

Sono previsti due possibili percorsi di valutazione (maggiori dettagli nel syllabus su Moodle):

**1) Due prove parziali e due lavori di gruppo (uno per modulo)**
- Prova intermedia (8 aprile) e prova finale (13 maggio)
- I lavori di gruppo sostituiscono le due domande aperte e possono essere svolti in gruppi di massimo tre studenti
- Ogni prova parziale vale fino a 10 punti
- Ogni lavoro di gruppo vale fino a 6 punti
- Voto finale calcolato come somma
- Iscrizione dei gruppi entro il 4 marzo tramite Moodle
- Scadenza 8 aprile; consegna tramite Moodle

Una nota a margine precisa il calcolo del voto per il primo modulo: il punteggio finale $T$ è determinato secondo la formula

$$T = \min\{16,\; P + G + B\},$$

dove $P$ è il punteggio della prova parziale, con $0 \le P \le 2$; $G$ è il punteggio relativo alle parti A–B–C del lavoro di gruppo, con $0 \le G \le 6$; e $B$ è il punteggio della parte bonus D del lavoro di gruppo, con $0 \le B \le 2$.

**2) Esame scritto finale al termine del secondo modulo (12 CFU)**
- Domande a risposta multipla
- Due domande aperte

*(slide 6–8)*

## Obiettivi del corso

Gli obiettivi principali del corso sono:

- Caratterizzare le scelte individuali di investimento attraverso la **teoria del portafoglio**
- Comprendere i meccanismi di formazione dei prezzi delle attività finanziarie attraverso modelli di **pricing di equilibrio**
- Reperire e utilizzare **dati finanziari** necessari a supportare le scelte di investimento mediante software statistici

*(slide 10)*

## Attività reali vs. attività finanziarie

> [!abstract] Definizione
> **Attività reali**
> - Hanno capacità produttiva
> - Esempi: terreni, edifici, macchinari, proprietà intellettuale
>
> **Attività finanziarie**
> - Sono diritti su attività reali
> - Non contribuiscono direttamente alla capacità produttiva
> - Esempi: azioni, obbligazioni

*(slide 11)*

## Il sistema finanziario: bilanci aggregati, intermediari e attori di mercato

**Figura — Table 1.1, Stato patrimoniale delle famiglie statunitensi** (Fonte: *Flow of Funds Accounts of the United States*, Board of Governors of the Federal Reserve System, marzo 2016). La tabella riporta, in miliardi di dollari e in percentuale sul totale, le attività reali delle famiglie USA (immobili, beni durevoli, altro), le attività finanziarie (depositi, riserve assicurative vita, riserve pensionistiche, capitale azionario, quote di imprese non costituite in società, quote di fondi comuni, titoli di debito, altro) e le passività (mutui, credito al consumo, prestiti bancari e altri, altro), da cui risulta il patrimonio netto (*net worth*). Conclusione: la ricchezza delle famiglie statunitensi è composta in larga parte da immobili residenziali tra le attività reali e da capitale azionario e riserve pensionistiche tra le attività finanziarie.

**Figura — Table 1.2, Ricchezza netta interna degli Stati Uniti** (stessa fonte). Scompone la ricchezza netta domestica (*domestic net worth*) in immobili commerciali, immobili residenziali, impianti e proprietà intellettuale, scorte (*inventories*) e beni durevoli dei consumatori. Conclusione: gli immobili (commerciali e residenziali) rappresentano la componente più rilevante della ricchezza reale interna del paese.

**Figura — Diagramma dei flussi di fondi (mercati finanziari vs. intermediari).** Mostra come i fondi (*funds*) fluiscano dai *lender-savers* (famiglie, imprese, governo, soggetti esteri) ai *borrower-spenders* (imprese, governo, famiglie, soggetti esteri) attraverso due canali: la **finanza diretta** (*direct finance*), tramite i mercati finanziari, e la **finanza indiretta** (*indirect finance*), tramite gli intermediari finanziari. Conclusione: il sistema finanziario incanala il risparmio verso l'investimento sia direttamente sia indirettamente.

**Gli attori nei mercati finanziari.** Nel piano (quantità di capitale, prezzo del capitale) si rappresenta una curva di offerta $S$ crescente e una curva di domanda $D$ decrescente, il cui incrocio determina l'equilibrio $E$ (prezzo e quantità di capitale scambiato).
- Chi offre capitale? → le **famiglie**
- Chi domanda capitale? → le **imprese**
- Il **governo** può svolgere sia il ruolo di prenditore sia quello di datore di fondi

*(slide 12–15)*

## Tipi di attività finanziarie

> [!abstract] Definizione
> - **Equity (capitale azionario):** rappresenta una quota di proprietà in una società (azioni, focus del corso)
> - **Titoli a reddito fisso:** promettono un flusso di reddito fisso o un flusso determinato da una formula specifica (debito)
> - **Derivati:** forniscono payoff determinati dai prezzi di altre attività
> - **Altro:** investimenti in valuta, cripto-attività, futures su commodity (ad esempio per copertura), ecc.

*(slide 16)*

## Mercato primario e secondario; il sottoprezzamento delle IPO

**Mercato primario**
- Nuove emissioni azionarie da parte di imprese private che si quotano in Borsa (offerte pubbliche iniziali, **IPO**)
- Nuove emissioni azionarie da parte di società già quotate (aumenti di capitale, **SEO**)
- L'emittente riceve il valore del titolo emesso

**Mercato secondario**
- Il possessore del titolo vende ad un altro acquirente
- L'emittente non riceve alcun trasferimento e non è coinvolto nella transazione

**Il fenomeno del sottoprezzamento delle IPO.** Le IPO tendono ad essere prezzate al di sotto del loro valore di mercato del primo giorno di negoziazione (*underpricing*), come mostra la seguente serie storica per il mercato statunitense:

| Year | No. IPOs | Mean First-day Return EW | Mean First-day Return VW | Median First-day Return | Aggregate Amount Left on the Table | Aggregate Proceeds |
|---|---|---|---|---|---|---|
| 2000 | 380 | 56.3% | 45.8% | 27.9% | $29.68 billion | $64.80 billion |
| 2001 | 80 | 14.0% | 8.4% | 10.2% | $2.97 billion | $35.29 billion |
| 2002 | 66 | 9.1% | 5.1% | 8.2% | $1.13 billion | $22.03 billion |
| 2003 | 63 | 11.7% | 10.4% | 8.7% | $1.00 billion | $9.54 billion |
| 2004 | 173 | 12.3% | 12.4% | 7.1% | $3.86 billion | $31.19 billion |
| 2005 | 159 | 10.3% | 9.3% | 5.8% | $2.64 billion | $28.23 billion |
| 2006 | 157 | 12.1% | 13.0% | 5.6% | $3.95 billion | $30.48 billion |
| 2007 | 159 | 14.0% | 13.9% | 6.8% | $4.95 billion | $35.66 billion |
| 2008 | 21 | 5.7% | 24.7% | -1.7% | $5.63 billion | $22.76 billion |
| 2009 | 41 | 9.8% | 11.1% | 5.7% | $1.46 billion | $13.17 billion |
| 2010 | 91 | 9.4% | 6.2% | 3.1% | $1.84 billion | $29.82 billion |
| 2011 | 81 | 13.9% | 13.0% | 8.5% | $3.51 billion | $26.97 billion |
| 2012 | 93 | 17.7% | 8.9% | 11.1% | $2.75 billion | $31.11 billion |
| 2013 | 158 | 20.9% | 19.0% | 13.0% | $7.89 billion | $41.56 billion |
| 2014 | 206 | 15.5% | 12.8% | 5.8% | $5.40 billion | $42.20 billion |
| 2015 | 118 | 19.2% | 18.9% | 10.3% | $4.16 billion | $22.00 billion |
| 2016 | 75 | 14.5% | 14.2% | 5.0% | $1.77 billion | $12.52 billion |
| 2017 | 106 | 12.9% | 16.0% | 9.0% | $3.68 billion | $22.98 billion |
| 2018 | 134 | 18.6% | 19.1% | 11.6% | $6.39 billion | $33.47 billion |
| 2019 | 113 | 23.5% | 17.6% | 17.9% | $6.95 billion | $39.28 billion |
| 2020 | 165 | 41.6% | 47.9% | 26.2% | $29.66 billion | $61.86 billion |
| 2021 | 311 | 32.1% | 24.0% | 17.0% | $28.65 billion | $119.36 billion |
| 2022 | 38 | 48.9% | 14.2% | 9.3% | $0.99 billion | $6.99 billion |
| 2023 | 54 | 11.9% | 16.1% | -0.5% | $1.92 billion | $11.92 billion |
| 2024 | 72 | 15.3% | 18.1% | 7.2% | $3.72 billion | $20.49 billion |
| 2025 | 90 | 29.3% | 33.6% | 13.7% | $13.11 billion | $38.97 billion |
| **1980-2025** | **9,343** | **19.0%** | **20.6%** | **7.0%** | **$250.1 billion** | **$1,190 billion** |

Fonte: sito web di Jay Ritter.

**Figura — Table 1 (Gahng, Ritter, Zhang, 2023), "Un'alternativa alle IPO tradizionali".** Confronta, su un campione di operazioni, i costi relativi (proventi ceduti/sconto rispetto al valore di mercato, in percentile) di tre modalità di quotazione: fusione con una SPAC, IPO tradizionale e direct listing. Conclusione: le operazioni tramite SPAC risultano generalmente più costose delle IPO tradizionali e dei direct listing.

**Figura — Tabella sulla performance di lungo periodo delle IPO 1980–2023** (Fonte: sito web di Jay Ritter). Confronta, nei primi cinque anni dalla quotazione (primi sei mesi, secondo semestre, anni 1–5, media geometrica anni 1–5), il rendimento delle imprese quotate tramite IPO con quello di imprese di controllo comparabili per dimensione (*size-matched*) e per dimensione e rapporto book-to-market (*size & BM matched*). Conclusione: nel lungo periodo le IPO tendono a sottoperformare i benchmark di controllo (differenza di rendimento negativa nella media geometrica).

*(slide 17–20)*

## Il mercato secondario: bid-ask spread e liquidità

> [!abstract] Definizione
> **Il mercato secondario** è il luogo in cui vengono scambiati titoli (azionari) già emessi. Per ciascun titolo sono quotati due prezzi:
> - **Bid** (denaro): prezzo che si riceve per una vendita immediata di un'unità
> - **Ask** (lettera): prezzo richiesto per l'acquisto immediato di un'unità
>
> Il prezzo ask deve superare il prezzo bid.La differenza tra ask e bid è il **bid-ask spread**:
>
> $$\text{Spread} = \text{Ask} - \text{Bid},$$
>
> ed è positiva poiché Ask > Bid. Ragioni per la sua esistenza: costi di transazione, costi di inventario, selezione avversa. In termini pratici lo spread è il costo di scambiare i titoli istantaneamente.
>
> **Liquidità.** Esistono due nozioni principali:
> - **Liquidità di mercato:** quanto sia facile/conveniente entrare o uscire da una posizione (su cui si concentra il corso)
> - **Liquidità creditizia:** facilità nell'ottenere fondi esterni per finanziare investimenti profittevoli
>
> La crisi finanziaria del 2007/2008 è stata caratterizzata da una mancanza di entrambe: difficoltà nell'uscire dalle posizioni a prezzi "buoni" (liquidità di mercato) e difficoltà nell'ottenere credito per rifinanziare investimenti in prodotti derivati strutturati, come i MBS (liquidità creditizia).
>
> Un mercato è **liquido** se i costi di negoziazione sono bassi e i volumi sono elevati: il ribilanciamento di un portafoglio non è né costoso né difficile (in termini di tempo). Kyle (1985) definisce un mercato liquido quando è:
> - **"Tight":** i costi di negoziazione per piccole quantità sono a loro volta bassi (bid-ask spread piccoli)
> - **"Deep":** i costi di negoziazione per grandi quantità sono bassi; ordini molto grandi non provocano grandi movimenti di prezzo
> - **"Resilient":** gli scostamenti tra i prezzi e i valori "veri" sono ridotti e vengono corretti molto rapidamente

*(slide 21–23)*

## Classificazione dei mercati finanziari, dei partecipanti e dei mercati OTC

**Tipi di mercati finanziari.** I mercati possono essere classificati lungo diverse dimensioni:
- *Dove* avvengono le transazioni: mercati fisici, mercati elettronici, over the counter (OTC)
- *Quando* avvengono le transazioni: aste (*call auctions* o *batch markets*), mercati continui (*continuous auctions* o *sequential markets*)
- Struttura del mercato: mercati **order-driven**, mercati **quote-driven**
- Tipi di intermediari: nessun intermediario (mercato a ricerca diretta), broker, market maker/dealer, mercati ad asta

**Tipi di partecipanti**
- Piccoli risparmiatori
- Investitori professionali (istituzionali): investitori di copertura (*hedger*), speculatori, arbitraggisti
- **Broker:** acquistano per conto e nell'interesse di un cliente; non forniscono direttamente liquidità, ma si limitano a "cercarla"; non hanno problemi di inventario
- **Dealer:** disposti a comprare e vendere per conto proprio, pubblicando prezzi bid e ask; forniscono liquidità e detengono un inventario. Corrono i rischi di:
  - incertezza sulla durata di una posizione e sui prezzi futuri di un titolo (**rischio di inventario**)
  - possibilità di scambiare con operatori informati (**selezione avversa**)
- Il bid-ask spread riflette i costi e i rischi dei dealer

**Mercati OTC.** Sono stati sviluppati per sottrarsi a regole e requisiti imposti dai mercati di Borsa. Sono gestiti da market maker (dealer) registrati, che traggono profitto dal bid-ask spread dei prezzi che quotano. Un investitore interessato contatta un broker registrato nel mercato OTC; il broker esamina i prezzi dei vari dealer, propone la migliore quotazione disponibile ed esegue l'ordine; l'investitore riceve il titolo e paga una commissione al broker.
- **Vantaggi:** contratti ritagliati su misura per le necessità delle parti coinvolte
- **Svantaggi:** frammentazione del mercato dovuta alla negoziazione su più tavoli diversi nello stesso momento

*(slide 24–26)*

## Tipi di ordini: market order e limit order

> [!abstract] Definizione
> - **Ordini di mercato (market order):** ordini di acquisto o vendita immediata al prezzo di mercato. Chi li invia rischia un'esecuzione a un prezzo lontano da quello desiderato: **tempo certo ma prezzo incerto**. I trader impazienti sono disposti a pagare un premio per l'esecuzione immediata e utilizzano ordini di mercato.
> - **Ordini limite (limit order):** ordini condizionati a un determinato livello di prezzo, eseguiti solo quando il prezzo di mercato è inferiore o superiore a una certa soglia. Ritardando l'esecuzione, il trader spera di ottenere prezzi migliori: **tempo incerto ma prezzo certo**. I trader pazienti tendono a scegliere ordini limite.
>   - **Ordini stop:** una tipologia comune di ordine limite che si attiva quando il prezzo di mercato raggiunge una soglia prestabilita, fornendo protezione contro perdite inattese (*stop loss*)

*(slide 27)*

## Strutture di mercato order-driven e quote-driven: un esempio di limit order book

> [!example] Esempio
> **Due principali strutture di mercato**
> - **Mercati quote-driven:** i market maker (dealer) competono tra loro e forniscono liquidità quotando prezzi bid-ask e quantità alle quali sono disposti a scambiare. Gli investitori domandano liquidità inviando ordini di mercato; gli ordini vengono eseguiti tramite incrocio con l'inventario del dealer. Esempi: NASDAQ (tradizionalmente), mercati obbligazionari, mercato valutario (Forex)
> - **Mercati order-driven:** gli investitori possono, ma non sono obbligati a, inserire ordini limite, memorizzati nel *limit order book*. Una transazione avviene quando un ordine di mercato incontra una quotazione corrispondente sul lato opposto. Gli ordini limite forniscono liquidità, gli ordini di mercato la consumano; gli ordini vengono eseguiti tramite incrocio con ordini di altri investitori. Esempi: NYSE (per lo più), London Stock Exchange, piattaforme di trading di criptovalute
>
> **Esempio numerico — evoluzione di un limit order book**
>
> *Limit order book a $t=0$:*
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | 10.000 | 100 | 5.000 |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> *A $t=1$ gli ordini limite vengono incrociati; il bid-ask spread è pari a 1 unità di conto.*
>
> Prima:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | 10.000 | 100 | 5.000 |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> Dopo:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | 5.000 | 100 | |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> *A $t=2$ un operatore invia un ordine di mercato di acquisto per 5.000 azioni; l'ordine viene eseguito contro gli ordini limite al prezzo di 100 e lascia l'order book con uno spread pari a 2.*
>
> Prima:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | 5.000 | 100 | |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> Dopo:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | | 100 | |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> *A $t=3$ arrivano simultaneamente un ordine limite di vendita per 6.000 azioni al prezzo di 102 e un ordine limite di acquisto per 2.000 azioni a 100; il bid-ask spread torna a 1 unità.*
>
> Prima:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 7.000 | 102 | |
> | 15.000 | 101 | |
> | | 100 | |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> Dopo:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 13.000 | 102 | |
> | 15.000 | 101 | |
> | | 100 | 2.000 |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> *Infine, a $t=3$ arriva un nuovo ordine di mercato di acquisto per 29.000 azioni, eseguito contro gli ordini limite a 101, 102 e 103. Costo totale:*
>
> $$15.000 \times 101 + 13.000 \times 102 + 1.000 \times 103 = 2.944.000,$$
>
> *ovvero 101,52 per azione. Lo spread sale a 3 unità.*
>
> Prima:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 2.000 | 103 | |
> | 13.000 | 102 | |
> | 15.000 | 101 | |
> | | 100 | 2.000 |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> Dopo:
>
> | Vendita | Prezzo | Acquisto |
> |---|---|---|
> | 1.000 | 103 | |
> | | 102 | |
> | | 101 | |
> | | 100 | 2.000 |
> | | 99 | 12.000 |
> | | 98 | 4.000 |
> | | 97 | 4.000 |
>
> **Riepilogo**
> 1. Gli ordini limite vengono incrociati automaticamente
> 2. La liquidità è fornita dagli ordini limite
> 3. La liquidità è assorbita dagli ordini di mercato e dall'incrocio degli ordini limite
> 4. Gli ordini di mercato di grandi dimensioni che "walk the book" aumentano i costi di esecuzione
> 5. Per questo motivo gli ordini di mercato di grandi dimensioni sono tipicamente suddivisi in molti ordini di mercato di piccole dimensioni
> 6. L'algo-trading ottimizza l'esecuzione degli ordini e individua grandi "meta ordini", cioè insiemi di scambi eseguiti in modo incrementale che fanno parte di una singola decisione di trading

*(slide 28–34)*

## Il flash crash dell'S&P Mini (6 maggio 2010)

> [!example] Esempio
> La microstruttura del mercato è fondamentale: può provocare notevoli oscillazioni dei prezzi senza variazioni dei fondamentali.
>
> **Figura — Andamento infragiornaliero del Dow Jones Industrial Average il 6 maggio 2010 ("Momentary Lapse").** Il grafico mostra un crollo improvviso dell'indice nel primo pomeriggio, con un minimo di circa -9,2% rispetto alla chiusura precedente, seguito da un recupero parziale fino a una chiusura a -3,2%. Conclusione: shock di liquidità legati alla microstruttura del mercato possono generare movimenti di prezzo estremi e temporanei senza alcuna variazione nei fondamentali economici.
>
> A seguito di episodi come questo sono stati introdotti i **circuit breaker** per l'intero mercato e la **sospensione delle negoziazioni** per singoli titoli in presenza di forti movimenti di prezzo.

*(slide 35)*

## Margin trading: definizioni e procedura

> [!abstract] Definizione
> Una delle funzioni dei broker (o delle piattaforme di scambio) è fornire finanziamenti agli investitori per le loro operazioni di investimento, consentendo le operazioni di **margin trading** (negoziazione con margine o a leva). Ciò consente agli investitori di assumere posizioni di dimensione maggiore rispetto a quanto potrebbero permettersi utilizzando solo fondi propri (**posizione con leva**).
>
> Il **margin** è il collaterale (garanzia) — in contanti o in titoli — che deve essere depositato presso il broker per coprire (in parte) il rischio di credito (rischio di controparte) associato alla posizione.
>
> Un **margin account** (conto a margine) è richiesto nei seguenti casi:
> - Acquisti di titoli a leva
> - Prestito di titoli per vendite allo scoperto
> - Contratti derivati
>
> **Procedura del margin trading**
> 1. **Apertura del conto:** l'investitore apre un margin account presso un broker per poter utilizzare la leva finanziaria o effettuare vendite allo scoperto
> 2. **Margine iniziale:** deposito iniziale obbligatorio (collaterale) richiesto per aprire una posizione
> 3. **Mark-to-market:** aggiornamento giornaliero del saldo del conto in base al prezzo di chiusura del titolo (i guadagni vengono accreditati, le perdite addebitate)
> 4. **Margine di mantenimento:** soglia minima di capitale; se le perdite giornaliere portano il capitale al di sotto di tale livello, viene inviata una **margin call** (richiesta di margine) che comporta il versamento di fondi aggiuntivi o la liquidazione forzata

*(slide 37–38)*

## Il margine iniziale: un acquisto con leva e la soglia di margin call

> [!example] Esempio
> Il margine iniziale è calcolato come:
>
> $$\text{Margine} = \frac{\text{VM dei titoli} - \text{Prestito}}{\text{VM dei titoli}} = \frac{\text{Capitale proprio}}{\text{VM dei titoli}}$$
>
> Il collaterale del prestito è rappresentato dal valore del titolo. Negli Stati Uniti, il Board of Governors della Federal Reserve System stabilisce i limiti per questo tipo di prestiti (ad esempio, margine iniziale $\ge 50\%$).
>
> **Esempio.** Un investitore acquista 100 azioni General Motors a \$50 per azione. Capitale proprio: l'investitore dispone di \$3.000; prestito: i restanti \$2.000 sono presi a prestito dal broker. Il margine iniziale è
>
> $$\text{Margine} = \frac{\text{Capitale proprio}}{\text{VM dei titoli}} = \frac{5.000-2.000}{5.000} = 60\%$$
>
> La leva finanziaria è
>
> $$\text{Leva} = \frac{\text{VM dei titoli}}{\text{Capitale proprio}} = \frac{1}{\text{Margine}} = 1,67$$
>
> Stato patrimoniale iniziale dell'investitore a $P=\$50$ (Margine $=60\%$, Leva $=1,67$):
>
> | Attività | | Passività | |
> |---|---|---|---|
> | Azioni | 5.000 | Prestito | 2.000 |
> | | | Capitale proprio | 3.000 |
>
> Se il prezzo scende a $P=\$48$, lo stato patrimoniale diventa (Margine $=58\%$, Leva $=1,71$):
>
> | Attività | | Passività | |
> |---|---|---|---|
> | Azioni | 4.800 | Prestito | 2.000 |
> | | | Capitale proprio | 2.800 |
>
> **Margine di mantenimento.** Supponiamo che il margine di mantenimento sia pari al 40%. Se il valore di mercato dei titoli scende e il margine va sotto il 40%, il broker invia una margin call per ripristinare il livello richiesto. Se $P$ è il prezzo dell'azione, il capitale proprio è
>
> $$\text{Capitale proprio} = \text{VM dei titoli} - \text{Prestito} = 100P - 2.000$$
>
> il margine come funzione di $P$ è
>
> $$\text{Margine} = \frac{\text{Capitale proprio}}{\text{VM dei titoli}} = \frac{100P-2.000}{100P}$$
>
> Per trovare il prezzo che attiva la margin call, si risolve rispetto a $P$:
>
> $$\frac{100P-2.000}{100P} = 0,40 \quad \Rightarrow \quad P = \frac{2.000}{60} = 33,33$$

*(slide 39–43)*

## Effetti della leva finanziaria: confronto tra strategie

> [!example] Esempio
> **Pro:** gli investitori possono assumere posizioni di dimensione maggiore. **Contro:** il rischio di perdite è molto più elevato.
>
> **Esempio.** $P_{t-1}=\$50$, poi il prezzo sale a $P_t=\$60$.
>
> - **Strategia 1:** investimento proprio di \$3.000 in 60 azioni. Il rendimento è
>
> $$R = \frac{60\times 60 - 3.000}{3.000} = 20\%$$
>
> - **Strategia 2:** prestito di \$2.000 al 10% per acquistare 100 azioni. Il flusso di cassa finale è $100\times 60 - 2.000\times(1+10\%) = 3.800$, e il rendimento è
>
> $$R = \frac{3.800-3.000}{3.000} = 26,67\%$$
>
> Supponiamo invece che il prezzo scenda a $P_t=\$40$:
>
> - **Strategia 1:** il rendimento è
>
> $$R = \frac{60\times 40 - 3.000}{3.000} = -20\%$$
>
> - **Strategia 2:** flusso di cassa finale pari a \$1.800, che implica un rendimento negativo di
>
> $$R = \frac{1.800-3.000}{3.000} = -40\%$$
>
> La leva amplifica sia i guadagni sia le perdite: strategia 2 (con leva) genera un rendimento più elevato in caso di rialzo (26,67% contro 20%) ma una perdita più profonda in caso di ribasso (-40% contro -20%).

*(slide 44–45)*

## La vendita allo scoperto (short selling)

> [!abstract] Definizione
> Prendendo in prestito un titolo da un broker, è possibile venderlo **allo scoperto**, ossia venderlo senza possederlo. Anche in questo caso è necessario un conto a margine. Obiettivo: realizzare profitti da diminuzioni del prezzo di mercato del titolo.
>
> Il trader prende in prestito il titolo dal broker — che lo ottiene solitamente da altri investitori (ad es. fondi passivi) — con la promessa di restituirlo in seguito al prezzo di mercato. Il titolo viene venduto oggi al prezzo di mercato (l'investitore incassa immediatamente il denaro) con la speranza di riacquistarlo a un prezzo inferiore. Se il prezzo del titolo aumenta, l'investitore deve pagare al broker il prezzo di mercato più le commissioni (interessi sul prestito).
>
> Ci si concentra qui sulle vendite allo scoperto **covered** (coperte). Le vendite allo scoperto **naked** (scoperte), cioè senza prendere in prestito il titolo, sono generalmente vietate (alto rischio di mancata consegna).
>
> **Flussi di cassa: posizione lunga vs. corta**
>
> Acquisto di un'azione (posizione lunga):
>
> | Tempo | Azione | Flusso di cassa* |
> |---|---|---|
> | 0 | Acquisto dell'azione | − Prezzo iniziale |
> | 1 | Incasso dividendo, vendita azione | Prezzo finale + Dividendo |
>
> Profitto = (Prezzo finale + Dividendo) − Prezzo iniziale
>
> Vendita allo scoperto di un'azione:
>
> | Tempo | Azione | Flusso di cassa* |
> |---|---|---|
> | 0 | Prestito dell'azione; vendita | + Prezzo iniziale |
> | 1 | Rimborso del dividendo e riacquisto dell'azione per restituire l'azione originariamente presa a prestito | − (Prezzo finale + Dividendo) |
>
> Profitto = Prezzo iniziale − (Prezzo finale + Dividendo)
>
> *Un flusso di cassa negativo implica un'uscita di cassa.
>
> **Differenza fondamentale rispetto all'acquisto con leva:** gli investitori prendono in prestito dei titoli invece di un ammontare di denaro. In un acquisto con leva, il collaterale è il valore del titolo; qui invece i proventi della vendita iniziale sono il collaterale. Tale collaterale va poi integrato con un ulteriore deposito per assorbire le variazioni del valore del titolo da riacquistare in futuro.
>
> **Esempio.** Un investitore vende allo scoperto \$5.000 di NVIDIA (100 azioni a \$50 per azione). Passività dell'investitore: $\$50\times 100 = \$5.000$. Il broker richiede un margine, supponiamo 60%; l'investitore è tenuto a fornire anche una garanzia in contanti depositando \$3.000 sul conto presso il broker.

*(slide 46–48)*

## Un esempio di vendita allo scoperto e la soglia di margin call

> [!example] Esempio
> Vendendo allo scoperto 100 azioni NVIDIA a \$50 per azione (valore totale \$5.000) e disponendo di un capitale iniziale di \$3.000, il margine iniziale è:
>
> $$\text{Margine} = \frac{\text{Capitale proprio}}{\text{VM dei titoli venduti allo scoperto}} = \frac{3.000}{5.000} = 60\%,$$
>
> e la leva finanziaria è
>
> $$\text{Leva} = \frac{\text{VM dei titoli venduti allo scoperto}}{\text{Capitale proprio}} = \frac{5.000}{3.000} = 1,67$$
>
> Supponiamo che il giorno successivo il prezzo scenda a \$40: chiudendo la posizione (acquisto delle 100 azioni a \$40 e restituzione del prestito in azioni al broker) il profitto è \$1.000. Se invece il prezzo sale a \$60 (passività \$6.000), con la stessa strategia di chiusura la perdita è \$1.000.
>
> **Bilancio iniziale dell'investitore a $P=\$50$, Margine $=60\%$:**
>
> | Attività | | Passività | |
> |---|---|---|---|
> | Liquidità (da vendita azioni) | 5.000 | Azioni dovute | 5.000 |
> | Liquidità (collaterale) | 3.000 | Capitale proprio | 3.000 |
>
> **Se il prezzo scende a $P=\$40$:**
>
> | Attività | | Passività | |
> |---|---|---|---|
> | Liquidità (da vendita azioni) | 5.000 | Azioni dovute | 4.000 |
> | Liquidità (collaterale) | 3.000 | Capitale proprio | 4.000 |
>
> Bilancio finale dell'investitore a $P=\$40$: Profitto = \$1.000.
>
> **Soglia di margin call.** Quando il margine della posizione scende sotto una certa soglia, il broker invia una margin call. Supponiamo che il margine di mantenimento sia 40%: il collaterale della posizione corta deve essere sempre almeno pari al 40% del valore di mercato delle azioni dovute.
>
> $$\text{Attività} = 5.000+3.000, \qquad \text{Azioni dovute} = 100P$$
>
> $$\text{Capitale proprio} = 8.000-100P, \qquad \text{Margine} = \frac{8.000-100P}{100P}$$
>
> Prezzo soglia per la margin call:
>
> $$\frac{8.000-100P}{100P} = 0,40 \quad \Rightarrow \quad P = \frac{8.000}{140} = \$57,14$$

*(slide 49–51)*

## Il modello base a un periodo: spazio degli stati e preferenze

> [!abstract] Definizione
> Si considera un modello base a un periodo per introdurre alcuni concetti chiave: struttura dei titoli, titoli ridondanti, completezza del mercato.
>
> **Spazio degli stati (evoluzione degli stati).** Due date, $t=0,1$; $S$ stati del mondo al tempo $t=1$ (in $t=0$ l'economia si trova in un unico nodo iniziale, da cui si dipartono gli stati $s=1,2,\ldots,S$ al tempo 1).
>
> **Preferenze.** $U(c_0,c_1,\ldots,c_S)$, e il saggio marginale di sostituzione tra lo stato $s$ e il tempo 0 (pendenza della curva di indifferenza) è
>
> $$MRS^A_{s,0} = -\frac{\partial U^A/\partial c_s^A}{\partial U^A/\partial c_0^A}$$
>
> **Struttura dei titoli.** Si distinguono un'economia alla Arrow-Debreu (AD) e una struttura generale dei titoli, trattate nella sezione seguente.

*(slide 53–54)*

## Titoli Arrow-Debreu, completezza dei mercati e titoli ridondanti

> [!abstract] Definizione
> **Struttura generale dei titoli.** Il titolo $j$ è rappresentato dal vettore dei payoff
>
> $$x^j = (x_1^j, x_2^j, \ldots, x_S^j)'$$
>
> La struttura dei titoli è rappresentata dalla matrice dei payoff
>
> $$X = \begin{pmatrix} x_1^1 & x_1^2 & \dots & x_1^J \\ x_2^1 & x_2^2 & \dots & x_2^J \\ \vdots & \vdots & \ddots & \vdots \\ x_S^1 & x_S^2 & \dots & x_S^J \end{pmatrix}$$
>
> **Titoli AD in $\mathbb{R}^2$.** Un titolo AD $e_1=(1,0)'$: il payoff $(2,2)$ non può essere replicato; solo i payoff sull'asse orizzontale possono esserlo (ad es. il titolo $(1,0)'$ stesso). I mercati sono **incompleti**; lo spazio dei payoff (*asset span*) $\langle X\rangle$ è $\mathbb{R}$ (l'asse orizzontale).
>
> Aggiungendo un secondo titolo AD $e_2=(0,1)'$ a $e_1=(1,0)'$, qualsiasi payoff in $\mathbb{R}^2$ (incluso $(2,2)$) può essere replicato: i mercati sono **completi** e $\langle X\rangle = \mathbb{R}^2$.
>
> Aggiungendo un ulteriore titolo $(1,2)'$ a $\begin{pmatrix}1&0\\0&1\end{pmatrix}$, il nuovo titolo è **ridondante**: non amplia lo spazio dei payoff.
>
> **Titoli AD in $\mathbb{R}^S$.**
>
> $$X = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix}$$
>
> Con $S$ titoli AD, ogni stato $s$ può essere assicurato individualmente; tutti i payoff sono linearmente indipendenti; rango di $X$ = $S$; i mercati sono completi.
>
> **Struttura generale (esempio con obbligazione priva di rischio).** Torniamo a una struttura generale: è disponibile solo un'obbligazione priva di rischio $(1,1)'$. Tutti i titoli privi di rischio sulla retta a 45 gradi sono replicabili, ma nessuno dei titoli al di fuori di essa lo è. Il payoff $(1,2)'$ non può essere ottenuto: i mercati sono **incompleti**.
>
> Aggiungendo il titolo rischioso $(2,1)'$ all'obbligazione priva di rischio $(1,1)'$: portafoglio esempio, acquista 3 obbligazioni prive di rischio, vendi allo scoperto 1 titolo rischioso, ottenendo il payoff $(1,2)'$. I mercati sono completi con struttura dei titoli $\begin{pmatrix}2&1\\1&1\end{pmatrix}$; lo spazio dei payoff $\langle X\rangle$ coincide con quello di $\begin{pmatrix}1&0\\0&1\end{pmatrix}$: due titoli generano lo spazio dei payoff.
>
> **Struttura generale dei titoli — definizioni formali.** Un **portafoglio** è un vettore $h\in\mathbb{R}^J$ (quantità per ciascun titolo). Il payoff del portafoglio $h$ è $\sum_j h^j x^j = Xh$.
>
> **Asset span:**
>
> $$\langle X\rangle = \{z\in\mathbb{R}^S : z = Xh \text{ per qualche } h\in\mathbb{R}^J\}$$
>
> - $\langle X\rangle$ è un sottospazio lineare di $\mathbb{R}^S$
> - Mercati completi $\iff \langle X\rangle = \mathbb{R}^S$
> - I mercati sono completi se e solo se $\text{rango}(X) = S$
> - Mercati incompleti se $\text{rango}(X) < S$
> - Il titolo $j$ è **ridondante** se $x^j = Xh$ con $h^j = 0$
>
> Dato il vettore dei prezzi $p\in\mathbb{R}^J$ dei titoli, il costo del portafoglio $h$ è
>
> $$p\cdot h := \sum_j p^j h^j$$
>
> Se $p^j\neq 0$, il vettore del rendimento (lordo) del titolo $j$ è
>
> $$R^j = \frac{x^j}{p^j}$$

*(slide 55–64)*

## Frizioni di mercato: incompletezza e vincoli al trading

L'**incompletezza dei mercati** è di per sé una frizione, equivalente a un mercato con costi di transazione infiniti per scambiare titoli i cui payoff sono linearmente indipendenti rispetto ai titoli esistenti, per i quali invece i costi di transazione sono nulli. L'innovazione finanziaria può aiutare a "completare" il mercato: ad esempio, i cat bond (obbligazioni catastrofali), i derivati (se non ridondanti), i mercati predittivi, ecc.

Anche le limitazioni al trading sono una frizione: **vincoli dimensionali** e **vincoli sulle vendite allo scoperto** (ad es., divieti di vendita allo scoperto). Nel piano $(c_1,c_2)$, un vincolo dimensionale e un vincolo sulle vendite allo scoperto restringono la parte dello spazio dei payoff effettivamente raggiungibile dal portafoglio dell'investitore.

**Figura — Cronologia dei divieti di vendita allo scoperto per paese durante la crisi 2007/09** (Fonte: Beber e Pagano, 2013). Per ciascuno dei principali paesi (tra cui Australia, Austria, Belgio, Canada, Francia, Germania, Grecia, Irlanda, Italia, Giappone, Paesi Bassi, Norvegia, Portogallo, Corea del Sud, Spagna, Svizzera, Regno Unito, Stati Uniti) mostra i periodi, tra settembre 2008 e giugno 2009, in cui sono stati imposti divieti di vendita allo scoperto "covered" e "naked" su titoli finanziari e non finanziari. Conclusione: durante la crisi molti paesi hanno introdotto restrizioni temporanee e non coordinate tra loro alla vendita allo scoperto, concentrate soprattutto sui titoli finanziari.

*(slide 65–66)*

## Notazione vettoriale e le tre forme di assenza di arbitraggio

> [!abstract] Definizione
> **Notazione vettoriale.** Per $y,x\in\mathbb{R}^n$:
> - $y\ge x \iff y_i\ge x_i$ per ogni $i=1,\ldots,n$
> - $y> x \iff y\ge x,\ y\neq x$
> - $y\gg x \iff y_i> x_i$ per ogni $i=1,\ldots,n$
>
> Prodotto interno: $y\cdot x = \sum_i y_i x_i$.
>
> **Tre forme di assenza di arbitraggio**
>
> 1. **Legge del prezzo unico (LPU)** (*law of one price*, LOOP):
>
> $$Xh = Xk \;\Rightarrow\; p\cdot h = p\cdot k$$
>
> 2. **Assenza di arbitraggio forte.** Non esiste un portafoglio $h$ che costituisca un arbitraggio forte, cioè tale che
>
> $$Xh \ge 0 \quad \text{e} \quad p\cdot h < 0$$
>
> 3. **Assenza di arbitraggio.** Non esiste né un arbitraggio forte né un portafoglio $k$ tale che
>
> $$Xk > 0 \quad \text{e} \quad p\cdot k \le 0$$
>
> **Relazioni tra le tre nozioni.** La LPU è equivalente a: "ogni portafoglio con payoff nullo ha prezzo nullo". Inoltre:
>
> $$\text{Assenza di arbitraggio} \;\Rightarrow\; \text{Assenza di arbitraggio forte} \;\Rightarrow\; \text{LPU}$$

*(slide 67–69)*

## Pricing relativo e pricing assoluto

Gli elementi di un modello di asset pricing sono: lo spazio degli stati (evoluzione degli stati), le preferenze per il rischio, l'aggregazione tra diversi agenti e la struttura dei titoli (prezzi dei titoli scambiati). Il problema è che è difficile osservare le preferenze per il rischio: cosa possiamo dire sull'esistenza dei prezzi di stato senza assumere specifiche funzioni di utilità/vincoli per tutti gli agenti dell'economia?

**Pricing assoluto**
- Collegamento alle fonti macroeconomiche di rischio
- Esempi: modelli basati sul consumo
- Comuni nella ricerca accademica
- Permettono di formulare previsioni sugli effetti, ad esempio, di shock di politica economica

**Pricing relativo**
- Valutazione delle attività rispetto ai prezzi di altre attività
- Non focalizzato sulle fonti fondamentali di rischio
- Ampiamente applicato nell'industria finanziaria (es. pricing dei derivati)

**Dove ci si colloca?** Generalmente tra i due estremi: ad esempio, i modelli fattoriali si basano su premi per il rischio dei fattori presi (in pratica) come dati.

**Figura — Schema pricing relativo vs. assoluto.** Da un lato, specificando preferenze per il rischio e tecnologia (evoluzione degli stati, aggregazione), si ottengono i prezzi di stato $q$ (equivalentemente il fattore di sconto stocastico o la misura martingala) tramite l'assenza di arbitraggio/LOOP, da cui si derivano i prezzi delle attività (**pricing assoluto**). Dall'altro lato, osservando/specificando i prezzi di attività esistenti si ottengono gli stessi prezzi di stato $q$, da cui si deriva il prezzo di una nuova attività (**pricing relativo**). Conclusione: entrambi gli approcci convergono nella stessa nozione di prezzi di stato $q$, mentre differiscono nel punto di partenza (fondamentali vs. prezzi osservati).

*(slide 70–72)*

## Funzionali di pricing e prezzi di stato

> [!note] Dimostrazione
> Per ogni $z\in\langle X\rangle$ si definisce
>
> $$v(z) := \{p\cdot h : z = Xh\}$$
>
> Se vale la LPU, $v(z)$ è un **funzionale lineare**: a valore unico (stesso $z$ implica stesso prezzo), lineare su $\langle X\rangle$, e $v(0)=0$. Viceversa, se $v$ è un funzionale lineare su $\langle X\rangle$, allora vale la LPU.
>
> Dalla LPU segue $v(Xh) = p\cdot h$. Un funzionale lineare $V\in\mathbb{R}^S$ è una **funzione di pricing** se
>
> $$V(z) = v(z) \quad \text{per ogni } z\in\langle X\rangle$$
>
> Si ha $V(z) = q\cdot z$ per qualche $q\in\mathbb{R}^S$, dove $q_s = V(e_s)$ ed $e_s$ è il vettore con $e_s^s=1$ ed $e_s^i=0$ se $i\neq s$ ($e_s$ è un titolo AD). Il vettore $q$ è un **vettore di prezzi di stato**. Per ogni $z\notin\langle X\rangle$, $V(z)=q\cdot z$ con $q\in\mathbb{R}^S$ e $q_s=V(e_s)$: dunque $V(z)$ estende $v(z)$ da $\langle X\rangle$ a $\mathbb{R}^S$.
>
> **Prezzi di stato $q$.** $q$ è un vettore di prezzi di stato se $p = X'q$, cioè
>
> $$p^j = x^j\cdot q \quad \text{per ogni } j=1,\ldots,J$$
>
> Se $V(z)=q\cdot z$ è un funzionale di pricing, allora $q$ è un vettore di prezzi di stato. Viceversa, supponiamo che $q$ sia un vettore di prezzi di stato e che valga la LPU: se $z=Xh$, la LPU implica
>
> $$v(z) = \sum_j h^j p^j = \sum_j\left(\sum_s x_s^j q_s\right) h^j = \sum_s\left(\sum_j x_s^j h^j\right) q_s = q\cdot z$$
>
> Quindi: $V(z)=q\cdot z$ è un funzionale di pricing $\iff$ $q$ è un vettore di prezzi di stato e vale la LPU.
>
> **Esempio.** Con titoli di base $(1,1)'$ e $(2,1)'$, il valore delle due attività di base è
>
> $$p(1,1) = q_1+q_2, \qquad p(2,1) = 2q_1+q_2$$
>
> e il valore del portafoglio $(1,2)$ è
>
> $$3p(1,1) - p(2,1) = q_1+2q_2$$

*(slide 73–76)*

## Il teorema fondamentale della finanza

> [!tip] Teorema
> **Proposizione 1.** I prezzi dei titoli escludono l'arbitraggio se e solo se esiste un funzionale di pricing con $q\gg 0$.
>
> **Proposizione 2.** Sia $X$ una matrice $S\times J$, e $p\in\mathbb{R}^J$. Non esiste alcun $h$ in $\mathbb{R}^J$ tale che $h\cdot p \le 0$, $Xh \ge 0$ e almeno una disuguaglianza stretta $\iff$ esiste un vettore $q\in\mathbb{R}^S$ con $q\gg 0$ e $p = X'q$:
>
> $$\text{Assenza di arbitraggio} \iff \text{Prezzi di stato positivi}$$
>
> **Proposizione 3.** Il mercato è completo e non ci sono opportunità di arbitraggio se e solo se esiste un unico funzionale di pricing.

*(slide 77)*

## Le quattro formule di asset pricing

> [!note] Dimostrazione
> Il teorema fondamentale ammette quattro rappresentazioni equivalenti del prezzo di un titolo $j$:
>
> 1. **Prezzi di stato:** $p^j = \sum_s q_s x_s^j$
> 2. **Fattore di sconto stocastico** (o *pricing kernel*): $p^j = \mathbb{E}[m x^j]$
> 3. **Misura martingala:** $p^j = \dfrac{1}{1+r_f}\, \mathbb{E}^{\hat\pi}[x^j]$
> 4. **Rappresentazione con beta:** $\mathbb{E}[R^j] - R_f = \beta_j\left(\mathbb{E}[R^*]-R_f\right)$
>
> **1. Prezzi di stato.** Il prezzo è espresso in termini dei prezzi AD (di stato):
>
> $$p^j = \sum_s q_s x_s^j$$
>
> **2. Fattore di sconto stocastico.** Riscrivendo con le probabilità $\pi_s$:
>
> $$p^j = \sum_s q_s x_s^j = \sum_s \pi_s\, \frac{q_s}{\pi_s}\, x_s^j$$
>
> Definendo il fattore di sconto stocastico $m_s := q_s/\pi_s$, si ottiene
>
> $$p^j = \mathbb{E}[m x^j]$$
>
> **Aggiustamento per il rischio nei payoff.** Sfruttando la scomposizione della covarianza,
>
> $$p = \mathbb{E}[mx] = \mathbb{E}[m]\mathbb{E}[x] + \text{cov}(m,x)$$
>
> Poiché $p_{\text{titolo privo di rischio}} = \mathbb{E}[m\times 1]$, il tasso privo di rischio soddisfa
>
> $$\frac{1}{1+r_f} = \frac{1}{R^f} = \mathbb{E}[m]$$
>
> e dunque
>
> $$p = \frac{\mathbb{E}[x]}{R_f} + \text{cov}(m,x)$$
>
> Osservazioni: se non esiste un titolo privo di rischio, $1/\mathbb{E}(m)-1$ è il tasso privo di rischio ombra; solitamente $\text{cov}(m,x)<0$, dunque questo termine riduce il prezzo e aumenta il rendimento.
>
> **Aggiustamento per il rischio nei rendimenti.** Con $R^j := x^j/p^j$:
>
> $$\mathbb{E}[mR^j] = 1, \qquad R_f\,\mathbb{E}[m] = 1 \;\Rightarrow\; \mathbb{E}\left[m\left(R^j-R_f\right)\right]=0$$
>
> $$\mathbb{E}[m]\,\mathbb{E}[R^j-R_f] + \text{cov}(m,R^j) = 0$$
>
> $$\Rightarrow \quad \mathbb{E}[R^j] - R_f = -\frac{\text{cov}(m,R^j)}{\mathbb{E}[m]} \qquad \text{(vale anche per portafogli } h\text{)}$$
>
> Nota: la correzione per il rischio dipende solo da $\text{cov}(m,\text{payoff/rendimento})$; è remunerato solo il rischio sistematico, non il rischio idiosincratico.
>
> **3. Misura martingala equivalente.** Il prezzo di un titolo privo di rischio è
>
> $$p_{\text{titolo privo di rischio}} = \sum_s q_s = \frac{1}{1+r_f}$$
>
> Quindi
>
> $$p^j = \frac{1}{1+r_f}\sum_s \frac{q_s}{\sum_{s'} q_{s'}}\, x_s^j = \frac{1}{1+r_f}\, \mathbb{E}^{\hat\pi}[x^j], \qquad \text{dove } \hat\pi_s = \frac{q_s}{\sum_{s'} q_{s'}}$$
>
> La misura martingala equivalente è anche detta **misura neutrale al rischio**.
>
> **4. Rappresentazione con beta.** Si parte dalla rappresentazione del premio per il rischio dell'attività $j$:
>
> $$\mathbb{E}[R^j] - R_f = -\frac{\text{cov}(m,R^j)}{\mathbb{E}[m]}$$
>
> Questo vale anche per tutti i portafogli $h$, quindi si può sostituire $m$ con $m^*$, assumendo: (i) $\text{var}(m^*)>0$; (ii) $R^*=\alpha m^*$ con $\alpha>0$. Allora, per qualsiasi portafoglio $h$:
>
> $$\mathbb{E}[R^h] - R_f = -\frac{\text{cov}(R^*,R^h)}{\mathbb{E}[R^*]}$$
>
> Definendo $\beta_h := \dfrac{\text{cov}(R^*,R^h)}{\text{var}(R^*)}$, e applicando la relazione anche a $R^*$ stesso:
>
> $$\mathbb{E}[R^*] - R_f = -\frac{\text{cov}(R^*,R^*)}{\mathbb{E}[R^*]} = -\frac{\text{var}(R^*)}{\mathbb{E}[R^*]}$$
>
> si ottiene, dividendo membro a membro,
>
> $$\mathbb{E}[R^h] - R_f = \beta_h\left(\mathbb{E}[R^*]-R_f\right), \qquad \beta_h := \frac{\text{cov}(R^*,R^h)}{\text{var}(R^*)}$$
>
> **Sintesi.** La rappresentazione con beta $\mathbb{E}[R^j]-R_f = \beta_j(\mathbb{E}[R^*]-R_f)$, con $R^j:=x^j/p^j$, riflette l'avversione al rischio sovra(sotto)-pesando gli stati "cattivi (buoni)" nella misura martingala. Cosa sappiamo su $q$, $m$, $\hat\pi$, $R^*$? La loro **esistenza** è equivalente all'assenza di arbitraggio (dunque un unico fattore di sconto/prezzi di stato esiste), mentre la loro **unicità** vale se e solo se i mercati sono completi.

*(slide 78–86)*

## Il trade-off rischio-rendimento e l'asset pricing basato sulla domanda

**Di cosa si occupa l'asset pricing?** Riguarda la valutazione dei prezzi (o dei rendimenti) di titoli che generano payoff futuri incerti: prezzo basso $\iff$ rendimento atteso elevato. Occorre tenere conto del profilo temporale dei payoff e del loro rischio; le correzioni per il rischio sono la sfida principale (le variazioni dei premi per il rischio sono "la materia oscura dell'asset pricing"). Tutto il corso, teoricamente ed empiricamente, ruoterà attorno a questo: un approccio unificato alla valutazione di azioni, obbligazioni e altre attività, con rappresentazioni equivalenti in termini di fattori di sconto, beta, frontiere media-varianza.

**Il trade-off rischio-rendimento.** In mercati concorrenziali, la teoria prevede che attività più rischiose siano prezzate in modo da offrire rendimenti attesi più elevati rispetto ad attività meno rischiose: rischio e rendimento atteso sono positivamente correlati. L'evidenza empirica è tuttavia ampia e, in parte, contraddittoria.

**Figura — Tabella 3 (Ang, Hodrick, Xing, Zhang, 2009), volatilità idiosincratica e rendimenti attesi nei paesi G7.** Riporta stime di regressioni cross-country dei rendimenti su misure di volatilità idiosincratica (attesa e realizzata), controllando per size, book-to-market e momentum, con errori standard e $R^2$ aggiustato. Conclusione: l'evidenza sul legame tra volatilità idiosincratica e rendimento atteso è mista e non sempre statisticamente significativa nei diversi paesi del G7.

**Figura 7 — Intervalli di confidenza per le stime del coefficiente di trade-off rischio-rendimento, per paese e per il campione completo.** Per ciascun paese (tra cui Argentina, Grecia, Austria, Belgio, Regno Unito, Australia, Francia, Cecoslovacchia) e per il campione completo, presenta l'intervallo di confidenza al 95% della stima del coefficiente $\gamma$ e il numero di osservazioni mensili utilizzate. Conclusione: le stime sono molto eterogenee tra paesi, con ampi intervalli di confidenza, e risultano statisticamente significative solo in alcuni casi.

**Perché concentrarsi sul trade-off rischio-rendimento?** Nei modelli standard di asset pricing, i titoli sono quasi perfetti sostituti (sono semplicemente diritti su flussi di cassa futuri): ciò che conta maggiormente è il beta di un titolo e il suo contributo al rischio aggregato. In altre parole, vi è quasi perfetta sostituibilità tra le (molte) azioni con esposizione simile al rischio aggregato, il che implica curve di domanda quasi piatte per i singoli titoli (non a livello aggregato). Da qui l'attenzione su rendimenti attesi e rischio, supportata da prime evidenze empiriche su scambi di pacchetti di azioni (es. Scholes, 1972).

**Asset pricing basato sulla domanda.** Una visione più recente enfatizza le frizioni che possono rendere titoli con rischio simile non perfetti sostituti: vincoli di mandato, benchmarking, limiti all'arbitraggio, costi di transazione, credenze eterogenee, ecc. Test quasi-sperimentali recenti forniscono una visione coerente sull'elasticità-prezzo della domanda,

$$\xi = -\frac{\Delta Q/Q}{\Delta P/P}$$

**Figura — Stime dell'elasticità-prezzo della domanda $\xi$ in diversi studi quasi-sperimentali** (Fonte: Gabaix e Koijen, 2023). Confronta l'elasticità implicita dalla teoria standard con quelle ottenute da test quasi-sperimentali su indici, fondi comuni, flussi di cassa, fattori, domanda di attività ed evidenza internazionale. Conclusione: le elasticità stimate empiricamente sono generalmente molto più basse di quanto previsto dalla teoria standard, a supporto dell'approccio dell'asset pricing basato sulla domanda.

*(slide 88–92)*
