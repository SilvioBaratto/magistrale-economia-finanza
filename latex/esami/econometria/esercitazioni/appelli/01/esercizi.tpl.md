<!-- ex a01_01 -->
# Esercizio 1 — La spesa dei consumatori: reddito, età e proprietà della casa

> [!abstract] Dati
> Si vuole analizzare quali variabili determinano la spesa mensile dei consumatori. A questo proposito sono state raccolte le seguenti osservazioni su un campione di $n = {{a01_01.n}}$ individui:
>
> - `spesa`: spesa mensile media (in dollari);
> - `reddito`: reddito personale, misurato in decine di migliaia di dollari (un'unità di `reddito` vale {{a01_01.unita}} dollari);
> - `eta`: età del titolare, in anni;
> - `proprietario`: variabile binaria che vale 1 se l'individuo è proprietario dell'abitazione in cui vive e 0 altrimenti.
>
> Si consideri il modello
>
> $$\log(\text{spesa}) = \beta_0 + \beta_1\,\text{reddito} + \beta_2\,\text{reddito}^2 + \beta_3\,\text{eta} + \beta_4\,\text{proprietario} + \epsilon ,$$
>
> in cui il quadrato del reddito compare nella tabella come `sq_reddito`. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Dove non è indicato altrimenti si usi il livello di significatività del 5\%, con il quantile $1{,}96$ della normale standard. Le stime sono riportate di seguito.
>
> **Stime OLS.**
>
> {{a01_01.tab.ols}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, la spesa di un proprietario rispetto a quella di un non proprietario con lo stesso reddito e la stessa età? **(b)** Di quanti anni deve aumentare l'età, a parità delle altre variabili, perché la spesa attesa si riduca del ${{a01_01.obiettivo}}\%$?

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** Una rivista sostiene che, a parità delle altre variabili, ${{a01_01.dx}}$ anni di età in più riducono la spesa attesa del ${{a01_01.rid}}\%$. Si costruisca l'intervallo di confidenza al 95\% per la variazione percentuale attesa $100\cdot{{a01_01.dx}}\cdot\beta_3$ della spesa quando l'età aumenta di ${{a01_01.dx}}$ anni. **(a)** Qual è l'estremo inferiore dell'intervallo? **(b)** Qual è l'estremo superiore? **(c)** L'affermazione della rivista, cioè $100\cdot{{a01_01.dx}}\cdot\beta_3=-{{a01_01.rid}}$, è compatibile con i dati, ossia il valore $-{{a01_01.rid}}$ cade nell'intervallo? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$ (cioè se la relazione fra reddito e $\log(\text{spesa})$ è lineare). **(b)** Sulla base del modello stimato, l'effetto marginale del reddito su $\log(\text{spesa})$ è decrescente al crescere del reddito? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 4 *(4 punti)*.** Si approssimi l'effetto di una variazione del reddito con l'effetto marginale, cioè con la derivata di $\log(\text{spesa})$ rispetto a `reddito`. Nel campione il reddito osservato va da ${{a01_01.rmin|m}}$ a ${{a01_01.rmax|m}}$ (decine di migliaia di dollari). **(a)** Per un consumatore con `reddito` pari a ${{a01_01.r0}}$, di quanto varia in percentuale la spesa attesa se il reddito aumenta di una unità, cioè di {{a01_01.unita}} dollari, a parità delle altre variabili? **(b)** A quale valore di `reddito` l'effetto marginale del reddito si annulla? **(c)** Il valore trovato in (b) cade nel campo di variazione osservato del reddito? Si risponda sì o no.

> [!abstract] Dati della Domanda 5
> Per ciascun regressore si è calcolato il fattore di inflazione della varianza $\text{VIF}(j)=1/(1-R(j)^2)$, dove $R(j)$ è il coefficiente di correlazione multipla fra la variabile $j$ e le altre variabili indipendenti del modello.
>
> **Fattori di inflazione della varianza (VIF).**
>
> {{a01_01.tab.vif}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** Si usi la soglia 10 per il VIF. **(a)** Quanti regressori presentano un VIF superiore alla soglia? **(b)** Il coefficiente di `proprietario` non risulta significativo al livello del 5\%: la quasi-collinearità può spiegare questa non significatività? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** Rispetto al caso ideale in cui i regressori fossero indipendenti fra loro (a parità di $\hat\sigma$ e di variabilità del regressore considerato), di quante volte ci si aspetta che sia gonfiato l'errore standard del coefficiente di **(a)** `reddito` e **(b)** `sq_reddito`?
<!-- /ex -->

<!-- ex a01_02 -->
# Esercizio 2 — Indice azionario: prezzi spot e futures

> [!abstract] Dati
> Si considerano i prezzi mensili di un indice azionario (`spot`) e dei relativi contratti futures sullo stesso indice (`futures`), osservati per $n = {{a01_02.n}}$ mesi. La figura rappresenta le due serie, le cui differenze prime risultano stazionarie (test non riportato). Tutti i test si intendono al livello del 5\%, con il quantile $1{,}96$ della normale standard dove serve.
>
> ![Prezzi mensili dello spot e dei futures dell'indice.]({{a01_02.fig.serie}}){width=85%}

> [!abstract] Dati della Domanda 7
> Per valutare la stazionarietà delle due serie sono state stimate le regressioni di Dickey-Fuller aumentate, con una costante, il livello ritardato e due ritardi della differenza prima. Per ciascuna serie si verifica $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$, dove $\delta$ è il coefficiente del livello ritardato: si rifiuta $H_0$ se la statistica $t$ del livello ritardato è minore del valore critico ${{a01_02.cv|m}}$, valido in entrambi i casi.
>
> **Regressione ADF — variabile dipendente `d_futures`.**
>
> {{a01_02.tab.adf_f}}
>
> **Regressione ADF — variabile dipendente `d_spot`.**
>
> {{a01_02.tab.adf_s}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Qual è il valore della statistica $t$ del test ADF per `spot`? **(b)** Per `futures`, si decida se rifiutare o non rifiutare $H_0$ (radice unitaria). **(c)** Per `spot`, si decida se rifiutare o non rifiutare $H_0$ (radice unitaria).

> [!abstract] Dati della Domanda 8
> Si è stimata la relazione di lungo periodo $\text{spot}_t=a+b\,\text{futures}_t+u_t$ con gli OLS. Il test di Engle-Granger è un test di radice unitaria sui residui $\hat u_t$: $H_0$ è che i residui abbiano una radice unitaria (assenza di cointegrazione), $H_1$ che siano stazionari. Il test ha p-value ${{a01_02.p_eg|m}}$.

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$ del test di Engle-Granger. **(b)** Tenendo conto anche del risultato della domanda 7, `spot` e `futures` sono cointegrate? Si risponda sì o no.

> [!abstract] Dati della Domanda 9
> Il modello a correzione dell'errore
>
> $$\Delta\text{spot}_t = \gamma_0 + \gamma_1\,\Delta\text{futures}_t + \lambda\,\text{ecm}_{t-1} + \epsilon_t ,\qquad \text{ecm}_{t-1}=\text{spot}_{t-1}-\hat a-\hat b\,\text{futures}_{t-1} ,$$
>
> è stimato con gli OLS su $n = {{a01_02.n_ecm}}$ osservazioni, con errori standard HAC (kernel di Bartlett, larghezza di banda ${{a01_02.banda}}$).
>
> **Stime OLS — variabile dipendente `d_spot`.**
>
> {{a01_02.tab.ecm}}

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(b)** Il modello risulta ben definito, anche sulla base dei risultati delle domande 7 e 8? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** Si ipotizzi che in $t-1$ si osservi un disequilibrio $z_{t-1}=\text{ecm}_{t-1}\neq 0$, che da $t$ in poi i prezzi `futures` restino costanti ($\Delta\text{futures}=0$), che tutti gli shock siano nulli e che si trascuri la costante. Il periodo $t$ è il primo periodo di aggiustamento: dopo $k$ periodi di aggiustamento il disequilibrio residuo è $z_{t+k-1}$. **(a)** Quale quota del disequilibrio iniziale, in percentuale, viene assorbita nel primo periodo di aggiustamento? **(b)** Qual è il minimo numero intero $k$ di periodi dopo il quale almeno ${{a01_02.q}}\%$ del disequilibrio iniziale è stato assorbito?
<!-- /ex -->
