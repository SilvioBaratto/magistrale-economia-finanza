{{testo:e05_01}}

> [!tip] Richiamo
> L'omoschedasticità richiede che $\text{Var}(\epsilon_i\mid X)=\sigma^2$ sia la stessa per ogni osservazione. I residui $\hat\epsilon_i$ sono la proxy osservabile degli errori, quindi il grafico di $\hat\epsilon$ contro $\hat y$ deve mostrare una fascia orizzontale di ampiezza costante attorno allo zero. Se l'ampiezza cresce o diminuisce con $\hat y$, la varianza condizionale dipende dai regressori: c'è eteroschedasticità. Gli stimatori OLS restano non distorti e consistenti, ma gli errori standard calcolati come radice di $\hat\sigma^2/\sum_i(x_i-\bar x)^2$ non sono consistenti e i test $t$ che li usano non sono affidabili.

> [!example] Svolgimento
> **Impostazione.** Si guarda l'ampiezza verticale dei residui al variare di $\hat y$: la media complessiva dei residui è zero per costruzione (con la costante); per l'omoschedasticità conta l'ampiezza della dispersione, mentre un andamento sistematico della posizione dei residui segnalerebbe non linearità.
>
> **(a)** Nel Modello A i residui sono poco dispersi per $\hat y$ piccolo e sempre più dispersi al crescere di $\hat y$: è una forma a ventaglio. La deviazione standard dei residui nel quarto quartile dei valori predetti è circa ${{e05_01.rapporto_a|m}}$ volte quella del primo. Il grafico non è coerente con l'omoschedasticità.
>
> **(b)** Nel Modello B i residui formano una fascia orizzontale di ampiezza costante: il rapporto fra le deviazioni standard del quarto e del primo quartile è ${{e05_01.rapporto_b|m}}$. Il grafico è coerente con l'omoschedasticità.
>
> **(c)** Nel Modello A la varianza degli errori dipende da $\hat y$, quindi $\hat\sigma^2/\sum_i(x_i-\bar x)^2$ non stima correttamente la varianza di $\hat\beta_1$: i test $t$ usuali non sono affidabili e vanno sostituiti da quelli con errori standard robusti.

> [!warning] Errore tipico
> Guardare la posizione dei residui invece della loro ampiezza: la media complessiva dei residui è zero per costruzione (con la costante), mentre per l'omoschedasticità conta l'ampiezza della dispersione; un andamento sistematico della posizione dei residui segnalerebbe invece non linearità. Un altro errore è concludere dal Modello B che l'omoschedasticità sia dimostrata: il grafico è solo indicativo, e per escludere l'eteroschedasticità serve un test.

> [!success] Risposta
> **(a)** No: la dispersione dei residui del Modello A aumenta con $\hat y$ (ventaglio). **(b)** Sì: nel Modello B la dispersione è costante. **(c)** No: con l'eteroschedasticità gli errori standard usuali non sono consistenti, quindi per i test $t$ del Modello A servono errori standard robusti.

![Deviazione standard dei residui in ciascun quartile dei valori predetti: nel Modello A cresce (il quarto quartile vale circa ${{e05_01.rapporto_a|m}}$ volte il primo), nel Modello B resta costante.]({{e05_01.fig.quartili}}){width=85%}

{{testo:e05_02}}

> [!tip] Richiamo
> Il test di Breusch-Pagan assume $\text{Var}(\epsilon\mid X)=\delta_0+\delta_1X_1+\dots+\delta_kX_k$, per cui $H_0:\text{Var}(\epsilon\mid X)=\sigma^2$ equivale a $H_0:\delta_1=\dots=\delta_k=0$ contro $H_1$: almeno un $\delta_j\neq 0$. Poiché $\epsilon^2$ non è osservabile, si stima la regressione ausiliaria di $\hat\epsilon^2$ sui regressori e si calcola $LM=nR^2_{\hat\epsilon^2}$, che sotto $H_0$ è approssimativamente $\chi^2_k$. Si rifiuta $H_0$ se $LM$ supera il valore critico. Se non si rifiuta, non si accetta $H_0$: il test al più permette di rifiutarla.

