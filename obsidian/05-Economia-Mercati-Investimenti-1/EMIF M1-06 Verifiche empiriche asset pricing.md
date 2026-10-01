---
title: "Verifiche empiriche dei modelli di asset pricing"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-06_Verifiche-empiriche-asset-pricing.pdf"
pages: 39
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: i modelli fattoriali lineari e le loro verifiche

> [!abstract] Definizione
> Si considerano i modelli più diffusi nella valutazione empirica dei titoli, cioè i **modelli fattoriali lineari**:
>
> $$p = E(mx), \qquad m = b'f$$
>
> Questa formulazione è equivalente a una **SML (Security Market Line) multivariata**:
>
> $$E(r^e) = \beta' \lambda$$
>
> I test di questi modelli sono tipicamente basati su due tipi di regressioni:
>
> 1. Regressioni su serie storiche (time-series regressions);
> 2. Regressioni sezionali (cross-sectional regressions).

*(slide 3)*

## Scelta della variabile dipendente

I modelli fattoriali lineari possono essere testati in termini di **rendimenti** o di **rendimenti in eccesso**. Ad esempio, nel caso del CAPM:

$$E(r_i) = r_f + \beta_i\big(E(r_m) - r_f\big) \qquad \text{oppure} \qquad E(r_i^e) = \beta_i\big(E(r_m) - r_f\big)$$

Le due specificazioni sono **equivalenti**, ma cambia l'interpretazione dei coefficienti di regressione:

- Nel primo caso, il modello implica che l'intercetta debba essere uguale a $r_f$;
- Nel secondo caso, l'intercetta dovrebbe essere zero.

In genere è più semplice lavorare sui rendimenti in eccesso, perché è possibile condurre semplicemente test di significatività sulle intercette stimate, vale a dire sugli **errori di pricing** (o alfa).

*(slide 4)*

## Scelta degli asset per i test

Generalmente è preferibile usare **portafogli** piuttosto che singoli titoli come test asset.

- L'uso di portafogli mitiga gli **errori nelle variabili** e migliora la stabilità delle stime di beta.
- Tali portafogli solitamente si ottengono ordinando i singoli titoli rispetto a una o più caratteristiche, per affinare la variazione sezionale.
  - Ad esempio, portafogli ampi casuali avranno beta prossimi a uno.
  - I **portafogli di Fama-French** sono la scelta più comune.
- I test basati su portafogli sono meno sensibili a eventuali effetti di microstruttura e illiquidità.

*(slide 5)*

## Regressioni su serie storiche: il modello a fattore singolo

> [!tip] Teorema
> Si considera un modello a fattore singolo in cui il fattore è un rendimento in eccesso, cioè è **traded** (ad es., $r_m^e = r_m - r_r$ nel CAPM), come tutti i test asset.
>
> La rappresentazione del modello rendimento atteso-beta è:
>
> $$E(r_i^e) = \beta_i E(f) \tag{1}$$
>
> che vale anche per il fattore stesso poiché è un rendimento in eccesso: $E(f) = 1 \times \lambda$.
>
> Il beta si può ottenere da una regressione di questo tipo:
>
> $$r_{it}^e = \alpha_i + \beta_i f_t + e_{it} \tag{2}$$
>
> Confrontando il modello (1) e il valore atteso di (2), l'implicazione del modello è:
>
> $$\alpha_i = 0, \qquad \forall i$$

*(slide 7)*

## Stima e test delle ipotesi nelle regressioni su serie storiche

Procedura tipica:

1. Stimare la specificazione (2) per ciascun test asset (tipicamente portafogli).
2. Stimare il premio per il rischio del fattore come media campionaria del fattore:

$$\hat\lambda = E(f)$$

3. Effettuare test $t$ per verificare la significatività degli errori di pricing $\alpha_i$.
4. Effettuare test per verificare se gli errori di pricing $\alpha_i$, $\forall i$, siano congiuntamente uguali a zero.

