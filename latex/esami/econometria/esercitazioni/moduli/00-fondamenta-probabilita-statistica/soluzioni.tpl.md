{{testo:e00_01}}

> [!tip] Richiamo
> La distribuzione condizionale di una variabile, dato un valore dell'altra, si ottiene dividendo ogni cella per il totale della riga (o della colonna) che si condiziona: $P(A\mid B)=n(A\cap B)/n(B)$. In generale $P(A\mid B)\neq P(B\mid A)$, perché i denominatori sono diversi. Se $A$ e $B$ sono indipendenti, $P(A\mid B)=P(A)$ per ogni $B$: le distribuzioni condizionali coincidono con quella complessiva, e il numero atteso di unità in $A\cap B$ è $n(B)\,P(A)$.

> [!example] Svolgimento
> **Impostazione.** Le percentuali si calcolano dentro ciascun gruppo, dividendo per il suo totale; il confronto fra gruppi si fa sulle percentuali condizionali e non sui conteggi, perché i gruppi hanno numerosità diverse.
>
> **(a)** Si condiziona sui laureati: $P(\text{favorevole}\mid\text{laureato})=\dfrac{ {{e00_01.lau_fav|m}} }{ {{e00_01.n_lau|m}} }={{e00_01.cond|m}}\%$.
>
> **(b)** Si condiziona sui favorevoli: $P(\text{laureato}\mid\text{favorevole})=\dfrac{ {{e00_01.lau_fav|m}} }{ {{e00_01.fav|m}} }={{e00_01.inversa|m}}\%$.
>
> **(c)** Distribuzione dell'opinione fra i diplomati (favorevole, indifferente, contrario): ${{e00_01.cd_f|m}}\%$, ${{e00_01.cd_i|m}}\%$, ${{e00_01.cd_c|m}}\%$. Fra i laureati: ${{e00_01.cl_f|m}}\%$, ${{e00_01.cl_i|m}}\%$, ${{e00_01.cl_c|m}}\%$. Le differenze (laureati meno diplomati) sono ${{e00_01.diff_f|m}}$, ${{e00_01.diff_i|m}}$ e ${{e00_01.diff_c|m}}$ punti percentuali; la più grande in valore assoluto è ${{e00_01.massimo|m}}$, maggiore di ${{e00_01.soglia|m}}$. Le due distribuzioni sono diverse: le variabili risultano associate.
>
> **(d)** Con l'indipendenza la percentuale di favorevoli sarebbe la stessa nei due gruppi, cioè quella complessiva ${{e00_01.fav|m}}/{{e00_01.tot|m}}={{e00_01.p_fav|m}}\%$. I laureati favorevoli attesi sono ${{e00_01.n_lau|m}}\times{{e00_01.fav|m}}/{{e00_01.tot|m}}={{e00_01.attesi|m}}$, contro ${{e00_01.lau_fav|m}}$ osservati.

> [!warning] Errore tipico
> Scambiare le due condizionali: la (a) e la (b) hanno lo stesso numeratore, ${{e00_01.lau_fav|m}}$, ma denominatori diversi (${{e00_01.n_lau|m}}$ laureati contro ${{e00_01.fav|m}}$ favorevoli) e quindi rispondono a domande diverse. Un altro errore è confrontare i conteggi grezzi dei due gruppi senza dividere per le loro numerosità.

> [!success] Risposta
> **(a)** Il ${{e00_01.cond|m}}\%$ dei laureati è favorevole. **(b)** Il ${{e00_01.inversa|m}}\%$ dei favorevoli è laureato. **(c)** Sì: per almeno un'opinione le percentuali dei due gruppi differiscono di più di ${{e00_01.soglia|m}}$ punti percentuali (al massimo ${{e00_01.massimo|m}}$), quindi titolo di studio e opinione non sono indipendenti. **(d)** Con l'indipendenza ci si aspetterebbero ${{e00_01.attesi|m}}$ laureati favorevoli, molti meno dei ${{e00_01.lau_fav|m}}$ osservati.

![Distribuzione dell'opinione fra i diplomati e fra i laureati, a confronto con la distribuzione complessiva (rombi rossi). Con l'indipendenza le barre di entrambi i gruppi coinciderebbero con i rombi; qui i laureati sono molto più favorevoli e molto meno contrari.]({{e00_01.fig.condizionali}}){width=85%}

{{testo:e00_02}}

> [!tip] Richiamo
> La covarianza campionaria è $s_{xy}=\dfrac{1}{n}\sum_i(x_i-\bar x)(y_i-\bar y)=\dfrac{1}{n}\sum_i x_iy_i-\bar x\bar y$. È positiva se i valori di $X$ sopra la media tendono ad accompagnarsi a valori di $Y$ sopra la media. Proprietà: $\text{Cov}(X,Y)=\text{Cov}(Y,X)$; $\text{Cov}(X,X)=\text{Var}(X)$; $\text{Cov}(aX,bY)=ab\,\text{Cov}(X,Y)$; $\text{Cov}(a+X,b+Y)=\text{Cov}(X,Y)$, cioè sommare una costante non cambia la covarianza.

> [!example] Svolgimento
> **Impostazione.** Si calcolano le medie, le deviazioni dalla media e la somma dei loro prodotti; poi le proprietà della covarianza evitano di ricalcolare tutto per le variabili trasformate.
>
> **(a)** Le medie sono $\bar x={{e00_02.mx|m}}$ e $\bar y={{e00_02.my|m}}$. La somma dei prodotti $(x_i-\bar x)(y_i-\bar y)$ vale ${{e00_02.somma|m}}$, quindi $s_{xy}=\dfrac{ {{e00_02.somma|m}} }{ {{e00_02.n|m}} }={{e00_02.cov|m}}$.
>
> **(b)** $\text{Cov}({{e00_02.scala|m}}X,\,Y+{{e00_02.bonus|m}})={{e00_02.scala|m}}\times\text{Cov}(X,Y)={{e00_02.scala|m}}\times\dfrac{ {{e00_02.somma|m}} }{ {{e00_02.n|m}} }={{e00_02.cov_t|m}}$: il fattore moltiplica la covarianza, la costante aggiunta non conta.
>
> **(c)** $\text{Cov}(X,X)=\text{Var}(X)=\dfrac{1}{n}\sum_i(x_i-\bar x)^2={{e00_02.cov_xx|m}}$.
>
> **(d)** Sì: $s_{xy}={{e00_02.cov|m}}>0$.

> [!warning] Errore tipico
> Aggiungere ${{e00_02.bonus|m}}$ alla covarianza, o moltiplicare per ${{e00_02.scala|m}}$ anche la costante: solo il fattore moltiplicativo entra nella covarianza (e al quadrato nella varianza), le traslazioni no. Un altro errore è dividere per $n-1$ invece di $n$: il testo fissa il divisore $n$.

> [!success] Risposta
> **(a)** $s_{xy}={{e00_02.cov|m}}$. **(b)** $\text{Cov}(X',Y')={{e00_02.cov_t|m}}$, cioè ${{e00_02.scala|m}}$ volte la covarianza di partenza. **(c)** $\text{Cov}(X,X)=\text{Var}(X)={{e00_02.cov_xx|m}}$. **(d)** Sì: la covarianza è positiva, chi studia più ore tende ad avere voti più alti.

