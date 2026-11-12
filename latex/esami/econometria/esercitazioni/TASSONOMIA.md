# Tassonomia dei tipi di domanda — Econometria EM0004

Perimetro di copertura delle esercitazioni. Generata il 2026-11-12 da un agente `opus-synthesizer` che ha letto i 70 quesiti dei sette appelli, i loro testi originali, le note ECON 01–07 e i tre ripassi di statistica; poi **controllata meccanicamente**: il JSON è valido, ogni occorrenza esiste come `## Domanda N` nel suo `ECON_Sol_*.md`, ogni quesito dei 70 appartiene ad almeno un tipo, non ci sono id duplicati e le quattro combinazioni d'appello usano solo tipi esistenti e coprono tutti i tipi `appello`.

Origini dei tipi (66 in tutto):

- `appello` (31): genere di domanda trovato nei 70 quesiti. Servono **almeno 2 esercizi, di cui 1 di livello 3**.
- `ripasso` (16): argomento dei tre ripassi di statistica del docente (modulo 0). Serve almeno 1 esercizio.
- `corso` (19): competenza insegnata dalle note o dalla soluzione ufficiale del 16/01/2024 ma mai chiesta nei 70 quesiti, aggiunta da Claude dopo la tassonomia (campo `fonte`). I moduli 01 e 02 nascono quasi solo da qui. Serve almeno 1 esercizio.

## Convenzioni fissate (valgono per ogni esercizio)

