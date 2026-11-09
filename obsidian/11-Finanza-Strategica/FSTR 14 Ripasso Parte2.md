---
title: "Riepilogo II: DCF, integrazioni e due diligence"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_14_Ripasso-Parte2.pdf"
text_layer: true
verified: true
generated: 2026-08-30
---

## Inquadramento

Il capitolo riepiloga la seconda parte del corso: lo scudo fiscale e i modelli DCF con il terminal value, i multipli di mercato e la loro comparabilità, il valore delle operazioni di integrazione tra imprese e la due diligence. Le definizioni sono richiamate in forma sintetica; le formule e gli esempi numerici completi si trovano nei capitoli a cui rinviano i collegamenti. La prima parte del riepilogo, su flussi di cassa, criteri di investimento, costo del capitale e multipli di borsa, è in [[FSTR 13 Ripasso Parte1|il riepilogo della prima parte]].

## Lo scudo fiscale e l'effetto sui flussi di cassa

Lo **scudo fiscale** (*tax shield*, t.s.) è il risparmio d'imposta che deriva dalla deducibilità degli oneri finanziari dal reddito imponibile:

$$t.s. = \text{Oneri finanziari} \times t_c$$

> [!example] Esempio
> Un'azienda ha un EBIT di 83.000, oneri finanziari di 22.000 e un carico fiscale del 27,9%. Le imposte calcolate sull'EBIT sono $83.000 \times 27{,}9\% = 23.157$; le imposte d'esercizio, calcolate sull'EBT di 61.000, sono $61.000 \times 27{,}9\% = 17.019$. La differenza, 6.138, è lo scudo fiscale: $22.000 \times 27{,}9\% = 6.138$.

L'effetto sui flussi di cassa è il seguente.

Il flusso della gestione operativa (FCFF) è calcolato con le imposte sull'EBIT, cioè come se l'impresa non avesse debito, e non include lo scudo. Il passaggio al FCFE sottrae gli oneri finanziari e somma lo scudo: l'onere effettivo del debito è quindi $\text{Oneri finanziari} \times (1-t_c)$ e il flusso disponibile per gli azionisti è maggiore di quello che si avrebbe senza deducibilità. In steady state il FCFF coincide con il NOPAT e il FCFE con il reddito di bilancio, per cui $NOPAT - \text{Oneri finanziari} + \text{scudo} = \text{reddito netto}$; nell'esempio $59.843 - 22.000 + 6.138 = 43.981$.

Lo scudo agisce anche sul tasso di sconto e sul valore. Nel WACC il costo del debito compare al netto delle imposte, $r_D(1-t_c)$. Nel modello del valore attuale modificato il valore dell'impresa indebitata è la somma del valore unlevered e del valore attuale dello scudo; per un debito $D$ costante e perpetuo, con oneri finanziari $D \cdot r_D$ scontati al tasso $r_D$, il valore dello scudo è

$$V_{TS} = \frac{D \cdot r_D \cdot t_c}{r_D} = D \cdot t_c \qquad\qquad V = V_U + V_{TS}$$

Lo sviluppo del modello, anche in crescita costante, è in [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|il modello del valore attuale modificato]].

## Il fondamento della valutazione assoluta

La valutazione assoluta è focalizzata sull'impresa considerata in sé e non sul confronto con altre. Si fonda su tre elementi: l'analisi delle caratteristiche dell'impresa (modello di business, strategie, management, patrimonio), la previsione dei suoi flussi economico-finanziari futuri e la misura del rischio operativo e finanziario, che determina il tasso di attualizzazione. Il significato economico dei risultati poggia sul principio di convenienza economica dell'investimento in capitale di rischio aziendale: il valore intrinseco è il valore attuale dei flussi che l'impresa è attesa produrre. La definizione generale è in [[FSTR 13 Ripasso Parte1|il riepilogo della prima parte]].

## I metodi DCF: modelli sintetici e analitici

I metodi DCF si applicano in due modi, che valgono sia nell'ottica assets sia nell'ottica equity.

| Modello sintetico | Modello analitico |
|---|---|
| Il valore si ottiene con formule compatte, che ipotizzano flussi costanti (steady state) o crescenti a un tasso costante $g$ (steady growth). | Il valore è la somma di un valore ricavato da un piano esplicito di 3-7 anni e di un terminal value attualizzato, calcolato con un metodo sintetico. |

