<!-- ex a04_01 -->
# Esercizio 1 — Prezzi delle case, inquinamento e distanza dal centro

> [!abstract] Dati
> In $n = {{a04_01.n}}$ aree urbane sono state osservate le seguenti variabili:
>
> - `prezzo`: prezzo mediano delle abitazioni dell'area, in migliaia di euro;
> - `nox`: concentrazione di ossidi di azoto nell'area, un indicatore dell'inquinamento dell'aria;
> - `crime`: tasso di criminalità, numero di reati per mille abitanti;
> - `rooms`: numero medio di stanze per abitazione;
> - `lontano`: variabile dummy, uguale a 1 se l'area dista più di 10 chilometri dal centro e a 0 altrimenti.
>
> Si consideri il modello
>
> $$\log(\text{prezzo}) = \beta_0 + \beta_1\,\text{l\_nox} + \beta_2\,\text{crime} + \beta_3\,\text{rooms} + \beta_4\,\text{lontano} + \beta_5\,\text{d\_nox} + \epsilon ,$$
>
> dove $\text{l\_nox}=\log(\text{nox})$ e $\text{d\_nox}=\text{lontano}\cdot(\text{l\_nox}-c)$, con $c={{a04_01.c|m}}$ il logaritmo di un livello di riferimento dell'inquinamento. Le stime OLS, con errori standard robusti all'eteroschedasticità (variante HC1), sono le seguenti.
>
> {{a04_01.tab.ols}}
>
> Se non specificato diversamente, si usi un livello di significatività del 5\%: i rapporti $t$ si confrontano con i quantili della normale standard, $1{,}96$ per i test bilaterali e $1{,}64$ per i test unilaterali. Le variazioni percentuali si calcolano con le approssimazioni $\Delta\%\,y\approx 100\,\Delta\log(y)$ e $\Delta\log(z)\approx\Delta z/z$.

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** Si considerino le aree vicine al centro ($\text{lontano}=0$). **(a)** Si calcoli l'elasticità del prezzo rispetto all'inquinamento. **(b)** Di quanto varia in percentuale il prezzo atteso se `nox` aumenta del ${{a04_01.var}}\%$, a parità delle altre variabili?

> [!question] Testo della domanda
> **Domanda 2 *(4 punti)*.** **(a)** Si calcoli l'elasticità del prezzo rispetto all'inquinamento per le aree lontane dal centro ($\text{lontano}=1$). **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_5=0$ contro $H_1:\beta_5\neq 0$, cioè se l'elasticità dipende dalla distanza dal centro. **(c)** Per le aree lontane, al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1+\beta_5=0$ contro $H_1:\beta_1+\beta_5\neq 0$, cioè se l'inquinamento incide sul prezzo. La covarianza fra gli stimatori $\hat\beta_1$ e $\hat\beta_5$ (stimata con la correzione HC1) è ${{a04_01.cov|m}}$.

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Un comitato di quartiere sostiene che un reato in più per mille abitanti riduca il prezzo atteso del ${{a04_01.riv}}\%$, a parità delle altre variabili. Si consideri il sistema $H_0:100\,\beta_2=-{{a04_01.riv}}$ contro $H_1:100\,\beta_2\neq-{{a04_01.riv}}$, al livello del 5\%. **(a)** Quanto vale il rapporto $t$ per $H_0$? **(b)** Si decida se rifiutare o non rifiutare $H_0$.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** Un'agenzia immobiliare afferma che ${{a04_01.delta}}$ stanze in più fanno aumentare il prezzo atteso di più del ${{a04_01.perc}}\%$, a parità delle altre variabili. Si consideri il sistema $H_0:{{a04_01.delta}}\,\beta_3\le{{a04_01.lim|m}}$ contro $H_1:{{a04_01.delta}}\,\beta_3>{{a04_01.lim|m}}$, al livello del 5\%. **(a)** Qual è la soglia $s$ tale che $H_0$ equivale a $\beta_3\le s$? **(b)** Quanto vale il rapporto $t=(\hat\beta_3-s)/\widehat{\text{se}}(\hat\beta_3)$? **(c)** Si decida se rifiutare o non rifiutare $H_0$.

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** A parità delle altre variabili e per un livello di inquinamento pari a quello di riferimento ($\text{l\_nox}=c$), di quanto differisce in percentuale il prezzo atteso di un'area lontana dal centro rispetto a quello di un'area vicina (prezzo dell'area lontana meno prezzo dell'area vicina)? **(b)** Di quante stanze deve aumentare `rooms` perché il prezzo atteso aumenti del ${{a04_01.ob}}\%$, a parità delle altre variabili?

