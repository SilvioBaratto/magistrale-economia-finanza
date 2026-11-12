<!-- ex e06_01 -->
# Esercizio 1 — Media, varianza e autocorrelazioni di un AR(1) e di un MA(1) *(livello base)*

> [!abstract] Dati
> Sia $\epsilon_t$ un rumore bianco, con $E[\epsilon_t]=0$ e $\text{Var}(\epsilon_t)=\sigma^2={{e06_01.s2}}$. Si considerano tre processi:
>
> - processo A: $Y_t={{e06_01.c}}+{{e06_01.phi|m}}\,Y_{t-1}+\epsilon_t$;
> - processo B: $X_t=\epsilon_t+({{e06_01.theta|m}})\,\epsilon_{t-1}$;
> - processo C: $Z_t=Z_{t-1}+\epsilon_t$.

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** Per il processo A, ammesso che sia stazionario: **(a)** quanto vale la media $E[Y_t]$? **(b)** Quanto vale la varianza $\text{Var}(Y_t)$? **(c)** Quanto vale l'autocorrelazione $\rho_k=\text{Corr}(Y_t,Y_{t-k})$ al ritardo $k={{e06_01.k}}$? Per il processo B: **(d)** quanto vale $\text{Var}(X_t)$? **(e)** Quanto vale l'autocorrelazione $\rho_1=\text{Corr}(X_t,X_{t-1})$? **(f)** Il processo C è stazionario? Si risponda sì o no.
<!-- /ex -->

<!-- ex e06_02 -->
# Esercizio 2 — Stazionaria o no? Il correlogramma di due serie *(livello base)*

> [!abstract] Dati
> Di due serie storiche A e B, osservate in $T={{e06_02.n}}$ periodi, si riportano l'autocorrelazione (ACF) e l'autocorrelazione parziale (PACF) campionarie fino al ritardo ${{e06_02.k}}$. La fascia azzurra è la banda di significatività al 5\%, $\pm 1{,}96/\sqrt{T}$; i ritardi che ne escono sono disegnati in rosso.
>
> ![ACF (in alto) e PACF (in basso) della serie A (a sinistra) e della serie B (a destra).]({{e06_02.fig.dati}}){width=92%}

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** La serie A è stazionaria? Si risponda sì o no. **(b)** La serie B è stazionaria? Si risponda sì o no. **(c)** Quanti fra i primi ${{e06_02.k}}$ ritardi della PACF della serie A escono dalla banda di significatività?
<!-- /ex -->

<!-- ex e06_03 -->
# Esercizio 3 — Cambio e spread: la regressione di Dickey-Fuller aumentata *(livello base)*

