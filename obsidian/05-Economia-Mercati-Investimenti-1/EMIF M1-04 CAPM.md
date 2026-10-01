---
title: "CAPM — Capital Asset Pricing Model"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-04_CAPM.pdf"
pages: 42
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione

**Corso**: Economia dei mercati ed investimenti finanziari (EM5002) — Modulo su CAPM. Docente: Stefano Colonnello, Università Ca' Foscari Venezia.

Il tema centrale del CAPM si inserisce nel problema generale dell'*asset pricing*: in che modo gli asset finanziari collegano rischio e rendimento atteso?

- **Asset pricing**: in che modo gli asset finanziari collegano rischio e rendimento atteso?
- **Equilibrio**: i prezzi si aggiustano in modo che la domanda sia uguale all'offerta
- **Teoria di portafoglio** (equilibrio parziale): dati i prezzi, ogni investitore sceglie un portafoglio ottimo (trade-off rischio-rendimento)
- **CAPM** (equilibrio generale): determina prezzi e rendimenti attesi quando tutti gli investitori ottimizzano e domanda = offerta

La teoria di portafoglio (media-varianza) risolve il problema del singolo investitore dati i prezzi; il CAPM chiude il modello imponendo che tutti gli investitori ottimizzino simultaneamente e che i mercati siano in equilibrio (domanda = offerta), determinando così prezzi e rendimenti attesi in modo endogeno.

*(slide 1–2)*

## Capital Asset Pricing Model (CAPM): panoramica

Il CAPM è il **modello di equilibrio generale** alla base della moderna teoria della finanza.

- Basato su **diversificazione** e scelta di portafoglio **media-varianza** sotto ipotesi semplificatrici
- Risultato chiave: una **relazione di pricing lineare** che lega i rendimenti attesi al **rischio sistematico**
- Determina:
  - il **prezzo di mercato del rischio** (premio per il rischio di mercato)
  - la **misura di rischio rilevante** per un singolo titolo ($\beta_i$)
  - il **rendimento atteso richiesto** coerente con l'equilibrio
- Sviluppato indipendentemente da **Sharpe (1964)**, **Lintner (1965)** e **Mossin (1966)**
- È una **teoria positiva**: descrive le implicazioni di equilibrio (non fornisce indicazione normativa)

*(slide 3)*

## Ipotesi del modello

> [!abstract] Definizione
> **Ipotesi (I): mercati**
>
> - **Concorrenza perfetta**: gli investitori sono price takers
> - Orizzonte di investimento di **un periodo**
> - Insieme di investimento limitato ai titoli **scambiati pubblicamente**
> - Gli investitori possono **prestare e prendere a prestito** al tasso privo di rischio $r_f$
> - **Assenza di frizioni**: nessuna imposta né costo di transazione
> - I titoli sono **infinitamente divisibili**
> - Sono consentite le **vendite allo scoperto** (nessun vincolo)
>
> **Ipotesi (II): informazione e preferenze**
>
> - **Informazione perfetta**: l'informazione è gratuita e ugualmente disponibile per tutti gli investitori
> - **Investitori razionali**: ottimizzatori media-varianza (la scelta di portafoglio dipende solo da media e varianza)
> - **Aspettative omogenee**: belief (credenze) comuni su rendimenti attesi, varianze e covarianze
>
> **Riepilogo delle ipotesi**
>
> *Mercati perfetti*
> - Scambi senza frizioni e informazione perfetta
> - Nessuna imperfezione (imposte, regolamentazioni, vincoli sulle vendite allo scoperto)
> - Tutti i titoli sono negoziati pubblicamente e perfettamente divisibili
> - Concorrenza perfetta: tutti gli investitori sono price taker
>
> *Investitori*
> - Stesso orizzonte a un periodo
> - Razionali, massimizzano l'utilità attesa in uno spazio media-varianza
> - Belief omogenei
>
> **Cosa non è realistico?**
>
> Diverse ipotesi sono forti e spesso violate nella realtà:
> - Vi sono imposte, commissioni e altre frizioni di scambio
> - Molti investitori hanno orizzonti multi-periodali e obiettivi dinamici
> - Le aspettative sono eterogenee (previsioni e insiemi informativi diversi)
>
> Tuttavia, il CAPM fornisce un **benchmark utile** (e piuttosto robusto) per ragionare su rischio, diversificazione e rendimenti attesi.

*(slide 4–7)*

## Equilibrio, portafoglio di mercato e capital market line (CML)

