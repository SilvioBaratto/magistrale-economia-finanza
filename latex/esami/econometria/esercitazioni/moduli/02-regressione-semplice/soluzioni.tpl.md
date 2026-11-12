{{testo:e02_01}}

> [!tip] Richiamo
> Nel modello $E[Y|X]=\alpha+\beta X$ lo stimatore OLS della pendenza è $\hat\beta=\widehat{\text{Cov}}(X,Y)\big/\widehat{\text{Var}}(X)$ e quello dell'intercetta è $\hat\alpha=\bar y-\hat\beta\,\bar x$: la retta passa per il punto delle medie $(\bar x,\bar y)$. Da $\Delta Y=\beta\,\Delta X$ la variazione attesa di $Y$ per $\Delta X$ unità in più di $X$ è $\hat\beta\,\Delta X$, e il valore atteso in $x_0$ è $\hat\alpha+\hat\beta\,x_0$. Il divisore ($n$ oppure $n-1$) è lo stesso in covarianza e varianza e si semplifica nel rapporto.

> [!example] Svolgimento
> **Impostazione.** Le statistiche campionarie bastano per le due stime; la (c) e la (d) usano la retta stimata.
>
> **(a)** $\hat\beta=\dfrac{\widehat{\text{Cov}}(X,Y)}{\widehat{\text{Var}}(X)}=\dfrac{ {{e02_01.cov|m}} }{ {{e02_01.vx|m}} }={{e02_01.b|m}}$.
>
> **(b)** $\hat\alpha=\bar y-\hat\beta\,\bar x={{e02_01.my|m}}-{{e02_01.b|m}}\times{{e02_01.mx|m}}={{e02_01.a|m}}$.
>
> **(c)** $\Delta Y=\hat\beta\,\Delta X={{e02_01.b|m}}\times{{e02_01.dx|m}}={{e02_01.dy|m}}$ punti.
>
> **(d)** $\hat\alpha+\hat\beta\,x_0={{e02_01.a|m}}+{{e02_01.b|m}}\times{{e02_01.x0|m}}={{e02_01.yhat|m}}$.

> [!warning] Errore tipico
> Dividere la covarianza per la varianza di `punteggio` (${{e02_01.vy|m}}$) invece che per quella di `ore`: nella pendenza di $Y$ su $X$ il denominatore è la varianza del regressore. Un altro errore è dimenticare l'intercetta nella previsione di (d): $\hat\beta\,x_0$ da solo non è il punteggio atteso.

> [!success] Risposta
> **(a)** $\hat\beta={{e02_01.b|m}}$: un'ora di studio in più si associa a circa ${{e02_01.b|m}}$ punti in più. **(b)** $\hat\alpha={{e02_01.a|m}}$, il punteggio atteso con zero ore di studio: zero ore è probabilmente fuori dall'intervallo dei dati (estrapolazione), quindi l'intercetta va letta con cautela. **(c)** Per ${{e02_01.dx|m}}$ ore in più il punteggio atteso cresce di circa ${{e02_01.dy|m}}$ punti. **(d)** Con ${{e02_01.x0|m}}$ ore a settimana il punteggio atteso è circa ${{e02_01.yhat|m}}$.

![Nuvola dei dati e retta OLS, che passa per il punto delle medie $(\bar x,\bar y)$: ${{e02_01.dx|m}}$ ore in più spostano la retta di ${{e02_01.dy|m}}$ punti.]({{e02_01.fig.retta}}){width=85%}

{{testo:e02_02}}

> [!tip] Richiamo
> Con errori omoschedastici $\hat\sigma^2=\dfrac{1}{n-2}\sum_i\hat\epsilon_i^2=\dfrac{\text{SSR}}{n-2}$ è uno stimatore non distorto di $\sigma^2$: si dividono i residui per $n-2$, e non per $n$, perché due gradi di libertà sono spesi per stimare $\alpha$ e $\beta$. L'errore standard della pendenza è $\widehat{\text{se}}(\hat\beta)=\sqrt{\hat\sigma^2\big/\sum_i(x_i-\bar x)^2}$: cresce con la dispersione dell'errore e diminuisce con la variabilità del regressore, che aumenta con la numerosità.

> [!example] Svolgimento
> **Impostazione.** Si passa da SSR a $\hat\sigma^2$, poi a $\hat\sigma$ e all'errore standard di $\hat\beta$; la (d) scala la formula.
>
> **(a)** I gradi di libertà sono $n-2={{e02_02.gdl|m}}$ e $\hat\sigma^2=\text{SSR}/(n-2)={{e02_02.ssr|m}}/{{e02_02.gdl|m}}={{e02_02.s2|m}}$.
>
> **(b)** $\hat\sigma=\sqrt{\hat\sigma^2}=\sqrt{ {{e02_02.s2|m}} }={{e02_02.s|m}}$.
>
> **(c)** $\widehat{\text{se}}(\hat\beta)=\sqrt{\hat\sigma^2\big/\sum_i(x_i-\bar x)^2}=\sqrt{ {{e02_02.s2|m}}/{{e02_02.ssx|m}} }={{e02_02.se|m}}$.
>
> **(d)** Con numerosità ${{e02_02.m|m}}$ volte più grande, a parità di $\hat\sigma$ e di varianza di `sup`, $\sum_i(x_i-\bar x)^2$ diventa ${{e02_02.m|m}}$ volte più grande, quindi $\widehat{\text{se}}(\hat\beta)$ si moltiplica per $1\big/\sqrt{ {{e02_02.m|m}} }={{e02_02.fattore|m}}$.

