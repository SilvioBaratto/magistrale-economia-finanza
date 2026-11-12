{{testo:a03_01}}

## Soluzione della Domanda 1 — Effetto marginale di un'ora di formazione, con e senza finanziamento

> [!tip] Richiamo
> Con il termine $\beta_3\,(\text{ore}\times\text{fin})$ l'effetto di un'ora di formazione dipende dal finanziamento. Da $\Delta\log(y)=\beta_2\,\Delta\text{ore}+\beta_3\,\Delta(\text{ore}\times\text{fin})$ e da $\Delta(\text{ore}\times\text{fin})=\text{fin}\,\Delta\text{ore}$ si ottiene $\Delta\log(y)=(\beta_2+\beta_3\,\text{fin})\,\Delta\text{ore}$: l'effetto vale $\beta_2$ per le aziende non finanziate ($\text{fin}=0$) e $\beta_2+\beta_3$ per quelle finanziate ($\text{fin}=1$), in percentuale $100$ volte tanto. Se $\beta_3=0$ il finanziamento non cambia l'effetto di un'ora: lo si verifica con $H_0:\beta_3=0$ e il rapporto $t$ confrontato con $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) valutano l'effetto marginale delle ore per $\text{fin}=1$ e per $\text{fin}=0$; la (c) è un test su $\beta_3$.
>
> **(a)** $100\,(\hat\beta_2+\hat\beta_3)=100\times\bigl({{a03_01.b2|m}}+({{a03_01.b3|m}})\bigr)={{a03_01.eff_fin|m}}\%$.
>
> **(b)** $100\,\hat\beta_2=100\times({{a03_01.b2|m}})={{a03_01.eff_nofin|m}}\%$.
>
> **(c)** Si verifica $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$. Il rapporto $t$ vale ${{a03_01.t_b3|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Leggere $\hat\beta_2={{a03_01.b2|m}}$ come l'effetto delle ore per tutte le aziende. Con l'interazione $\hat\beta_2$ vale solo per le aziende non finanziate; per quelle finanziate serve $\hat\beta_2+\hat\beta_3$. Un altro errore è dimenticare di moltiplicare per $100$: i coefficienti di un modello con la dipendente in logaritmo sono variazioni relative, non percentuali.

> [!success] Risposta
> **(a)** Per un'azienda finanziata un'ora di formazione in più varia il tasso di scarto di circa ${{a03_01.eff_fin|m}}\%$, cioè lo riduce. **(b)** Per un'azienda non finanziata la variazione è di circa ${{a03_01.eff_nofin|m}}\%$, una riduzione più contenuta. **(c)** Si rifiuta $H_0:\beta_3=0$: l'effetto di un'ora di formazione dipende dal finanziamento, ed è più forte per le aziende finanziate.

![Valori attesi di $\log(\text{scarto})$ al crescere delle ore di formazione: la retta delle aziende finanziate è più ripida, con ${{a03_01.eff_fin|m}}\%$ per ora contro ${{a03_01.eff_nofin|m}}\%$.]({{a03_01.fig.effetto}}){width=85%}

## Soluzione della Domanda 2 — Differenza fra due aziende con finanziamento e ore diversi

> [!tip] Richiamo
> La differenza attesa fra due aziende è la differenza delle medie condizionate. Per A ($\text{fin}=1$, $\text{ore}=h_A$) e B ($\text{fin}=0$, $\text{ore}=h_B$) si ha $(\beta_0+\beta_1+\beta_2h_A+\beta_3h_A)-(\beta_0+\beta_2h_B)=\beta_1+(h_A-h_B)\,\beta_2+h_A\,\beta_3$, una combinazione lineare $\sum_i w_i\beta_i$ con pesi $w=(1,\ h_A-h_B,\ h_A)$. La sua varianza stimata è
> $$\widehat{\text{Var}}=\sum_i w_i^2\,\widehat{\text{Var}}(\hat\beta_i)+2\sum_{i<j}w_iw_j\,\widehat{\text{Cov}}(\hat\beta_i,\hat\beta_j)$$
> e si decide con $t=\text{stima}/\widehat{\text{se}}$ confrontato con $1{,}96$, oppure con l'intervallo di confidenza al 95\%.

> [!example] Svolgimento
> **Impostazione.** Qui $h_A={{a03_01.ore_a|m}}$ e $h_B={{a03_01.ore_b|m}}$, quindi $h_A-h_B={{a03_01.dh|m}}$ e i pesi sono $(1,\ {{a03_01.dh|m}},\ {{a03_01.ore_a|m}})$.
>
> **(a)** $\hat\beta_1+({{a03_01.dh|m}})\,\hat\beta_2+{{a03_01.ore_a|m}}\,\hat\beta_3={{a03_01.b1|m}}+({{a03_01.dh|m}})\times({{a03_01.b2|m}})+{{a03_01.ore_a|m}}\times({{a03_01.b3|m}})={{a03_01.diff|m}}$, cioè $100\times({{a03_01.diff|m}})={{a03_01.diff_pct|m}}\%$.
>
> **(b)** $\widehat{\text{Var}}={{a03_01.s1|m}}^2+({{a03_01.dh|m}})^2\times{{a03_01.s2|m}}^2+{{a03_01.ore_a|m}}^2\times{{a03_01.s3|m}}^2+2\times({{a03_01.dh|m}})\times({{a03_01.c12|m}})+2\times{{a03_01.ore_a|m}}\times({{a03_01.c13|m}})+2\times({{a03_01.dh|m}})\times{{a03_01.ore_a|m}}\times({{a03_01.c23|m}})={{a03_01.var_diff|m}}$, quindi l'errore standard è $100\sqrt{ {{a03_01.var_diff|m}} }={{a03_01.se_diff|m}}$ punti percentuali.
>
> **(c)** Si verifica $H_0:\beta_1+({{a03_01.dh|m}})\,\beta_2+{{a03_01.ore_a|m}}\,\beta_3=0$ contro l'alternativa bilaterale. L'intervallo di confidenza al 95\% è ${{a03_01.diff_pct|m}}\pm 1{,}96\times{{a03_01.se_diff|m}}=[{{a03_01.ic_lo|m}};\,{{a03_01.ic_hi|m}}]$ e contiene lo zero. Lo stesso dice $t={{a03_01.diff_pct|m}}/{{a03_01.se_diff|m}}={{a03_01.t_diff|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.

> [!warning] Errore tipico
> Confrontare A e B con il solo $\hat\beta_1$, che è l'effetto del finanziamento a zero ore di formazione, trascurando che le ore sono diverse e che c'è l'interazione. Il peso di $\beta_3$ è $h_A$ e non $h_A-h_B$: il prodotto $\text{ore}\times\text{fin}$ vale $h_A$ per A e $0$ per B. Ignorare le tre covarianze dà un errore standard di ${{a03_01.se_ing|m}}$ punti invece di ${{a03_01.se_diff|m}}$.

> [!success] Risposta
> **(a)** Il tasso di scarto atteso di A differisce da quello di B di circa ${{a03_01.diff_pct|m}}\%$ (A meno B). **(b)** L'errore standard è ${{a03_01.se_diff|m}}$ punti percentuali. **(c)** Non si rifiuta l'ipotesi di uguaglianza: lo zero cade nell'intervallo di confidenza $[{{a03_01.ic_lo|m}};\,{{a03_01.ic_hi|m}}]$. Un'azienda finanziata con poche ore e una non finanziata con molte ore non si distinguono in modo statisticamente significativo.

![A sinistra i valori attesi di $\log(\text{scarto})$ con le due aziende, A e B, allo stesso livello; a destra l'intervallo di confidenza al 95\% per la loro differenza, in percentuale: lo zero è dentro l'intervallo.]({{a03_01.fig.profili}}){width=85%}

## Soluzione della Domanda 3 — Un'affermazione sull'effetto di più ore di formazione

> [!tip] Richiamo
> Per un'affermazione su un multiplo di un coefficiente, $H_0:k\,\beta=q$, il rapporto $t$ è $t=(k\,\hat\beta-q)/(k\,\widehat{\text{se}}(\hat\beta))$, da confrontare con $1{,}96$. Con la dipendente in logaritmo una variazione $\Delta x=k$ del regressore dà $\Delta\%\,y\approx 100\,\beta\,k$, quindi una riduzione del $r\%$ equivale a $k\beta=-r/100$. Per un'azienda non finanziata ($\text{fin}=0$) l'effetto delle ore è $\beta_2$.

> [!example] Svolgimento
> **Impostazione.** Con $k={{a03_01.ore3|m}}$ ore l'affermazione è $H_0:{{a03_01.ore3|m}}\,\beta_2=-{{a03_01.riv3|m}}/100$, cioè $\beta_2={{a03_01.beta2_riv|m}}$. La stima è $100\times{{a03_01.ore3|m}}\times({{a03_01.b2|m}})={{a03_01.stima3|m}}\%$.
>
> **(a)** $t=\dfrac{ {{a03_01.ore3|m}}\times({{a03_01.b2|m}})+{{a03_01.riv3|m}}/100 }{ {{a03_01.ore3|m}}\times{{a03_01.s2|m}} }={{a03_01.t3|m}}$.
>
> **(b)** $|t|>1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Dimenticare il fattore ${{a03_01.ore3|m}}$ confrontando $\hat\beta_2$ con $-{{a03_01.riv3|m}}/100$, oppure confrontare $\hat\beta_2$ con $-{{a03_01.riv3|m}}$ senza dividere per $100$. Un altro errore è dimenticare che $k$ moltiplica anche l'errore standard: $\widehat{\text{se}}(k\hat\beta_2)=k\,\widehat{\text{se}}(\hat\beta_2)$.

> [!success] Risposta
> **(a)** $t={{a03_01.t3|m}}$. **(b)** Si rifiuta $H_0$: nelle aziende non finanziate ${{a03_01.ore3|m}}$ ore di formazione in più comportano una variazione dello scarto di circa ${{a03_01.stima3|m}}\%$, non di $-{{a03_01.riv3|m}}\%$ come sostiene il responsabile.

![Intervallo di confidenza al 95\% per la variazione attesa dello scarto dovuta a ${{a03_01.ore3|m}}$ ore in più: il valore sostenuto, $-{{a03_01.riv3|m}}\%$, è fuori dall'intervallo.]({{a03_01.fig.affermazione}}){width=85%}

## Soluzione della Domanda 4 — Che cosa dice il grafico dei residui

> [!tip] Richiamo
> L'omoschedasticità richiede $\text{Var}(\epsilon_i\mid X)=\sigma^2$ uguale per ogni osservazione. I residui sono la proxy osservabile degli errori, quindi il grafico dei residui contro i valori predetti deve mostrare una fascia orizzontale di ampiezza costante attorno allo zero. Se l'ampiezza cresce o diminuisce con $\hat y$, la varianza dipende dai regressori: c'è eteroschedasticità. Gli stimatori OLS restano non distorti, ma gli errori standard usuali non sono più consistenti e i test $t$ che li usano non sono affidabili; si usano gli errori standard robusti.

> [!example] Svolgimento
> **Impostazione.** Si guarda l'ampiezza verticale dei residui al variare di $\hat y$: la media complessiva dei residui è zero per costruzione (con la costante); per l'omoschedasticità conta l'ampiezza della dispersione, mentre un andamento sistematico della posizione dei residui segnalerebbe non linearità.
>
> **(a)** I residui sono poco dispersi per i valori predetti piccoli e sempre più dispersi al crescere di $\hat y$: è una forma a ventaglio. La deviazione standard dei residui nel quarto quartile dei valori predetti è ${{a03_01.sd4|m}}$, circa ${{a03_01.rapporto|m}}$ volte quella del primo quartile (${{a03_01.sd1|m}}$). La varianza non è costante.
>
> **(b)** Con la varianza che dipende da $\hat y$, gli errori standard usuali non stimano correttamente la variabilità degli stimatori: non sono affidabili.

> [!warning] Errore tipico
> Guardare la posizione dei residui invece della loro ampiezza: la media complessiva dei residui è zero per costruzione (con la costante), mentre per l'omoschedasticità conta l'ampiezza della dispersione; un andamento sistematico della posizione dei residui segnalerebbe invece non linearità. Un altro errore è pensare che gli errori standard robusti usati nelle tabelle siano superflui: proprio questo grafico li giustifica.

> [!success] Risposta
> **(a)** No: la dispersione dei residui aumenta con i valori predetti (ventaglio), quindi la varianza non sembra costante. **(b)** No: con l'eteroschedasticità gli errori standard usuali non sono consistenti; servono quelli robusti, già usati nelle stime.

![Deviazione standard dei residui in ciascun quartile dei valori predetti: nel quarto quartile vale circa ${{a03_01.rapporto|m}}$ volte quella del primo.]({{a03_01.fig.quartili}}){width=85%}

## Soluzione della Domanda 5 — Il Modello 1 omette la dimensione aziendale?

> [!tip] Richiamo
> Se il modello completo ha il regressore omesso $z$ con coefficiente $\beta_z$ e si stima il modello senza di esso, la stima di ogni altro coefficiente cambia di $\tilde\beta_j=\hat\beta_j+\hat\beta_z\,\hat\delta_j$, dove $\hat\delta_j$ è il coefficiente di $x_j$ nella regressione di $z$ sui regressori inclusi: nel campione è un'identità esatta. C'è distorsione da variabile omessa su $\beta_j$ soltanto se valgono **entrambe** le condizioni: $z$ conta ($\beta_z\neq 0$) e $z$ è correlata con $x_j$ ($\delta_j\neq 0$).

> [!example] Svolgimento
> **Impostazione.** Si confrontano le stime di $\beta_2$ nei due modelli e si usa la regressione ausiliaria per capire da dove viene la differenza.
>
> **(a)** $100\,(\tilde\beta_2-\hat\beta_2)=100\times\bigl(({{a03_01.b2_m1|m}})-({{a03_01.b2_m2|m}})\bigr)={{a03_01.cambio|m}}$ punti percentuali.
>
> **(b)** Nel Modello 2 il rapporto $t$ di $\beta_4$ vale ${{a03_01.t_lv|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_4=0$, quindi la dimensione aziendale conta.
>
> **(c)** Nella regressione ausiliaria $\hat\delta_2={{a03_01.delta|m}}$ con $t={{a03_01.t_delta|m}}$, in valore assoluto maggiore di $1{,}96$: `l_vendite` è correlata con `ore`. Valgono entrambe le condizioni, quindi la stima di $\beta_2$ nel Modello 1 è distorta. Come verifica, $100\,\hat\beta_4\,\hat\delta_2=100\times({{a03_01.b_lv|m}})\times{{a03_01.delta|m}}={{a03_01.prodotto|m}}$ punti percentuali, uguale alla differenza in (a).

> [!warning] Errore tipico
> Concludere per la distorsione solo perché la stima cambia, senza controllare che la variabile omessa sia rilevante nel modello completo e correlata con il regressore in esame. Oppure presentare il Modello 2 come privo di distorsione: potrebbero mancare altre variabili.

> [!success] Risposta
> **(a)** $100\,(\tilde\beta_2-\hat\beta_2)={{a03_01.cambio|m}}$ punti percentuali: il Modello 1 stima per le ore un effetto più negativo di quello del Modello 2. **(b)** Si rifiuta $H_0:\beta_4=0$. **(c)** Sì: `l_vendite` è significativa e correlata con `ore`, quindi il Modello 1 attribuisce alle ore un effetto che in parte è della dimensione aziendale.

![Coefficiente di `ore`, con intervallo al 95\%: senza vendite (Modello 1) e con vendite (Modello 2).]({{a03_01.fig.confronto}}){width=85%}

## Soluzione della Domanda 6 — Una giornata di formazione in punti di scarto

> [!tip] Richiamo
> Per $\text{fin}=0$ la variazione di $\log(\text{scarto})$ dovuta a $\Delta\text{ore}$ ore è $\beta_2\,\Delta\text{ore}$. Il coefficiente è una variazione relativa per ora; per esprimere l'effetto in punti di scarto (pezzi difettosi su 100) lo si moltiplica per il livello di partenza, $\Delta\text{scarto}\approx\text{scarto}_0\,\beta_2\,\Delta\text{ore}$. Una giornata vale ${{a03_01.giornata|m}}$ ore, quindi $\Delta\text{ore}={{a03_01.giornata|m}}$. L'affermazione di una variazione di $q$ punti è $H_0:\text{scarto}_0\,\Delta\text{ore}\,\beta_2=q$ e $t=(\text{stima}-q)/\widehat{\text{se}}$ con la stima e l'errore standard nella stessa unità.

> [!example] Svolgimento
> **Impostazione.** Il coefficiente è per ora e in termini relativi, l'affermazione è per giornata e in punti: bisogna convertire entrambe le unità, con il fattore ${{a03_01.giornata|m}}\times{{a03_01.s0|m}}$.
>
> **(a)** Nel Modello 2, $\hat\beta_2={{a03_01.b2p|m}}$ e $\Delta\widehat{\text{scarto}}\approx{{a03_01.s0|m}}\times{{a03_01.giornata|m}}\times({{a03_01.b2p|m}})={{a03_01.eff6|m}}$ punti.
>
> **(b)** L'affermazione è $H_0:{{a03_01.giornata|m}}\times{{a03_01.s0|m}}\times\beta_2=-{{a03_01.c6|m}}$, cioè $\beta_2={{a03_01.beta6_riv|m}}$. L'errore standard in punti è ${{a03_01.giornata|m}}\times{{a03_01.s0|m}}\times{{a03_01.s2p|m}}={{a03_01.se6|m}}$ e
> $$t=\frac{ {{a03_01.eff6|m}}-(-{{a03_01.c6|m}}) }{ {{a03_01.se6|m}} }={{a03_01.t6|m}},$$
> in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.

> [!warning] Errore tipico
> Trascurare le unità. Tradurre l'affermazione come se fosse per ora anziché per giornata porta a un rapporto $t$ di circa ${{a03_01.t6_ora|m}}$ e a rifiutare a torto $H_0$; confrontare direttamente $\hat\beta_2$ con $-{{a03_01.c6|m}}$ sbaglierebbe ancora di più. Il coefficiente è una variazione relativa per ora, l'affermazione è una variazione in punti per giornata.

> [!success] Risposta
> **(a)** Una giornata di formazione in più riduce lo scarto di circa ${{a03_01.eff6|m}}$ punti (da ${{a03_01.s0|m}}$). **(b)** Non si rifiuta $H_0$: con le unità allineate l'affermazione del consulente (${{a03_01.c6|m}}$ punti in meno) è compatibile con i dati.

![Intervallo di confidenza al 95\% per la variazione attesa dello scarto dovuta a una giornata di formazione, in punti: il valore sostenuto, $-{{a03_01.c6|m}}$, è dentro l'intervallo.]({{a03_01.fig.giornata}}){width=85%}

{{testo:a03_02}}

## Soluzione della Domanda 7 — La regressione di Dickey-Fuller adatta alle due serie

> [!tip] Richiamo
> Nel test di Dickey-Fuller la componente deterministica si sceglie dal grafico: se la serie non ha un andamento tendenziale netto basta la costante; se ha un trend lineare netto si usano costante e trend, perché sotto $H_0$ il trend è il drift del random walk e sotto $H_1$ la serie è stazionaria attorno a una retta. Se $y_t$ è un AR($p$), la regressione aumentata ha $p-1$ ritardi della differenza. I coefficienti sono dunque la costante, l'eventuale trend, il livello ritardato $y_{t-1}$ e i $p-1$ ritardi. Il valore critico dipende dalla regressione: ${{a03_02.cv_c|m}}$ con la sola costante, ${{a03_02.cv_t|m}}$ con costante e trend.

> [!example] Svolgimento
> **Impostazione.** La (a) si decide dal grafico, la (b) conta i termini, la (c) sceglie il valore critico della regressione scelta.
>
> **(a)** Entrambe le serie salgono in modo netto lungo tutto il campione, con una pendenza media costante: c'è un trend lineare, quindi la regressione contiene costante e trend.
>
> **(b)** Con $p={{a03_02.p|m}}$ servono $p-1={{a03_02.ritardi|m}}$ ritardi della differenza. I coefficienti sono la costante, il trend, il livello ritardato e i ${{a03_02.ritardi|m}}$ ritardi: $3+(p-1)=3+({{a03_02.p|m}}-1)={{a03_02.n_coef|m}}$.
>
> **(c)** La regressione include costante e trend, quindi il valore critico è ${{a03_02.crit|m}}$.

> [!warning] Errore tipico
> Omettere il trend: se la serie è stazionaria attorno a una retta, un test con la sola costante tende a non rifiutare la radice unitaria. Un errore collegato è usare il valore critico ${{a03_02.cv_c|m}}$ della sola costante con una regressione che contiene anche il trend, e contare i ritardi come $p$ invece che $p-1$.

> [!success] Risposta
> **(a)** Sì: le serie hanno un trend lineare netto, la regressione ha costante e trend. **(b)** ${{a03_02.n_coef|m}}$ coefficienti: costante, trend, livello ritardato e ${{a03_02.ritardi|m}}$ ritardi della differenza. **(c)** ${{a03_02.crit|m}}$, il valore critico per la regressione con costante e trend.

![Le due serie con la retta di trend (tratteggiata) che la regressione di Dickey-Fuller deve contenere.]({{a03_02.fig.trend}}){width=85%}

## Soluzione della Domanda 8 — Le serie sono cointegrate?

> [!tip] Richiamo
> Il test di Dickey-Fuller ha $H_0:\delta=0$ (radice unitaria) e si rifiuta se $t$ è minore del valore critico (qui ${{a03_02.crit|m}}$): non rifiutare significa che la serie va trattata come non stazionaria. Si parla di cointegrazione se le serie sono non stazionarie e i residui della relazione di lungo periodo $y_t-\hat\alpha-\hat\beta x_t$ sono stazionari: il test di Engle-Granger ha $H_0$ di assenza di cointegrazione (residui con radice unitaria) e si rifiuta se il p-value è minore di $0{,}05$.

> [!example] Svolgimento
> **Impostazione.** Si guardano le due statistiche ADF, poi il p-value di Engle-Granger.
>
> **(a)** Per `pil_a` $t={{a03_02.t_a|m}}$, maggiore di ${{a03_02.crit|m}}$: non si rifiuta $H_0$, la serie è non stazionaria.
>
> **(b)** Per `pil_b` $t={{a03_02.t_b|m}}$, maggiore di ${{a03_02.crit|m}}$: non si rifiuta $H_0$, la serie è non stazionaria.
>
> **(c)** Il p-value di Engle-Granger è ${{a03_02.p_eg|m}}<0{,}05$: si rifiuta l'ipotesi di assenza di cointegrazione, i residui sono stazionari.
>
> **(d)** Le due serie sono non stazionarie e i residui di lungo periodo sono stazionari: c'è cointegrazione.

> [!warning] Errore tipico
> Confrontare le statistiche ADF con $\pm 1{,}96$, che vale per i test sui coefficienti e non per la radice unitaria, oppure con ${{a03_02.cv_c|m}}$, che vale senza trend. Un altro errore è leggere il p-value di Engle-Granger al contrario: qui rifiutare $H_0$ è la conclusione favorevole alla cointegrazione.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0$: `pil_a` è non stazionaria. **(b)** Non si rifiuta $H_0$: `pil_b` è non stazionaria. **(c)** Si rifiuta: il p-value ${{a03_02.p_eg|m}}$ è minore di $0{,}05$. **(d)** Sì: serie non stazionarie con residui di lungo periodo stazionari, cioè cointegrate.

![Le due statistiche ADF contro i valori critici (a sinistra) e il p-value di Engle-Granger contro la soglia del 5\% (a destra).]({{a03_02.fig.test}}){width=85%}

## Soluzione della Domanda 9 — I residui dell'ECM chiedono più dinamica di breve periodo

> [!tip] Richiamo
> Un modello a correzione dell'errore è ben definito se è bilanciato, cioè con variabili dello stesso ordine di integrazione ($\Delta y_t$, $\Delta x_t$ ed $\text{ecm}_{t-1}$ sono $I(0)$ quando le serie sono cointegrate), e se ha un meccanismo di correzione, cioè $\hat\lambda<0$ e significativo. I residui devono essere incorrelati. Se l'autocorrelazione è concentrata nei primi ritardi (ACF e PACF con il valore più alto al primo ritardo, fuori dalle bande $\pm1{,}96/\sqrt{n}$, e poi dentro le bande) manca dinamica di breve periodo: si aggiungono ritardi di $\Delta y$ e di $\Delta x$. La relazione di lungo periodo va rivista soltanto se la cointegrazione non regge o se l'ACF decade lentamente come in una radice unitaria.

> [!example] Svolgimento
> **Impostazione.** Si controlla la specificazione del modello, poi si legge la figura.
>
> **(a)** Per la Domanda 8 le serie sono cointegrate, e $\hat\lambda={{a03_02.lam|m}}$ è negativo con $t={{a03_02.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: il modello è ben definito. Il bilanciamento è dato dal test di Engle-Granger, mentre la significatività di $\hat\lambda$, con residui autocorrelati, va confermata dopo la ri-specificazione.
>
> **(b)** La banda è $\pm1{,}96/\sqrt{n}=\pm1{,}96/\sqrt{ {{a03_02.n_ecm|m}} }=\pm{{a03_02.banda|m}}$. Il primo ritardo dell'ACF vale circa ${{a03_02.rho1|m}}$ ed è fuori dalla banda; il numero di ritardi fuori dalle bande è ${{a03_02.fuori|m}}$ su $12$.
>
> **(c)** Sì: ACF e PACF hanno il valore più alto al primo ritardo e dal terzo ritardo in poi restano dentro le bande, cioè l'autocorrelazione è di basso ordine. Manca dinamica di breve periodo: si aggiungono $\Delta\text{pil\_a}_{t-1}$ e $\Delta\text{pil\_b}_{t-1}$.
>
> **(d)** No: il p-value di Engle-Granger ${{a03_02.p_eg|m}}$ è minore di $0{,}05$ e $\hat\lambda$ è negativo e significativo; l'ACF non decade lentamente. La relazione di lungo periodo regge.

> [!warning] Errore tipico
> Dedurre dalla significatività di $\hat\lambda$ che il modello sia ben specificato: i residui autocorrelati chiedono comunque più dinamica di breve periodo. Un altro errore è rispondere che va rivista la relazione di lungo periodo ogni volta che il correlogramma dei residui non è pulito: serve un'ACF che decade lentamente, non una struttura nei primi ritardi.

> [!success] Risposta
> **(a)** Sì: serie cointegrate (il bilanciamento dipende dal test di Engle-Granger) e $\hat\lambda$ negativo e significativo, da confermare dopo la ri-specificazione. **(b)** Ritardi dell'ACF fuori dalle bande: ${{a03_02.fuori|m}}$ su $12$. **(c)** Sì: l'autocorrelazione di basso ordine segnala una dinamica di breve periodo omessa. **(d)** No: la cointegrazione regge e l'ACF non decade lentamente.

![Ogni residuo dell'ECM contro il precedente: la pendenza della retta, circa ${{a03_02.rho1|m}}$, è la prima autocorrelazione che esce dalla banda.]({{a03_02.fig.ritardo}}){width=85%}

## Soluzione della Domanda 10 — Dopo un disequilibrio positivo

> [!tip] Richiamo
> Nel modello $\Delta y_t=\gamma_0+\gamma_1\Delta x_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t$ la variazione attesa di $y$ in $t+1$ è $\gamma_0+\gamma_1\Delta x_{t+1}+\lambda\,\text{ecm}_t$. A parità di $\Delta x_{t+1}$ e con shock nullo, la differenza rispetto al caso $\text{ecm}_t=0$ è $\lambda\,\text{ecm}_t$: con $\lambda<0$ un disequilibrio positivo ($y$ sopra la relazione di lungo periodo) riduce la crescita, uno negativo la aumenta. Con $\Delta x_{t+1}=0$, costante e shock nulli, $\text{ecm}_{t+1}=(1+\lambda)\,\text{ecm}_t$: nel periodo si assorbe la quota $-\lambda$ del disequilibrio.

> [!example] Svolgimento
> **Impostazione.** Si usa il segno di $\hat\lambda\,\text{ecm}_t$.
>
> **(a)** $\hat\lambda\,\text{ecm}_t=({{a03_02.lam|m}})\times{{a03_02.d|m}}$ è negativo: la variazione attesa è inferiore a quella con $\text{ecm}_t=0$.
>
> **(b)** $\hat\lambda\,\text{ecm}_t=({{a03_02.lam|m}})\times{{a03_02.d|m}}={{a03_02.delta|m}}$ punti.
>
> **(c)** La quota assorbita è $-100\,\hat\lambda=-100\times({{a03_02.lam|m}})={{a03_02.quota|m}}\%$: resta la frazione $1+\hat\lambda={{a03_02.resto|m}}$ del disequilibrio.

> [!warning] Errore tipico
> Dedurre dal disequilibrio positivo che `pil_a` cresca più in fretta: il segno negativo di $\hat\lambda$ lo inverte, e `pil_a` torna verso la relazione di lungo periodo crescendo più lentamente. Un altro errore è leggere $\hat\lambda$ come variazione in punti percentuali anziché come frazione del disequilibrio assorbita in ogni periodo.

> [!success] Risposta
> **(a)** Sì: la crescita attesa è inferiore a quella in equilibrio. **(b)** Di ${{a03_02.delta|m}}$ punti. **(c)** Circa il ${{a03_02.quota|m}}\%$ del disequilibrio è assorbito in un periodo.

![Effetto del disequilibrio sulla variazione attesa di `pil_a`: la retta $\hat\lambda\,\text{ecm}_t$ ha pendenza negativa; per $\text{ecm}_t={{a03_02.d|m}}$ vale ${{a03_02.delta|m}}$.]({{a03_02.fig.effetto}}){width=85%}
