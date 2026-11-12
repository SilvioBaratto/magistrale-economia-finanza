<!-- ex e07_01 -->
# Esercizio 1 — Il prezzo del grano a Chicago e a Rotterdam *(livello base)*

> [!abstract] Dati
> Si dispone di $n = {{e07_01.n}}$ osservazioni mensili del prezzo del grano a Rotterdam (`rot`) e a Chicago (`chi`), in dollari per tonnellata. Per ciascuna serie $s_t$ si è stimata la regressione di Dickey-Fuller aumentata
>
> $$\Delta s_t = c + \delta\,s_{t-1} + \phi\,\Delta s_{t-1} + \epsilon_t ,$$
>
> dove nelle tabelle `rot_1` e `chi_1` sono i livelli ritardati $s_{t-1}$ e `d_rot_1` e `d_chi_1` le differenze ritardate $\Delta s_{t-1}$. Il sistema di ipotesi è $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (serie stazionaria): si rifiuta $H_0$ se il rapporto $t$ di $\delta$ è minore del valore critico ${{e07_01.cv|m}}$.
>
> **Serie `rot`** (variabile dipendente `d_rot`).
>
> {{e07_01.tab.adf_y}}
>
> **Serie `chi`** (variabile dipendente `d_chi`).
>
> {{e07_01.tab.adf_x}}
>
> Si è poi stimata la relazione di lungo periodo $\text{rot}_t=\alpha+\beta\,\text{chi}_t+u_t$ e si è applicato il test di Engle-Granger ai residui: $H_0$ è che i residui abbiano una radice unitaria (assenza di cointegrazione), $H_1$ che siano stazionari (cointegrazione). Il p-value del test è ${{e07_01.p_eg|m}}$. Le regressioni usano le osservazioni che restano dopo la differenziazione e il ritardo.

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** Al livello del 5\%: **(a)** per la serie `rot`, si decida se rifiutare o non rifiutare $H_0:\delta=0$; **(b)** lo stesso per la serie `chi`; **(c)** si decida se rifiutare o non rifiutare l'ipotesi nulla del test di Engle-Granger; **(d)** si può parlare di una relazione di cointegrazione fra `rot` e `chi`? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_02 -->
# Esercizio 2 — Spread BTP-Bund e rendimento del Bund *(livello base)*

> [!abstract] Dati
> Su $n = {{e07_02.n}}$ osservazioni trimestrali si considerano lo spread fra i rendimenti dei titoli di Stato italiani e tedeschi (`spread`) e il rendimento del Bund decennale (`bund`), entrambi in punti percentuali. Per ciascuna serie $s_t$ si è stimata la regressione di Dickey-Fuller aumentata
>
> $$\Delta s_t = c + \delta\,s_{t-1} + \phi\,\Delta s_{t-1} + \epsilon_t ,$$
>
> dove nelle tabelle `spread_1` e `bund_1` sono i livelli ritardati $s_{t-1}$ e `d_spread_1` e `d_bund_1` le differenze ritardate. Il sistema di ipotesi è $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$ (serie stazionaria): si rifiuta $H_0$ se il rapporto $t$ di $\delta$ è minore del valore critico ${{e07_02.cv|m}}$.
>
> **Serie `spread`** (variabile dipendente `d_spread`).
>
> {{e07_02.tab.adf_y}}
>
> **Serie `bund`** (variabile dipendente `d_bund`).
>
> {{e07_02.tab.adf_x}}
>
> Si è infine stimata con OLS la relazione fra i livelli $\text{spread}_t=\alpha+\beta\,\text{bund}_t+u_t$.
>
> {{e07_02.tab.statica}}

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** Al livello del 5\%: **(a)** per la serie `spread`, si decida se rifiutare o non rifiutare $H_0:\delta=0$; **(b)** lo stesso per la serie `bund`; **(c)** la regressione statica di `spread` su `bund` è ben definita, cioè ha senso leggerla come relazione di lungo periodo fra livelli? Si risponda sì o no. **(d)** `spread` e `bund` possono essere cointegrate? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_03 -->
# Esercizio 3 — Consumi e reddito: il coefficiente di correzione *(livello base)*