> [!tip] Teorema
> **Condizioni di equilibrio**
>
> 1. Equilibrio degli investitori individuali (massimizzazione dell'utilità)
> 2. Domanda = offerta per tutti i titoli rischiosi (market clearing (1))
> 3. Crediti aggregati uguali ai debiti aggregati (market clearing (2))
>
> L'equilibrio risultante è tale che:
> - Tutti gli investitori detengono lo stesso portafoglio rischioso (il **portafoglio di mercato** $m$)
> - In questo caso, tutti ottengono la stessa MVF (frontiera media-varianza) e scelgono lo stesso portafoglio di tangenza
> - In equilibrio, il portafoglio di tangenza coincide con il portafoglio di mercato, cioè un portafoglio con pesi uguali al rapporto tra la capitalizzazione di mercato dei titoli e quella dell'intero mercato:
>
> $$w_i^{*} = \frac{P_i \times \#\,azioni_i}{\sum_i P_i \times \#\,azioni_i}$$
>
> **Portafoglio di tangenza comune**
>
> L'ingrediente aggiuntivo nel CAPM — oltre all'analisi media-varianza — è l'ipotesi che tutti gli investitori concordino su rendimenti attesi, varianze e covarianze dei titoli rischiosi. Di conseguenza, ogni investitore (indipendentemente da ricchezza o avversione al rischio) detiene i titoli rischiosi nelle stesse proporzioni: il portafoglio di tangenza è lo stesso per tutti e coincide con il portafoglio di mercato.
>
> **Il portafoglio di tangenza è il portafoglio di mercato**
>
> Ogni investitore detiene lo stesso portafoglio rischioso, ma in **quantità diverse**:
> - Gli investitori più ricchi possiedono un ammontare elevato del portafoglio, quelli più poveri uno esiguo
> - Investitori più (meno) avversi al rischio combinano più (meno) titolo privo di rischio con una posizione più piccola (più grande) nel portafoglio di tangenza
>
> Quindi, per equilibrare i mercati, il portafoglio di tangenza deve essere il portafoglio di mercato. La **capital market line (CML)** emerge endogenamente nel mondo CAPM come caso particolare della CAL (capital allocation line) in cui il portafoglio rischioso è il portafoglio di mercato.
>
> Poiché il portafoglio di mercato è efficiente in senso media-varianza, la CML è la CAL efficiente (quella con il massimo indice di Sharpe). L'implicazione è che la strategia ottima consiste nel detenere il portafoglio di mercato e regolare il rischio complessivo prendendo a prestito o investendo al tasso $r_f$. Questo fornisce il fondamento teorico per le strategie di **investimento passive** (ad esempio, investimenti indicizzati).
>
> **Figura (pag. 11)** — Capital Market Line (CML): asse verticale $E(r)$, asse orizzontale $\sigma$. La retta parte dal punto $(0, r_f)$ ed è tangente alla frontiera efficiente dei titoli rischiosi nel punto $m = (\sigma_m, E(r_m))$, etichettata CML. Mostra che ogni combinazione efficiente di rischio-rendimento si ottiene mescolando il titolo privo di rischio con il portafoglio di mercato.

*(slide 8–11)*

## Prezzo di mercato del rischio

> [!abstract] Definizione
> Il premio per il rischio di mercato dipende dall'avversione al rischio media, $\bar{A}$, e dal rischio aggregato non diversificabile:
>
> $$E(r_m) - r_f = \bar{A}\,\sigma_m^2$$
>
> Quindi il prezzo di una unità di rischio è:
>
> $$\bar{A} = \frac{E(r_m) - r_f}{\sigma_m^2}$$

*(slide 12)*

## CAPM: pricing assoluto vs pricing relativo

Il CAPM può essere visto in due modi complementari.

1. **Prospettiva di pricing assoluto**
   - Derivato da un modello completo di equilibrio generale
   - Indica quale deve essere il rendimento atteso di ciascun titolo in equilibrio
   - I prezzi sono determinati da preferenze aggregate, tecnologia e market clearing
   - Maggiori dettagli su questa prospettiva in appendice
2. **Prospettiva di pricing relativo**
   - In pratica, il modello è spesso derivato e usato per confrontare i titoli rispetto al mercato
   - I rendimenti attesi sono valutati in base all'esposizione al rischio sistematico (di mercato)
   - L'attenzione si sposta dai fondamenti di equilibrio a una relazione rischio-rendimento sezionale (cross-section)

**Tensione**: la teoria è derivata come modello di equilibrio assoluto, ma è più spesso applicata come benchmark di pricing relativo. Nel seguito il CAPM viene derivato come modello di pricing relativo.

*(slide 13)*

## Derivazione del CAPM: approccio di portafoglio

> [!note] Dimostrazione
> **Impostazione**
>
> Spesso le derivazioni del CAPM non partono dal modello basato sul consumo, ma seguono invece un **approccio di portafoglio**. Il CAPM mostra come collegare singoli titoli (o portafogli inefficienti) al portafoglio di mercato $m$: un investitore detiene un titolo solo se offre un rendimento atteso sufficiente a compensare il rischio che aggiunge al portafoglio efficiente. In equilibrio, il rischio aggiuntivo è esattamente compensato dal premio per il rischio aggiuntivo. Il rischio rilevante di un singolo titolo è la sua **covarianza** con il portafoglio di mercato.
>
> **Covarianza con il portafoglio di mercato**
>
> Il rendimento del portafoglio di mercato è:
>
> $$r_m = \sum_{i=1}^{N} w_i^{*} r_i$$
>
> Per un titolo generico $s$, la covarianza con il mercato è:
>
> $$\sigma_{sm} = Cov\!\left(r_s, \sum_{i=1}^{N} w_i^{*} r_i\right) = \sum_{i=1}^{N} w_i^{*}\,Cov(r_s, r_i)$$
>
> Ci si chiede quale sia il contributo del titolo $s$ al rischio del portafoglio di mercato.
>
> **Contributo al rischio di mercato**
>
> La varianza del portafoglio di mercato è:
>
> $$Var(r_m) = Var\!\left(\sum_{i=1}^{N} w_i^{*} r_i\right) = \sum_{i=1}^{N}\sum_{j=1}^{N} w_i^{*} w_j^{*}\,\sigma_{ij}$$
>
> Si può isolare il contributo del titolo $s$ prendendo i termini di una riga della matrice di covarianza con i corrispondenti pesi di portafoglio:
>
> $$\text{parte di } Var(r_m) \text{ dovuta a } s = \sum_{j=1}^{N} w_s^{*} w_j^{*} \sigma_{sj}$$
>
> Svolgendo la somma:
>
> $$= w_s^{*} w_1^{*} Cov(r_s,r_1) + w_s^{*} w_2^{*} Cov(r_s,r_2) + \cdots + w_s^{*} w_N^{*} Cov(r_s,r_N)$$
> $$= w_s^{*}\big(w_1^{*} Cov(r_s,r_1) + w_2^{*} Cov(r_s,r_2) + \cdots + w_N^{*} Cov(r_s,r_N)\big)$$
> $$= w_s^{*}\big(Cov(r_s, w_1^{*} r_1) + Cov(r_s, w_2^{*} r_2) + \cdots + Cov(r_s, w_N^{*} r_N)\big)$$
> $$= w_s^{*}\,Cov(r_s, w_1^{*} r_1 + w_2^{*} r_2 + \cdots + w_N^{*} r_N)$$
> $$= w_s^{*}\,Cov(r_s, r_m)$$
>
> Il contributo del titolo $s$ al rischio di mercato corrisponde quindi al prodotto tra la sua covarianza con il mercato e il suo peso nel portafoglio di mercato.
>
> **Contributo al rendimento atteso di mercato**
>
> Il rendimento atteso del portafoglio di mercato è:
>
> $$E(r_m) = E\!\left(\sum_{i=1}^{N} w_i^{*} r_i\right) = \sum_{i=1}^{N} w_i^{*} E(r_i)$$
>
> Il contributo del titolo $s$ è semplicemente:
>
> $$\text{parte di } E(r_m) \text{ dovuta a } s = w_s^{*} E(r_s)$$
>
> In termini di premio per il rischio:
>
> $$\text{parte di } [E(r_m) - r_f] \text{ dovuta a } s = w_s^{*}[E(r_s) - r_f]$$
>
> **Rischio e rendimento**
>
> La relazione rischio-rendimento per il titolo $s$ è il rapporto tra il contributo al premio e il contributo alla varianza:
>
> $$\frac{\text{parte di } [E(r_m)-r_f] \text{ dovuta a } s}{\text{parte di } Var(r_m) \text{ dovuta a } s} = \frac{w_s^{*}[E(r_s)-r_f]}{w_s^{*} Cov(r_s,r_m)} = \frac{E(r_s)-r_f}{\sigma_{sm}}$$
>
> Applicando la stessa relazione al portafoglio di mercato stesso:
>
> $$\frac{\text{parte di } [E(r_m)-r_f] \text{ dovuta a } m}{\text{parte di } Var(r_m) \text{ dovuta a } m} = \frac{E(r_m)-r_f}{\sigma_m^2}$$
>
> In equilibrio, tutti i titoli devono offrire lo stesso rendimento atteso aggiustato per la misura rilevante di rischio:
>
> $$\frac{E(r_s)-r_f}{\sigma_{sm}} = \frac{E(r_m)-r_f}{\sigma_m^2}$$
>
> **Equazione fondamentale del CAPM**
>
> Riarrangiando si ottiene l'equazione fondamentale del CAPM:
>
> $$E(r_s) - r_f = \beta_s [E(r_m) - r_f]$$
>
> oppure, in termini di rendimenti in eccesso:
>
> $$E(r_s^e) = \beta_s E(r_m^e), \qquad \text{dove } \beta_s = \frac{\sigma_{sm}}{\sigma_m^2}$$
>
> Il rendimento atteso del titolo $s$ è quindi la somma di:
> - **tasso privo di rischio**, che riflette il valore temporale del denaro;
> - **premio per il rischio**, proporzionale al premio per il rischio di mercato (MRP, market risk premium) e al coefficiente beta.
>
> Il premio per il rischio non dipende dalla volatilità totale del titolo: solo il **rischio sistematico** è prezzato.

*(slide 14–19)*

## CAPM per portafogli

> [!tip] Teorema
> L'equazione del CAPM vale per ciascun titolo $i$:
>
> $$E(r_i) = r_f + \beta_i [E(r_m) - r_f]$$
>
> Moltiplicando ciascuna equazione per il rispettivo peso di portafoglio $w_i$:
>
> $$w_1 E(r_1) = w_1 r_f + w_1 \beta_1 [E(r_m)-r_f]$$
> $$w_2 E(r_2) = w_2 r_f + w_2 \beta_2 [E(r_m)-r_f]$$
> $$\vdots$$
> $$w_n E(r_n) = w_n r_f + w_n \beta_n [E(r_m)-r_f]$$
>
> Sommando su tutti i titoli si ottiene il CAPM per un qualunque portafoglio $p$:
>
> $$E(r_p) = r_f + \beta_p [E(r_m) - r_f]$$
>
> In particolare, per il portafoglio di mercato $m$ stesso:
>
> $$E(r_m) = r_f + \beta_m [E(r_m) - r_f], \qquad \text{dove } \beta_m = 1 \text{ per costruzione}$$
>
> - $\beta_i > 1$: titoli con sensibilità al mercato superiore alla media
> - $\beta_i < 1$: titoli con sensibilità al mercato inferiore alla media

*(slide 20)*

## Security market line (SML)

> [!abstract] Definizione
> Il premio per il rischio di un singolo titolo dipende dal suo contributo al rischio del portafoglio di mercato. Graficamente, l'equazione fondamentale del CAPM è rappresentata nello spazio $(\beta_i, E(r_i))$ dalla **security market line (SML)**:
>
> $$E(r_i) = \underbrace{r_f}_{\text{intercetta}} + \underbrace{\beta_i [E(r_m) - r_f]}_{\text{pendenza (MRP)}}$$
>
> **Figura (pag. 21)** — SML nello spazio $(\beta, E(r_i))$: retta con intercetta $r_f$ e pendenza pari al premio per il rischio di mercato $E(r_m)-r_f$; il punto corrispondente a $\beta_m = 1{,}0$ ha ordinata $E(r_m)$. La pendenza della retta coincide con lo Slope of SML, cioè $E(r_m)-r_f$.
>
> **La SML: interpretazione**
>
> La SML fornisce il tasso di rendimento richiesto per un dato $\beta_i$.
>
> Implicazioni:
> - Un titolo correttamente prezzato giace esattamente sulla SML
> - In equilibrio, tutti i titoli devono giacere sulla SML
> - Titoli **sopra** la SML: **sottovalutati**
> - Titoli **sotto** la SML: **sopravvalutati**
>
> È ampiamente utilizzata nel settore del risparmio gestito per la valutazione della performance e la selezione dei titoli (spesso in forma multifattoriale — maggiori dettagli nella lezione su APT).
>
> **SML vs CML**
>
> | | SML | CML |
> |---|---|---|
> | Si applica a | singoli titoli (e a qualunque portafoglio) | portafogli efficienti, cioè combinazioni di $r_f$ e portafoglio $m$ |
> | Collega il rendimento atteso a | rischio sistematico $\beta$ | rischio totale $\sigma$ |
> | Rischio non remunerato | la volatilità totale non è remunerata di per sé; conta solo il rischio non diversificabile | il rischio totale è rilevante perché i portafogli sulla CML sono efficienti e ben diversificati |
> | Uso | strumento per valutazione del portafoglio | mostra che il rischio diversificabile non è remunerato |
>
> **Figura (pag. 23, sinistra)** — SML: asse $E(r)$ vs asse $\beta$ (range 0–1,5); una retta crescente su cui giace il punto $m$, con altri titoli/portafogli $A$, $B$, $C$, $D$ posizionati sopra o sotto la retta. Mostra come, nello spazio del beta, tutti i titoli correttamente prezzati giacciono sulla stessa retta indipendentemente dal loro rischio totale.
>
> **Figura (pag. 23, destra)** — CML: asse $E(r)$ vs asse $\sigma$ (range 0–0,2); una curva (frontiera efficiente) tangente a una retta che parte da $r_f$ e passa per $m$; gli stessi titoli $A$, $B$, $C$, $D$ sono sparsi nello spazio rischio totale-rendimento, generalmente sotto la CML se non efficienti. Mostra che solo i portafogli efficienti (combinazioni di $r_f$ e $m$) giacciono sulla CML, mentre i singoli titoli, pur avendo lo stesso $\beta$ nella SML, possono avere rischio totale molto diverso.

*(slide 21–23)*

## Uso del CAPM: alpha e gestione attiva

> [!example] Esempio
> **Uso del CAPM**
>
> Il CAPM determina il rendimento atteso di equilibrio di un'azione:
> - Rendimento atteso più alto di quanto implicato dal rischio sistematico → **sottovalutata** ($\alpha > 0$, sopra la SML)
> - Rendimento atteso più basso di quanto implicato dal rischio sistematico → **sopravvalutata** ($\alpha < 0$, sotto la SML)
>
> Questo apre la strada alla **gestione attiva** di portafoglio. In pratica, per ottenere $\alpha$ si stima una regressione single-index.
>
> **Figura (pag. 24)** — Grafico $E(r)$ (%) vs $\beta$ con la SML tracciata dai valori 6 (in $\beta=0$) fino a livelli più alti; un punto "Stock" è posizionato sopra la SML tra $\beta=1{,}0$ e $\beta=1{,}2$, con valori indicativi sull'asse $E(r)$ di 17, 15,6 e 14, e uno scarto $\alpha$ rispetto alla SML. Mostra graficamente un titolo sottovalutato, il cui rendimento atteso stimato eccede quello richiesto dal CAPM per il suo livello di $\beta$.
>
> **Modello a indice singolo e rendimenti in eccesso realizzati**
>
> Empiricamente, i rendimenti (in eccesso) realizzati sono spesso modellati tramite una regressione **single-index** su serie storiche. Questa specificazione è strettamente collegata al CAPM ma consente di avere $\alpha$ diverso da zero:
>
> $$r_{it}^{e} = \alpha_i + \beta_i r_{mt}^{e} + e_{it} \tag{1}$$
>
> dove $e_{it}$ è un termine di errore stocastico e $t = 1,\dots,T$.
>
> Supponiamo di ottenere le seguenti stime per il titolo A:
>
> $$r_{At}^{e} = 0.01 + 0.9\, r_{mt}^{e} + e_{At}$$
>
> Secondo il CAPM, il titolo A è sopravvalutato o sottovalutato?
>
> **Interpretare l'intercetta ($\alpha$)**
>
> L'intercetta della regressione è $0.01$. Secondo il CAPM, l'intercetta dovrebbe essere $0$: l'intercetta è quindi un "rendimento anomalo" non spiegato da $\hat\beta_A = 0.9$.
>
> Poiché $E(e_{At}) = 0$:
> - Single-index: $E(r_{At}^{e}) = 0.01 + 0.9\,E(r_{mt}^{e})$
> - CAPM: $E(r_{At}^{e}) = 0.9\,E(r_{mt}^{e})$
>
> L'azione è **sottovalutata** perché offre un rendimento atteso in eccesso più alto di quanto sarebbe coerente con il suo rischio sistematico.
>
> **Stime di alpha per fondi comuni**
>
> Alfa stimati per un campione di fondi comuni azionari con serie continua di 10 anni nel periodo 1972–1991, ottenuti stimando l'equazione (1). L'alfa medio è leggermente negativo e non significativo dal punto di vista statistico ($= -0.06$).
>
> Ci si chiede cosa dica questo risultato sulla performance corretta per il rischio dei fondi (l'evidenza è coerente con mercati efficienti in cui, al netto dei costi, i gestori attivi non riescono sistematicamente a battere il CAPM).
>
> **Figura (pag. 27)** — "Figure 1. Estimates of Individual Mutual-Fund Alphas 1972 to 1991" (Malkiel, 1995): istogramma della distribuzione di frequenza degli alfa stimati per fondi comuni azionari con serie continua di 10 anni. Mostra una distribuzione approssimativamente centrata vicino allo zero, coerente con un alfa medio del campione pari a $-0.06$ e non significativo.

*(slide 24–27)*

## CAPM: sintesi e valutazione

**Implicazione centrale**
- Il portafoglio di mercato è efficiente in senso media-varianza
- I rendimenti attesi sono lineari in $\beta_i$:
$$E(r_i) = r_f + \beta_i [E(r_m) - r_f]$$

**Premio per il rischio di mercato**
- Determinato dall'avversione al rischio aggregata $A$ e dalla varianza del mercato:
$$E(r_m) - r_f = A\,\sigma_m^2$$

**Intuizione economica**
- Solo il rischio sistematico (non diversificabile) è prezzato
- Il rischio idiosincratico è diversificabile e non è remunerato

**Punti di forza e limiti**
- Benchmark semplice e potente per il pricing dei titoli
- Può omettere altri fattori di rischio rilevanti
- Il vero portafoglio di mercato è inosservabile (problemi di misurazione)

*(slide 28)*

## Estensioni del CAPM

Il modello base è stato esteso in numerose direzioni:

- Assenza di titolo privo di rischio: **zero-beta CAPM** (Black, 1972)
- Titoli non negoziati / capitale umano: Mayers (1972)
- **CAPM intertemporale**: Merton (1973)
- Dividendi e imposte: Brennan (1970), Litzenberger e Ramaswamy (1979)
- Rischio di cambio: Solnik (1974)
- Inflazione: Long (1974), Friend, Landskroner e Losq (1976)
- CAPM internazionale, rischio PPP: Sercu (1980), Stulz (1981), Adler e Dumas (1983)
- Restrizioni agli investimenti: Stulz (1983)
- Effetti dimensione e book-to-market: Fama e French (1996)
- Ecc.

*(slide 29)*

## Zero-beta CAPM

> [!tip] Teorema
> In assenza di titolo privo di rischio (cioè in presenza di vincoli al finanziamento) si ottiene lo **zero-beta CAPM** (Black, 1972).
>
> - Ogni portafoglio sulla frontiera efficiente ha un portafoglio ad esso associato a correlazione zero sulla parte inefficiente della frontiera
> - Questo vale anche per il portafoglio di mercato $m$: esiste un portafoglio $z$ con $\beta_z = 0$ tale che si ottiene la seguente relazione:
>
> $$E(r_i) - E(r_z) = \beta_i [E(r_m) - E(r_z)]$$
>
> La SML risultante è più piatta di quella del CAPM standard, perché in genere $E(r_z) > r_f$.

*(slide 30)*

## CAPM intertemporale e portafogli di copertura

**CAPM intertemporale (ICAPM)**

Nel modello multiperiodale sviluppato da Merton nel 1973 (**CAPM intertemporale** o ICAPM) emergono fattori di rischio extra-mercato. Gli investitori ottimizzano consumo e investimento nel corso della loro vita e adattano continuamente tali piani alle nuove informazioni.

Oltre all'incertezza sui rendimenti di portafoglio (come nel CAPM base), in questo modello esistono altri due tipi di rischio:
- Cambiamenti nei parametri che descrivono le opportunità di investimento (tassi privi di rischio futuri, rendimenti attesi, rischio dei titoli)
- Cambiamenti nei prezzi dei beni di consumo (ad esempio, inflazione generale o variazioni dei prezzi di beni specifici come casa o energia)

**Portafogli di copertura (hedging)**

Finché i rendimenti di alcuni titoli sono correlati con cambiamenti nelle opportunità di investimento o nei prezzi di consumo, è possibile formare portafogli che coprono tali rischi (**portafogli di copertura** o di hedging). Gli investitori saranno disposti ad accettare rendimenti attesi più bassi sui portafogli di copertura.

Più in generale, $K$ fattori di rischio extra-mercato richiederanno premi per il rischio:

$$E(r_i) = \beta_{iM} E(r_m) + \sum_{k=1}^{K} \beta_{ik} E(r_k)$$

dove $\beta_{ik}$ è il beta sul $k$-esimo portafoglio di copertura. Il rendimento atteso è quindi la somma di: tasso privo di rischio, più premio per l'esposizione al rischio di mercato (come nel CAPM di base), più premi per il rischio per l'esposizione a ciascuna fonte di rischio extra-mercato.

*(slide 31–32)*

## Appendice: il modello basato sul consumo

> [!note] Dimostrazione
> *(Slide 33: pagina divisoria "Appendice")*
>
> Il CAPM può anche essere collegato alle scelte di consumo dell'investitore, in una logica di **pricing assoluto**.
>
> Si parte dal problema dell'investitore in un modello generale basato sul consumo:
> - Ottimizzazione di investimento, risparmio e composizione del portafoglio di titoli nel tempo
> - A partire da questo, si deriva il valore attuale al tempo $t$ di un titolo che dà accesso a un flusso di payoff futuri incerti
> - Si considera un payoff futuro $x_{t+1}$: ad esempio un'azione che paga un dividendo $d_{t+1}$ e ha un prezzo nel periodo successivo pari a $p_{t+1}$, tale che $x_{t+1} = d_{t+1} + p_{t+1}$
> - Domanda: qual è il valore che l'investitore attribuisce a $x_{t+1}$?
>
> **Il problema dell'investitore**
>
> L'investitore può comprare o vendere $x_{t+1}$ al prezzo $p_t$. Che quantità ($\xi$) ne acquisterà?
>
> - Funzione di utilità periodale $u(\cdot)$: crescente e concava (ad esempio, utilità potenza $u(c_t) = \frac{1}{1-\gamma} c_t^{1-\gamma}$, che diventa utilità logaritmica se $\gamma = 1$)
> - Fattore di sconto soggettivo ($\beta$): impazienza
> - Reddito ($e_t$)
>
> Il problema di ottimizzazione è:
>
> $$\max_{\{\xi\}} u(c_t) + E_t[\beta u(c_{t+1})]$$
>
> soggetto a:
>
> $$c_t = e_t - p_t \xi, \qquad c_{t+1} = e_{t+1} + x_{t+1}\xi$$
>
> Si deriva quindi la condizione del prim'ordine (CPO).
>
> **Fattore di sconto stocastico basato sul consumo**
>
> Dalla CPO si ottiene:
>
> $$p_t = E_t\!\left[\beta\,\frac{u'(c_{t+1})}{u'(c_t)}\,x_{t+1}\right]$$
>
> - La perdita di utilità da una unità aggiuntiva del titolo è $p_t\,u'(c_t)$
> - Il guadagno di utilità da una unità aggiuntiva del titolo è $E_t[\beta u'(c_{t+1}) x_{t+1}]$
> - Espresso in termini di quantità endogene, un modello completamente risolto esprime $p_t$ in funzione delle variabili esogene del modello (flusso di reddito $e_t$, $e_{t+1}$, insieme di titoli disponibili all'investitore)
>
> Quindi, nel modello basato sul consumo, il **fattore di sconto stocastico** è:
>
> $$m_{t+1} = \beta\,\frac{u'(c_{t+1})}{u'(c_t)}$$

*(slide 33–36)*

## Derivazione alternativa: utilità quadratica a due periodi

> [!note] Dimostrazione
> Il CAPM può essere derivato in contesti diversi, collegandolo alle scelte di consumo in vari modi, ad esempio con utilità quadratica a due periodi oppure con utilità esponenziale e distribuzione normale (trattata nella sezione successiva).
>
> **Impostazione**
>
> Gli investitori nascono con ricchezza $W_t$, non ricevono reddito da lavoro e possono investire in $N$ titoli diversi, ciascuno con rendimento $r_{it+1}$, con l'obiettivo di ottimizzare il consumo su due periodi secondo un'**utilità quadratica**:
>
> $$U(c_t, c_{t+1}) = -\frac{1}{2}(c^{*} - c_t)^2 - \frac{1}{2}\beta E\big[(c^{*}-c_{t+1})^2\big]$$
>
> Vincolo di bilancio:
>
> $$c_{t+1} = W_{t+1} = (1 + r_{Wt+1})(W_t - c_t)$$
> $$r_{Wt+1} = \sum_{i=1}^{N} w_i r_{it+1} \quad \text{(rendimento del portafoglio ricchezza)}$$
> $$\sum_{i=1}^{N} w_i = 1$$
>
> **Derivazione**
>
> Usando la definizione di $m_{t+1}$ basato sul consumo, si ottiene immediatamente la **linearità nel consumo** dell'utilità marginale:
>
> $$m_{t+1} = \beta\,\frac{u'(c_{t+1})}{u'(c_t)} = \beta\,\frac{c^{*}-c_{t+1}}{c^{*}-c_t}$$
>
> Sfruttando l'ipotesi che gli investitori consumino interamente la loro ricchezza nel secondo periodo ($c_{t+1} = W_{t+1}$), si può riscrivere $m_{t+1}$ ottenendo la sua dipendenza dal fattore $r_W$, che fa da proxy per l'utilità marginale:
>
> $$m_{t+1} = \beta\,\frac{c^{*} - (1+r_{Wt+1})(W_t - c_t)}{c^{*}-c_t}$$
>
> $$= \frac{\beta c^{*}}{c^{*}-c_t} - \frac{\beta(W_t - c_t)}{c^{*}-c_t}(1+r_{Wt+1})$$
>
> In forma più compatta, si ottiene una versione condizionata (cioè con quantità variabili nel tempo) del CAPM:
>
> $$m_{t+1} = a_t - b_t(1+r_{Wt+1})$$
>
> dove il portafoglio ricchezza coincide con il portafoglio di mercato.

*(slide 37–39)*

## Derivazione alternativa: utilità esponenziale e normalità

> [!note] Dimostrazione
> **Ipotesi**
>
> Si assume che gli investitori consumino solo nell'ultimo periodo e abbiano preferenze **CARA** (Constant Absolute Risk Aversion, utilità esponenziale):
>
> $$E[u(c)] = E[-e^{-Ac}]$$
>
> dove $A$ è il coefficiente di avversione al rischio assoluta (ARA).
>
> Assumendo consumo normalmente distribuito, $c \sim \mathcal{N}(E(c), \sigma^2(c))$, si può calcolare l'utilità attesa usando la funzione generatrice dei momenti:
>
> $$E[u(c)] = -e^{-AE(c) + (A^2/2)\sigma^2(c)}$$
>
> L'investitore sceglie tra il titolo privo di rischio e un paniere di titoli rischiosi; il suo vincolo di bilancio è:
>
> $$c = y_f R_f + y' R$$
> $$W = y_f + y'\mathbf{1}$$
>
> dove $R_i = 1 + r_i$, $y$ è il vettore $N \times 1$ contenente gli ammontari (non frazioni) investiti in ciascun titolo, $R$ è il vettore $N \times 1$ dei rendimenti.
>
> **Ottimizzazione**
>
> Usando il vincolo di bilancio, si può riscrivere $E[u(c)]$ come:
>
> $$E[u(c)] = -e^{-A[y_f R_f + y' E(R)] + (A^2/2) y' \Sigma y}$$
>
> dove $\Sigma$ è la matrice varianza-covarianza dei rendimenti rischiosi.
>
> Prendendo le CPO rispetto a $y$ e $y_f$, si trova l'ammontare ottimo da investire in titoli rischiosi:
>
> $$y = \Sigma^{-1}\,\frac{E(R) - R_f}{A}$$
>
> - Dipende dal rendimento atteso (linearmente), dalla varianza dei rendimenti e dall'avversione al rischio
> - È indipendente dalla ricchezza per via delle preferenze CARA
>
> **CAPM non condizionato**
>
> Si ottiene quindi un CAPM non condizionato:
>
> $$E(R) - R_f = A\Sigma y = A\,cov(R, R_W)$$
>
> - $y'R$: valore totale del portafoglio rischioso dell'investitore
> - $y_f R_f + y'R$: valore totale del portafoglio complessivo dell'investitore
> - $\Sigma y$: covarianza del rendimento di ciascun titolo con il portafoglio ricchezza
> - Con investitori identici (⇒ stesso portafoglio), $\Sigma y$ cattura anche la correlazione del rendimento di ciascun titolo con il portafoglio di mercato
>
> Applicando la relazione a $R_W$ stesso, si vede che il prezzo di mercato del rischio è direttamente collegato ad $A$ in questo contesto:
>
> $$E(R_W) - R_f = A\,\sigma^2(R_W)$$
>
> Questo è un caso specifico della rappresentazione con beta dei modelli di asset pricing (si veda la prima lezione).

*(slide 40–42)*