> [!abstract] Dati della Domanda 6
> Per verificare l'omoschedasticità si è eseguito il test di White sui residui del modello. La regressione ausiliaria di $\hat\epsilon^2$ ha come regressori `l_nox`, `crime` e `rooms`, i loro quadrati e i loro prodotti a coppie, per un totale di ${{a04_01.gl}}$ regressori oltre alla costante (le dummy non sono incluse).
>
> {{a04_01.tab.white}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi nulla di omoschedasticità. **(b)** Sulla base di questo risultato si può affermare che $E[\epsilon\mid X]\neq 0$, cioè che gli stimatori OLS dei coefficienti sono distorti? Si risponda sì o no. **(c)** Gli errori standard della tabella delle stime OLS sono robusti all'eteroschedasticità: in presenza di questo risultato sono preferibili agli errori standard usuali, calcolati nell'ipotesi di omoschedasticità? Si risponda sì o no.
<!-- /ex -->

<!-- ex a04_02 -->
# Esercizio 2 — Frumento e mais: prezzi giornalieri

> [!abstract] Dati
> Si dispone di $T = {{a04_02.T}}$ osservazioni giornaliere dei prezzi del frumento (`frumento`) e del mais (`mais`), in dollari per tonnellata. Le variabili `l_frumento` e `l_mais` sono i loro logaritmi e si pone $y_t=\text{l\_frumento}_t$ e $x_t=\text{l\_mais}_t$. Se non specificato diversamente, si usi un livello di significatività del 5\%, con il quantile $1{,}96$ della normale standard per i test bilaterali.

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** Per ciascuna delle due serie si è eseguito il test ADF con costante e un ritardo della differenza, con $H_0$: radice unitaria; si rifiuta $H_0$ se il p-value è minore di $0{,}05$. I p-value sono ${{a04_02.p_f|m}}$ per `l_frumento` e ${{a04_02.p_m|m}}$ per `l_mais`. **(a)** Per `l_frumento`, si decida se rifiutare o non rifiutare $H_0$. **(b)** Lo stesso per `l_mais`. **(c)** Le due serie hanno entrambe un comportamento non stazionario (una radice unitaria)? Si risponda sì o no.

> [!abstract] Dati della Domanda 8
> Si è stimata con OLS la relazione di lungo periodo $y_t=\alpha+\beta\,x_t+u_t$. La figura riporta l'ACF (in alto) e la PACF (in basso) dei residui $\hat u_t$, sui primi 12 ritardi, con le bande di confidenza al 95\%; le barre rosse escono dalle bande.
>
> ![ACF e PACF dei residui della relazione di lungo periodo.]({{a04_02.fig.correlogramma}}){width=85%}

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Quanti dei primi 12 ritardi dell'ACF dei residui escono dalle bande di confidenza? **(b)** Sulla base del correlogramma, i residui $\hat u_t$ sembrano stazionari? Si risponda sì o no.

> [!abstract] Dati della Domanda 9
> La relazione di lungo periodo è stata stimata anche con lo stimatore DOLS, aggiungendo ${{a04_02.ell}}$ anticipi, ${{a04_02.ell}}$ ritardi e il termine contemporaneo di $\Delta x_t$ (i loro coefficienti sono omessi dalla tabella). Gli errori standard sono HAC di Newey-West, con nucleo di Bartlett e ${{a04_02.m}}$ autocovarianze.
>
> {{a04_02.tab.dols}}

> [!question] Testo della domanda
> **Domanda 9 *(4 punti)*.** Un analista sostiene che l'elasticità di lungo periodo del frumento rispetto al mais sia unitaria, cioè considera $H_0:\beta={{a04_02.b0|m}}$ contro $H_1:\beta\neq{{a04_02.b0|m}}$. **(a)** Alla luce delle risposte alle Domande 7 e 8, la relazione di lungo periodo è ben definita, cioè le serie sono non stazionarie e cointegrate? Si risponda sì o no. Con la stima DOLS e l'errore standard HAC: **(b)** quanto vale il rapporto $t$ per $H_0$? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$. **(d)** Quanto vale l'estremo superiore dell'intervallo di confidenza al 95\% per $\beta$?

> [!abstract] Dati della Domanda 10
> Si stima il modello a correzione dell'errore
>
> $$\Delta y_t=\gamma_0+\gamma_1\,\Delta x_t+\gamma_2\,\Delta x_{t-1}+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=y_{t-1}-\hat\alpha-\hat\beta\,x_{t-1} ,$$
>
> dove $\hat\alpha$ e $\hat\beta$ sono le stime OLS della relazione di lungo periodo della Domanda 8 (non riportate: non servono per le domande, che usano solo l'output seguente). Le stime OLS (variabile dipendente `d_l_frumento`) sono le seguenti.
>
> {{a04_02.tab.ecm}}
>
> Si ipotizzi che in $t-1$ si osservi un disequilibrio $z_{t-1}=\text{ecm}_{t-1}\neq 0$, che dal periodo $t-2$ in poi il prezzo del mais resti costante (quindi $\Delta x_{t-1}=\Delta x_t=\Delta x_{t+1}=\dots=0$), che tutti gli shock siano nulli e che si trascuri la costante. Il periodo $t$ è il primo periodo di aggiustamento, cioè $k$ conta anche il periodo di impatto: dopo $k$ periodi di aggiustamento il disequilibrio residuo è $z_{t+k-1}$.

> [!question] Testo della domanda
> **Domanda 10 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(b)** Qual è il minimo numero intero $k$ di periodi dopo il quale almeno il ${{a04_02.q}}\%$ del disequilibrio iniziale è stato assorbito? **(c)** Quale quota del disequilibrio iniziale, in percentuale, risulta effettivamente assorbita dopo il numero di periodi trovato in (b)?
<!-- /ex -->
