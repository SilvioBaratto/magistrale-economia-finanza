{{testo:e03_01}}

> [!tip] Richiamo
> Con la dipendente in logaritmo, una variazione $\Delta x$ del regressore dà $\Delta\log(y)=\beta\,\Delta x$, e poiché $\Delta\log(y)\approx\Delta y/y$ la variazione percentuale attesa è $100\cdot\beta\,\Delta x$. Per decidere su $H_0:\beta=0$ si guarda l'intervallo di confidenza al 95\%, $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$: se lo zero ne sta fuori si rifiuta.

> [!example] Svolgimento
> **Impostazione.** La (a) chiede un effetto in percentuale su una dipendente in logaritmo; la (b) è un test bilaterale su $\beta_1$.
>
> **(a)** Con $\Delta\text{istr}=1$: $\Delta\%\,\text{salario}\approx 100\times\hat\beta_1 = 100\times {{e03_01.beta|m}} = {{e03_01.pct|m}}$.
>
> **(b)** Si verifica $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. L'intervallo di confidenza al 95\% è $[{{e03_01.ic_lo|m}};\,{{e03_01.ic_hi|m}}]$ e lo zero ne è fuori. Lo stesso dice il rapporto $t={{e03_01.t|m}}$, in valore assoluto maggiore di $1{,}96$.

> [!warning] Errore tipico
> Leggere $\hat\beta_1={{e03_01.beta|m}}$ come se fosse già una percentuale. Con la dipendente in logaritmo il coefficiente è una variazione in punti di $\log$: va moltiplicato per $100$.

> [!success] Risposta
> **(a)** Un anno di istruzione in più fa aumentare il salario di circa ${{e03_01.pct|m}}\%$. **(b)** Lo zero non cade nell'intervallo di confidenza al 95\%, quindi si rifiuta $H_0$: l'istruzione è significativa al 5\%.