Di norma si utilizza il modello analitico, che mostra il suo vantaggio nei periodi di discontinuità, per esempio grandi investimenti pluriennali o riduzione del debito, in cui i flussi non sono né costanti né crescenti a tasso costante.

Quando la società fornisce un piano industriale si procede con il modello analitico. Il piano viene anzitutto rivisto e se ne analizza la sostenibilità, attività che rientra nella financial due diligence. Si prendono poi i flussi dell'orizzonte esplicito, FCFF nell'ottica assets e FCFE nell'ottica equity, e si attualizzano al WACC o al costo dell'equity. A questi si aggiunge il valore attuale del terminal value, che rappresenta i flussi successivi all'ultimo anno del piano:

$$V = \sum_{t=1}^{N} \frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^N} \qquad E = \sum_{t=1}^{N} \frac{FCFE_t}{(1+r_E)^t} + \frac{TV}{(1+r_E)^N}$$

Il terminal value si calcola in ottica assets come rendita perpetua del risultato dell'ultimo anno, eventualmente normalizzato: $TV = NOPAT/WACC$ in steady state e

$$TV = \frac{NOPAT(1+g) - CINO \cdot g}{WACC - g}$$

con flussi crescenti al tasso $g < WACC$. In ottica equity si usano il reddito netto e il costo dell'equity, con il capitale proprio al posto del $CINO$. Se la valutazione parte dall'EV, l'equity value si ottiene sottraendo la PFN. Un peso del terminal value superiore all'85-90% del valore complessivo segnala possibili errori nei flussi espliciti, un orizzonte esplicito troppo breve o l'inutilità della stima analitica. Il calcolo e la verifica del peso sono sviluppati in [[FSTR 05 Annotazioni sul Terminal Value|il terminal value e il suo peso sul valore]] e in [[FSTR 04-full Modelli Valutazione Finanziaria Parte2|i modelli DCF analitici]].

### La durata limitata dell'azienda

La prassi valutativa assume una durata illimitata e assimila l'impresa a una rendita perpetua. Si ipotizza invece una durata limitata quando l'operatività è soggetta a limiti oggettivi:

| Natura del limite | Casi |
|---|---|
| normativa | imprese in regime di autorizzazione o di concessione, come reti autostradali e pubblici servizi |
| ambientale | attività basate sullo sfruttamento di risorse naturali, come cave, miniere e giacimenti |
| giuridica | soggetti con vita limitata per statuto, come joint venture, associazioni in partecipazione, reti d'imprese e consorzi |

Può portare a ipotizzare una durata limitata anche una ragione economica, cioè la scarsa rinnovabilità delle risorse distintive e delle capacità competitive. In questi casi è più corretto inserire nella valutazione il valore di liquidazione dell'azienda al termine del periodo previsto, e il valore terminale assume uno di due significati: contabile, se dipende dai valori contabili di attività e passività a quella data, oppure di liquidazione, se è funzione dei valori di cessione delle attività e di estinzione delle passività.

### I modelli multi-step

Una crescita del business superiore a quella generale dell'economia è difficile da mantenere a lungo, perché prima o poi ogni business giunge alla maturità. Lo stesso vale per una crescita dell'impresa superiore a quella del proprio business, che presuppone insieme un forte vantaggio competitivo, investimenti ingenti, concorrenti incapaci di reagire e barriere all'entrata che scoraggino nuovi ingressi. I **modelli multi-step** sostituiscono la crescita perpetua a un unico tasso con una crescita che cambia per fasi.

Nel modello a due stadi una fase iniziale di crescita superiore alla normalità, al tasso $g^h$, è seguita da una fase di crescita al tasso normale sostenibile nel lungo periodo, $g^{lt}$. Si adatta a imprese con vantaggi peculiari, come brevetti o barriere all'entrata, destinati a svanire dopo un periodo limitato. Il modello a tre stadi aggiunge una fase di transizione tra le due: nel periodo iniziale i ricavi crescono rapidamente con margini elevati, dividendi contenuti e investimenti attraenti, nella transizione la crescita, i margini e le opportunità di investimento diminuiscono mentre il pay out sale, nel periodo finale la crescita è stabile e pay out e ROE restano costanti.

## Il multiplo P/E e la comparabilità

