{{testo:e07_01}}

> [!tip] Richiamo
> Il test di Dickey-Fuller guarda il rapporto $t$ di $\delta$ nella regressione $\Delta s_t=c+\delta\,s_{t-1}+\phi\,\Delta s_{t-1}+\epsilon_t$: sotto $H_0:\delta=0$ (radice unitaria) lo si confronta, a una coda, con il valore critico (qui ${{e07_01.cv|m}}$) e si rifiuta se $t$ è minore. Il test di Engle-Granger è un test di radice unitaria sui residui della relazione di lungo periodo: $H_0$ è l'assenza di cointegrazione e si rifiuta se il p-value è minore di $0{,}05$. Due serie sono cointegrate quando sono entrambe non stazionarie (integrate) e una loro combinazione lineare è stazionaria: servono quindi due non rifiuti sulle serie e un rifiuto sui residui.

> [!example] Svolgimento
> **Impostazione.** Le domande (a) e (b) sono due test di Dickey-Fuller a una coda; la (c) legge il p-value di Engle-Granger; la (d) combina i tre risultati.
>
> **(a)** Per `rot` il rapporto $t$ di `rot_1` è ${{e07_01.t_y|m}}$, maggiore di ${{e07_01.cv|m}}$: non si rifiuta $H_0$, la serie va trattata come non stazionaria.
>
> **(b)** Per `chi` il rapporto $t$ di `chi_1` è ${{e07_01.t_x|m}}$, maggiore di ${{e07_01.cv|m}}$: non si rifiuta $H_0$, la serie va trattata come non stazionaria.
>
> **(c)** Il p-value ${{e07_01.p_eg|m}}$ è minore di $0{,}05$: si rifiuta l'ipotesi nulla di Engle-Granger, i residui della relazione di lungo periodo sono stazionari.
>
> **(d)** Le due serie vanno trattate come non stazionarie e Engle-Granger rifiuta l'assenza di cointegrazione: `rot` e `chi` risultano cointegrate.

> [!warning] Errore tipico
> Confrontare il rapporto $t$ di Dickey-Fuller con $\pm 1{,}96$ come in un test bilaterale: qui la regione di rifiuto è la sola coda sinistra, $t<{{e07_01.cv|m}}$, e il valore critico non è quello della normale. Un altro errore è fermarsi al p-value di Engle-Granger senza controllare che entrambe le serie siano non stazionarie.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0$: `rot` va trattata come non stazionaria. **(b)** Non si rifiuta $H_0$: anche `chi` va trattata come non stazionaria. **(c)** Si rifiuta l'ipotesi nulla di Engle-Granger perché il p-value è minore del 5\%: i residui sono stazionari. **(d)** Sì: due serie non stazionarie con una combinazione lineare stazionaria sono cointegrate, cioè il prezzo a Rotterdam e quello a Chicago condividono lo stesso trend stocastico.

![Sinistra: le statistiche di Dickey-Fuller di `rot` e `chi` restano a destra del valore critico ${{e07_01.cv|m}}$, fuori dalla regione di rifiuto. Destra: il p-value di Engle-Granger, ${{e07_01.p_eg|m}}$, cade nella regione di rifiuto sotto $0{,}05$.]({{e07_01.fig.test}}){width=85%}

{{testo:e07_02}}

> [!tip] Richiamo
> Una regressione fra livelli è una relazione di lungo periodo ben definita soltanto se le variabili hanno lo stesso comportamento: sono tutte stazionarie, oppure sono tutte integrate e cointegrate (residui stazionari). Se $y$ è stazionaria e $x$ ha una radice unitaria, $y-\alpha-\beta x$ eredita la radice unitaria di $x$ per ogni $\beta\neq 0$, e la statistica $t$ della regressione non ha la distribuzione usuale. La cointegrazione richiede serie non stazionarie. Il test di Dickey-Fuller si legge a una coda: si rifiuta $H_0:\delta=0$ se $t$ è minore del valore critico ${{e07_02.cv|m}}$.

> [!example] Svolgimento
> **Impostazione.** Si classificano le due serie con il test di Dickey-Fuller e si confrontano i loro ordini di integrazione.
>
> **(a)** Per `spread` il rapporto $t$ di `spread_1` è ${{e07_02.t_y|m}}$, minore di ${{e07_02.cv|m}}$: si rifiuta $H_0$, la serie è stazionaria.
>
> **(b)** Per `bund` il rapporto $t$ di `bund_1` è ${{e07_02.t_x|m}}$, maggiore di ${{e07_02.cv|m}}$: non si rifiuta $H_0$, la serie va trattata come non stazionaria.
>
> **(c)** La regressione mette in relazione una serie stazionaria con una integrata: non è ben definita come relazione di lungo periodo.
>
> **(d)** La cointegrazione richiede che entrambe le serie siano non stazionarie; `spread` è stazionaria, quindi non possono essere cointegrate.

> [!warning] Errore tipico
> Fidarsi della tabella della regressione statica: il rapporto $t$ di `bund` è ${{e07_02.t_beta|m}}$, in valore assoluto maggiore di $1{,}96$, e porterebbe a dire che il Bund spiega lo spread. Ma la regressione non è ben definita e quel $t$ non ha il significato di un test: prima di leggere i coefficienti si controllano gli ordini di integrazione.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: `spread` è stazionaria. **(b)** Non si rifiuta $H_0$: `bund` va trattata come non stazionaria. **(c)** No: la regressione statica lega una serie stazionaria a una non stazionaria e non è ben definita. **(d)** No: la cointegrazione richiede serie non stazionarie e `spread` è stazionaria.

![Lo spread oscilla attorno alla sua media (stazionaria), il rendimento del Bund vaga senza un livello medio (radice unitaria): nessuna combinazione lineare con un coefficiente non nullo può essere stazionaria.]({{e07_02.fig.serie}}){width=85%}

