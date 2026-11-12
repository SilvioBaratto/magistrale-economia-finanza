{{testo:a04_01}}

## Soluzione della Domanda 1 — Elasticità del prezzo rispetto all'inquinamento nelle aree vicine

> [!tip] Richiamo
> Con la dipendente e il regressore in logaritmo $\Delta\log(y)=\beta\,\Delta\log(x)$ e, poiché $\Delta\log(z)\approx\Delta z/z$, si ha $\Delta y/y\approx\beta\,\Delta x/x$: $\beta$ è l'elasticità, e una variazione di $x$ del $m$ per cento fa variare $y$ di $\beta\,m$ per cento. Con l'interazione $\text{d\_nox}=\text{lontano}\cdot(\text{l\_nox}-c)$ l'effetto di $\text{l\_nox}$ è $\beta_1+\beta_5\,\text{lontano}$: per $\text{lontano}=0$ il termine d'interazione si annulla e l'elasticità è $\beta_1$.

> [!example] Svolgimento
> **Impostazione.** Per le aree vicine $\text{d\_nox}=0$, quindi il modello è log-log nella sola $\text{l\_nox}$ e $\beta_1$ è l'elasticità.
>
> **(a)** $\hat\beta_1={{a04_01.el|m}}$.
>
> **(b)** $\Delta\%\,\text{prezzo}\approx\hat\beta_1\times\Delta\%\,\text{nox}={{a04_01.el|m}}\times{{a04_01.var|m}}={{a04_01.pct|m}}\%$.

> [!warning] Errore tipico
> Moltiplicare $\hat\beta_1$ per $100$ come si fa con un regressore in livello: qui $\hat\beta_1$ è già il rapporto fra due variazioni percentuali, e $100\times\hat\beta_1$ darebbe la variazione per $\Delta\log(\text{nox})=1$, non per un raddoppio: un raddoppio è $\Delta\log(\text{nox})=\ln 2$ e l'approssimazione lineare non regge per variazioni così grandi. Un altro errore è leggere $\hat\beta_1$ come l'elasticità di tutte le aree: vale solo per $\text{lontano}=0$.

> [!success] Risposta
> **(a)** L'elasticità del prezzo rispetto all'inquinamento nelle aree vicine al centro è ${{a04_01.el|m}}$: a ogni aumento dell'1\% di `nox` il prezzo atteso varia di circa ${{a04_01.el|m}}\%$. **(b)** Con `nox` $+{{a04_01.var|m}}\%$ il prezzo atteso varia di circa ${{a04_01.pct|m}}\%$.

![Variazione percentuale attesa del prezzo al variare di `nox` nelle aree vicine: retta di pendenza $\hat\beta_1={{a04_01.el|m}}$ con banda al 95\%. Per $+{{a04_01.var|m}}\%$ di `nox` il prezzo varia di ${{a04_01.pct|m}}\%$.]({{a04_01.fig.elasticita}}){width=85%}

## Soluzione della Domanda 2 — L'elasticità dipende dalla distanza?

> [!tip] Richiamo
> Derivando il modello rispetto a $\text{l\_nox}$ si ottiene l'effetto marginale $\partial\log(\text{prezzo})/\partial\text{l\_nox}=\beta_1+\beta_5\,\text{lontano}$, che dipende dalla dummy. Per le aree lontane vale $\beta_1+\beta_5$ e la sua varianza è $\text{Var}(\hat\beta_1)+\text{Var}(\hat\beta_5)+2\,\text{Cov}(\hat\beta_1,\hat\beta_5)$. L'elasticità dipende dalla distanza se $\beta_5\neq 0$: si confronta $t=\hat\beta_5/\widehat{\text{se}}(\hat\beta_5)$ con $1{,}96$. Un test diverso è quello su $\beta_1+\beta_5=0$, che chiede se per le aree lontane l'inquinamento incide sul prezzo.