> [!warning] Errore tipico
> Dividere SSR per $n$ invece che per $n-2$: si otterrebbe ${{e02_02.s2_n|m}}$ invece di ${{e02_02.s2|m}}$, una stima sistematicamente troppo bassa di $\sigma^2$ (in una simulazione SSR$/n$ resta in media sotto $\sigma^2$, SSR$/(n-2)$ no). Un altro errore è rispondere in (d) che l'errore standard si divide per ${{e02_02.m|m}}$ (cioè diventa $1/{{e02_02.m|m}}$ del valore) perché $n$ è moltiplicato per ${{e02_02.m|m}}$: è la radice di $n$ che entra, non $n$.

> [!success] Risposta
> **(a)** $\hat\sigma^2={{e02_02.s2|m}}$. **(b)** $\hat\sigma={{e02_02.s|m}}$. **(c)** $\widehat{\text{se}}(\hat\beta)={{e02_02.se|m}}$. **(d)** L'errore standard si moltiplica per ${{e02_02.fattore|m}}$, cioè si dimezza quando i dati diventano ${{e02_02.m|m}}$ volte tanti.

![Errore standard della pendenza al variare della numerosità, a parità di $\hat\sigma$ e di varianza di `sup`: con ${{e02_02.m|m}}$ volte i dati scende alla metà.]({{e02_02.fig.curva}}){width=85%}

{{testo:e02_03}}

> [!tip] Richiamo
> La devianza totale si scompone in spiegata e residua: $\text{SST}=\text{SSE}+\text{SSR}$, con $\text{SST}=\sum_i(y_i-\bar y)^2$, $\text{SSE}=\sum_i(\hat y_i-\bar y)^2$ e $\text{SSR}=\sum_i(y_i-\hat y_i)^2$. L'indice di adattamento è $R^2=\text{SSE}/\text{SST}=1-\text{SSR}/\text{SST}$, la quota della variabilità di $y$ spiegata da $x$. La varianza dell'errore si stima con $\hat\sigma^2=\text{SSR}/(n-2)$. Nella regressione semplice $R^2=\text{Corr}(x,y)^2$ e il coefficiente di correlazione ha il segno di $\hat\beta$.

> [!example] Svolgimento
> **Impostazione.** La tavola dà SST e SSR: da qui si ricava SSE, poi $R^2$; $\hat\sigma$ viene da SSR e la correlazione da $R^2$ e dal segno di $\hat\beta$.
>
> **(a)** $\text{SSE}=\text{SST}-\text{SSR}={{e02_03.sst|m}}-{{e02_03.ssr|m}}={{e02_03.sse|m}}$.
>
> **(b)** $R^2=\text{SSE}/\text{SST}={{e02_03.sse|m}}/{{e02_03.sst|m}}={{e02_03.r2|m}}$: `dist` spiega il ${{e02_03.spiegata|m}}\%$ della devianza di `affitto`.
>
> **(c)** $\hat\sigma=\sqrt{\text{SSR}/(n-2)}=\sqrt{ {{e02_03.ssr|m}}/{{e02_03.gdl|m}} }={{e02_03.s|m}}$, la radice della media delle devianze dei residui in tabella.
>
> **(d)** $\hat\beta={{e02_03.b|m}}$ è negativo, quindi $r=-\sqrt{R^2}=-\sqrt{ {{e02_03.r2|m}} }={{e02_03.corr|m}}$.

> [!warning] Errore tipico
> Rispondere ${{e02_03.radice|m}}$ in (d): la radice di $R^2$ è sempre positiva e dà solo il valore assoluto della correlazione. Il segno è quello di $\hat\beta$, e qui più distanza dal centro significa affitto più basso. Un altro errore è calcolare $R^2=\text{SSR}/\text{SST}$, che è la quota di variabilità **non** spiegata.

> [!success] Risposta
> **(a)** $\text{SSE}={{e02_03.sse|m}}$. **(b)** $R^2={{e02_03.r2|m}}$: la distanza spiega il ${{e02_03.spiegata|m}}\%$ della variabilità dell'affitto; il resto, ${{e02_03.inspiegata|m}}\%$, è lasciato ai residui. **(c)** $\hat\sigma={{e02_03.s|m}}$. **(d)** La correlazione fra distanza e affitto è ${{e02_03.corr|m}}$, negativa come $\hat\beta$.

![A sinistra la scomposizione di uno scarto, $y-\bar y=(\hat y-\bar y)+(y-\hat y)$; a destra SST ripartita fra SSE e SSR, con $R^2={{e02_03.r2|m}}$.]({{e02_03.fig.scomposizione}}){width=85%}

{{testo:e02_04}}

> [!tip] Richiamo
> La pendenza si scrive $\hat\beta=\beta+\sum_i\omega_i\epsilon_i$, con $\omega_i=(x_i-\bar x)\big/\sum_j(x_j-\bar x)^2$. Se $E[\epsilon|X]=0$ (esogeneità) allora $E[\hat\beta]=\beta$ e OLS è non distorto. Se $\text{Cov}(X,\epsilon)\neq 0$ la media di $\hat\beta$ non è $\beta$ e lo stimatore non è consistente: converge a $\beta+\text{Cov}(X,\epsilon)/\text{Var}(X)$, quindi aumentare $n$ restringe la distribuzione attorno al valore sbagliato. Il teorema di Gauss-Markov dà OLS come miglior stimatore lineare non distorto (BLUE) solo se valgono linearità, campione i.i.d., esogeneità e omoschedasticità.