La teoria della distribuzione può essere costruita sulle ipotesi base di OLS (errori non correlati e omoschedastici) oppure su casi più generali per la struttura della covarianza degli errori:

- Errori standard di OLS generalizzati;
- Errori standard robusti all'eteroschedasticità (White);
- Correzione per correlazione seriale tramite errori standard di Hansen-Hodrick (utile per rendimenti sovrapposti).

*(slide 8)*

## Estensione ai modelli multifattoriali (serie storiche)

> [!abstract] Definizione
> Si consideri ora il caso di fattori multipli (tutti espressi come rendimenti in eccesso):
>
> $$r_{it}^e = \alpha_i + \beta_i' f_t + e_{it}$$
>
> La predizione di $\alpha$ uguale a zero è basata sul modello di riferimento:
>
> $$E(r_i^e) = \beta_i' E(f)$$
>
> Anche in questo caso è possibile stimare i coefficienti $\alpha$ e $\beta$ tramite regressioni OLS su serie storiche.

*(slide 9)*

## Regressioni sezionali: concetto generale

> [!abstract] Definizione
> Si consideri un modello a $K$ fattori:
>
> $$E(r_i^e) = \beta_i' \lambda, \qquad i = 1, 2, \ldots, N$$
>
> Si vuole capire perché i rendimenti medi variano tra i titoli e verificare se questa variazione dipende dai beta / premi per il rischio.
>
> **Grafico SML (fattore singolo, es. CAPM)** — sull'asse verticale il rendimento atteso $E(r_i^e)$, sull'asse orizzontale il beta $\beta_i$. Una retta con pendenza $\lambda$ passa vicino ai punti che rappresentano i vari asset $i$; i punti si discostano leggermente dalla retta (scarti). Anche se il modello è correttamente specificato, ci saranno alcuni scarti tracciando i rendimenti medi come funzione dei beta. Sono necessari test statistici per valutare questi scarti.

*(slide 11)*

## Approccio a due stadi per le regressioni sezionali

> [!abstract] Definizione
> Idea principale: la regressione sezionale serve a fittare al meglio, nel campione, le combinazioni rendimento atteso-beta. Ciò è fatto tramite un **approccio a due stadi**:
>
> 1. Regressioni su serie storiche per stimare i beta:
>
> $$r_{it}^e = a_i + \beta_i' f_t + e_{it}, \qquad \forall i,\ t = 1, 2, \ldots, T \tag{3}$$
>
> 2. Regressione sezionale (SML) per stimare i premi per il rischio $\lambda$:
>
> $$E(r_i^e) = \alpha + \hat\beta_i' \lambda + u_i, \qquad i = 1, 2, \ldots, N \tag{4}$$
>
> $\alpha$ è l'**errore di pricing**. La regressione (4) può essere specificata con o senza costante (cioè il rendimento in eccesso a beta zero):
>
> - La previsione teorica è che dovrebbe essere zero;
> - Esiste un trade-off tra efficienza e robustezza nella scelta.

*(slide 12)*

## Confronto tra regressioni su serie storiche e regressioni sezionali

