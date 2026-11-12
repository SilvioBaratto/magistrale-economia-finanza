{{testo:e06_01}}

> [!tip] Richiamo
> Un AR(1) $Y_t=c+\phi\,Y_{t-1}+\epsilon_t$ è stazionario se $|\phi|<1$. Passando al valore atteso, $\mu=c+\phi\mu$, quindi $\mu=c/(1-\phi)$. Sostituendo all'indietro, $Y_t-\mu=\sum_{j\ge 0}\phi^j\epsilon_{t-j}$, da cui $\text{Var}(Y_t)=\sigma^2/(1-\phi^2)$ e $\text{Cov}(Y_t,Y_{t-k})=\phi^k\,\text{Var}(Y_t)$, cioè $\rho_k=\phi^k$. Per un MA(1) $X_t=\epsilon_t+\theta\epsilon_{t-1}$ si ha $\text{Var}(X_t)=(1+\theta^2)\sigma^2$, $\text{Cov}(X_t,X_{t-1})=\theta\sigma^2$ e covarianza nulla oltre il ritardo 1, quindi $\rho_1=\theta/(1+\theta^2)$ e $\rho_k=0$ per $k\ge 2$. Un random walk $Z_t=Z_{t-1}+\epsilon_t$ con $Z_0=0$ è la somma $Z_t=\sum_{j=1}^{t}\epsilon_j$ e ha $\text{Var}(Z_t)=t\sigma^2$, che dipende da $t$: non è stazionario.

> [!example] Svolgimento
> **Impostazione.** Il processo A è un AR(1) con $|\phi|<1$, il B un MA(1), il C un AR(1) con $\phi=1$.
>
> **(a)** $E[Y_t]=\dfrac{c}{1-\phi}=\dfrac{ {{e06_01.c|m}} }{1-{{e06_01.phi|m}}}={{e06_01.media|m}}$.
>
> **(b)** $\text{Var}(Y_t)=\dfrac{\sigma^2}{1-\phi^2}=\dfrac{ {{e06_01.s2|m}} }{1-{{e06_01.phi|m}}^2}={{e06_01.var|m}}$.
>
> **(c)** $\rho_{ {{e06_01.k|m}} }=\phi^{ {{e06_01.k|m}} }={{e06_01.phi|m}}^{ {{e06_01.k|m}} }={{e06_01.rho_k|m}}$.
>
> **(d)** $\text{Var}(X_t)=(1+\theta^2)\,\sigma^2=\bigl(1+({{e06_01.theta|m}})^2\bigr)\times{{e06_01.s2|m}}={{e06_01.var_ma|m}}$.
>
> **(e)** $\rho_1=\dfrac{\theta}{1+\theta^2}=\dfrac{ {{e06_01.theta|m}} }{1+({{e06_01.theta|m}})^2}={{e06_01.rho1_ma|m}}$.
>
> **(f)** Il processo C è un AR(1) con $\phi=1$: $\text{Var}(Z_t)=t\,\sigma^2$ cresce con $t$.

> [!warning] Errore tipico
> Scrivere la varianza del MA(1) come $(1+\theta)\sigma^2$, o prendere $\text{Var}(Y_t)=\sigma^2$ per l'AR(1): la varianza dell'AR(1) è $\sigma^2$ divisa per $1-\phi^2$, perché lo shock di oggi si somma ai residui persistenti di quelli passati. Un altro errore è leggere la costante $c$ come media del processo: la media è $c/(1-\phi)$.

> [!success] Risposta
> **(a)** La media del processo A è ${{e06_01.media|m}}$. **(b)** La sua varianza è ${{e06_01.var|m}}$, maggiore di $\sigma^2$ per la persistenza. **(c)** L'autocorrelazione al ritardo ${{e06_01.k|m}}$ è ${{e06_01.rho_k|m}}$: decade geometricamente senza annullarsi. **(d)** La varianza del processo B è ${{e06_01.var_ma|m}}$. **(e)** La sua autocorrelazione al ritardo 1 è ${{e06_01.rho1_ma|m}}$ e dal ritardo 2 in poi è nulla. **(f)** No: il processo C è un random walk, con varianza che cresce linearmente nel tempo.

