---
title: "Financial Economics — Sessione 2.4: Analisi di Stile"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_Financial-Economics-generale.pdf"
pages: 41
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione e riferimenti bibliografici

**Financial Economics (EM5021)** — Sessione 2.4: *Analisi di Stile*

Docente: Loriana Pelizzon — Università Ca' Foscari Venezia.

**Riferimenti:**
- EGBG
- BKM, capitolo **24 — Valutazione della Performance di Portafoglio**

*(slide 1–2)*

## Origine dell'analisi di stile: l'idea di Sharpe

L'**analisi di stile** è stata introdotta da **William Sharpe**.

- In un campione di **82 fondi comuni**, oltre il **90%** della variazione nei rendimenti di portafoglio deriva dall'asset allocation in azioni/obbligazioni/titoli a breve.
- Il resto è dovuto alla capacità del gestore di selezionare titoli e di fare market timing.

**Idea di base:** regredire i rendimenti del fondo su indici che rappresentano diverse classi di attività.
- Il coefficiente di regressione su ciascun indice misura l'allocazione implicita del fondo a quello "stile".
- L'$R^2$ misura la variabilità dei rendimenti dovuta allo stile (all'asset allocation).

Lettura consigliata: https://web.stanford.edu/~wfsharpe/art/sa/sa.htm

*(slide 3)*

## Il modello a fattori per classi di attività

> [!abstract] Definizione
> La maggior parte delle misure di performance deriva dal CAPM. L'analisi di stile è un metodo conveniente per tenere conto di molti fattori (in linea con l'impostazione APT) all'interno di un framework di regressione:
>
> $$\tilde{R}_i = b_{i1}\tilde{F}_1 + b_{i2}\tilde{F}_2 + \dots + b_{in}\tilde{F}_n + \tilde{e}_i \qquad (1)$$
>
> dove $R$ è il rendimento del portafoglio, $F$ è il valore del fattore, $b$ sono le esposizioni (beta) del fondo a ciascun fattore, e $e$ è la componente di rendimento non legata ai fattori.
>
> - La somma dei termini $bF$ è il rendimento dovuto **allo stile** (gestione passiva).
> - $e$ è il rendimento dovuto **alla selezione e al timing** (gestione attiva).
>
> Il *Modello a Fattori per Classi di Attività* si scrive equivalentemente come:
>
> $$\tilde{R}_t = \underbrace{\beta_1 \tilde{F}_{1t} + \dots + \beta_n \tilde{F}_{nt}}_{\text{Gestione passiva (Stile)}} + \overbrace{\hat{e}_t}^{\text{Gestione attiva (Selezione)}}, \qquad t = 1,\dots,T$$
>
> soggetto ai vincoli:
>
> $$0 \le \beta_i \le 1, \qquad \sum_{i=1}^{n} \beta_i = 1$$
>
> **Requisiti delle classi di attività.** Le classi di attività usate come fattori devono essere:
> 1. Mutuamente esclusive;
> 2. Esaustive;
> 3. Avere profili di rendimento diversi.
>
> Sono costruite come portafogli di titoli ponderati per capitalizzazione di mercato, in cui ciascun titolo è incluso in un solo portafoglio di stile, e gli stili hanno bassa correlazione (o varianze diverse) tra loro.
>
> **Varianza spiegata / non spiegata:**
>
> $$R^2 = 1 - \frac{\mathrm{Var}(\tilde e_i)}{\mathrm{Var}(\tilde R_i)} \qquad (2)$$
>
> **Il problema di ottimizzazione da risolvere** consiste nel massimizzare l'$R^2$ scegliendo i pesi $\beta_i$:
>
> $$\max_{\beta} \; R^2 = 1 - \frac{\mathrm{Var}(\tilde e_i)}{\mathrm{Var}(\tilde R_i)} \qquad (2)$$
>
> $$\text{s.t.} \quad 0 \le \beta_i \le 1, \qquad \sum_{i=1}^{n}\beta_i = 1$$

*(slide 4–7)*

## Determinazione delle esposizioni: procedura e classi di attività

**Determinazione delle esposizioni alle principali classi di attività** richiede di considerare:
- l'importo che l'investitore ha nei vari fondi;
- le esposizioni alle classi di attività, cioè ciò che il fondo ha investito nei vari titoli e l'esposizione dei titoli alle classi di attività.