> [!example] Svolgimento
> **Impostazione.** Si confronta la media delle stime con il vero $\beta$ in unità di errore standard della media, $\text{dev. std.}/\sqrt{R}$ con $\sqrt{R}={{e02_04.rad_r|m}}$.
>
> **(a)** Con $n={{e02_04.n1|m}}$: $\dfrac{|{{e02_04.m1|m}}-{{e02_04.beta|m}}|}{ {{e02_04.d1|m}}/{{e02_04.rad_r|m}} }={{e02_04.z_piccolo|m}}$, ben oltre 3: la media delle stime è lontana da $\beta$ e lo stimatore è distorto.
>
> **(b)** $\beta+\text{Cov}(X,\epsilon)/\text{Var}(X)={{e02_04.beta|m}}+{{e02_04.cov|m}}/{{e02_04.sx2|m}}={{e02_04.limite|m}}$: è il valore attorno a cui si concentrano le stime (la media a $n={{e02_04.n2|m}}$ è ${{e02_04.m2|m}}$).
>
> **(c)** Con $n={{e02_04.n2|m}}$: $\dfrac{|{{e02_04.m2|m}}-{{e02_04.beta|m}}|}{ {{e02_04.d2|m}}/{{e02_04.rad_r|m}} }={{e02_04.z_grande|m}}$, ancora oltre 3: la distorsione non è scomparsa, la dispersione è solo diminuita.
>
> **(d)** No: serve l'esogeneità, che qui non vale.
>
> **(e)** È violata l'esogeneità: $\text{Cov}(X,\epsilon)={{e02_04.cov|m}}\neq 0$, perché la motivazione non osservata sta in $\epsilon$ e muove anche $X$. Di conseguenza $E[\epsilon|X]\neq 0$.

> [!warning] Errore tipico
> Pensare che un campione più grande risolva il problema: con $\text{Cov}(X,\epsilon)\neq 0$ la numerosità riduce la varianza di $\hat\beta$ ma non la distorsione, quindi lo stimatore non è consistente. Un altro errore è leggere la piccola deviazione standard a $n={{e02_04.n2|m}}$ (${{e02_04.d2|m}}$) come prova di affidabilità: stima con precisione il valore sbagliato.

> [!success] Risposta
> **(a)** No: con $n={{e02_04.n1|m}}$ la media delle stime dista circa ${{e02_04.z_piccolo|m}}$ errori standard della media da $\beta$. **(b)** $\hat\beta$ converge a ${{e02_04.limite|m}}$, non al vero valore ${{e02_04.beta|m}}$. **(c)** No: anche con $n={{e02_04.n2|m}}$ la media dista circa ${{e02_04.z_grande|m}}$ errori standard della media da $\beta$. **(d)** No: Gauss-Markov richiede l'esogeneità. **(e)** L'ipotesi violata è l'esogeneità, $\text{Cov}(X,\epsilon)\neq 0$: la motivazione non osservata è nell'errore e correlata con la formazione.

![Distribuzione simulata delle stime OLS per le due numerosità: con $n$ grande si stringe, ma attorno a ${{e02_04.limite|m}}$ e non attorno al vero $\beta={{e02_04.beta|m}}$.]({{e02_04.fig.distribuzioni}}){width=85%}

{{testo:e02_05}}

> [!tip] Richiamo
> Da $\Delta Y=\beta\,\Delta X$, $\Delta X$ anni in più valgono $\beta\,\Delta X$: l'affermazione «$\Delta X$ anni valgono $c$ euro» equivale a $\beta=c/\Delta X$. Per un valore puntuale non nullo, $H_0:\beta=k$ contro $H_1:\beta\neq k$, la statistica è $t=(\hat\beta-k)/\widehat{\text{se}}(\hat\beta)$ e al 5\% si rifiuta se $|t|>1{,}96$. Equivalentemente si rifiuta se $k$ cade fuori dall'intervallo di confidenza $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$; l'intervallo dell'effetto di $\Delta X$ anni è $\Delta X$ volte quello di $\beta$.

> [!example] Svolgimento
> **Impostazione.** L'affermazione riguarda ${{e02_05.dx|m}}\beta$: la si riporta su $\beta$, poi si testa un valore diverso da zero.
>
> **(a)** ${{e02_05.dx|m}}\beta={{e02_05.claim|m}}$ equivale a $\beta=k={{e02_05.claim|m}}/{{e02_05.dx|m}}={{e02_05.k|m}}$.
>
> **(b)** $t=\dfrac{\hat\beta-k}{\widehat{\text{se}}(\hat\beta)}=\dfrac{ {{e02_05.b|m}}-{{e02_05.k|m}} }{ {{e02_05.se|m}} }={{e02_05.t|m}}$.
>
> **(c)** Il rapporto $t={{e02_05.t|m}}$ supera $1{,}96$ in valore assoluto: si rifiuta $H_0$.
>
> **(d)** L'intervallo per l'effetto di ${{e02_05.dx|m}}$ anni è ${{e02_05.dx|m}}\times\bigl({{e02_05.b|m}}\pm 1{,}96\times{{e02_05.se|m}}\bigr)=[{{e02_05.ic_lo|m}};\,{{e02_05.ic_hi|m}}]$ e ${{e02_05.claim|m}}$ ne è fuori. È la stessa conclusione del test.

