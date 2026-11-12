{{testo:a02_01}}

## Soluzione della Domanda 1 — La categoria di riferimento e le dummy di ruolo

> [!tip] Richiamo
> Con la costante nel modello, tre dummy che sommano a 1 non possono entrare insieme: la loro somma coincide con la colonna della costante e darebbe collinearità perfetta (la «trappola delle dummy»). Il programma ne omette una, ed è la categoria di riferimento. Ciascuna dummy rimasta ha un coefficiente $\delta$ che è il differenziale di $\log(\text{salario})$ rispetto alla categoria omessa, a parità delle altre variabili; la costante $\beta_0$ è il livello della categoria omessa. Con la dipendente in logaritmo il differenziale in percentuale è $100\,\delta$. Se si elimina la costante e si tengono tutte le dummy, ogni coefficiente diventa il livello della sua categoria: $\beta_0+\delta_j$ per le categorie incluse, $\beta_0$ per quella omessa.

> [!example] Svolgimento
> **Impostazione.** La (a) si legge dall'output; la (b) interpreta una dummy come differenziale in percentuale; la (c) riscrive lo stesso modello senza costante.
>
> **(a)** Nell'output compaiono `dif` e `att` ma non `cen`: la dummy omessa è quella dei centrocampisti, che sono la categoria di riferimento. Il codice del ruolo è ${{a02_01.base|m}}$.
>
> **(b)** Il coefficiente di `att` è $\hat\delta_3={{a02_01.b_att|m}}$: $100\times{{a02_01.b_att|m}}={{a02_01.pct_att|m}}\%$. Un attaccante guadagna in media circa il ${{a02_01.pct_att|m}}\%$ in più di un centrocampista con le stesse altre caratteristiche.
>
> **(c)** Senza la costante il coefficiente di `att` è il livello degli attaccanti: $\hat\beta_0+\hat\delta_3={{a02_01.b_const|m}}+{{a02_01.b_att|m}}={{a02_01.liv_att|m}}$.

> [!warning] Errore tipico
> Dire che senza la costante il coefficiente di `att` resta ${{a02_01.b_att|m}}$: senza costante non c'è più una categoria di riferimento e ogni coefficiente è un livello, non un differenziale. Un altro errore è leggere il coefficiente di `dif`, ${{a02_01.b_dif|m}}$, come lo stipendio dei difensori invece che come il loro scarto rispetto ai centrocampisti.

> [!success] Risposta
> **(a)** La categoria di riferimento è il centrocampista, codice ${{a02_01.base|m}}$: la sua dummy è stata omessa perché $\text{dif}+\text{cen}+\text{att}=1$ coincide con la costante. **(b)** Un attaccante guadagna in media circa il ${{a02_01.pct_att|m}}\%$ in più di un centrocampista. **(c)** Senza la costante il coefficiente di `att` varrebbe ${{a02_01.liv_att|m}}$, cioè $\hat\beta_0+\hat\delta_3$.

![A sinistra, con la costante, i differenziali di `dif` e `att` rispetto al centrocampista, che sta a zero; a destra, senza la costante, gli stessi tre ruoli come livelli: il livello degli attaccanti è ${{a02_01.liv_att|m}}$.]({{a02_01.fig.ruoli}}){width=85%}

## Soluzione della Domanda 2 — Il ruolo ha rilevanza? Il test $F$

> [!tip] Richiamo
> Per stabilire se un fattore qualitativo con più categorie conta si verificano insieme tutti i suoi differenziali: il ruolo non ha rilevanza se i tre ruoli hanno lo stesso livello atteso, cioè $H_0:\delta_1=\delta_2=\delta_3$ contro $H_1$: almeno una uguaglianza non vale. Le restrizioni indipendenti sono $q$, una in meno del numero di categorie. La statistica è $F=\dfrac{(\text{SSR}_r-\text{SSR}_u)/q}{\text{SSR}_u/(n-k)}$, dove $\text{SSR}_r$ è la somma dei quadrati dei residui del modello ristretto (senza le dummy di ruolo), $\text{SSR}_u$ quella del modello non ristretto e $k$ il numero dei suoi parametri. Si rifiuta $H_0$ se $F$ supera il valore critico di $F_{q,\,n-k}$.

