---
title: "Hedge Fund"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M2-06_Hedge-funds.pdf"
pages: 50
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione e panoramica del capitolo

Corso: **Financial Economics (EM5021)** — modulo su **Hedge Fund**, Loriana Pelizzon, Università Ca' Foscari Venezia.

Argomenti trattati nel capitolo:

- Hedge fund vs. fondi comuni
- Strategie degli hedge fund
- Alfa portabile e pure play
- Misurazione della performance degli hedge fund
- Esposizione a fattori di rischio omessi
- Struttura commissionale degli hedge fund
- High water mark
- Fondi di fondi

*(slide 1–2)*

## Hedge fund versus fondi comuni

Confronto strutturale tra hedge fund e fondi comuni di investimento su cinque dimensioni:

| Caratteristica | Hedge Fund | Fondo Comune |
|---|---|---|
| **Trasparenza** | Società in accomandita con comunicazione minima della strategia e della composizione del portafoglio | La regolamentazione richiede la comunicazione pubblica della strategia e della composizione del portafoglio |
| **Investitori** | Non più di 100 investitori "sofisticati" e facoltosi | Il numero non è limitato |
| **Strategie di investimento** | Molto flessibili, i fondi possono agire in modo opportunistico; effettuano un'ampia gamma di investimenti | Prevedibili, strategie stabili, dichiarate nel prospetto |
| **Uso di leva/short/opzioni** | Uso frequente di vendite allo scoperto, leva finanziaria, opzioni | Uso limitato di vendite allo scoperto, leva finanziaria, opzioni |
| **Liquidità** | Hanno periodi di lock-up, richiedono preavviso per il riscatto | Gli investimenti possono essere spostati più facilmente dentro e fuori dal fondo |
| **Struttura commissionale** | Commissione di gestione dell'1–2% del patrimonio e commissione di incentivo del 20% dei profitti | Le commissioni sono generalmente una percentuale fissa del patrimonio, tipicamente dallo 0,5% all'1,25% |

*(slide 3–5)*

## Evidenza empirica: dimensione dell'industria degli hedge fund

**Figura** — Grafico a barre dell'AUM (asset under management) globale degli hedge fund in trilioni di USD per anno:

| Anno | AUM (trilioni USD) |
|---|---|
| 2000 | 0,49 |
| 2005 | 1,11 |
| 2007 | 1,87 |
| 2010 | 1,92 |
| 2015 | 2,97 |
| 2020 | 3,6 |
| 2023 | 4,3 |
| 2025 (Q3) | 4,98 |

Il grafico mostra una crescita pressoché monotona dell'AUM del settore dal 2000 al 2025.

Punti chiave:

- Crescita da $0,5 trilioni (2000) a $4,98 trilioni (Q3 2025)
- Oltre 30.000 fondi registrati alle Cayman (75%+ del mercato offshore)
- La crescita nel 2024–25 è stata guidata da profitti (P&L), non da nuovi afflussi
- Fonte: BarclayHedge, CIMA, HFR (2025)

*(slide 6)*

## Strategie degli hedge fund: direzionali, non direzionali e stili

Le strategie degli hedge fund si dividono in due macro-categorie:

- **Direzionali**: scommesse sul fatto che un settore sovraperformerà rispetto ad altri settori
- **Non direzionali**: sfruttano disallineamenti temporanei nelle valutazioni relative tra settori; acquistano un tipo di titolo e ne vendono un altro; mirano ad essere *market neutral*

**Stili direzionali e macro**

| Stile | Descrizione | Profilo tipico |
|---|---|---|
| Dedicated short bias | Posizione netta corta, generalmente in azioni. | Alto \|β\|, negativo |
| Emerging markets | Sfrutta inefficienze nei mercati emergenti. Tipicamente solo long. | β elevato, alta volatilità |
| Global macro | Posizioni lunghe e corte su mercati dei capitali e derivati a livello mondiale, basate su visioni macroeconomiche. | β variabile |
| Long/short equity | Posizioni lunghe e corte su azioni a seconda delle prospettive. Non market neutral. | β moderatamente positivo |
| Managed futures | Utilizza futures finanziari, valutari o sulle materie prime. Approccio tecnico o discrezionale. | Bassa correlazione col mercato |

Caratteristica comune: queste strategie hanno un'esposizione netta significativa alla direzione del mercato o di un fattore macro.

**Stili di arbitraggio e relative value**

| Stile | Descrizione | Profilo tipico |
|---|---|---|
| Convertible arbitrage | Investimento con copertura in titoli convertibili: long convertibili, short azioni. | β ≈ 0, leva alta |
| Equity market neutral | Coperture long/short controllando esposizioni settoriali/dimensionali. Market-neutral con leva. | β ≈ 0 |
| Event driven | Profitto da fusioni, acquisizioni, ristrutturazioni, fallimenti. | β moderato |
| Fixed-income arbitrage | Anomalie di prezzo in titoli a reddito fisso correlati: swap, yield curve, MBS. | β ≈ 0, tail risk |
| Multistrategy | Scelta opportunistica della strategia. | Variabile |
| Fund of funds | Alloca liquidità a diversi hedge fund. | Diversificato |