**Regressioni.** Si effettua un'analisi di regressione multipla con due vincoli:
- i coefficienti sommano al 100%;
- le stime dei coefficienti sono comprese tra 0 e 1 (nessuna posizione corta).

**Esempio di 12 classi di attività** usate tipicamente come regressori nell'analisi di stile:

| | |
|---|---|
| Titoli a breve termine | Azioni large cap Growth |
| Obbligazioni gov. a medio termine | Azioni a media capitalizzazione |
| Obbligazioni gov. a lungo termine | Azioni a piccola capitalizzazione |
| Obbligazioni societarie | Obbligazioni non-USA |
| Titoli legati ai mutui | Azioni europee |
| Azioni large cap Value | Azioni giapponesi |

*(slide 8–9)*

## Esempio guidato: analisi di stile "da zero" di un fondo bilanciato

> [!example] Esempio
> Si consideri un fondo bilanciato. Sono disponibili 12 mesi di rendimenti e tre indici di classi di attività:
>
> | Mese | Fondo (%) | Indice Az. (%) | Indice Obbl. (%) | Liquidità (%) |
> |---|---|---|---|---|
> | 1 | 2.1 | 3.5 | 0.8 | 0.3 |
> | 2 | −1.4 | −2.8 | 0.5 | 0.3 |
> | 3 | 1.8 | 2.9 | 0.6 | 0.3 |
> | 4 | 0.5 | 0.2 | 1.0 | 0.3 |
> | 5 | −0.8 | −1.5 | 0.2 | 0.3 |
> | 6 | 3.0 | 4.8 | 0.7 | 0.3 |
> | 7 | 1.2 | 1.5 | 0.9 | 0.3 |
> | 8 | −2.0 | −3.5 | 0.4 | 0.3 |
> | 9 | 1.5 | 2.2 | 0.8 | 0.3 |
> | 10 | 0.9 | 1.0 | 1.1 | 0.3 |
> | 11 | 2.5 | 3.8 | 0.6 | 0.3 |
> | 12 | −0.3 | −0.9 | 0.7 | 0.3 |
>
> **Passo 1 — Regressione OLS non vincolata:**
>
> $$R_{fondo,t} = \beta_1 R_{azionario,t} + \beta_2 R_{obbl.,t} + \beta_3 R_{liquidità,t} + e_t$$
>
> L'OLS fornisce: $\hat\beta_1 = 0{,}62$, $\hat\beta_2 = 0{,}45$, $\hat\beta_3 = -0{,}08$.
>
> Problema: $\hat\beta_3 < 0$ (implica una posizione corta sulla liquidità) e $\sum \hat\beta_i = 0{,}99 \ne 1$.
>
> **Passo 2 — Ottimizzazione vincolata** (analisi di stile di Sharpe): minimizzare $\sum e_t^2$ soggetto a $\beta_i \ge 0$ e $\sum \beta_i = 1$:
>
> | | $\beta_{azionario}$ | $\beta_{obbl.}$ | $\beta_{liquidità}$ |
> |---|---|---|---|
> | Non vincolato | 0,62 | 0,45 | −0,08 |
> | **Vincolato** | **0,58** | **0,42** | **0,00** |
>
> Il vincolo forza il peso negativo della liquidità a zero, riallocando gli altri pesi.
>
> **Passo 3 — Interpretazione dei risultati.**
>
> **Figura** — Grafico a barre "Peso dello Stile (%)" con i pesi vincolati: Azionario 58, Obbligazionario 42, Liquidità 0. Il grafico mostra visivamente la ripartizione 58/42 tra azionario e obbligazionario, con esposizione nulla alla liquidità dopo il vincolo di non negatività.
>
> - $R^2 = 0{,}96$: il 96% della variazione dei rendimenti del fondo è spiegato dallo stile.
> - Il fondo si comporta come un mix 58/42 azionario/obbligazionario.
> - Il restante 4% ($=1-R^2$) è il contributo attivo del gestore.
> - Tracking error rispetto al benchmark di stile: $\sigma(e) \approx 0{,}35\%/\text{mese}$.

*(slide 10–12)*

## Caso di studio: Trustees' Commingled Fund (Sharpe, 1992)