![ACF teorica (barre) e ACF di un campione simulato molto lungo (punti): l'AR(1) decade geometricamente, il MA(1) si annulla dopo il ritardo 1, con $\rho_1={{e06_01.rho1_ma|m}}$.]({{e06_01.fig.acf}}){width=85%}

{{testo:e06_02}}

> [!tip] Richiamo
> La banda di significatività al 5\% di un'autocorrelazione campionaria è $\pm 1{,}96/\sqrt{T}$. In una serie stazionaria l'ACF si spegne al crescere del ritardo, cioè rientra nella banda; in una serie con radice unitaria (random walk) l'ACF resta elevata, vicina a $1$, anche a ritardi alti, e la PACF ha un solo picco, vicino a $1$, al ritardo 1. In un AR($p$) stazionario la PACF si annulla oltre il ritardo $p$.

> [!example] Svolgimento
> **Impostazione.** La banda è $\pm 1{,}96/\sqrt{ {{e06_02.n|m}} }=\pm{{e06_02.banda|m}}$; si guarda se l'ACF rientra nella banda e quanti ritardi della PACF ne escono.
>
> **(a)** L'ACF di A vale ${{e06_02.acf1_a|m}}$ al ritardo 1 e rientra nella banda dal ritardo ${{e06_02.rientro|m}}$: la dipendenza si spegne, la serie è stazionaria.
>
> **(b)** L'ACF di B resta fuori banda a tutti i ${{e06_02.k|m}}$ ritardi, con valore minimo ${{e06_02.acf_b_min|m}}$, e la PACF vale ${{e06_02.pacf1_b|m}}$ al ritardo 1: è la forma di un random walk, la serie non è stazionaria.
>
> **(c)** La PACF di A esce dalla banda solo al ritardo 1, dove vale ${{e06_02.pacf1_a|m}}$: i ritardi fuori banda sono ${{e06_02.n_pacf|m}}$.

> [!warning] Errore tipico
> Concludere che B è stazionaria perché la PACF ha un solo picco, come per un AR(1): conta l'ACF, che per B non si spegne e per un AR(1) stazionario sì. Un picco della PACF vicino a $1$ non è la firma di un AR(1) stazionario, ma di un random walk.

> [!success] Risposta
> **(a)** Sì: l'ACF di A rientra nella banda dal ritardo ${{e06_02.rientro|m}}$. **(b)** No: l'ACF di B resta vicina a $1$ anche a ritardi alti, come per un random walk. **(c)** ${{e06_02.n_pacf|m}}$: solo il ritardo 1 della PACF di A esce dalla banda, come in un AR(1).

![ACF delle due serie con la banda al 5\%: A rientra nella banda dopo i primi ritardi, B resta fuori banda a tutti i ritardi.]({{e06_02.fig.acf}}){width=85%}

{{testo:e06_03}}

> [!tip] Richiamo
> La regressione di Dickey-Fuller aumentata è $\Delta y_t=\beta_0+\delta\,y_{t-1}+\sum_{j}\psi_j\,\Delta y_{t-j}+\epsilon_t$, con $\delta=\beta_1+\dots+\beta_p-1$ se $y_t$ è un AR($p$). Il sistema di ipotesi è $H_0:\delta=0$ (radice unitaria, serie non stazionaria) contro $H_1:\delta<0$ (serie stazionaria). La statistica è il rapporto $t=\hat\delta/\widehat{\text{se}}(\hat\delta)$ del coefficiente di $y_{t-1}$ e di nessun altro regressore. Sotto $H_0$ non ha distribuzione Normale: si confronta con il valore critico di Dickey-Fuller dato dal testo e si rifiuta $H_0$ solo se $t$ è minore di quel valore (coda sinistra).

> [!example] Svolgimento
> **Impostazione.** La statistica del test è il rapporto $t$ della riga del livello ritardato, `cambio_1` o `spread_1`.
>
> **(a)** $t=\hat\delta/\widehat{\text{se}}(\hat\delta)={{e06_03.ca|m}}/{{e06_03.sa|m}}={{e06_03.ta|m}}$.
>
> **(b)** $H_0:\delta=0$ contro $H_1:\delta<0$. Siccome ${{e06_03.ta|m}}>{{e06_03.crit|m}}$ non si rifiuta $H_0$: la serie va trattata come non stazionaria.
>
> **(c)** $t={{e06_03.cb|m}}/{{e06_03.sb|m}}={{e06_03.tb|m}}$.
>
> **(d)** Siccome ${{e06_03.tb|m}}<{{e06_03.crit|m}}$ si rifiuta $H_0$: `spread` è stazionaria.
>
> **(e)** Una sola serie, `spread`, è stazionaria: il numero richiesto è ${{e06_03.conta|m}}$.

> [!warning] Errore tipico
> Leggere il rapporto $t$ di `d_cambio_1` o `d_cambio_2`, che sono regressori di controllo e non c'entrano con la radice unitaria, oppure confrontare la statistica con $-1{,}96$ o $-1{,}64$: la distribuzione di Dickey-Fuller è spostata a sinistra rispetto alla Normale, per cui con la soglia normale si rifiuterebbe troppo spesso la non stazionarietà.

> [!success] Risposta
> **(a)** La statistica ADF di `cambio` è ${{e06_03.ta|m}}$. **(b)** È maggiore di ${{e06_03.crit|m}}$: non si rifiuta $H_0$, sembra plausibile un trend stocastico e `cambio` va trattata come non stazionaria. **(c)** La statistica di `spread` è ${{e06_03.tb|m}}$. **(d)** È minore di ${{e06_03.crit|m}}$: si rifiuta $H_0$ e `spread` è stazionaria. **(e)** ${{e06_03.conta|m}}$ serie su due è stazionaria.

![Statistiche ADF delle due serie rispetto al valore critico ${{e06_03.crit|m}}$: la regione di rifiuto è a sinistra (zona rosa). La linea grigia tratteggiata è la soglia normale, non appropriata per questo test.]({{e06_03.fig.stat}}){width=85%}

{{testo:e06_04}}

> [!tip] Richiamo
> Nel test di Dickey-Fuller si sceglie la componente deterministica dal grafico: se la serie non ha un andamento tendenziale netto si usa la sola costante; se ha un trend lineare netto si usano costante e trend, perché sotto $H_0$ il trend è il drift del random walk e sotto $H_1$ la serie è stazionaria attorno a una retta. Se $y_t$ è un AR($p$), la regressione aumentata ha $p-1$ ritardi della differenza. Scrivendo l'AR(3) come $y_t=\beta_0+\beta_1y_{t-1}+\beta_2y_{t-2}+\beta_3y_{t-3}+\epsilon_t$ e sottraendo $y_{t-1}$ si ottiene $\Delta y_t=\beta_0+\delta\,y_{t-1}+\psi_1\Delta y_{t-1}+\psi_2\Delta y_{t-2}+\epsilon_t$ con $\delta=\beta_1+\beta_2+\beta_3-1$, $\psi_1=-(\beta_2+\beta_3)$ e $\psi_2=-\beta_3$.

> [!example] Svolgimento
> **Impostazione.** Le prime due domande si decidono dal grafico e dalla tabella; la (c) e la (d) contano i termini; la (e) riscrive l'AR(3).
>
> **(a)** La media di `produzione` passa da ${{e06_04.m1_a|m}}$ nel primo terzo a ${{e06_04.m3_a|m}}$ nell'ultimo, molto più della deviazione standard (${{e06_04.sd_a|m}}$): c'è un trend lineare netto, quindi la regressione contiene costante e trend.
>
> **(b)** La media di `tasso` passa da ${{e06_04.m1_b|m}}$ a ${{e06_04.m3_b|m}}$, una differenza piccola rispetto alla deviazione standard (${{e06_04.sd_b|m}}$): la serie oscilla attorno a un livello costante, quindi basta la costante.
>
> **(c)** Per un AR($p$) con $p={{e06_04.p|m}}$ servono $p-1={{e06_04.ritardi|m}}$ ritardi della differenza.
>
> **(d)** Per `produzione` i regressori sono la costante, il trend `time`, il livello ritardato e i ${{e06_04.ritardi|m}}$ ritardi della differenza: $3+({{e06_04.p|m}}-1)={{e06_04.n_coef|m}}$ coefficienti.
>
> **(e)** $\delta=\beta_1+\beta_2+\beta_3-1={{e06_04.b1|m}}+({{e06_04.b2|m}})+{{e06_04.b3|m}}-1={{e06_04.delta|m}}$. Gli altri coefficienti sono $\psi_1=-(\beta_2+\beta_3)={{e06_04.psi1|m}}$ e $\psi_2=-\beta_3={{e06_04.psi2|m}}$.

> [!warning] Errore tipico
> Omettere il trend per `produzione`: se la serie è stazionaria attorno a una retta, un test con la sola costante tende a non rifiutare la radice unitaria. Per il coefficiente di $y_{t-1}$ non si può usare $\delta=\beta_1-1$ come nell'AR(1): con $p={{e06_04.p|m}}$ vale $\delta=\beta_1+\beta_2+\beta_3-1$. Un altro errore è contare i ritardi come $p$ invece che $p-1$.

> [!success] Risposta
> **(a)** Sì: `produzione` ha un trend lineare netto, la regressione ha costante e trend. **(b)** No: `tasso` oscilla attorno a un livello costante, basta la costante. **(c)** ${{e06_04.ritardi|m}}$ ritardi della differenza, cioè $p-1$. **(d)** ${{e06_04.n_coef|m}}$ coefficienti: costante, trend, livello ritardato e due differenze ritardate. **(e)** $\delta=\beta_1+\beta_2+\beta_3-1={{e06_04.delta|m}}$.

![Le due serie con la componente deterministica da inserire nella regressione di Dickey-Fuller: una retta per `produzione`, una costante per `tasso`.]({{e06_04.fig.componenti}}){width=85%}

{{testo:e06_05}}

> [!tip] Richiamo
> Il test ADF ha $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (stazionarietà); la statistica è il rapporto $t$ del coefficiente di $y_{t-1}$ e si confronta con un valore critico che dipende dalla specificazione: più negativo se la regressione contiene anche il trend. Se non si rifiuta $H_0$ la serie va trattata come se avesse un trend stocastico: va differenziata. Dopo aver differenziato si ripete il test sulla serie delle differenze: se questa risulta stazionaria, la serie originale è integrata di ordine 1.

> [!example] Svolgimento
> **Impostazione.** La statistica è il rapporto $t$ della riga `prezzo_1` (con trend) e della riga `dprezzo_1` (con sola costante).
>
> **(a)** $t=\hat\delta/\widehat{\text{se}}(\hat\delta)={{e06_05.c1|m}}/{{e06_05.s1|m}}={{e06_05.t1|m}}$.
>
> **(b)** $H_0:\delta=0$ contro $H_1:\delta<0$. Siccome ${{e06_05.t1|m}}>{{e06_05.crit_ct|m}}$ non si rifiuta $H_0$: `prezzo` va trattata come non stazionaria.
>
> **(c)** $t={{e06_05.c2|m}}/{{e06_05.s2|m}}={{e06_05.t2|m}}$.
>
> **(d)** Siccome ${{e06_05.t2|m}}<{{e06_05.crit_c|m}}$ si rifiuta $H_0$: `dprezzo` è stazionaria.
>
> **(e)** `prezzo` va trattata come una serie con trend stocastico ma le sue differenze risultano stazionarie: la serie è integrata di ordine 1 e va differenziata prima di essere usata in una regressione, salvo che sia cointegrata con le altre variabili (modulo 07).

> [!warning] Errore tipico
> Confrontare la statistica della regressione con il trend con il valore critico ${{e06_05.crit_c|m}}$, che vale per la sola costante: con il trend la soglia è ${{e06_05.crit_ct|m}}$. Un altro errore è dedurre la stazionarietà dal fatto che la serie cresce in modo regolare: sotto $H_0$ un random walk con drift cresce proprio così.

> [!success] Risposta
> **(a)** La statistica ADF di `prezzo` è ${{e06_05.t1|m}}$. **(b)** È maggiore di ${{e06_05.crit_ct|m}}$: non si rifiuta $H_0$ e `prezzo` va trattata come non stazionaria. **(c)** La statistica di `dprezzo` è ${{e06_05.t2|m}}$. **(d)** È minore di ${{e06_05.crit_c|m}}$: si rifiuta $H_0$, le differenze sono stazionarie. **(e)** Sì: `prezzo` è integrata di ordine 1 e va differenziata prima di una regressione, salvo che sia cointegrata con le altre variabili (modulo 07).

![Statistiche ADF di `prezzo` (costante e trend) e di `dprezzo` (costante) rispetto ai rispettivi valori critici al 5\%: la prima sta a destra, la seconda molto a sinistra della soglia.]({{e06_05.fig.stat}}){width=85%}

{{testo:e06_06}}

> [!tip] Richiamo
> Un random walk $y_t=y_{t-1}+v_t$ ha un trend stocastico e non è stazionario. Se $x_t$ e $y_t$ sono due random walk indipendenti, il vero valore di $\beta_1$ è $0$, ma lo stimatore OLS non converge a $0$, la statistica $t$ non ha distribuzione Normale (è molto più dispersa) e l'$R^2$ converge a una variabile casuale che può assumere valori elevati: la regressione appare significativa e ben adattata senza che esista alcuna relazione (regressione spuria). Per evitarla si differenziano le serie, che diventano stazionarie, e si regredisce in differenze.

> [!example] Svolgimento
> **Impostazione.** Si leggono i due test di significatività e i due $R^2$, tenendo presente che le serie sono indipendenti per costruzione.
>
> **(a)** $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. In livelli $\hat\beta_1={{e06_06.b_liv|m}}$ e $t={{e06_06.t_liv|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** L'$R^2$ in livelli è ${{e06_06.r2|m}}$.
>
> **(c)** No: $x_t$ e $y_t$ sono indipendenti per costruzione, quindi il risultato della (a) è un artefatto. Con trend stocastici la $t$ non è confrontabile con $1{,}96$, e un $R^2$ elevato non indica un buon modello.
>
> **(d)** In differenze $\hat\beta_1={{e06_06.b_dif|m}}$ e $t={{e06_06.t_dif|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$, e l'$R^2$ è ${{e06_06.r2_dif|m}}$. La relazione scompare, com'è giusto.

> [!warning] Errore tipico
> Fidarsi di un rapporto $t$ molto grande e di un $R^2$ alto quando le serie hanno trend stocastico: in una regressione spuria la regola $|t|>1{,}96$ rifiuta molto più spesso del $5\%$ delle volte. Un altro errore è concludere che le due serie siano davvero legate, o che il coefficiente stimato misuri un effetto.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\beta_1=0$: in livelli $t={{e06_06.t_liv|m}}$. **(b)** $R^2={{e06_06.r2|m}}$. **(c)** No: le serie sono indipendenti per costruzione, la significatività è spuria perché entrambe sono random walk. **(d)** Non si rifiuta $H_0:\beta_1=0$: in differenze $t={{e06_06.t_dif|m}}$ e $R^2={{e06_06.r2_dif|m}}$, cioè nessuna relazione.

![A sinistra le due serie indipendenti, che sembrano muoversi insieme. A destra la distribuzione simulata del rapporto $t$ nella regressione in livelli fra due random walk indipendenti: molto più dispersa della Normale standard, con le linee tratteggiate a $\pm 1{,}96$.]({{e06_06.fig.spuria}}){width=85%}

{{testo:e06_07}}

> [!tip] Richiamo
> Un AR($p$), $Y_t=\beta_0+\beta_1Y_{t-1}+\dots+\beta_pY_{t-p}+\epsilon_t$, ha ACF che decresce gradualmente e PACF significativa solo ai primi $p$ ritardi, poi nulla. Un MA($q$), $Y_t=\alpha+\epsilon_t+\theta_1\epsilon_{t-1}+\dots+\theta_q\epsilon_{t-q}$, ha ACF significativa solo ai primi $q$ ritardi, poi nulla, e PACF che decresce gradualmente. L'ordine è il ritardo a cui si ferma la funzione che si annulla. Un'ACF che rientra nella banda $\pm 1{,}96/\sqrt{T}$ al crescere del ritardo è compatibile con la stazionarietà; una che resta vicina a $1$ indica radice unitaria.

> [!example] Svolgimento
> **Impostazione.** La banda è $\pm 1{,}96/\sqrt{ {{e06_07.T|m}} }=\pm{{e06_07.banda|m}}$. Per ogni serie si cerca quale delle due funzioni si annulla dopo un certo ritardo.
>
> **(a)** La PACF di C esce dalla banda ai ritardi 1 (${{e06_07.pacf1_c|m}}$) e 2 (${{e06_07.pacf2_c|m}}$) e poi resta dentro; l'ACF decresce gradualmente, fuori banda fino al ritardo ${{e06_07.acf_c_ult|m}}$. È la forma di un AR.
>
> **(b)** La PACF si ferma al ritardo 2: AR(2), $Y_t=\beta_0+\beta_1Y_{t-1}+\beta_2Y_{t-2}+\epsilon_t$.
>
> **(c)** L'ACF di D esce dalla banda ai ritardi 1 (${{e06_07.acf1_d|m}}$) e 2 (${{e06_07.acf2_d|m}}$) e poi resta dentro; la PACF esce dalla banda in ${{e06_07.n_pacf_d|m}}$ ritardi, l'ultimo dei quali è il ${{e06_07.pacf_d_ult|m}}$, e decresce gradualmente invece di annullarsi. Non è un AR: è la forma di un MA.
>
> **(d)** L'ACF si ferma al ritardo 2: MA(2), $Y_t=\alpha+\epsilon_t+\theta_1\epsilon_{t-1}+\theta_2\epsilon_{t-2}$.
>
> **(e)** L'ACF di C decresce e rientra nella banda, quella di D si annulla dopo il ritardo 2: entrambe le serie sono stazionarie.

> [!warning] Errore tipico
> Scambiare i ruoli delle due funzioni: l'ordine di un AR si legge sulla PACF, quello di un MA sull'ACF. Un altro errore è contare come ordine l'ultimo ritardo fuori banda della funzione che decresce gradualmente: è quella che non si annulla e non indica l'ordine.

> [!success] Risposta
> **(a)** Sì: la PACF di C si annulla dopo il ritardo 2 mentre l'ACF decresce gradualmente. **(b)** Ordine ${{e06_07.ord_c|m}}$: AR(2). **(c)** No: l'ACF di D si annulla dopo il ritardo 2 e la PACF decresce gradualmente, quindi MA. **(d)** Ordine ${{e06_07.ord_d|m}}$: MA(2). **(e)** Sì: entrambe le serie sono stazionarie, perché la dipendenza si spegne.

![Correlogrammi campionari (punti) e pattern teorico di un AR(2) (a sinistra) e di un MA(2) (a destra): nell'AR si annulla la PACF, nel MA l'ACF.]({{e06_07.fig.teoria}}){width=92%}

{{testo:e06_08}}

> [!tip] Richiamo
> Il test ADF ha $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (stazionarietà). Sotto $H_0$ la statistica $t$ non ha distribuzione Normale, ma una distribuzione di Dickey-Fuller spostata a sinistra e che dipende dai termini deterministici: per questo si usano i valori critici o i p-value calcolati dal programma, non quelli della Normale. Si rifiuta $H_0$, e la serie risulta stazionaria, se il p-value è minore di $0{,}05$; altrimenti non si rifiuta la radice unitaria e la serie va trattata come non stazionaria, cioè differenziata.

> [!example] Svolgimento
> **Impostazione.** Per ogni serie si confronta il p-value del test con $0{,}05$.
>
> **(a)** Per `oro` il p-value è {{e06_08.p_oro}}, maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(b)** Per `argento` la statistica è ${{e06_08.stat_arg|m}}$ e il p-value è {{e06_08.p_arg}}, maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(c)** Per `tasso` il p-value è {{e06_08.p_tasso}}, minore di $0{,}05$: si rifiuta $H_0$.
>
> **(d)** Non si rifiuta $H_0$ per `oro` e `argento`, che vanno trattate come non stazionarie e differenziate: ${{e06_08.conta|m}}$ serie.
>
> **(e)** No: la statistica ADF non è Normale sotto $H_0$. Il confronto con $-1{,}64$ farebbe rifiutare per `argento`, ma il p-value di Dickey-Fuller {{e06_08.p_arg}} dice che il risultato è del tutto compatibile con una radice unitaria.

> [!warning] Errore tipico
> Usare la soglia della Normale ($-1{,}64$ o $-1{,}96$) per un test di radice unitaria: la distribuzione di Dickey-Fuller è spostata a sinistra, per cui la soglia vera è più negativa e il test con la soglia normale rifiuta la non stazionarietà troppo spesso. Un altro errore è leggere un p-value alto come prova di stazionarietà invece che come mancato rifiuto della radice unitaria.

> [!success] Risposta
> **(a)** `oro`: il p-value {{e06_08.p_oro}} è maggiore di $0{,}05$, non si rifiuta $H_0$. **(b)** `argento`: il p-value {{e06_08.p_arg}} è maggiore di $0{,}05$, non si rifiuta $H_0$. **(c)** `tasso`: il p-value {{e06_08.p_tasso}} è minore di $0{,}05$, si rifiuta $H_0$ e la serie è stazionaria. **(d)** ${{e06_08.conta|m}}$ serie: `oro` e `argento`. **(e)** No: la distribuzione della statistica ADF non è la Normale.

![Distribuzione simulata della statistica ADF sotto $H_0$ (istogramma) contro la Normale standard (tratteggio): la soglia di Dickey-Fuller al 5\% (rosso) è molto più a sinistra di $-1{,}64$, e la statistica di `argento` (verde) sta a destra di essa.]({{e06_08.fig.nulla}}){width=85%}

{{testo:e06_09}}

> [!tip] Richiamo
> Con un break in una data nota $\tau$ si scrive il modello con la dummy $D_t=1$ per $t>\tau$ e le sue interazioni; il test di Chow verifica $H_0:\gamma_0=\gamma_1=0$ (parametri uguali nei due sottocampioni). È il test $F$ di $k$ restrizioni, dove il modello vincolato è quello sull'intero campione e il non vincolato è la coppia dei modelli sui due sottocampioni:
> $$F=\frac{(\text{SSR}_1-\text{SSR}_2-\text{SSR}_3)/k}{(\text{SSR}_2+\text{SSR}_3)/(T-2k)},$$
> con $k$ il numero di parametri del modello (qui costante e pendenza, $k=2$). Si rifiuta $H_0$ se $F$ supera il valore critico della $F(k,T-2k)$.

> [!example] Svolgimento
> **Impostazione.** Servono solo le tre somme dei quadrati dei residui, il numero di osservazioni e $k=2$.
>
> **(a)** $F=\dfrac{({{e06_09.ssr_p|m}}-{{e06_09.ssr_1|m}}-{{e06_09.ssr_2|m}})/2}{({{e06_09.ssr_1|m}}+{{e06_09.ssr_2|m}})/({{e06_09.T|m}}-4)}={{e06_09.F|m}}$.
>
> **(b)** Siccome ${{e06_09.F|m}}>{{e06_09.fcrit|m}}$ si rifiuta $H_0$: i parametri cambiano dopo la riforma.
>
> **(c)** $\hat\beta_1^{(3)}-\hat\beta_1^{(2)}={{e06_09.b2|m}}-{{e06_09.b1|m}}={{e06_09.salto|m}}$.
>
> **(d)** Il denominatore ha $T-2k={{e06_09.T|m}}-4={{e06_09.gl|m}}$ gradi di libertà; il numeratore ne ha $k=2$.

> [!warning] Errore tipico
> Dimenticare i gradi di libertà, cioè dividere per $\text{SSR}_2+\text{SSR}_3$ senza il fattore $T-2k$ e non dividere il numeratore per $k$. Un altro errore è confrontare le SSR in modo sbagliato: il modello vincolato è quello sull'intero campione, che ha la SSR più grande.

> [!success] Risposta
> **(a)** $F={{e06_09.F|m}}$. **(b)** È maggiore del valore critico ${{e06_09.fcrit|m}}$: si rifiuta $H_0$, c'è un break strutturale alla data della riforma. **(c)** La pendenza di `reddito` cambia di ${{e06_09.salto|m}}$: dopo la riforma è più bassa. **(d)** ${{e06_09.gl|m}}$ gradi di libertà.

![Le osservazioni dei due sottocampioni con le loro rette di regressione (continue) e quella dell'intero campione (tratteggiata): una sola retta non descrive i due regimi.]({{e06_09.fig.rette}}){width=85%}

{{testo:e06_10}}

> [!tip] Richiamo
> Il test di Chow in una data fissata $\tau$ usa $F(\tau)=\dfrac{(\text{SSR}-\text{SSR}_1-\text{SSR}_2)/2}{(\text{SSR}_1+\text{SSR}_2)/(T-4)}$ per il modello con costante e un regressore. Se la data è ignota si calcola $F(\tau)$ per ogni data, escludendo il 15\% iniziale e finale, e la statistica QLR è il massimo, $\text{QLR}=\max_\tau F(\tau)$. Il massimo di molte statistiche $F$ è più grande di una singola $F$: la sua distribuzione sotto $H_0$ non è la $F$ e va confrontato con il valore critico del QLR, più alto del valore critico della $F$ usuale.

> [!example] Svolgimento
> **Impostazione.** La statistica QLR è la $F$ di Chow nella data $\hat\tau$, in cui la sequenza $F(\tau)$ è massima; la si confronta con il valore critico del QLR.
>
> **(a)** $\text{QLR}=F(\hat\tau)=\dfrac{({{e06_10.ssr_p|m}}-{{e06_10.ssr_1|m}}-{{e06_10.ssr_2|m}})/2}{({{e06_10.ssr_1|m}}+{{e06_10.ssr_2|m}})/({{e06_10.T|m}}-4)}={{e06_10.F|m}}$.
>
> **(b)** $H_0$: nessun break contro $H_1$: break in almeno una data. Siccome ${{e06_10.F|m}}<{{e06_10.qcrit|m}}$ non si rifiuta $H_0$.
>
> **(c)** Con il valore critico della $F$ usuale, ${{e06_10.fcrit|m}}$, si avrebbe ${{e06_10.F|m}}>{{e06_10.fcrit|m}}$ e si rifiuterebbe $H_0$: un confronto sbagliato, perché la data $\hat\tau$ è stata scelta proprio come quella in cui $F$ è più grande.
>
> **(d)** Non si rifiuta $H_0$ nemmeno nella data in cui la statistica è massima: non c'è evidenza di break.

> [!warning] Errore tipico
> Confrontare il massimo delle $F(\tau)$ con il valore critico di una $F$ in una data fissata: la ricerca della data più sfavorevole gonfia la statistica e il test rifiuterebbe troppo spesso. Con data ignota si usa il valore critico del QLR.

> [!success] Risposta
> **(a)** La statistica QLR è ${{e06_10.F|m}}$. **(b)** È minore del valore critico ${{e06_10.qcrit|m}}$ del QLR: non si rifiuta $H_0$. **(c)** Sì, la si rifiuterebbe, ma il confronto sarebbe sbagliato perché il massimo di molte $F$ non si distribuisce come una $F$. **(d)** No: non emerge evidenza di break.

![Sequenza delle statistiche di Chow $F(\tau)$: il massimo (punto verde) supera il valore critico della $F$ usuale (tratteggio) ma non quello del QLR (linea rossa).]({{e06_10.fig.percorso}}){width=85%}

{{testo:e06_11}}

> [!tip] Richiamo
> La componente deterministica del test di Dickey-Fuller si sceglie dal grafico: con un trend lineare netto la regressione contiene costante e trend, perché sotto $H_0$ la serie è un random walk con drift e sotto $H_1$ è stazionaria attorno a una retta. Il valore critico dipende dalla specificazione ed è più negativo con il trend. Si rifiuta $H_0:\delta=0$ contro $H_1:\delta<0$ se $t=\hat\delta/\widehat{\text{se}}(\hat\delta)$ è minore del valore critico. Omettere un trend che c'è sposta la statistica verso lo zero e fa non rifiutare la radice unitaria. Se $y_t$ è un AR($p$) con trend, la regressione aumentata ha $\delta=\beta_1+\dots+\beta_p-1$.

> [!example] Svolgimento
> **Impostazione.** Il grafico decide quale modello usare; poi si legge la statistica di quel modello (riga `pil_1`) e la si confronta con il suo valore critico.
>
> **(a)** La media di `pil` passa da ${{e06_11.m1|m}}$ a ${{e06_11.m3|m}}$, più della deviazione standard (${{e06_11.sd|m}}$): c'è un trend lineare netto, quindi il modello appropriato è il Modello 2.
>
> **(b)** $t=\hat\delta/\widehat{\text{se}}(\hat\delta)={{e06_11.c2|m}}/{{e06_11.s2|m}}={{e06_11.t2|m}}$.
>
> **(c)** $H_0:\delta=0$ contro $H_1:\delta<0$. Siccome ${{e06_11.t2|m}}<{{e06_11.crit_ct|m}}$ si rifiuta $H_0$.
>
> **(d)** Si rifiuta la radice unitaria in una regressione che contiene il trend: la serie è stazionaria attorno a un trend deterministico.
>
> **(e)** Nel Modello 1 la statistica è ${{e06_11.t1|m}}$, maggiore di ${{e06_11.crit_c|m}}$: non si rifiuterebbe $H_0$. La decisione è opposta, perché il Modello 1 omette il trend.
>
> **(f)** $\delta=\beta_1+\beta_2+\beta_3-1$, quindi $\hat\beta_1+\hat\beta_2+\hat\beta_3=1+\hat\delta=1+({{e06_11.c2|m}})={{e06_11.somma|m}}$.

> [!warning] Errore tipico
> Fermarsi al Modello 1, che ha la statistica più vicina allo zero, e concludere che `pil` ha una radice unitaria: la serie cresce lungo una retta e senza il trend nella regressione il test tende a non rifiutare. Un altro errore è confrontare la statistica del Modello 2 con ${{e06_11.crit_c|m}}$, valore critico della sola costante, invece che con ${{e06_11.crit_ct|m}}$.

> [!success] Risposta
> **(a)** Sì: la serie ha un trend lineare netto e il modello appropriato ha costante e trend. **(b)** La statistica ADF del Modello 2 è ${{e06_11.t2|m}}$. **(c)** È minore di ${{e06_11.crit_ct|m}}$: si rifiuta $H_0$. **(d)** Sì: `pil` è stazionaria attorno a un trend deterministico. **(e)** No: il Modello 1 darebbe ${{e06_11.t1|m}}$, maggiore di ${{e06_11.crit_c|m}}$, quindi non rifiuterebbe, per l'omissione del trend. **(f)** $\hat\beta_1+\hat\beta_2+\hat\beta_3=1+\hat\delta={{e06_11.somma|m}}$.

![Sopra, la serie con la sua retta di trend. Sotto, le due statistiche ADF contro i rispettivi valori critici: senza trend (grigio) cade fuori dalla regione di rifiuto, con il trend (verde) ci cade dentro.]({{e06_11.fig.test}}){width=85%}

{{testo:e06_12}}

> [!tip] Richiamo
> Una serie con radice unitaria ha un'ACF che resta vicina a $1$ anche a ritardi alti e una PACF con un solo picco, vicino a $1$, al ritardo 1: non è stazionaria e si differenzia. Sulla serie differenziata si identifica il modello: ACF significativa solo ai primi $q$ ritardi e PACF che decresce gradualmente indicano un MA($q$); il contrario un AR($p$). Per un MA(1), $\rho_1=\theta/(1+\theta^2)$: uguagliando a $\hat\rho_1$ si ottiene $\hat\rho_1\theta^2-\theta+\hat\rho_1=0$, con soluzioni $\theta=\bigl(1\pm\sqrt{1-4\hat\rho_1^2}\bigr)/(2\hat\rho_1)$ il cui prodotto è $1$: una sola ha $|\theta|<1$.

> [!example] Svolgimento
> **Impostazione.** La banda è $\pm 1{,}96/\sqrt{ {{e06_12.T|m}} }=\pm{{e06_12.banda|m}}$. Prima si decide la stazionarietà di $y_t$ e di $\Delta y_t$, poi si identifica il modello della differenza.
>
> **(a)** L'ACF di $y_t$ resta fuori banda a tutti i ritardi, con valore minimo ${{e06_12.acf_y_min|m}}$, e la PACF vale ${{e06_12.pacf1_y|m}}$ al ritardo 1: è la firma di un random walk, $y_t$ non è stazionaria. Il picco unico della PACF non è un AR(1) stazionario.
>
> **(b)** L'ACF di $\Delta y_t$ ha un solo ritardo fuori banda e poi rientra: $\Delta y_t$ è stazionaria.
>
> **(c)** L'ACF di $\Delta y_t$ è fuori banda solo al ritardo 1 (${{e06_12.acf1_d|m}}$), mentre la PACF esce dalla banda in ${{e06_12.n_pacf_d|m}}$ ritardi, l'ultimo dei quali è il ${{e06_12.pacf_d_ult|m}}$, decrescendo gradualmente invece di annullarsi dopo il primo: non è un AR, è un MA.
>
> **(d)** L'ACF si ferma al ritardo ${{e06_12.ord_d|m}}$: MA(1), $\Delta y_t=\alpha+\epsilon_t+\theta\epsilon_{t-1}$.
>
> **(e)** $\theta=\dfrac{1-\sqrt{1-4\hat\rho_1^2}}{2\hat\rho_1}=\dfrac{1-\sqrt{1-4\times({{e06_12.rho1|m}})^2}}{2\times({{e06_12.rho1|m}})}={{e06_12.theta|m}}$. L'altra soluzione è $1/\theta={{e06_12.theta_alt|m}}$, con $|\theta|>1$, e si scarta.

> [!warning] Errore tipico
> Identificare un AR(1) sulla serie in livello perché la PACF ha un solo picco: con un'ACF che non si spegne la serie non è stazionaria e il modello va cercato sulla differenza. Un altro errore è tenere entrambe le soluzioni dell'equazione per $\theta$: ne esiste una sola con $|\theta|<1$.

> [!success] Risposta
> **(a)** No: l'ACF di $y_t$ resta vicina a $1$, come per un random walk. **(b)** Sì: l'ACF di $\Delta y_t$ rientra in banda dopo il ritardo 1. **(c)** No: l'ACF di $\Delta y_t$ si annulla dopo il ritardo 1 mentre la PACF decresce gradualmente, quindi MA. **(d)** Ordine ${{e06_12.ord_d|m}}$: MA(1). **(e)** $\theta={{e06_12.theta|m}}$, la soluzione con $|\theta|<1$ di $\hat\rho_1=\theta/(1+\theta^2)$ con $\hat\rho_1={{e06_12.rho1|m}}$.

![La relazione $\rho_1=\theta/(1+\theta^2)$: per $\hat\rho_1={{e06_12.rho1|m}}$ (tratteggio) ci sono due soluzioni, $\theta={{e06_12.theta|m}}$ e $1/\theta={{e06_12.theta_alt|m}}$; si tiene quella con $|\theta|<1$.]({{e06_12.fig.radici}}){width=85%}

{{testo:e06_13}}

> [!tip] Richiamo
> Se la relazione cambia a una data ignota, la statistica QLR è il massimo delle statistiche di Chow $F(\tau)$ sulle date candidate (escluso il 15\% iniziale e finale), e $F(\tau)=\dfrac{(\text{SSR}_1-\text{SSR}_2-\text{SSR}_3)/k}{(\text{SSR}_2+\text{SSR}_3)/(T-2k)}$, con il Modello 1 sull'intero campione e i Modelli 2 e 3 sui due sottocampioni, $k=2$. Si rifiuta $H_0$ (parametri stabili) se il QLR supera il suo valore critico, che è più alto di quello della $F$ usuale. Un break può mascherare una relazione sull'intero campione: se la pendenza ha segni opposti nei due regimi, la stima sull'intero campione può risultare vicina a zero e non descrive nessuno dei due regimi.

> [!example] Svolgimento
> **Impostazione.** Si legge il test di significatività del Modello 1, si calcola la $F$ di Chow in $\hat\tau$ dalle tre SSR e la si confronta con il valore critico del QLR; poi si confrontano le due pendenze.
>
> **(a)** $H_0:\beta=0$ contro $H_1:\beta\neq 0$. Nel Modello 1 $\hat\beta={{e06_13.b_pieno|m}}$ e $t={{e06_13.t_pieno|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.
>
> **(b)** $\text{QLR}=F(\hat\tau)=\dfrac{({{e06_13.ssr_p|m}}-{{e06_13.ssr_1|m}}-{{e06_13.ssr_2|m}})/2}{({{e06_13.ssr_1|m}}+{{e06_13.ssr_2|m}})/({{e06_13.T|m}}-4)}={{e06_13.F|m}}$.
>
> **(c)** $H_0$: parametri stabili contro $H_1$: break in almeno una data. Siccome ${{e06_13.F|m}}>{{e06_13.qcrit|m}}$ si rifiuta $H_0$: c'è un break strutturale.
>
> **(d)** No: il Modello 1 mescola due regimi diversi e la sua conclusione, che il mercato non spiega il rendimento, non è affidabile.
>
> **(e)** $\hat\beta^{(3)}-\hat\beta^{(2)}={{e06_13.b2|m}}-{{e06_13.b1|m}}={{e06_13.salto|m}}$: la pendenza passa da positiva a negativa.

> [!warning] Errore tipico
> Fermarsi al Modello 1 e concludere che non c'è relazione fra mercato e titolo: i due regimi hanno pendenze di segno opposto (${{e06_13.b1|m}}$ e ${{e06_13.b2|m}}$) che nell'intero campione si compensano, per cui la stima ${{e06_13.b_pieno|m}}$ è vicina a zero. Un altro errore è non dividere per i gradi di libertà nel calcolo della $F$.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0:\beta=0$: sull'intero campione $t={{e06_13.t_pieno|m}}$. **(b)** La statistica QLR è ${{e06_13.F|m}}$. **(c)** È maggiore di ${{e06_13.qcrit|m}}$: si rifiuta $H_0$, c'è un break strutturale in $\hat\tau$. **(d)** No: il risultato sull'intero campione è un artefatto del break, perché la pendenza ha segno opposto nei due regimi. **(e)** La pendenza cambia di ${{e06_13.salto|m}}$.

![A sinistra, le osservazioni dei due regimi con le loro rette e la retta dell'intero campione (tratteggiata), quasi piatta. A destra, la sequenza delle statistiche di Chow: il massimo (punto verde) supera di molto il valore critico del QLR (linea rossa).]({{e06_13.fig.rotture}}){width=85%}