> [!note] Dimostrazione
> L'approccio sezionale (cross-sectional) può essere usato anche con fattori che non sono rendimenti (non traded). L'approccio su serie storiche, invece, si basa su fattori in forma di rendimenti in eccesso per stimare i premi per il rischio come $\hat\lambda = E(f)$.
>
> Ci si può chiedere: perché non limitarsi a imporre una restrizione sulle intercette delle regressioni su serie storiche e testarla? Imponendo la restrizione $E(r_i^e) = \beta_i'\lambda$ sulla (3), si ottiene:
>
> $$r_{it}^e = \beta_i' \lambda + \beta_i'(f_t - E(f)) + e_{it}^i \qquad \forall i,\ t = 1, 2, \ldots, T$$
>
> da cui la restrizione sull'intercetta:
>
> $$a_i = \beta_i'(\lambda - E(f))$$
>
> L'intercetta è zero se $\lambda = E(f)$, ma questa restrizione non può essere verificata senza una stima di $\lambda$. Ne consegue che l'approccio sezionale è necessario se il fattore non è un rendimento.
>
> **Confronto interpretativo (fattore = rendimento):**
>
> - **Metodo su serie storiche**: il premio per il rischio del fattore è stimato come media campionaria del fattore; l'errore di pricing è nullo sul fattore stesso nel campione; il rendimento in eccesso è nullo sul rendimento in eccesso a beta zero; la SML stimata è semplicemente una retta passante per l'origine e per il fattore.
> - **Metodo sezionale**: la SML stimata è quella che fitta meglio il grafico a dispersione, consentendo anche di avere un'intercetta diversa da zero, minimizzando la somma dei quadrati degli errori di pricing.
>
> Il grafico di riferimento (identico a quello del paragrafo precedente) mostra $E(r_i^e)$ in funzione di $\beta_i$, con la retta di pendenza $\lambda$ e i punti-asset dispersi attorno a essa.

*(slide 13–14)*

## L'approccio di Fama e MacBeth (1973)

> [!abstract] Definizione
> Fama e MacBeth (1973) sviluppano un metodo alternativo per implementare l'approccio sezionale e correggere gli errori standard. Si consideri il caso a fattore singolo:
>
> 1. Si stimano i beta con regressioni su serie storiche a finestra mobile lungo l'intero campione.
> 2. Si stima una regressione sezionale in ogni periodo:
>
> $$r_{it}^e = \alpha_t + \hat\beta_i' \lambda_t + u_{it}, \qquad i = 1, 2, \ldots, N, \ \forall t$$
>
> 3. Infine si stimano $\lambda$ e $\alpha$ come medie nel tempo:
>
> $$\hat\lambda = \frac{1}{T}\sum_{t=1}^{T}\hat\lambda_t, \qquad \hat\alpha = \frac{1}{T}\sum_{t=1}^{T}\hat\alpha_t$$
>
> con errori di campionamento dati da:
>
> $$\sigma^2(\hat\lambda) = \frac{1}{T^2}\sum_{t=1}^{T}\big(\hat\lambda_t - \hat\lambda\big)^2, \qquad \sigma^2(\hat\alpha) = \frac{1}{T^2}\sum_{t=1}^{T}\big(\hat\alpha_t - \hat\alpha\big)^2$$
>
> dove si divide per $T^2$ perché di fatto sono errori standard di medie campionarie.
>
> **Intuizione.** L'errore di campionamento descrive come una statistica varia considerando campioni diversi; non è possibile studiarlo con un solo campione. L'approccio di Fama e MacBeth (1973) consiste nel partizionare il campione e studiare la variazione di $\hat\lambda_t$:
>
> - Varianza di campionamento della media campionaria per una serie $x_t$: $\sigma^2(\bar x) = \dfrac{\sigma^2(x)}{T} = \dfrac{1}{T^2}\sum_t (x_t - \bar x)^2$.
> - La stessa logica si applica alle stime di $\lambda$ e $\alpha_i$.
> - Il metodo consente anche di tener conto della correlazione seriale in $\hat\lambda_t$ (aspetto più importante in finanza aziendale che in asset pricing, dato che i rendimenti dei titoli mostrano bassa autocorrelazione).

*(slide 15–16)*

## Una breve storia dei test del CAPM

**Test iniziali** (ad es., Lintner, 1965):

- Basati su regressioni dei rendimenti medi delle singole azioni sui beta.
- Risultati insoddisfacenti: la SML risulta troppo piatta.
- Possibile ragione: errore di misurazione nei beta.

**Test basati su portafogli** (ad es., Jensen et al., 1972; Fama e MacBeth, 1973):