![Le coppie $(x_i,y_i)$ attorno alle medie (linee tratteggiate). I punti blu stanno nei quadranti in cui il prodotto $(x_i-\bar x)(y_i-\bar y)$ è positivo, i rossi in quelli in cui è negativo: i blu prevalgono, e la somma dei prodotti è ${{e00_02.somma|m}}$.]({{e00_02.fig.quadranti}}){width=85%}

{{testo:e00_03}}

> [!tip] Richiamo
> La media di una somma è la somma delle medie: $E[X+Y]=E[X]+E[Y]$. La varianza no: $\text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)+2\,\text{Cov}(X,Y)$ e, per la differenza, $\text{Var}(X-Y)=\text{Var}(X)+\text{Var}(Y)-2\,\text{Cov}(X,Y)$. La correlazione è $\rho_{XY}=\text{Cov}(X,Y)/(s_X\,s_Y)$ e sta sempre fra $-1$ e $1$. Variabili indipendenti hanno covarianza nulla: allora la varianza della somma è la somma delle varianze.

> [!example] Svolgimento
> **Impostazione.** Le deviazioni standard della tabella vanno elevate al quadrato per ottenere le varianze, ${{e00_03.var_x|m}}$ per $X$ e ${{e00_03.var_y|m}}$ per $Y$; la covarianza è ${{e00_03.cov|m}}$.
>
> **(a)** $E[Z]={{e00_03.mx|m}}+{{e00_03.my|m}}={{e00_03.media_z|m}}$ migliaia di euro.
>
> **(b)** $\text{Var}(Z)={{e00_03.var_x|m}}+{{e00_03.var_y|m}}+2\times{{e00_03.cov|m}}={{e00_03.var_z|m}}$.
>
> **(c)** $\rho_{XY}=\dfrac{ {{e00_03.cov|m}} }{ {{e00_03.sx|m}}\times{{e00_03.sy|m}} }={{e00_03.rho|m}}$.
>
> **(d)** $\text{Var}(X-Y)={{e00_03.var_x|m}}+{{e00_03.var_y|m}}-2\times{{e00_03.cov|m}}={{e00_03.var_d|m}}$.
>
> **(e)** Con $\text{Cov}=0$ la varianza della somma sarebbe ${{e00_03.var_x|m}}+{{e00_03.var_y|m}}={{e00_03.var_ind|m}}$, minore di ${{e00_03.var_z|m}}$: la covarianza positiva allarga la distribuzione della somma.

> [!warning] Errore tipico
> Sommare le varianze e basta, dimenticando $2\,\text{Cov}$, oppure sommare le deviazioni standard (${{e00_03.sx|m}}+{{e00_03.sy|m}}$ non è la deviazione standard di $Z$, che vale ${{e00_03.sd_z|m}}$). Per la differenza la covarianza entra con il segno meno: con redditi positivamente correlati $\text{Var}(X-Y)$ è più piccola di $\text{Var}(X+Y)$.

> [!success] Risposta
> **(a)** La media del reddito familiare è ${{e00_03.media_z|m}}$ migliaia di euro. **(b)** $\text{Var}(Z)={{e00_03.var_z|m}}$. **(c)** $\rho_{XY}={{e00_03.rho|m}}$: correlazione positiva e moderata. **(d)** $\text{Var}(X-Y)={{e00_03.var_d|m}}$. **(e)** Sì: con redditi indipendenti sarebbe ${{e00_03.var_ind|m}}$, perché la covarianza positiva aumenta la varianza della somma.

![Distribuzione del reddito familiare $Z=X+Y$ osservata (barre blu) e quella che si avrebbe se i redditi dei coniugi fossero indipendenti (linea rossa). La covarianza positiva allarga la distribuzione: la deviazione standard di $Z$ è ${{e00_03.sd_z|m}}$.]({{e00_03.fig.somma}}){width=85%}

{{testo:e00_04}}

> [!tip] Richiamo
> Per una variabile casuale discreta $E[X]=\sum_x x\,P(X=x)$ e $\text{Var}(X)=\sum_x(x-\mu)^2P(X=x)=E[X^2]-\mu^2$. Per una trasformazione lineare $Y=aX-c$ valgono $E[Y]=aE[X]-c$ (la media è lineare) e $\text{Var}(Y)=a^2\,\text{Var}(X)$: la costante non conta e il coefficiente entra al quadrato.

> [!example] Svolgimento
> **Impostazione.** Si calcolano $E[X]$ e $E[X^2]$ dalla tabella; $\text{Var}(X)$ ne segue, e le due trasformazioni lineari non richiedono nuove somme.
>
> **(a)** $E[X]=({{e00_04.x1|m}})({{e00_04.p1|m}})+({{e00_04.x2|m}})({{e00_04.p2|m}})+({{e00_04.x3|m}})({{e00_04.p3|m}})+({{e00_04.x4|m}})({{e00_04.p4|m}})+({{e00_04.x5|m}})({{e00_04.p5|m}})={{e00_04.mu|m}}$.
>
> **(b)** $E[X^2]={{e00_04.ex2|m}}$, quindi $\text{Var}(X)=E[X^2]-\mu^2={{e00_04.ex2|m}}-({{e00_04.mu|m}})^2={{e00_04.var|m}}$.
>
> **(c)** $E[Y]={{e00_04.a|m}}\times{{e00_04.mu|m}}-{{e00_04.c|m}}={{e00_04.mu_y|m}}$.
>
> **(d)** $\text{Var}(Y)={{e00_04.a|m}}^2\times\text{Var}(X)={{e00_04.a2|m}}\times{{e00_04.var|m}}={{e00_04.var_y|m}}$.

> [!warning] Errore tipico
> Sottrarre il costo fisso anche dalla varianza, scrivendo ${{e00_04.a2|m}}\,\text{Var}(X)-{{e00_04.c|m}}$: una costante sposta la distribuzione ma non ne cambia la dispersione. Un altro errore è moltiplicare la varianza per ${{e00_04.a|m}}$ invece che per ${{e00_04.a2|m}}$: è la deviazione standard a scalare con ${{e00_04.a|m}}$ (da ${{e00_04.sd|m}}$ a ${{e00_04.sd_y|m}}$).

> [!success] Risposta
> **(a)** $E[X]={{e00_04.mu|m}}$. **(b)** $\text{Var}(X)={{e00_04.var|m}}$. **(c)** $E[Y]={{e00_04.mu_y|m}}$. **(d)** $\text{Var}(Y)={{e00_04.var_y|m}}$: la leva moltiplica la deviazione standard per ${{e00_04.a|m}}$ e la varianza per ${{e00_04.a2|m}}$, mentre il costo fisso sposta soltanto la media.

![Distribuzione di $X$ (a sinistra) e di $Y=aX-c$ (a destra) con la media (linea rossa) e la fascia di una deviazione standard: la trasformazione sposta e dilata la distribuzione, e la fascia si allarga di un fattore ${{e00_04.a|m}}$.]({{e00_04.fig.distribuzioni}}){width=85%}

{{testo:e00_05}}