> [!warning] Errore tipico
> Usare il rapporto $t$ della tabella (${{e02_05.t0|m}}$), che verifica $H_0:\beta=0$, e non quello con $k$ al numeratore: porterebbe a rifiutare per il motivo sbagliato. Un altro errore è confrontare ${{e02_05.claim|m}}$ euro con $\hat\beta$, che è l'effetto di un solo anno, senza dividere per ${{e02_05.dx|m}}$ (o, all'inverso, senza moltiplicare $\hat\beta$ e il suo errore standard per ${{e02_05.dx|m}}$).

> [!success] Risposta
> **(a)** $k={{e02_05.k|m}}$ euro per anno. **(b)** $t={{e02_05.t|m}}$. **(c)** Si rifiuta $H_0$: l'affermazione non è compatibile con i dati al 5\%. **(d)** No: ${{e02_05.claim|m}}$ euro cade fuori dall'intervallo di confidenza al 95\% $[{{e02_05.ic_lo|m}};\,{{e02_05.ic_hi|m}}]$ dell'effetto di ${{e02_05.dx|m}}$ anni; l'effetto stimato è ${{e02_05.eff|m}}$ euro, più basso di quello dichiarato.

![Intervallo di confidenza al 95\% per l'effetto atteso di ${{e02_05.dx|m}}$ anni di istruzione, $[{{e02_05.ic_lo|m}};\,{{e02_05.ic_hi|m}}]$: il valore dichiarato è fuori.]({{e02_05.fig.ic}}){width=85%}

{{testo:e02_06}}

> [!tip] Richiamo
> Un'affermazione «almeno $k$» è l'ipotesi nulla: $H_0:\beta\ge k$ contro $H_1:\beta<k$, alternativa unilaterale a sinistra. Con una soglia $k\neq 0$ la statistica è $t=(\hat\beta-k)/\widehat{\text{se}}(\hat\beta)$ e al 5\% si rifiuta $H_0$ se $t<-1{,}64$, dove $1{,}64$ è il quantile unilaterale della normale standard. Se $H_0$ è rifiutata l'affermazione non è compatibile con i dati; se non lo è, è compatibile.

> [!example] Svolgimento
> **Impostazione.** Si riporta la soglia su $\beta$ ($k=\Delta Y/\Delta X$), poi si fa un test a una coda a sinistra.
>
> **(a)** $k=\Delta Y/\Delta X={{e02_06.dy|m}}/{{e02_06.dx|m}}={{e02_06.k|m}}$ pezzi all'ora per ogni ora di formazione.
>
> **(b)** $t=\dfrac{\hat\beta-k}{\widehat{\text{se}}(\hat\beta)}=\dfrac{ {{e02_06.b|m}}-{{e02_06.k|m}} }{ {{e02_06.se|m}} }={{e02_06.t|m}}$.
>
> **(c)** $t={{e02_06.t|m}}<-1{,}64$: si rifiuta $H_0:\beta\ge k$ a favore di $H_1:\beta<k$.
>
> **(d)** L'affermazione è l'ipotesi nulla e viene rifiutata: non è compatibile con i dati.

> [!warning] Errore tipico
> Guardare il rapporto $t$ della tabella (${{e02_06.t0|m}}$), che verifica $H_0:\beta=0$: è grande e positivo, ma risponde a un'altra domanda. Un altro errore è cercare la regione di rifiuto dalla parte sbagliata, $t>1{,}64$: con l'alternativa $\beta<k$ si rifiuta per valori molto negativi di $t$.

> [!success] Risposta
> **(a)** $k={{e02_06.k|m}}$. **(b)** $t={{e02_06.t|m}}$. **(c)** Si rifiuta $H_0$ al 5\%, perché $t<-1{,}64$. **(d)** No: la stima ${{e02_06.b|m}}$ è significativamente più bassa della soglia ${{e02_06.k|m}}$, quindi «almeno ${{e02_06.dy|m}}$ pezzi ogni ${{e02_06.dx|m}}$ ore» non è sostenibile.

![Regione di rifiuto a sinistra al 5\% (sotto $-1{,}64$) e rapporto $t={{e02_06.t|m}}$ osservato: cade nella regione di rifiuto.]({{e02_06.fig.test}}){width=85%}

{{testo:e02_07}}

> [!tip] Richiamo
> Con la dipendente in logaritmo $\Delta\log(y)=\beta\,\Delta x$ e $\Delta\%\,y\approx 100\,\beta\,\Delta x$. L'intervallo di confidenza al 95\% per $\beta$ è $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$; quello per la variazione percentuale dovuta a $\Delta x$ si ottiene moltiplicando entrambi gli estremi per $100\,\Delta x$. Un valore è compatibile con i dati al 5\% se cade nell'intervallo; «perdere il $c$\%» con $\Delta x$ anni equivale a $\beta=-c/(100\,\Delta x)$.

> [!example] Svolgimento
> **Impostazione.** Si costruisce l'intervallo di $\beta$, lo si trasforma in percentuale e si verifica se il valore del rivenditore vi cade.
>
> **(a)** e **(b)** $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)={{e02_07.b|m}}\pm 1{,}96\times{{e02_07.se|m}}$, cioè $[{{e02_07.lo|m}};\,{{e02_07.hi|m}}]$.
>
> **(c)** e **(d)** Moltiplicando per $100\,\Delta x=100\times{{e02_07.dx|m}}$ si ottiene $[{{e02_07.plo|m}};\,{{e02_07.phi|m}}]\%$.
>
> **(e)** Perdere il ${{e02_07.claim|m}}\%$ in ${{e02_07.dx|m}}$ anni equivale a $\beta=-{{e02_07.claim|m}}/(100\times{{e02_07.dx|m}})={{e02_07.k|m}}$, che sta in $[{{e02_07.lo|m}};\,{{e02_07.hi|m}}]$. Lo stesso dice $t=(\hat\beta-\beta_0)/\widehat{\text{se}}={{e02_07.t|m}}$, in valore assoluto minore di $1{,}96$.

