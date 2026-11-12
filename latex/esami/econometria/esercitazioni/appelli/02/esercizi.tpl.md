<!-- ex a02_01 -->
# Esercizio 1 — Gli stipendi dei calciatori professionisti

> [!abstract] Dati
> Per $n = {{a02_01.n|m}}$ calciatori professionisti di campo (portieri esclusi) sono state osservate le seguenti variabili:
>
> - `salario`: stipendio annuo lordo (in migliaia di euro);
> - `gol`: gol segnati nell'ultima stagione;
> - `pres`: presenze nell'ultima stagione;
> - `esper`: anni di esperienza da professionista, ed `esper2` il suo quadrato;
> - `dif`, `cen`, `att`: variabili dummy che identificano in maniera univoca il ruolo del calciatore. `dif` vale 1 per i difensori, `cen` per i centrocampisti e `att` per gli attaccanti, e 0 altrimenti. Si noti che $\text{dif}+\text{cen}+\text{att}=1$ per ogni calciatore.
>
> Si consideri il modello
>
> $$\log(\text{salario})=\beta_0+\beta_1\,\text{gol}+\beta_2\,\text{pres}+\beta_3\,\text{esper}+\beta_4\,\text{esper2}+\delta_1\,\text{dif}+\delta_2\,\text{cen}+\delta_3\,\text{att}+\epsilon .$$
>
> Salvo diversa indicazione i test sono al livello di significatività del 5\%; per la normale standard i quantili sono $1{,}96$ (test bilaterale) e $1{,}64$ (test unilaterale). Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime sono riportate di seguito; il programma ha omesso automaticamente una delle variabili.