> [!tip] Richiamo
> In un campione casuale semplice $\bar Y$ ha media $\mu$ ed errore standard $\sigma/\sqrt{n}$, che si stima con $s/\sqrt{n}$; per il teorema del limite centrale $\bar Y$ è approssimativamente normale. L'intervallo di confidenza per $\mu$ è $\bar y\pm z\,s/\sqrt{n}$, con $z=1{,}96$ al 95\% e $z=2{,}57$ al 99\%. Il 95\% si riferisce ai campioni ripetuti: costruendo l'intervallo su molti campioni, il 95\% degli intervalli contiene $\mu$. Non è la quota di dati dentro l'intervallo. Rifiutare $H_0:\mu=\mu_0$ al 5\% (bilaterale) equivale ad avere $\mu_0$ fuori dall'intervallo al 95\%.

> [!example] Svolgimento
> **Impostazione.** Dalla tabella: $n={{e00_05.n|m}}$, $\bar y={{e00_05.ybar|m}}$, $s={{e00_05.s|m}}$.
>
> **(a)** $s/\sqrt{n}={{e00_05.s|m}}/\sqrt{ {{e00_05.n|m}} }={{e00_05.se|m}}$.
>
> **(b)** $\bar y-1{,}96\times{{e00_05.se|m}}={{e00_05.ybar|m}}-{{e00_05.m95|m}}={{e00_05.lo|m}}$.
>
> **(c)** $\bar y+1{,}96\times{{e00_05.se|m}}={{e00_05.ybar|m}}+{{e00_05.m95|m}}={{e00_05.hi|m}}$.
>
> **(d)** Al 99\% l'intervallo è $\bar y\pm 2{,}57\times{{e00_05.se|m}}=[{{e00_05.lo99|m}};\,{{e00_05.hi99|m}}]$, con ampiezza $2\times2{,}57\times{{e00_05.se|m}}={{e00_05.ampiezza|m}}$.
>
> **(e)** L'intervallo di confidenza al 95\% è $[{{e00_05.lo|m}};\,{{e00_05.hi|m}}]$ e ${{e00_05.mu0|m}}$ ne è fuori: si rifiuta $H_0$. Lo stesso dice $t=({{e00_05.ybar|m}}-{{e00_05.mu0|m}})/{{e00_05.se|m}}={{e00_05.t|m}}$, in valore assoluto maggiore di $1{,}96$.
>
> **(f)** No. L'intervallo di $[{{e00_05.lo|m}};\,{{e00_05.hi|m}}]$ riguarda la media $\mu$ e ha l'errore standard $s/\sqrt{n}$. I singoli tempi variano con la deviazione standard $s$: se i tempi fossero approssimativamente normali, circa il 95\% di essi starebbe in $\bar y\pm1{,}96\,s=[{{e00_05.lo_s|m}};\,{{e00_05.hi_s|m}}]$, un intervallo molto più largo.

> [!warning] Errore tipico
> Usare la deviazione standard $s$ al posto dell'errore standard $s/\sqrt{n}$ (l'intervallo diventerebbe $\bar y\pm1{,}96\,s=[{{e00_05.lo_s|m}};\,{{e00_05.hi_s|m}}]$, troppo largo), o leggere l'intervallo come il campo in cui cade il 95\% delle osservazioni. Un altro errore è dire che $\mu$ ha il 95\% di probabilità di stare nell'intervallo calcolato: $\mu$ è un numero fisso, è l'intervallo a cambiare da campione a campione.

> [!success] Risposta
> **(a)** L'errore standard della media è ${{e00_05.se|m}}$ minuti. **(b)–(c)** L'intervallo di confidenza al 95\% per il tempo medio di attesa è $[{{e00_05.lo|m}};\,{{e00_05.hi|m}}]$. **(d)** L'intervallo al 99\% è più largo, ${{e00_05.ampiezza|m}}$ minuti. **(e)** ${{e00_05.mu0|m}}$ minuti sta fuori dall'intervallo al 95\%: si rifiuta $H_0$. **(f)** No: l'intervallo riguarda la media, non i singoli tempi di attesa, che sono molto più dispersi.

![Intervalli di confidenza al 99\% e al 95\% per il tempo medio di attesa e intervallo $\bar y\pm1{,}96\,s$ dei singoli valori. Il valore dichiarato (linea rossa) è fuori da entrambi gli intervalli per la media, ma i singoli valori lo contengono.]({{e00_05.fig.intervalli}}){width=85%}

{{testo:e00_06}}

> [!tip] Richiamo
> Sotto $H_0:\mu=\mu_0$ la statistica $t=(\bar y-\mu_0)/(s/\sqrt{n})$ è approssimativamente $N(0,\,1)$. L'alternativa decide dove si rifiuta. Contro $H_1:\mu<\mu_0$ si rifiuta se $t<-1{,}64$ e il p-value è $P(Z\le t_{\text{oss}})$; contro $H_1:\mu>\mu_0$ si rifiuta se $t>1{,}64$ e il p-value è $P(Z\ge t_{\text{oss}})$; contro $H_1:\mu\neq\mu_0$ si rifiuta se $|t|>1{,}96$ e il p-value è $2\,P(Z\ge|t_{\text{oss}}|)$. Si rifiuta quando il p-value è minore del livello. Il p-value è la probabilità, sotto $H_0$, di un risultato almeno così contrario a $H_0$ come quello osservato: non è la probabilità che $H_0$ sia vera.

> [!example] Svolgimento
> **Impostazione.** Con gli stessi dati le tre alternative danno regioni di rifiuto diverse; conta anche il segno di $t$.
>
> **(a)** $s/\sqrt{n}={{e00_06.s|m}}/\sqrt{ {{e00_06.n|m}} }={{e00_06.se|m}}$ e $t=\dfrac{ {{e00_06.ybar|m}}-{{e00_06.mu0|m}} }{ {{e00_06.se|m}} }={{e00_06.t|m}}$.
>
> **(b)** ${{e00_06.t|m}}<-1{,}64$: si rifiuta $H_0$ (p-value ${{e00_06.p_sx|m}}<0{,}05$).
>
> **(c)** ${{e00_06.t|m}}$ è negativo, quindi non supera $1{,}64$: non si rifiuta $H_0$ (p-value $1-{{e00_06.p_sx|m}}={{e00_06.p_dx|m}}$).
>
> **(d)** $|t|={{e00_06.t_abs|m}}$ è maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(e)** Il p-value bilaterale è il doppio di quello unilaterale: $2\times{{e00_06.p_sx|m}}={{e00_06.p_bi|m}}$.
>
> **(f)** No. Il p-value è la probabilità di un risultato così estremo se $H_0$ fosse vera, non la probabilità che $H_0$ sia vera.

> [!warning] Errore tipico
> Guardare solo $|t|$ e rifiutare anche contro $H_1:\mu>\mu_0$: l'alternativa unilaterale a destra si rifiuta soltanto con $t$ positivo e grande, e qui il campione sta dall'altra parte di $\mu_0$. Un altro errore è leggere il p-value ${{e00_06.p_bi|m}}$ come la probabilità che $H_0$ sia vera: dice quanto sarebbe raro un campione simile se $H_0$ fosse vera.