- L'errore di misurazione nei beta delle singole azioni provoca una distorsione di attenuazione (attenuation bias).
- Soluzione: formare portafogli ordinando le azioni sulla base dei loro beta.
- Calcolare quindi il beta dei portafogli ordinati per beta → stime più accurate.
- L'uso di portafogli rende anche più facile individuare differenze sezionali nei rendimenti medi.

**Test basati su portafogli formati ordinando le azioni** rispetto a dimensione, rapporto book-to-market, settore, ecc.

*(slide 18)*

## Procedura comune per testare i modelli fattoriali lineari

Procedura comune per testare modelli (fattoriali lineari) di asset pricing:

1. Identificare una caratteristica presumibilmente legata ai rendimenti medi.
2. Ordinare le azioni in base a tale caratteristica.
3. Verificare se i portafogli ordinati differiscono in termini di rendimento medio.
4. Stimare i beta dei portafogli.
5. Verificare se le differenze nei rendimenti medi tra portafogli sono spiegate dalle differenze nei beta dei portafogli.
6. Se no, questo può essere interpretato come un'**anomalia** e si rende necessario un modello con ulteriori fattori.

*(slide 19)*

## Evidenze sul CAPM: l'effetto piccola impresa

> [!example] Esempio
> Uno dei primi fallimenti del modello è l'**effetto piccola impresa** (Banz, 1981).
>
> **Figura 20.8** — *The CAPM. Average returns vs. betas on the NYSE value-weighted portfolio for 10 size-sorted stock portfolios, government bonds, and corporate bonds, 1947–1996. The solid line draws the CAPM prediction by fitting the market proxy and treasury bill rates exactly (a time-series test). The dashed line draws the CAPM prediction by fitting an OLS cross-sectional regression to the displayed data points. The small-firm portfolios are at the top right. The points far down and to the left are the government bond and treasury bill returns.* — Il grafico mostra i rendimenti medi in eccesso (%) sull'asse verticale e i beta sull'asse orizzontale; i portafogli delle piccole imprese si collocano in alto a destra, sopra la retta prevista dal CAPM (linea continua, test su serie storiche), evidenziando che tali imprese ottengono rendimenti superiori a quelli previsti dal loro beta di mercato. La retta tratteggiata (fit OLS cross-sectional) risulta più piatta della retta teorica.

*(slide 20)*

## CAPM vs. modello basato sul consumo