> [!warning] Errore tipico
> Dimenticare il fattore $100\,\Delta x$ e leggere gli estremi di $\beta$ come percentuali, oppure moltiplicare per $100\,\Delta x$ soltanto la stima e non l'errore standard (o un solo estremo). Un altro errore è dedurre dalla compatibilità del ${{e02_07.claim|m}}\%$ che l'affermazione sia vera: l'intervallo contiene molti altri valori.

> [!success] Risposta
> **(a)** ${{e02_07.lo|m}}$. **(b)** ${{e02_07.hi|m}}$. **(c)** ${{e02_07.plo|m}}\%$. **(d)** ${{e02_07.phi|m}}\%$. **(e)** Sì: il valore $-{{e02_07.claim|m}}\%$ cade nell'intervallo $[{{e02_07.plo|m}};\,{{e02_07.phi|m}}]\%$, quindi l'affermazione non si può escludere al 5\%. La stima puntuale è ${{e02_07.pct|m}}\%$.

![Intervallo di confidenza al 95\% per $\beta$ (sopra) e per la variazione percentuale del prezzo dopo ${{e02_07.dx|m}}$ anni (sotto): il valore del rivenditore cade dentro entrambi.]({{e02_07.fig.ic}}){width=85%}

{{testo:e02_08}}

> [!tip] Richiamo
> L'esogeneità, $E[\epsilon|X]=0$, rende OLS non distorto: $E[\hat\beta]=\beta$. L'omoschedasticità, $\text{Var}(\epsilon|X)=\sigma^2$, serve alla formula $\widehat{\text{se}}(\hat\beta)=\sqrt{\hat\sigma^2/\sum_i(x_i-\bar x)^2}$ e al teorema di Gauss-Markov, per cui OLS è il miglior stimatore lineare non distorto solo se valgono linearità, campione i.i.d., esogeneità e omoschedasticità. Con $\text{Var}(\epsilon|X)=\sigma^2(X)$ le stime restano non distorte, ma la formula usuale non misura più la vera dispersione di $\hat\beta$. In una simulazione la si controlla confrontando la deviazione standard delle stime con la media degli errori standard.

> [!example] Svolgimento
> **Impostazione.** Per ogni scenario si legge la tabella: la media dice se c'è distorsione, il rapporto fra dev. std. e media degli errori standard dice se la formula usuale è affidabile.
>
> **(a)** $\dfrac{|{{e02_08.me|m}}-{{e02_08.beta|m}}|}{ {{e02_08.de|m}}/{{e02_08.rad_r|m}} }={{e02_08.z|m}}$, con $\sqrt{R}={{e02_08.rad_r|m}}$: sotto 3, la media coincide con $\beta$ entro l'errore di simulazione. Sì, è non distorto.
>
> **(b)** No: manca l'omoschedasticità, una delle quattro ipotesi del teorema.
>
> **(c)** ${{e02_08.de|m}}/{{e02_08.se_e|m}}={{e02_08.rapporto|m}}$.
>
> **(d)** $|{{e02_08.rapporto|m}}-1|$ supera $0{,}10$ (cioè il 10\%): le stime variano molto più di quanto dicano gli errori standard. Non sono affidabili.
>
> **(e)** Nello scenario omoschedastico ${{e02_08.do|m}}/{{e02_08.se_o|m}}={{e02_08.rapporto_omo|m}}$, entro il 10\% da 1: affidabili.
>
> **(f)** Nel secondo scenario è violata l'omoschedasticità. La formula usuale sottostima la dispersione di $\hat\beta$ (rapporto maggiore di 1), quindi i rapporti $t$ risultano troppo grandi e il test rifiuta $H_0$ più spesso del 5\% anche quando è vera. Servono errori standard robusti all'eteroschedasticità.

> [!warning] Errore tipico
> Concludere dall'eteroschedasticità che le stime siano distorte: non lo sono, la media è ${{e02_08.me|m}}$ contro $\beta={{e02_08.beta|m}}$. Il difetto sta negli errori standard. L'errore opposto è fidarsi del test $t$ perché le stime sono centrate: un errore standard troppo piccolo gonfia il rapporto $t$.

> [!success] Risposta
> **(a)** Sì. **(b)** No: l'omoschedasticità è violata. **(c)** ${{e02_08.rapporto|m}}$. **(d)** No: il rapporto è lontano da 1. **(e)** Sì: il rapporto è ${{e02_08.rapporto_omo|m}}$. **(f)** È violata l'omoschedasticità: le stime restano non distorte ma gli errori standard usuali sono troppo piccoli, i rapporti $t$ troppo grandi e il test rifiuta troppo spesso; vanno usati errori standard robusti.

