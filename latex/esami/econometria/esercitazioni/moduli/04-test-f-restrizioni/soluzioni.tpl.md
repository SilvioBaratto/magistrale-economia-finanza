{{testo:e04_01}}

> [!tip] Richiamo
> Con la dipendente in logaritmo, una dummy che passa da 0 a 1 fa variare $\log(y)$ di $\beta$, cioè $y$ di circa $100\,\beta$ per cento. Le tre dummy di ruolo sommano a 1, come la costante: tenerle tutte e tre nel modello insieme alla costante darebbe collinearità perfetta (trappola delle dummy), perciò una va esclusa. La categoria esclusa è il riferimento e ogni coefficiente di dummy è la differenza attesa rispetto ad essa, a parità del resto; invertendo il confronto il segno cambia. Per decidere su $H_0:\beta=0$ si guarda l'intervallo di confidenza al 95\%, $\hat\beta\pm 1{,}96\,\widehat{\text{se}}(\hat\beta)$.

> [!example] Svolgimento
> **Impostazione.** `guardia` e `ala` sono confrontate con il centro, la categoria omessa.
>
> **(a)** Passando dal centro alla guardia, `guardia` va da 0 a 1 e `ala` resta 0: $\Delta\%\,\text{salario}\approx 100\,\hat\beta_1=100\times({{e04_01.bg|m}})={{e04_01.pct_g|m}}\%$.
>
> **(b)** Il confronto è invertito: $-100\,\hat\beta_1=-100\times({{e04_01.bg|m}})={{e04_01.pct_c|m}}\%$.
>
> **(c)** Si verifica $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. L'intervallo di confidenza al 95\% è $[{{e04_01.a_lo|m}};\,{{e04_01.a_hi|m}}]$ e contiene lo zero. Lo stesso dice $t={{e04_01.ta|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.
>
> **(d)** Si verifica $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. L'intervallo di confidenza al 95\% è $[{{e04_01.g_lo|m}};\,{{e04_01.g_hi|m}}]$ e lo zero ne è fuori. Lo stesso dice $t={{e04_01.tg|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(e)** I ruoli sono tre e le tre dummy sommano a 1, come la costante: per evitare la collinearità perfetta una è stata esclusa, e quella esclusa, il centro, è la categoria di riferimento. $\beta_1$ è la differenza attesa di $\log(\text{salario})$ fra una guardia e un centro e $\beta_2$ fra un'ala e un centro, a parità di punti ed esperienza.

> [!warning] Errore tipico
> Leggere $\hat\beta_1$ come differenza fra guardia e ala, o fra guardia e le altre due categorie: ogni coefficiente confronta il ruolo con il centro e nient'altro. Un altro errore è rispondere ${{e04_01.pct_g|m}}\%$ anche alla (b): invertire il confronto cambia il segno. Infine non si deve pensare che la dummy del centro sia stata dimenticata: è esclusa proprio per evitare la collinearità con la costante.

> [!success] Risposta
> **(a)** Da un centro a una guardia il salario varia di circa ${{e04_01.pct_g|m}}\%$. **(b)** Da una guardia a un centro varia di circa ${{e04_01.pct_c|m}}\%$. **(c)** Lo zero cade nell'intervallo di confidenza dell'ala: non si rifiuta $H_0:\beta_2=0$, un'ala non guadagna in modo significativamente diverso da un centro. **(d)** Lo zero non cade nell'intervallo della guardia: si rifiuta $H_0:\beta_1=0$, una guardia guadagna significativamente meno. **(e)** Il centro è la categoria di riferimento, esclusa per la trappola delle dummy; $\beta_1$ e $\beta_2$ sono le differenze di $\log(\text{salario})$ rispetto al centro.

![Differenza di salario rispetto al centro, in percentuale, con intervallo di confidenza al 95\%: quello dell'ala contiene lo zero, quello della guardia no.]({{e04_01.fig.ruoli}}){width=85%}

{{testo:e04_02}}

> [!tip] Richiamo
> Il test $F$ confronta il modello completo con il modello ristretto, che impone $H_0$. Con $s$ restrizioni e $n-k-1$ gradi di libertà del modello completo,
> $$F=\frac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-k-1)}=\frac{(R^2_c-R^2_r)/s}{(1-R^2_c)/(n-k-1)},$$
> dove la seconda forma vale perché i due modelli hanno la stessa variabile dipendente. $F$ è sempre positiva ($\text{SSR}_r\geq\text{SSR}_c$) e si rifiuta $H_0$ solo se $F$ supera il valore critico: il test è unilaterale destro.

> [!example] Svolgimento
> **Impostazione.** Le due variabili escluse dal modello ristretto danno le restrizioni; poi si usano le due somme dei quadrati dei residui, o i due $R^2$, stampati sotto le tabelle.
>
> **(a)** $H_0:\beta_4=0$ e $\beta_5=0$ sono due restrizioni: $s={{e04_02.s|m}}$ (quanti regressori in meno ha il modello ristretto).
>
> **(b)** Il modello completo ha $k={{e04_02.k|m}}$ regressori: $n-k-1={{e04_02.n|m}}-{{e04_02.k|m}}-1={{e04_02.df|m}}$.
>
> **(c)** $F=\dfrac{ ({{e04_02.ssr_r|m}}-{{e04_02.ssr_c|m}})/{{e04_02.s|m}} }{ {{e04_02.ssr_c|m}}/{{e04_02.df|m}} }=\dfrac{ {{e04_02.dssr|m}}/{{e04_02.s|m}} }{ {{e04_02.ssr_c|m}}/{{e04_02.df|m}} }={{e04_02.F|m}}$.
>
> **(d)** $F=\dfrac{ ({{e04_02.r2_c|m}}-{{e04_02.r2_r|m}})/{{e04_02.s|m}} }{ (1-{{e04_02.r2_c|m}})/{{e04_02.df|m}} }={{e04_02.F_r2|m}}$: lo stesso valore della (c).
>
> **(e)** $F={{e04_02.F|m}}$ è minore del valore critico ${{e04_02.fcrit|m}}$: non si rifiuta $H_0$.

> [!warning] Errore tipico
> Scrivere $\text{SSR}_c-\text{SSR}_r$ al numeratore: sarebbe negativo, ma $F$ non può esserlo. Un altro errore è dimenticare di dividere per $s$ il numeratore, o usare $n-k$ gradi di libertà invece di $n-k-1$ (la costante è un parametro). E $F$ non è la somma dei due $t^2$ di $\beta_4$ e $\beta_5$: con stimatori incorrelati coincide con la loro media, in generale dipende anche dalla covarianza fra gli stimatori.