> [!example] Svolgimento
> **Impostazione.** La (a) somma i due coefficienti; la (b) è un test su $\beta_5$; la (c) è un test su una combinazione lineare e usa la covarianza.
>
> **(a)** $\hat\beta_1+\hat\beta_5={{a04_01.b_nox|m}}+{{a04_01.b_int|m}}={{a04_01.eff6|m}}$, cioè ${{a04_01.eff|m}}$.
>
> **(b)** $t={{a04_01.b_int|m}}/{{a04_01.se_int|m}}={{a04_01.t_int|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(c)** $\widehat{\text{se}}(\hat\beta_1+\hat\beta_5)=\sqrt{ {{a04_01.se_nox|m}}^2+{{a04_01.se_int|m}}^2+2\times({{a04_01.cov|m}}) }={{a04_01.se_comb|m}}$ e $t={{a04_01.eff6|m}}/{{a04_01.se_comb|m}}={{a04_01.t_comb|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.

> [!warning] Errore tipico
> Sommare i due errori standard senza la covarianza, oppure usare $\widehat{\text{se}}(\hat\beta_5)$ per la combinazione. Un altro errore è dedurre dalla non significatività di $\hat\beta_1+\hat\beta_5$ che l'elasticità non cambi con la distanza: le due domande sono diverse. Qui l'elasticità è molto diversa fra aree vicine e lontane ($\beta_5$ è significativo), ma nelle aree lontane non si distingue da zero.

> [!success] Risposta
> **(a)** Nelle aree lontane l'elasticità stimata è ${{a04_01.eff|m}}$, molto più vicina a zero di quella delle aree vicine. **(b)** Si rifiuta $H_0:\beta_5=0$: l'elasticità dipende dalla distanza dal centro. **(c)** Non si rifiuta $H_0:\beta_1+\beta_5=0$: per le aree lontane i dati non permettono di distinguere l'effetto dell'inquinamento sul prezzo da zero.

![Variazione percentuale attesa del prezzo al variare di `nox`: nelle aree vicine la pendenza è ${{a04_01.el|m}}$, nelle aree lontane ${{a04_01.eff|m}}$ e la banda al 95\% contiene la retta orizzontale.]({{a04_01.fig.interazione}}){width=85%}

## Soluzione della Domanda 3 — Test su un valore specifico: l'effetto di un reato in più

> [!tip] Richiamo
> Per verificare che un effetto valga un valore dato $\theta_0$ si costruisce $t=(\hat\theta-\theta_0)/\widehat{\text{se}}(\hat\theta)$ e si rifiuta $H_0:\theta=\theta_0$ al 5\% se $|t|>1{,}96$. Con la dipendente in logaritmo la variazione percentuale per un reato in più è $100\,\beta_2$, quindi $H_0:100\,\beta_2=-{{a04_01.riv|m}}$ equivale a $\beta_2=-{{a04_01.riv|m}}/100$. Equivalentemente si rifiuta se il valore sotto $H_0$ cade fuori dall'intervallo di confidenza al 95\%.

> [!example] Svolgimento
> **Impostazione.** Il valore sotto $H_0$ non è zero: lo zero della tabella non c'entra.
>
> **(a)** $t=\dfrac{\hat\beta_2-(-{{a04_01.riv|m}}/100)}{\widehat{\text{se}}(\hat\beta_2)}=\dfrac{ {{a04_01.b_crime|m}}+{{a04_01.riv|m}}/100 }{ {{a04_01.se_crime|m}} }={{a04_01.t_valore|m}}$.
>
> **(b)** $|t|<1{,}96$: non si rifiuta $H_0$. In percentuale l'intervallo di confidenza al 95\% per $100\,\beta_2$ è $[{{a04_01.ic_lo|m}};\,{{a04_01.ic_hi|m}}]$ e contiene $-{{a04_01.riv|m}}$.

> [!warning] Errore tipico
> Usare il rapporto $t$ della tabella, ${{a04_01.t_crime|m}}$, che verifica $H_0:\beta_2=0$: la tabella dice che l'effetto dei reati è significativo, non che valga $-{{a04_01.riv|m}}\%$. Un altro errore è confrontare $\hat\beta_2$ con $-{{a04_01.riv|m}}$ senza dividere per $100$.

> [!success] Risposta
> **(a)** Il rapporto $t$ vale ${{a04_01.t_valore|m}}$. **(b)** Non si rifiuta $H_0$: l'affermazione del comitato (un reato in più riduce il prezzo del ${{a04_01.riv|m}}\%$) è compatibile con i dati, e la stima è una variazione di ${{a04_01.b_crime|m}}$ in logaritmi per reato, cioè di circa ${{a04_01.pct_crime|m}}\%$.

![Intervallo di confidenza al 95\% per la variazione percentuale del prezzo dovuta a un reato in più: contiene $-{{a04_01.riv|m}}\%$.]({{a04_01.fig.valore}}){width=85%}

## Soluzione della Domanda 4 — Test unilaterale sulla soglia per le stanze

> [!tip] Richiamo
> Con la dipendente in logaritmo $\Delta\%\,y\approx 100\,\beta\,\Delta x$, quindi per ${{a04_01.delta|m}}$ stanze in più la variazione di $\log(\text{prezzo})$ è ${{a04_01.delta|m}}\,\beta_3$. «Più del ${{a04_01.perc|m}}\%$» dà un sistema unilaterale: $H_0:{{a04_01.delta|m}}\,\beta_3\le{{a04_01.lim|m}}$ contro $H_1:{{a04_01.delta|m}}\,\beta_3>{{a04_01.lim|m}}$, cioè $H_0:\beta_3\le s$ con $s={{a04_01.lim|m}}/{{a04_01.delta|m}}$. Si costruisce $t=(\hat\beta_3-s)/\widehat{\text{se}}(\hat\beta_3)$ e, a una coda al 5\%, si rifiuta se $t>1{,}64$.

> [!example] Svolgimento
> **Impostazione.** La soglia entra nel numeratore del rapporto $t$; la regione di rifiuto è la sola coda destra.
>
> **(a)** $s={{a04_01.lim|m}}/{{a04_01.delta|m}}={{a04_01.soglia|m}}$.
>
> **(b)** $t=\dfrac{ {{a04_01.b_rooms|m}}-{{a04_01.soglia6|m}} }{ {{a04_01.se_rooms|m}} }={{a04_01.t_soglia|m}}$.
>
> **(c)** $t>1{,}64$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Dimenticare di dividere per ${{a04_01.delta|m}}$, cioè confrontare $\hat\beta_3$ con ${{a04_01.lim|m}}$ anziché con la soglia $s$ sul singolo coefficiente. Un altro errore è usare il rapporto $t$ della tabella, ${{a04_01.t_rooms|m}}$, che verifica $H_0:\beta_3=0$, oppure una regione bilaterale: qui $t$ supera anche $1{,}96$, ma in generale per un test a una coda la soglia al 5\% è $1{,}64$.

> [!success] Risposta
> **(a)** La soglia sul coefficiente è ${{a04_01.soglia|m}}$. **(b)** Il rapporto $t$ vale ${{a04_01.t_soglia|m}}$. **(c)** Si rifiuta $H_0$: ${{a04_01.delta|m}}$ stanze in più fanno aumentare il prezzo atteso di più del ${{a04_01.perc|m}}\%$ (la stima è circa ${{a04_01.pct_stanze|m}}\%$).

![Statistica $t={{a04_01.t_soglia|m}}$ contro la regione di rifiuto a una coda ($t>1{,}64$).]({{a04_01.fig.soglia}}){width=85%}

## Soluzione della Domanda 5 — Dummy e variazione necessaria del regressore

> [!tip] Richiamo
> Con la dipendente in logaritmo, per un regressore $x$ vale $\Delta\%\,y\approx 100\,\beta\,\Delta x$; per ottenere una variazione obiettivo si inverte, $\Delta x=(\Delta\%\,y/100)/\beta$. Con l'interazione, la differenza fra un'area lontana e una vicina a parità delle altre variabili è $\beta_4+\beta_5\,(\text{l\_nox}-c)$: a $\text{l\_nox}=c$ il secondo termine si annulla e resta $\beta_4$, con $\Delta\%\,y\approx 100\,\beta_4$.

> [!example] Svolgimento
> **Impostazione.** La (a) legge la dummy nel punto di riferimento dell'inquinamento; la (b) inverte l'effetto di `rooms`.
>
> **(a)** $100\,\hat\beta_4=100\times({{a04_01.b_lont|m}})={{a04_01.pct_lont|m}}\%$.
>
> **(b)** $\Delta\text{rooms}=\dfrac{ {{a04_01.ob|m}}/100 }{ \hat\beta_3 }=\dfrac{ {{a04_01.ob|m}}/100 }{ {{a04_01.b_rooms|m}} }={{a04_01.stanze|m}}$ stanze.

> [!warning] Errore tipico
> Leggere $\hat\beta_4$ come la differenza fra aree lontane e vicine a qualsiasi livello di inquinamento: vale solo per $\text{l\_nox}=c$, altrove si aggiunge $\hat\beta_5\,(\text{l\_nox}-c)$. Per la (b), un altro errore è dividere ${{a04_01.ob|m}}$ per $\hat\beta_3$ senza passare da $100$, ottenendo un numero cento volte più grande.

> [!success] Risposta
> **(a)** A parità di tutto e con `nox` al livello di riferimento, la differenza fra il prezzo atteso di un'area lontana dal centro e quello di un'area vicina (lontana meno vicina) è di circa ${{a04_01.pct_lont|m}}\%$: l'area lontana costa meno. **(b)** Servono circa ${{a04_01.stanze|m}}$ stanze in più perché il prezzo atteso aumenti del ${{a04_01.ob|m}}\%$.

![Sopra: variazione percentuale del prezzo al crescere delle stanze; l'obiettivo del ${{a04_01.ob|m}}\%$ si raggiunge con ${{a04_01.stanze|m}}$ stanze in più. Sotto: intervallo al 95\% per la differenza percentuale lontano meno vicino, ${{a04_01.pct_lont|m}}\%$.]({{a04_01.fig.percentuali}}){width=85%}

## Soluzione della Domanda 6 — Che cosa dice il test di White

> [!tip] Richiamo
> Il test di White ha $H_0$: omoschedasticità, cioè $\text{Var}(\epsilon\mid X)$ costante. La statistica è $LM=nR^2$ della regressione ausiliaria di $\hat\epsilon^2$ e sotto $H_0$ si distribuisce come un $\chi^2$ con tanti gradi di libertà quanti sono i regressori ausiliari; si rifiuta se il p-value è minore di $0{,}05$. L'eteroschedasticità riguarda la varianza dell'errore, non la sua media: se $E[\epsilon\mid X]=0$ gli stimatori OLS restano non distorti e consistenti. Ciò che cade è la formula usuale dell'errore standard, e si usano errori standard robusti.

> [!example] Svolgimento
> **Impostazione.** La (a) legge il p-value; la (b) e la (c) separano ciò che l'eteroschedasticità implica da ciò che non implica.
>
> **(a)** $LM={{a04_01.lm|m}}$ con ${{a04_01.gl|m}}$ gradi di libertà e p-value {{a04_01.p_white}}, minore di $0{,}05$: si rifiuta $H_0$.
>
> **(b)** Il test riguarda $E[\epsilon^2\mid X]$, non $E[\epsilon\mid X]$: dal rifiuto non segue alcuna distorsione.
>
> **(c)** Gli errori standard della tabella sono HC1, validi anche con $\text{Var}(\epsilon\mid X)$ non costante; quelli usuali non lo sono.

> [!warning] Errore tipico
> Leggere il rifiuto di $H_0$ come prova che il modello sia endogeno o che le stime siano distorte. Il test dice soltanto che $\text{Var}(\epsilon\mid X)$ non è costante, e con $E[\epsilon\mid X]=0$ i coefficienti restano non distorti; a cambiare è l'errore standard. Per questo i test $t$ delle domande precedenti usano gli errori standard robusti della tabella.

> [!success] Risposta
> **(a)** Si rifiuta l'omoschedasticità: il p-value è {{a04_01.p_white}}, molto minore del 5\%. **(b)** No: l'eteroschedasticità non dice nulla su $E[\epsilon\mid X]$, quindi non permette di concludere che gli stimatori siano distorti. **(c)** Sì: con eteroschedasticità gli errori standard robusti sono validi, quelli usuali no.

![Statistica di White $LM={{a04_01.lm|m}}$ contro la regione di rifiuto del $\chi^2$ con ${{a04_01.gl|m}}$ gradi di libertà.]({{a04_01.fig.white}}){width=85%}

{{testo:a04_02}}

## Soluzione della Domanda 7 — Le due serie hanno una radice unitaria?

> [!tip] Richiamo
> Nel test ADF l'ipotesi nulla è la radice unitaria (non stazionarietà, comportamento da random walk) contro l'alternativa di stazionarietà. Si rifiuta $H_0$ solo se il p-value è minore di $0{,}05$; un p-value più grande non dimostra la radice unitaria, ma lascia i dati compatibili con essa. Entrambe le serie devono essere non stazionarie perché abbia senso cercare una relazione di cointegrazione.

> [!example] Svolgimento
> **Impostazione.** Si confronta ogni p-value con $0{,}05$.
>
> **(a)** Per `l_frumento` il p-value ${{a04_02.p_f|m}}$ è maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(b)** Per `l_mais` il p-value ${{a04_02.p_m|m}}$ è maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(c)** In entrambi i casi non si rifiuta la radice unitaria: le due serie hanno un comportamento non stazionario.

> [!warning] Errore tipico
> Rifiutare $H_0$ perché il p-value è «grande», o leggerlo come la probabilità che la serie sia stazionaria. Si rifiuta soltanto sotto $0{,}05$; qui nessuno dei due p-value ci arriva.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0$: per `l_frumento` il p-value alto non dimostra la radice unitaria, ma i dati sono compatibili con essa. **(b)** Non si rifiuta $H_0$ nemmeno per `l_mais`. **(c)** Sì: in entrambi i casi la radice unitaria non si rifiuta, quindi le serie vanno trattate come non stazionarie ($I(1)$, il che non significa che siano random walk).

![P-value dei test ADF delle due serie contro la soglia del 5\%: entrambi cadono fuori dalla regione di rifiuto.]({{a04_02.fig.adf}}){width=85%}

## Soluzione della Domanda 8 — Residui di lungo periodo: stazionari o no?

> [!tip] Richiamo
> Se $y$ e $x$ sono integrate, i residui $\hat u_t=y_t-\hat\alpha-\hat\beta x_t$ sono stazionari se e solo se le serie sono cointegrate. Un residuo stazionario ha un'ACF che esce dalle bande $\pm1{,}96/\sqrt{T}$ soltanto nei primi ritardi e poi vi rientra; un residuo con radice unitaria ha un'ACF che scende lentissimamente, con quasi tutti i ritardi fuori dalle bande.

> [!example] Svolgimento
> **Impostazione.** Si conta quanti ritardi dell'ACF escono dalle bande e si guarda dove.
>
> **(a)** La banda è $\pm1{,}96/\sqrt{ {{a04_02.T|m}} }=\pm{{a04_02.banda|m}}$. I ritardi dell'ACF fuori dalle bande sono ${{a04_02.fuori|m}}$ su $12$, i primi della serie.
>
> **(b)** L'ACF rientra subito nelle bande e vi resta: i residui sembrano stazionari.

> [!warning] Errore tipico
> Giudicare la relazione dalla tabella di una regressione fra livelli: con due serie integrate un $R^2$ molto alto non prova nulla. La cointegrazione si decide sui residui. Un altro errore è leggere come non stazionario un correlogramma con qualche barra fuori banda nei primi ritardi: conta la persistenza, cioè quanti ritardi restano fuori.

> [!success] Risposta
> **(a)** I ritardi dell'ACF fuori dalle bande sono ${{a04_02.fuori|m}}$ su $12$. **(b)** Sì: l'ACF decade rapidamente e rientra nelle bande, i residui sembrano stazionari. Insieme alla Domanda 7 (serie non stazionarie) è un indizio di cointegrazione fra `l_frumento` e `l_mais`, da confermare con il test di Engle-Granger.

![Sinistra: i logaritmi dei due prezzi si muovono insieme senza un livello medio. Destra: i residui della relazione di lungo periodo oscillano attorno allo zero e vi ritornano.]({{a04_02.fig.residui}}){width=85%}

## Soluzione della Domanda 9 — Elasticità di lungo periodo unitaria?

> [!tip] Richiamo
> Una relazione di lungo periodo è ben definita se le variabili sono integrate e cointegrate (residui stazionari). Con variabili cointegrate $\hat\beta$ è superconsistente ma il rapporto $t$ della regressione statica non è normale; con il DOLS (anticipi e ritardi di $\Delta x$) e gli errori standard HAC $t=(\hat\beta-\beta_0)/\widehat{\text{se}}(\hat\beta)$ è approssimativamente normale standard, e si rifiuta $H_0:\beta=\beta_0$ al 5\% se $|t|>1{,}96$. L'intervallo di confidenza al 95\% è $\hat\beta\pm1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** La (a) rimanda alle Domande 7 e 8; le altre usano la riga `l_mais` della tabella DOLS, con il valore sotto $H_0$ pari a ${{a04_02.b0|m}}$ e non a zero.
>
> **(a)** Le serie sono non stazionarie (Domanda 7) e i residui sembrano stazionari (Domanda 8): indizio di cointegrazione, da confermare con il test di Engle-Granger. Alla luce di queste risposte la relazione risulta ben definita.
>
> **(b)** $t=(\hat\beta-{{a04_02.b0|m}})/\widehat{\text{se}}(\hat\beta)=({{a04_02.b|m}}-{{a04_02.b0|m}})/{{a04_02.se|m}}={{a04_02.t_b|m}}$.
>
> **(c)** $|t|>1{,}96$: si rifiuta $H_0$.
>
> **(d)** $\hat\beta+1{,}96\,\widehat{\text{se}}(\hat\beta)={{a04_02.b|m}}+1{,}96\times{{a04_02.se|m}}={{a04_02.ic_hi|m}}$; l'estremo inferiore è ${{a04_02.ic_lo|m}}$ e l'intervallo non contiene ${{a04_02.b0|m}}$.

> [!warning] Errore tipico
> Usare il rapporto $t$ della tabella, ${{a04_02.t_tabella|m}}$, che verifica $H_0:\beta=0$: il valore sotto $H_0$ è ${{a04_02.b0|m}}$, non zero. Un altro errore è fidarsi dell'errore standard usuale di una regressione statica OLS, che con variabili cointegrate non produce una statistica normale.

> [!success] Risposta
> **(a)** Sì: serie non stazionarie e residui che sembrano stazionari, indizio di cointegrazione da confermare con il test di Engle-Granger. **(b)** Il rapporto $t$ vale ${{a04_02.t_b|m}}$. **(c)** Si rifiuta $H_0$: l'elasticità di lungo periodo non è unitaria e la stima è inferiore a uno. **(d)** L'estremo superiore dell'intervallo di confidenza al 95\% è ${{a04_02.ic_hi|m}}$, minore di ${{a04_02.b0|m}}$.

![Intervallo di confidenza al 95\% per $\beta$ (DOLS, errore HAC): ${{a04_02.b0|m}}$ cade fuori dall'intervallo.]({{a04_02.fig.dols}}){width=85%}

## Soluzione della Domanda 10 — In quanti periodi si assorbe il disequilibrio

> [!tip] Richiamo
> Sia $z_t=y_t-\alpha-\beta x_t$ il disequilibrio. Con $x$ costante (quindi $\Delta x_t=\Delta x_{t-1}=0$, e il ritardo di $\Delta x$ non agisce), shock e costante nulli, $\Delta y_t=\lambda\,z_{t-1}$ e, poiché $x_t=x_{t-1}$, $z_t=z_{t-1}+\Delta y_t=(1+\lambda)\,z_{t-1}$. Dopo $k$ periodi di aggiustamento il disequilibrio residuo è $(1+\lambda)^k z_{t-1}$ e la quota assorbita è $1-(1+\lambda)^k$. Si cerca il minimo intero $k$ con $(1+\lambda)^k\le 1-q$, cioè $k=\lceil\ln(1-q)/\ln(1+\lambda)\rceil$.

> [!example] Svolgimento
> **Impostazione.** La (a) è un test su $\lambda$; la (b) e la (c) usano $(1+\hat\lambda)^k$.
>
> **(a)** $\hat\lambda={{a04_02.lam|m}}$ e $t={{a04_02.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** Qui $1-q={{a04_02.obiettivo|m}}$ e $1+\hat\lambda={{a04_02.phi|m}}$. Da $k\ge\ln({{a04_02.obiettivo|m}})/\ln({{a04_02.phi|m}})={{a04_02.log|m}}$ si ottiene $k={{a04_02.k|m}}$. Verifica: dopo ${{a04_02.km|m}}$ periodi resta ${{a04_02.phi|m}}^{ {{a04_02.km|m}} }={{a04_02.resto_prima|m}}>{{a04_02.obiettivo|m}}$, dopo ${{a04_02.k|m}}$ periodi resta ${{a04_02.phi|m}}^{ {{a04_02.k|m}} }={{a04_02.resto|m}}\le{{a04_02.obiettivo|m}}$.
>
> **(c)** Dopo ${{a04_02.k|m}}$ periodi resta la frazione ${{a04_02.resto|m}}$ del disequilibrio, quindi la quota assorbita è $100\times\bigl(1-{{a04_02.resto|m}}\bigr)={{a04_02.assorbito|m}}\%$.

> [!warning] Errore tipico
> Dividere la quota per il coefficiente, $q/|\hat\lambda|$, come se ogni periodo assorbisse la stessa frazione del disequilibrio iniziale: ogni periodo assorbe la frazione $|\hat\lambda|$ di quello rimasto. Un altro errore è non arrotondare $k$ per eccesso: con ${{a04_02.km|m}}$ periodi la soglia non è ancora raggiunta. Il coefficiente di $\Delta x_{t-1}$ non entra: con il prezzo del mais costante il ritardo vale zero.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\lambda=0$: il coefficiente di correzione è significativo e negativo. **(b)** Servono ${{a04_02.k|m}}$ periodi per assorbire almeno il ${{a04_02.q|m}}\%$ del disequilibrio. **(c)** Dopo ${{a04_02.k|m}}$ periodi risulta assorbito il ${{a04_02.assorbito|m}}\%$ del disequilibrio iniziale; nel primo periodo se ne assorbe il ${{a04_02.primo|m}}\%$.

![Quota di disequilibrio ancora presente dopo $k$ periodi, $(1+\hat\lambda)^k$: la stella segna il primo $k$ che scende sotto ${{a04_02.obiettivo|m}}$.]({{a04_02.fig.assorbimento}}){width=85%}