![Distribuzione simulata delle stime con errori eteroschedastici: la dispersione vera (verde) è molto più ampia di quella che gli errori standard usuali dichiarano (rosso tratteggiato).]({{e02_08.fig.stime}}){width=85%}

{{testo:e02_09}}

> [!tip] Richiamo
> $R^2=\text{SSE}/\text{SST}$ è la quota di devianza spiegata. La varianza dell'errore si stima con $\hat\sigma^2=\text{SSR}/(n-2)$, l'errore standard della pendenza con $\widehat{\text{se}}(\hat\beta)=\hat\sigma\big/\sqrt{\sum_i(x_i-\bar x)^2}$ e il test di $H_0:\beta=0$ usa $t=\hat\beta/\widehat{\text{se}}(\hat\beta)$, che si rifiuta al 5\% se $|t|>1{,}96$. La statistica $F=\dfrac{\text{SSE}/1}{\text{SSR}/(n-2)}$ con un solo regressore coincide con $t^2$. Un $R^2$ basso dice che $x$ spiega poco della variabilità di $y$, non che la pendenza sia nulla.

> [!example] Svolgimento
> **Impostazione.** Dalla tavola ANOVA si ottiene $R^2$ e $\hat\sigma$; con la dispersione di `qi` si passa all'errore standard, al rapporto $t$ e alla decisione.
>
> **(a)** $R^2=\text{SSE}/\text{SST}={{e02_09.sse|m}}/{{e02_09.sst|m}}={{e02_09.r2|m}}$.
>
> **(b)** $\hat\sigma=\sqrt{\text{SSR}/(n-2)}=\sqrt{ {{e02_09.ssr|m}}/{{e02_09.gdl|m}} }={{e02_09.s|m}}$ e $\widehat{\text{se}}(\hat\beta)=\hat\sigma/\sqrt{\sum_i(x_i-\bar x)^2}={{e02_09.s|m}}/\sqrt{ {{e02_09.ssx|m}} }={{e02_09.se|m}}$.
>
> **(c)** $t=\hat\beta/\widehat{\text{se}}(\hat\beta)={{e02_09.b|m}}/{{e02_09.se|m}}={{e02_09.t|m}}$.
>
> **(d)** $|t|={{e02_09.t|m}}$ supera $1{,}96$: si rifiuta $H_0$.
>
> **(e)** $F=\dfrac{ {{e02_09.sse|m}}/1 }{ {{e02_09.ssr|m}}/{{e02_09.gdl|m}} }={{e02_09.F|m}}$, che coincide con $t^2={{e02_09.t2|m}}$ a meno dell'arrotondamento.
>
> **(f)** No: la pendenza è significativa nonostante l'$R^2$ basso.

> [!warning] Errore tipico
> Concludere da un $R^2$ basso (${{e02_09.r2|m}}$) che $x$ non abbia effetto: l'$R^2$ misura quanta variabilità di $y$ è spiegata, il test su $\beta$ misura se la pendenza si distingue da zero. Con tanti dati si stima bene una pendenza anche se attorno alla retta c'è molta dispersione. Un altro errore è dividere SSR per $n$ invece che per $n-2$ nel calcolo di $\hat\sigma$.

> [!success] Risposta
> **(a)** $R^2={{e02_09.r2|m}}$. **(b)** $\widehat{\text{se}}(\hat\beta)={{e02_09.se|m}}$. **(c)** $t={{e02_09.t|m}}$. **(d)** Si rifiuta $H_0$: il QI è significativo al 5\%. **(e)** $F={{e02_09.F|m}}=t^2$. **(f)** No: il QI spiega poco della variabilità del salario ma la sua pendenza è significativamente diversa da zero.

![A sinistra la nuvola con la retta stimata ($R^2$ basso: molta dispersione); a destra il rapporto $t={{e02_09.t|m}}$ ben dentro la regione di rifiuto.]({{e02_09.fig.quadro}}){width=85%}

{{testo:e02_10}}

> [!tip] Richiamo
> Con la dipendente in logaritmo $\Delta\%\,y\approx 100\,\beta\,\Delta x$: «$\Delta x$ visite valgono il $s$\%» (con $s$ la percentuale dichiarata) equivale a $\beta=\kappa=s/(100\,\Delta x)$. Con $t=(\hat\beta-\kappa)/\widehat{\text{se}}(\hat\beta)$, l'affermazione «almeno» è $H_0:\beta\ge\kappa$ contro $H_1:\beta<\kappa$ e si rifiuta se $t<-1{,}64$; l'affermazione «più di» si verifica con $H_0:\beta\le\kappa$ contro $H_1:\beta>\kappa$ e si rifiuta se $t>1{,}64$. Si può affermare $H_1$ solo se $H_0$ è rifiutata: una stima puntuale oltre la soglia non basta.