> [!example] Esempio
> **Trustees' Commingled Fund** (Gennaio 1985 – Dicembre 1989). Confronto tra tre metodi di stima dei pesi di stile su 12 classi di attività:
>
> | | Regressione Non Vincolata | Regressione Vincolata | Programmazione Quadratica |
> |---|---|---|---|
> | Titoli a breve | 14,69 | 42,65 | 0 |
> | Obbl. a medio termine | −69,51 | −68,64 | 0 |
> | Obbl. a lungo termine | −2,54 | −2,38 | 0 |
> | Obbl. societarie | 16,57 | 15,29 | 0 |
> | Mutui | 5,19 | 4,58 | 0 |
> | Azioni Value | 109,52 | 110,35 | 69,81 |
> | Azioni Growth | −7,86 | −8,02 | 0 |
> | Azioni medie | −41,83 | −43,62 | 0 |
> | Azioni piccole | 45,65 | 47,17 | 30,04 |
> | Obbl. estere | −1,85 | −1,38 | 0 |
> | Azioni europee | 6,15 | 5,77 | 0,15 |
> | Azioni giapponesi | −1,46 | −1,79 | 0 |
> | **Totale** | **72,71** | **100,00** | **100,00** |
> | **R-quadro** | **95,20** | **95,16** | **92,22** |
>
> Si noti come la regressione non vincolata produca pesi estremi e persino negativi (es. −69,51 su obbligazioni a medio termine), che sommano solo a 72,71 anziché 100. Il vincolo di somma unitaria e non negatività (programmazione quadratica) concentra l'esposizione quasi interamente su Azioni Value e Azioni piccole, con un $R^2$ leggermente inferiore (92,22 contro 95,20).

*(slide 13)*

## Caso di studio: Fidelity Magellan Fund — scomposizione stile/selezione

> [!example] Esempio
> **Fidelity Magellan Fund**, Gennaio 1985 – Dicembre 1989. Stile stimato su 60 rendimenti mensili:
>
> | Classe di Attività | Peso (%) |
> |---|---|
> | Azioni Growth | 71 |
> | Azioni medie | 24 |
> | Azioni piccole | 5 |
> | Tutte le altre | 0 |
>
> **Scomposizione del rendimento:** $R^2$ = stile; $1-R^2$ = selezione (stock picking o market timing).
>
> **Figura** — Grafico a torta: Selezione 2,7%, Stile 97,3%. Mostra che oltre il 97% della variazione dei rendimenti del Fondo Magellan è spiegata dallo stile (asset allocation); meno del 3% è attribuibile alla selezione attiva del gestore. (Lo stesso grafico, con gli stessi valori, è ripresentato più avanti nel deck sotto il titolo "Analisi di Stile Sharpe (1992)".)
>
> **Portafoglio di stile con 7 indici (analisi alternativa):**
>
> | Portafoglio di Stile | Coefficiente di Regressione |
> |---|---|
> | T-Bill | 0 |
> | Small Cap | 0 |
> | Medium Cap | 35 |
> | Large Cap | 61 |
> | Alto P/E (growth) | 5 |
> | Medio P/E | 0 |
> | Basso P/E (value) | 0 |
> | **Totale** | **100** |
> | **R-quadro** | **97,5** |
>
> **Figura** — Diagramma $E(r)$ vs $\sigma$ con Capital Market Line (CML), la Capital Allocation Line del portafoglio $P$ (CAL(P)), il punto risk-free $F$, il portafoglio di mercato $M$, il portafoglio $M^2$ (aggiustato per il rischio del portafoglio in esame) e i punti $P$ e $P^*$. Il grafico illustra visivamente come il portafoglio del fondo ($P$) si collochi rispetto alla frontiera efficiente (CML) e alla propria CAL, un richiamo alle misure di performance risk-adjusted (Sessione 2.3) applicate al confronto tra $M$ e $P$.

*(slide 14–19)*

## Deriva di stile: analisi a finestra mobile

