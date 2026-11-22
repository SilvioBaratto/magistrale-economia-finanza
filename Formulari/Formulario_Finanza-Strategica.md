---
title: "Finanza Strategica — formulario"
subtitle: "Formule, quando usarle e come si calcola"
coursecode: "EM5005"
disclaimer: "Formulario personale a fini di studio (Finanza Strategica EM5005, prof. Alessandro Genovesi), costruito sulle note del corso. Non è materiale ufficiale del docente."
---

# Come usare il formulario

L'esame è scritto, dura 2 ore e ha tre parti: 20 domande a risposta singola, 2 esercizi di calcolo (procedimento e risultati in bella copia, al massimo 2 decimali) e una domanda di teoria a scelta tra due, in una facciata e mezza. Si usa **solo la calcolatrice**: nessun formulario. Per questo le formule vanno sapute a memoria, e questo foglio serve a impararle e a ripassarle.

Ogni voce ha la stessa forma: **Quando** si usa, **Formula**, **Come si decide o si calcola**, **Trappola**. Il simbolo † segna una formula ricavata dalle note e non scritta come tale nelle slide.

Notazione: $t_c$ aliquota fiscale, $D$ debito, $E$ capitale proprio (valore di mercato), $PFN$ posizione finanziaria netta, $g$ crescita costante, $N$ ultimo anno del piano esplicito.

**Convenzioni di segno.** $PFN>0$: l'impresa ha debito netto. $PFN<0$: ha più cassa che debito. $FCFO$ è il flusso operativo dopo le imposte e prima degli investimenti in capitale fisso. Nelle formule del VAN si usano i flussi $FCFO_t$ e l'investimento $I_0$ a parte.

# Dal testo alla formula

| Il testo dà o chiede | Si usa | Capitolo |
|---|---|---|
| flussi di un progetto, «conviene?» | VAN al WACC (VAM se si vuole il progetto «puro») | Criteri di scelta degli investimenti |
| due progetti, capitale limitato | indice di redditività | Criteri di scelta degli investimenti |
| WACC non affidabile | TIR o tempo di recupero | Criteri di scelta degli investimenti |
| scenari con probabilità e una scelta del management | opzioni reali | Opzioni reali |
| «tasso di sconto del progetto», «costo dell'equity» | CAPM, beta unlevered, WACC | Costo del capitale |
| beta di un comparabile da riportare all'impresa | $\beta_U$ e poi $\beta_L$ | Costo del capitale |
| valore di un'impresa da un piano a 3-5 anni | DCF analitico con terminal value | Metodi DCF |
| flussi costanti o in crescita costante | DCF sintetico (steady state, steady growth) | Metodi DCF |
| impresa non quotata, con debito, valore dello scudo fiscale | VAM | Metodi DCF |
| multipli di mercato, comparabili, EV/EBITDA | valutazione relativa | Multipli di mercato |
| «normalizzare l'EBITDA», «PFN», prezzo | due diligence finanziaria | Due diligence finanziaria |
| acquisizione, sinergie, prezzo massimo | stratificazione del valore, NPV | Sinergie, acquisizioni, fusioni |
| fusione, azioni da assegnare | rapporto di concambio | Sinergie, acquisizioni, fusioni |

# Valore del tempo e flussi di cassa

**Quando.** Per confrontare importi a date diverse e per capire quale flusso scontare.

$$100\ \text{oggi}=100(1+r)\ \text{fra un anno}\qquad\qquad 100\ \text{fra un anno}=\frac{100}{1+r}\ \text{oggi}$$

Un investimento che rende meno di $r$ (tasso privo di rischio) distrugge ricchezza. Il **rischio ha un prezzo**: a un progetto rischioso si chiede un rendimento superiore a $r$.

## Dalla gestione ai flussi: FCFO, FCFF, FCFE

| Passaggio | Voce |
|---|---|
| | MOL (= EBITDA) |
| $-$ | variazione del capitale circolante netto operativo (CCNO) |
| $=$ | cash flow gestionale lordo |
| $-$ | flusso fiscale operativo (imposte $+$ scudi $-$ variazione dei debiti per imposte) |
| $=$ | cash flow gestionale netto, **FCFO** |
| $-/+$ | investimenti / disinvestimenti in capitale fisso |
| $=$ | **FCFF** (free cash flow to the firm) |
| $+/-$ | proventi / oneri straordinari |
| $-$ | oneri finanziari netti |
| $+$ | scudo fiscale sugli oneri finanziari |
| $+/-$ | aumento / riduzione dei debiti finanziari |
| $=$ | **FCFE** (free cash flow to equity) |

$$\text{Cash flow gestionale lordo}=MOL-\Delta CCNO\qquad\qquad CCN=\text{crediti commerciali}+\text{rimanenze}-\text{debiti verso fornitori}$$