Il **P/E** (*Price/Earnings*) è il rapporto tra il prezzo di mercato di un'azione e l'utile per azione, o tra la capitalizzazione di borsa e gli utili. Indica quante volte l'utile è contenuto nel valore che il mercato attribuisce all'impresa. Un P/E elevato segnala che il mercato è disposto a pagare molto per il livello attuale degli utili, perché ne attende la crescita. Se gli utili restano costanti, il P/E è anche il numero di anni di utili necessari per recuperare il prezzo pagato: con un P/E pari a 5 servono cinque anni. Applicato a un utile di 100.000, quel multiplo dà un equity value di 500.000.

La comparabilità tra l'impresa da valutare e il campione presenta criticità che si leggono nella relazione che lega il P/E alle sue determinanti, ricavata dal modello di Gordon:

$$\frac{P}{EPS} = \frac{1-b}{r_0 + (r_0 - r_D)(1-t_c)\dfrac{D}{E} - ROE \cdot b}$$

dove $b$ è la quota di utili reinvestita. Ogni termine corrisponde a una fonte di difformità tra le imprese.

| Termine | Fonte di difformità |
|---|---|
| $EPS$ | regole contabili, che determinano l'utile |
| $r_0$ e $r_0 - r_D$ | rischio operativo (leva operativa) |
| $(1-t_c)$ | profili fiscali |
| $D/E$ | rischio finanziario (leva finanziaria) |
| $ROE \cdot b$ | crescita e redditività |

Le criticità di comparabilità sono quindi cinque: crescita e redditività, leva finanziaria, leva operativa, principi contabili e profili fiscali. Si aggiungono le criticità del singolo multiplo: proventi e oneri straordinari, investimenti extra, crediti fiscali, perdite e bilanci consolidati. I rimedi, che comprendono la scelta di comparable dello stesso paese e le *value maps*, sono in [[FSTR 07 Multipli di Borsa lez02|le criticità dei multipli e i rimedi]].

## Il valore delle operazioni di integrazione

### Tipi di integrazione

Sotto il profilo industriale le fusioni e le integrazioni si distinguono in tre tipi. L'integrazione **orizzontale** riunisce imprese della stessa linea di business. Nell'integrazione **verticale** un'impresa estende il proprio controllo a monte, verso le materie prime, o a valle, verso il consumatore finale. L'integrazione **conglomerale** coinvolge imprese di settori non correlati. Sotto il profilo giuridico, invece, la fusione per unione dà vita a una società nuova, la fusione per incorporazione lascia sopravvivere la sola incorporante e l'acquisto di azioni mantiene distinte le due società. Casi reali sono raccolti in [[FSTR 10 Esempi di Sinergie|gli esempi di integrazione industriale e giuridica]].

### Il valore di acquisizione

Il **valore di acquisizione** è il valore che l'impresa target ha per l'acquirente. È formato dal valore *stand alone*, cioè dai flussi di cassa che l'impresa genera da sola scontati al tasso di rendimento, e dal valore delle sinergie, cioè dei flussi differenziali che l'acquisizione rende ottenibili:

$$W_{acq} = W_S + W_D$$

Le sinergie hanno effetto sui flussi (sinergie operative), sul costo del capitale (sinergie finanziarie) e sugli scudi fiscali (sinergie fiscali). Il modello di stratificazione del valore le quantifica sommando il valore dei flussi incrementali, il valore del debito incrementale, cioè del maggiore scudo fiscale, e il valore della modifica del costo del capitale. Se si acquista una quota di controllo $\alpha$ e non l'intero capitale, al valore si aggiungono i benefici privati, che spettano solo a chi controlla:

$$W_\alpha = (W_S + W_{DIV})\,\alpha + W_{IND}$$

dove $W_{DIV}$ è il valore delle sinergie divisibili, ripartite in proporzione alla quota, e $W_{IND}$ quello dei benefici indivisibili, che vanno per intero a chi controlla. La valutazione di un'acquisizione si completa confrontando il valore con il prezzo: $NPV = W_{acq} - P_{pagato}$. La creazione di valore dipende da questo confronto e non dall'utile contabile dopo l'integrazione. Sinergie e stratificazione sono sviluppate in [[FSTR 11 Le Sinergie|le sinergie e i benefici privati]] e in [[FSTR 12 Valutazione Operazioni di Integrazione|la valutazione delle operazioni di integrazione]].

### I benefici privati

I **benefici privati** sono flussi di cui godono gli azionisti-manager di controllo. Si distinguono in due tipi a seconda dell'effetto sui flussi *stand alone* della società: quelli con effetto, che riducono i flussi, per esempio con remunerazioni più elevate degli standard di mercato ($W_{PB}$), e quelli senza effetto sui flussi aziendali, per esempio quando le risorse intangibili della società sono usate per sviluppare altri business non legati a essa ($W_{PB^*}$). Con questa distinzione il valore di una quota di controllo si scrive anche