> [!abstract] Dati
> Per stabilire se le serie `cambio` e `spread`, osservate in $T={{e06_03.T}}$ periodi, sono stazionarie, per ciascuna serie $y_t$ si è stimata la regressione di Dickey-Fuller aumentata con costante e due ritardi della differenza,
>
> $$\Delta y_t=\beta_0+\delta\,y_{t-1}+\psi_1\,\Delta y_{t-1}+\psi_2\,\Delta y_{t-2}+\epsilon_t ,$$
>
> dove `cambio_1` è $y_{t-1}$ per la serie `cambio` e `d_cambio_1`, `d_cambio_2` sono $\Delta y_{t-1}$ e $\Delta y_{t-2}$ (analogamente per `spread`). Il valore critico del test al 5\% è ${{e06_03.crit|m}}$ per entrambe le serie. Variabile dipendente $\Delta$`cambio`:
>
> {{e06_03.tab.a}}
>
> Variabile dipendente $\Delta$`spread`:
>
> {{e06_03.tab.b}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** **(a)** Quanto vale la statistica del test ADF per `cambio`? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (stazionarietà) per `cambio`: si rifiuta se la statistica è minore del valore critico. **(c)** Quanto vale la statistica del test ADF per `spread`? **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ per `spread`, con lo stesso criterio. **(e)** Quante delle due serie risultano stazionarie?
<!-- /ex -->

<!-- ex e06_04 -->
# Esercizio 4 — Quale regressione di Dickey-Fuller per `produzione` e `tasso`? *(livello intermedio)*

> [!abstract] Dati
> Si vuole verificare la stazionarietà delle serie `produzione` e `tasso`, osservate in $T={{e06_04.T}}$ periodi, con un test di Dickey-Fuller aumentato. Le serie sono nel grafico; la tabella ne riassume l'andamento con la media del primo e dell'ultimo terzo del campione e con la deviazione standard.
>
> ![Serie `produzione` (a sinistra) e `tasso` (a destra).]({{e06_04.fig.dati}}){width=85%}
>
> {{e06_04.tab.desc}}
>
> Un'analisi preliminare indica che entrambe le serie seguono un modello autoregressivo di ordine $p={{e06_04.p}}$, $y_t=\beta_0+\beta_1y_{t-1}+\dots+\beta_py_{t-p}+\epsilon_t$. Per `tasso` l'AR($p$) in livelli è stato stimato con $\hat\beta_1={{e06_04.b1|m}}$, $\hat\beta_2={{e06_04.b2|m}}$ e $\hat\beta_3={{e06_04.b3|m}}$.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** La regressione di Dickey-Fuller aumentata ha la forma $\Delta y_t=\beta_0^*+\alpha\,t+\delta\,y_{t-1}+\sum_{j=1}^{p-1}\psi_j\,\Delta y_{t-j}+\epsilon_t$, in cui il trend $\alpha\,t$ può essere omesso. **(a)** Per `produzione` la regressione deve includere il trend deterministico? Si risponda sì o no. **(b)** Per `tasso` la regressione deve includere il trend deterministico? Si risponda sì o no. **(c)** Quanti ritardi della differenza $\Delta y_{t-j}$ deve contenere la regressione? **(d)** Quanti coefficienti (costante compresa) ha la regressione di Dickey-Fuller di `produzione`? **(e)** Quanto vale $\delta$ nella regressione di Dickey-Fuller di `tasso`, ottenuta riscrivendo l'AR($p$) stimato?
<!-- /ex -->

<!-- ex e06_05 -->
# Esercizio 5 — Il prezzo ha una radice unitaria? Il test ADF in livelli e in differenze *(livello intermedio)*

> [!abstract] Dati
> La serie `prezzo`, osservata in $T={{e06_05.T}}$ periodi, cresce nel tempo. Si esegue il test di Dickey-Fuller aumentato con costante, trend e un ritardo della differenza,
>
> $$\Delta y_t=\beta_0+\alpha\,t+\delta\,y_{t-1}+\psi_1\,\Delta y_{t-1}+\epsilon_t ,$$
>
> dove `time` è il trend. Il valore critico del test al 5\% è ${{e06_05.crit_ct|m}}$.
>
> {{e06_05.tab.liv}}
>
> La serie delle differenze `dprezzo`$_t=\Delta$`prezzo`$_t$ non ha trend: per essa si esegue lo stesso test con la sola costante (`dprezzo_1` è `dprezzo`$_{t-1}$ e `d_dprezzo_1` è la sua differenza ritardata). Il valore critico al 5\% è ${{e06_05.crit_c|m}}$.
>
> {{e06_05.tab.dif}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Quanto vale la statistica del test ADF per `prezzo`? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ per `prezzo`: si rifiuta se la statistica è minore del valore critico. **(c)** Quanto vale la statistica del test ADF per `dprezzo`? **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ per `dprezzo`, confrontando la statistica con il valore critico della sua regressione. **(e)** Prima di usare `prezzo` come variabile di una regressione, occorre differenziarla? Si risponda sì o no.
<!-- /ex -->

<!-- ex e06_06 -->
# Esercizio 6 — Due random walk indipendenti: una regressione spuria *(livello intermedio)*

> [!abstract] Dati
> Le serie $x_t$ e $y_t$ ($T={{e06_06.T}}$ periodi) sono state generate al computer come due random walk indipendenti, $x_t=x_{t-1}+u_t$ e $y_t=y_{t-1}+v_t$, con $u_t$ e $v_t$ rumori bianchi indipendenti: nella relazione fra le due serie il vero valore di $\beta_1$ è quindi $0$. Regressione in livelli, $y_t=\beta_0+\beta_1x_t+\epsilon_t$:
>
> {{e06_06.tab.liv}}
>
> Regressione delle differenze prime, $\Delta y_t=\beta_0+\beta_1\,\Delta x_t+\epsilon_t$ (`dx` è $\Delta x_t$):
>
> {{e06_06.tab.dif}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$ nella regressione in livelli: si rifiuta se $|t|>1{,}96$. **(b)** Quanto vale l'$R^2$ della regressione in livelli? **(c)** La significatività osservata in (a) è un'evidenza affidabile di una relazione fra $x_t$ e $y_t$? Si risponda sì o no. **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$ nella regressione delle differenze.
<!-- /ex -->

<!-- ex e06_07 -->
# Esercizio 7 — AR o MA? L'identificazione dal correlogramma *(livello intermedio)*

> [!abstract] Dati
> Di due serie storiche C e D, osservate in $T={{e06_07.T}}$ periodi, si riportano l'ACF e la PACF campionarie fino al ritardo ${{e06_07.k}}$. La fascia azzurra è la banda di significatività al 5\%, $\pm 1{,}96/\sqrt{T}$; i ritardi che ne escono sono disegnati in rosso. Le serie vanno descritte con un modello AR($p$) oppure MA($q$).
>
> ![ACF (in alto) e PACF (in basso) della serie C (a sinistra) e della serie D (a destra).]({{e06_07.fig.dati}}){width=92%}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Per la serie C si propone un modello AR (e non un MA)? Si risponda sì o no. **(b)** Qual è l'ordine del modello proposto per C? **(c)** Per la serie D si propone un modello AR (e non un MA)? Si risponda sì o no. **(d)** Qual è l'ordine del modello proposto per D? **(e)** Entrambe le serie sono stazionarie? Si risponda sì o no.
<!-- /ex -->

<!-- ex e06_08 -->
# Esercizio 8 — Radici unitarie: statistica ADF e p-value *(livello intermedio)*

> [!abstract] Dati
> Su tre serie, osservate in $T={{e06_08.T}}$ periodi, si è eseguito il test di Dickey-Fuller aumentato con due ritardi della differenza e con i termini deterministici indicati. Per ciascuna serie il sistema di ipotesi è $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (stazionarietà). I p-value sono quelli del test di Dickey-Fuller, calcolati dal programma, e non quelli della $t$ di Student.
>
> {{e06_08.tab.adf}}

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ per `oro`: si rifiuta se il p-value è minore di $0{,}05$. **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ per `argento`. **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ per `tasso`. **(d)** Quante delle tre serie hanno una radice unitaria e vanno differenziate prima di essere usate in una regressione? **(e)** La statistica ADF di `argento` è minore della soglia $-1{,}64$ della Normale standard: il confronto con quella soglia è corretto per il test ADF? Si risponda sì o no.
<!-- /ex -->

<!-- ex e06_09 -->
# Esercizio 9 — Un break in una data nota: il test di Chow *(livello intermedio)*

> [!abstract] Dati
> Su $T={{e06_09.T}}$ osservazioni trimestrali si stima la relazione $\text{consumo}_t=\beta_0+\beta_1\,\text{reddito}_t+\epsilon_t$. Una riforma ha cambiato il regime dopo l'osservazione ${{e06_09.tau}}$ (data nota). Si stima il modello sull'intero campione (Modello 1), sulle prime ${{e06_09.tau}}$ osservazioni (Modello 2) e sulle restanti (Modello 3).
>
> Modello 1:
>
> {{e06_09.tab.intero}}
>
> Modello 2:
>
> {{e06_09.tab.prima}}
>
> Modello 3:
>
> {{e06_09.tab.dopo}}
>
> Il test di Chow verifica $H_0$: i parametri sono uguali nei due sottocampioni (nel modello con la dummy $D_t=1$ per $t>\tau$ e le sue interazioni, $\gamma_0=\gamma_1=0$) contro $H_1$: almeno un parametro cambia. È il test $F$ in cui il modello vincolato è il Modello 1 e il non vincolato è la coppia dei Modelli 2 e 3. Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà del test è ${{e06_09.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Quanto vale la statistica $F$ del test di Chow? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$: si rifiuta se $F$ supera il valore critico. **(c)** Di quanto cambia la stima della pendenza di `reddito` dopo la riforma, cioè $\hat\beta_1$ del Modello 3 meno $\hat\beta_1$ del Modello 2? **(d)** Quanti sono i gradi di libertà del denominatore della statistica $F$?
<!-- /ex -->

<!-- ex e06_10 -->
# Esercizio 10 — Un break in una data ignota: il valore critico del test QLR *(livello intermedio)*

> [!abstract] Dati
> Su $T={{e06_10.T}}$ osservazioni mensili si stima il CAPM, $r_t-r_{f}=\alpha+\beta\,(r_{mt}-r_{f})+\epsilon_t$. Non si conosce la data di un eventuale break strutturale: si calcola la statistica di Chow $F(\tau)$ per ogni data candidata $\tau$, escludendo il 15\% iniziale e il 15\% finale del campione, e la statistica QLR è il massimo di queste $F(\tau)$. Il massimo si ha in corrispondenza della data $\hat\tau={{e06_10.tau}}$ (la data $\tau$ è l'ultima osservazione del primo sottocampione). Le somme dei quadrati dei residui del modello sull'intero campione e sui due sottocampioni sono:
>
> {{e06_10.tab.ssr}}
>
> La statistica di Chow $F(\tau)$ è il test $F$ di $H_0$: i parametri (costante e pendenza) sono uguali nei due sottocampioni, in cui il modello vincolato è quello sull'intero campione e il non vincolato è la coppia dei due sottocampioni. Il test QLR ha $H_0$: parametri stabili in ogni data (nessun break) contro $H_1$: break in almeno una data. Il valore critico al 5\% del test QLR per due restrizioni, con il 15\% escluso agli estremi (il valore della nota del corso), è ${{e06_10.qcrit|m}}$. Per confronto, il valore critico al 5\% della $F$ usata per un test di Chow in una data fissata è ${{e06_10.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 10 *(3 punti)*.** **(a)** Quanto vale la statistica QLR, cioè la statistica $F$ di Chow nella data $\hat\tau$? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$ con il test QLR: si rifiuta se la statistica supera il valore critico del QLR. **(c)** Un analista confronta invece la statistica con il valore critico della $F$ usuale, ${{e06_10.fcrit|m}}$: con quel confronto rifiuterebbe $H_0$? Si risponda sì o no. **(d)** I break strutturali sono un problema per questa regressione? Si risponda sì o no.
<!-- /ex -->

<!-- ex e06_11 -->
# Esercizio 11 — Il test ADF su una serie che cresce: con o senza trend? *(livello appello)*

> [!abstract] Dati
> La serie `pil`, osservata in $T={{e06_11.T}}$ periodi, è nel grafico; la tabella riassume il suo andamento con la media del primo e dell'ultimo terzo del campione e con la deviazione standard.
>
> ![Serie `pil`.]({{e06_11.fig.dati}}){width=60%}
>
> {{e06_11.tab.desc}}
>
> Per verificare se è stazionaria si stimano due regressioni di Dickey-Fuller aumentate con ${{e06_11.lags}}$ ritardi della differenza: il Modello 1 con la sola costante e il Modello 2 con la costante e il trend `time`,
>
> $$\Delta y_t=\beta_0+\alpha\,t+\delta\,y_{t-1}+\psi_1\,\Delta y_{t-1}+\psi_2\,\Delta y_{t-2}+\epsilon_t ,$$
>
> dove nel Modello 1 manca il termine $\alpha\,t$. In entrambi il sistema di ipotesi è $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$. I valori critici al 5\% sono ${{e06_11.crit_c|m}}$ per il Modello 1 e ${{e06_11.crit_ct|m}}$ per il Modello 2.
>
> Modello 1:
>
> {{e06_11.tab.m1}}
>
> Modello 2:
>
> {{e06_11.tab.m2}}

> [!question] Testo della domanda
> **Domanda 11 *(4 punti)*.** **(a)** Il Modello 2, con il trend, è quello appropriato per `pil`? Si risponda sì o no. **(b)** Quanto vale la statistica del test ADF nel modello appropriato? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta=0$ contro $H_1:\delta<0$ con il modello appropriato: si rifiuta se la statistica è minore del valore critico di quel modello. **(d)** La serie `pil` è stazionaria attorno a un trend deterministico? Si risponda sì o no. **(e)** Con il Modello 1 e il suo valore critico si sarebbe giunti alla stessa decisione della domanda (c)? Si risponda sì o no. **(f)** Se `pil` seguisse l'AR(3) con trend $y_t=\beta_0+\alpha\,t+\beta_1y_{t-1}+\beta_2y_{t-2}+\beta_3y_{t-3}+\epsilon_t$ e il Modello 2 ne fosse la riscrittura, quanto varrebbe la stima di $\beta_1+\beta_2+\beta_3$?
<!-- /ex -->

<!-- ex e06_12 -->
# Esercizio 12 — Livello e differenza prima: stazionarietà e identificazione *(livello appello)*

> [!abstract] Dati
> Si dispone della serie $y_t$ e della sua differenza prima $\Delta y_t=y_t-y_{t-1}$, che ha $T={{e06_12.T}}$ osservazioni. Si riportano l'ACF e la PACF campionarie di entrambe fino al ritardo ${{e06_12.k}}$, con la banda di significatività al 5\% $\pm 1{,}96/\sqrt{T}$ (i ritardi che ne escono sono in rosso). L'autocorrelazione campionaria di $\Delta y_t$ al ritardo 1 vale $\hat\rho_1={{e06_12.rho1|m}}$.
>
> ![ACF (in alto) e PACF (in basso) di $y_t$ (a sinistra) e di $\Delta y_t$ (a destra).]({{e06_12.fig.dati}}){width=92%}

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** **(a)** La serie $y_t$ è stazionaria? Si risponda sì o no. **(b)** La serie $\Delta y_t$ è stazionaria? Si risponda sì o no. **(c)** Per $\Delta y_t$ si propone un modello AR (e non un MA)? Si risponda sì o no. **(d)** Qual è l'ordine del modello proposto per $\Delta y_t$? **(e)** Sia $\Delta y_t=\alpha+\epsilon_t+\theta\,\epsilon_{t-1}$ un MA(1), con $\text{Var}(\Delta y_t)=(1+\theta^2)\sigma^2$ e $\text{Cov}(\Delta y_t,\Delta y_{t-1})=\theta\sigma^2$. Uguagliando $\rho_1$ a $\hat\rho_1$ si ottengono due valori di $\theta$: si calcoli quello con $|\theta|<1$.
<!-- /ex -->

<!-- ex e06_13 -->
# Esercizio 13 — Una relazione che sparisce sull'intero campione: il test QLR *(livello appello)*

> [!abstract] Dati
> Su $T={{e06_13.T}}$ osservazioni mensili si stima il CAPM per l'extra-rendimento di un titolo, $r_t=\alpha+\beta\,m_t+\epsilon_t$, dove $m_t$ è l'extra-rendimento del mercato (`mkt`). Il Modello 1 è stimato sull'intero campione.
>
> Modello 1:
>
> {{e06_13.tab.pieno}}
>
> Si sospetta un break strutturale in una data ignota. Si calcola la statistica di Chow $F(\tau)$ per ogni data candidata $\tau$, escludendo il 15\% iniziale e il 15\% finale del campione, e la statistica QLR è il massimo delle $F(\tau)$. Il massimo si ha in corrispondenza di $\hat\tau={{e06_13.tau}}$ (ultima osservazione del primo sottocampione). Il Modello 2 è stimato sulle osservazioni $1,\dots,\hat\tau$ e il Modello 3 sulle restanti.
>
> Modello 2:
>
> {{e06_13.tab.prima}}
>
> Modello 3:
>
> {{e06_13.tab.dopo}}
>
> La statistica QLR è la $F$ di Chow in $\hat\tau$, cioè il test $F$ di $H_0$: i parametri sono uguali nei due sottocampioni, in cui il modello vincolato è il Modello 1 e quello non vincolato è la coppia dei Modelli 2 e 3 (costante e pendenza in ciascuno). Il valore critico al 5\% del test QLR per due restrizioni, con il 15\% escluso agli estremi, è ${{e06_13.qcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 13 *(4 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta=0$ contro $H_1:\beta\neq 0$ nel Modello 1 (cioè se il mercato spiega il rendimento del titolo): si rifiuta se $|t|>1{,}96$. **(b)** Quanto vale la statistica QLR? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0$ (parametri stabili) con il test QLR: si rifiuta se la statistica supera il valore critico. **(d)** Il risultato della domanda (a), cioè che il mercato non spiega il rendimento del titolo, è affidabile? Si risponda sì o no. **(e)** Di quanto cambia la stima della pendenza dopo $\hat\tau$, cioè $\hat\beta$ del Modello 3 meno $\hat\beta$ del Modello 2?
<!-- /ex -->