![Intervallo di confidenza al 95\% per $\beta_1$, $[{{e03_01.ic_lo|m}};\,{{e03_01.ic_hi|m}}]$: lo zero è fuori dall'intervallo.]({{e03_01.fig.ic}}){width=85%}

{{testo:e03_02}}

> [!tip] Richiamo
> Con dipendente e regressore entrambi in logaritmo, $\Delta\log(y)=\beta\,\Delta\log(x)$ e, poiché $\Delta\log(z)\approx\Delta z/z$, si ha $\Delta y/y\approx\beta\,\Delta x/x$: $\beta$ è l'elasticità, il rapporto fra la variazione percentuale di $y$ e quella di $x$. Una variazione di $x$ del $m$ per cento fa variare $y$ di $\beta\,m$ per cento. Per decidere su $H_0:\beta=0$ si guarda l'intervallo di confidenza al 95\%, $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** Dipendente e regressore sono in logaritmo: $\hat\beta_1$ si legge come elasticità e la variazione di `nox` entra già in percentuale, senza moltiplicare per $100$.
>
> **(a)** L'elasticità è $\hat\beta_1={{e03_02.el|m}}$.
>
> **(b)** $\Delta\%\,\text{prezzo}\approx\hat\beta_1\times\Delta\%\,\text{nox}={{e03_02.el|m}}\times {{e03_02.var|m}}={{e03_02.pct|m}}\%$.
>
> **(c)** Si verifica $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. L'intervallo di confidenza al 95\% è $[{{e03_02.ic_lo|m}};\,{{e03_02.ic_hi|m}}]$ e lo zero ne è fuori. Lo stesso dice $t={{e03_02.t|m}}$, in valore assoluto maggiore di $1{,}96$.

> [!warning] Errore tipico
> Moltiplicare $\hat\beta_1$ per $100$ come si fa con un regressore in livello. Qui $\hat\beta_1$ è già il rapporto fra due variazioni percentuali: $100\times\hat\beta_1$ darebbe la variazione per $\Delta\log(\text{nox})=1$, non per un raddoppio: un raddoppio è $\Delta\log(\text{nox})=\ln 2$ e l'approssimazione lineare non regge per variazioni così grandi.

> [!success] Risposta
> **(a)** L'elasticità del prezzo rispetto all'inquinamento è ${{e03_02.el|m}}$: ad ogni aumento dell'1\% di `nox` il prezzo atteso varia di circa ${{e03_02.el|m}}\%$. **(b)** Con `nox` $+{{e03_02.var|m}}\%$ il prezzo varia di circa ${{e03_02.pct|m}}\%$. **(c)** Lo zero non cade nell'intervallo di confidenza al 95\%, quindi si rifiuta $H_0$: l'effetto è significativo al 5\%.

![Variazione percentuale attesa del prezzo al variare di `nox`: retta di pendenza $\hat\beta_1={{e03_02.el|m}}$ con banda al 95\%. Per $+{{e03_02.var|m}}\%$ di `nox` il prezzo varia di ${{e03_02.pct|m}}\%$.]({{e03_02.fig.effetto}}){width=85%}

{{testo:e03_03}}

> [!tip] Richiamo
> Per lo stimatore di $\beta_j$ vale $\widehat{\text{Var}}(\hat\beta_j)=\dfrac{\hat\sigma^2}{\sum_i(x_{ij}-\bar x_j)^2}\cdot\dfrac{1}{1-R_j^2}$ e il secondo fattore è il $\text{VIF}_j$. Rispetto al caso di regressori indipendenti ($R_j^2=0$) la varianza è moltiplicata per il VIF e l'errore standard per $\sqrt{\text{VIF}_j}$. Con un VIF maggiore di $10$ si parla di quasi-collinearità. La quasi-collinearità non distorce gli stimatori: ne gonfia soltanto gli errori standard e abbassa le statistiche $t$.

> [!example] Svolgimento
> **Impostazione.** La (a) è un confronto di ogni VIF con la soglia $10$; la (b) è la radice quadrata del VIF di `reddito`; la (c) incrocia il VIF con la significatività del coefficiente.
>
> **(a)** I VIF di `reddito` (${{e03_03.vif|m}}$) e di `sq_reddito` (${{e03_03.vif_sq|m}}$) superano $10$; tutti gli altri stanno sotto soglia, il più alto è ${{e03_03.resto|m}}$. I regressori sopra soglia sono ${{e03_03.conta}}$.
>
> **(b)** $\sqrt{\text{VIF}}=\sqrt{{{e03_03.vif|m}}}={{e03_03.fattore|m}}$: l'errore standard di $\hat\beta_1$ è circa ${{e03_03.fattore|m}}$ volte quello che si avrebbe con regressori indipendenti.
>
> **(c)** Il coefficiente di `reddito` ha $t={{e03_03.t|m}}$, in valore assoluto minore di $1{,}96$: non è significativo. Il suo VIF supera $10$.

> [!warning] Errore tipico
> Rispondere ${{e03_03.vif|m}}$ volte, cioè il VIF stesso: il VIF moltiplica la varianza, e l'errore standard ne è la radice. Un altro errore è dedurre dal VIF alto che le stime siano distorte: la quasi-collinearità gonfia la varianza, non crea distorsione. Il VIF alto fra $x$ e $x^2$ è strutturale (centrando $x$ scompare, senza cambiare adattamento né effetti marginali), e la $t$ di $\beta_1$ verifica l'effetto marginale in $\text{reddito}=0$, non la rilevanza del reddito, che si giudica con un test $F$ congiunto su $H_0:\beta_1=\beta_2=0$ o con l'effetto marginale a livelli osservati.

> [!success] Risposta
> **(a)** Due regressori hanno un VIF superiore a $10$: `reddito` e `sq_reddito`, com'è naturale perché la seconda è il quadrato della prima. **(b)** L'errore standard di `reddito` è gonfiato di circa ${{e03_03.fattore|m}}$ volte. **(c)** Sì: il VIF è maggiore di $10$ e il coefficiente non è significativo, quindi la quasi-collinearità è una spiegazione plausibile della non significatività.

![VIF di ogni regressore con la soglia $10$ (a sinistra) e fattore $\sqrt{\text{VIF}}$ di aumento dell'errore standard (a destra): in rosso i due regressori sopra soglia.]({{e03_03.fig.vif}}){width=85%}

{{testo:e03_04}}

> [!tip] Richiamo
> Con la dipendente in logaritmo $\Delta y/y\approx\beta\,\Delta x$: l'effetto è una variazione relativa, non un importo. Per ottenere $\Delta x$ data una variazione relativa si inverte la formula, $\Delta x=(\Delta y/y)/\beta$. Per una dummy $\Delta x=1$ e la variazione percentuale è $100\,\beta$. Un importo in dollari si ottiene moltiplicando per il salario di partenza, $\Delta y\approx\beta\,y_0$; per confrontare un'affermazione in dollari con il coefficiente la si divide per $y_0$ e la si guarda nell'intervallo di confidenza $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** La (a) inverte l'effetto marginale di `istr`; la (b) legge la dummy come percentuale; la (c) e la (d) portano la percentuale in dollari.
>
> **(a)** Si cerca $\Delta\text{istr}$ tale che $\Delta\text{salario}/\text{salario}={{e03_04.obiettivo|m}}/100$: $\Delta\text{istr}=\dfrac{ {{e03_04.obiettivo|m}}/100 }{ \hat\beta_1 }=\dfrac{ {{e03_04.obiettivo|m}}/100 }{ {{e03_04.b1|m}} }={{e03_04.anni|m}}$ anni.
>
> **(b)** Per `sposato` $\Delta x=1$: $100\times\hat\beta_3=100\times{{e03_04.b3|m}}={{e03_04.pct|m}}\%$.
>
> **(c)** $\Delta\text{salario}\approx\hat\beta_3\times w_0={{e03_04.b3|m}}\times{{e03_04.w0|m}}={{e03_04.dollari|m}}$ dollari al mese.
>
> **(d)** L'affermazione equivale a $\beta_3\,w_0={{e03_04.riv|m}}$, cioè $\beta_3={{e03_04.riv|m}}/{{e03_04.w0|m}}={{e03_04.beta_riv|m}}$. L'intervallo di confidenza al 95\% per l'effetto in dollari è $\bigl(\hat\beta_3\pm 1{,}96\,\widehat{\text{se}}(\hat\beta_3)\bigr)\times w_0=[{{e03_04.ic_lo|m}};\,{{e03_04.ic_hi|m}}]$ e ${{e03_04.riv|m}}$ ne è fuori. Lo stesso dice $t=({{e03_04.b3|m}}-{{e03_04.beta_riv|m}})/{{e03_04.se3|m}}={{e03_04.t_riv|m}}$, in valore assoluto maggiore di $1{,}96$.

> [!warning] Errore tipico
> Leggere ${{e03_04.b3|m}}$ o ${{e03_04.pct|m}}$ come dollari. Con la dipendente in logaritmo il coefficiente della dummy è una variazione relativa del salario e diventa un importo in dollari solo moltiplicandolo per il salario di partenza. Per lo stesso motivo non si può confrontare l'affermazione in dollari direttamente con $\hat\beta_3$.

> [!success] Risposta
> **(a)** Servono circa ${{e03_04.anni|m}}$ anni di istruzione in più. **(b)** Uno sposato guadagna in media circa il ${{e03_04.pct|m}}\%$ in più di un single con le stesse altre caratteristiche. **(c)** Su un salario di ${{e03_04.w0|m}}$ dollari sono circa ${{e03_04.dollari|m}}$ dollari al mese. **(d)** No: l'intervallo di confidenza al 95\% per la differenza è $[{{e03_04.ic_lo|m}};\,{{e03_04.ic_hi|m}}]$ dollari e non contiene ${{e03_04.riv|m}}$, quindi l'affermazione non è compatibile con i dati.

![Sopra: variazione percentuale attesa del salario al crescere dell'istruzione; l'obiettivo del ${{e03_04.obiettivo|m}}\%$ si raggiunge con ${{e03_04.anni|m}}$ anni in più. Sotto: intervallo di confidenza al 95\% per la differenza in dollari fra sposato e single, con l'affermazione di ${{e03_04.riv|m}}$ dollari fuori dall'intervallo.]({{e03_04.fig.effetto}}){width=85%}

{{testo:e03_05}}

> [!tip] Richiamo
> Con la dipendente in livello e un regressore in logaritmo, $\Delta y=\beta\,\Delta\log(x)$ e, siccome $\Delta\log(x)\approx\Delta x/x$, si ha $\Delta y\approx\beta\,(\Delta x/x)$. Un aumento relativo del reddito del $m$ per cento ($\Delta x/x=m/100$) fa variare $y$ di $\beta\,m/100$ unità di misura di $y$: non è una percentuale di $y$, e non dipende dal livello di partenza di $x$. Per decidere su $H_0:\beta=0$ si guarda l'intervallo di confidenza al 95\%, $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** `rich` è in livello (migliaia di dollari) e `red` entra in logaritmo: $\hat\beta_1$ è in migliaia di dollari per unità di $\log(\text{red})$.
>
> **(a)** $\Delta\text{rich}\approx\hat\beta_1\times\dfrac{ {{e03_05.var|m}} }{100}={{e03_05.beta|m}}\times\dfrac{ {{e03_05.var|m}} }{100}={{e03_05.migliaia|m}}$ migliaia di dollari, cioè ${{e03_05.dollari|m}}$ dollari.
>
> **(b)** Da $\Delta\text{rich}=\hat\beta_1\,\Delta\text{red}/\text{red}$ si ha $\Delta\text{red}/\text{red}=\Delta\text{rich}/\hat\beta_1$, con $\Delta\text{rich}$ in migliaia di dollari: $\Delta\%\,\text{red}=100\times\dfrac{ {{e03_05.obiettivo|m}}/{{e03_05.scala|m}} }{ {{e03_05.beta|m}} }={{e03_05.pct|m}}\%$.
>
> **(c)** L'intervallo di confidenza al 95\% è $[{{e03_05.ic_lo|m}};\,{{e03_05.ic_hi|m}}]$ e lo zero ne è fuori. Lo stesso dice $t={{e03_05.t|m}}$, in valore assoluto maggiore di $1{,}96$.
>
> **(d)** La variazione attesa $\hat\beta_1\,\Delta\text{red}/\text{red}$ dipende solo dalla variazione relativa del reddito, non dal suo livello: per un aumento del ${{e03_05.var|m}}\%$ è ${{e03_05.migliaia|m}}$ migliaia di dollari sia con reddito ${{e03_05.ra|m}}$ sia con reddito ${{e03_05.rb|m}}$.

> [!warning] Errore tipico
> Leggere $\hat\beta_1={{e03_05.beta|m}}$ come una variazione percentuale della ricchezza, o moltiplicarlo per $100$, come si fa quando la dipendente è in logaritmo. Qui la dipendente è in livello: $\hat\beta_1$ è in migliaia di dollari e per una variazione relativa del reddito va diviso per $100$. Un altro errore è dimenticare di convertire le migliaia in dollari.

> [!success] Risposta
> **(a)** Con il reddito $+{{e03_05.var|m}}\%$ la ricchezza attesa aumenta di circa ${{e03_05.dollari|m}}$ dollari. **(b)** Per ${{e03_05.obiettivo|m}}$ dollari in più il reddito deve crescere di circa il ${{e03_05.pct|m}}\%$. **(c)** Lo zero non cade nell'intervallo di confidenza al 95\%, quindi si rifiuta $H_0$: il reddito è significativo al 5\%. **(d)** Sì: a parità di variazione relativa del reddito, la variazione attesa di ricchezza è la stessa per i due redditi.

![Ricchezza attesa in funzione del reddito, a età fissata: un aumento del ${{e03_05.var|m}}\%$ aggiunge circa ${{e03_05.migliaia|m}}$ migliaia di dollari sia partendo da ${{e03_05.ra|m}}$ sia da ${{e03_05.rb|m}}$.]({{e03_05.fig.curva}}){width=85%}

{{testo:e03_06}}

> [!tip] Richiamo
> Quando compaiono $x$ e $x^2$ l'effetto di $x$ dipende dal livello a cui lo si valuta. Da $\Delta\log(y)=\beta_2\,\Delta x+\beta_3\,\Delta(x^2)$ e $\Delta(x^2)\approx 2x\,\Delta x$ si ottiene l'effetto marginale $\Delta\log(y)\approx(\beta_2+2\beta_3 x)\,\Delta x$, in percentuale $100\,(\beta_2+2\beta_3 x)$. Si annulla in $x^*=-\beta_2/(2\beta_3)$: con $\beta_3<0$ l'effetto è positivo prima di $x^*$ e negativo dopo.

> [!example] Svolgimento
> **Impostazione.** La (a) è un test su $\beta_3$; la (b) valuta l'effetto marginale in un punto; la (c) cerca il punto in cui si annulla.
>
> **(a)** $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$. Il rapporto $t$ vale ${{e03_06.t3|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** $100\,(\hat\beta_2+2\hat\beta_3\,x_0)=100\times\bigl({{e03_06.b2|m}}+2\times({{e03_06.b3|m}})\times{{e03_06.x0|m}}\bigr)={{e03_06.eff|m}}$.
>
> **(c)** $x^*=-\hat\beta_2/(2\hat\beta_3)=-{{e03_06.b2|m}}\,/\,\bigl(2\times({{e03_06.b3|m}})\bigr)={{e03_06.punto|m}}$ anni.

> [!warning] Errore tipico
> Interpretare $\hat\beta_2$ da solo come effetto dell'esperienza: con il termine al quadrato nel modello l'effetto è $\hat\beta_2+2\hat\beta_3\,x$ e cambia con $x$. Un altro errore è dimenticare che $x^*$ va confrontato con l'intervallo di esperienza osservato: fuori da quell'intervallo è un'estrapolazione.

> [!success] Risposta
> **(a)** Il termine al quadrato è significativo al 5\%: la relazione non è lineare. **(b)** Con ${{e03_06.x0}}$ anni di esperienza un anno in più fa aumentare il salario di circa ${{e03_06.eff|m}}\%$. **(c)** L'effetto marginale si annulla a circa ${{e03_06.punto|m}}$ anni: prima il salario cresce con l'esperienza, poi decresce.

![Effetto marginale dell'esperienza: positivo fino a ${{e03_06.punto|m}}$ anni, poi negativo.]({{e03_06.fig.effetto}}){width=85%}

{{testo:e03_07}}

> [!tip] Richiamo
> Se il modello completo ha $x_1$ e $x_2$ e si omette $x_2$, la stima di $\beta_1$ nel modello ristretto è $\tilde\beta_1=\hat\beta_1+\hat\beta_2\,\hat\delta_1$, dove $\hat\delta_1$ è il coefficiente di $x_1$ nella regressione di $x_2$ sui regressori inclusi. La distorsione c'è soltanto se valgono **entrambe** le condizioni: $x_2$ conta ($\beta_2\neq 0$) e $x_2$ è correlata con $x_1$ ($\delta_1\neq 0$). Se ne manca una, omettere $x_2$ non distorce la stima di $\beta_1$.

> [!example] Svolgimento
> **Impostazione.** Si controllano le due condizioni, una nel Modello 2 e una nella regressione ausiliaria.
>
> **(a)** $100\times(\tilde\beta_1-\hat\beta_1)=100\times({{e03_07.b1_ristretto|m}}-{{e03_07.b1_completo|m}})={{e03_07.a|m}}$ punti percentuali: la stima quasi non si muove.
>
> **(b)** Nel Modello 2 il rapporto $t$ di `ore` vale ${{e03_07.t_ore|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_3=0$, quindi `ore` conta.
>
> **(c)** Nella regressione ausiliaria $\hat\delta_1={{e03_07.delta|m}}$ con $t={{e03_07.t_delta|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0:\delta_1=0$, quindi non c'è evidenza di correlazione (parziale) fra `ore` e `istr`.
>
> **(d)** Manca la seconda condizione. Come verifica, $100\,\hat\beta_3\,\hat\delta_1=100\times{{e03_07.b_ore|m}}\times({{e03_07.delta|m}})={{e03_07.c|m}}$ punti percentuali, uguale alla differenza in (a).

> [!warning] Errore tipico
> Concludere per la distorsione solo perché la variabile omessa è significativa nel Modello 2. Serve anche che sia correlata con il regressore incluso: se non lo è, il Modello 1 lascia `ore` nell'errore ma l'errore resta incorrelato con `istr`, e la stima del rendimento dell'istruzione cambia di poco. Il mancato rifiuto di $H_0:\delta_1=0$ non prova che $\delta_1$ sia nullo: dice che i dati non lo distinguono da zero, e infatti la stima cambia di poco.

> [!success] Risposta
> **(a)** $100\,(\tilde\beta_1-\hat\beta_1)={{e03_07.a|m}}$ punti percentuali: la stima del rendimento dell'istruzione quasi non cambia. **(b)** Si rifiuta $H_0:\beta_3=0$: `ore` è rilevante per il salario. **(c)** Non si rifiuta $H_0:\delta_1=0$: non c'è evidenza di correlazione (parziale) fra `ore` e `istr`. **(d)** No: il Modello 1 omette una variabile rilevante, ma non c'è evidenza di correlazione (parziale) fra `ore` e `istr`, quindi non c'è evidenza di distorsione da variabile omessa su $\hat\beta_1$.

![Coefficiente dell'istruzione, con intervallo al 95\%: nei due modelli i punti e gli intervalli sono quasi sovrapposti.]({{e03_07.fig.confronto}}){width=85%}

{{testo:e03_08}}

> [!tip] Richiamo
> Se si osserva $x^*=x+u$, con $u$ incorrelato con $x$ e con $\epsilon$, il modello $y=\alpha+\gamma\,x+\epsilon$ diventa $y=\alpha+\gamma\,x^*+\epsilon^*$ con $\epsilon^*=\epsilon-\gamma\,u$. Allora $\text{Cov}(x^*,\epsilon^*)=\text{Cov}(x+u,\,\epsilon-\gamma u)=-\gamma\,\text{Var}(u)\neq 0$: il regressore è endogeno anche se $u$ ha media nulla. Lo stimatore OLS converge a $\text{Cov}(x^*,y)/\text{Var}(x^*)=\gamma\,\text{Var}(x)/\bigl(\text{Var}(x)+\text{Var}(u)\bigr)$: la stima è attenuata verso zero e non è consistente.

> [!example] Svolgimento
> **Impostazione.** Si calcolano il fattore di attenuazione, il limite della stima e la covarianza che genera l'endogeneità, poi si confronta il limite con la tabella.
>
> **(a)** $\lambda=\dfrac{ {{e03_08.sx2|m}} }{ {{e03_08.sx2|m}}+{{e03_08.su2|m}} }={{e03_08.lam|m}}$.
>
> **(b)** Il limite è $\gamma\lambda={{e03_08.gamma|m}}\times{{e03_08.lam|m}}={{e03_08.limite|m}}$. La stima della tabella, ${{e03_08.b|m}}$, è molto più vicina a questo valore che a $\gamma$.
>
> **(c)** $\text{Cov}(x^*,\epsilon^*)=-\gamma\,\text{Var}(u)=-{{e03_08.gamma|m}}\times{{e03_08.su2|m}}={{e03_08.cov|m}}$.
>
> **(d)** L'intervallo di confidenza al 95\% per il coefficiente di `red_dich` è $[{{e03_08.ic_lo|m}};\,{{e03_08.ic_hi|m}}]$ e $\gamma={{e03_08.gamma|m}}$ ne è fuori.
>
> **(e)** Nel modello scritto con $x^*$ l'errore $\epsilon^*=\epsilon-\gamma u$ contiene $u$, e $u$ è una parte di $x^*=x+u$: regressore ed errore sono correlati, anche se $u$ ha media nulla e non è correlato con $x$.

> [!warning] Errore tipico
> Ritenere innocuo l'errore di misura perché ha media zero. Contano la correlazione fra il regressore osservato e l'errore, non la media di $u$: $x^*$ contiene $u$. Un altro errore è pensare che la distorsione sparisca aumentando $n$: è una non consistenza, la stima converge a $\gamma\lambda$ e non a $\gamma$.

> [!success] Risposta
> **(a)** $\lambda={{e03_08.lam|m}}$. **(b)** Il coefficiente di `red_dich` converge a $\gamma\lambda={{e03_08.limite|m}}$, non a $\gamma={{e03_08.gamma|m}}$: la stima è attenuata. **(c)** $\text{Cov}(x^*,\epsilon^*)={{e03_08.cov|m}}$. **(d)** No: l'intervallo di confidenza al 95\% non contiene il valore vero. **(e)** Il regressore osservato contiene l'errore di misura, che finisce anche nell'errore del modello: è endogeno, e gli stimatori OLS sono distorti e non consistenti.

![Consumi contro reddito vero e contro reddito dichiarato, con le due rette stimate: l'errore di misura appiattisce la pendenza.]({{e03_08.fig.rette}}){width=85%}

{{testo:e03_09}}

> [!tip] Richiamo
> Il teorema di Frisch-Waugh-Lovell dice che $\hat\beta_1$ della regressione multipla di $y$ su $x_1$ e $x_2$ si ottiene in tre passi: (1) si regredisce $x_1$ su $x_2$ e si prendono i residui $u_1$; (2) si regredisce $y$ su $x_2$ e si prendono i residui $u_y$; (3) si regredisce $u_y$ su $u_1$. La pendenza del passo (3) coincide con $\hat\beta_1$: è l'associazione fra $y$ e la parte di $x_1$ non spiegata da $x_2$. Il VIF di $x_1$ è $1/(1-R_1^2)$, con $R_1^2$ l'$R^2$ della regressione di $x_1$ sugli altri regressori, qui la (1).

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) si leggono dal passo (3); la (c) usa l'$R^2$ del passo (1).
>
> **(a)** Il coefficiente di `u_classe` nel passo (3) è $\hat\beta_1={{e03_09.beta|m}}$.
>
> **(b)** Si verifica $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. L'intervallo di confidenza al 95\% è $[{{e03_09.ic_lo|m}};\,{{e03_09.ic_hi|m}}]$ e contiene lo zero. Lo stesso dice $t={{e03_09.t|m}}$, in valore assoluto minore di $1{,}96$.
>
> **(c)** $R^2={{e03_09.r2|m}}$ nel passo (1), quindi $\text{VIF}=1/(1-R^2)=1/(1-{{e03_09.r2|m}})={{e03_09.vif|m}}$.
>
> **(d)** I residui di una regressione con la costante hanno media nulla; $u_{\text{punteggio}}$ e $u_{\text{classe}}$ hanno entrambi media zero, e la retta che li interpola passa per l'origine: la costante vale zero.

> [!warning] Errore tipico
> Leggere la pendenza del passo (1) o del passo (2) come effetto di `classe`: sono relazioni fra `reddito` e un'altra variabile. Un altro errore è stimare `punteggio` su `classe` senza controllare per `reddito`: la pendenza grezza è molto più negativa (figura a sinistra) perché assorbe l'effetto del reddito. Il passo (3) usa $n-2$ gradi di libertà anziché $n-3$, quindi la sua $t$ è appena più grande di quella della regressione completa: la decisione non cambia.

> [!success] Risposta
> **(a)** $\hat\beta_1={{e03_09.beta|m}}$: a parità di reddito, un'unità in più di `classe` fa variare il punteggio di questo valore. **(b)** Lo zero cade nell'intervallo di confidenza al 95\%: non si rifiuta $H_0$, `classe` non è significativa al 5\%. **(c)** $\text{VIF}={{e03_09.vif|m}}$, inferiore a $10$. **(d)** I residui hanno media zero, quindi la retta fra i residui passa per l'origine.

![A sinistra la nuvola grezza di `punteggio` contro `classe`, con la pendenza della regressione semplice; a destra i residui del passo (3), con pendenza $\hat\beta_1={{e03_09.beta|m}}$.]({{e03_09.fig.residui}}){width=85%}

{{testo:e03_10}}

> [!tip] Richiamo
> Con $x$ e $x^2$ nel modello l'effetto marginale è $\Delta\log(y)\approx(\beta_1+2\beta_2 x)\,\Delta x$, in percentuale $100\,(\beta_1+2\beta_2 x)$; è decrescente se $\beta_2<0$ e si annulla in $x^*=-\beta_1/(2\beta_2)$. La non linearità si verifica con $H_0:\beta_2=0$. L'errore standard dell'effetto in $x_0$ è quello di una combinazione lineare: $\text{Var}(\hat\beta_1+2x_0\hat\beta_2)=\text{Var}(\hat\beta_1)+4x_0^2\,\text{Var}(\hat\beta_2)+4x_0\,\text{Cov}(\hat\beta_1,\hat\beta_2)$. Se $x$ è misurata in unità da $u$ dollari, $x^*$ va moltiplicato per $u$ per averlo in dollari.

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) riguardano $\beta_2$; la (c) cerca lo zero dell'effetto marginale e lo converte in dollari; la (d) e la (e) valutano l'effetto in $x_0$ e ne testano la significatività con la covarianza.
>
> **(a)** $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. Il rapporto $t$ vale ${{e03_10.t2|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$ e la relazione non è lineare.
>
> **(b)** $\hat\beta_2={{e03_10.b2|m}}$ è negativo e significativo: l'effetto marginale $\beta_1+2\beta_2\,\text{red}$ decresce al crescere di `red`.
>
> **(c)** $\text{red}^*=-\hat\beta_1/(2\hat\beta_2)=-{{e03_10.b1|m}}\,/\,\bigl(2\times({{e03_10.b2|m}})\bigr)={{e03_10.punto_unita|m}}$. Un'unità di `red` vale ${{e03_10.unita|m}}$ dollari, quindi ${{e03_10.punto_unita|m}}\times{{e03_10.unita|m}}={{e03_10.punto|m}}$ dollari.
>
> **(d)** $100\,(\hat\beta_1+2\hat\beta_2\,x_0)=100\times\bigl({{e03_10.b1|m}}+2\times({{e03_10.b2|m}})\times{{e03_10.x0|m}}\bigr)={{e03_10.eff|m}}\%$.
>
> **(e)** $\widehat{\text{se}}=100\sqrt{\widehat{\text{se}}(\hat\beta_1)^2+4x_0^2\,\widehat{\text{se}}(\hat\beta_2)^2+4x_0\,\widehat{\text{Cov}}}=100\sqrt{{{e03_10.s1|m}}^2+4\times{{e03_10.x0|m}}^2\times{{e03_10.s2|m}}^2+4\times{{e03_10.x0|m}}\times({{e03_10.cov|m}})}={{e03_10.se_eff|m}}$. Il rapporto $t$ è ${{e03_10.eff|m}}/{{e03_10.se_eff|m}}={{e03_10.t_eff|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Calcolare l'errore standard dell'effetto marginale senza il termine di covarianza: si otterrebbe ${{e03_10.se_ingenuo|m}}$ invece di ${{e03_10.se_eff|m}}$ e non si rifiuterebbe l'ipotesi. $\hat\beta_1$ e $\hat\beta_2$ sono fortemente correlati, perché `red` e `sq_red` si muovono insieme, e la covarianza (negativa) riduce la varianza della combinazione. Un altro errore è dimenticare l'unità di misura: ${{e03_10.punto_unita|m}}$ sono decine di migliaia di dollari, non dollari.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\beta_2=0$: la relazione fra reddito e spesa non è lineare. **(b)** Sì: $\hat\beta_2$ è negativo e significativo, l'effetto marginale è decrescente. **(c)** L'effetto marginale si annulla per un reddito di circa ${{e03_10.punto|m}}$ dollari. **(d)** In $\text{red}={{e03_10.x0|m}}$ l'effetto marginale è del ${{e03_10.eff|m}}\%$ per ogni (piccolo) aumento di una decina di migliaia di dollari; per un aumento discreto di un'intera unità l'aumento è minore, perché $\hat\beta_2$ è negativo e l'effetto marginale decresce. **(e)** Con errore standard ${{e03_10.se_eff|m}}$ (che include la covarianza) il rapporto $t$ è ${{e03_10.t_eff|m}}$: si rifiuta $H_0$, l'effetto in $x_0$ è significativamente diverso da zero anche se già prossimo al punto di svolta.

![Effetto marginale del reddito con la banda al 95\% calcolata con la covarianza: positivo e significativo in $x_0={{e03_10.x0|m}}$ (punto verde), si annulla in ${{e03_10.punto_unita|m}}$ (linea tratteggiata verticale), dove la banda comprende lo zero.]({{e03_10.fig.effetto}}){width=85%}

{{testo:e03_11}}

> [!tip] Richiamo
> Con dipendente e regressore in logaritmo $\Delta y/y\approx\beta\,\Delta x/x$: $\beta$ è un'elasticità e una variazione di $x$ del $m$ per cento fa variare $y$ di $\beta\,m$ per cento. Con un regressore in livello $\Delta y/y\approx\beta\,\Delta x$, in percentuale $100\,\beta\,\Delta x$. Per confrontare due effetti li si porta entrambi in variazione percentuale di $y$. Un'affermazione «$x$ aumenta del $m$ per cento e $y$ del $p$ per cento» equivale a un'elasticità $p/m$, che si confronta con l'intervallo di confidenza $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** `mq` è in logaritmo (elasticità), `km` è in livello (semi-elasticità): le due vanno portate nella stessa unità, la variazione percentuale dell'affitto.
>
> **(a)** $\Delta\%\,\text{affitto}\approx\hat\beta_1\times\Delta\%\,\text{mq}={{e03_11.b1|m}}\times{{e03_11.ds|m}}={{e03_11.size|m}}\%$.
>
> **(b)** $\Delta\%\,\text{affitto}\approx100\times\hat\beta_2\times\Delta\text{km}=100\times({{e03_11.b2|m}})\times{{e03_11.dkm|m}}={{e03_11.km|m}}\%$.
>
> **(c)** Si cerca $s$ con $\hat\beta_1\,s+({{e03_11.km|m}})=0$, cioè $s=-({{e03_11.km|m}})/{{e03_11.b1|m}}={{e03_11.compensa|m}}\%$.
>
> **(d)** Un aumento della superficie del ${{e03_11.ds|m}}\%$ che fa salire l'affitto del ${{e03_11.riv|m}}\%$ equivale a un'elasticità ${{e03_11.riv|m}}/{{e03_11.ds|m}}={{e03_11.el|m}}$. L'intervallo di confidenza al 95\% per $\beta_1$ è $[{{e03_11.ic_lo|m}};\,{{e03_11.ic_hi|m}}]$ e contiene ${{e03_11.el|m}}$. Lo stesso dice $t=({{e03_11.b1|m}}-{{e03_11.el|m}})/\widehat{\text{se}}(\hat\beta_1)={{e03_11.t_riv|m}}$, in valore assoluto minore di $1{,}96$.

> [!warning] Errore tipico
> Applicare $100\,\hat\beta$ anche a `l_mq`: la superficie è in logaritmo e $\hat\beta_1$ è già un'elasticità, mentre la regola $100\,\hat\beta\,\Delta x$ vale per `km`, che è in livello. Un altro errore è confrontare «${{e03_11.ds|m}}\%$ di superficie» con «${{e03_11.dkm|m}}$ chilometri» senza portarli entrambi in variazione percentuale dell'affitto.

> [!success] Risposta
> **(a)** Con la superficie $+{{e03_11.ds|m}}\%$ l'affitto aumenta di circa ${{e03_11.size|m}}\%$. **(b)** Con ${{e03_11.dkm|m}}$ chilometri in più l'affitto varia di circa ${{e03_11.km|m}}\%$. **(c)** Per compensare la perdita serve una superficie maggiore di circa il ${{e03_11.compensa|m}}\%$. **(d)** Sì: l'elasticità implicita nell'affermazione, ${{e03_11.el|m}}$, cade nell'intervallo di confidenza al 95\% per $\beta_1$, quindi l'affermazione è compatibile con i dati.

![Variazione percentuale dell'affitto per un aumento della superficie (retta blu) contro la perdita dovuta ai ${{e03_11.dkm|m}}$ chilometri in più (linea rossa): le due si pareggiano in $+{{e03_11.compensa|m}}\%$ di superficie.]({{e03_11.fig.pareggio}}){width=85%}

{{testo:e03_12}}

> [!tip] Richiamo
> Per lo stimatore di $\beta_j$ vale $\widehat{\text{Var}}(\hat\beta_j)=\dfrac{\hat\sigma^2}{\sum_i(x_{ij}-\bar x_j)^2}\cdot\dfrac{1}{1-R_j^2}$ e il secondo fattore è il $\text{VIF}_j$: rispetto a regressori indipendenti l'errore standard cresce di $\sqrt{\text{VIF}_j}$. Con un VIF maggiore di $10$ si parla di quasi-collinearità, che gonfia gli errori standard ma non distorce le stime. Omettere invece un regressore rilevante e correlato con uno incluso distorce: $\tilde\beta_1=\hat\beta_1+\hat\beta_3\,\hat\delta_1$.

> [!example] Svolgimento
> **Impostazione.** Si leggono i VIF, li si confronta con il cambio degli errori standard fra i due modelli e si controlla che cosa succede alla stima quando si toglie `anz`.
>
> **(a)** I VIF di `esper` (${{e03_12.vif|m}}$) e di `anz` (${{e03_12.vif_anz|m}}$) superano $10$, quello di `istr` è ${{e03_12.vif_istr|m}}$: c'è quasi-collinearità fra `esper` e `anz`, com'è naturale perché più si lavora e più cresce l'anzianità.
>
> **(b)** $\sqrt{\text{VIF}}=\sqrt{{{e03_12.vif|m}}}={{e03_12.fattore|m}}$.
>
> **(c)** $\widehat{\text{se}}_1/\widehat{\text{se}}_2={{e03_12.se1|m}}/{{e03_12.se2|m}}={{e03_12.rapporto|m}}$, vicino a $\sqrt{\text{VIF}}$: nel Modello 2 `esper` ha solo `istr` come altro regressore, e con esso è quasi incorrelata.
>
> **(d)** Nel Modello 1 $t={{e03_12.t1|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0:\beta_2=0$.
>
> **(e)** Nel Modello 2 $t={{e03_12.t2|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_2=0$.
>
> **(f)** $100\times({{e03_12.b2|m}}-{{e03_12.b1|m}})={{e03_12.salto|m}}$ punti percentuali.
>
> **(g)** No. I dati non separano i due effetti: il salto della stima da ${{e03_12.b1|m}}$ a ${{e03_12.b2|m}}$ è $\hat\beta_3\,\hat\delta$, con $\hat\delta$ il coefficiente di `esper` nella regressione ausiliaria di `anz`, e ha la stessa imprecisione di $\hat\beta_3$, che non è significativo. La rilevanza di `anz` va motivata con la teoria o con un test $F$ congiunto su $H_0:\beta_2=\beta_3=0$; se `anz` è rilevante, eliminarla introduce una distorsione da variabile omessa.

> [!warning] Errore tipico
> Togliere `anz` perché fa risultare `esper` non significativa. Nel Modello 2 `esper` risulta significativa perché l'errore standard è più piccolo, ma i dati non separano i due effetti: se `anz` è rilevante, la stima di `esper` assorbe parte del suo effetto, sale e diventa distorta; la rilevanza di `anz` va motivata con la teoria o con un test $F$ congiunto su $H_0:\beta_2=\beta_3=0$. La quasi-collinearità non si cura eliminando un regressore che può essere rilevante: si accetta l'errore standard più grande, si raccolgono più dati o si lavora su una combinazione delle due variabili.

> [!success] Risposta
> **(a)** Sì: i VIF di `esper` e `anz` sono maggiori di $10$. **(b)** L'errore standard di `esper` è gonfiato di circa ${{e03_12.fattore|m}}$ volte. **(c)** Il Modello 1 ha un errore standard circa ${{e03_12.rapporto|m}}$ volte più grande del Modello 2, in linea con $\sqrt{\text{VIF}}$. **(d)** Non si rifiuta $H_0$ nel Modello 1. **(e)** Si rifiuta $H_0$ nel Modello 2. **(f)** La stima sale di ${{e03_12.salto|m}}$ punti percentuali. **(g)** No: i dati non separano i due effetti, e il salto della stima ha la stessa imprecisione di $\hat\beta_3$, che non è significativo. La rilevanza di `anz` va motivata con la teoria o con un test $F$ congiunto su $H_0:\beta_2=\beta_3=0$; se `anz` è rilevante, togliere `anz` introduce una distorsione da variabile omessa.

![A sinistra `esper` contro `anz`: i punti stanno quasi su una retta. A destra il coefficiente di `esper` con intervallo al 95\%: largo e con lo zero dentro nel Modello 1, stretto nel Modello 2 dove può assorbire l'effetto di `anz`.]({{e03_12.fig.collinearita}}){width=85%}

{{testo:e03_13}}

> [!tip] Richiamo
> Se il modello completo ha $x_1$ e $x_2$ e si omette $x_2$, la stima di $\beta_1$ nel modello ristretto è $\tilde\beta_1=\hat\beta_1+\hat\beta_2\,\hat\delta_1$, dove $\hat\delta_1$ è il coefficiente di $x_1$ nella regressione di $x_2$ sui regressori inclusi. La distorsione c'è se $x_2$ conta ($\beta_2\neq 0$) **e** è correlata con $x_1$ ($\delta_1\neq 0$). Nel campione la formula è un'identità esatta.

> [!example] Svolgimento
> **Impostazione.** Si confrontano i due modelli e si usa la regressione ausiliaria per capire da dove viene la differenza.
>
> **(a)** $100\times(\tilde\beta_1-\hat\beta_1)=100\times({{e03_13.b1_ristretto|m}}-{{e03_13.b1_completo|m}})={{e03_13.a|m}}$ punti percentuali.
>
> **(b)** Servono due condizioni. L'abilità conta nel Modello 2: $t={{e03_13.t_abil|m}}$, in valore assoluto maggiore di $1{,}96$. E l'abilità è correlata con l'istruzione: nella regressione ausiliaria $t={{e03_13.t_delta|m}}$ per $\hat\delta_1$. Entrambe sono soddisfatte.
>
> **(c)** $100\,\hat\beta_3\,\hat\delta_1=100\times{{e03_13.b_abil|m}}\times{{e03_13.delta|m}}={{e03_13.c|m}}$ punti percentuali: coincide con la risposta (a).
>
> **(d)** La differenza in (a) è positiva: $\tilde\beta_1>\hat\beta_1$. Con $\hat\beta_3>0$ e $\hat\delta_1>0$ l'omissione dell'abilità gonfia il rendimento dell'istruzione.

> [!warning] Errore tipico
> Concludere per la distorsione solo perché la stima cambia di molto, senza controllare che la variabile omessa sia rilevante e correlata con l'incluso. Oppure presentare il Modello 2 come privo di distorsione: potrebbero mancare altre variabili.

> [!success] Risposta
> **(a)** La stima del rendimento dell'istruzione scende di ${{e03_13.a|m}}$ punti percentuali passando dal Modello 1 al Modello 2. **(b)** Sì: il Modello 1 omette `abil`, che è significativa e correlata con `istr`. **(c)** $100\,\hat\beta_3\,\hat\delta_1={{e03_13.c|m}}$, uguale alla differenza in (a). **(d)** Sì: il segno è positivo, omettere l'abilità gonfia il rendimento dell'istruzione.

![Coefficiente dell'istruzione, con intervallo al 95\%: senza abilità (Modello 1) e con abilità (Modello 2).]({{e03_13.fig.confronto}}){width=85%}