Caratteristica comune: queste strategie cercano di essere market-neutral, ma sono spesso esposte a rischio di coda (tail risk) e rischio di liquidità.

*(slide 7–9)*

## Arbitraggio statistico

> [!abstract] Definizione
> **Arbitraggio Statistico**
>
> - Sistemi quantitativi che cercano numerosi disallineamenti temporanei e modesti nei prezzi
> - Operano su centinaia di titoli al giorno con brevi periodi di detenzione
> - **Pairs trading**: accoppiare società simili con rendimenti altamente correlati dove una è prezzata in modo più aggressivo
> - **Data mining**: scopre pattern sistematici nei prezzi
>
> **Esempio intuitivo**: Coca-Cola e Pepsi si muovono storicamente insieme. Se Coca-Cola scende del 3% e Pepsi rimane stabile senza notizie rilevanti, il pairs trader compra Coca-Cola e vende Pepsi, scommettendo sulla convergenza.

*(slide 10)*

## Evidenza empirica: evoluzione dei rendimenti per decennio

I rendimenti medi degli hedge fund sono cambiati drasticamente nel tempo:

| Periodo | HF Composito | S&P 500 | Vol. HF | Vol. S&P | Sharpe HF |
|---|---|---|---|---|---|
| Anni '90 (1990–1999) | 15–20% | 18,2% | 7–10% | 14,5% | > 1,0 |
| Anni 2000 (2000–2009) | 6–8% | −0,9% | 7,5% | 16,0% | 0,55 |
| Anni 2010 (2010–2019) | 4–6% | 13,6% | 5,5% | 13,5% | 0,40 |
| Anni 2020 (2020–2025) | 7–10% | 14,8% | 6,0% | 17,5% | 0,70 |

- **Anni '90**: "Età d'oro" — pochi fondi, mercati meno efficienti, alfa abbondante
- **Anni 2000**: gli HF sovraperformano l'S&P 500 grazie alla protezione durante dot-com (2000–02) e GFC (2008)
- **Anni 2010**: delusione — il bull market azionario rende difficile battere l'indice; alfa compresso
- **Anni 2020**: ripresa — volatilità e dispersione favoriscono i gestori attivi

Fonti: HFRI FWC, Bloomberg. Rendimenti annualizzati, al netto delle commissioni.