> [!success] Risposta
> **(a)** $s={{e04_02.s|m}}$. **(b)** $n-k-1={{e04_02.df|m}}$. **(c)** $F={{e04_02.F|m}}$ con le somme dei quadrati dei residui. **(d)** $F={{e04_02.F_r2|m}}$ con gli $R^2$, lo stesso valore. **(e)** $F$ è minore del valore critico ${{e04_02.fcrit|m}}$, quindi non si rifiuta $H_0$: al 5\% `balcone` e `box` non sono congiuntamente significative e i dati non danno evidenza contro il modello ristretto.

![Densità $F({{e04_02.s|m}},\,{{e04_02.df|m}})$ con la regione di rifiuto al 5\%: la statistica osservata ${{e04_02.F|m}}$ cade a sinistra del valore critico ${{e04_02.fcrit|m}}$, quindi non si rifiuta $H_0$.]({{e04_02.fig.f}}){width=85%}

{{testo:e04_03}}

> [!tip] Richiamo
> Una combinazione lineare di coefficienti ha varianza $\text{Var}(\hat\beta_1+\hat\beta_2)=\text{Var}(\hat\beta_1)+\text{Var}(\hat\beta_2)+2\,\text{Cov}(\hat\beta_1,\hat\beta_2)$: la tabella dà solo le varianze, la covarianza va presa dal testo. Il rapporto $t=(\hat\beta_1+\hat\beta_2-q)/\widehat{\text{se}}(\hat\beta_1+\hat\beta_2)$ si confronta con $1{,}96$; per una sola restrizione la statistica $F$ è $t^2$.

> [!example] Svolgimento
> **Impostazione.** L'ipotesi è una sola restrizione lineare, $\beta_1+\beta_2=1$: si stima la somma, se ne calcola l'errore standard con la covarianza e si fa un test $t$.
>
> **(a)** $\hat\beta_1+\hat\beta_2={{e04_03.b1|m}}+{{e04_03.b2|m}}={{e04_03.somma|m}}$.
>
> **(b)** $\widehat{\text{se}}=\sqrt{ {{e04_03.s1|m}}^2+{{e04_03.s2|m}}^2+2\times({{e04_03.cov|m}}) }={{e04_03.se|m}}$.
>
> **(c)** $t=\dfrac{ {{e04_03.somma|m}}-1 }{ {{e04_03.se|m}} }={{e04_03.t|m}}$.
>
> **(d)** $t={{e04_03.t|m}}$ è in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$. Lo stesso dice l'intervallo di confidenza al 95\% per $\beta_1+\beta_2$, $[{{e04_03.ic_lo|m}};\,{{e04_03.ic_hi|m}}]$, che non contiene $1$.
>
> **(e)** $F=t^2=({{e04_03.t|m}})^2={{e04_03.F|m}}$.

> [!warning] Errore tipico
> Calcolare l'errore standard senza la covarianza, $\sqrt{ {{e04_03.s1|m}}^2+{{e04_03.s2|m}}^2 }={{e04_03.se_ing|m}}$ invece di ${{e04_03.se|m}}$: si otterrebbe $t={{e04_03.t_ing|m}}$ e non si rifiuterebbe $H_0$. Capitale e lavoro si muovono insieme, i loro coefficienti sono correlati negativamente e la covarianza (negativa) riduce la varianza della somma. Un altro errore è sommare direttamente i due errori standard.

> [!success] Risposta
> **(a)** $\hat\beta_1+\hat\beta_2={{e04_03.somma|m}}$. **(b)** L'errore standard della somma, con la covarianza, è ${{e04_03.se|m}}$. **(c)** $t={{e04_03.t|m}}$. **(d)** Si rifiuta $H_0$: i rendimenti di scala non sono costanti e, essendo la somma minore di 1, sono decrescenti. **(e)** $F={{e04_03.F|m}}$.

![Intervallo di confidenza al 95\% per $\beta_1+\beta_2$, $[{{e04_03.ic_lo|m}};\,{{e04_03.ic_hi|m}}]$: il valore $1$ dei rendimenti di scala costanti è fuori dall'intervallo.]({{e04_03.fig.ic}}){width=85%}

{{testo:e04_04}}

> [!tip] Richiamo
> Una variabile qualitativa con tre categorie si codifica con tre dummy mutuamente esclusive che sommano a 1. Con la costante nel modello se ne tengono due: la terza è la categoria di riferimento e ogni coefficiente di dummy è la differenza attesa rispetto ad essa, a parità del resto (tenerle tutte e tre con la costante dà collinearità perfetta). Il titolo di studio conta se almeno una di queste differenze non è nulla: $H_0:\delta_1=\delta_2=0$ contro $H_1$: almeno un $\delta_j\neq 0$, cioè $s$ restrizioni. Il modello ristretto esclude le dummy e
> $$F=\frac{(R^2_c-R^2_r)/s}{(1-R^2_c)/(n-k-1)},$$
> da confrontare con il valore critico: si rifiuta se $F$ lo supera. Cambiare la categoria di riferimento non cambia l'adattamento del modello.

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) traducono la domanda in un sistema d'ipotesi; poi si contano le restrizioni e si calcola $F$ dagli $R^2$ dei due modelli.
>
> **(a)** Le dummy esplicite sono `obbligo` e `diploma`: la categoria di riferimento è la laurea, che ha entrambe le dummy a 0. $\delta_1$ è la differenza attesa di $\log(\text{salario})$ fra un lavoratore con la sola scuola dell'obbligo e un laureato (${{e04_04.d1|m}}$) e $\delta_2$ quella fra un diplomato e un laureato (${{e04_04.d2|m}}$). La dummy dei laureati non compare perché le tre dummy sommano a 1, come la costante: tenerle tutte darebbe collinearità perfetta.
>
> **(b)** $H_0:\delta_1=\delta_2=0$ contro $H_1:\delta_1\neq 0$ oppure $\delta_2\neq 0$. Se $H_0$ è vera il titolo di studio non ha rilevanza e il modello si riduce a quello ristretto.
>
> **(c)** Due uguaglianze: $s={{e04_04.s|m}}$.
>
> **(d)** Il modello completo ha $k={{e04_04.k|m}}$ regressori: $n-k-1={{e04_04.n|m}}-{{e04_04.k|m}}-1={{e04_04.df|m}}$.
>
> **(e)** $F=\dfrac{ ({{e04_04.r2_c|m}}-{{e04_04.r2_r|m}})/{{e04_04.s|m}} }{ (1-{{e04_04.r2_c|m}})/{{e04_04.df|m}} }=\dfrac{ {{e04_04.dr2|m}}/{{e04_04.s|m}} }{ (1-{{e04_04.r2_c|m}})/{{e04_04.df|m}} }={{e04_04.F|m}}$.
>
> **(f)** $F={{e04_04.F|m}}$ è maggiore del valore critico ${{e04_04.fcrit|m}}$: si rifiuta $H_0$.
>
> **(g)** No. Con il diploma come riferimento le dummy cambierebbero (`obbligo` e `laurea`) ma il modello avrebbe gli stessi valori stimati, lo stesso $R^2$ e lo stesso modello ristretto: la stessa $F$.