> [!example] Esempio
> Un "Fondo Value" viene analizzato con finestre mobili di 24 mesi.
>
> **Figura** — Grafico ad area impilata "Peso dello Stile (%)" nel tempo (2019–2024) con tre serie: Value, Growth, Small Cap. Mostra che il peso Value scende progressivamente nel tempo mentre Growth e Small Cap aumentano la propria quota.
>
> Il fondo è *derivato* dal 75% value al 22% value in cinque anni. Un'analisi sull'intero campione mostrerebbe $\approx 45\%$ value, mascherando completamente lo spostamento: le finestre mobili rivelano la vera traiettoria.
>
> **Perché la deriva di stile è importante?**
> - **Per l'investitore:** se si è scelto un fondo value per la diversificazione e questo deriva verso il growth, il portafoglio complessivo diventa sbilanciato senza che l'investitore se ne accorga.
> - **Per la valutazione della performance:** l'alfa di una regressione sull'intero campione è privo di significato se il benchmark è cambiato a metà campione. Il fondo potrebbe mostrare un alfa positivo rispetto a un indice value semplicemente perché si è spostato verso il growth durante un rally growth.
> - **Per la gestione del rischio:** le caratteristiche di rischio cambiano con lo stile. Una deriva da value a growth aumenta l'esposizione del portafoglio al rischio di duration e alle inversioni di momentum.
>
> **Regola pratica:** confrontare sempre i pesi di stile sull'intero campione con quelli della finestra mobile più recente. Una grande discrepanza segnala una deriva attiva.
>
> **Applicazione al Trustees' Commingled Fund (composizione di stile del portafoglio U.S., 1986–1989):** l'analisi di stile a finestra mobile mostra che il fondo era prevalentemente investito in Azioni Value ($\approx 60$–$80\%$), con allocazioni minori in Azioni Small, Azioni Growth, Azioni Europee e Azioni Giapponesi, variabili nel tempo. In questo caso la composizione di stile era notevolmente stabile, con le Azioni Value che dominavano costantemente l'allocazione durante l'intero periodo campionario (a differenza dell'esempio del "Fondo Value" sopra, dove la finestra mobile rivela invece una deriva marcata).

*(slide 16–18)*

## Benchmark multifattoriali e tracking error

L'analisi di stile rivela il **benchmark più vicino** al fondo. Occorre però prudenza con i benchmark multifattoriali:
- l'uso di un benchmark diverso dal singolo indice è legittimo solo se si assume che i portafogli fattoriali facciano parte della strategia passiva disponibile al fondo;
- ad esempio, il benchmark Fama-French a 3 fattori (FF3) implicherebbe che la strategia passiva sia la combinazione dell'indice di mercato con i fattori SMB e HML.

**Figura 24.5** — *Average tracking error for 636 mutual funds, 1985–1989* (fonte: William F. Sharpe, "Asset Allocation: Management Style and Performance Evaluation", Journal of Portfolio Management, Winter 1992, pp. 7–19). Istogramma della distribuzione del tracking error medio mensile (%) su 636 fondi comuni: la distribuzione è concentrata e simmetrica attorno a valori vicini allo zero, con la maggior parte dei fondi che presenta un tracking error medio compreso approssimativamente tra −0,50% e +0,50% al mese rispetto al proprio benchmark di stile.

*(slide 20–28)*

## Confronto: analisi di stile basata sui rendimenti vs. sulle posizioni

| | Basata sui Rendimenti (Sharpe) | Basata sulle Posizioni (Morningstar) |
|---|---|---|
| **Dati necessari** | Solo rendimenti del fondo e degli indici | Comunicazione completa delle posizioni in portafoglio |
| **Cattura derivati e leva** | Sì — riflette l'esposizione effettiva | No — vede solo le posizioni dichiarate |
| **Tempestività** | Retrospettiva (usa una finestra passata) | Più attuale (data dell'ultima segnalazione) |
| **Trading dinamico** | Cattura lo stile medio sulla finestra | Istantanea in un singolo momento |
| **Sensibilità alla finestra** | I risultati dipendono dal periodo di stima | Non applicabile |
| **Disponibilità** | Universale (qualsiasi fondo con storico di rendimenti) | Solo fondi che comunicano le posizioni |

**Best practice:** usare entrambe. L'analisi basata sui rendimenti cattura ciò che il fondo *effettivamente fa* nel tempo (incluse leva e derivati), mentre l'analisi basata sulle posizioni fornisce una fotografia più tempestiva e diretta della composizione dichiarata del portafoglio.

*(slide 21)*

## Esempio: individuare un closet indexer e il costo delle commissioni

> [!example] Esempio
> Il fondo "**Alpha Select European Equity**" è commercializzato come a gestione attiva, con commissione dell'1,20% annuo. Analisi di stile rispetto all'MSCI Europe:
>
> | | Fondo "Alpha Select" | Fondo Attivo Tipico |
> |---|---|---|
> | $\beta_{\text{MSCI Europe}}$ | 0,97 | 0,85 |
> | $R^2$ | 0,98 | 0,88 |
> | Tracking error (ann.) | 1,2% | 5,5% |
> | Active Share | 15% | 65% |
> | Commissioni | 1,20% | 1,20% |
>
> Con $R^2 = 0{,}98$ e Active Share = 15%, "Alpha Select" è un **closet indexer**: replica essenzialmente l'MSCI Europe applicando commissioni da gestione attiva. L'investitore potrebbe acquistare un ETF che replica lo stesso indice per $\approx 0{,}10\%$ e risparmiare oltre l'1% all'anno.
>
> **Il peso delle commissioni nel tempo.** Costo cumulato del closet indexing su 20 anni, con $100\,000 investiti.
>
> **Figura** — Grafico del valore del portafoglio ($) nel tempo (0–20 anni) con due serie: ETF (commissione 0,10%) e Closet Indexer (commissione 1,20%). La curva dell'ETF si stacca progressivamente al di sopra di quella del Closet Indexer, con un divario che si allarga nel tempo per effetto della capitalizzazione composta della differenza di commissione.
>
> Con un rendimento lordo di mercato del 7%: ETF → $379\,000 vs. Closet Indexer → $308\,000 dopo 20 anni. La differenza annua dell'1,1% nelle commissioni si capitalizza in una perdita di $71\,000 (19% del patrimonio finale) — senza alcuna competenza aggiuntiva da parte del gestore.

*(slide 22–23)*

## Come selezionare gli indici (fattori) per il benchmark di stile

Un buon portafoglio benchmark dovrebbe essere:
- un'alternativa praticabile;
- non facilmente battibile;
- a basso costo;
- identificabile a priori.

**Procedura pratica.** Si utilizza ciò che si sa sulla strategia del fondo per selezionare manualmente una serie di "soliti sospetti", per poi procedere in due modi alternativi:

1. Partire da un gran numero di indici e iterativamente escludere quelli statisticamente non significativi.
2. Partire da una lista breve di indici che rappresentano le principali classi di attività:
   - eliminare le classi di attività non significative;
   - sostituire gli indici rimanenti con sotto-indici;
   - ripetere l'analisi eliminando nuovamente i sotto-indici non significativi.

*(slide 24–25)*

## Analisi di stile e CAPM: il confronto Magellan (SML vs. sei indici di stile)

> [!example] Esempio
> L'analisi di stile fornisce una misura di performance **alternativa** rispetto a quella ottenuta con la SML del CAPM.
> - La SML utilizza un solo portafoglio, il portafoglio di mercato.
> - L'analisi di stile è libera di scegliere un numero arbitrario di indici diversi.
>
> **Esempio (BKM): Fidelity Magellan Fund, 1986–1991.**
> - $R^2$ della regressione SML pari a 0,99.
> - $R^2$ della regressione di stile pari a 0,975.
> - Alfa SML: 25 pb; alfa Stile: 32 pb.
>
> **Figura 24.4** — *Fidelity Magellan Fund cumulative return difference: Fund versus style benchmark and fund versus SML benchmark* (fonte: elaborazioni degli autori). Il grafico riporta i "Cumulative Residuals from Style Analysis" e i "Cumulative Residuals from SML" nel tempo (Oct-86 – Oct-91): entrambe le serie di residui cumulati crescono nel tempo, con la serie SML che tende a rimanere sopra quella dello stile verso la fine del periodo, coerentemente con l'alfa SML più alto.
>
> Nell'esempio del fondo Magellan, la SML era data da: Beta = 1,1, $R^2 = 99\% > 97{,}5\%$ dell'analisi di stile. Domanda aperta posta nel corso: come si può spiegare l'$R^2$ più elevato della regressione a singolo fattore (l'indice di mercato) rispetto alla regressione dell'analisi di stile che utilizza sei indici azionari?
>
> **Tabella di sintesi — due alfa da due benchmark:**
>
> | | SML (CAPM) | Analisi di Stile |
> |---|---|---|
> | Benchmark | Solo indice di mercato | 6 indici azionari di stile |
> | $\beta$ / pesi | $\beta = 1{,}1$ | vedi Tabella 24.4 (portafoglio di stile con $R^2=97{,}5$, riportato nella sezione dedicata al Magellan Fund) |
> | $R^2$ | 99,0% | 97,5% |
> | $\alpha$ (mensile) | 25 pb | 32 pb |
>
> **Perché gli alfa differiscono?** L'alfa è sempre misurato *rispetto a un benchmark*. Un benchmark diverso implica un alfa diverso. Il benchmark SML è il portafoglio di mercato; il benchmark di stile è una combinazione personalizzata di indici dimensionali/value/growth.
>
> **Quando usare quale?** Si usa l'alfa CAPM quando si ritiene che il portafoglio di mercato sia l'unico fattore di rischio rilevante; si usa l'alfa di stile quando si vuole tenere conto esplicitamente delle esposizioni dimensionali e value/growth del fondo.

*(slide 26–27)*

## Caso di studio: stima dei pesi di stile con il Risolutore di Excel

> [!abstract] Definizione
> Per calcolare i coefficienti di regressione nell'analisi di stile utilizzando il **Risolutore di Excel**:
>
> 1. Impostare valori iniziali arbitrari per i parametri $\alpha$ e i vari $\beta$.
> 2. Calcolare i residui della regressione come:
>
> $$e(t) = R(t) - \big[\alpha + \beta_1 R_1(t) + \beta_2 R_2(t) + \beta_3 R_3(t)\big]$$
>
> 3. Utilizzare il Risolutore per minimizzare la somma dei quadrati dei residui:
>
> $$\min \sum e(t)^2$$
>
> 4. Modificando $\alpha, \beta_1, \beta_2, \beta_3$ sotto i vincoli appropriati (non negatività e somma unitaria dei beta).

*(slide 29)*

## Esempio: analisi di stile di un fondo azionario europeo

> [!example] Esempio
> "**Eurozone Select Fund**" — analisi di stile con quattro indici MSCI su 36 mesi:
>
> | Indice di Stile | Peso |
> |---|---|
> | MSCI Europe Large Value | 38% |
> | MSCI Europe Large Growth | 27% |
> | MSCI Europe Small Cap | 22% |
> | Indice Obbl. Gov. Euro | 13% |
> | **Totale** | **100%** |
> | **$R^2$** | **94,2%** |
>
> **Figura** — Grafico a barre "Peso (%)" per le quattro categorie (LV, LG, SC, Obbl.): 38, 27, 22, 13.
>
> Nonostante sia etichettato come "fondo azionario Eurozona", l'analisi di stile rivela un'esposizione obbligazionaria effettiva del 13% — probabilmente dovuta a posizioni di liquidità o copertura. L'inclinazione verso il value (38% vs. 27% growth) conferma l'orientamento value dichiarato dal fondo.

*(slide 30)*

## Arbitrage Pricing Theory: premi al rischio stimati per i fattori

Premi al rischio stimati per l'esposizione ai fattori di rischio, periodo 1978–1990:

| Fattore | Premio al Rischio Stimato ($r_{\text{fattore}} - r_f$) |
|---|---|
| Spread di rendimento | 5,10% |
| Tasso di interesse | −0,61 |
| Tasso di cambio | −0,59 |
| PIL reale | 0,49 |
| Inflazione | −0,83 |
| Mercato | 6,36 |

*(slide 31)*

## Analisi di stile per hedge fund: dai fattori azionari ai fattori di Hasanhodzic e Lo

> [!example] Esempio
> **Regressione dei rendimenti CMP sui rendimenti S&P 500**, Gennaio 1926 – Dicembre 2004:
>
> $$y = 0{,}5476x + 0{,}0206, \qquad R^2 = 0{,}7027$$
>
> **Figura** — Scatterplot "Rendimento CMP" (asse y) contro "Rendimento S&P 500" (asse x), con la retta di regressione sovrapposta. I punti mostrano una relazione lineare positiva ma con dispersione, coerente con un $R^2$ di circa 0,70: il rendimento CMP è in parte spiegato dal mercato azionario, ma una quota rilevante di variabilità resta non spiegata.
>
> **Hasanhodzic e Lo:** coefficienti medi di regressione per regressioni lineari multivariate dei rendimenti mensili di hedge fund (database TASS Live, Feb 1986 – Set 2005) su sei fattori: S&P 500, Lehman Corporate AA Intermediate Bond Index, US Dollar Index, Credit Spread, DVIX e GSCI.
>
> **Principali risultati per strategia di hedge fund:**
> - **Convertible Arbitrage:** esposizione positiva a S&P 500 e obbligazioni.
> - **Dedicated Short Bias:** forte esposizione negativa a S&P 500.
> - **Equity Market Neutral:** bassa esposizione a tutti i fattori.
> - **Long/Short Equity:** esposizione positiva significativa a S&P 500.
> - **Managed Futures:** esposizione significativa alle materie prime, forte DVIX positivo.
> - **Emerging Markets:** alta esposizione a S&P 500 e materie prime.

*(slide 32–33)*

## Confronto di performance: hedge fund reali vs. cloni fattoriali

> [!example] Esempio
> **Cloni lineari a pesi fissi** (stimati sull'intero campione):
>
> | Strategia | Fondi (Sharpe Medio) | Cloni Lineari (Sharpe Medio) |
> |---|---|---|
> | Convertible Arbitrage | 2,70 | 1,52 |
> | Dedicated Short Bias | 0,32 | 0,25 |
> | Emerging Markets | 0,88 | 1,42 |
> | Equity Market Neutral | 1,42 | 1,44 |
> | Event Driven | 1,99 | 1,43 |
> | Fixed Income Arbitrage | 2,05 | 1,48 |
> | Global Macro | 1,07 | 1,41 |
> | Long/Short Equity | 0,98 | 1,06 |
> | Managed Futures | 0,67 | 1,36 |
> | Multi-Strategy | 1,86 | 1,51 |
> | Fund of Funds | 1,59 | 1,66 |
> | Tutti escluso FoF | 1,39 | 1,19 |
>
> **Cloni a finestra mobile di 24 mesi** (senza guardare avanti nei dati):
>
> | Strategia | Fondi (Sharpe Medio) | Cloni Rolling (Sharpe Medio) |
> |---|---|---|
> | Convertible Arbitrage | 2,31 | 0,71 |
> | Dedicated Short Bias | 0,09 | 0,02 |
> | Emerging Markets | 1,74 | 0,47 |
> | Equity Market Neutral | 1,44 | 0,64 |
> | Event Driven | 2,01 | 1,05 |
> | Fixed Income Arbitrage | 2,17 | 0,84 |
> | Global Macro | 1,08 | 0,91 |
> | Long/Short Equity | 1,04 | 0,76 |
> | Managed Futures | 0,66 | 0,91 |
> | Multi-Strategy | 1,86 | 0,71 |
> | Fund of Funds | 1,67 | 1,11 |
> | Tutti escluso FoF | 1,38 | 0,79 |
>
> Si noti il pattern opposto tra le due tabelle: con i pesi fissi i cloni spesso *superano* i fondi (es. Emerging Markets 1,42 vs. 0,88), mentre con la finestra mobile i fondi *superano* nettamente i cloni in quasi tutte le strategie (es. Convertible Arbitrage 2,31 vs. 0,71).

*(slide 34–35)*

## Perché i cloni a pesi fissi sovraperformano? Discussione e risultati cumulati

Il risultato sorprendente è che i cloni a pesi fissi spesso battono gli hedge fund reali. Le ragioni:

1. **Nessun peso delle commissioni 2-and-20.** Gli hedge fund applicano $\sim 2\%$ di commissione di gestione più 20% di commissione di performance. I cloni costruiti con prodotti indicizzati a basso costo pagano $\sim 0{,}1$–$0{,}3\%$.
2. **Bias di look-ahead.** I cloni a pesi fissi usano coefficienti di regressione stimati sull'intero campione, cioè *dopo* aver visto i dati. I cloni a finestra mobile (che non hanno questo bias) performano molto peggio.
3. **Bias di sopravvivenza nei premi fattoriali.** I fattori di stile (azionario, credit spread, ecc.) hanno guadagnato premi positivi nel campione osservato. Un'esposizione statica a questi premi si capitalizza in modo potente.
4. **Nessun vincolo di capacità.** Gli hedge fund reali affrontano vincoli di liquidità e costi di impatto sul mercato. I cloni fattoriali scalano liberamente.

**Conclusione:** il confronto a finestra mobile è il test corretto. Lì, i fondi sovraperformano i loro cloni, fornendo evidenza di un'abilità genuina (ma modesta) del gestore.

**Rendimento cumulato: Fondi vs. Cloni vs. S&P 500 (Feb 1986 – Dic 2004).**

*Cloni lineari a pesi fissi:*
- i cloni lineari (a pesi fissi) hanno significativamente sovraperformato sia i fondi che l'S&P 500;
- valori terminali: Cloni $\approx 50\times$, Fondi $\approx 18\times$, S&P 500 $\approx 10\times$;
- ma questo risultato include il bias di look-ahead (pesi stimati sull'intero campione).

*Cloni a finestra mobile di 24 mesi:*
- valori terminali: Fondi $\approx 10\times$, S&P 500 $\approx 6\times$, Cloni Rolling $\approx 5\times$;
- i fondi sovraperformano i loro cloni rolling $\Rightarrow$ evidenza di alfa genuino;
- i cloni rolling sottoperformano quelli a pesi fissi $\Rightarrow$ conferma il bias di look-ahead.

*(slide 36–37)*

## Origine della sovraperformance dei fondi "clone/tracking"

I risultati di Hasanhodzic e Lo (2007) mostrano che anche gli hedge fund possono essere replicati.

**Domanda:** qual è l'origine della sovraperformance dei fondi "clone/tracking"?

1. **Reverse engineering** delle strategie di trading degli hedge fund.
2. **Identificazione dei fattori di rischio** che generano questi rendimenti (tail risk, rischio di liquidità, rischio di credito).

Costruendo portafogli esposti agli stessi tipi di rischio, è possibile guadagnare i premi al rischio associati in modo trasparente, scalabile e a basso costo. In questo senso, l'**alfa viene trasformato in beta**.

Il principale vantaggio è che questi tipi di rischio sono scarsamente correlati con quelli tradizionali (es. il rischio di mercato azionario).

*(slide 38)*

## Valutazione critica: limiti dell'analisi di stile

1. **Multicollinearità.** Gli indici di stile sono spesso altamente correlati (es. large value e large growth si muovono entrambi con il mercato ampio). Ciò rende le stime dei singoli $\beta_i$ instabili anche quando l'$R^2$ è elevato.
2. **Bias del vincolo di non vendita allo scoperto.** Se la vera esposizione del fondo è negativa (es. short sulle obbligazioni), il vincolo $\beta_i \ge 0$ forza il peso a zero e distorce tutti gli altri pesi. L'$R^2$ diminuisce (come nel Trustees' Fund: 95,2% non vincolato → 92,2% vincolato).
3. **Sensibilità alla scelta degli indici.** Sostituire "Large Value" con "S&P 500 Value" vs. "Russell 1000 Value" può cambiare materialmente i pesi di stile.
4. **Ipotesi di stile costante.** La regressione sull'intero campione assume che il fondo abbia mantenuto lo stesso stile durante tutto il periodo. I gestori attivi modificano la loro allocazione, violando questa ipotesi.
5. **Trade-off sulla lunghezza della finestra.** Finestre brevi danno stime rumorose; finestre lunghe mascherano la deriva di stile. Non esiste una lunghezza di finestra universalmente ottimale.

*(slide 39)*

## Sintesi: il kit di strumenti per la valutazione della performance

Confronto tra gli strumenti visti nella Sessione 2.3 (misure di performance risk-adjusted) e quelli della Sessione 2.4 (analisi di stile):

| Dalla Sessione 2.3 | Dalla Sessione 2.4 | Collegamento |
|---|---|---|
| Indice di Sharpe | $R^2$ di stile | Entrambi misurano il rischio totale; l'$R^2$ lo scompone |
| Alfa di Jensen (CAPM) | Alfa di stile | Benchmark diversi $\Rightarrow$ alfa diversi |
| Information Ratio | Tracking error dall'analisi di stile | $IR = \alpha/\sigma(e)$; l'analisi di stile fornisce $\sigma(e)$ |
| Treynor-Mazuy market timing | Analisi di stile a finestra mobile | Entrambi rilevano comportamenti variabili nel tempo del gestore |
| Active Share (Cremers & Petajisto) | Pesi di stile | Alto $R^2$ + basso Active Share = closet indexer |

L'analisi di stile **non sostituisce** le misure della Sessione 2.3: è un **complemento** che risponde a una domanda diversa: *da dove provengono i rendimenti del fondo?*

*(slide 40–41)*