> [!example] Svolgimento
> **Impostazione.** La statistica si ricava da $n$ e da $R^2$ della regressione ausiliaria, poi si confronta con il valore critico della $\chi^2_{{{e05_02.k}}}$.
>
> **(a)** $LM=nR^2={{e05_02.n}}\times{{e05_02.r2|m}}={{e05_02.lm|m}}$.
>
> **(b)** $LM={{e05_02.lm|m}}>{{e05_02.crit|m}}$, il valore critico al 5\%: si rifiuta $H_0$. La varianza degli errori dipende dai regressori.
>
> **(c)** Sì. Rifiutata l'omoschedasticità, gli errori standard usuali non sono affidabili e per i test $t$ conviene usare gli errori standard robusti di White.

> [!warning] Errore tipico
> Confrontare $R^2$ con il valore critico senza moltiplicarlo per $n$, oppure decidere dai singoli rapporti $t$ della regressione ausiliaria: l'ipotesi è congiunta ($\delta_1=\delta_2=\delta_3=0$) e la statistica da usare è $LM=nR^2$.

> [!success] Risposta
> **(a)** $LM={{e05_02.lm|m}}$. **(b)** $LM$ supera il valore critico ${{e05_02.crit|m}}$ della $\chi^2_{{{e05_02.k}}}$ al 5\%, quindi si rifiuta $H_0$: c'è evidenza di eteroschedasticità. **(c)** Sì, conviene usare gli errori standard robusti.

![Statistica $LM={{e05_02.lm|m}}$ nella coda della $\chi^2_{{{e05_02.k}}}$: ben oltre il valore critico ${{e05_02.crit|m}}$.]({{e05_02.fig.chi2}}){width=85%}

{{testo:e05_03}}

> [!tip] Richiamo
> Sotto eteroschedasticità $\hat\beta_j$ resta non distorto e consistente, ma l'errore standard usuale non è consistente. White stima la varianza vera con i residui: $\widehat{\text{Var}}(\hat\beta_j)=\dfrac{\sum_i\hat r_{ij}^2\,\hat\epsilon_i^2}{\bigl(\sum_i\hat r_{ij}^2\bigr)^2}$, dove $\hat r_{ij}$ è il residuo della regressione di $x_j$ sugli altri regressori; i software moltiplicano per $n/(n-k-1)$ (variante HC1). I coefficienti non cambiano, cambiano solo gli errori standard e quindi $t=\hat\beta_j/\widehat{\text{se}}(\hat\beta_j)$, gli intervalli e i p-value. Si rifiuta $H_0:\beta_j=0$ se $|t|>1{,}96$.