> [!example] Esempio
> La performance del CAPM è comunque superiore a quella di un semplice modello basato sul consumo.
>
> **Figura 20.8 (a) CAPM** — stesso grafico descritto in precedenza (rendimenti medi in eccesso vs. beta sul portafoglio value-weighted NYSE, 10 portafogli ordinati per dimensione più titoli di stato e obbligazioni societarie, 1947–1996).
>
> **Figura 2.4 (b) Modello basato sul consumo** — *Mean excess returns for 10 CRSP size portfolios versus predictions of the power utility consumption-based model. The predictions are generated by $-E[u'(c_{t+1})R^e]$ with $u = \beta(c_{t+1}/c_t)^{-\gamma}$, $\beta = 0.98$ and $\gamma = 241$ as picked by first-stage GMM to minimize the sum of squared pricing errors (deviation from 45° line). Source: Cochrane (1996).* — Il grafico confronta i rendimenti medi in eccesso osservati con quelli predetti dal modello basato sul consumo (asse orizzontale «predicted mean excess return»); i punti si discostano marcatamente dalla retta a 45°, indicando un fit peggiore rispetto al CAPM.

*(slide 21)*

## La critica di Roll

> [!tip] Teorema
> Le implicazioni verificabili del CAPM, $E(r_i^e) = \beta_i E(r_m^e)$, sono:
>
> 1. Relazione lineare tra rendimento atteso e $\beta$;
> 2. $\beta$ è l'unico rischio prezzato;
> 3. $\beta = 0 \Rightarrow E(r_i) = r_f$;
> 4. $\beta = 1 \Rightarrow E(r_i) = E(r_m)$;
> 5. Nessun rendimento anomalo non correlato al rischio sistematico;
> 6. Il portafoglio di mercato è **efficiente in media-varianza (MVE)**.
>
> **Roll (1977)**: l'implicazione principale del CAPM è che il portafoglio di mercato sia MVE.
>
> - Il vero portafoglio di mercato è non osservabile.
> - Qualsiasi proxy che sia MVE ex post soddisferà meccanicamente il CAPM.
> - Implicazione: i test del CAPM testano congiuntamente il modello **e** la proxy del mercato.
>
> **Repliche a Roll:**
>
> - **Stambaugh (1982)**: estendere la proxy (azioni + obbligazioni + immobili).
> - **Shanken (1987)**: anche con una proxy del mercato imperfetta, se questa è sufficientemente correlata con il vero portafoglio di mercato, il rifiuto del CAPM usando la proxy implica il rifiuto del CAPM stesso.
> - **Roll & Ross (1994)**: il CAPM può essere rigettato anche con proxy quasi efficienti.

*(slide 22)*

## Il modello a tre fattori di Fama e French (1993)

> [!abstract] Definizione
> Il modello a tre fattori di Fama-French (Fama and French, 1993, 1996) è il modello multifattoriale più comune nella letteratura. Risolve un importante limite del CAPM nello spiegare le differenze nei rendimenti medi tra imprese con diversi rapporti book-to-market.
>
> **Terminologia ed evidenze stilizzate:**
>
> - **Titoli value**: titoli con alto rapporto book-to-market.
> - **Titoli growth**: titoli con basso rapporto book-to-market.
> - **Value premium**: i titoli value mostrano rendimenti medi superiori rispetto ai titoli growth.
> - Questo premio non è spiegato da differenze nei beta di mercato medi.
>
> **Figura 20.9** — *Average returns vs. market beta for 25 stock portfolios sorted on the basis of size and book/market ratio.* — Lo scatterplot (excess return sull'asse verticale, beta on market sull'asse orizzontale) mostra portafogli con rendimenti medi molto dispersi (0,25–1,25) pur avendo beta di mercato concentrati in un intervallo ristretto (0,6–1,4): il value premium non è quindi spiegato da differenze nei beta di mercato.
>
> **Figura 20.10** — *Average excess returns vs. market beta. Lines connect portfolios of different size category within book/market category.* — **Figura 20.11** — *Average excess returns vs. market beta. Lines connect portfolios with different book market categories within size categories.* — Entrambi i grafici mostrano che, a parità di categoria dimensionale, i titoli value ordinati per book-to-market tendono ad avere rendimenti medi più alti pur presentando beta di mercato pari o persino inferiori rispetto ai titoli growth.
>
> In linea con l'**ICAPM**, Fama e French (1993) propongono un modello a tre fattori per spiegare queste tendenze nei rendimenti:
>
> $$E(r_i) - r_f = \beta_{i,m} E(r_m - r_f) + \beta_{i,h} HML + \beta_{i,s} SMB$$
>
> - **HML** (high-minus-low): rendimento di un portafoglio long su titoli value e short su titoli growth.
> - **SMB** (small-minus-big): rendimento di un portafoglio long su titoli small e short su titoli big.
>
> I beta sui fattori SMB e HML sembrano spiegare la variazione dei rendimenti medi di portafoglio:
>
> **Figura 20.12** — *Average excess return vs. prediction of the Fama-French three-factor model. Lines connect portfolios of different size category within book/market category.* — **Figura 20.13** — *Average excess returns vs. prediction of the Fama-French three-factor model. Lines connect portfolios of different book market category within the same size category.* — In entrambi i grafici (rendimento in eccesso atteso realizzato sull'asse verticale, rendimento predetto dal modello a tre fattori sull'asse orizzontale) i punti si allineano molto più vicini alla retta a 45° rispetto ai grafici basati sul solo beta di mercato, indicando che il modello a tre fattori spiega bene la variazione sezionale dei rendimenti medi.

*(slide 23–27)*

## Aggiustamento di HML per attività intangibili

> [!example] Esempio
> Eisfeldt, Kim e Papanikolaou (2022) trovano una performance aggiuntiva sul portafoglio fattoriale HML se si aggiusta il valore contabile per le attività intangibili ($HML^{INT}$). Inoltre, $HML^{INT}$ mantiene la capacità di pricing dell'HML tradizionale.
>
> **Figura 4** — *Note: This figure plots the cumulative returns of a portfolio that is long the long leg of $HML^{INT}$ and short the long leg of $HML^{TR}$ (solid blue line), as well as the returns of a portfolio that is long the short leg of $HML^{INT}$ and short the short leg of $HML^{TR}$ (dashed black line). Each panel plots returns from the beginning of 1975, 1985, and 2007. $HML^{TR}$ adds intangible assets to the book equity term of the book-to-market equity ratio for the HML portfolio sorts. Further details on factor construction can be found in Section 2 and Appendix A.* — I tre pannelli (a partire dal 1975, 1985 e 2007) mostrano che la componente long di $HML^{INT}$ rispetto a $HML^{TR}$ genera rendimenti cumulati positivi crescenti nel tempo, mentre la componente short mostra un andamento meno marcato: l'aggiustamento per gli intangibili aggiunge performance al fattore HML.

*(slide 28)*

## Perché esiste il premio su HML e SMB?

Perché gli investitori chiedono un premio per detenere titoli value e titoli small? Esistono due grandi filoni interpretativi:

- **Interpretazioni basate sul rischio** (rischio di dissesto finanziario, rischio macroeconomico).
- **Interpretazioni comportamentali**.

Si può inoltre vedere il modello di Fama e French (1993) semplicemente come un'implementazione della **APT**:

- Elevato $R^2$, tra il 90 e il 95%.
- Possibilità di ottenere quasi-arbitraggi in presenza di deviazioni dal rendimento atteso predetto dal modello?

*(slide 29)*

## Interpretazioni basate sul rischio

> [!example] Esempio
> **Liew e Vassalou (2000)** → il titolo sembra prevedere la crescita del PIL. Rispetto al rendimento di mercato, HML mostra una capacità aggiuntiva di previsione della crescita del PIL:
>
> $$GDP_{t\to t+1} = a + 0.065\, MKT_{t-1\to t} + 0.058\, HML_{t-1\to t} + e_{t+1}$$
>
> **Figura 13.2** — *Difference in return to factor portfolios in year prior to above-average versus below-average GDP growth. Both SMB and HML portfolio returns tend to be higher in years preceding better GDP growth. Source: L. Liew and M. Vassalou, "Can Book-to-Market, Size and Momentum Be Risk Factors That Predict Economic Growth?" Journal of Financial Economics 57 (2000), pp. 221–45.* — Il grafico a barre, per otto paesi (Australia, Canada, Francia, Germania, Italia, Giappone, Paesi Bassi, Svizzera, Regno Unito, Stati Uniti), mostra che le differenze di rendimento dei portafogli HML e SMB nell'anno precedente sono generalmente positive e più elevate quando la crescita del PIL successiva è superiore alla media.
>
> **Petkova and Zhang (2009)** → CAPM condizionale:
>
> - In espansione: beta value < beta growth.
> - In recessione: beta value > beta growth.
>
> **Figura 13.3** — *HML beta in different economic states. The beta of the HML portfolio is higher when the market risk premium is higher. Source: Rolitsa Petkova and Lu Zhang, "Is Value Riskier than Growth?" Journal of Financial Economics 78 (2005), pp. 187–202.* — Il beta del portafoglio HML nei diversi stati dell'economia (Value Beta < Growth Beta a sinistra, Value Beta > Growth Beta a destra) assume i seguenti valori:
>
> | Stato economico | Beta di HML |
> |---|---|
> | Peak | −0.33 |
> | Expansion | −0.15 |
> | Recession | 0.05 |
> | Trough | 0.40 |
>
> Il beta del portafoglio HML è quindi più elevato quando il premio per il rischio di mercato è più elevato (fasi recessive), coerentemente con un'interpretazione basata sul rischio del value premium.

*(slide 30–31)*

## Interpretazioni comportamentali

**Titoli glamour:**

- Recente buona performance.
- Prezzi elevati.
- Rapporti book-to-market più bassi.

**Prezzi elevati:**

- Ottimismo eccessivo.
- Sovrareazione ed estrapolazione di buone notizie.

**Figura 13.4** — *The book-to-market ratio reflects past growth, but not future growth prospects. B/M tends to fall with income growth experienced at the end of a five-year period, but actually increases slightly with future income growth rates. Source: L. K. C. Chan, J. Karceski, and J. Lakonishok, "The Level and Persistence of Growth Rates," Journal of Finance 58 (April 2003), pp. 643–84.* — Il grafico riporta sull'asse orizzontale i decili di tasso di crescita (Growth Rate Decile) e sull'asse verticale il rapporto book/market; la curva «Median Growth Rate» cresce monotonamente tra i decili, mentre «Beginning B/M» è pressoché piatta intorno a 0,6 e «Ending B/M» decresce da valori superiori a 1 fino a circa 0,4: ciò mostra che il book-to-market riflette la crescita passata ma non prevede la crescita futura.

**Figura 13.5** — *Value minus growth returns surrounding earnings announcements, 1971–1992. Announcement effects are measured for each of four years following classification as a value versus growth firm. Source: R. La Porta, J. Lakonishok, A. Shleifer, and R. W. Vishny, "Good News for Value Stocks," Journal of Finance 52 (1997), pp. 859–874.* — La differenza di rendimento (%) intorno agli annunci di utili, per anno successivo alla classificazione value/growth, è la seguente:

| Postformation Year | Difference in Returns (%) |
|---|---|
| 1 | 3.22 |
| 2 | 2.79 |
| 3 | 2.26 |
| 4 | 1.60 |
| 5 | 1.18 |

La differenza è massima nel primo anno successivo alla classificazione e decresce progressivamente, coerentemente con un'interpretazione comportamentale legata a sorprese sistematiche negli utili annunciati dai titoli growth (glamour) rispetto ai titoli value.

*(slide 32–34)*

## Fattori macroeconomici non traded

> [!example] Esempio
> Fattori macroeconomici (non traded), ad esempio Chen, Roll e Ross (1986):
>
> - Produzione industriale (IP);
> - Rischio di default (CG);
> - Struttura a termine dei tassi d'interesse (GB);
> - Inflazione (EI, UI);
> - (Oltre al mercato: EWNY, VWNY).
>
> Stime dal metodo a due stadi su portafogli costruiti per dimensione (capitalizzazione di mercato) come test asset:
>
> | | EWNI / VWNI | IP | EI | UI | CG | GB | Constant |
> |---|---|---|---|---|---|---|---|
> | **A (EWNI)** | 5.021 (1.218) | 14.009 (3.774) | −0.128 (−1.666) | −0.848 (−2.541) | 0.130 (2.855) | −5.017 (−1.576) | 6.409 (1.848) |
> | **B (VWNI)** | −2.403 (−0.633) | 11.756 (3.054) | −0.123 (−1.600) | −0.796 (−2.376) | 8.274 (2.972) | −5.905 (−1.879) | 10.713 (2.755) |
>
> Dove: VWNY = Return on the value-weighted NYSE index; EWNY = Return on the equally weighted NYSE index; IP = Monthly growth rate in industrial production; EI = Change in expected inflation; UI = Unanticipated inflation; CG = Unanticipated change in the risk premium (Baa and under return − Long-term government bond return); GB = Unanticipated change in the term structure (long-term government bond return − Treasury-bill rate); i t-statistics sono riportati tra parentesi.

*(slide 35)*

## Performance passata: momentum e inversione

> [!example] Esempio
> Performance passata:
>
> - **Momentum** (a breve termine).
> - **Inversione** (a lungo termine).
> - È comune integrare i fattori di Fama e French (1993) con un fattore di momentum.
> - Implicazioni per l'efficienza del mercato? (argomento della prossima sessione).
>
> **Tabella 20.12** — *Average monthly returns from reversal and momentum strategies.* Ogni mese si allocano tutti i titoli NYSE presenti nel CRSP in 10 portafogli in base alla loro performance durante l'intervallo dei «portfolio formation months». Ad esempio, l'intervallo 60-13 forma i portafogli sulla base dei rendimenti da 5 anni fa fino a 1 anno e 1 mese fa. Si acquista poi il portafoglio decile con la performance migliore e si vende allo scoperto quello con la performance peggiore.
>
> | Strategy | Period | Portfolio Formation Months | Average Return, 10-1 (Monthly %) |
> |---|---|---|---|
> | Reversal | 6307-9312 | 60-13 | −0.74 |
> | Momentum | 6307-9312 | 12-2 | +1.51 |
> | Reversal | 3101-6302 | 60-13 | −1.61 |
> | Momentum | 3101-6302 | 12-2 | +0.38 |
>
> Fonte: Fama and French (1996, Table VI).

*(slide 36)*

## Rischio di liquidità

> [!example] Esempio
> **Liquidità**: capacità di negoziare rapidamente a basso costo (costi di negoziazione, impatto sul prezzo, profondità del mercato).
>
> **Idea chiave di Pástor e Stambaugh (2003):**
>
> - Il flusso degli ordini induce inversioni di prezzo nei titoli illiquidi.
> - Inversioni maggiori ⇒ minor liquidità.
> - Si costruisce una misura aggregata di liquidità a partire dalle inversioni di rendimento.
>
> **Risultato principale:**
>
> - Il rischio di liquidità è **prezzato**.
> - I titoli che covariano con la liquidità aggregata ottengono rendimenti più alti.
>
> **Figura 13.6** — *Alphas of value-weighted portfolios sorted on liquidity betas. Source: L. Pástor and R. F. Stambaugh, "Liquidity Risk and Expected Stock Returns," Journal of Political Economy 111 (2003), pp. 642–85, Table 4.* — Il grafico a barre mostra, per decile di illiquidità (Lowest → Highest) e per due modelli (CAPM Alpha e FF Alpha), che gli alfa sono fortemente negativi nei decili più bassi (titoli meno esposti al rischio di liquidità) e diventano positivi nei decili più alti, indicando che i titoli più sensibili al rischio di liquidità aggregata ottengono rendimenti anomali più elevati non spiegati né dal CAPM né dal modello a tre fattori di Fama-French.

*(slide 37–38)*

## Anomalie rispetto al CAPM e lo zoo dei fattori

Le evidenze contro il CAPM mostrano una variazione sezionale dei rendimenti attesi non spiegata solo dai beta di mercato.

**Principali categorie di anomalie** (Hou, Xue, and Zhang, 2015):

- Value vs. growth;
- Investimento;
- Redditività;
- Intangibili;
- Frizioni di trading;
- Momentum.

Si osserva inoltre la crescita del cosiddetto **"zoo dei fattori"** (molti predittori proposti in letteratura):

- Problemi di data mining / test multipli.
- Molte anomalie si indeboliscono dopo la loro scoperta.

**Conclusione**: la variazione sistematica dei rendimenti va oltre il beta del CAPM.

*(slide 39)*
