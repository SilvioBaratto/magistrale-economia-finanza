<!-- ex e02_01 -->
# Esercizio 1 — Ore di studio e punteggio: la retta dai momenti campionari *(livello base)*

> [!abstract] Dati
> Su $n = {{e02_01.n|m}}$ studenti si osservano le ore di studio settimanali (`ore`) e il punteggio ottenuto a una prova (`punteggio`, su 100). Si stima con OLS il modello
>
> $$\text{punteggio} = \alpha + \beta\,\text{ore} + \epsilon .$$
>
> Le medie e le varianze campionarie sono nella tabella; la covarianza campionaria fra `ore` e `punteggio` è ${{e02_01.cov|m}}$. Varianze e covarianza sono calcolate con lo stesso divisore ($n$ oppure $n-1$): il loro rapporto non dipende dalla scelta.
>
> {{e02_01.tab.momenti}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Si calcoli la stima OLS $\hat\beta$ della pendenza. **(b)** Si calcoli la stima OLS $\hat\alpha$ dell'intercetta. **(c)** Di quanti punti varia in media il punteggio per ${{e02_01.dx|m}}$ ore di studio in più? **(d)** Qual è il punteggio atteso di uno studente che studia ${{e02_01.x0|m}}$ ore a settimana?
<!-- /ex -->

<!-- ex e02_02 -->
# Esercizio 2 — Prezzo e superficie: varianza dell'errore ed errore standard *(livello base)*

> [!abstract] Dati
> Su $n = {{e02_02.n|m}}$ appartamenti in vendita si è stimato con OLS il modello
>
> $$\text{prezzo} = \alpha + \beta\,\text{sup} + \epsilon ,$$
>
> dove `prezzo` è in migliaia di euro e `sup` è la superficie in metri quadrati. Gli errori sono omoschedastici. Dalla stima si ricavano la somma dei quadrati dei residui, $\text{SSR}=\sum_i\hat\epsilon_i^2={{e02_02.ssr|m}}$, e la somma dei quadrati degli scarti della superficie dalla sua media, $\sum_i(x_i-\bar x)^2={{e02_02.ssx|m}}$.

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** Si calcoli la stima non distorta $\hat\sigma^2$ della varianza dell'errore. **(b)** Si calcoli $\hat\sigma$, l'errore standard della regressione. **(c)** Si calcoli l'errore standard stimato di $\hat\beta$. **(d)** Se la numerosità del campione fosse ${{e02_02.m|m}}$ volte più grande, a parità di $\hat\sigma$ e di varianza campionaria di `sup` (quindi con $\sum_i(x_i-\bar x)^2$ ${{e02_02.m|m}}$ volte più grande), per quale fattore si moltiplicherebbe l'errore standard di $\hat\beta$?
<!-- /ex -->

<!-- ex e02_03 -->
# Esercizio 3 — Affitto e distanza: la tavola ANOVA incompleta *(livello base)*

> [!abstract] Dati
> Su $n = {{e02_03.n|m}}$ appartamenti in affitto si è stimato il modello
>
> $$\text{affitto} = \alpha + \beta\,\text{dist} + \epsilon ,$$
>
> dove `affitto` è il canone mensile in centinaia di euro e `dist` la distanza dal centro in chilometri. La stima della pendenza è $\hat\beta={{e02_03.b|m}}$. Le devianze sono $\text{SST}=\sum_i(y_i-\bar y)^2$ (totale), $\text{SSE}=\sum_i(\hat y_i-\bar y)^2$ (spiegata dal modello) e $\text{SSR}=\sum_i(y_i-\hat y_i)^2$ (residua), con $\text{SST}=\text{SSE}+\text{SSR}$. Della tavola ANOVA è rimasta soltanto la riga dei residui e quella del totale.
>
> {{e02_03.tab.anova}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** **(a)** Quanto vale la devianza spiegata SSE? **(b)** Si calcoli l'indice $R^2$. **(c)** Si calcoli $\hat\sigma$, l'errore standard della regressione. **(d)** Qual è il coefficiente di correlazione lineare fra `dist` e `affitto`, con il suo segno? (Nella regressione semplice $R^2$ è il quadrato di tale coefficiente.)
<!-- /ex -->

<!-- ex e02_04 -->
# Esercizio 4 — Formazione e rendimento: quando OLS è distorto *(livello base)*

> [!abstract] Dati
> Un ricercatore vuole misurare l'effetto delle ore di formazione ($X$) sul rendimento ($Y$) con il modello
>
> $$Y = \alpha + \beta\,X + \epsilon, \qquad \beta = {{e02_04.beta|m}} .$$
>
> I lavoratori più motivati scelgono più formazione e la motivazione, che non si osserva, finisce in $\epsilon$: $\text{Var}(X)={{e02_04.sx2|m}}$ e $\text{Cov}(X,\epsilon)={{e02_04.cov|m}}$. Per capire come si comporta OLS simula $R={{e02_04.reps|m}}$ campioni da questo modello, per due numerosità, e riporta per ciascuna la media delle $R$ stime di $\beta$, la loro deviazione standard e la media degli errori standard calcolati con la formula usuale.
>
> {{e02_04.tab.mc}}
>
> Si consideri la media delle stime lontana dal vero $\beta$ se $|\text{media}-\beta|$ supera 3 volte l'errore standard della media delle stime, cioè $\text{dev. std.}/\sqrt{R}$.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** Con $n={{e02_04.n1|m}}$ lo stimatore OLS di $\beta$ è non distorto in questo modello? Si risponda sì o no. **(b)** A quale valore converge $\hat\beta$ quando $n$ tende all'infinito? (Si ricordi che, con $\text{Cov}(X,\epsilon)\neq 0$, $\hat\beta$ converge a $\beta+\text{Cov}(X,\epsilon)/\text{Var}(X)$.) **(c)** Con $n={{e02_04.n2|m}}$ la distorsione è scomparsa, cioè la media delle stime è vicina al vero $\beta$? Si risponda sì o no. **(d)** Il teorema di Gauss-Markov garantisce che OLS sia il miglior stimatore lineare non distorto in questo modello? Si risponda sì o no. **(e)** Quale ipotesi del modello è violata? Si spieghi.
<!-- /ex -->

<!-- ex e02_05 -->
# Esercizio 5 — Salario e istruzione: un valore dichiarato *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e02_05.n|m}}$ lavoratori si è stimato il modello
>
> $$\text{salario} = \alpha + \beta\,\text{istr} + \epsilon ,$$
>
> dove `salario` è la retribuzione oraria in euro e `istr` gli anni di istruzione. Le stime OLS sono le seguenti.
>
> {{e02_05.tab.ols}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** Un'agenzia di orientamento sostiene che ${{e02_05.dx|m}}$ anni di istruzione in più fanno salire il salario orario atteso di ${{e02_05.claim|m}}$ euro. Si usi il quantile $1{,}96$. **(a)** Quale valore di $\beta$ corrisponde all'affermazione? **(b)** Si calcoli il rapporto $t$ per il sistema $H_0:{{e02_05.dx|m}}\beta={{e02_05.claim|m}}$ contro $H_1:{{e02_05.dx|m}}\beta\neq{{e02_05.claim|m}}$, cioè la differenza fra la stima e il valore sotto $H_0$ divisa per il suo errore standard. **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$. **(d)** Il valore dichiarato di ${{e02_05.claim|m}}$ euro cade nell'intervallo di confidenza al 95\% per l'effetto di ${{e02_05.dx|m}}$ anni, $[{{e02_05.dx|m}}(\hat\beta\pm 1{,}96\,\widehat{\text{se}})]$? Si risponda sì o no.
<!-- /ex -->

<!-- ex e02_06 -->
# Esercizio 6 — Formazione e produttività: «almeno» *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e02_06.n|m}}$ operai si è stimato il modello
>
> $$\text{prod} = \alpha + \beta\,\text{ore} + \epsilon ,$$
>
> dove `prod` è la produttività oraria (pezzi all'ora) e `ore` le ore di formazione ricevute nell'anno. Le stime OLS sono le seguenti.
>
> {{e02_06.tab.ols}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** Un'azienda sostiene che ogni ${{e02_06.dx|m}}$ ore di formazione in più fanno salire la produttività di almeno ${{e02_06.dy|m}}$ pezzi all'ora. Si indichi con $k$ il valore di $\beta$ per cui ${{e02_06.dx|m}}$ ore valgono esattamente ${{e02_06.dy|m}}$ pezzi. Il quantile unilaterale al 5\% della normale standard è $1{,}64$. **(a)** Quanto vale $k$? **(b)** Si calcoli il rapporto $t=(\hat\beta-k)/\widehat{\text{se}}(\hat\beta)$. **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta\ge k$ contro $H_1:\beta<k$. **(d)** L'affermazione dell'azienda è compatibile con i dati? Si risponda sì o no (l'affermazione è l'ipotesi nulla).
<!-- /ex -->

<!-- ex e02_07 -->
# Esercizio 7 — Auto usate: intervallo di confidenza per un effetto percentuale *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e02_07.n|m}}$ auto usate si è stimato il modello
>
> $$\log(\text{prezzo}) = \alpha + \beta\,\text{eta} + \epsilon ,$$
>
> dove `eta` è l'età dell'auto in anni. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e02_07.tab.ols}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** Si usi il quantile $1{,}96$. **(a)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\beta$? **(b)** E l'estremo superiore? **(c)** Si trasformi l'intervallo in una variazione percentuale del prezzo per ${{e02_07.dx|m}}$ anni di età in più: qual è l'estremo inferiore, cioè il valore più basso (il più negativo) della variazione? **(d)** E l'estremo superiore, cioè il valore più alto? **(e)** Un rivenditore sostiene che ${{e02_07.dx|m}}$ anni di età in più fanno perdere in media il ${{e02_07.claim|m}}\%$ del prezzo. L'affermazione è compatibile con i dati, cioè il valore $-{{e02_07.claim|m}}\%$ cade nell'intervallo di (c)-(d)? Si risponda sì o no.
<!-- /ex -->

<!-- ex e02_08 -->
# Esercizio 8 — Spesa e reddito: eteroschedasticità in una simulazione *(livello intermedio)*

> [!abstract] Dati
> Si studia la spesa mensile (`spesa`) in funzione del reddito mensile (`reddito`) con il modello $\text{spesa}=\alpha+\beta\,\text{reddito}+\epsilon$ e $\beta={{e02_08.beta|m}}$. Per capire quando OLS è affidabile si simulano $R={{e02_08.reps|m}}$ campioni di $n={{e02_08.n|m}}$ osservazioni in due scenari: nel primo gli errori hanno varianza costante, nel secondo la variabilità della spesa cresce con il reddito (la figura seguente ne mostra un campione per scenario). Per ogni scenario si riportano la media delle $R$ stime di $\beta$, la loro deviazione standard e la media degli errori standard calcolati con la formula usuale $\sqrt{\hat\sigma^2/\sum_i(x_i-\bar x)^2}$.
>
> {{e02_08.tab.mc}}
>
> Si consideri la media delle stime lontana dal vero $\beta$ se $|\text{media}-\beta|$ supera 3 volte $\text{dev. std.}/\sqrt{R}$. Gli errori standard si considerano affidabili se il rapporto fra la deviazione standard delle stime e la media degli errori standard dista da 1 per meno del 10\%.

![Un campione simulato per scenario: la nuvola attorno alla retta ha ampiezza costante a sinistra e crescente con il reddito a destra.]({{e02_08.fig.dati}}){width=85%}

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Nello scenario con errori eteroschedastici lo stimatore OLS di $\beta$ è ancora non distorto? Si risponda sì o no. **(b)** In quello scenario il teorema di Gauss-Markov garantisce che OLS sia il miglior stimatore lineare non distorto? Si risponda sì o no. **(c)** Si calcoli, nello scenario eteroschedastico, il rapporto fra la deviazione standard delle stime e la media degli errori standard. **(d)** Gli errori standard usuali sono affidabili nello scenario eteroschedastico? Si risponda sì o no. **(e)** E nello scenario con errori a varianza costante? Si risponda sì o no. **(f)** Quale ipotesi è violata nel secondo scenario e quale conseguenza ha sul test $t$ di $H_0:\beta=0$? Si spieghi.
<!-- /ex -->

<!-- ex e02_09 -->
# Esercizio 9 — Salario e QI: R quadro basso, pendenza significativa *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e02_09.n}}$ lavoratori si è stimato il modello
>
> $$\text{salario} = \alpha + \beta\,\text{qi} + \epsilon ,$$
>
> dove `salario` è il salario mensile in centinaia di euro e `qi` il punteggio di un test di quoziente intellettivo. La stima della pendenza è $\hat\beta={{e02_09.b|m}}$ e la somma dei quadrati degli scarti di `qi` dalla sua media è $\sum_i(x_i-\bar x)^2={{e02_09.ssx|m}}$. La tavola ANOVA, con $\text{SST}=\text{SSE}+\text{SSR}$ (totale, spiegata, residua), è la seguente.
>
> {{e02_09.tab.anova}}

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** Si usi il quantile $1{,}96$. **(a)** Si calcoli $R^2$. **(b)** Si calcoli l'errore standard stimato di $\hat\beta$. **(c)** Si calcoli il rapporto $t$ per $H_0:\beta=0$. **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta=0$ contro $H_1:\beta\neq 0$. **(e)** Si calcoli la statistica $F=\dfrac{\text{SSE}/1}{\text{SSR}/(n-2)}$. **(f)** Un $R^2$ così basso implica che il QI non abbia alcun effetto sul salario? Si risponda sì o no.
<!-- /ex -->

<!-- ex e02_10 -->
# Esercizio 10 — Visite commerciali e vendite: oltre la soglia, ma non significativamente *(livello appello)*

> [!abstract] Dati
> Su $n = {{e02_10.n|m}}$ agenti commerciali si è stimato il modello
>
> $$\log(\text{vendite}) = \alpha + \beta\,\text{visite} + \epsilon ,$$
>
> dove `visite` è il numero di visite settimanali ai clienti. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e02_10.tab.ols}}

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** Il direttore commerciale sostiene che ${{e02_10.dx|m}}$ visite in più alla settimana fanno salire le vendite del ${{e02_10.soglia|m}}\%$. Si indichi con $\kappa$ il valore di $\beta$ per cui ${{e02_10.dx|m}}$ visite valgono esattamente il ${{e02_10.soglia|m}}\%$. Il quantile unilaterale al 5\% della normale standard è $1{,}64$. **(a)** Di quanto varia in percentuale, secondo la stima, il valore atteso delle vendite per ${{e02_10.dx|m}}$ visite in più? **(b)** Si calcoli il rapporto $t=(\hat\beta-\kappa)/\widehat{\text{se}}(\hat\beta)$. **(c)** Se l'affermazione fosse «almeno il ${{e02_10.soglia|m}}\%$», al livello del 5\% si decida se rifiutare o non rifiutare $H_0:\beta\ge\kappa$ contro $H_1:\beta<\kappa$. **(d)** Se l'affermazione fosse «più del ${{e02_10.soglia|m}}\%$», al livello del 5\% si decida se rifiutare o non rifiutare $H_0:\beta\le\kappa$ contro $H_1:\beta>\kappa$. **(e)** Si può affermare, al livello del 5\%, che ${{e02_10.dx|m}}$ visite in più fanno salire le vendite di più del ${{e02_10.soglia|m}}\%$? Si affermi soltanto ciò che i dati permettono di dedurre rifiutando l'ipotesi nulla contraria. Si risponda sì o no.
<!-- /ex -->

<!-- ex e02_11 -->
# Esercizio 11 — Costi di produzione: errori standard e due test *(livello appello)*

> [!abstract] Dati
> Su $n = {{e02_11.n|m}}$ mesi di attività di un'impresa si è stimato il modello
>
> $$\text{costo} = \alpha + \beta\,\text{prod} + \epsilon ,$$
>
> dove `costo` è il costo totale mensile in migliaia di euro e `prod` la produzione mensile in migliaia di pezzi: $\alpha$ misura i costi fissi e $\beta$ il costo variabile per migliaio di pezzi. Gli errori sono omoschedastici. I coefficienti stimati sono i seguenti.
>
> {{e02_11.tab.coef}}
>
> Si conoscono inoltre la somma dei quadrati dei residui, $\text{SSR}={{e02_11.ssr|m}}$, la somma dei quadrati degli scarti della produzione dalla sua media, $\sum_i(x_i-\bar x)^2={{e02_11.ssx|m}}$, e la produzione media, $\bar x={{e02_11.mx|m}}$. L'errore standard dell'intercetta è $\widehat{\text{se}}(\hat\alpha)=\sqrt{\hat\sigma^2\,\bigl(\tfrac1n\sum_i x_i^2\bigr)\big/\sum_i(x_i-\bar x)^2}$, con $\sum_i x_i^2=\sum_i(x_i-\bar x)^2+n\bar x^2$.

> [!question] Testo della domanda
> **Domanda 11 *(4 punti)*.** L'impresa dichiara che il costo variabile è di ${{e02_11.riv_b|m}}$ euro per ogni migliaio di pezzi e che i costi fissi sono di ${{e02_11.riv_a|m}}$ euro al mese. Si usi il quantile $1{,}96$. **(a)** Si calcoli $\hat\sigma$, l'errore standard della regressione. **(b)** Si calcoli l'errore standard stimato di $\hat\beta$. **(c)** Si indichi con $\beta_0$ il costo variabile dichiarato, espresso nelle unità del modello: si calcoli il rapporto $t=(\hat\beta-\beta_0)/\widehat{\text{se}}(\hat\beta)$ per $H_0:\beta=\beta_0$ contro $H_1:\beta\neq\beta_0$. **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare tale $H_0$. **(e)** Si calcoli l'errore standard stimato di $\hat\alpha$. **(f)** Si indichi con $\alpha_0$ il costo fisso dichiarato, espresso nelle unità del modello: al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\alpha=\alpha_0$ contro $H_1:\alpha\neq\alpha_0$.
<!-- /ex -->

<!-- ex e02_12 -->
# Esercizio 12 — Nord e Sud: la differenza fra due pendenze *(livello appello)*

> [!abstract] Dati
> Un'agenzia stima separatamente, su $n_N={{e02_12.nn|m}}$ appartamenti del Nord e su $n_S={{e02_12.ns|m}}$ del Sud, il modello
>
> $$\text{prezzo} = \alpha + \beta\,\text{sup} + \epsilon ,$$
>
> dove `prezzo` è in migliaia di euro e `sup` è la superficie in metri quadrati; $\beta_N$ e $\beta_S$ sono i prezzi marginali (migliaia di euro per metro quadrato) delle due aree. I due campioni sono indipendenti, quindi le due stime sono incorrelate: $\widehat{\text{Cov}}(\hat\beta_N,\hat\beta_S)=0$.
>
> Nord:
>
> {{e02_12.tab.nord}}
>
> Sud:
>
> {{e02_12.tab.sud}}

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** Si usi il quantile $1{,}96$. **(a)** Gli intervalli di confidenza al 95\% per $\beta_N$ e per $\beta_S$ si sovrappongono? Si risponda sì o no. **(b)** Si calcoli l'errore standard stimato della differenza $\hat\beta_N-\hat\beta_S$. **(c)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\beta_N-\beta_S$? **(d)** E l'estremo superiore? **(e)** Al livello del 5\%, la differenza fra i due prezzi marginali è significativa, cioè si rifiuta $H_0:\beta_N=\beta_S$ contro $H_1:\beta_N\neq\beta_S$? Si risponda sì o no. **(f)** La risposta di (a) basta a decidere su (e)? Si spieghi.
<!-- /ex -->
