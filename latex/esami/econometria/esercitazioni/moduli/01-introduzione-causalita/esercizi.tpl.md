<!-- ex e01_01 -->
# Esercizio 1 — Palestra aziendale e assenze per malattia *(livello base)*

> [!abstract] Dati
> In un'azienda con $n = {{e01_01.n}}$ dipendenti si è rilevato, in un solo momento, se ciascuno è iscritto alla palestra aziendale e se nell'ultimo anno ha fatto almeno un'assenza per malattia. Non si sa quando i dipendenti si siano iscritti. Si può parlare di causalità $X\to Y$ solo se valgono contemporaneamente tre criteri: (1) c'è associazione fra le variabili; (2) c'è un ordine logico o temporale, con la causa che precede l'effetto; (3) sono escluse le spiegazioni alternative. I conteggi sono i seguenti.
>
> {{e01_01.tab.cont}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Quale percentuale degli iscritti ha fatto almeno un'assenza? **(b)** Quale percentuale dei non iscritti? **(c)** Si calcoli la differenza «percentuale degli iscritti meno percentuale dei non iscritti», in punti percentuali. **(d)** Il criterio (1), l'associazione, è soddisfatto, giudicando dal solo confronto delle due percentuali (senza test statistico)? Si risponda sì o no. **(e)** I dati permettono di stabilire che l'iscrizione precede le assenze, cioè che il criterio (2) è soddisfatto? Si risponda sì o no. **(f)** Si può concludere che l'iscrizione alla palestra riduce le assenze per malattia? Si risponda sì o no.
<!-- /ex -->

<!-- ex e01_02 -->
# Esercizio 2 — Che tipo di dati sono? *(livello base)*

> [!abstract] Dati
> I dati si dicono *cross section* se osservano molti soggetti in un solo istante, *serie storica* se osservano un solo soggetto in istanti successivi, *panel* se osservano gli stessi soggetti in più istanti. Quattro insiemi di dati sono riportati con una riga per ogni coppia soggetto-periodo.
>
> Dataset A, fatturato di alcune imprese (milioni di euro):
>
> {{e01_02.tab.a}}
>
> Dataset B, prezzo di chiusura mensile di un titolo (euro):
>
> {{e01_02.tab.b}}
>
> Dataset C, investimenti annui (milioni di euro). La tabella ne mostra un estratto: il dataset completo contiene $N = {{e01_02.N}}$ imprese osservate per $T = {{e01_02.T}}$ anni consecutivi, senza dati mancanti.
>
> {{e01_02.tab.c}}
>
> Dataset D, prezzo di vendita (migliaia di dollari) delle case vendute in un comune nel 1978 e nel 1981, ciascuna con il proprio codice:
>
> {{e01_02.tab.d}}

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** Il dataset A è una serie storica? Si risponda sì o no. **(b)** Il dataset B è una serie storica? Si risponda sì o no. **(c)** Il dataset C è un panel? Si risponda sì o no. **(d)** Il dataset D è un panel? Si risponda sì o no. **(e)** Quante osservazioni, cioè quante righe, contiene il dataset C completo? **(f)** Se del dataset C si tenessero soltanto le righe di un'impresa, i dati sarebbero un panel? Si risponda sì o no.
<!-- /ex -->

<!-- ex e01_03 -->
# Esercizio 3 — Polizia e criminalità *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e01_03.n}}$ città si osservano `reati` (reati ogni mille abitanti) e `poliziotti` (poliziotti ogni mille abitanti). Si è stimata la regressione semplice di `reati` su `poliziotti`
>
> $$\text{reati} = \beta_0 + \beta_1\,\text{poliziotti} + \epsilon ,$$
>
> {{e01_03.tab.A}}
>
> e quella con i ruoli scambiati,
>
> $$\text{poliziotti} = \gamma_0 + \gamma_1\,\text{reati} + u .$$
>
> {{e01_03.tab.B}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Si usi il valore critico 1,96. **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(b)** Se si leggesse la prima regressione in senso causale, di quanti reati ogni mille abitanti varierebbe in media il numero di reati per un aumento di ${{e01_03.dpol|m}}$ poliziotti ogni mille abitanti? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\gamma_1=0$ contro $H_1:\gamma_1\neq 0$. **(d)** Le due regressioni hanno lo stesso rapporto $t$ per la pendenza e lo stesso $R^2$? Si risponda sì o no. **(e)** Dalla sola associazione fra le due variabili si può stabilire quale è la causa e quale l'effetto? Si risponda sì o no.
<!-- /ex -->

<!-- ex e01_04 -->
# Esercizio 4 — La spesa riportata male *(livello intermedio)*

> [!abstract] Dati
> Un'indagine chiede a $n = {{e01_04.n}}$ famiglie la spesa settimanale al supermercato e la spesa mensile non alimentare `y`. Le famiglie ricordano la spesa settimanale in modo impreciso: l'errore di ricordo è in media nullo. I dati sono simulati, quindi si conosce anche la spesa vera `spesa_vera`, che nella realtà non si osserva, mentre `spesa_rip` è quella riportata dalle famiglie. La spesa mensile è stata generata a partire dalla spesa vera con un coefficiente $\beta = {{e01_04.beta|m}}$. Le medie e le deviazioni standard del campione sono le seguenti.
>
> {{e01_04.tab.desc}}
>
> Modello V, `y` su `spesa_vera`:
>
> {{e01_04.tab.vera}}
>
> Modello R, `y` su `spesa_rip` (stesse famiglie):
>
> {{e01_04.tab.rip}}
>
> Modello G, `y` su `spesa_rip`, con un campione di ${{e01_04.grande}}$ famiglie generate allo stesso modo:
>
> {{e01_04.tab.grande}}

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** In percentuale della media della spesa vera, di quanto differisce la media della spesa riportata (media riportata meno media vera)? **(b)** Quanto vale il rapporto fra la pendenza del Modello R e quella del Modello V, cioè la prima divisa per la seconda? **(c)** Quanto vale il rapporto fra la pendenza del Modello G e $\beta$, cioè la prima divisa per il secondo? **(d)** Nel Modello G, al livello del 5\% (valore critico 1,96), si decida se rifiutare o non rifiutare $H_0:\beta_1=\beta$ contro $H_1:\beta_1\neq\beta$, con $t=(\hat\beta_1-\beta)/\widehat{\text{se}}(\hat\beta_1)$. **(e)** Alla luce dei punti precedenti, un campione più grande basta a eliminare la distorsione dovuta all'errore di misura? Si risponda sì o no.
<!-- /ex -->

<!-- ex e01_05 -->
# Esercizio 5 — Gelati e incidenti in acqua *(livello d'appello)*

> [!abstract] Dati
> Su $n = {{e01_05.n}}$ località balneari si osservano in agosto `incidenti` (incidenti in acqua ogni 100 mila bagnanti), `gelati` (porzioni di gelato vendute per abitante a settimana) e `temperatura` (temperatura media in gradi centigradi). Si sono stimati il Modello 1
>
> $$\text{incidenti} = \beta_0 + \beta_1\,\text{gelati} + \epsilon$$
>
> {{e01_05.tab.m1}}
>
> il Modello 2, che aggiunge la temperatura,
>
> $$\text{incidenti} = \beta_0 + \beta_1\,\text{gelati} + \beta_2\,\text{temperatura} + \epsilon$$
>
> {{e01_05.tab.m2}}
>
> e la regressione ausiliaria $\text{gelati} = \delta_0 + \delta_1\,\text{temperatura} + u$.
>
> {{e01_05.tab.aux}}

> [!question] Testo della domanda
> **Domanda 5 *(4 punti)*.** In tutti i test si usi il livello del 5\% e il valore critico 1,96. **(a)** Nel Modello 1, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(b)** Se si leggesse il Modello 1 in senso causale, di quanti incidenti ogni 100 mila bagnanti varierebbe in media il numero di incidenti per un aumento di ${{e01_05.dg}}$ porzioni di gelato a settimana? **(c)** Nel Modello 2, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(d)** Nel Modello 2, di quanti incidenti ogni 100 mila bagnanti varia in media il numero di incidenti per un aumento di ${{e01_05.dt}}$ gradi della temperatura, a parità di gelati? **(e)** Nella regressione ausiliaria, si decida se rifiutare o non rifiutare $H_0:\delta_1=0$ contro $H_1:\delta_1\neq 0$. **(f)** Sia $b$ la stima del coefficiente di `gelati` nel Modello 1. Nel Modello 2, si decida se rifiutare o non rifiutare $H_0:\beta_1=b$ contro $H_1:\beta_1\neq b$, con $t=(\hat\beta_1-b)/\widehat{\text{se}}(\hat\beta_1)$, dove $\hat\beta_1$ e $\widehat{\text{se}}(\hat\beta_1)$ sono quelli del Modello 2.
<!-- /ex -->

<!-- ex e01_06 -->
# Esercizio 6 — Un fondo e il CAPM *(livello d'appello)*

> [!abstract] Dati
> Per $n = {{e01_06.n}}$ mesi consecutivi si osservano l'extra-rendimento mensile di un fondo, $R_t$, e quello del portafoglio di mercato, $R_{mt}$, entrambi in percentuale e al netto del tasso privo di rischio. Il CAPM prevede, per gli extra-rendimenti, $E[R_t]=\beta\,E[R_{mt}]$, cioè un'intercetta nulla. Per verificarlo si stima
>
> $$R_t = \alpha + \beta\,R_{mt} + \epsilon_t ,\qquad \text{Var}(R_t)=\beta^2\,\text{Var}(R_{mt})+\sigma^2 ,$$
>
> dove $\sigma$ è il rischio idiosincratico, stimato con $\hat\sigma=\sqrt{\text{SSR}/(n-2)}$. Le stime OLS sono le seguenti.
>
> {{e01_06.tab.ols}}

> [!question] Testo della domanda
> **Domanda 6 *(4 punti)*.** In tutti i test si usi il livello del 5\% e il valore critico 1,96. **(a)** I dati sono una serie storica? Si risponda sì o no. **(b)** Si decida se rifiutare o non rifiutare $H_0:\alpha=0$ contro $H_1:\alpha\neq 0$. **(c)** Il risultato del punto (b) dimostra che il CAPM è vero? Si risponda sì o no. **(d)** Si decida se rifiutare o non rifiutare $H_0:\beta=1$ contro $H_1:\beta\neq 1$, con $t=(\hat\beta-1)/\widehat{\text{se}}(\hat\beta)$. **(e)** Di quanti punti percentuali varia in media l'extra-rendimento del fondo se quello del mercato aumenta di ${{e01_06.dm}}$ punti percentuali? **(f)** Quanto vale la stima $\hat\sigma$ del rischio idiosincratico?
<!-- /ex -->
