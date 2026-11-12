{{testo:a01_01}}

## Soluzione della Domanda 1 — Effetti percentuali in un modello log-livello

> [!tip] Richiamo
> Con la dipendente in logaritmo, una variazione $\Delta x$ del regressore dà $\Delta\log(y)=\beta\,\Delta x$ e, poiché $\Delta\log(y)\approx\Delta y/y$, la variazione percentuale attesa è $100\cdot\beta\,\Delta x$. Per una dummy $\Delta x=1$ (si passa da non proprietario a proprietario). Per ottenere una variazione relativa data $p/100$ si inverte la formula: $\Delta x=(p/100)/\beta$.

> [!example] Svolgimento
> **Impostazione.** `spesa` è in logaritmo: i coefficienti di `proprietario` e di `eta` si leggono come variazioni relative della spesa.
>
> **(a)** $\Delta\%\,\text{spesa}\approx 100\times\hat\beta_4=100\times{{a01_01.b_prop|m}}={{a01_01.pct|m}}\%$.
>
> **(b)** Si cerca $\Delta\text{eta}$ tale che $\hat\beta_3\,\Delta\text{eta}=-{{a01_01.obiettivo|m}}/100$, quindi $\Delta\text{eta}=\dfrac{ -{{a01_01.obiettivo|m}}/100 }{ {{a01_01.b_eta|m}} }={{a01_01.anni|m}}$ anni.

> [!warning] Errore tipico
> Leggere $\hat\beta_4={{a01_01.b_prop|m}}$ come se fosse già una percentuale: con la dipendente in logaritmo il coefficiente è una variazione in punti di $\log$ e va moltiplicato per $100$. Nella (b) l'errore speculare è usare ${{a01_01.obiettivo|m}}$ al posto di ${{a01_01.obiettivo|m}}/100$, che dà un'età cento volte troppo grande. Il segno: l'età deve *aumentare*, e la risposta è positiva perché sono negativi sia $\hat\beta_3$ sia la variazione richiesta.

> [!success] Risposta
> **(a)** Un proprietario spende in media circa il ${{a01_01.pct|m}}\%$ in più di un non proprietario con lo stesso reddito e la stessa età; la stima è quella indicata, ma non è significativamente diversa da zero ($t={{a01_01.t_prop|m}}$). **(b)** Servono circa ${{a01_01.anni|m}}$ anni in più perché la spesa attesa si riduca del ${{a01_01.obiettivo|m}}\%$.

![Spesa attesa, in logaritmo, al variare dell'età per i due gruppi, a reddito medio: la distanza verticale fra le rette è l'effetto di `proprietario` (${{a01_01.pct|m}}\%$), la pendenza dà ${{a01_01.stima|m}}\%$ ogni ${{a01_01.dx|m}}$ anni.]({{a01_01.fig.effetti}}){width=85%}

## Soluzione della Domanda 2 — Intervallo di confidenza per un effetto percentuale

> [!tip] Richiamo
> Se $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$ è l'intervallo di confidenza al 95\% per $\beta$, moltiplicando stima ed errore standard per la costante $c=100\cdot\Delta x$ si ottiene l'intervallo per $c\,\beta$, la variazione percentuale attesa dovuta a $\Delta x$ unità del regressore. Un valore è compatibile con i dati, al 5\%, se cade nell'intervallo; equivalentemente se $|t|=|\text{(stima}-\text{valore)}/\text{se}|<1{,}96$.

> [!example] Svolgimento
> **Impostazione.** Si costruisce l'intervallo per $c\,\beta_3$ con $c=100\cdot{{a01_01.dx|m}}$ e lo si confronta con il valore sostenuto dalla rivista.
>
> **(a), (b)** Stima: $c\,\hat\beta_3=100\times{{a01_01.dx|m}}\times({{a01_01.b_eta|m}})={{a01_01.stima|m}}$. Errore standard: $c\,\widehat{\text{se}}(\hat\beta_3)=100\times{{a01_01.dx|m}}\times{{a01_01.se_eta|m}}={{a01_01.se_pct|m}}$. Intervallo al 95\%: ${{a01_01.stima|m}}\pm 1{,}96\times{{a01_01.se_pct|m}}=[{{a01_01.ic_lo|m}};\,{{a01_01.ic_hi|m}}]$.
>
> **(c)** L'affermazione è $c\,\beta_3=-{{a01_01.rid|m}}$. Il valore $-{{a01_01.rid|m}}$ sta a sinistra dell'estremo inferiore ${{a01_01.ic_lo|m}}$, quindi fuori dall'intervallo. Lo stesso dice $t=({{a01_01.stima|m}}+{{a01_01.rid|m}})/{{a01_01.se_pct|m}}={{a01_01.t_riv|m}}$, in valore assoluto maggiore di $1{,}96$.