> [!example] Svolgimento
> **Impostazione.** Si porta la soglia su $\beta$, si calcola un'unica statistica $t$ e la si confronta con le due code.
>
> **(a)** $100\times{{e02_10.dx|m}}\times\hat\beta=100\times{{e02_10.dx|m}}\times{{e02_10.b|m}}={{e02_10.pct|m}}\%$, sopra la soglia del ${{e02_10.soglia|m}}\%$.
>
> **(b)** $\kappa={{e02_10.soglia|m}}/(100\times{{e02_10.dx|m}})={{e02_10.k|m}}$ e $t=\dfrac{\hat\beta-\kappa}{\widehat{\text{se}}(\hat\beta)}=\dfrac{ {{e02_10.b|m}}-{{e02_10.k|m}} }{ {{e02_10.se|m}} }={{e02_10.t|m}}$.
>
> **(c)** «Almeno»: $t={{e02_10.t|m}}>-1{,}64$, non si rifiuta $H_0:\beta\ge\kappa$.
>
> **(d)** «Più di»: $t={{e02_10.t|m}}<1{,}64$, non si rifiuta $H_0:\beta\le\kappa$.
>
> **(e)** Per affermare «più del ${{e02_10.soglia|m}}\%$» si dovrebbe rifiutare $H_0:\beta\le\kappa$, e non succede: no.

> [!warning] Errore tipico
> Concludere dalla stima puntuale (${{e02_10.pct|m}}\%$ contro ${{e02_10.soglia|m}}\%$) che l'effetto superi la soglia. Lo scarto è di soli ${{e02_10.t|m}}$ errori standard: i dati sono compatibili sia con $\beta\ge\kappa$ sia con $\beta<\kappa$, nessuna delle due ipotesi si rifiuta. Un altro errore è usare il rapporto $t$ della tabella (${{e02_10.t0|m}}$), che verifica $\beta=0$, o confrontare con la coda sbagliata.

> [!success] Risposta
> **(a)** Circa ${{e02_10.pct|m}}\%$. **(b)** $t={{e02_10.t|m}}$. **(c)** Non si rifiuta $H_0$. **(d)** Non si rifiuta $H_0$. **(e)** No: la stima supera la soglia ma non in modo statisticamente significativo, quindi non si può affermare che le vendite crescano di più del ${{e02_10.soglia|m}}\%$ e non si può nemmeno escludere che crescano di meno.

![Lo stesso rapporto $t={{e02_10.t|m}}$ nelle due regioni di rifiuto unilaterali al 5\%: in nessuno dei due test cade nella regione.]({{e02_10.fig.test}}){width=85%}

{{testo:e02_11}}

> [!tip] Richiamo
> Con errori omoschedastici $\hat\sigma^2=\text{SSR}/(n-2)$, $\widehat{\text{se}}(\hat\beta)=\sqrt{\hat\sigma^2\big/\sum_i(x_i-\bar x)^2}$ e $\widehat{\text{se}}(\hat\alpha)=\sqrt{\hat\sigma^2\,\bigl(\tfrac1n\sum_i x_i^2\bigr)\big/\sum_i(x_i-\bar x)^2}$, con $\sum_i x_i^2=\sum_i(x_i-\bar x)^2+n\bar x^2$. Per un valore puntuale non nullo, $H_0:\theta=\theta_0$ contro $H_1:\theta\neq\theta_0$, la statistica è $t=(\hat\theta-\theta_0)/\widehat{\text{se}}(\hat\theta)$ e al 5\% si rifiuta se $|t|>1{,}96$. Il valore dichiarato va espresso nelle unità del modello.

> [!example] Svolgimento
> **Impostazione.** Gli errori standard non sono dati: si costruiscono da SSR e dalla dispersione di `prod`. I valori dichiarati sono in euro, il modello è in migliaia di euro: si dividono per mille.
>
> **(a)** $n-2={{e02_11.gdl|m}}$, $\hat\sigma^2={{e02_11.ssr|m}}/{{e02_11.gdl|m}}={{e02_11.s2|m}}$ e $\hat\sigma=\sqrt{ {{e02_11.s2|m}} }={{e02_11.s|m}}$.
>
> **(b)** $\widehat{\text{se}}(\hat\beta)=\sqrt{ {{e02_11.s2|m}}/{{e02_11.ssx|m}} }={{e02_11.se_b|m}}$.
>
> **(c)** Il costo variabile dichiarato è ${{e02_11.riv_b|m}}/{{e02_11.scala|m}}={{e02_11.kb|m}}$ migliaia di euro per migliaio di pezzi. $t=\dfrac{ {{e02_11.b|m}}-{{e02_11.kb|m}} }{ {{e02_11.se_b|m}} }={{e02_11.tb|m}}$.
>
> **(d)** $|t|={{e02_11.tb|m}}$ è minore di $1{,}96$: non si rifiuta $H_0$.
>
> **(e)** $\sum_i x_i^2={{e02_11.ssx|m}}+{{e02_11.n|m}}\times{{e02_11.mx|m}}^2={{e02_11.somma_x2|m}}$ e $\widehat{\text{se}}(\hat\alpha)=\sqrt{ {{e02_11.s2|m}}\times\dfrac{ {{e02_11.somma_x2|m}} }{ {{e02_11.n|m}} }\Big/{{e02_11.ssx|m}} }={{e02_11.se_a|m}}$.
>
> **(f)** I costi fissi dichiarati sono ${{e02_11.riv_a|m}}/{{e02_11.scala|m}}={{e02_11.ka|m}}$ migliaia di euro. $t=\dfrac{ {{e02_11.a|m}}-{{e02_11.ka|m}} }{ {{e02_11.se_a|m}} }={{e02_11.ta|m}}$, maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Confrontare ${{e02_11.riv_b|m}}$ con $\hat\beta={{e02_11.b|m}}$ senza convertire in migliaia di euro: il rapporto $t$ verrebbe enorme e si rifiuterebbe sempre. Altri errori: dividere SSR per $n$ invece che per $n-2$, e usare per l'intercetta l'errore standard della pendenza (${{e02_11.se_b|m}}$ invece di ${{e02_11.se_a|m}}$), che ignora il termine $\bar x^2$: l'intercetta è stimata molto meno precisamente perché la retta è estrapolata fino a produzione zero.