> [!example] Svolgimento
> **Impostazione.** Si scrive il sistema di ipotesi, se ne contano le restrizioni e si calcola $F$ con le due somme dei quadrati dei residui.
>
> **Sistema.** $H_0:\delta_1=\delta_2=\delta_3$ contro $H_1$: almeno una uguaglianza non vale. Con il centrocampista come riferimento, equivale ad annullare insieme i coefficienti di `dif` e `att`.
>
> **(a)** Le restrizioni indipendenti sono $\delta_1-\delta_2=0$ e $\delta_2-\delta_3=0$: $q={{a02_01.q|m}}$, una in meno dei tre ruoli.
>
> **(b)** Il modello non ristretto stima $k=7$ parametri (la costante e sei regressori): $n-k={{a02_01.n|m}}-7={{a02_01.gl|m}}$ gradi di libertà.
>
> **(c)** $F=\dfrac{({{a02_01.ssr_r|m}}-{{a02_01.ssr_u|m}})/{{a02_01.q|m}}}{ {{a02_01.ssr_u|m}}/{{a02_01.gl|m}} }={{a02_01.F|m}}$. Siccome ${{a02_01.F|m}}>{{a02_01.fcrit|m}}$, si rifiuta $H_0$.

> [!warning] Errore tipico
> Contare tre restrizioni perché le dummy del testo sono tre: sono due le uguaglianze indipendenti, e il numeratore ha $q={{a02_01.q|m}}$ gradi di libertà. Un altro errore è usare nel denominatore i gradi di libertà del modello ristretto o fare due test $t$ separati sui coefficienti di `dif` e `att`: il test è congiunto.

> [!success] Risposta
> Il sistema è $H_0:\delta_1=\delta_2=\delta_3$ contro $H_1$: almeno una uguaglianza non vale. **(a)** Ci sono ${{a02_01.q|m}}$ restrizioni. **(b)** Il denominatore ha ${{a02_01.gl|m}}$ gradi di libertà. **(c)** $F={{a02_01.F|m}}$ supera il valore critico ${{a02_01.fcrit|m}}$: si rifiuta $H_0$ e il ruolo ha rilevanza nello spiegare il salario medio.

![Statistica $F={{a02_01.F|m}}$ e regione di rifiuto al 5\% (oltre ${{a02_01.fcrit|m}}$) della distribuzione $F$ con ${{a02_01.q|m}}$ e ${{a02_01.gl|m}}$ gradi di libertà.]({{a02_01.fig.f}}){width=85%}

## Soluzione della Domanda 3 — Il termine quadratico e la non linearità

> [!tip] Richiamo
> Con `esper` ed `esper2` nel modello l'effetto marginale dell'esperienza è $\beta_3+2\beta_4\,\text{esper}$, perché $\Delta(\text{esper}^2)\approx 2\,\text{esper}\,\Delta\text{esper}$: dipende dal livello di esperienza. La relazione è non lineare se $\beta_4\neq 0$, e si verifica con $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$, rifiutando se $|t|>1{,}96$. Se $\beta_4<0$ l'effetto marginale diminuisce al crescere dell'esperienza.