> [!example] Svolgimento
> **Impostazione.** Cambia solo il denominatore del rapporto $t$: si confrontano i due errori standard di $\hat\beta_2$ e si rifà il test con ciascuno.
>
> **(a)** $\dfrac{\widehat{\text{se}}_{\text{rob}}}{\widehat{\text{se}}_{\text{us}}}=\dfrac{ {{e05_03.se_robusto|m}} }{ {{e05_03.se_usuale|m}} }={{e05_03.fattore|m}}$.
>
> **(b)** Con gli errori standard usuali $t={{e05_03.b|m}}/{{e05_03.se_usuale|m}}={{e05_03.t_usuale|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(c)** Con gli errori standard robusti $t={{e05_03.b|m}}/{{e05_03.se_robusto|m}}={{e05_03.t_robusto|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$. L'intervallo di confidenza al 95\% robusto, $[{{e05_03.ic_lo|m}};\,{{e05_03.ic_hi|m}}]$, contiene lo zero.
>
> **(d)** No: il coefficiente di `giardino` è ${{e05_03.b|m}}$ in entrambe le tabelle, e lo stesso vale per gli altri coefficienti. Gli errori standard robusti correggono solo la precisione delle stime.

> [!warning] Errore tipico
> Credere che gli errori standard robusti modifichino le stime dei coefficienti, oppure fermarsi alla tabella con gli errori standard usuali. Un altro errore è pensare che quelli robusti siano sempre più grandi: qui lo sono, ma il segno della correzione dipende da dove si concentrano i residui grandi rispetto ai $\hat r_{ij}^2$.

> [!success] Risposta
> **(a)** L'errore standard robusto è ${{e05_03.fattore|m}}$ volte quello usuale. **(b)** Con gli errori standard usuali si rifiuta $H_0$ ($t={{e05_03.t_usuale|m}}$). **(c)** Con quelli robusti non si rifiuta ($t={{e05_03.t_robusto|m}}$): la conclusione sul giardino cambia. **(d)** No, i coefficienti sono gli stessi. Gli errori standard robusti sono validi in ogni caso; il divario rispetto agli usuali suggerisce eteroschedasticità.

![Intervalli di confidenza al 95\% per il coefficiente di `giardino`: con gli errori standard robusti l'intervallo, $[{{e05_03.ic_lo|m}};\,{{e05_03.ic_hi|m}}]$, contiene lo zero; con quelli usuali no.]({{e05_03.fig.intervalli}}){width=85%}

{{testo:e05_04}}

> [!tip] Richiamo
> I residui al quadrato $\hat\epsilon_i^2$ sono la proxy della varianza condizionale. Si stima la regressione ausiliaria $\hat\epsilon^2=a+b\,\hat y+u$ e si verifica $H_0:b=0$ con la statistica $t=\hat b/\widehat{\text{se}}(\hat b)$: se $|t|>1{,}96$ si rifiuta, cioè la varianza dei residui dipende dai valori predetti e c'è eteroschedasticità. Il segno di $\hat b$ dice in che direzione: con $\hat b>0$ la varianza cresce con $\hat y$, con $\hat b<0$ decresce. La varianza stimata per un valore $y_0$ è $\hat a+\hat b\,y_0$.

> [!example] Svolgimento
> **Impostazione.** Il grafico e la pendenza $\hat b$ danno la stessa informazione: la direzione della dispersione. Il test su $b$ la rende formale.
>
> **(a)** Nel grafico i residui sono molto dispersi per $\hat y$ piccolo e si stringono verso destra. Lo conferma $\hat b={{e05_04.b|m}}<0$: la varianza dei residui diminuisce al crescere di $\hat y$.
>
> **(b)** $H_0:b=0$ contro $H_1:b\neq 0$. Il rapporto $t$ vale ${{e05_04.t|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(c)** $\hat a+\hat b\,y_0={{e05_04.a|m}}+({{e05_04.b|m}})\times{{e05_04.y0|m}}={{e05_04.var|m}}$, e la deviazione standard è $\sqrt{ {{e05_04.var|m}} }={{e05_04.sd|m}}$.
>
> **(d)** Sì: rifiutata l'omoschedasticità, gli errori standard usuali non sono affidabili.

> [!warning] Errore tipico
> Leggere la risposta «no» alla (a) come assenza di eteroschedasticità: il test cerca una dipendenza in qualunque direzione, e una varianza che decresce con $\hat y$ è eteroschedasticità quanto una che cresce. Un altro errore è interpretare $\hat a+\hat b\,y_0$ come deviazione standard, senza la radice quadrata.

> [!success] Risposta
> **(a)** No: la dispersione dei residui diminuisce al crescere di $\hat y$ ($\hat b={{e05_04.b|m}}$). **(b)** $t={{e05_04.t|m}}$, si rifiuta $H_0:b=0$: la varianza dipende dai valori predetti. **(c)** Per $\hat y={{e05_04.y0|m}}$ la varianza stimata è ${{e05_04.var|m}}$ e la deviazione standard circa ${{e05_04.sd|m}}$. **(d)** Sì, conviene usare gli errori standard robusti.

![Residui al quadrato contro valori predetti: la retta ausiliaria è decrescente e in $\hat y={{e05_04.y0|m}}$ vale ${{e05_04.var|m}}$.]({{e05_04.fig.ausiliaria}}){width=85%}

{{testo:e05_05}}

> [!tip] Richiamo
> Breusch-Pagan e White hanno la stessa ipotesi nulla, l'omoschedasticità, ma alternative diverse. Breusch-Pagan regredisce $\hat\epsilon^2$ sui $k$ regressori e usa $LM=nR^2\sim\chi^2_k$; White aggiunge i quadrati e i prodotti dei regressori e usa $LM=nR^2\sim\chi^2_{\#\text{vincoli}}$, con molti più vincoli. Si rifiuta $H_0$ al 5\% se il p-value è minore di $0{,}05$. Nessuno di questi test accetta l'ipotesi nulla: al più permettono di rifiutarla. Se uno dei due rifiuta, la varianza condizionale dipende dai regressori e si usano errori standard robusti.

> [!example] Svolgimento
> **Impostazione.** Si confronta ogni p-value con $0{,}05$, poi si ragiona sul perché i due test possono discordare.
>
> **(a)** Breusch-Pagan, con ${{e05_05.gl_bp}}$ gradi di libertà: p-value {{e05_05.p_bp}}, minore di $0{,}05$: si rifiuta $H_0$.
>
> **(b)** White, con ${{e05_05.gl_w}}$ gradi di libertà: p-value {{e05_05.p_w}}, maggiore di $0{,}05$: non si rifiuta $H_0$.
>
> **(c)** No. Non rifiutare non significa accettare: White spende ${{e05_05.gl_w}}$ vincoli, fra quadrati e prodotti, e se la dipendenza è semplice (lineare in un regressore) ha meno potenza di Breusch-Pagan, che ne usa ${{e05_05.gl_bp}}$.
>
> **(d)** Sì: Breusch-Pagan rileva una dipendenza significativa di $\hat\epsilon^2$ dai regressori.

> [!warning] Errore tipico
> Considerare i due test in contraddizione e fidarsi di quello che non rifiuta, oppure dedurre dal non rifiuto di White che il modello sia omoschedastico. I test hanno alternative diverse, quindi i risultati possono discordare senza paradosso, e un test che non rifiuta non dimostra l'ipotesi nulla.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$ (p-value {{e05_05.p_bp}}). **(b)** Non si rifiuta $H_0$ (p-value {{e05_05.p_w}}). **(c)** No: il non rifiuto non accetta l'omoschedasticità, e White ha meno potenza perché usa più vincoli. **(d)** Sì: poiché Breusch-Pagan rifiuta, sembra ragionevole l'ipotesi di eteroschedasticità e conviene usare errori standard robusti.

![Breusch-Pagan (a sinistra) e White (a destra): solo il primo cade nella regione di rifiuto al 5\%.]({{e05_05.fig.test}}){width=85%}

{{testo:e05_06}}

> [!tip] Richiamo
> L'omoschedasticità non serve per la non distorsione e la consistenza di OLS: bastano $E[\epsilon\mid X]=0$ e le ipotesi usuali. Serve per la formula dell'errore standard. Con $\text{Var}(\epsilon_i\mid x_i)=\sigma_i^2$ la varianza vera di $\hat\beta_1$ è $\sum_i(x_i-\bar x)^2\sigma_i^2/\bigl[\sum_i(x_i-\bar x)^2\bigr]^2$, mentre $\hat\sigma^2/\sum_i(x_i-\bar x)^2$ non converge ad essa nemmeno per $n$ grande. Qui $\sigma_i^2=x_i^2$: la varianza vera tende a $E[x^4]/n=3/n$ e quella usuale a $1/n$, quindi l'errore standard usuale è sotto di un fattore $\sqrt{3}$ a ogni $n$. L'errore standard di White (HC1) è consistente.

> [!example] Svolgimento
> **Impostazione.** Si leggono tre cose dalla tabella: dove stanno le medie delle stime, quanto è larga la dispersione vera rispetto a quella usuale, e quante volte si rifiuta una $H_0$ vera.
>
> **(a)** Per ogni $n$ la media delle stime è vicina a ${{e05_06.beta|m}}$: lo scarto massimo vale ${{e05_06.z_max|m}}$ volte l'errore di simulazione, meno di $2$. OLS non è distorto, come atteso perché $E[\epsilon\mid x]=0$.
>
> **(b)** Per $n={{e05_06.n3}}$: ${{e05_06.dev|m}}/{{e05_06.mse_u|m}}={{e05_06.rapporto|m}}$, vicino al valore teorico $\sqrt 3={{e05_06.teorico|m}}$. Il $t$ usuale divide per un errore standard troppo piccolo.
>
> **(c)** Con il $t$ usuale si rifiuta la $H_0$ vera nel ${{e05_06.rif_u|m}}\%$ dei campioni, non nel $5\%$: lo scarto dal $5\%$ supera ${{e05_06.tol|m}}$ punti. Il problema non si attenua al crescere di $n$.
>
> **(d)** Con il $t$ robusto la frequenza è ${{e05_06.rif_r|m}}\%$, entro ${{e05_06.tol|m}}$ punti dal $5\%$.

> [!warning] Errore tipico
> Dedurre dagli errori standard sbagliati che anche le stime siano distorte, oppure aspettarsi che il problema sparisca con campioni grandi. Le stime sono non distorte e consistenti; è l'errore standard usuale a non essere consistente, e la frequenza di rifiuto resta lontana dal $5\%$ anche per $n={{e05_06.n3}}$.

> [!success] Risposta
> **(a)** No: la media delle stime resta entro due errori di simulazione dal valore vero per ogni $n$. **(b)** Circa ${{e05_06.rapporto|m}}$: la dispersione vera delle stime è molto maggiore dell'errore standard usuale. **(c)** No: il $t$ usuale rifiuta la $H_0$ vera nel ${{e05_06.rif_u|m}}\%$ dei casi, anche con $n={{e05_06.n3}}$. **(d)** Sì: il $t$ robusto rifiuta nel ${{e05_06.rif_r|m}}\%$ dei casi.

![Frequenza di rifiuto della $H_0$ vera al crescere di $n$: con gli errori standard usuali resta lontana dal $5\%$, con quelli robusti vi si avvicina.]({{e05_06.fig.frequenze}}){width=85%}

{{testo:e05_07}}

> [!tip] Richiamo
> La varianza di White è $\widehat{\text{Var}}(\hat\beta_j)=\dfrac{1}{\sum_i\hat r_{ij}^2}\cdot\dfrac{\sum_i\hat r_{ij}^2\,\hat\epsilon_i^2}{\sum_i\hat r_{ij}^2}$, dove $\hat r_{ij}$ è il residuo della regressione di $x_j$ sugli altri regressori (la variante HC1 la moltiplica per $n/(n-k-1)$). Il secondo fattore è la media dei $\hat\epsilon_i^2$ pesata con i $\hat r_{ij}^2$, mentre l'errore standard usuale, $\widehat{\text{Var}}(\hat\beta_j)=\hat\sigma^2/\sum_i\hat r_{ij}^2$, usa la media semplice. Se i residui grandi stanno dove $\hat r_{ij}^2$ è piccolo, cioè fra le osservazioni centrali del regressore, l'errore standard robusto è più piccolo di quello usuale. Intervallo al 95\%: $\hat\beta\pm 1{,}96\,\widehat{\text{se}}$.

> [!example] Svolgimento
> **Impostazione.** Si rifà lo stesso test con i due errori standard di $\hat\beta_2$ e si costruisce l'intervallo robusto.
>
> **(a)** $\dfrac{\widehat{\text{se}}_{\text{rob}}}{\widehat{\text{se}}_{\text{us}}}=\dfrac{ {{e05_07.se_robusto|m}} }{ {{e05_07.se_usuale|m}} }={{e05_07.fattore|m}}$.
>
> **(b)** $t={{e05_07.b|m}}/{{e05_07.se_usuale|m}}={{e05_07.t_usuale|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0$.
>
> **(c)** $t={{e05_07.b|m}}/{{e05_07.se_robusto|m}}={{e05_07.t_robusto|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0$.
>
> **(d)** L'estremo inferiore è ${{e05_07.b|m}}-1{,}96\times{{e05_07.se_robusto|m}}={{e05_07.ic_lo|m}}$; l'estremo superiore è ${{e05_07.ic_hi|m}}$. Lo zero è fuori dall'intervallo.

> [!warning] Errore tipico
> Credere che gli errori standard robusti siano sempre più grandi, e quindi più prudenti, di quelli usuali. Qui sono circa ${{e05_07.fattore|m}}$ volte quelli usuali: la correzione può andare in entrambe le direzioni, e può far diventare significativo un coefficiente che con gli errori standard usuali non lo era.

> [!success] Risposta
> **(a)** Il rapporto è ${{e05_07.fattore|m}}$: l'errore standard robusto è più piccolo. **(b)** Con gli errori standard usuali non si rifiuta $H_0:\beta_2=0$ ($t={{e05_07.t_usuale|m}}$). **(c)** Con quelli robusti si rifiuta ($t={{e05_07.t_robusto|m}}$): la conclusione cambia. **(d)** L'intervallo robusto al 95\% è $[{{e05_07.ic_lo|m}};\,{{e05_07.ic_hi|m}}]$, con estremo inferiore ${{e05_07.ic_lo|m}}$.

![A sinistra, residui contro `scarto`: sono più dispersi al centro che agli estremi, dove $\hat r_{ij}^2$ è grande. A destra, gli intervalli al 95\% per $\beta_2$: quello robusto è più stretto e non contiene lo zero.]({{e05_07.fig.scarto}}){width=85%}

{{testo:e05_08}}

> [!tip] Richiamo
> Il grafico di $\hat\epsilon$ contro $\hat y=X\hat\beta$ è solo indicativo: guarda la dispersione rispetto a una sola combinazione dei regressori. La varianza $\text{Var}(\epsilon\mid X)$ può dipendere da un singolo regressore che pesa poco su $\hat y$: allora il grafico appare omogeneo, ma la regressione ausiliaria di $\hat\epsilon^2$ sui regressori (Breusch-Pagan) lo rileva e rifiuta $H_0$ se il p-value è minore di $0{,}05$. Gli errori standard robusti sono validi anche in omoschedasticità, quindi un grafico pulito non basta a escluderli. La statistica $t$ robusta è $\hat\beta_j/\widehat{\text{se}}_{\text{rob}}(\hat\beta_j)$, da confrontare con $1{,}96$.

> [!example] Svolgimento
> **Impostazione.** Grafico e test rispondono a domande diverse: il grafico guarda $\hat y$, il test guarda tutti i regressori. Poi si rifà il $t$ con gli errori standard robusti.
>
> **(a)** I residui formano una nuvola di ampiezza costante rispetto a $\hat y$, senza ventaglio: è coerente con l'omoschedasticità.
>
> **(b)** Il p-value è {{e05_08.p_bp}}, minore di $0{,}05$: si rifiuta l'omoschedasticità. Il test rileva una dipendenza della varianza dai regressori; la figura mostra che riguarda `formazione`, che incide poco sui valori predetti, dove il grafico non la mostra.
>
> **(c)** No: il grafico non permette di escludere l'eteroschedasticità, e il test la rileva. In ogni caso gli errori standard robusti restano validi.
>
> **(d)** $t={{e05_08.b|m}}/{{e05_08.se_rob|m}}={{e05_08.t_rob|m}}$.
>
> **(e)** $|t|={{e05_08.t_rob|m}}>1{,}96$: si rifiuta $H_0:\beta_2=0$ anche con gli errori standard robusti.

> [!warning] Errore tipico
> Concludere dal grafico pulito che l'omoschedasticità valga e che gli errori standard robusti siano inutili. Il grafico contro $\hat y$ può nascondere una varianza che dipende da un solo regressore; nessun test può dimostrare l'omoschedasticità: può solo rilevare l'eteroschedasticità, e un grafico pulito non basta a escluderla.

> [!success] Risposta
> **(a)** Sì: nel grafico non c'è ventaglio. **(b)** Si rifiuta $H_0$ (p-value {{e05_08.p_bp}}): c'è eteroschedasticità. **(c)** No: il grafico non basta, perché guarda solo $\hat y$, mentre il test rileva una dipendenza della varianza dai regressori e la figura mostra che riguarda `formazione`. **(d)** $t_{\text{rob}}={{e05_08.t_rob|m}}$. **(e)** Si rifiuta $H_0:\beta_2=0$: `formazione` è significativa anche con gli errori standard robusti.

![A sinistra i residui contro $\hat y$ formano una nuvola; a destra, contro `formazione`, si allargano nettamente: la dipendenza della varianza riguarda questo regressore.]({{e05_08.fig.confronto}}){width=85%}

{{testo:e05_09}}

> [!tip] Richiamo
> Per $q$ restrizioni lineari la statistica $F$ usuale è $F=\dfrac{(\text{SSR}_R-\text{SSR}_U)/q}{\text{SSR}_U/(n-k-1)}$, con $\text{SSR}_R$ e $\text{SSR}_U$ le somme dei quadrati dei residui del modello ristretto e di quello completo; si rifiuta $H_0$ se $F$ supera il valore critico. Sotto eteroschedasticità questa $F$ non è affidabile. La versione robusta è una statistica di Wald, $F=\frac1q\,(R\hat\beta)'\bigl(R\hat V_{\text{rob}}R'\bigr)^{-1}(R\hat\beta)$ con $\hat V_{\text{rob}}$ la matrice di covarianza di White: non si calcola con le somme dei quadrati, la fornisce il software e si confronta con lo stesso valore critico.

> [!example] Svolgimento
> **Impostazione.** Il test di White dice se l'$F$ usuale è affidabile; poi si calcola l'$F$ usuale dalle due tabelle e la si confronta con quella robusta.
>
> **(a)** Il p-value di White è {{e05_09.p_w}}, minore di $0{,}05$: si rifiuta l'omoschedasticità.
>
> **(b)** $F=\dfrac{(\text{SSR}_R-\text{SSR}_U)/q}{\text{SSR}_U/(n-k-1)}=\dfrac{({{e05_09.ssr_r|m}}-{{e05_09.ssr_u|m}})/{{e05_09.q|m}}}{ {{e05_09.ssr_u|m}}/{{e05_09.gl|m}} }={{e05_09.F|m}}$.
>
> **(c)** ${{e05_09.F|m}}>{{e05_09.crit|m}}$, il valore critico al 5\%: con gli errori standard usuali si rifiuta $H_0$.
>
> **(d)** La $F$ robusta vale ${{e05_09.F_rob|m}}<{{e05_09.crit|m}}$: con gli errori standard robusti non si rifiuta $H_0$.
>
> **(e)** Sì: la conclusione cambia, da «rifiuta» a «non rifiuta».

> [!warning] Errore tipico
> Fidarsi della $F$ usuale dopo che White ha rifiutato l'omoschedasticità, oppure cercare di ricavare la $F$ robusta dalle somme dei quadrati dei residui: la formula con $\text{SSR}$ vale solo sotto omoschedasticità. Con l'eteroschedasticità l'$F$ usuale è sbagliata e può portare a rifiutare un'ipotesi nulla vera.

> [!success] Risposta
> **(a)** Si rifiuta l'omoschedasticità (p-value {{e05_09.p_w}}). **(b)** $F={{e05_09.F|m}}$. **(c)** Si rifiuta $H_0:\beta_2=\beta_3=0$, perché ${{e05_09.F|m}}$ supera ${{e05_09.crit|m}}$. **(d)** Non si rifiuta, perché la $F$ robusta, ${{e05_09.F_rob|m}}$, è sotto ${{e05_09.crit|m}}$. **(e)** Sì: poiché i residui sono eteroschedastici va considerata la $F$ robusta, e `formazione` e `ricerca` non risultano congiuntamente significative.

![$F$ usuale (a sinistra) e $F$ robusta (a destra) contro il valore critico al 5\%: la prima cade nella regione di rifiuto, la seconda no.]({{e05_09.fig.f}}){width=85%}

{{testo:e05_10}}

> [!tip] Richiamo
> Eteroschedasticità ed endogeneità sono due questioni distinte. L'eteroschedasticità riguarda $E[\epsilon^2\mid X]$ e lascia $\hat\beta$ non distorto e consistente, perché per questo basta $E[\epsilon\mid X]=0$; rende però sbagliato l'errore standard usuale. Un errore correlato con il regressore, $\text{Cov}(x,\epsilon)\neq 0$, distorce $\hat\beta$: nel modello semplice $\hat\beta_1\to\beta_1+\text{Cov}(x,\epsilon)/\text{Var}(x)$. Gli errori standard robusti correggono la varianza di $\hat\beta$, non la sua distorsione. Un test di White o di Breusch-Pagan che rifiuta dice solo che $E[\epsilon^2\mid X]$ non è costante, non che $E[\epsilon\mid X]\neq 0$.

> [!example] Svolgimento
> **Impostazione.** Si confrontano i tre scenari: nel II l'errore è eteroschedastico ma a media zero, nel III è omoschedastico ma correlato con $x$.
>
> **(a)** Scenario II: lo scarto della media dal valore vero è ${{e05_10.z_ii|m}}$ volte l'errore di simulazione, meno di $2$: OLS non è distorto. Il $t$ usuale rifiuta però la $H_0$ vera nel ${{e05_10.rif_u_ii|m}}\%$ dei casi e quello robusto nel ${{e05_10.rif_r_ii|m}}\%$.
>
> **(b)** Nello scenario III la distorsione media è la media delle stime meno ${{e05_10.beta|m}}$, cioè ${{e05_10.distorsione|m}}$. Coincide con $\text{Cov}(x,\epsilon)/\text{Var}(x)=\rho\gamma={{e05_10.teorica|m}}$.
>
> **(c)** Nello scenario III il $t$ robusto rifiuta la $H_0$ vera nel ${{e05_10.rif_r_iii|m}}\%$ dei casi (quello usuale nel ${{e05_10.rif_u_iii|m}}\%$), lontano dal $5\%$. Gli errori standard robusti misurano bene la dispersione delle stime, ma l'intervallo è centrato su una stima distorta, che dista dal valore vero circa ${{e05_10.bias_se|m}}$ deviazioni standard.
>
> **(d)** Il p-value di White, {{e05_10.p_w}}, rifiuta $H_0$: il campione è eteroschedastico. Ma nello scenario II $E[\epsilon\mid x]=0$ per costruzione, e la tabella mostra OLS non distorto.

> [!warning] Errore tipico
> Leggere il rifiuto del test di White come prova che il modello è endogeno o che le stime sono distorte, e pensare che gli errori standard robusti rimedino a una distorsione. Il test riguarda la varianza di $\epsilon$ e i robusti correggono solo gli errori standard: la distorsione dello scenario III resta.

> [!success] Risposta
> **(a)** No: nello scenario II OLS non è distorto (la media delle stime è a meno di due errori di simulazione dal valore vero). **(b)** La distorsione media dello scenario III vale ${{e05_10.distorsione|m}}$, cioè $\rho\gamma$. **(c)** No: anche con il $t$ robusto si rifiuta la $H_0$ vera nel ${{e05_10.rif_r_iii|m}}\%$ dei casi, perché gli errori standard robusti non eliminano la distorsione. **(d)** No: il test di White rifiuta l'omoschedasticità, cioè riguarda $E[\epsilon^2\mid X]$, e non dice nulla su $E[\epsilon\mid X]$.

![Distorsione media (a sinistra) e frequenza di rifiuto della $H_0$ vera con il $t$ robusto (a destra) nei tre scenari: solo nel III la distorsione è diversa da zero e il test robusto sbaglia.]({{e05_10.fig.scenari}}){width=85%}