> [!success] Risposta
> **(a)** $t={{e00_06.t|m}}$. **(b)** Contro $H_1:\mu<\mu_0$ si rifiuta $H_0$. **(c)** Contro $H_1:\mu>\mu_0$ non si rifiuta $H_0$: $t$ ha il segno sbagliato. **(d)** Contro $H_1:\mu\neq\mu_0$ si rifiuta $H_0$. **(e)** Il p-value bilaterale è ${{e00_06.p_bi|m}}$. **(f)** No: è la probabilità di un campione così estremo sotto $H_0$.

![Distribuzione di $t$ sotto $H_0$ con le regioni di rifiuto dei tre test al 5\%. La $t$ osservata (${{e00_06.t|m}}$, linea verde) cade nella regione di rifiuto dell'alternativa a sinistra e del test bilaterale, non in quella dell'alternativa a destra.]({{e00_06.fig.regioni}}){width=85%}

{{testo:e00_07}}

> [!tip] Richiamo
> In un campione casuale semplice le $Y_i$ sono indipendenti e hanno la distribuzione della popolazione: $E[Y_i]=\mu$, $\text{Var}(Y_i)=\sigma^2$, $\text{Cov}(Y_i,Y_j)=0$ per $i\neq j$. Quindi $E[\bar Y]=\frac{1}{n}\sum_iE[Y_i]=\mu$ (stimatore corretto) e $\text{Var}(\bar Y)=\frac{1}{n^2}\bigl[\sum_i\text{Var}(Y_i)+\sum_{i\neq j}\text{Cov}(Y_i,Y_j)\bigr]=\sigma^2/n$: l'errore standard è $\sigma/\sqrt{n}$ e tende a zero al crescere di $n$ (legge dei grandi numeri). Per il teorema del limite centrale $(\bar Y-\mu)/(\sigma/\sqrt{n})$ è approssimativamente $N(0,\,1)$ anche se $Y$ non è normale, quindi $P(|\bar Y-\mu|\le1{,}96\,\sigma/\sqrt{n})\approx0{,}95$.