> [!example] Svolgimento
> **Impostazione.** Un test $t$ bilaterale su $\beta_4$ decide la linearità; il segno di $\hat\beta_4$ dice se l'effetto marginale cresce o diminuisce.
>
> **(a)** $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$. Il rapporto $t$ vale ${{a02_01.t_q|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** $\hat\beta_4={{a02_01.b_esper2|m}}<0$ ed è significativo: l'effetto marginale stimato è $\hat\beta_3+2\hat\beta_4\,\text{esper}={{a02_01.b_esper|m}}+2\times({{a02_01.b_esper2|m}})\,\text{esper}$, una retta decrescente in `esper`. Sì, diminuisce.

> [!warning] Errore tipico
> Leggere $\hat\beta_3={{a02_01.b_esper|m}}$ da solo come effetto dell'esperienza: con il termine al quadrato l'effetto cambia con il livello di esperienza. Un altro errore è confondere «decrescente» con «negativo»: l'effetto marginale è positivo per i giovani e diminuisce, fino a diventare negativo oltre un certo livello di esperienza.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\beta_4=0$: il termine al quadrato è significativo al 5\% e la relazione non è lineare. **(b)** Sì: $\hat\beta_4$ è negativo, quindi ogni anno di esperienza in più aggiunge al $\log(\text{salario})$ meno dell'anno precedente.

![Effetto marginale stimato dell'esperienza, $\hat\beta_3+2\hat\beta_4\,\text{esper}$: decresce al crescere di `esper`.]({{a02_01.fig.effetto}}){width=85%}

## Soluzione della Domanda 4 — Breusch-Pagan contro White

> [!tip] Richiamo
> Breusch-Pagan e White hanno la stessa ipotesi nulla, l'omoschedasticità, ma alternative diverse. Breusch-Pagan regredisce $\hat\epsilon^2$ sui regressori e cerca una dipendenza lineare; White aggiunge quadrati e prodotti dei regressori continui e cerca anche dipendenze non lineari. In entrambi $LM=nR^2\sim\chi^2$ con tanti gradi di libertà quanti sono i regressori ausiliari, e si rifiuta $H_0$ al 5\% se il p-value è minore di $0{,}05$. Un test che non rifiuta non dimostra l'omoschedasticità. Se almeno uno rifiuta, la varianza condizionale dipende dai regressori e si usano errori standard robusti.

> [!example] Svolgimento
> **Impostazione.** Si confronta ogni p-value con $0{,}05$, poi si decide che cosa farne.
>
> **(a)** Breusch-Pagan, con ${{a02_01.gl_bp|m}}$ gradi di libertà: p-value {{a02_01.p_bp}}, maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(b)** White, con ${{a02_01.gl_w|m}}$ gradi di libertà: p-value {{a02_01.p_w}}, minore di $0{,}05$: si rifiuta $H_0$.
>
> **(c)** Sì: White rileva una dipendenza significativa di $\hat\epsilon^2$ dai regressori, per cui l'ipotesi di omoschedasticità non regge e conviene usare errori standard robusti.

> [!warning] Errore tipico
> Concludere dal non rifiuto di Breusch-Pagan che gli errori siano omoschedastici. Quel test cerca soltanto una dipendenza lineare di $\hat\epsilon^2$ dai regressori: una varianza più alta agli estremi delle presenze, come quella del grafico, ha una retta di regressione piatta e gli sfugge, mentre White, che include i quadrati, la rileva.

> [!success] Risposta
> **(a)** Non si rifiuta l'omoschedasticità con Breusch-Pagan (p-value {{a02_01.p_bp}}). **(b)** Si rifiuta con White (p-value {{a02_01.p_w}}). **(c)** Sì: i due test non si contraddicono, hanno alternative diverse; poiché White rifiuta, sembra ragionevole l'ipotesi di eteroschedasticità e conviene usare errori standard robusti.

![Residui al quadrato contro le presenze: la media per classe ha forma di U, la retta di Breusch-Pagan è piatta, la parabola di White segue i dati.]({{a02_01.fig.varianza}}){width=85%}

## Soluzione della Domanda 5 — Gol e salario: effetti in percentuale

> [!tip] Richiamo
> Con la dipendente in logaritmo, $\Delta\log(y)=\beta\,\Delta x$ e, poiché $\Delta\log(y)\approx\Delta y/y$, la variazione percentuale attesa è $100\,\beta\,\Delta x$, a parità delle altre variabili. Per ottenere la variazione del regressore necessaria a un obiettivo percentuale $m$ si inverte la formula: $\Delta x=m/(100\,\beta)$.

> [!example] Svolgimento
> **Impostazione.** Il modello è log-livello rispetto a `gol`: $\hat\beta_1$ è una variazione relativa per gol, da moltiplicare per $100$ e per i gol aggiunti.
>
> **(a)** $\Delta\%\,\text{salario}\approx100\times\hat\beta_1\times\Delta\text{gol}=100\times{{a02_01.b_gol|m}}\times{{a02_01.dgol|m}}={{a02_01.pct_gol|m}}\%$.
>
> **(b)** Da $100\,\hat\beta_1\,\Delta\text{gol}={{a02_01.obiettivo|m}}$ si ha $\Delta\text{gol}=\dfrac{ {{a02_01.obiettivo|m}} }{100\times{{a02_01.b_gol|m}} }={{a02_01.gol_servono|m}}$.

> [!warning] Errore tipico
> Leggere $\hat\beta_1={{a02_01.b_gol|m}}$ come una variazione percentuale (senza moltiplicare per $100$) o dimenticare di moltiplicare per i gol aggiunti. Un altro errore è calcolare $\Delta\text{gol}$ come ${{a02_01.obiettivo|m}}\times\hat\beta_1$ invece di dividere: il coefficiente è un effetto per gol, e per raggiungere un obiettivo si divide l'obiettivo per l'effetto.

> [!success] Risposta
> **(a)** ${{a02_01.dgol|m}}$ gol in più fanno aumentare il salario atteso di circa il ${{a02_01.pct_gol|m}}\%$. **(b)** Per un aumento del ${{a02_01.obiettivo|m}}\%$ servono circa ${{a02_01.gol_servono|m}}$ gol in più.

![Variazione percentuale attesa del salario al crescere dei gol: ${{a02_01.dgol|m}}$ gol valgono ${{a02_01.pct_gol|m}}\%$ e l'obiettivo del ${{a02_01.obiettivo|m}}\%$ si raggiunge con ${{a02_01.gol_servono|m}}$ gol.]({{a02_01.fig.gol}}){width=85%}

## Soluzione della Domanda 6 — Le presenze: un test unilaterale su una soglia

> [!tip] Richiamo
> L'affermazione «una presenza in più fa crescere il salario di meno del $c\%$» è, con la dipendente in logaritmo, $\beta<c/100$: è l'ipotesi alternativa, e il sistema è $H_0:\beta\ge c/100$ contro $H_1:\beta<c/100$, unilaterale a sinistra. Con una soglia non nulla la statistica è $t=(\hat\beta-c/100)/\widehat{\text{se}}(\hat\beta)$ e al 5\% si rifiuta $H_0$ se $t<-1{,}64$. Rifiutare $H_0$ significa che i dati sostengono l'affermazione.

> [!example] Svolgimento
> **Impostazione.** Si traduce la percentuale in una soglia sul coefficiente, poi si fa un test a una coda a sinistra.
>
> **(a)** $c={{a02_01.riv|m}}/100={{a02_01.soglia|m}}$.
>
> **(b)** $t=\dfrac{\hat\beta_2-c}{\widehat{\text{se}}(\hat\beta_2)}=\dfrac{ {{a02_01.b_pres|m}}-{{a02_01.soglia|m}} }{ {{a02_01.se_pres|m}} }={{a02_01.t_riv|m}}$.
>
> **(c)** ${{a02_01.t_riv|m}}<-1{,}64$: si rifiuta $H_0:\beta_2\ge c$ a favore di $H_1:\beta_2<c$.

> [!warning] Errore tipico
> Guardare il rapporto $t$ della tabella, ${{a02_01.t_pres|m}}$, che verifica $H_0:\beta_2=0$ e risponde a un'altra domanda. Un altro errore è cercare la regione di rifiuto dalla parte sbagliata, $t>1{,}64$, o confrontare $t$ con $1{,}96$: con l'alternativa $\beta_2<c$ si rifiuta solo per valori molto negativi di $t$.

> [!success] Risposta
> **(a)** $c={{a02_01.soglia|m}}$. **(b)** $t={{a02_01.t_riv|m}}$. **(c)** Si rifiuta $H_0$ al 5\%, perché $t<-1{,}64$: la stima ${{a02_01.b_pres|m}}$ è significativamente sotto la soglia ${{a02_01.soglia|m}}$, quindi i dati sostengono l'affermazione che una presenza in più valga meno del ${{a02_01.riv|m}}\%$.

![Regione di rifiuto a sinistra al 5\% (sotto $-1{,}64$) e rapporto $t={{a02_01.t_riv|m}}$ osservato: cade nella regione di rifiuto.]({{a02_01.fig.soglia}}){width=85%}

{{testo:a02_02}}

## Soluzione della Domanda 7 — Le serie hanno una radice unitaria?

> [!tip] Richiamo
> Il test ADF ha $H_0$: radice unitaria (la serie è integrata, non stazionaria) contro $H_1$: stazionarietà. È a una coda: si rifiuta se la statistica è minore del valore critico, qui ${{a02_02.cv|m}}$. Una serie è integrata di ordine $d$ se occorre differenziarla $d$ volte per renderla stazionaria: si testa il livello e, se non si rifiuta, si testa la differenza prima.

> [!example] Svolgimento
> **Impostazione.** Si confronta ogni statistica con ${{a02_02.cv|m}}$, a sinistra del quale si rifiuta.
>
> **(a)** Per $\log(\text{elet})$ in livello la statistica è ${{a02_02.t_y|m}}>{{a02_02.cv|m}}$: non si rifiuta $H_0$, la serie ha una radice unitaria.
>
> **(b)** Per $\log(\text{pil})$ in livello la statistica è ${{a02_02.t_x|m}}>{{a02_02.cv|m}}$: non si rifiuta $H_0$, anche questa serie ha una radice unitaria.
>
> **(c)** Sulla differenza prima di $\log(\text{elet})$ la statistica è ${{a02_02.t_dy|m}}<{{a02_02.cv|m}}$: si rifiuta, la differenza è stazionaria. Una sola differenziazione basta, quindi l'ordine di integrazione è ${{a02_02.ord_y|m}}$; lo stesso vale per $\log(\text{pil})$, la cui differenza ha statistica ${{a02_02.t_dx|m}}$.

> [!warning] Errore tipico
> Rifiutare quando la statistica è maggiore del valore critico, come in un test $t$ a coda destra: nel test ADF si rifiuta per valori molto negativi. Un altro errore è fermarsi al livello e dire soltanto «non stazionaria»: l'ordine di integrazione richiede anche il test sulla differenza prima.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0$: $\log(\text{elet})$ ha una radice unitaria. **(b)** Non si rifiuta $H_0$ nemmeno per $\log(\text{pil})$. **(c)** La differenza prima è stazionaria (si rifiuta la radice unitaria), quindi $\log(\text{elet})$ è integrata di ordine ${{a02_02.ord_y|m}}$, come $\log(\text{pil})$.

![Le statistiche ADF dei livelli stanno a destra del valore critico ${{a02_02.cv|m}}$ (non si rifiuta), quelle delle differenze a sinistra (si rifiuta): entrambe le serie sono $I(1)$.]({{a02_02.fig.adf}}){width=85%}

## Soluzione della Domanda 8 — Engle-Granger e regressione in livelli

> [!tip] Richiamo
> Una regressione fra livelli è una relazione di lungo periodo ben definita solo se le serie sono integrate e cointegrate, cioè se i residui sono stazionari. Il test di Engle-Granger è un test di radice unitaria sui residui $\hat u_t$: $H_0$ è la radice unitaria nei residui, cioè l'assenza di cointegrazione, e si rifiuta se il p-value è minore di $0{,}05$. Ha senso solo per serie non stazionarie: se le serie fossero stazionarie anche i residui lo sarebbero e il test dovrebbe rifiutare. Se non si rifiuta, la regressione in livelli è spuria: $R^2$ alto e rapporti $t$ enormi non hanno il significato usuale, e la relazione va studiata in differenze.

> [!example] Svolgimento
> **Impostazione.** Si legge il p-value, lo si confronta con gli ordini di integrazione della Domanda 7 e si decide che cosa vale la regressione in livelli.
>
> **(a)** Il p-value ${{a02_02.p_eg|m}}$ è maggiore di $0{,}05$: non si rifiuta $H_0$: non c'è evidenza di cointegrazione e la regressione in livelli va trattata come spuria.
>
> **(b)** Per la Domanda 7 le due serie sono $I(1)$: il test è applicabile e un p-value alto è plausibile, perché due serie integrate non cointegrate hanno residui non stazionari. Sì, l'esito è credibile e coerente.
>
> **(c)** La regressione ha $\hat\beta={{a02_02.b_stat|m}}$, $t={{a02_02.t_stat|m}}$ e $R^2={{a02_02.r2|m}}$, ma non si rifiuta la radice unitaria nei residui: la regressione in livelli va trattata come spuria, e i coefficienti non si leggono come una relazione di lungo periodo. No, non è ben definita.

> [!warning] Errore tipico
> Fidarsi di $R^2={{a02_02.r2|m}}$ e di $t={{a02_02.t_stat|m}}$ e concludere che $\log(\text{pil})$ spieghi $\log(\text{elet})$ nel lungo periodo: con serie integrate non cointegrate sono valori tipici di una regressione spuria. Un altro errore è leggere un p-value alto come prova di cointegrazione: $H_0$ è l'assenza di cointegrazione, e non rifiutarla significa che non c'è evidenza di cointegrazione.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0$ (p-value ${{a02_02.p_eg|m}}>0{,}05$): non c'è evidenza di cointegrazione e la regressione in livelli va trattata come spuria. **(b)** Sì: con due serie $I(1)$ il test è applicabile e l'esito è coerente. **(c)** No: non si rifiuta la radice unitaria nei residui, la regressione in livelli va trattata come spuria e non è ben definita come relazione di lungo periodo.

![A sinistra i residui della regressione in livelli, che vagano senza tornare a zero; a destra la loro ACF, che decade lentamente: i residui non sembrano stazionari, il p-value ${{a02_02.p_eg|m}}$ non rifiuta.]({{a02_02.fig.residui}}){width=85%}

## Soluzione della Domanda 9 — Il test QLR sulla regressione in differenze

> [!tip] Richiamo
> Il test QLR verifica che i parametri siano stabili in una data non nota: calcola la statistica $F$ di Chow (qui con due restrizioni, intercetta e pendenza) per ogni data candidata, escludendo il 15\% iniziale e finale del campione, e prende il massimo $F^*$. Sotto $H_0$ (parametri stabili in ogni data) il massimo non ha distribuzione $F$ e il suo valore critico è più alto di quello della $F$ ordinaria; qui è ${{a02_02.qcrit|m}}$ al 5\%. Si rifiuta se $F^*$ lo supera. Se si rifiuta c'è un break: la regressione sull'intero campione mescola due regimi e la sua pendenza non descrive nessuno dei due.

> [!example] Svolgimento
> **Impostazione.** Si confronta $F^*$ con il valore critico del test QLR, poi si leggono le pendenze dei due sottocampioni.
>
> **(a)** $F^*={{a02_02.F|m}}>{{a02_02.qcrit|m}}$: si rifiuta $H_0$, i parametri non sono stabili e c'è un break strutturale.
>
> **(b)** La pendenza sull'intero campione, ${{a02_02.b_intero|m}}$, è una media fra due regimi diversi, ${{a02_02.b_primo|m}}$ prima e ${{a02_02.b_secondo|m}}$ dopo il break: sì, i break sono un problema.
>
> **(c)** $\hat\beta_{\text{secondo}}-\hat\beta_{\text{primo}}={{a02_02.b_secondo|m}}-{{a02_02.b_primo|m}}={{a02_02.salto|m}}$.

> [!warning] Errore tipico
> Confrontare $F^*$ con il valore critico della $F$ ordinaria con $2$ e ${{a02_02.gl_den|m}}$ gradi di libertà, ${{a02_02.f_ord|m}}$: il massimo di molte statistiche supera quel valore anche in assenza di break, e si rifiuterebbe troppo spesso. Qui la conclusione non cambia, ma il valore critico giusto è ${{a02_02.qcrit|m}}$. Un altro errore è non rifiutare perché la pendenza dell'intero campione è molto significativa: la significatività media non esclude che il parametro cambi nel tempo.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: $F^*={{a02_02.F|m}}$ supera ${{a02_02.qcrit|m}}$. **(b)** Sì: c'è un break strutturale e la stima sull'intero campione, ${{a02_02.b_intero|m}}$, è una media di due regimi. **(c)** La stima di $\beta$ varia di ${{a02_02.salto|m}}$ dal primo al secondo sottocampione, cioè cala.

![Statistica di Chow a ogni data ammissibile: il massimo, ${{a02_02.F|m}}$, supera il valore critico del test QLR (${{a02_02.qcrit|m}}$), non solo quello della $F$ ordinaria.]({{a02_02.fig.qlr}}){width=85%}

## Soluzione della Domanda 10 — ACF e PACF: stazionarietà e scelta fra AR e MA

> [!tip] Richiamo
> ACF e PACF campionarie si leggono rispetto alla banda di significatività al 5\%, $\pm 1{,}96/\sqrt{n}$. Una serie stazionaria ha un ACF che decade e rientra nella banda. In un AR($p$) la PACF si annulla dopo il ritardo $p$ e l'ACF decade gradualmente; in un MA($q$) è l'ACF ad annullarsi di colpo dopo il ritardo $q$, mentre la PACF decade. L'ordine è il ritardo dopo il quale si annulla la funzione che si interrompe.

> [!example] Svolgimento
> **Impostazione.** Si calcola la banda e si guarda quale delle due funzioni si interrompe.
>
> La banda è $\pm 1{,}96/\sqrt{ {{a02_02.n_d|m}} }=\pm{{a02_02.banda|m}}$.
>
> **(a)** L'ACF vale ${{a02_02.acf1|m}}$, ${{a02_02.acf2|m}}$ e ${{a02_02.acf3|m}}$ ai primi tre ritardi, poi decade e resta dentro la banda: la serie è stazionaria (in accordo con il test ADF sulla differenza della Domanda 7).
>
> **(b)** La PACF esce dalla banda soltanto al ritardo 1 (${{a02_02.pacf1|m}}$) e poi vi resta (ritardo 2: ${{a02_02.pacf2|m}}$), mentre l'ACF decade gradualmente: è la configurazione di un AR, non di un MA.
>
> **(c)** La PACF si annulla dopo il ritardo ${{a02_02.ordine|m}}$: il modello proposto è un AR(${{a02_02.ordine|m}}$), $\text{Dpil}_t=c+\phi\,\text{Dpil}_{t-1}+\epsilon_t$, con $\hat\phi$ vicino a ${{a02_02.pacf1|m}}$.

> [!warning] Errore tipico
> Contare i ritardi dell'ACF fuori banda e proporre un MA($q$) con quell'ordine: un MA si riconosce da un ACF che si annulla di colpo, qui invece l'ACF decade gradualmente. Un altro errore è leggere l'ACF persistente come radice unitaria: rientra nella banda dopo pochi ritardi, quindi la serie è stazionaria.

> [!success] Risposta
> **(a)** Sì: l'ACF decade e rientra nella banda $\pm{{a02_02.banda|m}}$. **(b)** Sì: la PACF si annulla dopo il primo ritardo e l'ACF decade gradualmente, quindi serve un AR e non un MA. **(c)** L'ordine è ${{a02_02.ordine|m}}$: si propone un AR(${{a02_02.ordine|m}}$) per $\text{Dpil}$.

![ACF e PACF campionarie (punti) di $\text{Dpil}$ contro il profilo teorico di un AR(1) (barre): la PACF si annulla dopo il primo ritardo, l'ACF decade.]({{a02_02.fig.teoria}}){width=85%}