> [!warning] Errore tipico
> Decidere dai due rapporti $t$ delle dummy: quello di `obbligo` è ${{e04_04.t1|m}}$ e quello di `diploma` è ${{e04_04.t2|m}}$, ma ciascuno confronta una categoria con la laurea e non dice nulla sull'ipotesi congiunta; ripetere i test $t$ non controlla il livello del 5\%. Un altro errore è scrivere $H_0:\delta_1=\delta_2$, che confronta obbligo e diploma fra loro (una restrizione), e non $H_0:\delta_1=\delta_2=0$ (due).

> [!success] Risposta
> **(a)** La categoria di riferimento è la laurea; $\delta_1$ e $\delta_2$ sono le differenze rispetto ai laureati e la dummy dei laureati è omessa per evitare la collinearità perfetta con la costante. **(b)** $H_0:\delta_1=\delta_2=0$ contro $H_1:\delta_1\neq 0$ oppure $\delta_2\neq 0$. **(c)** $s={{e04_04.s|m}}$. **(d)** $n-k-1={{e04_04.df|m}}$. **(e)** $F={{e04_04.F|m}}$. **(f)** $F$ supera il valore critico ${{e04_04.fcrit|m}}$: si rifiuta $H_0$ e il titolo di studio ha rilevanza nel modello. **(g)** No: la scelta della categoria di riferimento non cambia $F$.

![Densità $F({{e04_04.s|m}},\,{{e04_04.df|m}})$ con la regione di rifiuto al 5\%: la statistica osservata ${{e04_04.F|m}}$ cade nella regione di rifiuto, a destra del valore critico ${{e04_04.fcrit|m}}$.]({{e04_04.fig.f}}){width=85%}

{{testo:e04_05}}

> [!tip] Richiamo
> Con il termine $\beta_4(\text{donna}\times\text{istr})$ la variazione attesa per un anno di istruzione in più è $\Delta\log(y)=(\beta_1+\beta_4\,\text{donna})\,\Delta\text{istr}$: $\beta_1$ per gli uomini, $\beta_1+\beta_4$ per le donne, in percentuale $100\times$ questi valori. L'effetto dipende dal genere solo se $\beta_4\neq 0$, che si verifica con $H_0:\beta_4=0$. Il divario donna meno uomo a parità di esperienza e con $\text{istr}=e$ è la differenza dei due log-salari attesi, $\beta_2+\beta_4\,e$: dipende dal livello $e$ e coincide con $\beta_2$ solo per $e=0$.

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) sono le due pendenze, la (c) è il test sull'interazione, la (d) la differenza fra le due rette in un punto.
>
> **(a)** Per un uomo `donna`$=0$ e l'effetto è $100\,\hat\beta_1=100\times{{e04_05.b1|m}}={{e04_05.eff_u|m}}\%$.
>
> **(b)** Per una donna `donna`$=1$: $100\,(\hat\beta_1+\hat\beta_4)=100\times({{e04_05.b1|m}}+({{e04_05.b4|m}}))={{e04_05.eff_d|m}}\%$.
>
> **(c)** $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$. L'intervallo di confidenza al 95\% è $[{{e04_05.lo4|m}};\,{{e04_05.hi4|m}}]$ e lo zero ne è fuori. Lo stesso dice $t={{e04_05.t4|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(d)** $100\,(\hat\beta_2+e_0\,\hat\beta_4)=100\times\bigl({{e04_05.b2|m}}+{{e04_05.e0|m}}\times({{e04_05.b4|m}})\bigr)={{e04_05.gap|m}}\%$.
>
> **(e)** No. $\hat\beta_2={{e04_05.b2|m}}$ è il divario per $\text{istr}=0$, un livello che non si osserva fra i lavoratori; il divario cambia con l'istruzione e a ${{e04_05.e0|m}}$ anni vale ${{e04_05.gap|m}}\%$, di segno opposto.

> [!warning] Errore tipico
> Leggere $\hat\beta_1$ come rendimento dell'istruzione per tutti: vale per gli uomini, e per le donne va sommato $\hat\beta_4$. Un altro errore è interpretare la dummy `donna` da sola: qui $\hat\beta_2$ è positivo, ma il divario a ${{e04_05.e0|m}}$ anni di istruzione è negativo perché l'interazione $\hat\beta_4$ lo trascina verso il basso.

> [!success] Risposta
> **(a)** Per un uomo un anno di istruzione in più aumenta il salario di circa ${{e04_05.eff_u|m}}\%$. **(b)** Per una donna di circa ${{e04_05.eff_d|m}}\%$. **(c)** Si rifiuta $H_0:\beta_4=0$: il rendimento dell'istruzione dipende dal genere. **(d)** A ${{e04_05.e0|m}}$ anni di istruzione il salario atteso di una donna differisce di circa ${{e04_05.gap|m}}\%$ da quello di un uomo con la stessa esperienza. **(e)** No: $\beta_2$ è il divario solo per un'istruzione nulla; per gli altri livelli serve $\beta_2+\beta_4\,\text{istr}$.

