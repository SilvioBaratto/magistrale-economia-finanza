<!-- ex a03_01 -->
# Esercizio 1 — Formazione finanziata e tasso di scarto

> [!abstract] Dati
> Un'agenzia regionale ha finanziato corsi di formazione per i dipendenti di alcune aziende manifatturiere. Per misurare l'effetto della formazione sulla qualità della produzione, su $n = {{a03_01.n}}$ aziende sono state osservate le seguenti variabili:
>
> - `scarto`: tasso di scarto, cioè il numero di pezzi difettosi ogni 100 pezzi prodotti;
> - `fin`: variabile dummy, uguale a 1 se l'azienda ha ricevuto il finanziamento per la formazione e a 0 altrimenti;
> - `ore`: ore annue di formazione per dipendente;
> - `vendite`: fatturato annuo, in milioni di euro.
>
> Si consideri il Modello 1
>
> $$\log(\text{scarto}) = \beta_0 + \beta_1\,\text{fin} + \beta_2\,\text{ore} + \beta_3\,\text{ore\_fin} + \epsilon ,$$
>
> dove $\text{ore\_fin}=\text{ore}\times\text{fin}$. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime sono riportate di seguito.
>
> **Stime OLS del Modello 1.** Variabile dipendente: `l_scarto`. Errori standard robusti rispetto all'eteroschedasticità, variante HC1.
>
> {{a03_01.tab.m1}}

> [!note] Nota
> Se non specificato diversamente, si consideri un livello di significatività del 5\% e si usi il quantile 1,96 della normale standard per i test bilaterali.

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, il tasso di scarto di un'azienda finanziata per un'ora di formazione in più per dipendente? **(b)** E quello di un'azienda non finanziata? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$ (cioè se l'effetto di un'ora di formazione sul tasso di scarto dipende dal finanziamento).

> [!question] Testo della domanda
> **Domanda 2 *(4 punti)*.** Si considerino due aziende. L'azienda A ha ricevuto il finanziamento e fornisce ${{a03_01.ore_a}}$ ore annue di formazione per dipendente; l'azienda B non ha ricevuto il finanziamento e ne fornisce ${{a03_01.ore_b}}$. Le covarianze stimate fra gli stimatori (con errori standard robusti) valgono $\text{Cov}(\hat\beta_1,\hat\beta_2)={{a03_01.c12|m}}$, $\text{Cov}(\hat\beta_1,\hat\beta_3)={{a03_01.c13|m}}$ e $\text{Cov}(\hat\beta_2,\hat\beta_3)={{a03_01.c23|m}}$. **(a)** Di quanto differisce in percentuale, in media, il tasso di scarto di A da quello di B (A meno B)? **(b)** Quanto vale l'errore standard di tale differenza, in punti percentuali? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\text{E}[\log(\text{scarto})\mid A]=\text{E}[\log(\text{scarto})\mid B]$ (i due tassi di scarto attesi sono uguali) contro l'alternativa bilaterale.

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Il responsabile del programma sostiene che, in un'azienda non finanziata, ${{a03_01.ore3}}$ ore annue di formazione in più per dipendente riducono il tasso di scarto del ${{a03_01.riv3}}\%$. Si consideri il sistema di ipotesi $H_0:{{a03_01.ore3|m}}\,\beta_2=-{{a03_01.riv3|m}}/100$ contro $H_1:{{a03_01.ore3|m}}\,\beta_2\neq -{{a03_01.riv3|m}}/100$. **(a)** Quanto vale la statistica $t$ del test, calcolata come $(\text{stima}-\text{valore sotto }H_0)/\text{errore standard}$? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$.

La Figura 1 rappresenta i residui del Modello 1 contro i valori predetti di $\log(\text{scarto})$.

![Figura 1 — Residui del Modello 1 contro i valori predetti.]({{a03_01.fig.residui}}){width=85%}

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** Si risponda sì o no. **(a)** Dal grafico, la varianza dei residui del Modello 1 sembra costante al variare dei valori predetti? **(b)** Gli errori standard usuali dell'OLS, calcolati assumendo l'omoschedasticità, sarebbero affidabili per i test $t$ sui coefficienti del Modello 1?