> [!success] Risposta
> **(a)** $\hat\sigma={{e02_11.s|m}}$. **(b)** $\widehat{\text{se}}(\hat\beta)={{e02_11.se_b|m}}$. **(c)** $t={{e02_11.tb|m}}$. **(d)** Non si rifiuta $H_0$: il costo variabile dichiarato è compatibile con i dati. **(e)** $\widehat{\text{se}}(\hat\alpha)={{e02_11.se_a|m}}$. **(f)** Si rifiuta $H_0$: i costi fissi dichiarati sono significativamente diversi dalla stima ${{e02_11.a|m}}$ migliaia di euro (rapporto $t={{e02_11.ta|m}}$).

![Intervalli di confidenza al 95\% di $\beta$ (sopra) e $\alpha$ (sotto) con i valori dichiarati: il costo variabile è dentro l'intervallo, i costi fissi sono fuori.]({{e02_11.fig.intervalli}}){width=85%}

{{testo:e02_12}}

> [!tip] Richiamo
> L'intervallo di confidenza al 95\% per una pendenza è $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$. Per la differenza di due stime da campioni indipendenti la covarianza è nulla, quindi $\text{Var}(\hat\beta_N-\hat\beta_S)=\text{Var}(\hat\beta_N)+\text{Var}(\hat\beta_S)$ e $\widehat{\text{se}}(\hat\beta_N-\hat\beta_S)=\sqrt{\widehat{\text{se}}_N^2+\widehat{\text{se}}_S^2}$, che è minore di $\widehat{\text{se}}_N+\widehat{\text{se}}_S$. L'intervallo della differenza è $(\hat\beta_N-\hat\beta_S)\pm 1{,}96\,\widehat{\text{se}}(\hat\beta_N-\hat\beta_S)$ e la differenza è significativa al 5\% se lo zero ne sta fuori.

> [!example] Svolgimento
> **Impostazione.** Si confrontano prima i due intervalli, poi si costruisce l'intervallo della differenza con l'errore standard giusto.
>
> **(a)** Nord: ${{e02_12.bn|m}}\pm 1{,}96\times{{e02_12.sn|m}}=[{{e02_12.lo_n|m}};\,{{e02_12.hi_n|m}}]$. Sud: ${{e02_12.bs|m}}\pm 1{,}96\times{{e02_12.ss|m}}=[{{e02_12.lo_s|m}};\,{{e02_12.hi_s|m}}]$. Il limite inferiore del Nord, ${{e02_12.lo_n|m}}$, è sotto il limite superiore del Sud, ${{e02_12.hi_s|m}}$: gli intervalli si sovrappongono.
>
> **(b)** $\widehat{\text{se}}(\hat\beta_N-\hat\beta_S)=\sqrt{ {{e02_12.sn|m}}^2+{{e02_12.ss|m}}^2 }={{e02_12.sd|m}}$.
>
> **(c)** e **(d)** $\hat\beta_N-\hat\beta_S={{e02_12.bn|m}}-{{e02_12.bs|m}}={{e02_12.d|m}}$ e l'intervallo è ${{e02_12.d|m}}\pm 1{,}96\times{{e02_12.sd|m}}=[{{e02_12.lo|m}};\,{{e02_12.hi|m}}]$.
>
> **(e)** Lo zero è fuori dall'intervallo: si rifiuta $H_0:\beta_N=\beta_S$. Lo stesso dice $t={{e02_12.d|m}}/{{e02_12.sd|m}}={{e02_12.t|m}}$, maggiore di $1{,}96$.
>
> **(f)** No: la sovrapposizione dei due intervalli singoli non implica che la differenza non sia significativa.

> [!warning] Errore tipico
> Concludere dalla sovrapposizione degli intervalli che la differenza non sia significativa. Sommando gli errori standard, ${{e02_12.sn|m}}+{{e02_12.ss|m}}={{e02_12.somma_se|m}}$ invece di sommare le varianze, si ottiene un intervallo troppo largo, con limite inferiore ${{e02_12.lo_somma|m}}$, che include lo zero: ma per due stime indipendenti si sommano le varianze, non gli errori standard, e l'errore standard della differenza è ${{e02_12.sd|m}}$.

> [!success] Risposta
> **(a)** Sì, i due intervalli si sovrappongono. **(b)** ${{e02_12.sd|m}}$. **(c)** ${{e02_12.lo|m}}$. **(d)** ${{e02_12.hi|m}}$. **(e)** Sì: lo zero è fuori dall'intervallo $[{{e02_12.lo|m}};\,{{e02_12.hi|m}}]$, quindi si rifiuta $H_0$ e il prezzo marginale del Nord è significativamente più alto. **(f)** No: due intervalli singoli possono sovrapporsi anche quando la differenza è significativa, perché l'errore standard della differenza è minore della somma dei due.

![In alto i due intervalli singoli, che si sovrappongono; in basso l'intervallo della differenza $\beta_N-\beta_S$, che non contiene lo zero.]({{e02_12.fig.differenza}}){width=85%}