![Log-salario atteso in funzione dell'istruzione, a esperienza media: la retta delle donne ha pendenza minore e il divario (segmento verde) a ${{e04_05.e0|m}}$ anni vale ${{e04_05.gap|m}}\%$.]({{e04_05.fig.rette}}){width=85%}

{{testo:e04_06}}

> [!tip] Richiamo
> Con la costante e tre dummy per quattro gruppi, il gruppo con tutte le dummy a 0 è il riferimento e ogni $\delta_j$ è la differenza attesa rispetto ad esso, a parità di esperienza. La differenza fra due lavoratori è la differenza delle loro medie condizionate, una combinazione lineare dei coefficienti: per A (sposato laureato, esperienza $e_A$) e B (riferimento, esperienza $e_B$) vale $\delta_3+(e_A-e_B)\,\beta$. Per la varianza, con $d=e_A-e_B$,
> $$\text{Var}(\hat\delta_3+d\,\hat\beta)=\text{Var}(\hat\delta_3)+d^2\,\text{Var}(\hat\beta)+2\,d\,\text{Cov}(\hat\delta_3,\hat\beta),$$
> e l'intervallo di confidenza al 95\% è la stima $\pm\,1{,}96\,\widehat{\text{se}}$.

> [!example] Svolgimento
> **Impostazione.** Si scrive la differenza A meno B come combinazione lineare dei coefficienti, poi si stima, si calcola l'errore standard con la covarianza e si costruisce l'intervallo.
>
> **(a)** Il riferimento è il gruppo dei single non laureati (le tre dummy valgono 0). Per A: $E[\log(\text{salario})]=\alpha+\delta_3+\beta\,e_A$; per B: $\alpha+\beta\,e_B$. La differenza è $\delta_3+(e_A-e_B)\,\beta$, con $e_A-e_B={{e04_06.ea|m}}-{{e04_06.eb|m}}={{e04_06.dex|m}}$.
>
> **(b)** $\hat\delta_3+d\,\hat\beta={{e04_06.b1|m}}+{{e04_06.dex|m}}\times{{e04_06.b2|m}}={{e04_06.stima|m}}$, cioè ${{e04_06.diff|m}}\%$.
>
> **(c)** $\widehat{\text{Var}}={{e04_06.s1|m}}^2+{{e04_06.dex|m}}^2\times{{e04_06.s2|m}}^2+2\times{{e04_06.dex|m}}\times({{e04_06.cov|m}})={{e04_06.var|m}}$, quindi $100\sqrt{ {{e04_06.var|m}} }={{e04_06.se|m}}$ punti percentuali.
>
> **(d)** e **(e)** ${{e04_06.diff|m}}\pm 1{,}96\times{{e04_06.se|m}}=[{{e04_06.lo|m}};\,{{e04_06.hi|m}}]$.
>
> **(f)** Si verifica $H_0:\delta_3+d\,\beta=0$ contro l'alternativa bilaterale. Lo zero non cade nell'intervallo di confidenza; lo stesso dice $t={{e04_06.diff|m}}/{{e04_06.se|m}}={{e04_06.t|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Leggere $\hat\delta_3$ da solo come differenza fra A e B: vale solo per due lavoratori con la stessa esperienza, e qui A ha ${{e04_06.dex|m}}$ anni in più, che pesano $d\,\hat\beta$. Un altro errore è omettere la covarianza: l'errore standard sarebbe ${{e04_06.se_ing|m}}$ invece di ${{e04_06.se|m}}$. Fra una dummy di gruppo e l'esperienza la covarianza è diversa da zero perché gli sposati hanno in media più esperienza.

> [!success] Risposta
> **(a)** Il riferimento è il gruppo dei single non laureati; la differenza A meno B è $\delta_3+(e_A-e_B)\,\beta$. **(b)** A guadagna in media circa ${{e04_06.diff|m}}\%$ più di B. **(c)** L'errore standard è ${{e04_06.se|m}}$ punti percentuali. **(d)** L'estremo inferiore dell'intervallo al 95\% è ${{e04_06.lo|m}}\%$. **(e)** L'estremo superiore è ${{e04_06.hi|m}}\%$. **(f)** Lo zero è fuori dall'intervallo: si rifiuta l'ipotesi di uguale salario atteso.

![Intervallo di confidenza al 95\% per la differenza attesa fra A e B, in percentuale: $[{{e04_06.lo|m}};\,{{e04_06.hi|m}}]$, lo zero è fuori.]({{e04_06.fig.ic}}){width=85%}

{{testo:e04_07}}

> [!tip] Richiamo
> Il test di significatività congiunta confronta il modello completo con quello che ha la sola costante, per cui $R^2_r=0$ e $s=k$:
> $$F=\frac{R^2/k}{(1-R^2)/(n-k-1)} ,$$
> da confrontare con il valore critico. Ripetere i test $t$ non è una soluzione valida: se i test fossero indipendenti la probabilità di rifiutare almeno una volta quando $H_0$ è vera sarebbe $1-(1-0{,}05)^{k}$, molto più del 5\%. Inoltre con regressori molto correlati gli errori standard sono grandi e i singoli $t$ piccoli anche quando insieme i regressori spiegano molto.

> [!example] Svolgimento
> **Impostazione.** Si contano i coefficienti con $|t|>1{,}96$, poi si calcola $F$ dall'$R^2$ stampato sotto la tabella, con modello ristretto la sola costante.
>
> **(a)** I rapporti $t$ sono ${{e04_07.t1|m}}$, ${{e04_07.t2|m}}$ e ${{e04_07.t3|m}}$, tutti in valore assoluto minori di $1{,}96$: i coefficienti significativi sono ${{e04_07.conta|m}}$.
>
> **(b)** Tre uguaglianze, $\beta_1=0$, $\beta_2=0$, $\beta_3=0$: $s={{e04_07.s|m}}$.
>
> **(c)** $n-k-1={{e04_07.n|m}}-{{e04_07.s|m}}-1={{e04_07.df|m}}$.
>
> **(d)** $F=\dfrac{ {{e04_07.r2|m}}/{{e04_07.s|m}} }{ (1-{{e04_07.r2|m}})/{{e04_07.df|m}} }={{e04_07.F|m}}$.
>
> **(e)** $F={{e04_07.F|m}}$ è maggiore del valore critico ${{e04_07.fcrit|m}}$: si rifiuta $H_0$.
>
> **(f)** $1-(1-0{,}05)^{ {{e04_07.s|m}} }={{e04_07.prob|m}}$.

> [!warning] Errore tipico
> Concludere dai tre $t$ non significativi che nessun punteggio conta. I tre test misurano in buona parte la stessa abilità, sono molto correlati e le stime individuali sono imprecise, ma insieme spiegano una parte importante del salario: il test $F$ rifiuta $H_0$. Per lo stesso motivo non si può decidere sul test congiunto guardando i singoli $t$: il valore ${{e04_07.prob|m}}$ è il livello del procedimento «tre test separati» solo se i test fossero indipendenti; con regressori correlati le $t$ non lo sono e il livello vero sta fra $0{,}05$ e quel valore. Questo esercizio mostra soprattutto una perdita di potenza dei test singoli: nessuna $t$ è significativa, ma $F$ rifiuta.

> [!success] Risposta
> **(a)** Nessuno dei tre coefficienti è significativo al 5\%: ${{e04_07.conta|m}}$. **(b)** $s={{e04_07.s|m}}$. **(c)** $n-k-1={{e04_07.df|m}}$. **(d)** $F={{e04_07.F|m}}$. **(e)** $F$ supera il valore critico ${{e04_07.fcrit|m}}$: si rifiuta $H_0$, i tre punteggi sono congiuntamente significativi. **(f)** La probabilità è ${{e04_07.prob|m}}$, quasi il triplo del 5\%.

![A sinistra gli intervalli di confidenza al 95\% dei tre coefficienti: tutti contengono lo zero. A destra la densità $F({{e04_07.s|m}},\,{{e04_07.df|m}})$: la statistica ${{e04_07.F|m}}$ supera di molto il valore critico ${{e04_07.fcrit|m}}$.]({{e04_07.fig.congiunto}}){width=85%}

{{testo:e04_08}}

> [!tip] Richiamo
> Con il termine $\beta_3(\text{istr}\times\text{esper})$ la variazione attesa per un anno di istruzione in più è $\Delta\log(y)=(\beta_1+\beta_3\,\text{esper})\,\Delta\text{istr}$: l'effetto dipende dall'esperienza se e solo se $\beta_3\neq 0$. $\beta_1$ è l'effetto per $\text{esper}=0$, cioè per un lavoratore senza esperienza. Per $\text{esper}=x_0$ l'effetto è la combinazione lineare $\beta_1+x_0\,\beta_3$, in percentuale $100\,(\beta_1+x_0\,\beta_3)$, con
> $$\text{Var}(\hat\beta_1+x_0\hat\beta_3)=\text{Var}(\hat\beta_1)+x_0^2\,\text{Var}(\hat\beta_3)+2\,x_0\,\text{Cov}(\hat\beta_1,\hat\beta_3).$$
> Si decide con il rapporto $t$ della combinazione, da confrontare con $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** La (a) dà l'effetto marginale; la (b) e la (c) sono i test sui due coefficienti; dalla (d) alla (f) si valuta l'effetto in $x_0$ e si verifica che non sia nullo.
>
> **(a)** $\Delta\log(\text{salario})\approx(\beta_1+\beta_3\,\text{esper})\,\Delta\text{istr}$ con $\Delta\text{istr}=1$: dipende dall'esperienza, attraverso $\beta_3$.
>
> **(b)** $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$: $t={{e04_08.t3|m}}$, in valore assoluto maggiore di $1{,}96$, si rifiuta $H_0$ e l'effetto dell'istruzione dipende dall'esperienza.
>
> **(c)** $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$: $t={{e04_08.t1|m}}$, in valore assoluto minore di $1{,}96$, non si rifiuta $H_0$. $\beta_1$ si riferisce a un lavoratore con $\text{esper}=0$.
>
> **(d)** $100\,(\hat\beta_1+x_0\,\hat\beta_3)=100\times\bigl({{e04_08.b1|m}}+{{e04_08.x0|m}}\times{{e04_08.b3|m}}\bigr)={{e04_08.eff|m}}\%$.
>
> **(e)** $100\sqrt{ {{e04_08.s1|m}}^2+{{e04_08.x0|m}}^2\times{{e04_08.s3|m}}^2+2\times{{e04_08.x0|m}}\times({{e04_08.cov|m}}) }={{e04_08.se|m}}$ punti percentuali.
>
> **(f)** L'intervallo di confidenza al 95\% per l'effetto è ${{e04_08.eff|m}}\pm 1{,}96\times{{e04_08.se|m}}=[{{e04_08.lo|m}};\,{{e04_08.hi|m}}]$ e lo zero ne è fuori. Lo stesso dice $t={{e04_08.eff|m}}/{{e04_08.se|m}}={{e04_08.t_eff|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Concludere dalla (c) che l'istruzione non conta: $\hat\beta_1$ non significativo dice solo che l'effetto per un lavoratore senza esperienza non si distingue da zero; con ${{e04_08.x0|m}}$ anni di esperienza l'effetto è ${{e04_08.eff|m}}\%$ ed è significativo. Un altro errore è dimenticare la covarianza: l'errore standard sarebbe ${{e04_08.se_ing|m}}$ invece di ${{e04_08.se|m}}$, il rapporto $t$ scenderebbe a ${{e04_08.t_ing|m}}$ e non si rifiuterebbe $H_0$. $\hat\beta_1$ e $\hat\beta_3$ sono fortemente correlati negativamente, perché `istr` e il prodotto si muovono insieme.

> [!success] Risposta
> **(a)** L'effetto marginale dell'istruzione è $\beta_1+\beta_3\,\text{esper}$, quindi dipende dall'esperienza. **(b)** Si rifiuta $H_0:\beta_3=0$. **(c)** Non si rifiuta $H_0:\beta_1=0$: $\beta_1$ è l'effetto per $\text{esper}=0$. **(d)** Con ${{e04_08.x0|m}}$ anni di esperienza un anno di istruzione in più fa aumentare il salario di circa ${{e04_08.eff|m}}\%$. **(e)** L'errore standard è ${{e04_08.se|m}}$ punti percentuali. **(f)** Si rifiuta $H_0:\beta_1+{{e04_08.x0|m}}\,\beta_3=0$: l'effetto è significativo.

![Effetto marginale dell'istruzione in funzione dell'esperienza, con la banda al 95\% calcolata con la covarianza: il punto ambra è $\hat\beta_1$ (esperienza nulla, banda che comprende lo zero), il punto verde è l'effetto a ${{e04_08.x0|m}}$ anni, ${{e04_08.eff|m}}\%$, significativamente diverso da zero.]({{e04_08.fig.effetto}}){width=85%}

{{testo:e04_09}}

> [!tip] Richiamo
> Con $\beta_3(\text{pub}\times\text{promo})$ l'effetto di mille euro in più di pubblicità è $\Delta\log(y)=(\beta_2+\beta_3\,\text{promo})\,\Delta\text{pub}$: $\beta_2$ senza promozione, $\beta_2+\beta_3$ con la promozione, in percentuale $100\times$ questi valori. La differenza fra due profili è la differenza delle medie condizionate: A (promo $=1$, pub $=p_A$) e B (promo $=0$, pub $=p_B$) differiscono di $\beta_1+(p_A-p_B)\,\beta_2+p_A\,\beta_3$. Per una combinazione $w_1\hat\beta_1+w_2\hat\beta_2+w_3\hat\beta_3$,
> $$\text{Var}=\sum_i w_i^2\,\text{Var}(\hat\beta_i)+2\sum_{i<j}w_iw_j\,\text{Cov}(\hat\beta_i,\hat\beta_j).$$
> Si decide con il rapporto $t=(\text{stima}-q)/\widehat{\text{se}}$ confrontato con $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** La (a) e la (b) riguardano la combinazione $\beta_2+\beta_3$ (due termini, una covarianza); dalla (c) alla (e) il confronto fra A e B è una combinazione di tre termini (tre covarianze).
>
> **(a)** $100\,(\hat\beta_2+\hat\beta_3)=100\times({{e04_09.b2|m}}+({{e04_09.b3|m}}))={{e04_09.eff|m}}\%$.
>
> **(b)** $\widehat{\text{se}}(\hat\beta_2+\hat\beta_3)=\sqrt{ {{e04_09.s2|m}}^2+{{e04_09.s3|m}}^2+2\times({{e04_09.c_pp|m}}) }={{e04_09.se_eff|m}}$. L'intervallo di confidenza al 95\% per $\beta_2+\beta_3$ è $[{{e04_09.eff_lo|m}};\,{{e04_09.eff_hi|m}}]$ e contiene ${{e04_09.kappa|m}}$. Lo stesso dice $t=\dfrac{ {{e04_09.b_eff|m}}-{{e04_09.kappa|m}} }{ {{e04_09.se_eff|m}} }={{e04_09.t_riv|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.
>
> **(c)** Con $p_A-p_B={{e04_09.dpub|m}}$ la differenza è $\beta_1+{{e04_09.dpub|m}}\,\beta_2+{{e04_09.pa|m}}\,\beta_3$, stimata da $100\times\bigl({{e04_09.b1|m}}+{{e04_09.dpub|m}}\times{{e04_09.b2|m}}+{{e04_09.pa|m}}\times({{e04_09.b3|m}})\bigr)={{e04_09.diff|m}}\%$.
>
> **(d)** $\widehat{\text{Var}}={{e04_09.s1|m}}^2+{{e04_09.dpub|m}}^2\times{{e04_09.s2|m}}^2+{{e04_09.pa|m}}^2\times{{e04_09.s3|m}}^2+2\times{{e04_09.dpub|m}}\times({{e04_09.c_ap|m}})+2\times{{e04_09.pa|m}}\times({{e04_09.c_ai|m}})+2\times{{e04_09.dpub|m}}\times{{e04_09.pa|m}}\times({{e04_09.c_pp|m}})={{e04_09.var_diff|m}}$, quindi $100\sqrt{ {{e04_09.var_diff|m}} }={{e04_09.se_diff|m}}$ punti percentuali.
>
> **(e)** L'intervallo di confidenza al 95\% è ${{e04_09.diff|m}}\pm 1{,}96\times{{e04_09.se_diff|m}}=[{{e04_09.lo|m}};\,{{e04_09.hi|m}}]$ e lo zero ne è fuori; $t={{e04_09.t_diff|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.

> [!warning] Errore tipico
> Scambiare $\beta_2$ con l'effetto con la promozione: $\hat\beta_2$ vale solo per i negozi senza promozione, per gli altri serve $\hat\beta_2+\hat\beta_3$. Un altro errore è confrontare A e B con il solo $\hat\beta_1$, trascurando che hanno anche una spesa pubblicitaria diversa, o dimenticare uno dei tre termini di covarianza. Il peso di $\beta_3$ è $p_A$ e non $p_A-p_B$: il prodotto $\text{pub}\times\text{promo}$ vale $p_A$ per A e $0$ per B.

> [!success] Risposta
> **(a)** Con la promozione mille euro in più di pubblicità fanno crescere le vendite di circa ${{e04_09.eff|m}}\%$. **(b)** $t={{e04_09.t_riv|m}}$: non si rifiuta $H_0:\beta_2+\beta_3={{e04_09.kappa|m}}$, l'affermazione è compatibile con i dati. **(c)** Le vendite di A superano quelle di B di circa ${{e04_09.diff|m}}\%$. **(d)** L'errore standard della differenza è ${{e04_09.se_diff|m}}$ punti percentuali. **(e)** Lo zero è fuori dall'intervallo di confidenza: si rifiuta l'ipotesi che A e B abbiano le stesse vendite attese.

![A sinistra il log-vendite atteso in funzione della pubblicità, con e senza promozione; i punti sono i negozi A e B. A destra l'intervallo di confidenza al 95\% per la loro differenza, in percentuale: lo zero è fuori.]({{e04_09.fig.profili}}){width=85%}

{{testo:e04_10}}

> [!tip] Richiamo
> Senza costante e con $G$ dummy che sommano a 1, ogni coefficiente $\delta_j$ è il livello (l'intercetta) della zona $j$, non una differenza: le dummy sommano a 1, prendono il posto della costante e nessuna va eliminata (con la costante ne andrebbe tolta una, trappola delle dummy). Il modello equivalente con la costante e $G-1$ dummy, con la zona 4 di riferimento, ha costante $\delta_4$ e coefficienti $\delta_j-\delta_4$, stessa SSR e stessi valori stimati. La zona non ha rilevanza se i livelli sono uguali: $H_0:\delta_1=\delta_2=\delta_3=\delta_4$, cioè $G-1$ restrizioni indipendenti ($\delta_1-\delta_4=0$, $\delta_2-\delta_4=0$, $\delta_3-\delta_4=0$). Il modello ristretto ha una costante comune e
> $$F=\frac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-p)},$$
> con $p$ i parametri del modello completo. Qui si usano le SSR: l'$R^2$ di un modello senza costante non è calcolato rispetto alla media e non è confrontabile con quello del modello con la costante.

> [!example] Svolgimento
> **Impostazione.** Le tre domande iniziali traducono la richiesta in un sistema d'ipotesi; poi si calcola $F$ dalle due SSR e si riscrive il modello con una zona di riferimento.
>
> **(a)** Le quattro dummy sommano a 1, come farebbe la costante: sono già esaustive e il modello non ha costante, quindi non c'è collinearità perfetta e nessuna dummy va eliminata. $\delta_j$ è l'intercetta specifica della zona $j$; le differenze $\delta_j-\delta_k$ sono i divari a parità di `crime` e `rooms`. Le stime sono ${{e04_10.d1|m}}$, ${{e04_10.d2|m}}$, ${{e04_10.d3|m}}$ e ${{e04_10.d4|m}}$.
>
> **(b)** $H_0:\delta_1=\delta_2=\delta_3=\delta_4$ contro $H_1$: almeno una delle uguaglianze non vale. Sotto $H_0$ resta una sola costante comune.
>
> **(c)** Tre uguaglianze indipendenti: $s={{e04_10.s|m}}$, pari alla differenza fra i parametri dei due modelli, ${{e04_10.p|m}}-{{e04_10.p_r|m}}$.
>
> **(d)** $n-p={{e04_10.n|m}}-{{e04_10.p|m}}={{e04_10.df|m}}$.
>
> **(e)** $F=\dfrac{ ({{e04_10.ssr_r|m}}-{{e04_10.ssr_c|m}})/{{e04_10.s|m}} }{ {{e04_10.ssr_c|m}}/{{e04_10.df|m}} }=\dfrac{ {{e04_10.dssr|m}}/{{e04_10.s|m}} }{ {{e04_10.ssr_c|m}}/{{e04_10.df|m}} }={{e04_10.F|m}}$.
>
> **(f)** $F={{e04_10.F|m}}$ è maggiore del valore critico ${{e04_10.fcrit|m}}$: si rifiuta $H_0$.
>
> **(g)** Con la zona 4 di riferimento la costante è il livello della zona 4: $\hat\delta_4={{e04_10.cost|m}}$.
>
> **(h)** Il coefficiente di `zona1` è la differenza fra i livelli: $100\,(\hat\delta_1-\hat\delta_4)=100\times({{e04_10.d1|m}}-{{e04_10.d4|m}})={{e04_10.coef1|m}}\%$.

> [!warning] Errore tipico
> Credere che manchi una dummy o che la costante sia stata dimenticata: qui la costante è assente per costruzione. Un altro errore è leggere $\delta_1$ come differenza rispetto a una zona di riferimento, mentre è il livello della zona 1. Infine non si deve calcolare $F$ con gli $R^2$ stampati da un software per il modello senza costante: non sono confrontabili con quelli del modello con la costante, e con le SSR il confronto è corretto in ogni caso.

> [!success] Risposta
> **(a)** Le quattro dummy sommano a 1 e sostituiscono la costante, che non c'è: nessuna va eliminata e ogni $\delta_j$ è il livello della zona $j$. **(b)** $H_0:\delta_1=\delta_2=\delta_3=\delta_4$ contro $H_1$: almeno una uguaglianza non vale. **(c)** $s={{e04_10.s|m}}$. **(d)** ${{e04_10.df|m}}$ gradi di libertà. **(e)** $F={{e04_10.F|m}}$. **(f)** $F$ supera il valore critico ${{e04_10.fcrit|m}}$: si rifiuta $H_0$, la zona ha rilevanza nel livello dei prezzi. **(g)** La costante vale ${{e04_10.cost|m}}$. **(h)** Il coefficiente di `zona1` vale ${{e04_10.coef1|m}}\%$.

![A sinistra i quattro livelli stimati $\hat\delta_j$ e la costante del modello ristretto (linea tratteggiata). A destra le differenze fra ciascuna zona e la zona 4, in percentuale, con intervallo al 95\%: sono i coefficienti del modello con la costante e le tre dummy, e il test $F$ le verifica insieme.]({{e04_10.fig.livelli}}){width=85%}

{{testo:e04_11}}

> [!tip] Richiamo
> Con la costante e le dummy `nord` e `sud` (riferimento: centro) le medie condizionate sono $E[y\mid\text{centro}]=\alpha$, $E[y\mid\text{nord}]=\alpha+\delta_1$ ed $E[y\mid\text{sud}]=\alpha+\delta_2$ (a parità del resto). Con il sud come riferimento e le dummy `centro` e `nord` le stesse medie sono $\alpha'$, $\alpha'+\delta_1'$ e $\alpha'+\delta_2'$: quindi $\alpha'=\alpha+\delta_2$, $\delta_1'=-\delta_2$ e $\delta_2'=\delta_1-\delta_2$. Il modello non cambia, cambia solo la lettura dei coefficienti. L'errore standard di una differenza è $\sqrt{\text{Var}(\hat\delta_1)+\text{Var}(\hat\delta_2)-2\,\text{Cov}(\hat\delta_1,\hat\delta_2)}$, e il test $F$ sull'irrilevanza dell'area, che confronta con un modello senza dummy, non dipende dal riferimento.

> [!example] Svolgimento
> **Impostazione.** Si leggono i due test della tabella, poi si ricostruiscono i coefficienti del modello con il Sud come riferimento come combinazioni lineari di quelli stampati.
>
> **(a)** $H_0:\delta_1=0$: $t={{e04_11.tn|m}}$, in valore assoluto minore di $1{,}96$, non si rifiuta $H_0$.
>
> **(b)** $H_0:\delta_2=0$: $t={{e04_11.ts|m}}$, in valore assoluto minore di $1{,}96$, non si rifiuta $H_0$.
>
> **(c)** $\hat\delta_1'=-\hat\delta_2$: $100\times(-({{e04_11.bs|m}}))={{e04_11.centro|m}}\%$.
>
> **(d)** $\hat\delta_2'=\hat\delta_1-\hat\delta_2$: $100\times({{e04_11.bn|m}}-({{e04_11.bs|m}}))={{e04_11.nord|m}}\%$.
>
> **(e)** $\widehat{\text{se}}(\hat\delta_2')=100\sqrt{ {{e04_11.sn|m}}^2+{{e04_11.ss|m}}^2-2\times({{e04_11.cov|m}}) }={{e04_11.se|m}}$ punti percentuali.
>
> **(f)** $t={{e04_11.nord|m}}/{{e04_11.se|m}}={{e04_11.t_ns|m}}$, in valore assoluto maggiore di $1{,}96$; l'intervallo di confidenza al 95\% è $[{{e04_11.lo|m}};\,{{e04_11.hi|m}}]$ e lo zero ne è fuori: si rifiuta $H_0$.
>
> **(g)** No: i valori stimati, la SSR e il modello ristretto senza dummy sono gli stessi, quindi $F$ non cambia.

> [!warning] Errore tipico
> Dedurre dal fatto che il Nord e il Sud non differiscono significativamente dal Centro che il Nord e il Sud non differiscono fra loro. Ogni test della tabella confronta un'area con il riferimento; il confronto fra Nord e Sud è un'altra combinazione lineare, $\delta_1-\delta_2$, con un altro errore standard. Se si omette la covarianza l'errore standard diventa ${{e04_11.se_ing|m}}$ invece di ${{e04_11.se|m}}$ e non si rifiuta: i due stimatori sono correlati positivamente perché condividono la stima del riferimento, e la covarianza riduce la varianza della differenza.

> [!success] Risposta
> **(a)** Non si rifiuta $H_0:\delta_1=0$. **(b)** Non si rifiuta $H_0:\delta_2=0$. **(c)** $\hat\delta_1'={{e04_11.centro|m}}\%$. **(d)** $\hat\delta_2'={{e04_11.nord|m}}\%$. **(e)** L'errore standard è ${{e04_11.se|m}}$ punti percentuali. **(f)** Nel nuovo modello si rifiuta $H_0:\delta_2'=0$: il Nord e il Sud differiscono significativamente, pur non differendo significativamente dal Centro. **(g)** No: cambiare la categoria di riferimento non cambia $F$.

![Coefficienti delle aree in percentuale, con intervallo al 95\%. A sinistra con il Centro come riferimento: entrambi gli intervalli comprendono lo zero. A destra con il Sud come riferimento: l'intervallo del Nord ne è fuori.]({{e04_11.fig.basi}}){width=85%}

{{testo:e04_12}}

> [!tip] Richiamo
> Il modello ristretto si ottiene imponendo $H_0$ nel modello completo e riscrivendolo: con $\beta_2=\beta_1$ e $\beta_3=0$ il termine $\beta_1\,\text{istr}+\beta_2\,\text{esper}$ diventa $\beta_1\,(\text{istr}+\text{esper})$ e `anz` sparisce. Con $s$ restrizioni,
> $$F=\frac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-k-1)},$$
> da confrontare con il valore critico. Per una sola restrizione lineare $\beta_1=\beta_2$ la statistica $F$ è il quadrato di $t=(\hat\beta_1-\hat\beta_2)/\widehat{\text{se}}$, con
> $$\widehat{\text{se}}=\sqrt{\text{Var}(\hat\beta_1)+\text{Var}(\hat\beta_2)-2\,\text{Cov}(\hat\beta_1,\hat\beta_2)}.$$

> [!example] Svolgimento
> **Impostazione.** Due restrizioni si testano insieme con $F$ dalle SSR dei due modelli; la prima, presa da sola, si può testare anche con una $t$.
>
> **(a)** $\beta_1=\beta_2$ e $\beta_3=0$: $s={{e04_12.s|m}}$ (il modello completo ha $k={{e04_12.k|m}}$ regressori, il ristretto due).
>
> **(b)** $n-k-1={{e04_12.n|m}}-{{e04_12.k|m}}-1={{e04_12.df|m}}$.
>
> **(c)** $F=\dfrac{ ({{e04_12.ssr_r|m}}-{{e04_12.ssr_c|m}})/{{e04_12.s|m}} }{ {{e04_12.ssr_c|m}}/{{e04_12.df|m}} }=\dfrac{ {{e04_12.dssr|m}}/{{e04_12.s|m}} }{ {{e04_12.ssr_c|m}}/{{e04_12.df|m}} }={{e04_12.F|m}}$.
>
> **(d)** $F={{e04_12.F|m}}$ è maggiore del valore critico ${{e04_12.fcrit|m}}$: si rifiuta $H_0$.
>
> **(e)** $\hat\beta_1-\hat\beta_2={{e04_12.b1|m}}-{{e04_12.b2|m}}={{e04_12.dif|m}}$ e $\widehat{\text{se}}=\sqrt{ {{e04_12.s1|m}}^2+{{e04_12.s2|m}}^2-2\times({{e04_12.cov|m}}) }={{e04_12.se_dif|m}}$, quindi $t=\dfrac{ {{e04_12.dif|m}} }{ {{e04_12.se_dif|m}} }={{e04_12.t1|m}}$ e $F=t^2={{e04_12.F1|m}}$.
>
> **(f)** $|t|={{e04_12.t1|m}}$ è maggiore di $1{,}96$: si rifiuta $H_0:\beta_1=\beta_2$.
>
> **(g)** Sotto $H_0$ si sostituisce $\beta_2=\beta_1$ e si pone $\beta_3=0$: $\beta_1\,\text{istr}+\beta_1\,\text{esper}=\beta_1\,(\text{istr}+\text{esper})$. Il modello ristretto ha come regressori la somma `istr_esper` e `donna`.

> [!warning] Errore tipico
> Imporre solo $\beta_3=0$, o solo $\beta_1=\beta_2$, nel modello ristretto: il numero di restrizioni $s$ e la SSR non sono più quelli di $H_0$. Un altro errore è togliere `istr` e `esper` dal modello ristretto invece di sostituirle con la loro somma: $\beta_1=\beta_2$ non significa $\beta_1=\beta_2=0$. Infine nella $t$ non va dimenticata la covarianza: in generale l'errore standard della differenza dipende dal termine $-2\,\widehat{\text{Cov}}$ (qui è piccolo, perché istruzione ed esperienza sono quasi incorrelate).

> [!success] Risposta
> **(a)** $s={{e04_12.s|m}}$. **(b)** $n-k-1={{e04_12.df|m}}$. **(c)** $F={{e04_12.F|m}}$. **(d)** $F$ supera il valore critico ${{e04_12.fcrit|m}}$: si rifiuta $H_0$, istruzione ed esperienza non hanno lo stesso effetto oppure l'anzianità conta. **(e)** Per la sola restrizione $\beta_1=\beta_2$, $F=t^2={{e04_12.F1|m}}$. **(f)** Si rifiuta anche $H_0:\beta_1=\beta_2$: un anno di istruzione e uno di esperienza non valgono lo stesso. **(g)** Si sostituiscono $\beta_2=\beta_1$ e $\beta_3=0$ e si usa la somma `istr`$+$`esper` come unico regressore.

![A sinistra le SSR del modello completo e del ristretto: imporre $H_0$ le fa crescere. A destra la densità $F({{e04_12.s|m}},\,{{e04_12.df|m}})$: la statistica ${{e04_12.F|m}}$ cade nella regione di rifiuto, oltre il valore critico ${{e04_12.fcrit|m}}$.]({{e04_12.fig.f}}){width=85%}