> [!abstract] Dati
> Si considerano i consumi (`cons`) e il reddito disponibile (`red`) trimestrali, entrambi misurati in 100 volte il logaritmo, per cui una variazione di una unità vale un punto. I test ADF indicano che entrambe le serie sono integrate di ordine 1; il test di Engle-Granger sui residui della relazione di lungo periodo $\text{cons}_t=\alpha+\beta\,\text{red}_t+u_t$ ($H_0$: assenza di cointegrazione) ha p-value ${{e07_03.p_eg|m}}$. Il modello a correzione dell'errore
>
> $$\Delta\text{cons}_t=\gamma_0+\gamma_1\,\Delta\text{red}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{cons}_{t-1}-\hat\alpha-\hat\beta\,\text{red}_{t-1} ,$$
>
> è stimato con OLS su $n = {{e07_03.n}}$ osservazioni (variabile dipendente `d_cons`).
>
> {{e07_03.tab.ecm}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(b)** Il modello è ben definito, cioè bilanciato e con un meccanismo di correzione dell'errore? Si risponda sì o no. Si supponga ora che in $t$ i consumi siano al di sotto della relazione di lungo periodo, $\text{ecm}_t={{e07_03.d|m}}$, che $\Delta\text{red}_{t+1}=0$, che lo shock $\epsilon_{t+1}$ sia nullo e si trascuri la costante. **(c)** La variazione attesa dei consumi in $t+1$ è superiore a quella che si avrebbe con $\text{ecm}_t=0$? Si risponda sì o no. **(d)** Quanto vale, in punti, la variazione attesa $\Delta\text{cons}_{t+1}$?
<!-- /ex -->

<!-- ex e07_04 -->
# Esercizio 4 — Il prezzo della benzina: in quanti mesi si assorbe il disequilibrio *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e07_04.n}}$ osservazioni mensili si considerano il prezzo della benzina alla pompa (`benz`) e il prezzo del petrolio (`petr`). Le serie sono cointegrate e il modello a correzione dell'errore
>
> $$\Delta\text{benz}_t=\gamma_0+\gamma_1\,\Delta\text{petr}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{benz}_{t-1}-\hat\alpha-\hat\beta\,\text{petr}_{t-1} ,$$
>
> è stimato con OLS (variabile dipendente `d_benz`).
>
> {{e07_04.tab.ecm}}
>
> Si ipotizzi che in $t-1$ si osservi un disequilibrio $z_{t-1}=\text{ecm}_{t-1}\neq 0$, che da $t$ in poi il prezzo del petrolio resti costante ($\Delta\text{petr}=0$), che tutti gli shock siano nulli e che si trascuri la costante. Il periodo $t$ è il primo periodo di aggiustamento: dopo $k$ periodi di aggiustamento il disequilibrio residuo è $z_{t+k-1}$.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(b)** Quale quota del disequilibrio iniziale $z_{t-1}$, in percentuale, viene assorbita nel primo periodo di aggiustamento? **(c)** Qual è il minimo numero intero $k$ di periodi dopo il quale almeno il ${{e07_04.q1}}\%$ del disequilibrio iniziale è stato assorbito? **(d)** E perché ne sia assorbito almeno il ${{e07_04.q2}}\%$? **(e)** Quale quota del disequilibrio iniziale, in percentuale, risulta effettivamente assorbita dopo il numero di periodi trovato in (d)?
<!-- /ex -->

<!-- ex e07_05 -->
# Esercizio 5 — Due coppie di serie, due correlogrammi *(livello intermedio)*

> [!abstract] Dati
> Si considerano due coppie di serie mensili, tutte integrate di ordine 1 secondo il test ADF, ciascuna con $n = {{e07_05.n}}$ osservazioni.
>
> **Coppia A**: il tasso d'interesse a 12 mesi (`r12`) e quello a 3 mesi (`r3`). Relazione di lungo periodo $\text{r12}_t=\alpha+\beta\,\text{r3}_t+u_t$.
>
> {{e07_05.tab.a}}
>
> **Coppia B**: il prezzo del caffè (`caffe`) e l'indice della produzione industriale (`ind`), che non hanno un legame economico noto. Relazione di lungo periodo $\text{caffe}_t=\alpha+\beta\,\text{ind}_t+u_t$.
>
> {{e07_05.tab.b}}
>
> La figura riporta l'ACF (in alto) e la PACF (in basso) dei residui $\hat u_t$ delle due relazioni, sui primi 12 ritardi; le barre rosse escono dalle bande di confidenza al 95\%.
>
> ![ACF e PACF dei residui delle relazioni di lungo periodo: coppia A a sinistra, coppia B a destra.]({{e07_05.fig.correlogrammi}}){width=85%}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Per la coppia A, quanti dei primi 12 ritardi dell'ACF dei residui escono dalle bande di confidenza al 95\%? **(b)** I residui della coppia A sembrano stazionari? Si risponda sì o no. **(c)** I residui della coppia B sembrano stazionari? Si risponda sì o no. **(d)** Per la coppia B l'$R^2$ è elevato e il rapporto $t$ di `ind` è molto grande: si può per questo parlare di cointegrazione fra `caffe` e `ind`? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_06 -->
# Esercizio 6 — Importazioni e PIL: i residui dell'ECM *(livello intermedio)*

> [!abstract] Dati
> Si considerano le importazioni (`imp`) e il PIL (`pil`) trimestrali, integrati di ordine 1. Il test di Engle-Granger sui residui della relazione di lungo periodo $\text{imp}_t=\alpha+\beta\,\text{pil}_t+u_t$ ($H_0$: assenza di cointegrazione) ha p-value ${{e07_06.p_eg|m}}$. Il modello a correzione dell'errore
>
> $$\Delta\text{imp}_t=\gamma_0+\gamma_1\,\Delta\text{pil}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{imp}_{t-1}-\hat\alpha-\hat\beta\,\text{pil}_{t-1} ,$$
>
> è stimato con OLS su $n = {{e07_06.n}}$ osservazioni (variabile dipendente `d_imp`).
>
> {{e07_06.tab.ecm}}
>
> La figura riporta l'ACF (in alto) e la PACF (in basso) dei residui del modello, sui primi 12 ritardi, con le bande di confidenza al 95\%; le barre rosse escono dalle bande.
>
> ![ACF e PACF dei residui del modello a correzione dell'errore.]({{e07_06.fig.correlogramma}}){width=85%}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(b)** Il primo ritardo dell'ACF dei residui esce dalle bande di confidenza? Si risponda sì o no. **(c)** Occorre ri-specificare la dinamica di breve periodo del modello, per esempio aggiungendo ritardi di $\Delta\text{imp}$ e di $\Delta\text{pil}$? Si risponda sì o no. **(d)** Occorre ri-specificare la relazione di lungo periodo? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_07 -->
# Esercizio 7 — Benzina e petrolio: l'effetto di lungo periodo con il DOLS *(livello intermedio)*

> [!abstract] Dati
> Si considerano il prezzo della benzina alla pompa (`benz`, in centesimi al litro) e il prezzo del petrolio (`petr`, in dollari al barile), osservazioni settimanali. I test ADF di radice unitaria ($H_0$: radice unitaria) hanno p-value ${{e07_07.p_y|m}}$ per `benz` e ${{e07_07.p_x|m}}$ per `petr`; il test di Engle-Granger sui residui della relazione di lungo periodo ($H_0$: assenza di cointegrazione) ha p-value ${{e07_07.p_eg|m}}$.
>
> La relazione di lungo periodo $\text{benz}_t=\alpha+\beta\,\text{petr}_t+u_t$ è stimata con lo stimatore DOLS, aggiungendo ${{e07_07.ell|m}}$ anticipi, ${{e07_07.ell|m}}$ ritardi e il termine contemporaneo di $\Delta\text{petr}$ (i loro coefficienti sono omessi dalla tabella). Gli errori standard sono HAC di Newey-West, con nucleo di Bartlett e ${{e07_07.banda|m}}$ autocovarianze. La stima usa $n = {{e07_07.n}}$ osservazioni.
>
> {{e07_07.tab.dols}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Si può parlare di una relazione di cointegrazione fra `benz` e `petr`, al livello del 5\%? Si risponda sì o no. Si indichi con $\theta$ la variazione attesa di `benz` quando `petr` aumenta di ${{e07_07.delta|m}}$ dollari. **(b)** Quanto vale la stima puntuale di $\theta$, in centesimi al litro? **(c)** Qual è l'estremo inferiore e **(d)** qual è l'estremo superiore dell'intervallo di confidenza al 95\% per $\theta$? **(e)** Un analista afferma che un aumento di ${{e07_07.delta|m}}$ dollari del petrolio fa aumentare la benzina di ${{e07_07.riv|m}}$ centesimi, cioè $H_0:\theta={{e07_07.riv|m}}$ contro $H_1:\theta\neq{{e07_07.riv|m}}$. Al livello del 5\%, l'affermazione è compatibile con i dati? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_08 -->
# Esercizio 8 — Superconsistenza e DOLS in una simulazione *(livello intermedio)*

> [!abstract] Dati
> Per illustrare la stima di una relazione di lungo periodo si sono simulate ${{e07_08.sim}}$ coppie di serie in due casi, con coefficiente vero $\beta={{e07_08.beta|m}}$.
>
> **Caso A (serie cointegrate).** $x_t$ è una passeggiata aleatoria con deriva ${{e07_08.deriva|m}}$ e innovazioni di varianza 1; $y_t=2+\beta\,x_t+u_t$, con $u_t$ un AR(1) di coefficiente ${{e07_08.phi_a|m}}$ e innovazioni di varianza 1.
>
> **Caso B (serie stazionarie).** $x_t$ è un AR(1) di coefficiente ${{e07_08.phi_b|m}}$ e innovazioni di varianza 1; $y_t=2+\beta\,x_t+\epsilon_t$, con $\epsilon_t$ IID di varianza 1.
>
> Per ogni caso e per tre numerosità campionarie $T$ si è stimato $\beta$ con OLS sulla regressione statica di $y$ su $x$ e si riporta la deviazione standard delle ${{e07_08.sim}}$ stime $\hat\beta$.
>
> {{e07_08.tab.sd}}
>
> Nel caso A, con $T={{e07_08.durata_cop}}$, si è inoltre calcolata la frequenza con cui l'intervallo di confidenza al 95\% per $\beta$ contiene il valore vero, con due metodi: la regressione statica OLS con l'errore standard usuale e il DOLS ({{e07_08.ell|m}} anticipi e {{e07_08.ell|m}} ritardi di $\Delta x$) con errori standard HAC di Newey-West ({{e07_08.banda|m}} autocovarianze).
>
> {{e07_08.tab.cop}}

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Nel caso A, quanto vale il rapporto fra la deviazione standard di $\hat\beta$ con $T={{e07_08.durata_cop}}$ e quella con $T=100$? **(b)** E nel caso B? **(c)** Nel caso A l'errore di stima si riduce più rapidamente, all'aumentare di $T$, che nel caso B (cioè il rapporto in (a) è minore di quello in (b))? Si risponda sì o no. **(d)** Di quanti punti percentuali la copertura dell'intervallo OLS con errore standard usuale è inferiore al 95\%? **(e)** Si consideri affidabile un intervallo la cui copertura differisce dal 95\% per non più di ${{e07_08.tolleranza|m}}$ punti percentuali: l'intervallo OLS con errore standard usuale è affidabile? Si risponda sì o no. **(f)** L'intervallo DOLS con errori HAC ha una copertura più vicina al 95\% di quello OLS? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_09 -->
# Esercizio 9 — Borsa di Milano e di Francoforte: quale errore standard *(livello appello)*

> [!abstract] Dati
> Si considerano gli indici azionari di Milano (`mib`) e di Francoforte (`dax`), $n = {{e07_09.n}}$ osservazioni settimanali. I test ADF di radice unitaria ($H_0$: radice unitaria) hanno p-value ${{e07_09.p_y|m}}$ per `mib` e ${{e07_09.p_x|m}}$ per `dax`; il test di Engle-Granger sui residui della relazione di lungo periodo $\text{mib}_t=\alpha+\beta\,\text{dax}_t+u_t$ ($H_0$: assenza di cointegrazione) ha p-value ${{e07_09.p_eg|m}}$.
>
> **Stima OLS della regressione statica** (errori standard usuali).
>
> {{e07_09.tab.ols}}
>
> **Stima DOLS** con ${{e07_09.ell|m}}$ anticipi, ${{e07_09.ell|m}}$ ritardi e il termine contemporaneo di $\Delta\text{dax}$ (coefficienti omessi), errori standard HAC di Newey-West con ${{e07_09.banda|m}}$ autocovarianze.
>
> {{e07_09.tab.dols}}
>
> Un analista sostiene che $\beta={{e07_09.b0|m}}$.

> [!question] Testo della domanda
> **Domanda 9 *(4 punti)*.** **(a)** Si può parlare di una relazione di cointegrazione fra `mib` e `dax`, al livello del 5\%? Si risponda sì o no. Si consideri il sistema di ipotesi $H_0:\beta={{e07_09.b0|m}}$ contro $H_1:\beta\neq{{e07_09.b0|m}}$. **(b)** Usando la stima OLS della regressione statica con l'errore standard usuale e i quantili della normale, si decida se rifiutare o non rifiutare $H_0$ al livello del 5\%. **(c)** Quanto vale il rapporto $t$ per $H_0$ ottenuto dalla stima DOLS con errore standard HAC? **(d)** Al livello del 5\%, usando lo stimatore e l'errore standard appropriati per variabili cointegrate, l'affermazione dell'analista è compatibile con i dati? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_10 -->
# Esercizio 10 — Margine, benzina e petrolio: quando Engle-Granger inganna *(livello appello)*

> [!abstract] Dati
> Su $n = {{e07_10.n}}$ osservazioni mensili si considerano il prezzo del petrolio (`petr`), il prezzo della benzina alla pompa (`benz`) e il margine lordo dei distributori (`margine`). Per ciascuna serie si è stimata la regressione di Dickey-Fuller aumentata con costante e un ritardo, con $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$: si rifiuta $H_0$ se la statistica $t$ del test è minore del valore critico ${{e07_10.cv|m}}$.
>
> {{e07_10.tab.adf}}
>
> Si è poi applicato il test di Engle-Granger ai residui delle due relazioni di lungo periodo indicate, con $H_0$: assenza di cointegrazione. Una regressione statica fra livelli si dice ben definita se ha senso leggerla come relazione di lungo periodo.
>
> {{e07_10.tab.eg}}

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** Al livello del 5\%: **(a)** per la serie `margine`, si decida se rifiutare o non rifiutare $H_0:\delta=0$; **(b)** si può parlare di cointegrazione fra `margine` e `petr`? Si risponda sì o no. **(c)** Si può parlare di cointegrazione fra `benz` e `petr`? Si risponda sì o no. **(d)** La regressione statica di `margine` su `petr` è ben definita? Si risponda sì o no. **(e)** La regressione statica di `benz` su `petr` è ben definita? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_11 -->
# Esercizio 11 — Investimenti e PIL: dopo un disequilibrio positivo *(livello appello)*

> [!abstract] Dati
> Si considerano gli investimenti (`inv`) e il PIL (`pil`) trimestrali, entrambi in 100 volte il logaritmo, per cui una variazione di una unità vale un punto. I test ADF di radice unitaria ($H_0$: radice unitaria) hanno p-value ${{e07_11.p_y|m}}$ per `inv` e ${{e07_11.p_x|m}}$ per `pil`; il test di Engle-Granger sui residui della relazione di lungo periodo ($H_0$: assenza di cointegrazione) ha p-value ${{e07_11.p_eg|m}}$. Il modello a correzione dell'errore
>
> $$\Delta\text{inv}_t=\gamma_0+\gamma_1\,\Delta\text{pil}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{inv}_{t-1}-\hat\alpha-\hat\beta\,\text{pil}_{t-1} ,$$
>
> è stimato con OLS su $n = {{e07_11.n}}$ osservazioni (variabile dipendente `d_inv`).
>
> {{e07_11.tab.ecm}}
>
> Si consideri questo scenario: in $t$ gli investimenti sono al di sopra della relazione di lungo periodo, $\text{ecm}_t={{e07_11.d|m}}$; in $t+1$ il PIL cresce di ${{e07_11.g|m}}$ punti, $\Delta\text{pil}_{t+1}={{e07_11.g|m}}$; lo shock $\epsilon_{t+1}$ è nullo e si trascura la costante.

> [!question] Testo della domanda
> **Domanda 11 *(4 punti)*.** **(a)** Il modello è ben definito, cioè bilanciato e con un meccanismo di correzione dell'errore, al livello del 5\%? Si risponda sì o no. **(b)** Quanto vale, in punti, la variazione attesa degli investimenti $\Delta\text{inv}_{t+1}$ nello scenario? **(c)** Di quanto differisce, in punti e con il suo segno, dalla variazione attesa che si avrebbe con $\text{ecm}_t=0$ (a parità di $\Delta\text{pil}_{t+1}$)? **(d)** La variazione attesa nello scenario è inferiore a quella che si avrebbe con $\text{ecm}_t=0$? Si risponda sì o no. **(e)** La variazione attesa degli investimenti in $t+1$ è negativa? Si risponda sì o no.
<!-- /ex -->

<!-- ex e07_12 -->
# Esercizio 12 — Vendite e reddito: un ECM da valutare per intero *(livello appello)*

> [!abstract] Dati
> Si considerano le vendite al dettaglio (`vend`) e il reddito (`red`) trimestrali, indici con un trend crescente. Per ciascuna serie si è stimata la regressione di Dickey-Fuller aumentata con costante, trend lineare e un ritardo, con $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$: si rifiuta $H_0$ se la statistica $t$ del test è minore del valore critico ${{e07_12.cv|m}}$.
>
> {{e07_12.tab.adf}}
>
> Il test di Engle-Granger sui residui della relazione di lungo periodo $\text{vend}_t=\alpha+\beta\,\text{red}_t+u_t$ ($H_0$: assenza di cointegrazione) ha p-value ${{e07_12.p_eg|m}}$. Il modello a correzione dell'errore
>
> $$\Delta\text{vend}_t=\gamma_0+\gamma_1\,\Delta\text{red}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{vend}_{t-1}-\hat\alpha-\hat\beta\,\text{red}_{t-1} ,$$
>
> è stimato con OLS su $n = {{e07_12.n}}$ osservazioni (variabile dipendente `d_vend`).
>
> {{e07_12.tab.ecm}}
>
> La figura riporta l'ACF (in alto) e la PACF (in basso) dei residui del modello, sui primi 12 ritardi, con le bande di confidenza al 95\%; le barre rosse escono dalle bande.
>
> ![ACF e PACF dei residui del modello a correzione dell'errore.]({{e07_12.fig.correlogramma}}){width=85%}
>
> Per l'ultima domanda si ipotizzi che in $t-1$ si osservi un disequilibrio $z_{t-1}=\text{ecm}_{t-1}\neq 0$, che da $t$ in poi il reddito resti costante ($\Delta\text{red}=0$), che tutti gli shock siano nulli e che si trascuri la costante. Il periodo $t$ è il primo periodo di aggiustamento: dopo $k$ periodi di aggiustamento il disequilibrio residuo è $z_{t+k-1}$.

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** **(a)** Si può parlare di una relazione di cointegrazione fra `vend` e `red`, al livello del 5\%? Si risponda sì o no. **(b)** Il modello a correzione dell'errore è ben definito? Si risponda sì o no. **(c)** Occorre ri-specificare la dinamica di breve periodo del modello, sulla base della figura? Si risponda sì o no. **(d)** Qual è il minimo numero intero $k$ di periodi dopo il quale almeno il ${{e07_12.q|m}}\%$ del disequilibrio iniziale è stato assorbito?
<!-- /ex -->

<!-- ex e07_13 -->
# Esercizio 13 — Fatturato e pubblicità: un coefficiente significativo che inganna *(livello appello)*

> [!abstract] Dati
> Su $n = {{e07_13.n_serie}}$ osservazioni mensili si considerano il fatturato di un'impresa (`fatt`) e la sua spesa pubblicitaria (`pub`). Per ciascuna serie si è stimata la regressione di Dickey-Fuller aumentata con costante e un ritardo, con $H_0:\delta=0$ (radice unitaria) contro $H_1:\delta<0$: si rifiuta $H_0$ se la statistica $t$ del test è minore del valore critico ${{e07_13.cv|m}}$.
>
> {{e07_13.tab.adf}}
>
> Il test di Engle-Granger sui residui della relazione di lungo periodo $\text{fatt}_t=\alpha+\beta\,\text{pub}_t+u_t$ ($H_0$: assenza di cointegrazione) ha p-value ${{e07_13.p_eg|m}}$. Il modello a correzione dell'errore
>
> $$\Delta\text{fatt}_t=\gamma_0+\gamma_1\,\Delta\text{pub}_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t ,\qquad \text{ecm}_{t-1}=\text{fatt}_{t-1}-\hat\alpha-\hat\beta\,\text{pub}_{t-1} ,$$
>
> è stimato con OLS (variabile dipendente `d_fatt`).
>
> {{e07_13.tab.ecm}}

> [!question] Testo della domanda
> **Domanda 13 *(4 punti)*.** **(a)** Si può parlare di una relazione di cointegrazione fra `fatt` e `pub`, al livello del 5\%? Si risponda sì o no. **(b)** Al livello del 5\%, in base al p-value stampato, si decida se rifiutare o non rifiutare $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. **(c)** Il modello a correzione dell'errore è ben definito? Si risponda sì o no.
<!-- /ex -->