**Figura — Le Tre Ere dei Rendimenti degli Hedge Fund**: grafico a barre affiancate che confronta il rendimento medio annualizzato (%) di HFRI Composito e S&P 500 nei quattro sotto-periodi (Anni '90, Anni 2000, Anni 2010, 2020–2025), accompagnato dalla tabella seguente:

| | Anni '90 | Anni 2000 | Anni 2010 | 2020–2025 |
|---|---|---|---|---|
| Contesto | Pochi fondi, mercati inefficienti | Dot-com, GFC, volatilità alta | QE, tassi zero, bassa volatilità | COVID, inflazione, geopolitica |
| HF vs. S&P | ≈ pari | HF molto superiori | HF molto inferiori | HF inferiori ma più stabili |
| N. fondi | ∼2.000 | ∼10.000 | ∼15.000 | ∼30.000 |

Il grafico conferma visivamente il pattern della tabella dei rendimenti per decennio: HF e S&P sostanzialmente allineati negli anni '90, ampio vantaggio HF negli anni 2000, vantaggio S&P negli anni 2010, e HF più stabili (anche se inferiori in media) nel 2020–2025. Fonti: HFRI 1990–2025, S&P 500 total return, HFR, Bloomberg.

*(slide 11–12)*

## Evidenza empirica: rendimenti anno per anno e vincitori per regime di mercato

**Rendimenti anno per anno (2018–2025, in %)**

| | '18 | '19 | '20 | '21 | '22 | '23 | '24 | '25 |
|---|---|---|---|---|---|---|---|---|
| HFRI Composito | −4,1 | +10,4 | +11,8 | +10,3 | −4,3 | +7,5 | +10,4 | +12,6 |
| Equity Hedge | −6,9 | +13,7 | +17,5 | +12,4 | −10,2 | +11,4 | +12,5 | +17,3 |
| Event Driven | −2,0 | +7,5 | +9,3 | +12,0 | −4,3 | +10,4 | +9,5 | +11,0 |
| Macro | −4,1 | +8,2 | +5,2 | +8,0 | +9,3 | −0,3 | +6,5 | +9,9 |
| Multi-Strategy | +1,2 | +7,8 | +6,3 | +6,3 | −1,5 | +6,3 | +13,6 | +10,5 |
| S&P 500 | −4,4 | +31,5 | +18,4 | +28,7 | −18,1 | +26,3 | +25,0 | +23,3 |

**Figura** — grafico a barre affiancate del rendimento annuo (%) di HFRI Composito vs. S&P 500 dal 2018 al 2025, che visualizza la tabella precedente.

**Lezione chiave**: nel 2022 gli HF perdono solo −4,3% vs. −18,1% dell'S&P. L'S&P batte gli HF nei rialzi, ma gli HF proteggono nei ribassi. Il 2025 segna la migliore performance HFRI dal 2009.

**Le strategie vincenti cambiano con il regime di mercato**

| Regime | Strategie vincenti | Strategie perdenti | Perché |
|---|---|---|---|
| Rialzo prolungato (2019, 2021, 2023–25) | Long/Short Equity, Event Driven | Ded. Short Bias, Macro | Beta positivo premia; shorting distrugge valore |
| Ribasso/Crisi (2008, 2022) | Macro, Managed Futures, Short Bias | L/S Equity, Emerging Mkts | Trend-following e coperture pagano; leva amplifica perdite |
| Alta volatilità (2020, Q1 2025) | Multi-Strategy, Macro | Mkt Neutral, FI Arb | Dispersione crea opportunità; strategie di carry soffrono |
| Tassi in rialzo (2022–23) | Macro, CTA | Fixed Income Arb, Convert. Arb | Duration penalizza; trend FX/tassi premia |

**Implicazione per l'investitore**: non esiste una strategia "sempre vincente". La diversificazione tra stili HF è essenziale, e la scelta del timing di allocazione richiede una visione sul regime macroeconomico atteso.

*(slide 13–14)*

## Evidenza empirica: performance per strategia nel lungo periodo (1994–2025)

| Strategia | Rend. Medio Ann. (1994–2025) | Volatilità Ann. | Sharpe Ratio |
|---|---|---|---|
| Equity Market Neutral | 5,3% | 3,8% | 0,66 |
| Long/Short Equity | 9,5% | 9,5% | 0,65 |
| Global Macro | 8,5% | 7,2% | 0,72 |
| Event Driven | 9,0% | 6,8% | 0,85 |
| Managed Futures | 5,8% | 11,2% | 0,30 |
| Multi-Strategy | 7,5% | 4,0% | 1,10 |
| Emerging Markets | 7,4% | 14,1% | 0,35 |
| S&P 500 | 10,5% | 15,2% | 0,48 |
| 60/40 Equity/Bond | 7,2% | 9,8% | 0,44 |

**Osservazioni chiave**:

- Molte strategie HF offrono Sharpe ratio superiori all'S&P 500 e al 60/40, pur con rendimenti assoluti inferiori
- Il multi-strategy ha lo Sharpe più alto (≈ 1,1) grazie alla bassa volatilità — coerente con il dato Aurum (5y CAR +10,5%, Sharpe 2,1)
- L'S&P 500 ha il rendimento più alto ma anche la volatilità più alta (15,2%)

Fonti: HFRI, Aurum Hedge Fund Data Engine, Bloomberg.

*(slide 15)*

## Le Isole Cayman e la domiciliazione offshore

> [!example] Esempio
> Le Isole Cayman sono il principale centro offshore per gli hedge fund.
>
> | Dato | Valore |
> |---|---|
> | Fondi registrati | >30.000 |
> | Quota HF globali | ≈ 75% offshore |
> | % net assets (SEC) | 53,6% |
> | AUM settore (Q3 '25) | $4,98 trilioni |
> | Imposte dirette | Zero |
>
> **Perché le Cayman?**
>
> - **Neutralità fiscale**: nessuna imposta su redditi, capital gain, ritenute alla fonte
> - **Struttura master-feeder**: investitori USA e non-USA confluiscono in un unico fondo "master" offshore
> - **Infrastruttura**: studi legali, revisori, amministratori specializzati
> - **Flessibilità regolamentare** con standard riconosciuti da investitori istituzionali
>
> **Attenzione**: i gestori operano a New York, Londra, Hong Kong — le Cayman sono solo il veicolo giuridico. I rendimenti lordi sono identici a quelli di un fondo onshore con la stessa strategia. Il vantaggio è nei rendimenti netti.
>
> **Dove vanno i rendimenti lordi? (esempio con lordo 12%)**
>
> Verifica (somma = 12%):
>
> | Componente | Cayman | Onshore |
> |---|---|---|
> | Netto investitore | 7,2% | 5,4% |
> | Commissioni 2+20 | 4,4% | 4,4% |
> | Tasse fondo | 0,0% | 1,8% |
> | Altro | 0,4% | 0,4% |
> | **Totale lordo** | **12,0%** | **12,0%** |
>
> Differenza netto investitore Cayman vs. Onshore: Δ = 1,8% annuo.
>
> Impatto cumulato su 20 anni (investimento iniziale $1M):
>
> | Scenario | Valore dopo 20 anni |
> |---|---|
> | Cayman (7,2% netto) | $401.000 |
> | Onshore (5,4% netto) | $287.000 |
> | **Gap** | **$114.000** |
>
> *Ipotesi: onshore con 15% di tassazione effettiva sui redditi del fondo. Il gap annuo dell'1,8% si compone su 20 anni ⇒ >75% dei fondi globali sceglie le Cayman.*

*(slide 16–17)*

## Alfa portabile: l'idea

> [!abstract] Definizione
> L'alfa portabile è una tecnica in tre passi:
>
> 1. Trovare alfa in un settore A (tramite futures/swap)
> 2. Coprire il rischio sistematico di A (tramite ETF/indice)
> 3. Aggiungere esposizione passiva al settore B
>
> **Risultato**: trasferite l'alfa dal settore dove lo trovate alla classe di attività in cui volete essere esposti.
>
> **Perché è utile?** Un gestore può essere bravo a selezionare titoli del settore tecnologico (alfa > 0), ma il cliente vuole esposizione all'obbligazionario. Con l'alfa portabile, il gestore investe in tech, copre il beta di mercato, e poi usa futures obbligazionari per dare al cliente l'esposizione desiderata.

*(slide 18)*

## Alfa portabile: esempio numerico completo (pure play)

> [!example] Esempio
> **Dati del portafoglio** (valore $2,1 milioni):
>
> | Parametro | Valore |
> |---|---|
> | Valore del portafoglio | $2.100.000 |
> | Beta (β) | 1,2 |
> | Alfa (α) mensile | 2% |
> | Tasso privo di rischio (r_f) mensile | 1% |
> | S&P 500 (S₀) | 2.016 punti |
> | Moltiplicatore S&P 500 | $50 per punto |
>
> **Situazione**: si ritiene che alfa > 0 (il portafoglio è sottovalutato), ma si prevede un ribasso del mercato (r_M < 0). Si vuole catturare l'alfa eliminando il beta.
>
> Il rendimento del portafoglio è:
> $$r_{\text{portafoglio}} = r_f + \beta(r_M - r_f) + \alpha + e$$
>
> **Passo 1 — Calcolo della copertura**: numero di contratti futures da vendere.
>
> La formula del rapporto di copertura:
> $$N = \frac{\text{Valore portafoglio}}{\text{Valore di un contratto futures}} \times \beta = \frac{\$2.100.000}{2.016 \times \$50} \times 1,2$$
> $$N = \frac{\$2.100.000}{\$100.800} \times 1,2 = 20,83 \times 1,2 = 25 \text{ contratti}$$
>
> *Intuizione*: se β = 1,0, basterebbe coprire il valore di mercato del portafoglio (circa 21 contratti). Ma poiché β = 1,2, il portafoglio è più sensibile del mercato, quindi servono il 20% di contratti in più ⇒ 25.
>
> **Azione**: vendete 25 contratti futures sull'S&P 500.
>
> **Passo 2 — Valore del portafoglio dopo 1 mese** (prima della copertura):
> $$\$2.100.000(1+r_p) = \$2.100.000\left[1 + \underbrace{0,01}_{r_f} + 1,2\,(r_m - 0,01) + \underbrace{0,02}_{\alpha} + e\right]$$
> $$= \underbrace{\$2.137.800}_{\text{parte certa}} + \underbrace{\$2.520.000 \times r_m}_{\text{parte legata al mercato}} + \$2.100.000 \times e$$
>
> **Passo 3 — Proventi dalla posizione in futures** (mark-to-market):
> $$25 \times \$50 \times (F_0 - F_1) = \$1.250 \times [S_0(1,01) - S_1]$$
> $$= \$1.250 \times S_0[1,01 - (1+r_M)] \quad (\text{poiché } S_1 = S_0(1+r_M))$$
> $$= \$25.200 - \$2.520.000 \times r_M$$
>
> **Passo 4 — Somma portafoglio + futures**:
> $$\text{Proventi totali} = (\$2.137.800 + \$2.520.000 \cdot r_m) + (\$25.200 - \$2.520.000 \cdot r_M) + \$2.100.000 \cdot e$$
> $$= \$2.163.000 + \$2.100.000 \cdot e$$
>
> I termini in $r_M$ si cancellano perfettamente ⇒ **Beta = 0**.
>
> Il rendimento mensile coperto:
> $$r_{\text{coperto}} = \frac{\$2.163.000}{\$2.100.000} - 1 = 3\% \quad (= r_f + \alpha = 1\% + 2\%)$$
>
> **Conclusione**: avete isolato l'alfa (2%) e guadagnate il tasso privo di rischio (1%) + alfa, indipendentemente da cosa fa il mercato.
>
> **Verifica numerica — due scenari a confronto**
>
> | | Mercato +5% | Mercato −5% |
> |---|---|---|
> | **Portafoglio (senza copertura)**: r_p = 0,01 + 1,2(r_m − 0,01) + 0,02 | 5,8% | −4,2% |
> | Valore portafoglio | $2.221.800 | $2.011.800 |
> | **Profitto/perdita futures** (25 contratti): $25.200 − $2.520.000 × r_M | −$100.800 | +$151.200 |
> | **Totale coperto** | $2.121.000* | $2.163.000* |
> | **Rendimento coperto** | ≈ 3% | ≈ 3% |
>
> *La piccola differenza dipende dal termine residuo e; a meno di e, il rendimento è esattamente r_f + α = 3% in entrambi i casi.*
>
> Il mercato sale ⇒ il portafoglio guadagna di più, ma i futures perdono. Il mercato scende ⇒ il portafoglio perde, ma i futures compensano. In entrambi i casi: rendimento ≈ 3%.
>
> **Figura 26.1 — Un Pure Play**. Pannello A: rette "Return on Positive Alpha Portfolio" e "Return for Fairly Priced Assets" nel piano Excess Rate of Return vs. Excess Market Return, con gap costante pari all'alfa (2%). Pannello B: dopo la copertura del beta, la linea caratteristica del portafoglio coperto è piatta a un rendimento del 3% (r_f = 1% + α = 2%), indipendentemente dal rendimento di mercato. La figura illustra visivamente che la copertura del beta isola l'alfa in un rendimento costante, mentre senza copertura il rendimento resta legato linearmente al mercato.

*(slide 19–24)*

## Analisi di stile per hedge fund

Esposizioni fattoriali tipiche riscontrate nell'analisi di stile:

- **I fondi equity market-neutral**: hanno beta bassi e non significativi
- **I fondi dedicated short bias**: hanno beta negativi sostanziali rispetto all'indice S&P
- **I fondi su imprese in difficoltà (distressed)**: hanno un'esposizione significativa alle condizioni del credito
- **I fondi global macro**: mostrano un'esposizione negativa a un dollaro USA più forte

*(slide 25)*

## Misurazione della performance degli hedge fund

**Stime standard del modello a indice** (periodo ottobre 2011 – settembre 2016, S&P 500 come benchmark di mercato):

- Risultati di performance inferiori alla media
- L'alfa medio era leggermente negativo
- L'indice di Sharpe medio era inferiore a quello dell'S&P 500

**Contestualizzazione storica**:

- In periodi precedenti (in particolare prima del 2010) gli hedge fund hanno generalmente sovraperformato in modo sostanziale gli indici passivi
- Nel periodo 2010–2019, i rendimenti sono stati deludenti rispetto al bull market azionario
- Dal 2020, i rendimenti sono migliorati: il 2025 ha registrato la migliore performance HFRI dal 2009 (+12,6%), trainata da equity hedge (+17,3%) e event driven (+11,0%)
- Indipendentemente da questa variabilità nei risultati, diversi fattori rendono difficile la valutazione della performance degli hedge fund

*(slide 26–27)*

## Evidenza empirica: ascesa, declino e ripresa dell'alfa

**Figura — Alfa annualizzato (%) per sotto-periodo (95-00, 00-05, 05-10, 10-15, 15-20, 20-25)**: grafico a barre che mostra l'evoluzione dell'alfa medio stimato rispetto a modelli multifattoriali lungo tre fasi distinte, descritte di seguito. Il pattern complessivo del grafico è quello di un alfa elevato negli anni '90/inizio 2000, una progressiva compressione fino al 2020, e una lieve ripresa nel periodo più recente.

**Tre fasi distinte**:

1. **1990–2005 (Età d'oro)**: pochi fondi, mercati inefficienti ⇒ alfa elevato
2. **2005–2020 (Compressione)**: affollamento, maggiore efficienza, commissioni elevate, tassi zero
3. **2020–2025 (Ripresa)**: volatilità da COVID/inflazione/geopolitica; dispersione settoriale favorisce i gestori attivi; HFRI +12,6% nel 2025

Fonti: Fung et al. (2008), Berk & Green (2004), HFRI (2025). Alfa stimato vs. modelli multifattoriali.

*(slide 28)*

## Evidenza empirica: dispersione dei rendimenti top vs. bottom

**Figura — Rendimento annuo (%) 2019–2024**: grafico a barre che confronta, per ciascun anno, il rendimento del decile superiore (top decile), dell'HFRI Composito e del decile inferiore (bottom decile) dei fondi. Il grafico mostra visivamente che la media (HFRI Composito) nasconde una dispersione enorme tra fondi individuali.

- La dispersione top/bottom nel 2023 era di oltre 51 punti percentuali
- Circa il 20% dei fondi ha registrato rendimenti negativi anche in anni positivi per la media
- **Implicazione**: la selezione del gestore è più importante della scelta della strategia

Fonte: HFR, HFRI FWC performance dispersion data (2019–2024).

*(slide 29)*

## Liquidità e performance: attività illiquide e correlazione seriale

> [!example] Esempio
> **Perché gli hedge fund detengono attività illiquide?**
>
> - Gli hedge fund tendono a detenere attività più illiquide rispetto ad altri investitori istituzionali
> - **Aragon**: l'alfa tipico potrebbe essere un premio per la liquidità di equilibrio piuttosto che abilità nella selezione
> - **Hasanhodzic e Lo**: i rendimenti degli hedge fund presentano correlazione seriale → indizio di problemi di liquidità
>
> **Esempio: perché l'illiquidità genera correlazione seriale**
>
> Immaginate un fondo che detiene un immobile commerciale:
>
> | | Gen | Feb | Mar | Apr | Mag |
> |---|---|---|---|---|---|
> | Valore "vero" | 100 | 95 | 90 | 92 | 94 |
> | Valore riportato (stima) | 100 | 98 | 94 | 91 | 93 |
> | Rendimento riportato | – | −2% | −4% | −3% | +2% |
>
> - L'immobile non è quotato in borsa ⇒ il suo valore viene stimato ("marked to model"), non osservato sul mercato
> - La stima si aggiorna con ritardo: il calo reale di gennaio si manifesta nei rendimenti riportati di febbraio e marzo
> - Questo smoothing crea correlazione seriale positiva nei rendimenti riportati
>
> **Conseguenza**: la volatilità riportata è sottostimata ⇒ l'indice di Sharpe risulta gonfiato ⇒ il fondo sembra migliore di quanto sia realmente.
>
> **Figura 26.2 — Hedge Fund con Maggiore Correlazione Seriale nei Rendimenti**: due scatterplot con retta di regressione, uno di Alfa vs. Correlazione Seriale dei rendimenti e uno di Sharpe Ratio vs. Correlazione Seriale dei rendimenti, entrambi con relazione positiva. La figura mostra che i fondi con maggiore correlazione seriale (proxy di illiquidità/smoothing) tendono a riportare alfa e Sharpe ratio più elevati, confermando che parte della performance misurata è un artefatto della valutazione ritardata di attività illiquide.

*(slide 30–32)*

## Liquidità e performance: effetto Santa e rischio di liquidità sistematico

- **Sadka**: cali inattesi della liquidità di mercato sono un importante determinante dei rendimenti medi degli hedge fund
- **Effetto Santa**: gli hedge fund riportano rendimenti medi a dicembre sostanzialmente superiori rispetto agli altri mesi
- Il picco dei rendimenti di dicembre è più marcato per i fondi a minore liquidità, suggerendo che le attività illiquide vengono valutate in modo più generoso a dicembre

**Interpretazione**: a dicembre, i gestori hanno un incentivo a "rivalutare al rialzo" le posizioni illiquide per migliorare la performance annuale e massimizzare le commissioni di incentivo.

**Figura 26.3 — Rendimenti Medi degli Hedge Fund in Funzione del Rischio di Liquidità**: scatterplot di Average Excess Return (%/mese) contro Liquidity Beta, con retta di regressione a pendenza positiva. Il grafico mostra che i fondi con maggiore sensibilità (beta) a shock sistematici di liquidità di mercato ottengono in media rendimenti in eccesso più elevati, coerente con l'esistenza di un premio per il rischio di liquidità.

*(slide 33–34)*

## Bias di sopravvivenza e backfill bias

**Backfill bias**:

- Gli hedge fund comunicano i rendimenti solo se scelgono di farlo
- Possono farlo solo quando la performance passata è stata positiva

**Bias di sopravvivenza**:

- I fondi falliti escono dal database
- I tassi di uscita degli hedge fund sono più del doppio rispetto a quelli dei fondi comuni

**Evidenza empirica: quanto pesano i bias?**

| Tipo di bias | Stima dell'impatto | Fonte |
|---|---|---|
| Bias di sopravvivenza | +2,0–3,6% annuo | Malkiel & Saha (2005) |
| Backfill bias | +1,4% annuo | Fung & Hsieh (2009) |
| Bias combinato | +3,0–5,0% annuo | Aggarwal & Jorion (2010) |
| Tasso di chiusura annuo (vs. fondi comuni: ∼3–4%) | ∼8–10% | BarclayHedge |

**Implicazione**: se l'alfa medio riportato dai database è circa +2% annuo, e i bias combinati valgono +3–5%, allora l'alfa corretto è probabilmente negativo per il fondo medio.

Questo non significa che nessun fondo generi alfa, ma che la media del settore è molto inferiore a quanto i dati grezzi suggeriscano.

*(slide 35–36)*

## Esposizioni variabili ai fattori e market timing come opzione call

> [!tip] Teorema
> Gli hedge fund sono opportunistici e possono modificare frequentemente i loro profili di rischio. Se il rischio non è costante, gli alfa saranno distorti nel modello a indice lineare standard.
>
> **Conclusioni**:
>
> - Market timing perfetto → linea caratteristica non lineare e quindi maggiore sensibilità al mercato rialzista
> - I fondi che vendono opzioni hanno maggiore sensibilità al mercato quando questo scende rispetto a quando sale
> - Linee caratteristiche non lineari suggeriscono che molti hedge fund sono implicitamente venditori di opzioni
>
> **Esempio: market timing perfetto = payoff di un'opzione call**
>
> Un market timer perfetto sceglie ogni mese tra azioni e titoli risk-free:
>
> | Scenario | r_M | r_f | Rendimento del Timer |
> |---|---|---|---|
> | Mercato in forte rialzo | +8% | 1% | max(8%, 1%) = +8% |
> | Mercato in lieve rialzo | +2% | 1% | max(2%, 1%) = +2% |
> | Mercato in ribasso | −5% | 1% | max(−5%, 1%) = +1% |
> | Mercato in forte ribasso | −12% | 1% | max(−12%, 1%) = +1% |
>
> Il rendimento del timer è:
> $$r_{\text{timer}} = \max(r_M, r_f) = r_f + \max(r_M - r_f, 0)$$
>
> Questo è esattamente il payoff di una posizione in T-Bill + opzione call sul mercato con prezzo di esercizio = r_f. La linea caratteristica è **piatta a sinistra** (non perde mai più di r_f) e **crescente a destra** (cattura i rialzi).
>
> **Figura 26.4 — Linea Caratteristica di un Market Timer Perfetto**: grafico di Portfolio Return vs. Market Return con una linea spezzata "Return to Perfect Market Timer" (piatta a r_f a sinistra, crescente con pendenza 1 a destra, come una call) confrontata con una "Fitted Regression Line" tratteggiata. La vera linea caratteristica presenta un punto angoloso (come una call). Adattare una retta porterà a una stima errata: l'alfa è sovrastimato e il beta è sottostimato.
>
> **Figura 26.5 — Linee Caratteristiche di Portafogli Azionari con Opzioni Vendute**. Pannello A ("Stock with Written Put" vs. "Stock Alone"): un portafoglio con una put venduta ha rendimenti tagliati verso il basso rispetto al possesso diretto delle azioni. Pannello B ("Stock with WrittenCall" vs. "Stock Alone"): un portafoglio con una call venduta ha rendimenti tagliati verso l'alto. Entrambi i profili generano linee caratteristiche non lineari, tipiche di molte strategie hedge fund.

*(slide 37–40)*

## Perché molti hedge fund vendono opzioni implicitamente

> [!example] Esempio
> **Meccanismo**: strategie come il convertible arbitrage o il fixed-income arbitrage generano rendimenti piccoli e stabili nella maggior parte dei mesi, ma subiscono perdite eccezionali in periodi di crisi. Questo profilo "tanti piccoli guadagni, rare grandi perdite" è tipico della vendita di opzioni.
>
> **Esempio numerico**: un fondo di convertible arbitrage:
>
> | | Mesi normali (95%) | Mesi di crisi (5%) |
> |---|---|---|
> | Rendimento mensile | +0,8% | −8,0% |
>
> Rendimento medio: $0,95 \times 0,8\% + 0,05 \times (-8,0\%) = +0,36\%/\text{mese}$
>
> Ma lo Sharpe ratio *appare* elevato perché la volatilità misurata su periodi normali è bassa. Il vero rischio è nelle code della distribuzione — ed è esattamente il rischio che un venditore di opzioni sopporta.
>
> **Figura 26.6 — Rendimento Mensile degli Indici Hedge Fund vs. S&P 500** (5 anni fino a settembre 2016): la curvatura verso il basso (concava) osservata in due dei pannelli del grafico conferma che i rendimenti di alcuni stili hedge fund, messi in relazione con il rendimento dell'S&P 500, replicano il profilo payoff di una posizione implicitamente corta su opzioni — a conferma della vendita implicita di opzioni discussa in precedenza.

*(slide 41–42)*

## Eventi estremi e rischio di coda

**Nassim Taleb**: molti hedge fund accumulano fama attraverso strategie che generano profitti la maggior parte del tempo, ma espongono gli investitori a perdite rare ma estreme.

**Esempi storici**:

- Il crollo dell'ottobre 1987
- **Long Term Capital Management (1998)**: perdita di $4,6 miliardi in poche settimane; leva 25:1; ha richiesto un salvataggio coordinato dalla Fed
- **Amaranth Advisors (2006)**: perdita di $6 miliardi su futures sul gas naturale
- **Archegos Capital (2021)**: perdita di $20+ miliardi nelle banche prime broker

*(slide 43)*

## Struttura commissionale 2+20 e commissione di incentivo come opzione call

> [!example] Esempio
> **2% del patrimonio più una commissione di incentivo pari al 20% dei profitti.**
>
> Le commissioni di incentivo sono effettivamente opzioni call sul portafoglio con:
> $$X = (\text{Valore del portafoglio}) \times (1 + \text{Rendimento del benchmark})$$
>
> **Esempio numerico**: portafoglio iniziale $S_0 = \$100$ milioni, $r_f = 3\%$
>
> | | Scenario A (Rend. +15%) | Scenario B (Rend. +3%) | Scenario C (Rend. −10%) |
> |---|---|---|---|
> | Valore fine anno | $115M | $103M | $90M |
> | Soglia ($S_0 \times 1,03$) | $103M | $103M | $103M |
> | Profitto sopra soglia | $12M | $0 | $0 |
> | Comm. incentivo (20%) | $2,4M | $0 | $0 |
> | Comm. gestione (2%) | $2,3M | $2,06M | $1,8M |
>
> Il gestore guadagna comunque la commissione di gestione anche nello Scenario C (−10%): **asimmetria a favore del gestore**.
>
> **Figura 26.7 — Commissioni di Incentivo come Opzione Call**: grafico dell'Incentive Fee in funzione del valore finale del portafoglio $S_T$, nullo fino alla soglia $S_0(1+r_f)$ e poi crescente linearmente con pendenza 0,20. La commissione di incentivo è equivalente a 0,20 opzioni call sul portafoglio con prezzo di esercizio $S_0(1+r_f)$. Il gestore ha un payoff convesso: guadagna nei rialzi, non perde nei ribassi ⇒ incentivo ad assumere rischio.

*(slide 44–45)*

## High water mark

> [!abstract] Definizione
> **High water mark**: il livello massimo raggiunto dal NAV del fondo.
>
> - Se un fondo subisce perdite, nessuna commissione di incentivo fino al recupero del valore massimo precedente
> - Con perdite ingenti, il recupero può essere troppo difficile ⇒ il fondo chiude
>
> **Esempio**:
>
> | | Anno 1 | Anno 2 | Anno 3 | Anno 4 |
> |---|---|---|---|---|
> | NAV per quota | $100 | $120 | $90 | $115 |
> | High water mark | $100 | $120 | $120 | $120 |
> | Profitto sopra HWM | $20 | – | – | – |
> | Comm. incentivo | Sì (20% di $20) | No | No | No |
>
> Nell'Anno 4, il NAV è risalito a $115 ma è ancora sotto il HWM di $120 ⇒ nessuna commissione. Il gestore deve prima recuperare il 33% di perdita prima di guadagnare incentivi. Molti preferiscono chiudere e aprire un nuovo fondo.

*(slide 46)*

## Fondi di fondi

> [!example] Esempio
> **Fondi di fondi (feeder fund)**
>
> - Hedge fund che investono in uno o più altri fondi → diversificano tra hedge fund
> - Dovrebbero fornire due diligence nella selezione dei fondi meritevoli
> - Lo scandalo Madoff ha dimostrato che questi vantaggi non sempre si realizzano
>
> I fondi di fondi:
>
> - Pagano una commissione di incentivo a ciascun fondo sottostante che sovraperforma, anche se la performance aggregata è negativa
> - Se i fondi sottostanti hanno stili simili, la diversificazione può essere un'illusione
>
> **Il problema dei FoF — esempio numerico**
>
> | | Fondo 1 | Fondo 2 | Fondo 3 | Fondo di Fondi |
> |---|---|---|---|---|
> | Inizio anno (milioni) | $1,00 | $1,00 | $1,00 | $3,00 |
> | Fine anno (milioni) | $1,20 | $1,40 | $0,25 | $2,85 |
> | Rendimento lordo | 20% | 40% | −75% | −5% |
> | Comm. incentivo (20%) | $0,04 | $0,08 | $0,00 | $0,12 |
> | Fine anno, netto | $1,16 | $1,32 | $0,25 | $2,73 |
> | Rendimento netto | 16% | 32% | −75% | −9% |
>
> Se fosse un fondo unico con rendimento lordo −5%: commissione di incentivo = $0.
>
> Come fondo di fondi: commissione di incentivo = $0,12M ⇒ il rendimento netto peggiora da −5% a −9%.
>
> **Il costo della struttura FoF**: 4 punti percentuali di rendimento perso.

*(slide 47–48)*

## Evidenza empirica: performance degli hedge fund nelle crisi

| Evento di crisi | S&P 500 | HF Composito | Miglior strategia HF |
|---|---|---|---|
| Crisi LTCM (ago–ott 1998) | −12,5% | −7,7% | Macro: +4,2% |
| Bolla dot-com (2000–2002) | −44,7% | −4,0% | Short Bias: +22% |
| Crisi finanziaria (2008) | −38,5% | −19,0% | Mgd Futures: +18% |
| COVID crash (feb–mar 2020) | −19,6% | −8,4% | Macro: +1,5% |
| Bear market 2022 (anno) | −18,1% | −4,3% | Macro: +9,3% |

- Gli hedge fund dimezzano le perdite rispetto all'S&P nei ribassi — il vero valore è nella protezione
- Le strategie macro e managed futures sono le migliori "assicurazioni" nei periodi di crisi
- Ma nel 2008 le correlazioni sono aumentate ("correlations go to one") — nessuna protezione completa
- **2022 è il caso più eloquente**: S&P −18%, obbligazioni −13%, ma HF solo −4%; il macro ha generato +9%

Fonti: HFRI, Bloomberg. Rendimenti cumulati nei periodi indicati.

*(slide 49)*

## Sintesi: messaggi chiave

1. **Flessibilità a caro prezzo**: gli hedge fund offrono strategie flessibili ma con commissioni elevate (2+20), bassa trasparenza e limitata liquidità
2. **Rendimenti variabili nel tempo**: dall'età d'oro degli anni '90 (15–20% annuo), al declino 2010–2019 (4–6%), alla ripresa 2020–2025 (+12,6% nel 2025) — il contesto di mercato è determinante
3. **Valore nelle crisi**: gli HF perdono meno dell'S&P nei ribassi (2008: −19% vs. −38%; 2022: −4% vs. −18%) — il vero beneficio è nella protezione del portafoglio
4. **Domiciliazione offshore**: il 75%+ dei fondi è alle Cayman — non per rendimenti lordi superiori, ma per neutralità fiscale a livello del veicolo
5. **Attenzione ai bias**: sopravvivenza, backfill, illiquidità e smoothing gonfiano la performance apparente di 3–5% annuo
6. **Rischio di coda nascosto**: molte strategie hanno profili simili alla vendita di opzioni — rendimenti stabili con rare perdite catastrofiche
7. **Sharpe ratio vs. rendimenti**: gli HF spesso battono l'S&P 500 su base corretta per il rischio, non in rendimento assoluto

*(slide 50)*