> [!warning] Errore tipico
> Costruire l'intervallo per $\beta_3$ e confrontarlo con ${{a01_01.rid|m}}\%$ senza cambiare scala: l'affermazione riguarda ${{a01_01.dx|m}}$ anni e una percentuale, mentre $\beta_3$ è per un anno e in punti di $\log$. Un altro errore è moltiplicare la stima per $c$ e non l'errore standard, ottenendo un intervallo troppo stretto.

> [!success] Risposta
> **(a)** L'estremo inferiore è ${{a01_01.ic_lo|m}}$. **(b)** L'estremo superiore è ${{a01_01.ic_hi|m}}$. **(c)** No: l'intervallo di confidenza al 95\% per la variazione percentuale dovuta a ${{a01_01.dx|m}}$ anni in più è $[{{a01_01.ic_lo|m}};\,{{a01_01.ic_hi|m}}]$ e non contiene $-{{a01_01.rid|m}}$, quindi l'affermazione non è compatibile con i dati.

![Intervallo di confidenza al 95\% per la variazione percentuale attesa a ${{a01_01.dx|m}}$ anni in più, $[{{a01_01.ic_lo|m}};\,{{a01_01.ic_hi|m}}]$: il valore $-{{a01_01.rid|m}}$ cade fuori.]({{a01_01.fig.ic}}){width=85%}

## Soluzione della Domanda 3 — Il termine quadratico e la curvatura

> [!tip] Richiamo
> Il termine al quadrato misura la curvatura della relazione. Per decidere se è lineare si verifica $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$ con il rapporto $t=\hat\beta_2/\widehat{\text{se}}(\hat\beta_2)$: si rifiuta se $|t|>1{,}96$. Con $x$ e $x^2$ nel modello l'effetto marginale è $\beta_1+2\beta_2x$, una retta in $x$ di pendenza $2\beta_2$: decrescente se $\beta_2<0$, crescente se $\beta_2>0$.