**Come si decide quale flusso usare.** Il flusso e il tasso devono essere coerenti: FCFF con il WACC (dà il valore dell'impresa, EV); FCFE con il costo dell'equity $r_E$ (dà direttamente il valore del capitale proprio); FCFO con $r_0$ (VAM).

**Trappola.** Un aumento di CCN assorbe liquidità: entra con il segno meno. Un aumento dei debiti verso fornitori riduce il CCN e libera liquidità.

# Criteri di scelta degli investimenti

**Quando.** Un progetto ha un esborso iniziale $I_0$ e flussi attesi $FCFO_t$ per $N$ anni.

| Criterio | Formula | Si accetta se |
|---|---|---|
| **VAN** | $VAN=-I_0+\displaystyle\sum_{t=1}^{N}\frac{FCFO_t}{(1+WACC)^t}$ | $VAN>0$ |
| **VAM** | $VAM=-I_0+\displaystyle\sum_{t=1}^{N}\frac{FCFO_t}{(1+r_0)^t}$ | $VAM>0$ |
| **Indice di redditività** | $IR=\dfrac{VA}{I_0}$, con $VA$ valore attuale dei flussi | $IR>1$ |
| **TIR** | $r$ tale che $-I_0+\displaystyle\sum_{t=1}^N\dfrac{FCFO_t}{(1+r)^t}=0$ | $TIR>WACC$ |
| **Tempo di recupero** | minimo $t$ con $\sum_{i=1}^{t}FCFO_i\ge I_0$ | $t\le$ cut-off |
| **Recupero attualizzato** | minimo $t$ con $\sum_{s=1}^{t}\dfrac{FCFO_s}{(1+WACC)^s}\ge I_0$ | $t\le$ cut-off |

Il VAN usa il WACC; il VAM usa $r_0$, il costo del capitale *unlevered*, indipendente dalla struttura finanziaria. Il VAN è l'unica misura **in euro di valore creato**.

## Quale criterio usare

| WACC | Flussi di cassa | Metodo |
|---|---|---|
| affidabile | affidabili | VAN e indice di redditività |
| affidabile | non affidabili | tempo di recupero attualizzato |
| non affidabile | affidabili | TIR o tempo di recupero |
| non affidabile | non affidabili | tempo di recupero |

Nella prassi i più usati sono VAN, TIR e, in parte, il recupero attualizzato.

**Razionamento di capitale.** Il VAN non lo considera: tra due progetti, quello con VAN più alto può richiedere un esborso molto maggiore. Con capitale limitato si guarda l'indice di redditività, che misura il valore creato per euro investito.

**Trappole.**

1. Il TIR non funziona con **flussi che cambiano segno più volte**.
2. Il tempo di recupero semplice ignora il valore del tempo e i flussi oltre il cut-off; il cut-off è arbitrario.
3. I VAN di progetti molto diversi (aprire un punto vendita, acquisire una catena) sono poco comparabili nella realtà.
4. Il tasso di sconto non è il tasso privo di rischio: ci vuole il costo del capitale (WACC o $r_0$).

# Opzioni reali

**Quando.** Il testo dà **scenari con probabilità** e una scelta che il management può fare dopo aver visto lo scenario: espandere, attendere, abbandonare. Il VAN tradizionale assume un management passivo e ignora questo valore.

$$\text{valore dell'opzione}=VAN_{\text{con opzione}}-VAN_{\text{senza opzione}}\qquad\quad VAN=\sum_s p_s\cdot VAN_s$$

**Procedura (uguale per le tre opzioni).**

1. Calcolare il VAN di ogni scenario **senza opzione** e pesarlo con le probabilità: VAN senza opzione.
2. Riscrivere i flussi dello scenario in cui l'opzione viene esercitata (con i **tempi giusti**) e calcolare il VAN di quello scenario.
3. Pesare con le probabilità: VAN con opzione. Il valore dell'opzione è la differenza.

| Opzione | Quando conviene | Come cambiano i flussi |
|---|---|---|
| **Espansione** | lo scenario buono dà accesso a un nuovo investimento | l'esborso della seconda linea è un flusso di $T_1$ (si attualizza di un anno), non di $T_0$; i suoi incassi seguono |
| **Attesa** | rinviare il lancio di un progetto già sviluppato, per vedere il riscontro | l'investimento resta in $I_0$; nello scenario avverso il flusso del primo anno è zero e gli incassi slittano di un anno |
| **Abbandono** | lo scenario cattivo fa perdere più di quanto vale chiudere | si interrompono i flussi e si incassa il valore di realizzo dell'impianto |

**Trappole.**

1. Il VAN senza opzione si calcola sempre e non cambia con l'opzione.
2. Nell'abbandono, se si chiude alla fine del primo anno, si discute se aggiungere al valore di realizzo anche il flusso operativo incassato in quell'anno. Controllare la traccia.
3. Le opzioni reali sono forzature della realtà: probabilità difficili da stimare e progetti poco comparabili. Servono a ragionare in modo flessibile.

# Costo del capitale

## WACC e costo del debito

**Quando.** Tasso di sconto di un'impresa o di un progetto finanziato con equity e debito.

$$WACC=r_E\,\frac{E}{E+D}+r_D\,(1-t_c)\,\frac{D}{E+D}$$

$$r_D=\frac{\sum_i(\text{Debito}_i\times\text{tasso}_i)}{\sum_i\text{Debito}_i}\qquad r_D^{\text{post-tax}}=r_D(1-t_c)$$

I pesi sono a valori di mercato. Il debito costa meno dell'equity perché ha priorità sui flussi (rischio minore) e gode dello scudo fiscale.

## CAPM e beta

$$r_E=r_f+\beta\,(R_m-r_f)\qquad\qquad\beta=\frac{\mathrm{COV}(R_t;R_m)}{\mathrm{VAR}(R_m)}$$

| Componente | Significato |
|---|---|
| $r_f$ | tasso privo di rischio, il «valore del tempo». Per imprese italiane il **Bund tedesco a 10 anni** (non il BTP, che incorpora già il rischio Paese) |
| $\beta$ | quantità di rischio sistematico |
| $R_m-r_f$ | premio per il rischio di mercato, il «prezzo del rischio» |

**Lettura del beta.** $\beta>1$: il titolo amplifica il mercato (settori ciclici: automotive, costruzioni, lusso, turismo, compagnie aeree). $\beta=1$: segue il mercato (trasporti, assicurazioni). $0<\beta<1$: più tiepido (utilities, farmaceutico, beni di prima necessità). Il beta dipende da ciclicità dei ricavi, leva operativa (costi fissi su variabili) e leva finanziaria.

## Rischio Paese: due alternative equivalenti

Si carica il rischio Paese **in un solo punto**, per coerenza.

| | Tasso privo di rischio | Premio di mercato | Costo dell'equity |
|---|---|---|---|
| **Alternativa 1** | rendimento del bond del Paese (BTP) | $MRP$ di un mercato a rischio minimo (USA) | $r_E=r_{BTP}+\beta\,MRP$ |
| **Alternativa 2** | Bund | $MRP+CRP$ | $r_E=r_{Bund}+\beta\,(MRP+CRP)$ |

$$CRP=\text{spread sovrano}\times\frac{\sigma_{\text{azioni}}}{\sigma_{\text{obbligazioni}}}$$

Esempio del corso (valori Damodaran): $MRP=4{,}12\%$, $CRP_{Italia}=1{,}08\%$, quindi $4{,}12\%+1{,}08\%=5{,}20\%$; Bund $2{,}20\%$, BTP $4{,}40\%$. Con questi numeri i due metodi coincidono solo per $\beta\approx2{,}04$; per beta più bassi il metodo 1 dà il valore più alto. Fa fede il Paese dove si svolge il business, non la sede legale.

## Beta unlevered e tasso di sconto del progetto

**Quando.** Il beta osservato di un comparabile incorpora la sua leva finanziaria ($\beta_L$, levered); per un progetto si vuole il rischio operativo, senza debito e senza cassa.

| Situazione | $\beta_U$ da $\beta_L$ | $\beta_L$ da $\beta_U$ ($\dagger$) |
|---|---|---|
| $PFN>0$ (debito) | $\beta_U=\dfrac{\beta_L}{1+\dfrac{PFN}{E}(1-t_c)}$ | $\beta_L=\beta_U\left[1+\dfrac{PFN}{E}(1-t_c)\right]$ |
| $PFN<0$ (cassa) | $\beta_U=\beta_L\,\dfrac{E}{E+PFN}$ | $\beta_L=\beta_U\,\dfrac{E+PFN}{E}$ |

$$r_0=r_f+\beta_U\,(R_m-r_f)$$

Con $PFN>0$ si ha $\beta_U<\beta_L$; con $PFN<0$ si ha $\beta_U>\beta_L$. Nella formula con cassa **non compare** $(1-t_c)$: chi ha cassa non ha scudo fiscale. In entrambe il beta del debito è posto uguale a zero.

**Seconda proposizione di Modigliani-Miller con imposte** (debito costante e perpetuo):

$$r_E=r_0+(r_0-r_D)(1-t_c)\frac{D}{E}$$

# Grandezze di valutazione e relazioni fra loro

| Grandezza | Formula |
|---|---|
| Enterprise value | $EV=MKCAP+PFN$ |
| Equity value | $E=EV-PFN$ |
| NOPAT | $NOPAT=EBIT\times(1-t_c)$ |
| Capitale investito netto | $CIN=CCN+\text{immobilizzazioni caratteristiche nette}=\text{Patrimonio netto}+PFN$ |
| PFN | $PFN=\text{debiti finanziari}-\text{disponibilità liquide}$ |
| ROE | $\dfrac{\text{utile}}{\text{patrimonio netto}}$ |
| ROI | $\dfrac{EBIT}{CIN}$ (vedi le decisioni aperte) |
| ROS | $\dfrac{EBIT}{Sales}$ |
| EPS, DPS | $EPS=\dfrac{\text{utile}}{n^\circ\text{ azioni}}\qquad DPS=EPS\,(1-b)$, con $b$ quota di utile trattenuta |
| Book value per azione | $\dfrac{\text{patrimonio netto}}{n^\circ\text{ azioni}}$ |

Ottica **assets** (valore dell'attività operativa): EV, CIN, NOPAT, FCFF, WACC. Ottica **equity** (valore del capitale proprio): MK CAP, patrimonio netto, reddito di bilancio, FCFE, $r_E$.

**Trappola.** Se $PFN<0$ (cassa netta) l'equity value supera l'EV: $E=EV-PFN=EV+\lvert PFN\rvert$.

# Metodi DCF

## Formule generali

**Quando.** Il valore è il valore attuale dei flussi futuri.

$$V=\sum_{t=1}^{\infty}\frac{FCFF_t}{(1+WACC)^t}\qquad E=\sum_{t=1}^{\infty}\frac{FCFE_t}{(1+r_E)^t}\qquad E=V-D$$

## Modelli sintetici: flussi costanti o in crescita costante

**Quando.** Impresa in regime, senza un piano esplicito: si usano formule chiuse.

| | Ottica assets | Ottica equity |
|---|---|---|
| **Steady state** (nessuna crescita) | $V=\dfrac{NOPAT}{WACC}$ | $E=\dfrac{\text{Reddito di bilancio}}{r_E}$ |
| **Steady growth** (crescita $g$) | $V=\dfrac{NOPAT\,(1+g)-CINO\cdot g}{WACC-g}$ | $E=\dfrac{\text{Reddito di bilancio}\,(1+g)-C.P.\cdot g}{r_E-g}$ |

In steady state $FCFF=NOPAT$ e $FCFE=$ reddito di bilancio; il termine $CINO\cdot g$ (o $C.P.\cdot g$) è l'investimento che finanzia la crescita. Con $g=0$ le formule di steady growth coincidono con quelle di steady state. La serie converge solo se $g<WACC$ (assets) o $g<r_E$ (equity).

**Flusso nei due regimi (da ricordare).**

| Voce | Generale | Steady state | Steady growth |
|---|---|---|---|
| FCFF | $MOL-\Delta CCNO-\text{imposte}\mp\text{investimenti}$ | $NOPAT$ | $NOPAT(1+g)-g\cdot CINO$ |
| FCFE | FCFF $-$ oneri fin. netti $+$ scudo $\pm\Delta$ debiti | reddito di bilancio | $\text{Reddito}(1+g)-g\cdot C.P.$ |

## Modelli analitici: piano esplicito più terminal value

**Quando.** C'è un piano di 3-7 anni.

$$V=\sum_{t=1}^{N}\frac{FCFF_t}{(1+WACC)^t}+\frac{TV}{(1+WACC)^N}\qquad E=\sum_{t=1}^{N}\frac{FCFE_t}{(1+r_E)^t}+\frac{TV}{(1+r_E)^N}$$

**Terminal value** (rendita perpetua posticipata, riferita a fine anno $N$):

| Ipotesi dopo l'anno $N$ | $TV$ assets | $TV$ equity |
|---|---|---|
| steady state | $\dfrac{NOPAT}{WACC}$ | $\dfrac{\text{Reddito netto}}{r_E}$ |
| crescita costante $g$ | $\dfrac{NOPAT(1+g)-CINO\cdot g}{WACC-g}$ | $\dfrac{\text{Reddito netto}(1+g)-CP\cdot g}{r_E-g}$ |

$NOPAT$, $CINO$, reddito netto e $CP$ sono quelli dell'ultimo anno esplicito. Forma di Gordon con il flusso del primo anno del TV:

$$TV_N=\frac{FCFF_{N+1}}{WACC-g}\qquad\text{oppure}\qquad TV_N=\frac{NOPAT_{N+1}\left(1-\dfrac{g}{ROIC}\right)}{WACC-g}\ \ (\dagger)$$

Con $ROIC=\dfrac{NOPAT_{N+1}}{CINO_N}$: se $ROIC=WACC$ la crescita non aggiunge valore ($TV=NOPAT_{N+1}/WACC$ per qualunque $g$); se $ROIC>WACC$ il TV cresce con $g$; se $ROIC<WACC$ diminuisce.

**Come si calcola il valore attuale del TV.** Dividere $TV$ per $(1+WACC)^N$ (o $(1+r_E)^N$).

**Peso del TV e controlli.**

$$\frac{TV_{Assets}}{V_{Assets}}\qquad\frac{TV_{equity}}{Equity}$$

Un peso oltre il **85-90%** segnala: errori nei flussi espliciti, piano troppo breve, oppure che conviene un metodo sintetico. Altri controlli: coerenza fra fatturato e capitale fisso, andamento di MOL/ricavi. Il fattore $1/(WACC-g)$ rende il TV molto sensibile a piccole variazioni di $g$ e del WACC. La crescita di lungo periodo sta di norma fra 0% e 2%, al massimo la crescita nominale dell'economia.

**Tipi di TV.** *Economico*: l'impresa mantiene una redditività superiore al costo-opportunità. *Di equilibrio*: redditività uguale al minimo atteso, nessuna creazione di valore dopo $N$. Per imprese a vita limitata (concessioni, miniere, joint venture): valore terminale **contabile** o **di liquidazione**, non rendita perpetua.

**Modelli multi-step.** Crescita iniziale alta $g^h$, poi normale $g^{lt}$ (due stadi); con un periodo intermedio di transizione a crescita decrescente (tre stadi), perché una crescita sopra quella dell'economia non dura per sempre.

## VAM (Valore Attuale Modificato)

**Quando.** Impresa non quotata (non serve il valore di mercato dell'equity), struttura finanziaria che cambia, si vuole vedere separatamente il valore dello scudo fiscale.

$$V=V_U+V_{TS}$$

**Steady state** (debito $D$ costante e perpetuo, $\text{oneri finanziari}=D\,r_D$):

$$V=\frac{EBIT\,(1-t_c)}{r_0}+D\,t_c$$

L'EBIT dopo le imposte (NOPAT) si attualizza a $r_0$; lo scudo $D\,r_D\,t_c$ si attualizza a $r_D$ e vale $D\,t_c$.

**Steady growth:**

$$V=\frac{EBIT_N(1-t_c)(1+g)-g\cdot CIN_N}{r_0-g}+\frac{D_N\,r_D\,t_c}{r_D-g}$$

Se anche i benefici fiscali crescono con il resto, si sconta lo scudo a $r_0$ (versione di **Ruback**): stesso denominatore $r_0-g$ per entrambi i termini.

**Analitico (quattro componenti).**

$$V=V_{U,\text{esplicita}}+V_{TS,\text{esplicita}}+TV_U+TV_{TS}$$

$$V_{U,\text{esplicita}}=\sum_{i=1}^{N}\frac{FCFO_i}{(1+r_0)^i}\qquad V_{TS,\text{esplicita}}=\sum_{i=1}^{N}\frac{\text{Oneri fin.}_i\cdot t_c}{(1+r_D)^i}$$

$$TV_U=\frac{EBIT_N(1-t_c)(1+g)-g\cdot CIN_N}{r_0-g}\cdot\frac{1}{(1+r_0)^N}\qquad TV_{TS}=\frac{D_N\,r_D\,t_c}{r_D-g}\cdot\frac{1}{(1+r_D)^N}$$

**Vantaggi del VAM.** Non richiede il valore di mercato dell'equity; $r_0$ non cambia se cambia l'indebitamento; è trasparente (valore unlevered e scudo fiscale restano addendi distinti).

**Trappola.** Il $TV_{TS}$ qui sopra non ha il fattore $(1+g)$. Se $D_N$ fosse il debito su cui maturano gli oneri dell'anno $N$, il primo flusso sarebbe $D_N\,r_D\,t_c(1+g)$ (vedi le decisioni aperte).

# Multipli di mercato (valutazione relativa)

**Quando.** Si valuta per confronto con imprese simili (*comparables*), con finalità orientative, in vista di transazioni ravvicinate. Si assume che i prezzi dei comparabili siano stime non distorte del valore e che il valore dipenda da un'unica grandezza.

$$K\ (\text{multiplo})=\frac{\text{valore (assets o equity)}}{\text{grandezza economica o patrimoniale}}\qquad EV=EBITDA\times\text{multiplo}$$

| Ottica assets (numeratore $EV$) | Ottica equity (numeratore prezzo o MK CAP) |
|---|---|
| EV/Sales, EV/EBITDA, EV/EBIT, EV/CIN | P/E, P/Cash flow reddituale, P/E adjusted, P/BV |

**Procedura (assets).**

1. Scegliere i comparabili (campione o settore).
2. Calcolare il multiplo di ciascuno e la **media** (o mediana) del campione.
3. Moltiplicare il multiplo medio per la grandezza dell'impresa da valutare (EBITDA, Sales, CIN…): si ottiene l'**EV**.
4. Sottrarre la PFN: $E=EV-PFN$.

Legame utile: $\dfrac{EV}{EBITDA}=\dfrac{EV/Sales}{\text{margine EBITDA}}$.

**Origine dei multipli.** *Di borsa*: prezzi di transazioni di minoranza, risultato di molte negoziazioni. *Delle transazioni concluse*: pacchetti di maggioranza o di minoranza qualificata, risultato di una sola operazione. Per i prezzi di borsa si può usare la media dei 6 o 12 mesi precedenti.

## Da che cosa dipende il P/E (comparabilità)

Dal modello di Gordon, con $b$ quota di utile reinvestita, $g=ROE\cdot b$ e la proposizione II di Modigliani-Miller:

$$P=\frac{EPS\,(1-b)}{r_E-g}\qquad\frac{P}{EPS}=\frac{1-b}{r_0+(r_0-r_D)(1-t_c)\dfrac{D}{E}-ROE\cdot b}$$

| Termine | Fonte di difformità fra imprese |
|---|---|
| $EPS$ | principi contabili |
| $r_0$, $(r_0-r_D)$ | rischio operativo |
| $(1-t_c)$ | profili fiscali |
| $D/E$ | leva finanziaria |
| $ROE\cdot b$ | crescita e redditività |

In assenza di crescita $P/EPS=1/r_E$. Un P/E alto indica attese di crescita elevate.

## Criticità dei multipli

*Comparabilità*: crescita e redditività, leva finanziaria, leva operativa, principi contabili, profili fiscali. *Costruzione del singolo multiplo*: proventi e oneri straordinari, investimenti extra, crediti fiscali, perdite, bilanci consolidati. In presenza di perdite il P/E perde significato: si usano EV/Sales o EV/EBITDA rettificato. Rimedi: comparabili dello stesso paese (contabilità e fisco), campione con crescita simile, oppure le *value maps*.

## Value maps

**Quando.** Si vuole correggere la comparabilità di crescita e redditività legando il multiplo a un indicatore di redditività.

**Relazioni teoriche in assenza di crescita:**

$$\frac{P_0}{BV_0}=\frac{ROE}{r_E}\qquad\frac{EV_0}{CIN_0}=\frac{ROI\,(1-t_c)}{WACC}\qquad\frac{EV_0}{Sales_0}=\frac{ROS_0\,(1-t_c)}{WACC}$$

Se $ROE=r_E$ il valore di mercato è uguale al valore contabile ($P/BV=1$); se $ROE>r_E$ il management crea ricchezza ($P/BV>1$); se $ROE<r_E$ il valore di mercato è sotto il contabile. Per $ROI\,(1-t_c)$ contro $WACC$ vale lo stesso con $EV/CIN$. Il ROI compare moltiplicato per $(1-t_c)$ perché è un rapporto sull'EBIT: con l'utile netto le imposte sarebbero dedotte due volte.

**Applicazione (regressione sul campione di comparabili).**

| Ottica | Passi |
|---|---|
| equity (P/BV su ROE) | $P/BV=\alpha+\beta\,ROE+\varepsilon$; $(P/BV)_{imp.}=\alpha+\beta\,ROE_{imp.}$; $E_{imp.}=(P/BV)_{imp.}\times CP_{imp.}$ |
| assets (EV/CIN su ROI) | $EV/CIN=\alpha+\beta\,ROI+\varepsilon$; $EV_{imp.}=(EV/CIN)_{imp.}\times CIN_{imp.}$; $E_{imp.}=EV_{imp.}-PFN_{imp.}$ |
| assets (EV/Sales su ROS) | $EV/Sales=\alpha+\beta\,ROS+\varepsilon$; $EV_{imp.}=(EV/Sales)_{imp.}\times Sales_{imp.}$; $E_{imp.}=EV_{imp.}-PFN_{imp.}$ |

**Value map unlevered** (corregge anche la diversa leva). Si usa il multiplo su un EV depurato dello scudo fiscale:

$$EV/CIN\ UL=\alpha+\beta\,ROI+\varepsilon\quad\Rightarrow\quad EV\,UL_{imp.}=(EV/CIN\ UL)_{imp.}\times CIN_{imp.}$$

$$EV_{imp.}=EV\,UL_{imp.}+D\times t_c\qquad E_{imp.}=EV_{imp.}-PFN_{imp.}$$

Lo scudo fiscale si calcola sul debito dell'impresa da valutare, non su quello del campione.

# Due diligence finanziaria

**Quando.** Nel passaggio dal prezzo concordato all'equity effettivamente pagato, e nel controllare la qualità dei numeri su cui si applica il multiplo.

$$EV=EBITDA\times\text{multiplo}\qquad\text{Equity value}=EV-PFN$$

I tre indicatori da analizzare sono **EBITDA, PFN e CCN**.

## EBITDA e normalizzazione

$$EBITDA=\text{A) Valore della produzione}-\text{B) Costi della produzione}+\text{Ammortamenti e svalutazioni delle immobilizzazioni}$$

**Normalizzare** significa eliminare gli elementi eccezionali o estranei al core business, positivi e negativi, per avere una redditività sostenibile. Tre categorie: elementi **non ricorrenti**, **politiche di bilancio** (per esempio capitalizzazioni), **costi o ricavi mal collocati** (per esempio spese bancarie).

**Regola dei segni.** $EBITDA_{rettificato}=EBITDA_{civilistico}+\text{rettifiche}$: una rettifica **positiva** (costo non ricorrente da riaggiungere) aumenta l'EBITDA; una **negativa** (ricavo non ricorrente o non inerente, costo di competenza non ancora a bilancio) lo riduce.

| Voce | Verso |
|---|---|
| buonuscita all'amministratore (costo non ricorrente) | $+$ |
| rilascio di un fondo (ricavo non di competenza) | $-$ |
| plusvalenza su immobile non operativo | $-$ |
| spese bancarie (costo operativo, da portare sopra l'EBITDA) | $-$ |
| manutenzioni sotto il livello congruo | $-$ (differenza dalla media storica) |
| contenzioso di competenza non a bilancio | $-$ |
| crediti incagliati non svalutati | $-$ |
| contributi in conto esercizio (non ricorrenti) | $-$ |

**Effetto sul prezzo.** A parità di multiplo, $\Delta EV=\Delta EBITDA\times\text{multiplo}$.

## PFN e CCN

$$PFN=\text{debiti finanziari}-\text{disponibilità liquide}$$

Perché $E=EV-PFN$, una PFN sottostimata fa salire il prezzo: va **normalizzata** per rappresentare il reale indebitamento. Si **aggiungono** ai debiti i *debt-like items* (fornitori scaduti oltre il normale, debiti maturati e non pagati, passività potenziali non a bilancio come derivati e leasing, finanziamenti intercompany e dei soci, TFR quando assume natura di finanziamento) e si **tolgono** dalla liquidità le voci non liquide (conti vincolati, titoli, crediti finanziari). La PFN può cambiare alla data di *closing*: si fa un *price adjustment*.

$CCN$ varia con crediti commerciali e rimanenze (lo aumentano) e debiti verso fornitori (lo riducono). Un CCN anomalamente basso a ridosso della vendita obbliga l'acquirente a esborsi subito dopo. CCN e PFN sono **vasi comunicanti**: un fornitore pagato con grande ritardo gonfia la cassa ma è in realtà un finanziamento, quindi appartiene alla PFN.

# Sinergie, acquisizioni, fusioni

## Valore di acquisizione e sinergie

$$W_{acq}=W_S+W_D$$

con $W_S$ valore *stand alone* del target (valore dell'equity) e $W_D$ valore delle sinergie.

**Con benefici privati** (flussi di cui godono gli azionisti di controllo) e quota $\alpha$:

$$W_\alpha=(W_S+W_D)\,\alpha+W_{PB^*}+(1-\alpha)\,W_{PB}$$

con $W_{PB^*}$ benefici privati senza effetto sui flussi *stand alone* e $W_{PB}$ benefici privati con effetto. In forma sintetica, con sinergie e opportunità **divisibili** e **indivisibili**:

$$W_\alpha=(W_S+W_{DIV})\,\alpha+W_{IND}\qquad\qquad w=\frac{W_\alpha}{N\alpha}$$

Il valore **unitario** aumenta al diminuire di $\alpha$ perché $W_{IND}$ si ripartisce su meno azioni: $w(\alpha)=\dfrac{W_S+W_{DIV}}{N}+\dfrac{W_{IND}}{N\alpha}$. Premio di controllo: dovuto ai benefici privati. Sconto di minoranza: mancanza di controllo e di liquidità.

## Stratificazione del valore: le sinergie in tre strati

**Quando.** L'esercizio dà i flussi e i tassi di A e B stand alone e chiede il valore delle sinergie, il prezzo massimo, il NPV.

Base (VAM in steady state):

$$W_U=\frac{FCFO}{r_0}\qquad W_L=W_U+D\,t_c\qquad W_E=W_L-D$$

$$W_D=W_{flussi}+W_{TS}+W_{c.cap.}$$

| Strato | Effetto | Formula |
|---|---|---|
| Flussi incrementali (sinergie operative) | quantità | $W_{flussi}=\dfrac{\Delta FCFO_A+\Delta FCFO_B}{r_{0,A+B}}$ |
| Debito incrementale (sinergie fiscali) | struttura finanziaria | $W_{TS}=\Delta D\cdot t_c$ |
| Modifica del costo del capitale (sinergie finanziarie) | qualità, cioè rischio | $W_{c.cap.}=\dfrac{FCFO_A+FCFO_B}{r_{0,A+B}}-\left(\dfrac{FCFO_A}{r_{0,A}}+\dfrac{FCFO_B}{r_{0,B}}\right)$ |

**Verifica.** $W_D=W_{L,A+B}-(W_{L,A}+W_{L,B})$.

## Prezzo massimo, NPV, premio

$$\text{premio}_{MAX}=W_D\qquad P_{MAX}=W_S+W_D=W_{acq}$$

$$NPV(\text{acquisizione})=W_{acq}-P=W_D-(P-W_S)$$

L'acquisizione crea valore per l'acquirente se $P<W_{acq}$, cioè se il premio $P-W_S$ è minore delle sinergie. Per $P=W_{acq}$ il NPV è zero e le sinergie vanno interamente al venditore. $NPV(\text{investimento})=\text{V.A. lordo}-\text{Inv. iniziale}$. Per riportare il prezzo massimo a valore d'impresa si somma il debito netto del target.

## Procedura per l'esercizio di acquisizione con sinergie

1. Calcolare il valore stand alone di ciascuna impresa: $W_U=FCFO/r_0$, poi $W_L=W_U+D\,t_c$, poi $W_E=W_L-D$. Il $W_S$ del target è il suo $W_E$.
2. Calcolare i tre strati: $W_{flussi}$ (a $r_{0,A+B}$), $W_{c.cap.}$ (nuovo tasso contro i tassi separati), $W_{TS}=\Delta D\cdot t_c$.
3. $W_D$ è la somma; $W_{acq}=W_S+W_D$.
4. Premio massimo $=W_D$, prezzo massimo $=W_{acq}$, $NPV=W_{acq}-P$ per il prezzo dato.
5. Se la traccia dà una quota $\alpha<100\%$, scalare il valore secondo $W_\alpha$ (vedi la nota sotto).

**Nota sul metodo.** Nei simulati e negli esercizi del docente la quota $\alpha$ scala **solo la sinergia di tasso**. La nota del corso scrive invece $\alpha\,(W_S+W_D)$. Il segno del NPV non cambia nei dieci simulati, i valori sì: con $\alpha<100\%$ mostrare entrambe le letture e indicare quale segue la chiave. La scelta è da confermare con il docente.

## Rapporto di concambio

**Quando.** Fusione per incorporazione di B in A: quante azioni di A ricevono gli azionisti di B.

Con $N_A$, $N_B$ azioni, $W_A$, $W_B$ valori stand alone del capitale e $W_{A+B}=W_A+W_B+W_D$ il valore dopo la fusione:

$$RC_{MAX}=\frac{N_A}{N_B}\cdot\frac{W_{A+B}-W_A}{W_A}\qquad\qquad RC_{MIN}=\frac{W_B\,N_A}{N_B\,(W_{A+B}-W_B)}$$

Dopo la fusione le azioni sono $N_A+N_B\,RC$. $RC_{MAX}$ è il massimo accettabile dagli azionisti di A (oltre scendono sotto $W_A$); $RC_{MIN}$ è il minimo accettabile dagli azionisti di B. Il rapporto negoziato cade nell'intervallo, che esiste solo se $W_D\ge0$. Agli estremi l'intero $W_D$ va a una sola delle due parti.

## Perché si fa una fusione

Ragioni valide: **economie di scala**, **integrazione verticale** (a monte o a valle), **risorse complementari**, **eccesso di fondi** (le *cash cows* hanno pochi progetti a VAN positivo). Ragione dubbia: la **diversificazione**, perché l'azionista può diversificare da solo e il mercato applica un *discount* di gruppo.

# Decisioni aperte: dove nota e slide divergono

Per queste voci non c'è ancora una scelta definitiva. Se un esercizio le tocca, esporre le due letture e seguire la chiave.

| # | Argomento | Nota del corso | Slide, dataset o esercizi del docente |
|---|---|---|---|
| 1 | EV con PFN negativa | capitalizzazione di mercato $+$ PFN (95 e 74) | intero attivo (105 e 84) |
| 2 | ROI | $EBIT/CIN$ | utile netto/CIN |
| 3 | Plusvalenza nella normalizzazione dell'EBITDA | totale 169.917 con rettifica di 5.000 | dati con plusvalenza di 95.000 (EBITDA rettificato 79.917) |
| 4 | Razionamento di capitale, flussi di B | 900.000 (dedotti) | 700.000 |
| 5 | FCFE di DeLonghi | 90.791.207 | 176.605.112, senza FCFF |
| 6 | TV dello scudo fiscale | senza $(1+g)$ | da confermare sul libro (formula 8.30) |
| 7 | Quota $\alpha$ nell'acquisizione | $\alpha\,(W_S+W_D)$ | $\alpha$ solo sulla sinergia di tasso (simulati, docente) |
| 8 | Eni e Matrìca-Novamont | fusione per incorporazione (fonti) | fusione per unione |

**Errore noto.** Nella soluzione dell'esercizio 4 (abbandono) delle dispense di esercizi extra il flusso del primo anno è scontato due volte, perché si calcola $(900-38)/(1+r)$. L'appello simulato 08 usa il calcolo corretto.