1. **Valori critici.** Il testo dell'esercizio li dà sempre come parametri, mai da sapere a memoria, salvo i quantili normali che i veri appelli fissano in una nota iniziale: 1,96 (bilaterale 5%), 1,64 (unilaterale 5%, come in 2022-12-22 D1; non l'1,96 del ripasso 03, che per il test unilaterale al 5% contraddice i testi), 2,57 (1%). Per Dickey-Fuller si usano i valori dei testi, −2,38 e −3,43; per Engle-Granger si preferisce il p-value, come in 5 appelli su 7, e −1,95 solo come nel 15/06/2023 D8. I testi non dicono con quale specificazione vanno letti: ogni statistica deve quindi stare a più del 15% dal valore critico, così la decisione non dipende dalla convenzione.
2. **Segno dell'ECM.** Come nei testi: Δy = … + λ·ecm(−1) con λ stimato negativo. Non la convenzione −α con α>0 delle note (ECON 07 righe 290–310).
3. **Tabelle.** Formato uniforme gretl: 6 cifre significative per coefficienti ed errori standard, 4 per la t, p-value a 4 decimali (o notazione scientifica a 3 cifre sotto 1e-4), virgola decimale. Le irregolarità dei testi veri (colonne a 5 cifre, punto decimale, t non coerente con coef/se) non si replicano.
4. **Appelli simulati.** L'appello N usa la combinazione N di `combinazioni_appelli`: 6 domande di cross-section e 4 di serie storiche, come 5 appelli su 7.
5. **Lacune delle note.** Modelli log-livello e log-log, elasticità, quadratici, interazioni, VIF e ARMA non compaiono in ECON 01–07. Una soluzione che le usa deve derivare la formula dai due mattoni del corso (ΔY=βΔX e la varianza di una combinazione lineare) e la derivazione va verificata numericamente in `ex.py`. Non si citano righe delle note che non esistono.
6. **Errori noti da non copiare.** ECON 07 righe 216, 324 e 326 (le soluzioni su assorbimento e direzione dell'ECM non si ricavano da lì). La contraddizione ECON 06 sulla varianza dell'MA(1) non c'è più: la varianza giusta è (1+θ²)σ².
7. **Incoerenze dei testi veri da non riprodurre.** 2025-01-21 D7 dà p-value 0,001 e 0,022 e D8–D10 procedono comunque con Engle-Granger ed ECM; 2023-08-29 D9 valuta un ECM dopo p-value di cointegrazione alti; 2023-01-17 D6 chiede l'errore standard di β2+β3 senza dare la covarianza (qui la covarianza va sempre data nel testo).
8. **Domande ambigue.** «Riduca del 2%» e «migliore del 25%» (2023-06-15 D4, 2023-08-29 D5) ammettono letture unilaterale e bilaterale: negli esercizi l'ipotesi è sempre dichiarata nel testo.

Il rapporto completo dell'agente (classificazioni difficili, tabelle riciclate fra appelli) non è conservato: le decisioni che toccano gli esercizi sono le otto sopra.

## Dati (JSON)

```json
{
 "tipi": [
  {
   "id": "variazione-percentuale-log-livello",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Tradurre il coefficiente di un regressore, anche dummy, di un modello log-livello nella variazione percentuale attesa della dipendente per una variazione data del regressore, o ricavare la variazione del regressore necessaria per un obiettivo percentuale.",
   "occorrenze": [
    "2022-12-22:D1",
    "2022-12-22:D2",
    "2023-01-17:D6",
    "2023-06-15:D4",
    "2023-08-29:D1",
    "2023-08-29:D5",
    "2023-12-21:D1",
    "2023-12-21:D2",
    "2023-12-21:D6",
    "2024-06-13:D5",
    "2025-01-21:D1"
   ]
  },
  {
   "id": "test-unilaterale-su-soglia",
   "modulo": 2,
   "origine": "appello",
   "descrizione": "Formulare H0 e H1 unilaterali per un'affermazione del tipo «almeno», «superiore a», «meno di» (soglia anche non nulla, riportata sul coefficiente) e decidere con la statistica t al livello indicato.",
   "occorrenze": [
    "2022-12-22:D2",
    "2023-01-17:D6",
    "2023-08-29:D1",
    "2023-12-21:D6",
    "2024-06-13:D1",
    "2024-06-13:D5",
    "2025-01-21:D1"
   ]
  },
  {
   "id": "test-su-valore-specifico",
   "modulo": 2,
   "origine": "appello",
   "descrizione": "Verificare se un coefficiente, o un suo multiplo, è compatibile con un valore puntuale non nullo indicato dal testo, con la statistica t costruita come (stima - valore)/errore standard.",
   "occorrenze": [
    "2023-06-15:D4",
    "2023-06-15:D10",
    "2023-08-29:D5",
    "2023-12-21:D2",
    "2023-12-21:D9",
    "2025-01-21:D3"
   ]
  },
  {
   "id": "ic-per-verificare-un-valore",
   "modulo": 2,
   "origine": "appello",
   "descrizione": "Costruire un intervallo di confidenza al 95% per un coefficiente o per una differenza di coefficienti e usarlo per giudicare la plausibilità di un valore o la significatività della differenza.",
   "occorrenze": [
    "2022-12-22:D1",
    "2025-01-21:D4"
   ]
  },
  {
   "id": "dummy-categoria-base",
   "modulo": 4,
   "origine": "appello",
   "descrizione": "Riconoscere la categoria di riferimento di un gruppo di dummy, interpretare i coefficienti rispetto a essa e spiegare perché una dummy viene o non viene eliminata (trappola delle dummy, modello senza costante).",
   "occorrenze": [
    "2022-12-22:D3",
    "2024-06-13:D1",
    "2025-01-21:D2"
   ]
  },
  {
   "id": "sistema-ipotesi-f-dummy-congiunte",
   "modulo": 4,
   "origine": "appello",
   "descrizione": "Scrivere il sistema d'ipotesi congiunto da verificare con un test F per stabilire se un fattore qualitativo codificato con più dummy ha rilevanza nel modello.",
   "occorrenze": [
    "2022-12-22:D3",
    "2024-06-13:D2",
    "2025-01-21:D5"
   ]
  },
  {
   "id": "differenza-tra-profili-combinazione-lineare",
   "modulo": 4,
   "origine": "appello",
   "descrizione": "Esprimere la differenza attesa fra due unità con caratteristiche date come combinazione lineare dei coefficienti, calcolarne la stima puntuale e impostarne la verifica d'ipotesi, anche usando la covarianza fra stimatori.",
   "occorrenze": [
    "2023-01-17:D7",
    "2023-06-15:D2",
    "2023-08-29:D3",
    "2025-01-21:D4"
   ]
  },
  {
   "id": "termine-quadratico-nonlinearita",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Verificare la significatività del termine al quadrato per decidere sulla linearità della relazione e stabilire se l'effetto marginale è crescente o decrescente.",
   "occorrenze": [
    "2022-12-22:D4",
    "2023-01-17:D10",
    "2023-06-15:D1",
    "2024-06-13:D3"
   ]
  },
  {
   "id": "punto-di-svolta-quadratico",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Calcolare il valore del regressore in cui l'effetto marginale di una specificazione quadratica si annulla, cioè il massimo o minimo della dipendente attesa.",
   "occorrenze": [
    "2022-12-22:D4",
    "2024-06-13:D6"
   ]
  },
  {
   "id": "interazione-effetto-marginale-condizionato",
   "modulo": 4,
   "origine": "appello",
   "descrizione": "Derivare l'effetto marginale di un regressore che compare in un termine d'interazione, valutarlo a un livello dato dell'altra variabile e decidere se dipende da essa.",
   "occorrenze": [
    "2023-01-17:D6",
    "2023-01-17:D7",
    "2023-06-15:D2",
    "2023-06-15:D3",
    "2023-08-29:D3",
    "2023-08-29:D4"
   ]
  },
  {
   "id": "elasticita-log-log",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Leggere il coefficiente di un regressore in logaritmo come elasticità e tradurre una variazione percentuale del regressore nella variazione percentuale attesa della dipendente.",
   "occorrenze": [
    "2023-06-15:D3",
    "2025-01-21:D3"
   ]
  },
  {
   "id": "unita-di-misura-e-scala",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Tenere conto delle unità di misura (dollari contro percentuali in un modello in logaritmi, punti base) prima di confrontare un'affermazione del testo con un coefficiente.",
   "occorrenze": [
    "2023-06-15:D10",
    "2023-12-21:D2"
   ]
  },
  {
   "id": "collinearita-diagnosi",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Decidere se c'è quasi-collinearità e se spiega la non significatività di un coefficiente, dai VIF o dal confronto degli errori standard fra due modelli.",
   "occorrenze": [
    "2022-12-22:D5",
    "2023-06-15:D6",
    "2023-12-21:D5"
   ]
  },
  {
   "id": "vif-inflazione-errore-standard",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Quantificare di quanto aumenta l'errore standard di un coefficiente rispetto al caso di regressori indipendenti, come radice quadrata del VIF.",
   "occorrenze": [
    "2022-12-22:D5",
    "2023-08-29:D6"
   ]
  },
  {
   "id": "endogeneita-variabile-omessa",
   "modulo": 3,
   "origine": "appello",
   "descrizione": "Confrontare le stime prima e dopo l'aggiunta di un regressore per giudicare se il modello ristretto soffre di distorsione da variabile omessa, cioè di endogeneità.",
   "occorrenze": [
    "2023-01-17:D9",
    "2023-12-21:D4"
   ]
  },
  {
   "id": "eteroschedasticita-grafico-residui",
   "modulo": 5,
   "origine": "appello",
   "descrizione": "Giudicare omoschedasticità o eteroschedasticità dal grafico dei residui contro i valori predetti.",
   "occorrenze": [
    "2023-01-17:D8",
    "2023-12-21:D3",
    "2025-01-21:D6"
   ]
  },
  {
   "id": "test-eteroschedasticita",
   "modulo": 5,
   "origine": "appello",
   "descrizione": "Interpretare un test di eteroschedasticità (White, Breusch-Pagan o regressione ausiliaria dei residui al quadrato) da statistica e p-value, anche quando due test danno esiti diversi.",
   "occorrenze": [
    "2023-06-15:D5",
    "2023-08-29:D2",
    "2024-06-13:D4"
   ]
  },
  {
   "id": "eteroschedasticita-implicazioni",
   "modulo": 5,
   "origine": "appello",
   "descrizione": "Distinguere che cosa l'eteroschedasticità implica e che cosa no: non dice nulla su E[eps|X], e un grafico compatibile con l'omoschedasticità non basta a escludere gli errori standard robusti.",
   "occorrenze": [
    "2023-08-29:D2",
    "2023-12-21:D3"
   ]
  },
  {
   "id": "adf-specificazione-regressione",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Scrivere la regressione di Dickey-Fuller, eventualmente aumentata, adatta alla serie, scegliendo le componenti deterministiche dal grafico, insieme al sistema d'ipotesi.",
   "occorrenze": [
    "2023-01-17:D1",
    "2023-06-15:D7",
    "2023-12-21:D7"
   ]
  },
  {
   "id": "adf-lettura-output-regressione",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Individuare nell'output di una regressione ADF la statistica sul livello ritardato e decidere sulla radice unitaria.",
   "occorrenze": [
    "2022-12-22:D6",
    "2023-12-21:D8"
   ]
  },
  {
   "id": "adf-decisione-statistica-o-pvalue",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Decidere se una serie ha trend stocastico (radice unitaria, comportamento da random walk) confrontando la statistica ADF con il valore critico dato o usando il p-value.",
   "occorrenze": [
    "2023-01-17:D2",
    "2023-06-15:D8",
    "2023-06-15:D10",
    "2023-08-29:D7",
    "2023-12-21:D9",
    "2024-06-13:D7",
    "2025-01-21:D7"
   ]
  },
  {
   "id": "stazionarieta-da-correlogramma",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Giudicare la stazionarietà di una serie, o dei residui di una relazione di lungo periodo, dalla forma di ACF e PACF.",
   "occorrenze": [
    "2022-12-22:D7",
    "2024-06-13:D10",
    "2025-01-21:D10"
   ]
  },
  {
   "id": "identificazione-ar-ma-arma",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Proporre un modello AR, MA o ARMA dall'andamento di ACF e PACF rispetto alle bande di significatività.",
   "occorrenze": [
    "2023-01-17:D5",
    "2024-06-13:D10",
    "2025-01-21:D10"
   ]
  },
  {
   "id": "break-strutturale-qlr",
   "modulo": 6,
   "origine": "appello",
   "descrizione": "Interpretare il p-value del test QLR per break strutturali a data ignota e decidere se i break sono un problema per la regressione.",
   "occorrenze": [
    "2024-06-13:D9"
   ]
  },
  {
   "id": "cointegrazione-decisione",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Decidere se due serie integrate sono cointegrate dal test di Engle-Granger sui residui della relazione di lungo periodo (statistica con valore critico, o p-value) oppure dal correlogramma di quei residui.",
   "occorrenze": [
    "2022-12-22:D7",
    "2023-01-17:D2",
    "2023-06-15:D8",
    "2023-08-29:D8",
    "2023-12-21:D9",
    "2024-06-13:D8",
    "2025-01-21:D8"
   ]
  },
  {
   "id": "regressione-statica-ben-definita",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Giudicare se una regressione statica fra livelli è ben definita, o se un esito di cointegrazione è credibile, dati gli ordini d'integrazione delle serie.",
   "occorrenze": [
    "2023-06-15:D10",
    "2024-06-13:D8"
   ]
  },
  {
   "id": "inferenza-coefficiente-lungo-periodo",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Verificare un'affermazione sul coefficiente della relazione di lungo periodo, stimata con OLS o DOLS, dopo aver stabilito che la relazione è ben definita.",
   "occorrenze": [
    "2023-06-15:D10",
    "2023-12-21:D9"
   ]
  },
  {
   "id": "ecm-ben-definito",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Giudicare se un modello a correzione dell'errore è bilanciato e ben definito alla luce dei test di radice unitaria e di cointegrazione e del coefficiente di aggiustamento stimato.",
   "occorrenze": [
    "2022-12-22:D8",
    "2023-01-17:D3",
    "2023-08-29:D9",
    "2025-01-21:D9"
   ]
  },
  {
   "id": "ecm-rispecificazione-da-residui",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Decidere dal correlogramma dei residui dell'ECM se va ri-specificata la dinamica di breve o quella di lungo periodo.",
   "occorrenze": [
    "2022-12-22:D9",
    "2023-01-17:D3"
   ]
  },
  {
   "id": "ecm-direzione-aggiustamento",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Prevedere, dal segno del disequilibrio e del coefficiente di aggiustamento, se la dipendente crescerà più o meno velocemente dell'altra serie nei periodi successivi.",
   "occorrenze": [
    "2023-01-17:D4",
    "2023-06-15:D9",
    "2023-08-29:D10"
   ]
  },
  {
   "id": "ecm-velocita-assorbimento",
   "modulo": 7,
   "origine": "appello",
   "descrizione": "Calcolare dal coefficiente di aggiustamento dell'ECM in quanti periodi viene riassorbita una quota data del disequilibrio, con regressore costante e shock nulli.",
   "occorrenze": [
    "2022-12-22:D10",
    "2023-08-29:D9",
    "2023-12-21:D10",
    "2025-01-21:D9"
   ]
  },
  {
   "id": "associazione-variabili-categoriche",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Leggere una tabella di contingenza, ricavare le distribuzioni condizionate e decidere se due variabili categoriche sono statisticamente indipendenti.",
   "occorrenze": []
  },
  {
   "id": "covarianza-e-sue-proprieta",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Calcolare e interpretare la covarianza campionaria e di popolazione e usarne le proprietà (simmetria, cov(aX,bY)=ab cov(X,Y), invarianza alle traslazioni).",
   "occorrenze": []
  },
  {
   "id": "correlazione-e-indipendenza",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Calcolare il coefficiente di correlazione, sapere che è compreso fra -1 e 1 e che l'indipendenza implica incorrelazione ma non viceversa.",
   "occorrenze": []
  },
  {
   "id": "media-e-varianza-di-una-somma",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Calcolare media e varianza di una somma di variabili, Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y), base per l'errore standard di una combinazione di stimatori.",
   "occorrenze": []
  },
  {
   "id": "campionamento-casuale-semplice",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Spiegare perché in un campione casuale semplice le osservazioni sono variabili casuali indipendenti con la stessa distribuzione della popolazione.",
   "occorrenze": []
  },
  {
   "id": "media-campionaria-correttezza-e-errore-standard",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Dimostrare che la media campionaria è corretta, ha varianza sigma^2/n ed è consistente (legge dei grandi numeri), e definirne l'errore standard.",
   "occorrenze": []
  },
  {
   "id": "teorema-del-limite-centrale",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Applicare il teorema del limite centrale per approssimare con una normale la distribuzione della media campionaria standardizzata.",
   "occorrenze": []
  },
  {
   "id": "intervallo-di-confidenza-per-la-media",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Costruire un intervallo di confidenza per la media con i quantili z (1,64, 1,96, 2,57) sostituendo sigma con la deviazione standard campionaria, e interpretarlo nel senso dei campioni ripetuti.",
   "occorrenze": []
  },
  {
   "id": "intervallo-di-confidenza-per-una-proporzione",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Stimare una proporzione come media di variabili Bernoulli e costruirne l'intervallo di confidenza con errore standard radice di p(1-p)/n.",
   "occorrenze": []
  },
  {
   "id": "logica-del-test-e-p-value",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Formulare ipotesi nulla e alternativa, distinguere errori di primo e secondo tipo, fissare il livello di significatività e decidere con il p-value.",
   "occorrenze": []
  },
  {
   "id": "test-unilaterali-e-bilaterali-sulla-media",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Impostare e risolvere i tre casi di test sulla media (alternativa maggiore, minore, diverso), con regione di rifiuto e p-value a una o due code.",
   "occorrenze": []
  },
  {
   "id": "distribuzione-t-e-piccoli-campioni",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Scegliere fra quantili normali e quantili della t di Student con n-1 gradi di libertà secondo la numerosità del campione.",
   "occorrenze": []
  },
  {
   "id": "test-su-una-proporzione",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Verificare un'ipotesi su una proporzione usando l'errore standard calcolato sotto l'ipotesi nulla.",
   "occorrenze": []
  },
  {
   "id": "confronto-tra-due-medie-campioni-indipendenti",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Confrontare le medie di due gruppi indipendenti con la statistica t sulla differenza, sapendo che Var(differenza) include -2Cov e che la sovrapposizione degli intervalli è solo un'indicazione.",
   "occorrenze": []
  },
  {
   "id": "confronto-tra-due-proporzioni",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Confrontare due proporzioni con la proporzione combinata stimata sotto l'ipotesi nulla di uguaglianza.",
   "occorrenze": []
  },
  {
   "id": "confronto-per-dati-appaiati",
   "modulo": 0,
   "origine": "ripasso",
   "descrizione": "Verificare l'effetto in un disegno a coppie appaiate con il test t sulla media delle differenze.",
   "occorrenze": []
  },
  {
   "id": "causalita-criteri-e-confutazione",
   "modulo": 1,
   "origine": "corso",
   "descrizione": "Applicare i criteri di causalità e il ruolo della confutazione, e riconoscere quando un'associazione non implica causalità (confondenti, causalità inversa).",
   "fonte": "ECON 01, «Causalità: definizione e criteri» e «Associazione non implica causalità»",
   "occorrenze": []
  },
  {
   "id": "tipi-di-dato-e-cause-di-problemi",
   "modulo": 1,
   "origine": "corso",
   "descrizione": "Classificare dati cross-section, serie storiche e panel e riconoscere le tre cause di problemi nella stima.",
   "fonte": "ECON 01, «Tipi di dato» e «Tre cause di problemi nella stima»",
   "occorrenze": []
  },
  {
   "id": "stima-ols-semplice",
   "modulo": 2,
   "origine": "corso",
   "descrizione": "Calcolare intercetta e pendenza OLS da medie, varianze e covarianza campionarie e interpretarle.",
   "fonte": "ECON 02, «Stima del modello: il metodo dei minimi quadrati ordinari»",
   "occorrenze": []
  },
  {
   "id": "proprieta-ols-gauss-markov",
   "modulo": 2,
   "origine": "corso",
   "descrizione": "Elencare le ipotesi OLS, distinguere non distorsione e consistenza, riconoscere l'ipotesi violata in un caso dato e dire che cosa garantisce Gauss-Markov.",
   "fonte": "ECON 02, «Le ipotesi del modello» e «Le proprietà degli stimatori OLS»",
   "occorrenze": []
  },
  {
   "id": "varianza-errore-standard",
   "modulo": 2,
   "origine": "corso",
   "descrizione": "Stimare la varianza dell'errore e l'errore standard di una pendenza da SSR, n e variabilità del regressore.",
   "fonte": "ECON 02, «Lo stimatore della varianza σ² e gli errori standard»",
   "occorrenze": []
  },
  {
   "id": "r2-anova",
   "modulo": 2,
   "origine": "corso",
   "descrizione": "Scomporre la devianza totale in spiegata e residua, calcolare e interpretare R² e leggere la tavola ANOVA.",
   "fonte": "ECON 02, «Misure di bontà di adattamento: l'R²»",
   "occorrenze": []
  },
  {
   "id": "errore-di-misura-endogeneita",
   "modulo": 3,
   "origine": "corso",
   "descrizione": "Spiegare perché un errore di misura nel regressore genera endogeneità anche se non è distorto, e che cosa ne segue per la stima.",
   "fonte": "ECON 03, «Cause di endogeneità: errori di misura»; soluzione ufficiale 2024-01-16",
   "occorrenze": []
  },
  {
   "id": "frisch-waugh-lovell",
   "modulo": 3,
   "origine": "corso",
   "descrizione": "Ottenere un coefficiente della regressione multipla con il regressore ausiliario (Frisch-Waugh-Lovell) e verificare la coincidenza numerica.",
   "fonte": "ECON 03, «Il teorema di Frisch-Waugh-Lovell (caso a due regressori)»",
   "occorrenze": []
  },
  {
   "id": "effetto-livello-log",
   "modulo": 3,
   "origine": "corso",
   "descrizione": "Modello con dipendente in livello e regressore in logaritmo: variazione attesa della dipendente per una variazione percentuale del regressore.",
   "fonte": "Soluzione ufficiale 2024-01-16 (ricchezza netta e log del reddito); formula derivata dai due mattoni ΔY=βΔX e Δlog X≈ΔX/X, non presente nelle note",
   "occorrenze": []
  },
  {
   "id": "test-f-calcolo-da-ssr",
   "modulo": 4,
   "origine": "corso",
   "descrizione": "Costruire la statistica F dal modello completo e da quello ristretto (SSR o R²), contare le restrizioni, decidere con il valore critico o il p-value.",
   "fonte": "ECON 04, «La statistica F: definizione» e «Proprietà del test F, regola di decisione e p-value»; nessuno dei 70 quesiti chiede il calcolo",
   "occorrenze": []
  },
  {
   "id": "test-su-combinazione-lineare-dei-coefficienti",
   "modulo": 4,
   "origine": "corso",
   "descrizione": "Verificare un vincolo su una somma di coefficienti (come β1+β5=κ con κ ricavato dal testo) con la t sulla combinazione, usando la covarianza fra gli stimatori, o con F.",
   "fonte": "ECON 04, «Restrizioni lineari: definizione generale»; soluzione ufficiale 2024-01-16",
   "occorrenze": []
  },
  {
   "id": "errori-standard-robusti",
   "modulo": 5,
   "origine": "corso",
   "descrizione": "Confrontare errori standard naïve e robusti di White, rifare t ed F con quelli robusti e dire se la decisione cambia.",
   "fonte": "ECON 05, «Stimatori robusti» e «Test robusti all'eteroschedasticità: t e F»",
   "occorrenze": []
  },
  {
   "id": "proprieta-ar-ma",
   "modulo": 6,
   "origine": "corso",
   "descrizione": "Condizione di stazionarietà dell'AR(1), varianza e autocorrelazioni teoriche di AR(1) e MA(1) (varianza MA(1) = (1+θ²)σ²), forma attesa di ACF e PACF.",
   "fonte": "ECON 06, «Modelli a media mobile MA(1) e MA(q)», «Modelli autoregressivi AR(1) e AR(p)», «L'ipotesi di stazionarietà nel caso AR(1)»",
   "occorrenze": []
  },
  {
   "id": "random-walk-e-regressione-spuria",
   "modulo": 6,
   "origine": "corso",
   "descrizione": "Riconoscere un random walk (con e senza drift), la sua non stazionarietà e perché la regressione fra due random walk indipendenti può sembrare significativa.",
   "fonte": "ECON 06, «Il random walk e la sua non stazionarietà» e «La regressione spuria»",
   "occorrenze": []
  },
  {
   "id": "test-di-chow",
   "modulo": 6,
   "origine": "corso",
   "descrizione": "Test di Chow per un break strutturale in una data nota: F con le SSR del modello unico e dei due sottocampioni, decisione.",
   "fonte": "ECON 06, «Break strutturali e il test di Chow»",
   "occorrenze": []
  },
  {
   "id": "superconsistenza-e-dols",
   "modulo": 7,
   "origine": "corso",
   "descrizione": "Dire perché OLS stima in modo superconsistente il coefficiente di lungo periodo fra serie cointegrate e quando serve DOLS per fare inferenza.",
   "fonte": "ECON 07, «Stima OLS in presenza di cointegrazione: superconsistenza» e «Lo stimatore DOLS»",
   "occorrenze": []
  },
  {
   "id": "variabile-casuale-valore-atteso-varianza",
   "modulo": 0,
   "origine": "corso",
   "descrizione": "Calcolare valore atteso e varianza di una variabile casuale discreta e di una trasformazione lineare aX+b, usando la linearità del valore atteso.",
   "fonte": "Ripassi di statistica (correlazione, distribuzioni campionarie); ECON 02, «Il termine d'errore ε: proprietà»",
   "occorrenze": []
  },
  {
   "id": "probabilita-condizionata-e-indipendenza",
   "modulo": 0,
   "origine": "corso",
   "descrizione": "Probabilità condizionata da una tabella congiunta, indipendenza fra due eventi o variabili e legame con l'incorrelazione.",
   "fonte": "Ripasso 01 (tabelle di contingenza, indipendenza); ECON 03, «L'errore ε: momenti condizionali»",
   "occorrenze": []
  },
  {
   "id": "valore-atteso-condizionato-e-esogeneita",
   "modulo": 0,
   "origine": "corso",
   "descrizione": "Valore atteso condizionato E[Y|X]: da E[ε|X]=0 seguono media nulla dell'errore e incorrelazione con X, non viceversa; riconoscere un errore con E[ε|X]≠0.",
   "fonte": "ECON 02, «Le ipotesi del modello di regressione OLS»; ECON 03, «L'errore ε: momenti condizionali»",
   "occorrenze": []
  }
 ],
 "valori_critici": [
  {
   "statistica": "normale standard, quantile destro al 2,5% (IC 95%, test bilaterale al 5%)",
   "valore": 1.96,
   "appello": "2022-12-22",
   "domanda": "D1",
   "nota": "Dato dentro il testo della D1 («si ricordi che i valori critici a destra per una normale standardizzata al 2.5% ed al 5%...»); le domande successive dell'esercizio non lo ripetono."
  },
  {
   "statistica": "normale standard, quantile destro al 5% (test unilaterale al 5%)",
   "valore": 1.64,
   "appello": "2022-12-22",
   "domanda": "D1",
   "nota": "Stessa frase della D1; il testo scrive 1.64, non 1,645."
  },
  {
   "statistica": "Dickey-Fuller aumentato, valore critico",
   "valore": -2.38,
   "appello": "2022-12-22",
   "domanda": "D6",
   "nota": "Valido «in entrambi i casi» (futures e spot); regressioni ADF con costante e due ritardi della differenza, senza colonna p-value."
  },
  {
   "statistica": "test di radice unitaria, valore critico",
   "valore": -3.43,
   "appello": "2023-01-17",
   "domanda": "D2",
   "nota": "Per le statistiche su USA e Australia (-0,686 e -0,401). Il test sui residui (-3,779) è dato solo con p-value 1,4%, senza valore critico Engle-Granger."
  },
  {
   "statistica": "ADF sui residui della regressione di lungo periodo (Engle-Granger), valore critico al 5%",
   "valore": -1.95,
   "appello": "2023-06-15",
   "domanda": "D8",
   "nota": "Unico valore critico per un test sui residui in tutti i testi; coincide con il valore DF senza costante di ECON 06 r. 833, mentre ECON 07 r. 129 dice che la distribuzione CDF differisce da quella dei test di radice unitaria classici."
  },
  {
   "statistica": "test di radice unitaria, valore critico",
   "valore": -3.43,
   "appello": "2023-06-15",
   "domanda": "D10",
   "nota": "Per i tassi italiani (statistica -5,12)."
  },
  {
   "statistica": "Dickey-Fuller aumentato, valore critico al 5%",
   "valore": -2.38,
   "appello": "2024-06-13",
   "domanda": "D7",
   "nota": "Per gfr e pe (statistiche -3,306 e -2,871); stesso numero del 2022-12-22."
  },
  {
   "statistica": "Dickey-Fuller / ADF (nessun valore critico)",
   "valore": null,
   "appello": null,
   "domanda": null,
   "nota": "In 2023-06-15 D8 (p-value 25% e 28%), 2023-08-29 D7 (tabella statistica + p-value), 2023-12-21 D8 (output ADF con t=0,3448 e p-value 0,9806 su gold_1) e D9 (p-value 74%), 2025-01-21 D7 (p-value 0,001 e 0,022) il testo non dà valori critici. Se servissero a memoria, la nota ECON 06 r. 833 riporta -2,85 (con costante), -1,95 (senza) e -1,64 per la N(0,1); -2,38 e -3,43 dei testi non compaiono nelle note."
  },
  {
   "statistica": "Engle-Granger / CDF (nessun valore critico)",
   "valore": null,
   "appello": null,
   "domanda": null,
   "nota": "Solo p-value in 2023-01-17 D2 (1,4%), 2023-08-29 D8 (tabella con p-value), 2023-12-21 D9 (0,007%), 2024-06-13 D8 (68%), 2025-01-21 D8 (2,67%); l'unico valore critico è il -1,95 del 2023-06-15 D8. Nessuna nota del corso tabula valori critici EG."
  },
  {
   "statistica": "chi-quadro (nessun quantile)",
   "valore": null,
   "appello": "2024-06-13",
   "domanda": "D4",
   "nota": "Il testo dà LM e p-value con i gradi di libertà: White LM=42,5928, P(chi2(40)>42,5928)=0,360144; Breusch-Pagan LM=24,6878, P(chi2(8)>24,6878)=0,00175558. In 2023-08-29 D2 il White è 24,697 con p-value 0,016, senza gradi di libertà."
  },
  {
   "statistica": "F (nessun valore)",
   "valore": null,
   "appello": null,
   "domanda": null,
   "nota": "Nessun testo riporta una statistica F o un suo quantile: 2022-12-22 D3, 2024-06-13 D2 e 2025-01-21 D5 chiedono solo di formulare il sistema d'ipotesi. L'unico quantile F nelle note è l'esempio 2,76 per F(3,60) in ECON 04 r. 160."
  },
  {
   "statistica": "t di Student / normale (fuori dal 2022-12-22)",
   "valore": null,
   "appello": null,
   "domanda": null,
   "nota": "Gli altri testi non danno quantili: 2023-06-15, 2023-08-29 e 2023-12-21 fissano alpha=5% in una Nota iniziale, 2023-12-21 D6 e 2025-01-21 D1 e D8 lo ripetono nella domanda. Lo studente deve sapere 1,96 e 1,64/1,645 a memoria. Il ripasso 03 (slide 10) indica t>=1,96 anche per un test unilaterale al 5%, in contrasto con l'1,64 del 2022-12-22 D1."
  },
  {
   "statistica": "QLR (nessun valore critico)",
   "valore": null,
   "appello": "2024-06-13",
   "domanda": "D9",
   "nota": "Solo p-value 0,372 e data del massimo (settembre 1943). Le note citano un valore critico al 5% di 5,86 solo per l'esempio Exelon (ECON 06 r. 626)."
  }
 ],
 "combinazioni_appelli": [
  {
   "esercizio_1": {
    "scenario": "Cross-section di consumatori: log(spesa) su reddito, reddito al quadrato, età e dummy proprietario di casa; output OLS con E.S. della regressione e R-quadro, poi tabella VIF.",
    "domande": [
     "variazione-percentuale-log-livello",
     "ic-per-verificare-un-valore",
     "termine-quadratico-nonlinearita",
     "punto-di-svolta-quadratico",
     "collinearita-diagnosi",
     "vif-inflazione-errore-standard"
    ]
   },
   "esercizio_2": {
    "scenario": "Prezzi mensili spot e futures di uno stesso indice: due regressioni ADF stampate con valore critico, test di Engle-Granger sui residui, ECM stimato con errori standard HAC.",
    "domande": [
     "adf-lettura-output-regressione",
     "cointegrazione-decisione",
     "ecm-ben-definito",
     "ecm-velocita-assorbimento"
    ]
   }
  },
  {
   "esercizio_1": {
    "scenario": "Cross-section di stipendi di atleti professionisti: log(salario) con dummy di ruolo a tre categorie (una omessa), esperienza ed esperienza al quadrato, statistiche di gioco; test di White e di Breusch-Pagan forniti.",
    "domande": [
     "dummy-categoria-base",
     "sistema-ipotesi-f-dummy-congiunte",
     "termine-quadratico-nonlinearita",
     "test-eteroschedasticita",
     "variazione-percentuale-log-livello",
     "test-unilaterale-su-soglia"
    ]
   },
   "esercizio_2": {
    "scenario": "Due serie annuali con statistiche ADF e valore critico, p-value di Engle-Granger da giudicare per coerenza con gli ordini d'integrazione, test QLR sulla regressione in differenze, correlogramma della serie differenziata.",
    "domande": [
     "adf-decisione-statistica-o-pvalue",
     "regressione-statica-ben-definita",
     "break-strutturale-qlr",
     "identificazione-ar-ma-arma"
    ]
   }
  },
  {
   "esercizio_1": {
    "scenario": "Cross-section di aziende: log(tasso di scarto) su dummy di finanziamento, ore di formazione e loro interazione con errori standard robusti; grafico residui-valori predetti; secondo modello con log(vendite) aggiunto.",
    "domande": [
     "interazione-effetto-marginale-condizionato",
     "differenza-tra-profili-combinazione-lineare",
     "test-su-valore-specifico",
     "eteroschedasticita-grafico-residui",
     "endogeneita-variabile-omessa",
     "unita-di-misura-e-scala"
    ]
   },
   "esercizio_2": {
    "scenario": "PIL trimestrale di due paesi con trend visibile nel grafico: specificazione della regressione ADF, statistiche di radice unitaria e test sui residui, ECM con correlogramma dei residui, segno del disequilibrio.",
    "domande": [
     "adf-specificazione-regressione",
     "cointegrazione-decisione",
     "ecm-rispecificazione-da-residui",
     "ecm-direzione-aggiustamento"
    ]
   }
  },
  {
   "esercizio_1": {
    "scenario": "Cross-section di aree urbane: log(prezzo delle case) su log(inquinamento), criminalità, numero di stanze e dummy di distanza interagita con log(inquinamento); statistica e p-value del test di White.",
    "domande": [
     "elasticita-log-log",
     "interazione-effetto-marginale-condizionato",
     "test-su-valore-specifico",
     "test-unilaterale-su-soglia",
     "variazione-percentuale-log-livello",
     "eteroschedasticita-implicazioni"
    ]
   },
   "esercizio_2": {
    "scenario": "Prezzi giornalieri di due commodity: p-value ADF delle due serie, correlogramma dei residui della relazione di lungo periodo, stima DOLS del coefficiente di lungo periodo, ECM con un ritardo della differenza del regressore.",
    "domande": [
     "adf-decisione-statistica-o-pvalue",
     "stazionarieta-da-correlogramma",
     "inferenza-coefficiente-lungo-periodo",
     "ecm-velocita-assorbimento"
    ]
   }
  }
 ],
 "precisione_tabelle": {
  "coef": 6,
  "se": 6,
  "t": 4,
  "p": "4 decimali (es. 0,0225) se il p-value è almeno 1e-4; sotto, notazione scientifica con 3 cifre significative (es. 2,13e-07); «0,0000» quando gretl non stampa di più (2023-12-21 D9 e D10, 2025-01-21 zona2)",
  "note": "Formato gretl uniforme, con eccezioni. Coefficienti a 5 cifre: 2022-12-22 uhat4_1 (-0.51197), 2023-01-17 D9 grant (-0,081663). Errori standard a 5 cifre: 2022-12-22 derog (0.033544), 2023-01-17 D10 hrsemp (0,0012498); a 4: 2022-12-22 sq_income (0.007891), 2023-01-17 sq_hrsemp (0,0009034); a 7: 2023-01-17 h_grant (0,001724751). Rapporto t a 3 cifre: 2022-12-22 age (-0.943); a 5: 2022-12-22 uhat4_1 (-4.1257), 2023-08-29 shrs (2,5443), 2023-12-21 uhat6_1 (-10,014). P-value fuori formato: 2023-01-17 h_grant 0,007288, grant 0.000102, h_grant 0,000567. Separatore decimale: punto nel 2022-12-22 (ma 0,517343 e 3,69e-05), virgola negli altri (ma 0.000102 nel 2023-01-17). 2023-12-21 D4 usa una tabella compatta a 3 decimali con errori standard tra parentesi e stelle; stelle anche in 2022-12-22 D8, 2023-12-21 e 2025-01-21 D9. Le regressioni ADF del 2022-12-22 non hanno colonna p-value. Incoerenze interne: 2024-06-13 expersq ha t stampato -2,882 ma coef/se = -2,804; p-value non coerenti con t in 2022-12-22 sq_income (0.0287 con t=-2,579), 2024-06-13 expersq (0,0123), 2023-12-21 uhat6_1 (0,0008 con t=-10,014). Tabelle riciclate: l'ECM di 2023-08-29 D9 è identico a 2023-06-15 D9, quello di 2023-08-29 D10 a 2023-01-17 D3 (solo nomi cambiati). Le altre righe hanno t = coef/se entro l'1%."
 }
}
```