{{testo:e07_03}}

> [!tip] Richiamo
> Nel modello $\Delta y_t=\gamma_0+\gamma_1\Delta x_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t$, con $\text{ecm}_{t-1}=y_{t-1}-\hat\alpha-\hat\beta x_{t-1}$ il residuo ritardato della relazione di lungo periodo, $\lambda$ è il coefficiente di aggiustamento. Il modello è ben definito (bilanciato) se $y$ e $x$ sono $I(1)$ e cointegrate: allora $\Delta y_t$, $\Delta x_t$ ed $\text{ecm}_{t-1}$ sono tutti stazionari. Con $\lambda<0$ un disequilibrio positivo ($y$ sopra la relazione di lungo periodo) riduce la crescita attesa di $y$, uno negativo la aumenta. Se $\Delta x_{t+1}=0$, lo shock e la costante sono nulli, $\Delta y_{t+1}=\lambda\,\text{ecm}_t$. Per decidere su $H_0:\lambda=0$ si confronta il rapporto $t$ con $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** La (a) è un test su $\lambda$; la (b) richiede cointegrazione e un $\lambda$ di segno giusto e significativo; la (c) e la (d) usano $\Delta y_{t+1}=\lambda\,\text{ecm}_t$.
>
> **(a)** $\hat\lambda={{e07_03.lam|m}}$ e $t={{e07_03.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** Le serie sono $I(1)$, il p-value di Engle-Granger ${{e07_03.p_eg|m}}$ è minore di $0{,}05$ (cointegrazione) e $\hat\lambda$ è negativo e significativo: il modello è ben definito.
>
> **(c)** Con $\text{ecm}_t={{e07_03.d|m}}<0$ e $\hat\lambda<0$ il termine di correzione $\hat\lambda\,\text{ecm}_t$ è positivo: la variazione attesa è superiore a quella con $\text{ecm}_t=0$.
>
> **(d)** $\Delta\widehat{\text{cons}}_{t+1}=\hat\lambda\times\text{ecm}_t=({{e07_03.lam|m}})\times({{e07_03.d|m}})={{e07_03.delta|m}}$ punti.

> [!warning] Errore tipico
> Dedurre dal segno negativo di $\hat\lambda$ che la crescita dei consumi rallenti comunque: $\hat\lambda<0$ riduce la crescita solo se il disequilibrio è positivo; con $\text{ecm}_t<0$ il prodotto $\hat\lambda\,\text{ecm}_t$ è positivo e la crescita attesa aumenta. Un altro errore è dimenticare il segno del disequilibrio.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\lambda=0$: il coefficiente di correzione è significativo. **(b)** Sì: serie $I(1)$ e cointegrate, $\hat\lambda$ negativo e significativo. **(c)** Sì: con i consumi sotto la relazione di lungo periodo la crescita attesa è più alta che in equilibrio. **(d)** La variazione attesa è di circa ${{e07_03.delta|m}}$ punti: i consumi risalgono verso la relazione di lungo periodo.

![Effetto del disequilibrio sulla variazione attesa di `cons`: la retta $\hat\lambda\,\text{ecm}_t$ ha pendenza negativa $\hat\lambda={{e07_03.lam|m}}$; per $\text{ecm}_t={{e07_03.d|m}}$ vale ${{e07_03.delta|m}}$.]({{e07_03.fig.effetto}}){width=85%}

{{testo:e07_04}}

> [!tip] Richiamo
> Sia $z_t=y_t-\alpha-\beta x_t$ il disequilibrio. Con $x$ costante ($\Delta x=0$), shock e costante nulli, $\Delta y_t=\lambda\,z_{t-1}$ e, poiché $x_t=x_{t-1}$, $z_t=z_{t-1}+\Delta y_t=(1+\lambda)\,z_{t-1}$. Dopo $k$ periodi di aggiustamento il disequilibrio residuo è $(1+\lambda)^k z_{t-1}$ e la quota assorbita è $1-(1+\lambda)^k$. Si cerca il minimo intero $k$ con $(1+\lambda)^k\le 1-q$, cioè $k=\left\lceil \ln(1-q)/\ln(1+\lambda)\right\rceil$ (entrambi i logaritmi sono negativi se $-1<\lambda<0$).

> [!example] Svolgimento
> **Impostazione.** La (a) è un test su $\lambda$; la (b) è la quota assorbita con $k=1$; la (c), la (d) e la (e) usano $(1+\hat\lambda)^k$.
>
> **(a)** $\hat\lambda={{e07_04.lam|m}}$ e $t={{e07_04.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** Nel primo periodo $\Delta y_t=\hat\lambda\,z_{t-1}$ è assorbita la quota $-100\,\hat\lambda=-100\times({{e07_04.lam|m}})={{e07_04.primo|m}}\%$ del disequilibrio.
>
> **(c)** Qui $1-q={{e07_04.obiettivo1|m}}$ e $1+\hat\lambda={{e07_04.phi|m}}$. Da $k\ge\ln({{e07_04.obiettivo1|m}})/\ln({{e07_04.phi|m}})={{e07_04.log1|m}}$ si ottiene $k={{e07_04.k1|m}}$. Verifica: dopo ${{e07_04.k1m|m}}$ periodi resta ${{e07_04.phi|m}}^{ {{e07_04.k1m|m}} }={{e07_04.resto1_prima|m}}>{{e07_04.obiettivo1|m}}$, dopo ${{e07_04.k1|m}}$ periodi resta ${{e07_04.phi|m}}^{ {{e07_04.k1|m}} }={{e07_04.resto1|m}}\le{{e07_04.obiettivo1|m}}$.
>
> **(d)** Qui $1-q={{e07_04.obiettivo2|m}}$: $k\ge\ln({{e07_04.obiettivo2|m}})/\ln({{e07_04.phi|m}})={{e07_04.log2|m}}$, quindi $k={{e07_04.k2|m}}$. Verifica: ${{e07_04.phi|m}}^{ {{e07_04.k2m|m}} }={{e07_04.resto2_prima|m}}>{{e07_04.obiettivo2|m}}$ e ${{e07_04.phi|m}}^{ {{e07_04.k2|m}} }={{e07_04.resto2|m}}\le{{e07_04.obiettivo2|m}}$.
>
> **(e)** Dopo ${{e07_04.k2|m}}$ periodi resta il ${{e07_04.resto2|m}}$ del disequilibrio, quindi la quota assorbita è $100\times\bigl(1-{{e07_04.resto2|m}}\bigr)={{e07_04.assorbito|m}}\%$.

> [!warning] Errore tipico
> Dividere la quota per il coefficiente, cioè $q/|\hat\lambda|$, come se ogni periodo assorbisse la stessa frazione del disequilibrio *iniziale*: ogni periodo assorbe la frazione $|\hat\lambda|$ del disequilibrio *rimasto*, che diminuisce. Un altro errore è non arrotondare $k$ per eccesso: con ${{e07_04.k1m|m}}$ periodi la soglia non è ancora raggiunta. Infine, i testi d'esame non contano tutti allo stesso modo: qui $k$ conta anche il periodo $t$ di impatto, ma un testo può chiedere «quanti periodi dopo l'impatto», e allora la risposta è $k-1$. Si legge sempre come il testo definisce il periodo di partenza.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\lambda=0$. **(b)** Nel primo periodo si assorbe il ${{e07_04.primo|m}}\%$ del disequilibrio. **(c)** Servono ${{e07_04.k1|m}}$ periodi per assorbirne almeno il ${{e07_04.q1|m}}\%$. **(d)** Ne servono ${{e07_04.k2|m}}$ per assorbirne almeno il ${{e07_04.q2|m}}\%$. **(e)** Dopo ${{e07_04.k2|m}}$ periodi risulta assorbito il ${{e07_04.assorbito|m}}\%$ del disequilibrio iniziale; il disequilibrio non si azzera mai in un numero finito di periodi, si avvicina a zero.

![Quota di disequilibrio ancora presente dopo $k$ periodi, $(1+\hat\lambda)^k$, con le due soglie: le stelle segnano il primo $k$ che scende sotto ${{e07_04.obiettivo1|m}}$ e sotto ${{e07_04.obiettivo2|m}}$.]({{e07_04.fig.assorbimento}}){width=85%}

{{testo:e07_05}}

> [!tip] Richiamo
> Se $y$ e $x$ sono integrate, i residui $\hat u_t=y_t-\hat\alpha-\hat\beta x_t$ sono stazionari se e solo se le serie sono cointegrate: è l'idea del test di Engle-Granger. Un residuo con una radice unitaria ha un'ACF che scende molto lentamente, con valori vicini a $1$ e quasi tutti i ritardi fuori dalle bande $\pm 1{,}96/\sqrt{n}$; un residuo stazionario ha un'ACF che rientra presto nelle bande. Un $R^2$ elevato e un rapporto $t$ molto grande non provano la cointegrazione: con due serie integrate e non cointegrate sono la norma (regressione spuria).

> [!example] Svolgimento
> **Impostazione.** Si legge la velocità con cui l'ACF dei residui rientra nelle bande e se ne deduce se i residui hanno una radice unitaria.
>
> **(a)** La banda è $\pm1{,}96/\sqrt{n}=\pm1{,}96/\sqrt{ {{e07_05.n|m}} }=\pm{{e07_05.banda|m}}$. Per la coppia A i ritardi dell'ACF fuori dalle bande sono ${{e07_05.fuori_a|m}}$ su $12$: l'ACF rientra subito.
>
> **(b)** Sì: i residui di A sembrano stazionari, tornano rapidamente alla loro media (si veda la figura sotto): è un indizio di cointegrazione, da confermare con il test di Engle-Granger (i residui OLS appaiono più stazionari dell'errore vero).
>
> **(c)** No: per la coppia B tutti i ${{e07_05.fuori_b|m}}$ ritardi mostrati escono dalle bande e l'ACF scende lentissimamente, come in un residuo con radice unitaria.
>
> **(d)** No: in B l'$R^2$ e il $t$ elevati sono l'effetto di due trend stocastici distinti (non cointegrati). I residui non sembrano stazionari: non c'è evidenza di cointegrazione e la regressione va trattata come spuria.

> [!warning] Errore tipico
> Giudicare la relazione di lungo periodo dalla tabella: nella coppia B l'$R^2$ è alto e il $t$ di `ind` è enorme, ma proprio questo è il segnale tipico della regressione spuria. La cointegrazione si decide sui residui, non sul $t$ della regressione.

> [!success] Risposta
> **(a)** Per la coppia A i ritardi dell'ACF fuori dalle bande sono ${{e07_05.fuori_a|m}}$ su $12$. **(b)** Sì: l'ACF dei residui rientra subito nelle bande, i residui sembrano stazionari: è un indizio di cointegrazione per A, da confermare con il test di Engle-Granger. **(c)** No: l'ACF dei residui di B ha tutti i ritardi fuori dalle bande e decade molto lentamente. **(d)** No: $R^2$ e $t$ elevati non bastano; senza residui stazionari la regressione di B è spuria.

![Residui delle due relazioni di lungo periodo: quelli della coppia A oscillano attorno allo zero, quelli della coppia B vagano come un random walk.]({{e07_05.fig.residui}}){width=85%}

{{testo:e07_06}}

> [!tip] Richiamo
> I residui di un modello a correzione dell'errore ben specificato sono incorrelati. Se l'autocorrelazione dei residui è concentrata nei primi ritardi (ACF e PACF con il valore più alto al primo ritardo, fuori dalle bande $\pm 1{,}96/\sqrt{n}$, e poi dentro le bande), segnala una dinamica di breve periodo omessa: si aggiungono ritardi di $\Delta y$ e di $\Delta x$. La relazione di lungo periodo va rivista soltanto se la cointegrazione non regge (Engle-Granger non rifiuta, oppure $\hat\lambda$ non è negativo e significativo) o se l'ACF decade lentamente come in una radice unitaria.

> [!example] Svolgimento
> **Impostazione.** Si guarda il primo ritardo dell'ACF e della PACF e poi si controlla che il lungo periodo regga.
>
> **(a)** $\hat\lambda={{e07_06.lam|m}}$ e $t={{e07_06.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$, ma con residui autocorrelati e il livello ritardato fra i regressori l'errore standard usuale non vale, quindi la significatività di $\hat\lambda$ non prova da sola la relazione di lungo periodo.
>
> **(b)** La banda è $\pm1{,}96/\sqrt{n}=\pm{{e07_06.banda|m}}$ e il primo ritardo dell'ACF vale circa ${{e07_06.rho1|m}}$: esce dalla banda.
>
> **(c)** Sì: ACF e PACF hanno il valore più alto al primo ritardo e dal quinto ritardo in poi restano dentro le bande, cioè l'autocorrelazione è di basso ordine. Manca dinamica di breve periodo: si aggiungono $\Delta\text{imp}_{t-1}$ e $\Delta\text{pil}_{t-1}$.
>
> **(d)** No: il p-value di Engle-Granger ${{e07_06.p_eg|m}}$ è minore di $0{,}05$ e l'ACF non decade lentamente: la relazione di lungo periodo regge. La significatività di $\hat\lambda$ non lo prova, perché con residui autocorrelati l'errore standard usuale non vale; $\hat\lambda$ va ristimato e ritestato dopo aver aggiunto i ritardi di $\Delta\text{imp}$ e $\Delta\text{pil}$.

> [!warning] Errore tipico
> Concludere che, se i residui sono autocorrelati, la relazione di lungo periodo o la cointegrazione sono da rivedere. L'autocorrelazione dei residui dell'ECM riguarda la dinamica di breve periodo: il lungo periodo si rimette in discussione soltanto se il test di Engle-Granger o il coefficiente $\hat\lambda$ non supportano la cointegrazione.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\lambda=0$, ma con residui autocorrelati l'errore standard usuale non vale e il risultato non prova da solo la relazione di lungo periodo. **(b)** Sì: il primo ritardo dell'ACF, circa ${{e07_06.rho1|m}}$, supera la banda $\pm{{e07_06.banda|m}}$. **(c)** Sì: l'autocorrelazione è di basso ordine, va ri-specificata la dinamica di breve periodo aggiungendo ritardi di $\Delta\text{imp}$ e $\Delta\text{pil}$. **(d)** No: il p-value di Engle-Granger rifiuta l'assenza di cointegrazione e il lungo periodo non va toccato; $\hat\lambda$ va invece ristimato e ritestato dopo aver aggiunto i ritardi di $\Delta\text{imp}$ e $\Delta\text{pil}$.

![Ogni residuo dell'ECM contro il precedente: la pendenza positiva, ${{e07_06.rho1|m}}$, è l'autocorrelazione al primo ritardo che la dinamica di breve periodo omessa lascia nei residui.]({{e07_06.fig.ritardo}}){width=85%}

{{testo:e07_07}}

> [!tip] Richiamo
> Con serie cointegrate $\hat\beta$ è superconsistente ma la sua statistica $t$ usuale non è normale; con il DOLS (anticipi e ritardi di $\Delta x$) e gli errori standard HAC la statistica $t=(\hat\beta-\beta_0)/\widehat{\text{se}}(\hat\beta)$ è approssimativamente normale standard e si usano i quantili normali. Una variazione $\Delta x$ del regressore produce $\Delta y=\beta\,\Delta x$, quindi la variazione attesa è $\theta=\Delta x\cdot\beta$, stimata da $\Delta x\cdot\hat\beta$ con errore standard $\Delta x\cdot\widehat{\text{se}}(\hat\beta)$ e intervallo al 95\% $\Delta x\bigl(\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)\bigr)$. Si parla di cointegrazione se le due serie hanno una radice unitaria (p-value ADF maggiori di $0{,}05$) e i residui sono stazionari (p-value di Engle-Granger minore di $0{,}05$).

> [!example] Svolgimento
> **Impostazione.** La (a) controlla la cointegrazione; le altre portano il coefficiente $\beta$ alla scala dell'affermazione, un aumento di ${{e07_07.delta|m}}$ dollari.
>
> **(a)** I p-value ADF, ${{e07_07.p_y|m}}$ e ${{e07_07.p_x|m}}$, sono maggiori di $0{,}05$: non si rifiuta la radice unitaria e le serie vanno trattate come non stazionarie. Il p-value di Engle-Granger, ${{e07_07.p_eg|m}}$, è minore di $0{,}05$: i residui sono stazionari. Le serie sono cointegrate.
>
> **(b)** $\hat\theta={{e07_07.delta|m}}\times\hat\beta={{e07_07.delta|m}}\times{{e07_07.b|m}}={{e07_07.stima|m}}$ centesimi al litro.
>
> **(c)** e **(d)** $\theta$ ha errore standard ${{e07_07.delta|m}}\times\widehat{\text{se}}$ e l'intervallo è ${{e07_07.delta|m}}\times\bigl({{e07_07.b|m}}\pm1{,}96\times{{e07_07.se|m}}\bigr)=[{{e07_07.ic_lo|m}};\,{{e07_07.ic_hi|m}}]$.
>
> **(e)** L'affermazione $\theta={{e07_07.riv|m}}$ cade nell'intervallo di confidenza al 95\%: non si rifiuta $H_0$. Equivale a $\beta={{e07_07.riv|m}}/{{e07_07.delta|m}}={{e07_07.beta_riv|m}}$, che sta nell'intervallo per $\beta$.

> [!warning] Errore tipico
> Confrontare ${{e07_07.riv|m}}$ con l'intervallo di $\beta$ invece che con quello di $\theta$: l'affermazione riguarda un aumento di ${{e07_07.delta|m}}$ dollari e non di uno, e con $\hat\beta={{e07_07.b|m}}$ il valore ${{e07_07.riv|m}}$ sarebbe lontanissimo dall'intervallo, portando a rifiutare a torto. Un altro errore è usare la $t$ della regressione statica OLS al posto di quella del DOLS con errori HAC.

> [!success] Risposta
> **(a)** Sì: radice unitaria non rifiutata per le serie e residui che risultano stazionari, cioè serie cointegrate. **(b)** La stima puntuale è di circa ${{e07_07.stima|m}}$ centesimi al litro. **(c)** L'estremo inferiore dell'intervallo al 95\% è ${{e07_07.ic_lo|m}}$. **(d)** L'estremo superiore è ${{e07_07.ic_hi|m}}$. **(e)** Sì: ${{e07_07.riv|m}}$ cade nell'intervallo, quindi l'affermazione è compatibile con i dati.

![Intervallo di confidenza al 95\% per la variazione attesa della benzina dopo un aumento di ${{e07_07.delta|m}}$ dollari del petrolio: contiene l'affermazione di ${{e07_07.riv|m}}$ centesimi.]({{e07_07.fig.intervallo}}){width=85%}

{{testo:e07_08}}

> [!tip] Richiamo
> In presenza di cointegrazione lo stimatore OLS di $\beta$ è superconsistente: converge al valore vero più velocemente di $\sqrt{T}$, il tasso delle regressioni con variabili stazionarie. Raddoppiando $T$ la deviazione standard si riduce di un fattore vicino a $1/2$ nel caso A e di un fattore vicino a $1/\sqrt{2}$ nel caso B. Però l'intervallo costruito con l'errore standard usuale ha copertura inferiore a quella nominale, perché l'errore standard usuale ignora l'autocorrelazione dei residui di lungo periodo. Il DOLS aggiunge anticipi e ritardi di $\Delta x$ e usa errori standard HAC, e riporta l'inferenza sulla normale.

> [!example] Svolgimento
> **Impostazione.** Le prime tre domande leggono la tabella delle deviazioni standard, le altre la tabella delle coperture.
>
> **(a)** Caso A: $\dfrac{ {{e07_08.a200|m}} }{ {{e07_08.a100|m}} }={{e07_08.rapp_a|m}}$, vicino a $1/2$.
>
> **(b)** Caso B: $\dfrac{ {{e07_08.b200|m}} }{ {{e07_08.b100|m}} }={{e07_08.rapp_b|m}}$, vicino a $1/\sqrt{2}$.
>
> **(c)** Il rapporto del caso A, ${{e07_08.rapp_a|m}}$, è minore di quello del caso B, ${{e07_08.rapp_b|m}}$: nel caso A l'errore di stima si riduce più in fretta.
>
> **(d)** $95-{{e07_08.cop_ols|m}}={{e07_08.manca|m}}$ punti percentuali.
>
> **(e)** Lo scarto dal 95\% è ${{e07_08.manca|m}}$ punti, maggiore di ${{e07_08.tolleranza|m}}$: l'intervallo OLS usuale non è affidabile.
>
> **(f)** Il DOLS con errori HAC ha copertura ${{e07_08.cop_dols|m}}\%$, a ${{e07_08.manca_dols|m}}$ punti dal 95\%, più vicina del ${{e07_08.cop_ols|m}}\%$ dell'OLS.

> [!warning] Errore tipico
> Concludere dalla superconsistenza che l'inferenza OLS usuale sia affidabile: la superconsistenza riguarda la velocità della stima puntuale, non l'affidabilità dell'inferenza: l'errore standard usuale ignora l'autocorrelazione dei residui di lungo periodo. Un altro errore è aspettarsi che il DOLS con errori HAC porti la copertura esattamente al 95\%: in campioni finiti l'avvicina soltanto.

> [!success] Risposta
> **(a)** Il rapporto nel caso A è ${{e07_08.rapp_a|m}}$. **(b)** Nel caso B è ${{e07_08.rapp_b|m}}$. **(c)** Sì: la stima converge più rapidamente nel caso A, come previsto dalla superconsistenza. **(d)** L'intervallo OLS copre il vero $\beta$ in ${{e07_08.cop_ols|m}}\%$ dei casi, ${{e07_08.manca|m}}$ punti sotto il 95\%. **(e)** No: lo scarto supera la tolleranza. **(f)** Sì: il DOLS con errori HAC copre in ${{e07_08.cop_dols|m}}\%$ dei casi, più vicino al 95\%.

![Sinistra: deviazione standard di $\hat\beta$ contro $T$ su scala logaritmica, più ripida per le serie cointegrate (superconsistenza) che per quelle stazionarie (come $1/\sqrt{T}$). Destra: copertura simulata dell'intervallo al 95\% (linea tratteggiata), per OLS ed errore usuale e per DOLS con errori HAC.]({{e07_08.fig.simulazione}}){width=85%}

{{testo:e07_09}}

> [!tip] Richiamo
> Con serie cointegrate la regressione statica fornisce una stima superconsistente di $\beta$, ma il suo errore standard usuale non permette inferenza: la statistica $t$ non è normale e l'errore standard sottostima la variabilità quando i residui sono autocorrelati. Per testare $H_0:\beta=\beta_0$ si usa il DOLS con errori standard HAC, $t=(\hat\beta-\beta_0)/\widehat{\text{se}}_{\text{HAC}}$, approssimativamente normale standard, da confrontare con $1{,}96$. Si parla di cointegrazione se i p-value ADF delle due serie sono maggiori di $0{,}05$ (radice unitaria) e quello di Engle-Granger è minore di $0{,}05$.

> [!example] Svolgimento
> **Impostazione.** Si stabilisce la cointegrazione, poi si calcola la stessa statistica con i due errori standard.
>
> **(a)** I p-value ADF, ${{e07_09.p_y|m}}$ e ${{e07_09.p_x|m}}$, sono maggiori di $0{,}05$ e quello di Engle-Granger, ${{e07_09.p_eg|m}}$, è minore di $0{,}05$: le serie sono cointegrate.
>
> **(b)** Con l'OLS statica $t=(\hat\beta-\beta_0)/\widehat{\text{se}}=({{e07_09.b_ols|m}}-{{e07_09.b0|m}})/{{e07_09.se_ols|m}}={{e07_09.t_ols|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(c)** Con il DOLS $t=({{e07_09.b_dols|m}}-{{e07_09.b0|m}})/{{e07_09.se_dols|m}}={{e07_09.t_dols|m}}$.
>
> **(d)** Il rapporto $t={{e07_09.t_dols|m}}$ è in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$, l'affermazione è compatibile con i dati.

> [!warning] Errore tipico
> Usare la tabella della regressione statica e rifiutare $H_0$: l'errore standard usuale dell'OLS è ${{e07_09.se_ols|m}}$ contro ${{e07_09.se_dols|m}}$ del DOLS con HAC, circa ${{e07_09.rapporto|m}}$ volte più piccolo, perché non tiene conto dell'autocorrelazione dei residui di lungo periodo. La stima puntuale è praticamente la stessa; cambia la conclusione del test.

> [!success] Risposta
> **(a)** Sì: radice unitaria non rifiutata per le serie e residui che risultano stazionari, cioè serie cointegrate. **(b)** Con l'errore standard usuale dell'OLS si rifiuterebbe $H_0$ (con $t={{e07_09.t_ols|m}}$), ma questa conclusione non è attendibile. **(c)** Il rapporto $t$ del DOLS con errore HAC è ${{e07_09.t_dols|m}}$. **(d)** Sì: con lo stimatore e l'errore standard appropriati l'affermazione $\beta={{e07_09.b0|m}}$ è compatibile con i dati.

![Intervalli di confidenza al 95\% per $\beta$: quello dell'OLS statica, con l'errore usuale, esclude il valore ${{e07_09.b0|m}}$ dell'analista; quello del DOLS con errore HAC lo contiene.]({{e07_09.fig.confronto}}){width=85%}

{{testo:e07_10}}

> [!tip] Richiamo
> Il test di Engle-Granger rifiuta l'assenza di cointegrazione quando i residui di $y$ su $x$ sono stazionari, ma ciò può succedere anche perché $y$ è già stazionaria: la cointegrazione richiede che *tutte* le serie siano non stazionarie ($I(1)$) e che una loro combinazione lineare sia stazionaria. Prima di leggere il test si classificano le serie con Dickey-Fuller (rifiuto di $H_0:\delta=0$ se $t$ è minore del valore critico ${{e07_10.cv|m}}$). Una regressione statica fra livelli è ben definita se le variabili sono tutte stazionarie, oppure tutte $I(1)$ e cointegrate.

> [!example] Svolgimento
> **Impostazione.** Si classificano le tre serie, poi si abbinano i risultati di Engle-Granger alle due relazioni.
>
> **(a)** Per `margine` $t={{e07_10.t_m|m}}$, minore di ${{e07_10.cv|m}}$: si rifiuta $H_0$, la serie è stazionaria. Per `petr` ($t={{e07_10.t_p|m}}$) e `benz` ($t={{e07_10.t_b|m}}$), maggiori di ${{e07_10.cv|m}}$, non si rifiuta $H_0$: vanno trattate come $I(1)$.
>
> **(b)** Il p-value di Engle-Granger per `margine` su `petr`, ${{e07_10.p1|m}}$, è minore di $0{,}05$, ma `margine` è stazionaria: il rifiuto dipende dal fatto che il residuo eredita la stazionarietà di `margine`, non da un trend comune. Non c'è cointegrazione.
>
> **(c)** `benz` e `petr` sono entrambe $I(1)$ e il p-value ${{e07_10.p2|m}}$ è minore di $0{,}05$: sono cointegrate.
>
> **(d)** `margine` su `petr` lega una serie stazionaria a una $I(1)$ e non è cointegrata: non è ben definita.
>
> **(e)** `benz` su `petr` lega due serie $I(1)$ cointegrate: è ben definita.

> [!warning] Errore tipico
> Concludere che c'è cointegrazione in entrambi i casi perché i due p-value di Engle-Granger sono minori di $0{,}05$. Il test non verifica che le serie siano $I(1)$: con una serie stazionaria e una $I(1)$ il rifiuto è quasi automatico quando la serie stazionaria è la dipendente, ma una serie stazionaria non può avere un trend stocastico in comune con un'altra.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: `margine` è stazionaria, mentre per `petr` e `benz` non si rifiuta la radice unitaria. **(b)** No: `margine` è stazionaria e quindi non può essere cointegrata con `petr`, nonostante il p-value di Engle-Granger sia minore di $0{,}05$. **(c)** Sì: `benz` e `petr` sono $I(1)$ e i residui sono stazionari. **(d)** No: lega una serie stazionaria a una $I(1)$. **(e)** Sì: due serie $I(1)$ cointegrate.

![Sinistra: le statistiche di Dickey-Fuller; solo `margine` cade nella regione di rifiuto. Destra: i due p-value di Engle-Granger sono entrambi sotto $0{,}05$, ma uno solo dei due risultati ha senso.]({{e07_10.fig.test}}){width=85%}

{{testo:e07_11}}

> [!tip] Richiamo
> Nel modello $\Delta y_t=\gamma_0+\gamma_1\Delta x_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t$ la variazione attesa di $y$ in $t+1$ è $\gamma_0+\gamma_1\Delta x_{t+1}+\lambda\,\text{ecm}_t$ (con shock nullo). Con la costante trascurata, la crescita attesa è la somma di una componente di breve periodo, $\gamma_1\Delta x_{t+1}$, e di una di correzione, $\lambda\,\text{ecm}_t$. Con $\lambda<0$ un disequilibrio positivo riduce la crescita attesa rispetto a quella in equilibrio, $\gamma_1\Delta x_{t+1}$, ma la variazione resta positiva se la componente di breve periodo è più grande in valore assoluto. Il modello è ben definito se le serie sono $I(1)$ e cointegrate e se $\lambda$ è negativo e significativo.

> [!example] Svolgimento
> **Impostazione.** Si controlla la specificazione, poi si calcolano le due componenti della variazione attesa.
>
> **(a)** I p-value ADF, ${{e07_11.p_y|m}}$ e ${{e07_11.p_x|m}}$, sono maggiori di $0{,}05$ (non si rifiuta la radice unitaria), il p-value di Engle-Granger ${{e07_11.p_eg|m}}$ è minore di $0{,}05$ (cointegrazione) e $\hat\lambda={{e07_11.lam|m}}$ è negativo con $t={{e07_11.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: il modello è ben definito.
>
> **(b)** $\Delta\widehat{\text{inv}}_{t+1}=\hat\gamma_1\,\Delta\text{pil}_{t+1}+\hat\lambda\,\text{ecm}_t={{e07_11.gam|m}}\times{{e07_11.g|m}}+({{e07_11.lam|m}})\times{{e07_11.d|m}}={{e07_11.crescita|m}}$ punti.
>
> **(c)** La differenza rispetto a $\text{ecm}_t=0$, dove la variazione attesa sarebbe $\hat\gamma_1\,\Delta\text{pil}_{t+1}={{e07_11.equilibrio|m}}$, è $\hat\lambda\,\text{ecm}_t=({{e07_11.lam|m}})\times{{e07_11.d|m}}={{e07_11.effetto|m}}$ punti.
>
> **(d)** Siccome $\hat\lambda\,\text{ecm}_t={{e07_11.effetto|m}}<0$, la variazione attesa è inferiore a quella in equilibrio.
>
> **(e)** ${{e07_11.crescita|m}}>0$: gli investimenti crescono ancora.

> [!warning] Errore tipico
> Dedurre dal fatto che il disequilibrio è positivo e $\hat\lambda<0$ che gli investimenti diminuiranno. La correzione riduce la crescita ma non la rende negativa, perché la componente di breve periodo $\hat\gamma_1\,\Delta\text{pil}_{t+1}={{e07_11.equilibrio|m}}$ è maggiore in valore assoluto di quella di correzione.

> [!success] Risposta
> **(a)** Sì: serie $I(1)$ cointegrate, $\hat\lambda$ negativo e significativo. **(b)** La variazione attesa degli investimenti in $t+1$ è di circa ${{e07_11.crescita|m}}$ punti. **(c)** La differenza rispetto all'equilibrio è ${{e07_11.effetto|m}}$ punti. **(d)** Sì: la crescita è più lenta che con $\text{ecm}_t=0$. **(e)** No: resta positiva, perché la spinta del PIL prevale sulla correzione.

![Variazione attesa degli investimenti in $t+1$ in funzione del disequilibrio: in $\text{ecm}_t={{e07_11.d|m}}$ vale ${{e07_11.crescita|m}}$, sotto la crescita in equilibrio (linea tratteggiata, ${{e07_11.equilibrio|m}}$) ma ancora sopra lo zero.]({{e07_11.fig.scenario}}){width=85%}

{{testo:e07_12}}

> [!tip] Richiamo
> Per parlare di cointegrazione servono serie non stazionarie (test ADF che non rifiuta $H_0:\delta=0$ se $t$ è maggiore del valore critico, qui ${{e07_12.cv|m}}$ con costante e trend) e residui di lungo periodo stazionari (Engle-Granger rifiuta se il p-value è minore di $0{,}05$). L'ECM è ben definito se c'è cointegrazione e $\hat\lambda$ è negativo e significativo. I residui dell'ECM devono essere incorrelati: se ACF e PACF restano nelle bande $\pm1{,}96/\sqrt{n}$ non serve ri-specificare. Con $\Delta x=0$, shock e costante nulli, $z_t=(1+\lambda)\,z_{t-1}$: il disequilibrio residuo dopo $k$ periodi è $(1+\lambda)^k z_{t-1}$ e il minimo $k$ che ne assorbe la quota $q$ soddisfa $(1+\lambda)^k\le 1-q$, cioè $k=\left\lceil \ln(1-q)/\ln(1+\lambda)\right\rceil$.

> [!example] Svolgimento
> **Impostazione.** Si decide la cointegrazione, poi la specificazione, i residui e infine la velocità.
>
> **(a)** Le statistiche ADF con trend, ${{e07_12.t_y|m}}$ per `vend` e ${{e07_12.t_x|m}}$ per `red`, sono maggiori di ${{e07_12.cv|m}}$: non si rifiuta la radice unitaria e le serie vanno trattate come non stazionarie. Il p-value di Engle-Granger ${{e07_12.p_eg|m}}$ è minore di $0{,}05$: i residui sono stazionari. Le serie sono cointegrate.
>
> **(b)** Con cointegrazione, $\hat\lambda={{e07_12.lam|m}}$ è negativo e $t={{e07_12.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: il modello è ben definito.
>
> **(c)** Nella figura nessun ritardo dell'ACF né della PACF esce dalle bande: non c'è evidenza di autocorrelazione dei residui e non serve ri-specificare la dinamica di breve periodo.
>
> **(d)** Qui $1+\hat\lambda={{e07_12.phi|m}}$ e $1-q={{e07_12.obiettivo|m}}$. Da $k\ge\ln({{e07_12.obiettivo|m}})/\ln({{e07_12.phi|m}})={{e07_12.log|m}}$ si ottiene $k={{e07_12.k|m}}$. Verifica: ${{e07_12.phi|m}}^{ {{e07_12.km|m}} }={{e07_12.resto_prima|m}}>{{e07_12.obiettivo|m}}$ e ${{e07_12.phi|m}}^{ {{e07_12.k|m}} }={{e07_12.resto|m}}\le{{e07_12.obiettivo|m}}$, cioè è assorbito il ${{e07_12.assorbito|m}}\%$.

> [!warning] Errore tipico
> Confrontare le statistiche ADF con $\pm1{,}96$, oppure con il valore critico senza trend, quando il test include costante e trend: la regione di rifiuto è la coda sinistra oltre ${{e07_12.cv|m}}$. Un altro errore è rispondere $k=\lceil q/|\hat\lambda|\rceil$ oppure arrotondare $\ln(1-q)/\ln(1+\hat\lambda)$ per difetto: la soglia si raggiunge solo al primo intero che la supera.

> [!success] Risposta
> **(a)** Sì: serie non stazionarie e residui di lungo periodo stazionari. **(b)** Sì: c'è cointegrazione e $\hat\lambda$ è negativo e significativo. **(c)** No: ACF e PACF dei residui restano dentro le bande, non c'è evidenza di autocorrelazione dei residui. **(d)** Servono ${{e07_12.k|m}}$ periodi per assorbire almeno il ${{e07_12.q|m}}\%$ del disequilibrio iniziale.

![Quota di disequilibrio ancora presente dopo $k$ periodi, $(1+\hat\lambda)^k$: scende sotto ${{e07_12.obiettivo|m}}$ per $k={{e07_12.k|m}}$.]({{e07_12.fig.assorbimento}}){width=85%}

{{testo:e07_13}}

> [!tip] Richiamo
> Un modello a correzione dell'errore è ben definito solo se $\text{ecm}_{t-1}=y_{t-1}-\hat\alpha-\hat\beta x_{t-1}$ è stazionario, cioè se $y$ e $x$ sono $I(1)$ e cointegrate: allora tutti i termini sono $I(0)$ (modello bilanciato). Senza cointegrazione $\text{ecm}_{t-1}$ ha una radice unitaria, il modello non è bilanciato e il rapporto $t$ di $\lambda$ non ha la distribuzione usuale: la sua significatività non è evidenza di correzione dell'errore. La cointegrazione si decide con le serie non stazionarie (ADF) e il test di Engle-Granger sui residui.

> [!example] Svolgimento
> **Impostazione.** Prima si controlla la cointegrazione, poi si legge $\hat\lambda$ alla luce di quel risultato.
>
> **(a)** Le statistiche ADF, ${{e07_13.t_y|m}}$ per `fatt` e ${{e07_13.t_x|m}}$ per `pub`, sono maggiori di ${{e07_13.cv|m}}$: non si rifiuta la radice unitaria e le serie vanno trattate come non stazionarie. Il p-value di Engle-Granger ${{e07_13.p_eg|m}}$ è maggiore di $0{,}05$: non si rifiuta l'assenza di cointegrazione, quindi non c'è evidenza di cointegrazione.
>
> **(b)** $\hat\lambda={{e07_13.lam|m}}$ e $t={{e07_13.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\lambda=0$.
>
> **(c)** Senza cointegrazione $\text{ecm}_{t-1}$ non è stazionario e il modello non è bilanciato: non è ben definito, benché $\hat\lambda$ sia negativo e significativo.

> [!warning] Errore tipico
> Concludere che il modello sia valido perché $\hat\lambda$ è negativo e significativo ($t={{e07_13.t_lam|m}}$). Il segno e la significatività di $\hat\lambda$ hanno senso solo se $\text{ecm}_{t-1}$ è stazionario; qui il test di Engle-Granger non rifiuta l'assenza di cointegrazione, quindi non c'è evidenza che lo sia. Per questo non ha senso nemmeno calcolare in quanti periodi si riassorbe un disequilibrio.

> [!success] Risposta
> **(a)** No: le serie vanno trattate come non stazionarie ma Engle-Granger non rifiuta l'assenza di cointegrazione. **(b)** Si rifiuta $H_0:\lambda=0$, ma il risultato non è interpretabile. **(c)** No: senza cointegrazione il termine di correzione non è stazionario, il modello non è bilanciato e il coefficiente $\hat\lambda$ non misura una velocità di aggiustamento.

![Sinistra: il rapporto $t$ di $\hat\lambda$ cade oltre $-1{,}96$. Destra: il p-value di Engle-Granger, ${{e07_13.p_eg|m}}$, resta a destra di $0{,}05$. Il primo segnale non basta senza il secondo.]({{e07_13.fig.contrasto}}){width=85%}