> [!example] Svolgimento
> **Impostazione.** La (a) è un test bilaterale su $\beta_2$; la (b) legge il segno di $\beta_2$ una volta accertato che il termine conta.
>
> **(a)** $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. Il rapporto $t$ vale ${{a01_01.t_sq|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** Il termine al quadrato è significativo e $\hat\beta_2={{a01_01.b_sq|m}}<0$: la pendenza dell'effetto marginale, $2\hat\beta_2$, è negativa.

> [!warning] Errore tipico
> Guardare il segno di $\hat\beta_1={{a01_01.b_red|m}}$, positivo, e concludere che l'effetto è crescente: la dipendenza dell'effetto marginale dal reddito passa da $2\beta_2$, non da $\beta_1$. Un altro errore è rispondere «sì» alla (b) anche quando il test della (a) non rifiuta: se $\beta_2$ non è significativo, la decrescenza stimata non è statisticamente sostenuta.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: il termine al quadrato è significativo al 5\% e la relazione non è lineare. **(b)** Sì: poiché $\hat\beta_2<0$ e significativo, l'effetto marginale del reddito è decrescente.

![Rapporto $t$ del termine al quadrato, ${{a01_01.t_sq|m}}$, nella regione di rifiuto $|t|>1{,}96$ del test bilaterale al 5\%.]({{a01_01.fig.test_sq}}){width=85%}

## Soluzione della Domanda 4 — Effetto marginale e punto di svolta

> [!tip] Richiamo
> Da $\Delta\log(y)=\beta_1\,\Delta x+\beta_2\,\Delta(x^2)$ e $\Delta(x^2)\approx 2x\,\Delta x$ si ottiene l'effetto marginale $\Delta\log(y)\approx(\beta_1+2\beta_2x)\,\Delta x$, in percentuale $100\,(\beta_1+2\beta_2x)$ per $\Delta x=1$. Si annulla in $x^*=-\beta_1/(2\beta_2)$: con $\beta_2<0$ è positivo prima di $x^*$ e negativo dopo. Se $x^*$ cade fuori dal campo osservato del regressore, è un'estrapolazione.

> [!example] Svolgimento
> **Impostazione.** La (a) valuta l'effetto marginale in un punto, la (b) cerca dove si annulla, la (c) lo confronta con il campo osservato.
>
> **(a)** $100\,(\hat\beta_1+2\hat\beta_2\,x_0)=100\times\bigl({{a01_01.b_red|m}}+2\times({{a01_01.b_sq|m}})\times{{a01_01.r0|m}}\bigr)={{a01_01.eff|m}}\%$ per un aumento di una unità di `reddito`.
>
> **(b)** $x^*=-\hat\beta_1/(2\hat\beta_2)=-{{a01_01.b_red|m}}\,/\,\bigl(2\times({{a01_01.b_sq|m}})\bigr)={{a01_01.punto|m}}$, in decine di migliaia di dollari: circa {{a01_01.punto_mila}} mila dollari di reddito.
>
> **(c)** Il reddito osservato va da ${{a01_01.rmin|m}}$ a ${{a01_01.rmax|m}}$ e ${{a01_01.punto|m}}$ sta in questo intervallo.

> [!warning] Errore tipico
> Leggere $\hat\beta_1$ da solo come effetto del reddito: con il termine al quadrato nel modello l'effetto è $\hat\beta_1+2\hat\beta_2x$ e cambia con $x$. Un altro errore è dimenticare il fattore $2$ nel punto di svolta, calcolando $-\hat\beta_1/\hat\beta_2$, oppure lasciare il risultato in decine di migliaia di dollari quando si parla di dollari.

> [!success] Risposta
> **(a)** Con reddito ${{a01_01.r0|m}}$ un'unità di reddito in più fa aumentare la spesa attesa di circa il ${{a01_01.eff|m}}\%$. **(b)** L'effetto marginale si annulla per un reddito di ${{a01_01.punto|m}}$, cioè circa {{a01_01.punto_mila}} mila dollari: prima la spesa cresce con il reddito, poi decresce. **(c)** Sì: ${{a01_01.punto|m}}$ cade nel campo osservato, da ${{a01_01.rmin|m}}$ a ${{a01_01.rmax|m}}$.

![Effetto marginale del reddito, $\hat\beta_1+2\hat\beta_2\,\text{reddito}$: vale ${{a01_01.eff|m}}\%$ in reddito ${{a01_01.r0|m}}$ e si annulla in ${{a01_01.punto|m}}$; la fascia grigia è il campo osservato.]({{a01_01.fig.svolta}}){width=85%}

## Soluzione della Domanda 5 — Quasi-collinearità: che cosa spiega e che cosa no

> [!tip] Richiamo
> Il fattore di inflazione della varianza è $\text{VIF}_j=1/(1-R_j^2)$, dove $R_j^2$ è l'$R^2$ della regressione di $x_j$ sugli altri regressori. Con un VIF maggiore di $10$ si parla di quasi-collinearità. La quasi-collinearità gonfia l'errore standard del coefficiente del regressore coinvolto e ne abbassa la statistica $t$: può dunque spiegare la non significatività di un coefficiente solo se il VIF di *quel* regressore è alto.

> [!example] Svolgimento
> **Impostazione.** La (a) confronta ogni VIF con la soglia $10$; la (b) incrocia il VIF di `proprietario` con la sua significatività.
>
> **(a)** I VIF di `reddito` (${{a01_01.vif_red|m}}$) e di `sq_reddito` (${{a01_01.vif_sq|m}}$) superano $10$; gli altri stanno sotto soglia e il più alto è ${{a01_01.resto|m}}$. I regressori sopra soglia sono ${{a01_01.conta|m}}$.
>
> **(b)** Il coefficiente di `proprietario` ha $t={{a01_01.t_prop|m}}$, in valore assoluto minore di $1{,}96$: non è significativo. Il suo VIF è ${{a01_01.vif_prop|m}}$, molto sotto $10$: `proprietario` è quasi incorrelato con gli altri regressori e il suo errore standard non è gonfiato.

> [!warning] Errore tipico
> Rispondere «sì» alla (b) perché nella tabella c'è collinearità: quella fra `reddito` e `sq_reddito` è strutturale, dato che la seconda è il quadrato della prima, e riguarda i due coefficienti di reddito, non quello di `proprietario`. La non significatività di `proprietario` ha un'altra origine: l'effetto stimato è piccolo rispetto alla sua incertezza.

> [!success] Risposta
> **(a)** Due regressori hanno un VIF superiore a $10$: `reddito` e `sq_reddito`. **(b)** No: il VIF di `proprietario` è ${{a01_01.vif_prop|m}}$, quindi la quasi-collinearità non può spiegare la non significatività del suo coefficiente.

![VIF di ogni regressore con la soglia $10$ tratteggiata: in rosso i due regressori sopra soglia, `reddito` e `sq_reddito`.]({{a01_01.fig.vif}}){width=85%}

## Soluzione della Domanda 6 — Di quanto è gonfiato l'errore standard

> [!tip] Richiamo
> Per lo stimatore di $\beta_j$ vale $\widehat{\text{Var}}(\hat\beta_j)=\dfrac{\hat\sigma^2}{\sum_i(x_{ij}-\bar x_j)^2}\cdot\dfrac{1}{1-R_j^2}$ e il secondo fattore è il $\text{VIF}_j$. Nel caso ideale di regressori incorrelati ($R_j^2=0$) il fattore vale $1$: rispetto a esso la varianza è moltiplicata per il VIF e l'errore standard per $\sqrt{\text{VIF}_j}$.

> [!example] Svolgimento
> **Impostazione.** L'inflazione dell'errore standard è la radice quadrata del VIF del regressore.
>
> **(a)** $\sqrt{\text{VIF}(\text{reddito})}=\sqrt{ {{a01_01.vif_red|m}} }={{a01_01.f_red|m}}$.
>
> **(b)** $\sqrt{\text{VIF}(\text{sq\_reddito})}=\sqrt{ {{a01_01.vif_sq|m}} }={{a01_01.f_sq|m}}$.
>
> Per `reddito` l'errore standard stimato è ${{a01_01.se_red|m}}$; con regressori indipendenti sarebbe ${{a01_01.se_red|m}}/{{a01_01.f_red|m}}={{a01_01.se_ideale|m}}$.

> [!warning] Errore tipico
> Rispondere ${{a01_01.vif_red|m}}$ volte, cioè il VIF stesso: il VIF moltiplica la varianza, e l'errore standard ne è la radice. Un altro errore è dedurre dal VIF alto che le stime siano distorte: la quasi-collinearità gonfia soltanto gli errori standard e, qui, i due coefficienti restano comunque significativi ($t={{a01_01.t_red|m}}$ e $t={{a01_01.t_sq|m}}$).

> [!success] Risposta
> **(a)** L'errore standard del coefficiente di `reddito` è gonfiato di circa ${{a01_01.f_red|m}}$ volte. **(b)** Quello di `sq_reddito` di circa ${{a01_01.f_sq|m}}$ volte.

![Intervallo di confidenza al 95\% per $\hat\beta_1$ con l'errore standard stimato, ${{a01_01.se_red|m}}$, e con quello dei regressori indipendenti, ${{a01_01.se_ideale|m}}$: il primo è ${{a01_01.f_red|m}}$ volte più largo.]({{a01_01.fig.inflazione}}){width=85%}

{{testo:a01_02}}

## Soluzione della Domanda 7 — Test ADF: leggere la riga giusta

> [!tip] Richiamo
> La regressione di Dickey-Fuller aumentata è $\Delta y_t=\alpha+\delta\,y_{t-1}+\gamma_1\,\Delta y_{t-1}+\gamma_2\,\Delta y_{t-2}+\epsilon_t$. La radice unitaria si verifica con $H_0:\delta=0$ contro $H_1:\delta<0$ e la statistica del test è il rapporto $t$ della sola riga del livello ritardato $y_{t-1}$, da confrontare con il valore critico ${{a01_02.cv|m}}$ nella coda sinistra: si rifiuta $H_0$ (serie stazionaria) se $t<{{a01_02.cv|m}}$. La costante e le differenze ritardate non entrano nel test. Sotto $H_0$ la statistica non è normale, quindi non si usa $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** Si individua in ciascuna tabella la riga del livello ritardato (`futures_1`, `spot_1`) e si confronta il suo $t$ con ${{a01_02.cv|m}}$.
>
> **(a)** Nella tabella di `spot` la riga `spot_1` ha $t={{a01_02.t_s|m}}$.
>
> **(b)** Per `futures` la riga `futures_1` dà $t={{a01_02.t_f|m}}>{{a01_02.cv|m}}$: non si rifiuta $H_0$.
>
> **(c)** Per `spot` $t={{a01_02.t_s|m}}>{{a01_02.cv|m}}$: non si rifiuta $H_0$.

> [!warning] Errore tipico
> Leggere la riga sbagliata. Nella tabella di `spot` la riga `d_spot_1` ha $t={{a01_02.t_ds|m}}$, minore di ${{a01_02.cv|m}}$, ma è il coefficiente di una differenza ritardata e non fa parte del test. Un altro errore è confrontare il $t$ con $\pm 1{,}96$ come per un test normale.

> [!success] Risposta
> **(a)** La statistica per `spot` è ${{a01_02.t_s|m}}$. **(b)** Per `futures` non si rifiuta $H_0$. **(c)** Per `spot` non si rifiuta $H_0$. In entrambi i casi resta plausibile la radice unitaria: le due serie sono non stazionarie.

![Statistiche $t$ del livello ritardato per `spot` e `futures` rispetto al valore critico ${{a01_02.cv|m}}$: entrambe fuori dalla regione di rifiuto.]({{a01_02.fig.adf}}){width=85%}

## Soluzione della Domanda 8 — Engle-Granger e cointegrazione

> [!tip] Richiamo
> Due serie non stazionarie sono cointegrate se esiste una loro combinazione lineare stazionaria. Il test di Engle-Granger verifica la radice unitaria sui residui $\hat u_t$ della relazione di lungo periodo: $H_0$ è l'assenza di cointegrazione, $H_1$ la stazionarietà dei residui. Con un p-value minore di $0{,}05$ si rifiuta $H_0$. Si parla di cointegrazione quando le serie sono non stazionarie e il test di Engle-Granger rifiuta.

> [!example] Svolgimento
> **Impostazione.** La (a) confronta il p-value con $0{,}05$; la (b) lo combina con la non stazionarietà accertata nella domanda 7.
>
> **(a)** Il p-value ${{a01_02.p_eg|m}}$ è minore di $0{,}05$: si rifiuta $H_0$ e i residui di lungo periodo risultano stazionari.
>
> **(b)** Nella domanda 7 `spot` e `futures` risultano non stazionarie e i residui della relazione di lungo periodo sono stazionari: le due serie sono cointegrate.

> [!warning] Errore tipico
> Leggere il p-value come se $H_0$ fosse la cointegrazione: nel test di Engle-Granger $H_0$ è l'assenza di cointegrazione, quindi un p-value piccolo porta a *rifiutare* $H_0$ e a concludere che c'è cointegrazione. Un altro errore è concludere dal solo p-value, senza aver accertato che le serie siano non stazionarie.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: i residui sono stazionari. **(b)** Sì: `spot` e `futures` sono non stazionarie e i residui della loro relazione di lungo periodo sono stazionari, quindi sono cointegrate.

![A sinistra i residui della relazione di lungo periodo, che oscillano attorno a zero; a destra il p-value di Engle-Granger, ${{a01_02.p_eg|m}}$, nella regione di rifiuto sotto $0{,}05$.]({{a01_02.fig.eg}}){width=85%}

## Soluzione della Domanda 9 — Il modello a correzione dell'errore è ben definito?

> [!tip] Richiamo
> Il modello $\Delta y_t=\gamma_0+\gamma_1\,\Delta x_t+\lambda\,\text{ecm}_{t-1}+\epsilon_t$ è ben definito (bilanciato) se tutti i termini sono stazionari: $\Delta y_t$ e $\Delta x_t$ lo sono se le serie hanno una sola radice unitaria, e $\text{ecm}_{t-1}$ lo è se le serie sono cointegrate. Inoltre $\lambda$ deve essere negativo e significativo, altrimenti non c'è un meccanismo che riporti il sistema verso l'equilibrio. Per il test su $\lambda$ si usa il rapporto $t$ con errori standard HAC.

> [!example] Svolgimento
> **Impostazione.** La (a) è un test su $\lambda$; la (b) verifica insieme cointegrazione e segno e significatività di $\hat\lambda$.
>
> **(a)** $H_0:\lambda=0$ contro $H_1:\lambda\neq 0$. Il rapporto $t$ di `ecm_1` vale ${{a01_02.t_lam|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(b)** Dalle domande 7 e 8 le serie sono non stazionarie e cointegrate, quindi i tre termini del modello sono stazionari. Inoltre $\hat\lambda={{a01_02.lam|m}}$ è negativo e significativo.

> [!warning] Errore tipico
> Giudicare il modello dal solo coefficiente di aggiustamento: un $\hat\lambda$ negativo e significativo non basta se non c'è cointegrazione, perché allora $\text{ecm}_{t-1}$ non è stazionario e la regressione è sbilanciata. Un altro errore è guardare il $t$ della costante o di `d_futures` invece di quello di `ecm_1`.

> [!success] Risposta
> **(a)** Si rifiuta $H_0:\lambda=0$: il coefficiente di aggiustamento è significativo al 5\%. **(b)** Sì: le serie sono cointegrate e $\hat\lambda={{a01_02.lam|m}}$ è negativo e significativo, quindi il modello è ben definito.

![Intervallo di confidenza al 95\% per $\lambda$ con errore standard HAC: stima ${{a01_02.lam|m}}$, lo zero è fuori dall'intervallo.]({{a01_02.fig.lambda}}){width=85%}

## Soluzione della Domanda 10 — Velocità di assorbimento del disequilibrio

> [!tip] Richiamo
> Sia $z_t=\text{ecm}_t$ il disequilibrio. Con $\Delta x=0$, shock e costante nulli, $\Delta y_t=\lambda\,z_{t-1}$ e, poiché $x_t=x_{t-1}$, $z_t=z_{t-1}+\Delta y_t=(1+\lambda)\,z_{t-1}$. Dopo $k$ periodi di aggiustamento (il primo è $t$) il disequilibrio residuo è $(1+\lambda)^k z_{t-1}$ e la quota assorbita è $1-(1+\lambda)^k$. Il minimo $k$ che ne assorbe almeno la quota $q$ soddisfa $(1+\lambda)^k\le 1-q$, cioè $k=\left\lceil \ln(1-q)/\ln(1+\lambda)\right\rceil$ (entrambi i logaritmi sono negativi se $-1<\lambda<0$).

> [!example] Svolgimento
> **Impostazione.** La (a) è la quota assorbita con $k=1$; la (b) cerca il primo $k$ con $(1+\hat\lambda)^k\le 1-q$.
>
> **(a)** Nel primo periodo $\Delta\text{spot}_t=\hat\lambda\,z_{t-1}$ è assorbita la quota $-100\,\hat\lambda=-100\times({{a01_02.lam|m}})={{a01_02.primo|m}}\%$ del disequilibrio.
>
> **(b)** Qui $1+\hat\lambda={{a01_02.phi|m}}$ e $1-q={{a01_02.obiettivo|m}}$. Da $k\ge\ln({{a01_02.obiettivo|m}})/\ln({{a01_02.phi|m}})={{a01_02.log|m}}$ si ottiene $k={{a01_02.k|m}}$. Verifica: dopo ${{a01_02.km|m}}$ periodi resta ${{a01_02.phi|m}}^{ {{a01_02.km|m}} }={{a01_02.resto_prima|m}}>{{a01_02.obiettivo|m}}$, dopo ${{a01_02.k|m}}$ periodi resta ${{a01_02.phi|m}}^{ {{a01_02.k|m}} }={{a01_02.resto|m}}\le{{a01_02.obiettivo|m}}$, cioè è assorbito il ${{a01_02.assorbito|m}}\%$.

> [!warning] Errore tipico
> Dividere la quota per il coefficiente, cioè $q/|\hat\lambda|$, come se ogni periodo assorbisse la stessa frazione del disequilibrio *iniziale*: ogni periodo assorbe la frazione $|\hat\lambda|$ del disequilibrio *rimasto*, che diminuisce. Un altro errore è non arrotondare $k$ per eccesso: con ${{a01_02.km|m}}$ periodi la soglia non è ancora raggiunta. Infine, qui $k$ conta anche il periodo $t$ di impatto, come definito nel testo: un testo che chiedesse i periodi *dopo* l'impatto avrebbe come risposta $k-1$.

> [!success] Risposta
> **(a)** Nel primo periodo si assorbe il ${{a01_02.primo|m}}\%$ del disequilibrio. **(b)** Servono $k={{a01_02.k|m}}$ periodi per assorbirne almeno il ${{a01_02.q|m}}\%$; dopo ${{a01_02.k|m}}$ periodi risulta assorbito il ${{a01_02.assorbito|m}}\%$ del disequilibrio iniziale.

![Quota di disequilibrio ancora presente dopo $h$ periodi, $(1+\hat\lambda)^h$: scende sotto ${{a01_02.obiettivo|m}}$ per $h={{a01_02.k|m}}$.]({{a01_02.fig.assorbimento}}){width=85%}