> [!example] Svolgimento
> **Impostazione.** Si usano indipendenza e identica distribuzione per ottenere media e varianza di $\bar Y$; la normalità approssimata di $\bar Y$ dà poi l'intervallo.
>
> **(a)** Per l'indipendenza $\text{Cov}(Y_1,Y_2)=0$, quindi $\text{Var}(Y_1+Y_2)=\sigma^2+\sigma^2=2\times{{e00_07.sigma|m}}^2={{e00_07.var_somma|m}}$.
>
> **(b)** $E[\bar Y]=\dfrac{1}{n}\sum_iE[Y_i]=\dfrac{1}{n}\,n\,\mu=\mu$: sì, è corretto, per qualsiasi $n$.
>
> **(c)** $\sigma/\sqrt{n}={{e00_07.sigma|m}}/\sqrt{ {{e00_07.n|m}} }={{e00_07.se|m}}$.
>
> **(d)** Da $\sigma/\sqrt{n'}={{e00_07.obiettivo|m}}$ si ricava $n'=(\sigma/{{e00_07.obiettivo|m}})^2=({{e00_07.sigma|m}}/{{e00_07.obiettivo|m}})^2={{e00_07.n_obs|m}}$.
>
> **(e)** $c=1{,}96\times{{e00_07.se|m}}={{e00_07.c|m}}$, quindi l'intervallo è $[{{e00_07.lo|m}};\,{{e00_07.hi|m}}]$.
>
> **(f)** $z=(\bar y-\mu)/(\sigma/\sqrt{n})=({{e00_07.ybar|m}}-{{e00_07.mu|m}})/{{e00_07.se|m}}={{e00_07.z|m}}$, in valore assoluto maggiore di $1{,}96$: ${{e00_07.ybar|m}}$ cade fuori dall'intervallo.

> [!warning] Errore tipico
> Usare $\sigma$ invece di $\sigma/\sqrt{n}$ nell'intervallo di (e): $1{,}96\,\sigma$ descrive la dispersione di un singolo reddito, non quella della media. Un altro errore è pensare che $\bar Y$ sia normale solo se $Y$ lo è: il teorema del limite centrale vale anche per popolazioni asimmetriche, purché $n$ sia abbastanza grande. In (a), poi, $\text{Var}(Y_1+Y_2)$ vale $2\sigma^2$ e non $4\sigma^2$: la somma di due variabili indipendenti ha varianza pari alla somma delle varianze.

> [!success] Risposta
> **(a)** $\text{Var}(Y_1+Y_2)={{e00_07.var_somma|m}}$. **(b)** Sì: $E[\bar Y]=\mu$. **(c)** L'errore standard è ${{e00_07.se|m}}$. **(d)** Servono ${{e00_07.n_obs|m}}$ osservazioni. **(e)** $c={{e00_07.c|m}}$: $\bar Y$ cade in $[{{e00_07.lo|m}};\,{{e00_07.hi|m}}]$ con probabilità circa $0{,}95$. **(f)** No: ${{e00_07.ybar|m}}$ sta fuori, ed è un valore insolito per la media di un campione casuale di questa popolazione.

![A sinistra la popolazione, asimmetrica, con la media $\mu$ (linea rossa). A destra le medie di molti campioni di $n={{e00_07.n|m}}$ osservazioni: il loro istogramma segue la normale con media $\mu$ ed errore standard ${{e00_07.se|m}}$ (linea blu). La fascia verde è $[\mu-c,\ \mu+c]$; la linea rossa è la media osservata ${{e00_07.ybar|m}}$, fuori dalla fascia.]({{e00_07.fig.campionaria}}){width=85%}

{{testo:e00_08}}

> [!tip] Richiamo
> Una proporzione è la media di variabili di Bernoulli: $\hat\pi=x/n$ ha media $\pi$ e varianza $\pi(1-\pi)/n$, ed è approssimativamente normale. Per l'intervallo di confidenza, che non assume nulla su $\pi$, si stima l'errore standard con $\hat\pi$: $\hat\pi\pm1{,}96\sqrt{\hat\pi(1-\hat\pi)/n}$. Per un test su $H_0:\pi=\pi_0$ si calcola invece l'errore standard sotto $H_0$, $\text{se}_0=\sqrt{\pi_0(1-\pi_0)/n}$, e $z=(\hat\pi-\pi_0)/\text{se}_0$; contro $H_1:\pi>\pi_0$ si rifiuta se $z>1{,}64$.

> [!example] Svolgimento
> **Impostazione.** La stima puntuale è $\hat\pi=x/n={{e00_08.x|m}}/{{e00_08.n|m}}={{e00_08.phat|m}}$.
>
> **(a)** $\sqrt{\hat\pi(1-\hat\pi)/n}=\sqrt{ {{e00_08.phat|m}}\times(1-{{e00_08.phat|m}})/{{e00_08.n|m}} }={{e00_08.se|m}}$.
>
> **(b)–(c)** $\hat\pi\pm1{,}96\times{{e00_08.se|m}}=[{{e00_08.lo|m}};\,{{e00_08.hi|m}}]$. L'intervallo sta tutto sopra ${{e00_08.pi0|m}}$.
>
> **(d)** $\text{se}_0=\sqrt{ {{e00_08.pi0|m}}\times(1-{{e00_08.pi0|m}})/{{e00_08.n|m}} }={{e00_08.se0|m}}$.
>
> **(e)** $z=\dfrac{ {{e00_08.phat|m}}-{{e00_08.pi0|m}} }{ {{e00_08.se0|m}} }={{e00_08.z|m}}$.
>
> **(f)** ${{e00_08.z|m}}>1{,}64$: si rifiuta $H_0:\pi={{e00_08.pi0|m}}$ a favore di $H_1:\pi>{{e00_08.pi0|m}}$. Equivalentemente $\hat\pi$ supera la soglia $\pi_0+1{,}64\,\text{se}_0={{e00_08.soglia|m}}$.

> [!warning] Errore tipico
> Usare nel test l'errore standard stimato ${{e00_08.se|m}}$ al posto di $\text{se}_0={{e00_08.se0|m}}$: il test calcola la distribuzione di $\hat\pi$ nel mondo in cui $H_0$ è vera, quindi $\pi=\pi_0$. Un altro errore è usare $1{,}96$ per il test unilaterale: il valore critico unilaterale al 5\% è $1{,}64$.

> [!success] Risposta
> **(a)** L'errore standard stimato è ${{e00_08.se|m}}$. **(b)–(c)** L'intervallo di confidenza al 95\% per $\pi$ è $[{{e00_08.lo|m}};\,{{e00_08.hi|m}}]$. **(d)** Sotto $H_0$ l'errore standard è ${{e00_08.se0|m}}$. **(e)** $z={{e00_08.z|m}}$. **(f)** Si rifiuta $H_0$: al 5\% i dati indicano che la maggioranza è favorevole.

![A sinistra l'intervallo di confidenza al 95\% per $\pi$ e il valore ${{e00_08.pi0|m}}$ sotto $H_0$ (linea rossa), fuori dall'intervallo. A destra la distribuzione di $\hat\pi$ sotto $H_0$ con la regione di rifiuto al 5\% (in rosso) e la stima osservata ${{e00_08.phat|m}}$ (linea verde).]({{e00_08.fig.proporzione}}){width=85%}

{{testo:e00_09}}

> [!tip] Richiamo
> Se la popolazione è normale e $n$ è piccolo (sotto 25–30 osservazioni), $t=(\bar y-\mu_0)/(s/\sqrt{n})$ ha distribuzione $t$ di Student con $n-1$ gradi di libertà. La $t$ ha code più pesanti della normale: il valore critico è più grande e l'intervallo $\bar y\pm t_{n-1}\,s/\sqrt{n}$ è più largo di quello con $1{,}96$. Al crescere di $n$ la $t$ si avvicina alla normale. Con troppo pochi dati la normale rifiuta $H_0$ troppo spesso.

> [!example] Svolgimento
> **Impostazione.** Dai quattro valori: $\bar y={{e00_09.media|m}}$, $s={{e00_09.s|m}}$ e $s/\sqrt{n}={{e00_09.se|m}}$.
>
> **(a)** $t=\dfrac{ {{e00_09.media|m}}-{{e00_09.mu0|m}} }{ {{e00_09.se|m}} }={{e00_09.t|m}}$.
>
> **(b)** Gradi di libertà: $n-1={{e00_09.gdl|m}}$.
>
> **(c)** $|t|={{e00_09.t_abs|m}}$ è minore del valore critico ${{e00_09.qt|m}}$: non si rifiuta $H_0$.
>
> **(d)** Con $1{,}96$ si avrebbe ${{e00_09.t_abs|m}}>1{,}96$ e si rifiuterebbe $H_0$: conclusione opposta, ma sbagliata con soli quattro dati.
>
> **(e)–(f)** $\bar y\pm{{e00_09.qt|m}}\times{{e00_09.se|m}}=[{{e00_09.lo|m}};\,{{e00_09.hi|m}}]$, che contiene ${{e00_09.mu0|m}}$. Con $1{,}96$ l'intervallo sarebbe $[{{e00_09.lo_z|m}};\,{{e00_09.hi_z|m}}]$, troppo stretto, e lascerebbe fuori ${{e00_09.mu0|m}}$.

> [!warning] Errore tipico
> Usare $1{,}96$ per ogni $n$. Con $3$ gradi di libertà la probabilità che $|t|$ superi $1{,}96$ sotto $H_0$ è quasi il 15\%, non il 5\%: usare la normale vorrebbe dire rifiutare per errore in circa un caso su sette in cui $H_0$ è vera. Un altro errore è contare $n$ invece di $n-1$ per i gradi di libertà.

> [!success] Risposta
> **(a)** $t={{e00_09.t|m}}$. **(b)** I gradi di libertà sono ${{e00_09.gdl|m}}$. **(c)** Non si rifiuta $H_0$: ${{e00_09.t_abs|m}}<{{e00_09.qt|m}}$. **(d)** Con $1{,}96$ si rifiuterebbe $H_0$, ma il valore critico giusto per quattro dati è ${{e00_09.qt|m}}$. **(e)–(f)** L'intervallo di confidenza al 95\% è $[{{e00_09.lo|m}};\,{{e00_09.hi|m}}]$ e comprende ${{e00_09.mu0|m}}$ ml.

![Densità della normale e della $t$ di Student con $3$ gradi di libertà, con i rispettivi valori critici al 5\%. La $t$ osservata, ${{e00_09.t|m}}$, supera il valore critico normale ma non quello della $t$.]({{e00_09.fig.densita}}){width=85%}

{{testo:e00_10}}

> [!tip] Richiamo
> Per due campioni indipendenti $\text{Var}(\bar Y_1-\bar Y_2)=\text{Var}(\bar Y_1)+\text{Var}(\bar Y_2)-2\,\text{Cov}(\bar Y_1,\bar Y_2)$ e la covarianza è nulla, quindi $\text{se}=\sqrt{s_1^2/n_1+s_2^2/n_2}$. Si testa $H_0:\mu_1=\mu_2$ con $t=(\bar y_1-\bar y_2)/\text{se}$ (rifiuto se $|t|>1{,}96$) o, in modo equivalente, con l'intervallo $(\bar y_1-\bar y_2)\pm1{,}96\,\text{se}$: si rifiuta se non contiene lo zero. Gli intervalli delle due medie che si sovrappongono sono solo un'indicazione: la differenza può essere significativa anche così, perché $\text{se}<\text{se}_1+\text{se}_2$.

> [!example] Svolgimento
> **Impostazione.** Dalla tabella: servizio A, $n_1={{e00_10.n1|m}}$, $\bar y_1={{e00_10.m1|m}}$, $s_1={{e00_10.s1|m}}$; servizio B, $n_2={{e00_10.n2|m}}$, $\bar y_2={{e00_10.m2|m}}$, $s_2={{e00_10.s2|m}}$. Differenza: $\bar y_1-\bar y_2={{e00_10.diff|m}}$.
>
> **(a)** $\text{se}=\sqrt{ {{e00_10.s1|m}}^2/{{e00_10.n1|m}}+{{e00_10.s2|m}}^2/{{e00_10.n2|m}} }=\sqrt{ {{e00_10.e1|m}}^2+{{e00_10.e2|m}}^2 }={{e00_10.se_d|m}}$.
>
> **(b)** $t={{e00_10.diff|m}}/{{e00_10.se_d|m}}={{e00_10.t|m}}$.
>
> **(c)** $|t|={{e00_10.t|m}}>1{,}96$: si rifiuta $H_0:\mu_1=\mu_2$.
>
> **(d)** Gli intervalli sono $[{{e00_10.lo1|m}};\,{{e00_10.hi1|m}}]$ per A e $[{{e00_10.lo2|m}};\,{{e00_10.hi2|m}}]$ per B: si sovrappongono, perché il limite inferiore di A, ${{e00_10.lo1|m}}$, sta sotto il limite superiore di B, ${{e00_10.hi2|m}}$.
>
> **(e)–(f)** $({{e00_10.diff|m}})\pm1{,}96\times{{e00_10.se_d|m}}=[{{e00_10.lo|m}};\,{{e00_10.hi|m}}]$: lo zero è fuori, in accordo con (c).

> [!warning] Errore tipico
> Concludere dalla sovrapposizione degli intervalli di (d) che le medie non differiscono. Gli intervalli si sovrappongono finché $|\bar y_1-\bar y_2|<1{,}96\,(\text{se}_1+\text{se}_2)={{e00_10.lim|m}}$, mentre il test rifiuta già quando $|\bar y_1-\bar y_2|>1{,}96\sqrt{\text{se}_1^2+\text{se}_2^2}={{e00_10.z_se|m}}$: fra i due valori gli intervalli si sovrappongono e la differenza è comunque significativa.

> [!success] Risposta
> **(a)** L'errore standard della differenza è ${{e00_10.se_d|m}}$. **(b)** $t={{e00_10.t|m}}$. **(c)** Si rifiuta $H_0$: i due tempi medi sono diversi al 5\%. **(d)** Sì, gli intervalli delle due medie si sovrappongono, ma non basta per concludere che le medie coincidano. **(e)–(f)** L'intervallo di confidenza al 95\% per $\mu_1-\mu_2$ è $[{{e00_10.lo|m}};\,{{e00_10.hi|m}}]$ e non contiene lo zero.

![In alto gli intervalli di confidenza al 95\% delle due medie: si sovrappongono (zona ocra). In basso l'intervallo per la differenza, ${{e00_10.diff|m}}$: lo zero ne è fuori, quindi il test rifiuta $H_0$.]({{e00_10.fig.intervalli}}){width=85%}

{{testo:e00_11}}

> [!tip] Richiamo
> Le proporzioni sono medie di variabili di Bernoulli. Sotto $H_0:\pi_1=\pi_2$ i due campioni provengono dalla stessa popolazione, quindi la proporzione comune si stima con quella combinata $\hat\pi=(x_1+x_2)/(n_1+n_2)$ e $\text{se}_0=\sqrt{\hat\pi(1-\hat\pi)(1/n_1+1/n_2)}$; si rifiuta se $|z|>1{,}96$. L'intervallo per $\pi_1-\pi_2$ non assume $H_0$ e usa gli errori standard separati: $\hat\pi_1-\hat\pi_2\pm1{,}96\sqrt{\hat\pi_1(1-\hat\pi_1)/n_1+\hat\pi_2(1-\hat\pi_2)/n_2}$.

> [!example] Svolgimento
> **Impostazione.** $\hat\pi_1={{e00_11.x1|m}}/{{e00_11.n1|m}}={{e00_11.p1|m}}$, $\hat\pi_2={{e00_11.x2|m}}/{{e00_11.n2|m}}={{e00_11.p2|m}}$; differenza ${{e00_11.diff|m}}$.
>
> **(a)** $\hat\pi=\dfrac{ {{e00_11.x1|m}}+{{e00_11.x2|m}} }{ {{e00_11.n1|m}}+{{e00_11.n2|m}} }={{e00_11.pool|m}}$.
>
> **(b)** $\text{se}_0=\sqrt{ {{e00_11.pool|m}}\times(1-{{e00_11.pool|m}})\times\bigl(1/{{e00_11.n1|m}}+1/{{e00_11.n2|m}}\bigr) }={{e00_11.se0|m}}$.
>
> **(c)** $z=\dfrac{ {{e00_11.diff|m}} }{ {{e00_11.se0|m}} }={{e00_11.z|m}}$.
>
> **(d)** $|z|={{e00_11.z|m}}>1{,}96$: si rifiuta $H_0:\pi_1=\pi_2$.
>
> **(e)–(f)** L'errore standard senza $H_0$ è ${{e00_11.se_u|m}}$ e l'intervallo è $({{e00_11.diff|m}})\pm1{,}96\times{{e00_11.se_u|m}}=[{{e00_11.lo|m}};\,{{e00_11.hi|m}}]$: lo zero è fuori, in accordo con (d).

> [!warning] Errore tipico
> Calcolare $\text{se}_0$ come per un solo campione, $\sqrt{\hat\pi(1-\hat\pi)/(n_1+n_2)}$ con $n_1+n_2={{e00_11.n_tot|m}}$, invece di $\sqrt{\hat\pi(1-\hat\pi)(1/n_1+1/n_2)}$: l'errore standard verrebbe ${{e00_11.se_err|m}}$ e la statistica ${{e00_11.z_err|m}}$, molto più grande. La varianza della differenza è la somma delle varianze dei due campioni. Un altro errore è costruire l'intervallo di (e)–(f) con $\text{se}_0$: l'intervallo non può assumere $\pi_1=\pi_2$ e usa gli errori standard separati. Infine, la proporzione combinata va pesata con le numerosità e non è la media semplice delle due quote.

> [!success] Risposta
> **(a)** $\hat\pi={{e00_11.pool|m}}$. **(b)** $\text{se}_0={{e00_11.se0|m}}$. **(c)** $z={{e00_11.z|m}}$. **(d)** Si rifiuta $H_0$: le due offerte hanno quote di accettazione diverse al 5\%. **(e)–(f)** L'intervallo di confidenza al 95\% per $\pi_1-\pi_2$ è $[{{e00_11.lo|m}};\,{{e00_11.hi|m}}]$ e non contiene lo zero.

![A sinistra le due quote di accettazione e la proporzione combinata. A destra la distribuzione di $z$ sotto $H_0$ con la regione di rifiuto al 5\% e la statistica osservata, ${{e00_11.z|m}}$.]({{e00_11.fig.proporzioni}}){width=85%}

{{testo:e00_12}}

> [!tip] Richiamo
> Con dati appaiati si lavora sulle differenze $d_i=\text{dopo}_i-\text{prima}_i$: la media delle differenze è la differenza delle medie e la loro varianza è $s_d^2=s_{\text{dopo}}^2+s_{\text{prima}}^2-2\,s_{\text{dopo},\text{prima}}$, dalla varianza di una combinazione lineare. La covarianza positiva, perché le due misure riguardano lo stesso operaio, riduce la varianza delle differenze e quindi l'errore standard $s_d/\sqrt{n}$. Il coefficiente di correlazione è $r=s_{xy}/(s_x\,s_y)$. Trattare le due misure come indipendenti, cioè ignorare la covarianza, usa una varianza troppo grande e fa perdere potenza al test.

> [!example] Svolgimento
> **Impostazione.** Dalla tabella: prima $\bar y={{e00_12.m_pre|m}}$, $s={{e00_12.s_pre|m}}$; dopo $\bar y={{e00_12.m_post|m}}$, $s={{e00_12.s_post|m}}$; covarianza ${{e00_12.cov|m}}$.
>
> **(a)** $\bar d={{e00_12.m_post|m}}-{{e00_12.m_pre|m}}={{e00_12.d|m}}$.
>
> **(b)** $r=\dfrac{ {{e00_12.cov|m}} }{ {{e00_12.s_pre|m}}\times{{e00_12.s_post|m}} }={{e00_12.r|m}}$: le due misure sono fortemente correlate.
>
> **(c)** $s_d^2={{e00_12.var_pre|m}}+{{e00_12.var_post|m}}-2\times{{e00_12.cov|m}}={{e00_12.var_d|m}}$, quindi $s_d={{e00_12.sd_d|m}}$.
>
> **(d)** $t=\dfrac{ {{e00_12.d|m}} }{ {{e00_12.sd_d|m}}/\sqrt{ {{e00_12.n|m}} } }=\dfrac{ {{e00_12.d|m}} }{ {{e00_12.se|m}} }={{e00_12.t|m}}$.
>
> **(e)** ${{e00_12.t|m}}>1{,}64$: si rifiuta $H_0:\mu_D=0$ a favore di $H_1:\mu_D>0$.
>
> **(f)** Con $\text{Cov}=0$ si avrebbe $s_d^2={{e00_12.var_pre|m}}+{{e00_12.var_post|m}}={{e00_12.somma_var|m}}$, errore standard ${{e00_12.se_ind|m}}$ e $t={{e00_12.d|m}}/{{e00_12.se_ind|m}}={{e00_12.t_ind|m}}$.
>
> **(g)** ${{e00_12.t_ind|m}}<1{,}64$: con quella statistica non si rifiuterebbe $H_0$.

> [!warning] Errore tipico
> Confrontare le due medie come se venissero da due campioni indipendenti, con $\text{se}=\sqrt{(s_{\text{dopo}}^2+s_{\text{prima}}^2)/n}={{e00_12.se_ind|m}}$: si ignora il termine $-2\,s_{\text{dopo},\text{prima}}={{e00_12.due_cov|m}}$ con il segno meno e l'errore standard viene ${{e00_12.rapporto|m}} volte quello giusto (${{e00_12.se|m}}$). La conclusione si ribalta: l'aumento sembra non significativo mentre la produttività media è aumentata in modo significativo. Attribuirlo al corso richiede di escludere altre cause, e un confronto prima/dopo senza gruppo di controllo non lo permette. Con dati appaiati la variabilità fra operai si cancella nelle differenze.

> [!success] Risposta
> **(a)** $\bar d={{e00_12.d|m}}$. **(b)** $r={{e00_12.r|m}}$. **(c)** $s_d={{e00_12.sd_d|m}}$. **(d)** $t={{e00_12.t|m}}$. **(e)** Si rifiuta $H_0$: al 5\% la produttività media è aumentata in modo significativo; attribuirlo al corso richiede di escludere altre cause, e un confronto prima/dopo senza gruppo di controllo non lo permette. **(f)** Ignorando la covarianza si ottiene $t={{e00_12.t_ind|m}}$. **(g)** Con quella statistica non si rifiuta $H_0$: è la conclusione sbagliata, dovuta a un errore standard gonfiato.

![A sinistra le coppie (prima, dopo) stanno vicino alla retta tratteggiata e tendono a stare sopra: le due misure sono molto correlate. A destra la differenza media ${{e00_12.d|m}}$ con l'intervallo $\bar d\pm1{,}64\,\text{se}$: con la covarianza l'estremo inferiore sta sopra lo zero (rifiuto), ignorandola l'intervallo comprende lo zero.]({{e00_12.fig.appaiati}}){width=85%}

{{testo:e00_13}}

> [!tip] Richiamo
> $E[\epsilon\mid X=x]$ è la media dell'errore fra le unità con $X=x$. Se $E[\epsilon\mid X=x]=0$ per ogni $x$, allora $E[\epsilon]=0$, $\text{Cov}(X,\epsilon)=0$ e $E[Y\mid X]=\alpha+\beta X$, quindi $\Delta E[Y\mid X]=\beta\,\Delta X$. Non vale il contrario: un errore può essere incorrelato con $X$ ed avere comunque media condizionale non nulla (dipendenza non lineare). Allora $E[Y\mid X=x]=\alpha+\beta x+E[\epsilon\mid X=x]$ non è la retta e $\Delta E[Y\mid X]=\beta\,\Delta X+\Delta E[\epsilon\mid X]$. Se invece $\text{Cov}(X,\epsilon)\neq0$, la pendenza della regressione è $\text{Cov}(X,Y)/\text{Var}(X)=\beta+\text{Cov}(X,\epsilon)/\text{Var}(X)\neq\beta$.

> [!example] Svolgimento
> **Impostazione.** Dalla distribuzione di $X$: $E[X]={{e00_13.ex|m}}$ e $\text{Var}(X)={{e00_13.varx|m}}$.
>
> **(a)** $E[\epsilon]=({{e00_13.p1|m}})({{e00_13.ep1|m}})+({{e00_13.p2|m}})({{e00_13.ep2|m}})+({{e00_13.p3|m}})({{e00_13.ep3|m}})+({{e00_13.p4|m}})({{e00_13.ep4|m}})+({{e00_13.p5|m}})({{e00_13.ep5|m}})={{e00_13.e_eps_p|m}}$.
>
> **(b)** $E[X\epsilon]=\sum_x x\,P(X=x)\,E[\epsilon\mid X=x]={{e00_13.exe_p|m}}$, quindi $\text{Cov}(X,\epsilon)={{e00_13.exe_p|m}}-{{e00_13.ex|m}}\times{{e00_13.e_eps_p|m}}={{e00_13.cov_p|m}}$.
>
> **(c)** No: le medie condizionali valgono ${{e00_13.ep1|m}}$, ${{e00_13.ep2|m}}$, ${{e00_13.ep3|m}}$, ${{e00_13.ep4|m}}$, ${{e00_13.ep5|m}}$, non sono tutte nulle. Covarianza nulla non implica media condizionale nulla: nel modello P l'errore dipende da $X$ attraverso $(X-{{e00_13.ex|m}})^2$, una relazione non lineare che la covarianza non vede.
>
> **(d)** $E[Y\mid X=x]=\alpha+\beta x+E[\epsilon\mid X=x]$. Per $x={{e00_13.xa|m}}$ vale ${{e00_13.ey_a|m}}$ e per $x={{e00_13.xb|m}}$ vale ${{e00_13.ey_b|m}}$: la variazione è $\beta+\bigl(E[\epsilon\mid X={{e00_13.xb|m}}]-E[\epsilon\mid X={{e00_13.xa|m}}]\bigr)={{e00_13.beta|m}}+\bigl({{e00_13.ep4|m}}-({{e00_13.ep3|m}})\bigr)={{e00_13.delta|m}}$, e non $\beta={{e00_13.beta|m}}$.
>
> **(e)** Nel modello Q $E[\epsilon]={{e00_13.e_eps_q|m}}$ e $E[X\epsilon]={{e00_13.exe_q|m}}$, quindi $\text{Cov}(X,\epsilon)={{e00_13.cov_q|m}}$.
>
> **(f)** $\dfrac{\text{Cov}(X,Y)}{\text{Var}(X)}-\beta=\dfrac{\text{Cov}(X,\epsilon)}{\text{Var}(X)}=\dfrac{ {{e00_13.cov_q|m}} }{ {{e00_13.varx|m}} }={{e00_13.bias_q|m}}$: la pendenza della regressione vale ${{e00_13.slope_q|m}}$ e non $\beta={{e00_13.beta|m}}$.

> [!warning] Errore tipico
> Concludere dalla covarianza nulla del modello P che $E[\epsilon\mid X]=0$ e quindi che $\beta$ misuri ovunque l'effetto di $X$ su $Y$: l'incorrelazione è solo una conseguenza di $E[\epsilon\mid X]=0$, non equivale ad essa. Nel modello P la pendenza della regressione è ancora ${{e00_13.slope_p|m}}$, ma l'effetto di un passo di $X$ cambia con $x$. Nel modello Q, invece, anche la pendenza è sbagliata di ${{e00_13.bias_q|m}}$.

> [!success] Risposta
> **(a)** Nel modello P $E[\epsilon]={{e00_13.e_eps_p|m}}$. **(b)** $\text{Cov}(X,\epsilon)={{e00_13.cov_p|m}}$. **(c)** No: l'errore ha medie condizionali non nulle, benché incorrelato con $X$. **(d)** $E[Y\mid X]$ varia di ${{e00_13.delta|m}}$, non di $\beta={{e00_13.beta|m}}$. **(e)** Nel modello Q $\text{Cov}(X,\epsilon)={{e00_13.cov_q|m}}$. **(f)** La pendenza della regressione supera $\beta$ di ${{e00_13.bias_q|m}}$.

![Medie condizionali $E[Y\mid X=x]$ (punti) contro la retta $\alpha+\beta x$ (tratteggio grigio) e la retta di regressione (rossa). Nel modello P i punti formano una curva attorno alla retta, che ha però pendenza $\beta$: covarianza nulla ma media condizionale non nulla. Nel modello Q i punti stanno su una retta più ripida, di pendenza ${{e00_13.slope_q|m}}$.]({{e00_13.fig.medie}}){width=85%}

{{testo:e00_14}}

> [!tip] Richiamo
> In un campione casuale semplice le $Y_i$ sono indipendenti, $\text{Cov}(Y_i,Y_j)=0$, e $\text{Var}(\bar Y)=\sigma^2/n$. Se ogni coppia di osservazioni ha correlazione $\rho$, $\text{Cov}(Y_i,Y_j)=\rho\,\sigma^2$ e $\text{Var}(Y_1+\dots+Y_n)=\sum_i\text{Var}(Y_i)+\sum_{i\neq j}\text{Cov}(Y_i,Y_j)=n\sigma^2+n(n-1)\rho\sigma^2=n\sigma^2\,[1+(n-1)\rho]$. Dunque $\text{Var}(\bar Y)=\frac{\sigma^2}{n}\,[1+(n-1)\rho]$. La media resta corretta, $E[\bar Y]=\mu$, perché il valore atteso non dipende dalle covarianze, ma l'errore standard cresce di $\sqrt{1+(n-1)\rho}$: osservazioni correlate valgono meno di osservazioni indipendenti, e trattarle da indipendenti fa rifiutare troppo.

> [!example] Svolgimento
> **Impostazione.** Si confrontano la varianza della somma sotto indipendenza e con correlazione $\rho$, poi si ripete il test con i due errori standard.
>
> **(a)** $\sigma/\sqrt{n}={{e00_14.sigma|m}}/\sqrt{ {{e00_14.n|m}} }={{e00_14.se_ing|m}}$.
>
> **(b)** $E[\bar Y]=\dfrac{1}{n}\sum_iE[Y_i]=\mu$: sì, la correlazione non incide sul valore atteso.
>
> **(c)** I termini con $i\neq j$ sono $n(n-1)={{e00_14.n_coppie|m}}$, ciascuno con covarianza $\rho\sigma^2={{e00_14.var_coppie|m}}$. Quindi $\text{Var}(Y_1+\dots+Y_n)={{e00_14.n|m}}\times{{e00_14.sigma|m}}^2+{{e00_14.n_coppie|m}}\times{{e00_14.var_coppie|m}}={{e00_14.var_somma|m}}$, contro ${{e00_14.var_ind|m}}$ con osservazioni indipendenti.
>
> **(d)** $\text{se}=\sqrt{\text{Var}(\bar Y)}=\sqrt{ {{e00_14.var_somma|m}} }/{{e00_14.n|m}}={{e00_14.se_vero|m}}$, cioè ${{e00_14.fattore|m}}$ volte l'errore standard di (a): $\sqrt{1+(n-1)\rho}=\sqrt{ {{e00_14.fatt_var|m}} }$.
>
> **(e)** $t=({{e00_14.ybar|m}}-{{e00_14.mu0|m}})/{{e00_14.se_ing|m}}={{e00_14.t_ing|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(f)** $t=({{e00_14.ybar|m}}-{{e00_14.mu0|m}})/{{e00_14.se_vero|m}}={{e00_14.t_vero|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$. L'intervallo di confidenza al 95\% è $[{{e00_14.lo|m}};\,{{e00_14.hi|m}}]$ e contiene ${{e00_14.mu0|m}}$, mentre con l'errore standard ingenuo sarebbe $[{{e00_14.lo_ing|m}};\,{{e00_14.hi_ing|m}}]$.

> [!warning] Errore tipico
> Usare $\sigma/\sqrt{n}$ come se gli alunni fossero un campione casuale semplice. La correlazione non distorce $\bar Y$ ma ne cambia la varianza: l'errore standard ingenuo è ${{e00_14.fattore|m}}$ volte troppo piccolo e porta a rifiutare $H_0$ per un effetto che può essere solo l'effetto classe. Le ${{e00_14.n|m}}$ osservazioni correlate valgono come ${{e00_14.neff|m}}$ osservazioni indipendenti.

> [!success] Risposta
> **(a)** L'errore standard con osservazioni indipendenti sarebbe ${{e00_14.se_ing|m}}$. **(b)** Sì: $\bar Y$ resta corretto. **(c)** $\text{Var}(Y_1+\dots+Y_n)={{e00_14.var_somma|m}}$. **(d)** L'errore standard è ${{e00_14.se_vero|m}}$. **(e)** Con l'errore standard ingenuo si rifiuta $H_0$. **(f)** Con quello corretto non si rifiuta $H_0$: la differenza dalla media nazionale non è significativa.

![Distribuzione di $\bar Y$ sotto $H_0$ con l'errore standard ingenuo (blu) e con quello corretto per la correlazione (rosso); le linee tratteggiate sono $\mu_0\pm1{,}96\,\text{se}$. La media osservata, ${{e00_14.ybar|m}}$, sta fuori dalle linee blu e dentro quelle rosse.]({{e00_14.fig.densita}}){width=85%}