$$W_\alpha = (W_S + W_D)\,\alpha + W_{PB^*} + (1-\alpha)\,W_{PB}$$

Il valore dei benefici privati con effetto sui flussi è sottratto dal valore ripartibile tra tutti gli azionisti e assegnato per intero a chi controlla.

### Il premio di controllo

Il **premio di controllo** è l'aggiustamento del valore di acquisizione che riflette i benefici del controllo, quando l'acquisizione di una partecipazione consente di controllare la società. È determinato dai benefici privati, monetari e non monetari, come il potere di decidere gli indirizzi strategici e la quotazione in Borsa. Nel modello della quota di controllo questi benefici confluiscono in $W_{IND}$, e per questo il valore unitario delle azioni cresce al diminuire della quota acquisita.

> [!example] Esempio
> Siano $W_S = 180$, $W_{DIV} = 20$, $W_{IND} = 65$ (milioni) e $N = 100$ azioni. Con il 100% del capitale $W = 180 + 20 + 65 = 265$ e il valore per azione è $2{,}65$. Con il 60% $W = 180 \times 0{,}6 + 20 \times 0{,}6 + 65 = 185$ e il valore per azione è $185/60 = 3{,}083$: il valore indivisibile si distribuisce su un numero minore di azioni.

Per le quote di minoranza vale invece lo **sconto di minoranza**, dovuto all'impossibilità di decidere gli indirizzi strategici e alla minore liquidità della partecipazione.

### Valide ragioni e criticità di una fusione

Tre ragioni economicamente valide per una fusione sono le economie di scala, le economie di integrazione verticale e la combinazione di risorse complementari. Le economie di scala riducono i costi medi unitari, perché i costi fissi si distribuiscono su una produzione maggiore. L'integrazione verticale, a monte o a valle, riduce i costi e aumenta l'efficienza quando due attività sono strettamente collegate. La combinazione di risorse complementari completa ciò che manca alle imprese coinvolte, come un'impresa con un prodotto esclusivo e un'altra con la rete distributiva. Un'ulteriore ragione è l'eccesso di fondi nelle imprese mature con pochi progetti a VAN positivo, per le quali l'acquisizione può essere un'alternativa all'impiego interno della liquidità.

Le criticità di un'operazione di fusione riguardano il prezzo, la tenuta delle sinergie, il concambio e le motivazioni.

Il premio pagato sopra il valore *stand alone* del target non dovrebbe superare il valore complessivo delle sinergie attese, fiscali, operative e finanziarie: oltre quel limite l'acquisizione ha NPV negativo e distrugge valore per gli azionisti dell'acquirente. Le sinergie, inoltre, si stimano con difficoltà crescente passando dai flussi incrementali al debito incrementale e alla modifica del costo del capitale, e possono ridursi dopo l'operazione. Nell'esempio di [[FSTR 11 Le Sinergie|il valore nelle operazioni di integrazione]] la sostituzione del management porta alla perdita di alcuni clienti: i flussi da sinergie scendono da 50 a 40 e il valore di acquisizione da 1.625 a 1.500.

Nella fusione per incorporazione il rapporto di concambio, che è un prezzo negoziato tra le parti, deve collocarsi tra un valore minimo, che tutela gli azionisti dell'incorporata, e un valore massimo, che tutela quelli dell'incorporante ([[FSTR 12 Valutazione Operazioni di Integrazione|il rapporto di concambio massimo e minimo]]).

Una motivazione dubbia è la diversificazione: è più facile da ottenere per l'azionista, che può diversificare da solo il proprio portafoglio, e gli investitori non pagano un premio per le società diversificate, anzi applicano uno sconto di gruppo. Possono infine emergere dalla due diligence elementi critici, in particolare i *deal breakers*, che fanno fallire l'operazione.

## La due diligence e la normalizzazione di EBITDA e PFN

### Perché si normalizzano

Con il metodo dei multipli l'enterprise value è dato da $EBITDA \times \text{multiplo}$ e l'equity value, cioè il prezzo, da $EV - PFN$. L'attenzione della due diligence si concentra perciò su due grandezze: un EBITDA sovrastimato fa salire l'enterprise value, e una PFN sottostimata fa salire il prezzo. Gli esempi numerici completi sono in [[FSTR 08 Financial Due Diligence|la normalizzazione di EBITDA e PFN nella financial due diligence]].