> [!abstract] Dati della Domanda 5
> Si consideri ora il Modello 2, che aggiunge $\log(\text{vendite})$ come proxy della dimensione aziendale,
>
> $$\log(\text{scarto}) = \beta_0 + \beta_1\,\text{fin} + \beta_2\,\text{ore} + \beta_3\,\text{ore\_fin} + \beta_4\,\log(\text{vendite}) + \epsilon ,$$
>
> le cui stime, con gli stessi errori standard robusti HC1, sono riportate di seguito (`l_vendite` è $\log(\text{vendite})$).
>
> {{a03_01.tab.m2}}
>
> Si è stimata infine la regressione ausiliaria $\log(\text{vendite})=\delta_0+\delta_1\,\text{fin}+\delta_2\,\text{ore}+\delta_3\,\text{ore\_fin}+u$, anch'essa con errori standard robusti HC1.
>
> {{a03_01.tab.aux}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** Si indichi con $\tilde\beta_2$ la stima di $\beta_2$ nel Modello 1 e con $\hat\beta_2$ quella nel Modello 2. **(a)** Quanto vale, in punti percentuali, $100\,(\tilde\beta_2-\hat\beta_2)$? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$ nel Modello 2. **(c)** Al livello del 5\%, la stima di $\beta_2$ nel Modello 1 soffre di distorsione da variabile omessa dovuta a `l_vendite`? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** Si consideri il Modello 2. Un'azienda non finanziata ha un tasso di scarto di ${{a03_01.s0}}$, cioè ${{a03_01.s0}}$ pezzi difettosi ogni 100, e una giornata di formazione equivale a ${{a03_01.giornata}}$ ore. Per le variazioni dello scarto in punti si usi l'approssimazione $\Delta\text{scarto}\approx\text{scarto}\times\Delta\log(\text{scarto})$. **(a)** Di quanti punti varia, secondo la stima del Modello 2, il tasso di scarto di questa azienda se la formazione aumenta di una giornata per dipendente? **(b)** Un consulente sostiene che una giornata di formazione in più riduce lo scarto di {{a03_01.c6}} punti. Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$: la variazione attesa dello scarto è di $-{{a03_01.c6|m}}$ punti, contro l'alternativa bilaterale.
<!-- /ex -->

<!-- ex a03_02 -->
# Esercizio 2 — PIL di due paesi: stazionarietà, cointegrazione e correzione dell'errore

> [!abstract] Dati
> Si considera il prodotto interno lordo reale trimestrale di due paesi, osservato per $T = {{a03_02.T}}$ trimestri:
>
> - `pil_a`: PIL reale del paese A, in 100 volte il logaritmo;
> - `pil_b`: PIL reale del paese B, in 100 volte il logaritmo.
>
> Una variazione di una unità vale quindi circa un punto percentuale. L'andamento delle due serie è riportato nella Figura 2.

> [!note] Nota
> Se non specificato diversamente, si consideri un livello di significatività del 5\% e si usi il quantile 1,96 della normale standard per i test bilaterali.

![Figura 2 — PIL trimestrale dei due paesi: `pil_a` (a sinistra) e `pil_b` (a destra).]({{a03_02.fig.serie}}){width=85%}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** Si vuole verificare la stazionarietà di `pil_a` e di `pil_b` con un test di Dickey-Fuller aumentato. Un'analisi preliminare indica che per ciascuna serie la dinamica è descritta da un modello autoregressivo di ordine $p={{a03_02.p}}$. La regressione di Dickey-Fuller aumentata ha la forma $\Delta y_t=\beta_0^*+\alpha\,t+\delta\,y_{t-1}+\sum_{j=1}^{p-1}\psi_j\,\Delta y_{t-j}+\epsilon_t$, in cui il trend $\alpha\,t$ può essere omesso. Il sistema d'ipotesi è $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ e si rifiuta $H_0$ se la statistica $t$ di $\hat\delta$ è minore del valore critico al 5\%, che vale ${{a03_02.cv_c|m}}$ con la sola costante e ${{a03_02.cv_t|m}}$ con costante e trend. **(a)** La regressione di Dickey-Fuller di ciascuna serie deve includere il trend deterministico? Si risponda sì o no. **(b)** Quanti coefficienti (costante compresa) ha la regressione di Dickey-Fuller di ciascuna serie? **(c)** Con quale valore critico va confrontata la statistica $t$?

> [!abstract] Dati della Domanda 8
> Le statistiche $t$ del test di Dickey-Fuller aumentato, calcolate con la regressione specificata alla Domanda 7, sono le seguenti.
>
> {{a03_02.tab.adf}}
>
> **Stime OLS della relazione di lungo periodo** $\text{pil\_a}_t=\alpha+\beta\,\text{pil\_b}_t+u_t$. Variabile dipendente: `pil_a`.
>
> {{a03_02.tab.lungo}}
>
> Il test di Engle-Granger sui residui della relazione di lungo periodo ($H_0$: assenza di cointegrazione) ha p-value ${{a03_02.p_eg|m}}$.

> [!question] Testo della domanda
> **Domanda 8 *(4 punti)*.** Al livello del 5\%: **(a)** per `pil_a`, si decida se rifiutare o non rifiutare $H_0:\delta=0$ (radice unitaria); **(b)** si decida lo stesso per `pil_b`; **(c)** si decida se rifiutare o non rifiutare l'ipotesi nulla di assenza di cointegrazione del test di Engle-Granger; **(d)** si può parlare di una relazione di cointegrazione fra `pil_a` e `pil_b`? Si risponda sì o no.

> [!abstract] Dati della Domanda 9
> Il modello a correzione dell'errore
>
> $$\Delta\text{pil\_a}_t=\gamma_0+\gamma_1\,\Delta\text{pil\_b}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{pil\_a}_{t-1}-\hat\alpha-\hat\beta\,\text{pil\_b}_{t-1} ,$$
>
> è stimato con OLS su $n = {{a03_02.n_ecm}}$ osservazioni (variabile dipendente `d_pil_a`).
>
> {{a03_02.tab.ecm}}
>
> La Figura 3 riporta l'autocorrelogramma (ACF, in alto) e l'autocorrelogramma parziale (PACF, in basso) dei residui del modello, sui primi 12 ritardi, con le bande di confidenza al 95\%; le barre rosse escono dalle bande.

![Figura 3 — ACF e PACF dei residui del modello a correzione dell'errore.]({{a03_02.fig.correlogramma}}){width=85%}

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Il modello è ben definito, cioè bilanciato e con un meccanismo di correzione dell'errore, al livello del 5\%? Si risponda sì o no. **(b)** Quanti dei primi 12 ritardi dell'ACF dei residui escono dalle bande di confidenza al 95\%? **(c)** Occorre ri-specificare la dinamica di breve periodo del modello, per esempio aggiungendo ritardi di $\Delta\text{pil\_a}$ e di $\Delta\text{pil\_b}$? Si risponda sì o no. **(d)** Occorre ri-specificare la relazione di lungo periodo? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 10 *(3 punti)*.** Si consideri questo scenario con il modello della Domanda 9: al tempo $t$ il disequilibrio vale $\text{ecm}_t={{a03_02.d|m}}$, cioè `pil_a` sta al di sopra della relazione di lungo periodo. **(a)** La variazione attesa $\Delta\text{pil\_a}_{t+1}$ è inferiore a quella che si avrebbe con $\text{ecm}_t=0$, a parità di $\Delta\text{pil\_b}_{t+1}$ e di shock nullo? Si risponda sì o no. **(b)** Quanto vale, in punti e con il suo segno, la differenza fra la variazione attesa $\Delta\text{pil\_a}_{t+1}$ con $\text{ecm}_t={{a03_02.d|m}}$ e quella con $\text{ecm}_t=0$ (la prima meno la seconda)? **(c)** Si supponga che `pil_b` non cresca in $t+1$ ($\Delta\text{pil\_b}_{t+1}=0$) e che costante e shock siano trascurabili: quale percentuale del disequilibrio $\text{ecm}_t$ viene assorbita nel periodo $t+1$?
<!-- /ex -->