> [!abstract] Dati
> **Stime OLS.**
>
> {{a02_01.tab.ols}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** Si indichi con 1 il ruolo di difensore, con 2 quello di centrocampista e con 3 quello di attaccante. **(a)** Quale ruolo è la categoria di riferimento, cioè quale dummy è stata omessa dall'output? Si risponda con il numero del ruolo. **(b)** Di quanto è più alto, in percentuale e in media, il salario di un attaccante rispetto a quello di un calciatore del ruolo di riferimento, a parità di altre caratteristiche? **(c)** Si supponga di ristimare il modello eliminando la costante e mantenendo tutte e tre le dummy di ruolo, oltre alle altre variabili: quanto varrebbe il coefficiente stimato di `att`?

> [!abstract] Dati
> Per la Domanda 2 si è stimato anche il modello ristretto, che esclude dal modello originale le variabili di ruolo:
>
> {{a02_01.tab.rist}}

> [!question] Testo della domanda
> **Domanda 2 *(4 punti)*.** Sulla base del modello stimato, si definisca un opportuno sistema di ipotesi per decidere con un test $F$ se il ruolo del calciatore ha rilevanza nello spiegare il livello medio dei salari. **(a)** Quante restrizioni contiene l'ipotesi nulla? **(b)** Con quanti gradi di libertà al denominatore si valuta la statistica $F$ del test? **(c)** Usando le somme dei quadrati dei residui (SSR) dei due modelli, e sapendo che il valore critico al 5\% della distribuzione $F$ con i gradi di libertà appropriati è ${{a02_01.fcrit|m}}$, si decida se rifiutare o non rifiutare l'ipotesi nulla.

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Si vuole stabilire se la relazione fra esperienza e salario sia lineare. **(a)** Si decida se rifiutare o non rifiutare $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$. **(b)** L'effetto marginale dell'esperienza sul $\log(\text{salario})$ diminuisce al crescere dell'esperienza? Si risponda sì o no.

> [!abstract] Dati
> Per verificare l'omoschedasticità degli errori si sono eseguiti due test sui residui $\hat\epsilon$, entrambi con ipotesi nulla l'omoschedasticità e alternativa l'eteroschedasticità. Il test di Breusch-Pagan usa come regressori ausiliari quelli del modello (`gol`, `pres`, `esper`, `esper2`, `dif`, `att`); il test di White usa i regressori continui `gol`, `pres` ed `esper`, i loro quadrati e i loro prodotti a coppie (le dummy di ruolo non sono incluse). In entrambi i casi la statistica è $LM=nR^2$ della regressione ausiliaria di $\hat\epsilon^2$.
>
> {{a02_01.tab.bp}}
>
> {{a02_01.tab.white}}

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** Al livello del 5\%: **(a)** si decida se rifiutare o non rifiutare l'ipotesi nulla di omoschedasticità con il test di Breusch-Pagan; **(b)** si decida lo stesso con il test di White; **(c)** alla luce dei due test, conviene usare errori standard robusti all'eteroschedasticità? Si risponda sì o no.

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, il salario di un calciatore che segna ${{a02_01.dgol|m}}$ gol in più, a parità di altre caratteristiche? **(b)** Di quanti gol in più dovrebbe aumentare il numero di gol perché il salario atteso aumenti del ${{a02_01.obiettivo|m}}\%$, a parità di altre caratteristiche?

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** Un dirigente sostiene che una presenza in più faccia crescere il salario atteso di un valore inferiore a ${{a02_01.riv|m}}\%$, a parità di altre caratteristiche. Si indichi con $c$ la soglia su $\beta_2$ (il valore del coefficiente, non una percentuale) che traduce l'affermazione. Si usino gli errori standard della tabella e il quantile unilaterale $1{,}64$. **(a)** Quanto vale $c$? **(b)** Si calcoli il rapporto $t=(\hat\beta_2-c)/\widehat{\text{se}}(\hat\beta_2)$. **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2\ge c$ contro $H_1:\beta_2<c$.
<!-- /ex -->

<!-- ex a02_02 -->
# Esercizio 2 — Consumo di elettricità e PIL

> [!abstract] Dati
> Si dispone di osservazioni annuali dal ${{a02_02.anno0|m}}$ al ${{a02_02.anno1|m}}$ ($T={{a02_02.T|m}}$) sul consumo di elettricità pro capite (`elet`) e sul PIL pro capite (`pil`) di un Paese. L'analisi è condotta sui logaritmi delle due serie, rappresentati nella Figura 1. Salvo diversa indicazione i test sono al livello di significatività del 5\%.
>
> ![Figura 1 — Le serie $\log(\text{elet})$ e $\log(\text{pil})$.]({{a02_02.fig.serie}}){width=85%}

> [!abstract] Dati
> Per la Domanda 7 si è eseguito il test di Dickey-Fuller aumentato, con una costante e due ritardi della differenza, sui livelli e sulle differenze prime delle due serie. L'ipotesi nulla è la radice unitaria (serie integrata) contro la stazionarietà: si rifiuta se la statistica è minore del valore critico al 5\%, ${{a02_02.cv|m}}$.
>
> {{a02_02.tab.adf}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Per $\log(\text{elet})$ in livello, si decida se rifiutare o non rifiutare l'ipotesi nulla di radice unitaria. **(b)** Lo stesso per $\log(\text{pil})$ in livello. **(c)** Qual è l'ordine di integrazione di $\log(\text{elet})$, cioè quante volte occorre differenziare la serie per ottenerne una stazionaria?

> [!abstract] Dati
> Per la Domanda 8 la relazione fra i livelli
>
> $$\log(\text{elet}_t)=\alpha+\beta\,\log(\text{pil}_t)+u_t$$
>
> è stata stimata con OLS (nella tabella `l_pil` è $\log(\text{pil})$).
>
> {{a02_02.tab.statica}}
>
> Il test di Engle-Granger sui residui $\hat u_t$ ha ipotesi nulla l'assenza di cointegrazione e fornisce un p-value di ${{a02_02.p_eg|m}}$.

> [!question] Testo della domanda
> **Domanda 8 *(4 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi nulla del test di Engle-Granger. **(b)** Alla luce dei risultati della Domanda 7, l'esito del test è credibile, cioè coerente con gli ordini di integrazione delle due serie? Si risponda sì o no. **(c)** La regressione in livelli è ben definita, cioè i suoi coefficienti si possono leggere come una relazione di lungo periodo fra le due serie? Si risponda sì o no.

> [!abstract] Dati
> Per la Domanda 9 si considera la relazione fra le differenze, $\Delta\log(\text{elet}_t)=\alpha+\beta\,\Delta\log(\text{pil}_t)+u_t$, con $\text{Dpil}=\Delta\log(\text{pil})$. Il test QLR ne verifica la stabilità (intercetta e pendenza): la sua statistica è il massimo delle statistiche $F$ di Chow, con due restrizioni, su tutte le date comprese fra il 15\% e l'85\% del campione. Il massimo, $F^*={{a02_02.F|m}}$, si ottiene dividendo il campione nei due sottocampioni della tabella; il valore critico al 5\% del test QLR è ${{a02_02.qcrit|m}}$. L'ipotesi nulla è che i parametri siano stabili in ogni data, contro l'alternativa di un break in almeno una data.
>
> {{a02_02.tab.qlr}}

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi nulla di stabilità dei parametri: si rifiuta se $F^*$ supera il valore critico. **(b)** I break strutturali sono un problema per la regressione stimata sull'intero campione? Si risponda sì o no. **(c)** Di quanto cambia la stima di $\beta$ passando dal primo al secondo sottocampione, cioè (stima nel secondo) $-$ (stima nel primo)?

> [!abstract] Dati
> La Figura 2 riporta l'autocorrelogramma (ACF, in alto) e l'autocorrelogramma parziale (PACF, in basso) della serie $\text{Dpil}=\Delta\log(\text{pil})$, sui primi ${{a02_02.k|m}}$ ritardi. La fascia azzurra è la banda di significatività al 5\%, $\pm 1{,}96/\sqrt{ {{a02_02.n_d|m}} }$; i ritardi che ne escono sono disegnati in rosso.
>
> ![Figura 2 — ACF e PACF della serie $\text{Dpil}$.]({{a02_02.fig.correlogramma}}){width=85%}

> [!question] Testo della domanda
> **Domanda 10 *(3 punti)*.** Si descriva la serie $\text{Dpil}$ con un modello AR($p$) oppure MA($q$). **(a)** La serie sembra stazionaria? Si risponda sì o no. **(b)** Il correlogramma suggerisce un modello AR (e non un MA)? Si risponda sì o no. **(c)** Qual è l'ordine del modello proposto?
<!-- /ex -->