### La normalizzazione dell'EBITDA

**Normalizzare** l'EBITDA significa eliminare dalla redditività d'esercizio gli elementi eccezionali per loro natura o estranei al core business, positivi o negativi, per ottenere un livello di redditività sostenibile nel tempo e utilizzabile nei modelli di valutazione. Gli elementi interessati sono quelli non ricorrenti o straordinari, le politiche di bilancio come le capitalizzazioni e i costi e ricavi collocati in modo non corretto, come le spese bancarie. Ogni rettifica positiva aumenta l'EBITDA e ogni rettifica negativa lo riduce.

> [!example] Esempio
> Da un EBITDA civilistico di 439.712 si sommano 100.000, la buonuscita pagata a un amministratore e registrata tra i costi per servizi: è un costo non ricorrente, e la rettifica è positiva. Si sottraggono invece 161.000, il rilascio di un fondo accantonato per una causa poi vinta: è un provento non di competenza dell'esercizio, e la rettifica è negativa. Un'altra rettifica negativa è quella dei contributi in conto esercizio per 31.749, ricavi non ricorrenti e non inerenti. Con queste sole tre rettifiche l'EBITDA passa a $439.712 + 100.000 - 161.000 - 31.749 = 346.963$; il quadro completo ne comprende altre.

### La normalizzazione della PFN

La PFN è la differenza tra i debiti finanziari, non solo bancari, e le disponibilità liquide. **Normalizzarla** significa fare in modo che rappresenti il reale indebitamento dell'azienda: ai debiti finanziari contabili si aggiungono i *debt-like items*, cioè le passività di natura finanziaria che il bilancio non classifica come debiti finanziari, e dalle disponibilità liquide si escludono le voci che non sono liquidità, come i conti con vincoli allo smobilizzo, i titoli, le partecipazioni e i crediti finanziari. Tutte le rettifiche aumentano la PFN, e a parità di enterprise value riducono l'equity value dello stesso importo.

> [!example] Esempio
> La PFN civilistica è $18.234.663 + 220 - 8.786.219 = 9.448.664$. Si aggiungono 360.000 di ricevute bancarie presentate e non ancora incassate, che sono un credito e non liquidità; 55.000 accantonati per una controversia in cui la società è stata condannata in primo grado; 77.000 di scaduto verso i fornitori oltre 180 giorni, che supera la dilazione fisiologica; 155.000 di buonuscita a un ex dirigente, da pagare in rate semestrali, che è un debito finanziario iscritto tra gli altri debiti del capitale circolante. La PFN rettificata è $9.448.664 + 360.000 + 55.000 + 77.000 + 155.000 = 10.095.664$, cioè 647.000 in più.

### Le fasi di un deal

Un processo di acquisizione si articola in nove fasi, descritte in [[FSTR 09 La Due Diligence|le fasi del processo di acquisizione]].

| Fase | Contenuto |
|---|---|
| 1. Targeting | selezione della società target in base a dimensione, marginalità, modello di business, posizionamento, distribuzione, brand |
| 2. Contatti preliminari | descrizione sintetica della target in un teaser anonimo e sottoscrizione di un accordo di riservatezza (NDA) |
| 3. Non binding offer (NBO) | offerta non vincolante che riassume i principali accordi tra venditore e acquirente, senza impegnare le parti |
| 4. Lettera di intenti (LOI) | contratto preliminare con cui le parti si impegnano a concludere l'operazione dopo la due diligence |
| 5. Due diligence | investigazione e analisi delle peculiarità e delle criticità della target |
| 6. Negoziazione | discussione delle evidenze della due diligence e fissazione del prezzo finale |
| 7. Signing | firma del contratto definitivo, con prezzo, clausole, assetti societari, garanzie, patti di non concorrenza ed *earn out* |
| 8. Financing | definizione del finanziamento, con apporto di capitale dei soci o ricorso al capitale di terzi |
| 9. Closing | trasferimento delle quote o azioni e pagamento del prezzo |

La due diligence si articola a sua volta in cinque passaggi: ricevimento dell'incarico e definizione dello *scope of work*, invio di una check-list dei documenti, raccolta delle informazioni, analisi dei rischi e delle criticità, redazione del report, la cui sintesi è l'*executive summary* e che in presenza di fatti critici importanti può essere accompagnato da un *red flag report*.
