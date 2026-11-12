{{testo:e01_01}}

> [!tip] Richiamo
> In una tabella di contingenza si confrontano le percentuali di riga: per un gruppo con $n_g$ soggetti di cui $k_g$ hanno l'evento, la percentuale è $100\cdot k_g/n_g$. Confrontare i conteggi sarebbe sbagliato quando i gruppi hanno numerosità diverse. Si può parlare di causalità $X\to Y$ solo se valgono contemporaneamente tre criteri: associazione, ordine logico o temporale, esclusione di spiegazioni alternative. L'associazione è un criterio statistico e simmetrico: la correlazione fra $X$ e $Y$ è la stessa di quella fra $Y$ e $X$, quindi non dice quale variabile preceda l'altra. Se il verso del legame non è chiaro si parla di causalità inversa.

> [!example] Svolgimento
> **Impostazione.** Le prime tre domande sono percentuali di riga; le ultime tre applicano i tre criteri.
>
> **(a)** $100\times\dfrac{ {{e01_01.k_si|m}} }{ {{e01_01.n_si|m}} }={{e01_01.p_si|m}}\%$.
>
> **(b)** $100\times\dfrac{ {{e01_01.k_no|m}} }{ {{e01_01.n_no|m}} }={{e01_01.p_no|m}}\%$.
>
> **(c)** ${{e01_01.p_si|m}}-{{e01_01.p_no|m}}={{e01_01.diff|m}}$ punti percentuali: fra gli iscritti le assenze sono meno frequenti.
>
> **(d)** Sì. Le due percentuali sono diverse e la differenza, ${{e01_01.diff|m}}$ punti, è ampia: il criterio (1) è soddisfatto.
>
> **(e)** No. L'informazione è raccolta in un solo momento e non si sa quando i dipendenti si siano iscritti, quindi non si può stabilire che l'iscrizione preceda le assenze. Anzi, anche il verso opposto ha senso logico: chi sta spesso male difficilmente si iscrive in palestra (causalità inversa). Il criterio (2) non è soddisfatto.
>
> **(f)** No. Dei tre criteri è soddisfatto soltanto il primo: l'ordine non è chiaro e non sono escluse spiegazioni alternative, per esempio l'età o la mansione, che possono influire sia sull'iscrizione sia sulle assenze.

> [!warning] Errore tipico
> Confrontare i conteggi, ${{e01_01.k_si|m}}$ assenti fra gli iscritti contro ${{e01_01.k_no|m}}$ fra i non iscritti, invece delle percentuali: i due gruppi hanno numerosità diverse (${{e01_01.n_si|m}}$ e ${{e01_01.n_no|m}}$) e il confronto dei conteggi esagera la differenza. L'errore più grave è concludere dall'associazione che la palestra riduca le assenze.

> [!success] Risposta
> **(a)** Fra gli iscritti ha fatto almeno un'assenza il ${{e01_01.p_si|m}}\%$. **(b)** Fra i non iscritti il ${{e01_01.p_no|m}}\%$. **(c)** La differenza è di ${{e01_01.diff|m}}$ punti percentuali. **(d)** Sì: c'è associazione. **(e)** No: i dati non dicono se l'iscrizione venga prima delle assenze, e potrebbe valere il verso opposto. **(f)** No: l'associazione è solo il primo dei tre criteri di causalità.

![Percentuale di dipendenti con almeno un'assenza, per iscritti e non iscritti: la differenza fra le barre è l'associazione, il primo criterio. Il grafico non dice nulla sull'ordine fra iscrizione e assenze.]({{e01_01.fig.percentuali}}){width=85%}

{{testo:e01_02}}

> [!tip] Richiamo
> Si guardano due cose: quanti soggetti e quanti periodi compaiono, e se gli stessi soggetti ricompaiono in periodi diversi. *Cross section*: molti soggetti in un solo periodo. *Serie storica*: un solo soggetto in molti periodi, e il tempo ne definisce l'ordine. *Panel*: gli stessi soggetti osservati in più periodi, con una doppia dimensione, soggetto e tempo; se i soggetti sono $N$ e i periodi $T$, senza dati mancanti le osservazioni sono $N\times T$. Se in ogni periodo si osservano soggetti diversi non è un panel, ma una sequenza di cross section.

> [!example] Svolgimento
> **Impostazione.** Per ogni dataset si contano soggetti e periodi e si controlla se i soggetti si ripetono.
>
> **(a)** Le imprese del dataset A compaiono tutte nello stesso anno: è una {{e01_02.tipo_a}}, non una serie storica. No.
>
> **(b)** Il dataset B ha un solo soggetto, il titolo, osservato in mesi successivi: è una {{e01_02.tipo_b}}. Sì.
>
> **(c)** Le stesse imprese ricompaiono in tutti gli anni: il dataset C è un {{e01_02.tipo_c}}. Sì.
>
> **(d)** Nel 1978 e nel 1981 i codici delle case sono diversi: nessuna casa è osservata due volte, quindi il dataset D è una {{e01_02.tipo_d}} e non un panel. No.
>
> **(e)** Con $N={{e01_02.N|m}}$ imprese e $T={{e01_02.T|m}}$ anni, senza dati mancanti, le righe sono $N\times T={{e01_02.N|m}}\times{{e01_02.T|m}}={{e01_02.oss|m}}$.
>
> **(f)** Con una sola impresa il soggetto è uno e il tempo definisce l'ordine delle osservazioni: i dati sono una {{e01_02.tipo_f}}, non un panel. No.

> [!warning] Errore tipico
> Chiamare panel il dataset D perché copre due anni. Un panel richiede di osservare gli stessi soggetti in più periodi, come fa il dataset C con le imprese; qui in ciascun anno c'è un campione diverso di case. Un altro errore è sommare invece di moltiplicare: le osservazioni di un panel sono $N\times T$, non $N+T$.

> [!success] Risposta
> **(a)** No: A è una {{e01_02.tipo_a}}. **(b)** Sì: B è una {{e01_02.tipo_b}}. **(c)** Sì: C è un {{e01_02.tipo_c}}. **(d)** No: D è una {{e01_02.tipo_d}}, perché le case del 1978 e del 1981 sono diverse. **(e)** Il dataset C completo ha ${{e01_02.oss|m}}$ osservazioni. **(f)** No: con una sola impresa è una {{e01_02.tipo_f}}.

![Ogni dataset come griglia di soggetti (righe) per periodi (colonne): un quadrato è una coppia osservata. Una colonna sola è una cross section, una riga sola una serie storica, una griglia in cui gli stessi soggetti ricompaiono è un panel; in D nessun soggetto si ripete.]({{e01_02.fig.griglie}}){width=85%}

{{testo:e01_03}}

> [!tip] Richiamo
> In una regressione semplice $y=\beta_0+\beta_1 x+\epsilon$ una variazione $\Delta x$ comporta $\Delta y=\beta_1\,\Delta x$. Il rapporto $t=\hat\beta_1/\widehat{\text{se}}(\hat\beta_1)$ e l'$R^2$ dipendono dai dati solo attraverso la correlazione campionaria $r$ fra $x$ e $y$, $t=r\sqrt{n-2}/\sqrt{1-r^2}$ e $R^2=r^2$, che è simmetrica: scambiando i ruoli di $x$ e di $y$ restano uguali $t$ e $R^2$, mentre le pendenze cambiano e il loro prodotto è $R^2$. Una correlazione non dice quale variabile sia la causa. Se non è chiaro se $x$ influenzi $y$ o il contrario si ha causalità inversa: si crea un riferimento circolare e il regressore risulta correlato con l'errore, per cui la stima del coefficiente è problematica.

> [!example] Svolgimento
> **Impostazione.** Le due regressioni usano gli stessi dati con gli assi scambiati; si confrontano le loro statistiche e si ragiona sul verso del legame.
>
> **(a)** Il rapporto $t$ di $\hat\beta_1$ è ${{e01_03.tA|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_1=0$.
>
> **(b)** $\Delta\text{reati}=\hat\beta_1\times\Delta\text{poliziotti}={{e01_03.bA|m}}\times{{e01_03.dpol|m}}={{e01_03.effA|m}}$ reati ogni mille abitanti: letta in senso causale, la stima direbbe che più poliziotti portano più reati.
>
> **(c)** Il rapporto $t$ di $\hat\gamma_1$ è ${{e01_03.tB|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\gamma_1=0$.
>
> **(d)** Sì. I due rapporti $t$ coincidono (${{e01_03.tA|m}}$ e ${{e01_03.tB|m}}$) e coincide l'$R^2$, ${{e01_03.r2|m}}$. Le pendenze invece sono diverse, ${{e01_03.bA|m}}$ e ${{e01_03.bB|m}}$, e il loro prodotto è ${{e01_03.bA|m}}\times{{e01_03.bB|m}}={{e01_03.prod|m}}=R^2$.
>
> **(e)** No. L'associazione è la stessa in entrambe le direzioni ed è significativa in entrambe: non dice se siano i poliziotti a influire sui reati o i reati ad attirare i poliziotti. La seconda lettura è plausibile (le città con più reati assumono più poliziotti): può trattarsi di causalità inversa (o di variabili omesse), l'ordine logico non è chiaro e quindi non si può parlare di causalità.

> [!warning] Errore tipico
> Credere che la seconda pendenza sia l'inverso della prima: $1/\hat\beta_1={{e01_03.inv|m}}$, mentre $\hat\gamma_1={{e01_03.bB|m}}$, perché il loro prodotto è $R^2$ e non $1$. L'errore più grave è concludere dalla (a) che aumentare i poliziotti faccia aumentare i reati: il segno e la significatività della stima possono essere prodotti dalla causalità inversa (o da variabili omesse); l'ordine logico non è chiaro, quindi non si può parlare di causalità.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: la pendenza è significativa. **(b)** Letta in senso causale, la stima darebbe ${{e01_03.effA|m}}$ reati in più ogni mille abitanti. **(c)** Si rifiuta $H_0$ anche nella regressione scambiata. **(d)** Sì: stesso $t$ (${{e01_03.tA|m}}$) e stesso $R^2$ (${{e01_03.r2|m}}$). **(e)** No: l'associazione è simmetrica e non indica il verso del legame; la stima può essere prodotta dalla causalità inversa (o da variabili omesse), l'ordine logico non è chiaro e quindi non si può parlare di causalità.

![La stessa nuvola di città con gli assi scambiati: a sinistra reati su poliziotti, a destra poliziotti su reati. In entrambi i casi la retta è significativa, con lo stesso $t$ e lo stesso $R^2$: i dati non indicano il verso del legame.]({{e01_03.fig.nuvola}}){width=85%}

{{testo:e01_04}}

> [!tip] Richiamo
> Un errore di misura nel regressore rende distorta (attenuata) la stima dei parametri, anche se il modello è corretto e anche se l'errore è in media nullo: la media del campione può restare corretta, ma l'errore aggiunge rumore alla variabile osservata e la stima del coefficiente si sposta. La distorsione non è una fluttuazione campionaria e non scompare aumentando il numero di osservazioni: un campione più grande rende solo più precisa, cioè con errore standard più piccolo, una stima sbagliata. Per verificare se un valore $\beta_0$ è compatibile con i dati si usa $t=(\hat\beta_1-\beta_0)/\widehat{\text{se}}(\hat\beta_1)$ e si rifiuta se $|t|>1{,}96$.

> [!example] Svolgimento
> **Impostazione.** Si confrontano le medie, che non risentono dell'errore, con le pendenze, che ne risentono, e poi si guarda che cosa cambia con un campione più grande.
>
> **(a)** $100\times\dfrac{ {{e01_04.mr|m}}-{{e01_04.mv|m}} }{ {{e01_04.mv|m}} }={{e01_04.dm|m}}\%$: le due medie sono quasi uguali.
>
> **(b)** $\dfrac{\hat\beta_R}{\hat\beta_V}=\dfrac{ {{e01_04.b_rip|m}} }{ {{e01_04.b_vera|m}} }={{e01_04.r_pic|m}}$: con la spesa riportata la pendenza stimata è molto più piccola di quella che si ottiene con la spesa vera.
>
> **(c)** $\dfrac{\hat\beta_G}{\beta}=\dfrac{ {{e01_04.b_gr|m}} }{ {{e01_04.beta|m}} }={{e01_04.r_gr|m}}$: con un campione molto più grande il rapporto è praticamente lo stesso.
>
> **(d)** $t=\dfrac{ {{e01_04.b_gr|m}}-{{e01_04.beta|m}} }{ {{e01_04.s_gr|m}} }={{e01_04.t_g|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_1=\beta$.
>
> **(e)** No. Con il campione grande l'errore standard è più piccolo ma la stima resta lontana da $\beta$, e il valore vero è escluso con grande sicurezza: la distorsione non dipende dalla numerosità.

> [!warning] Errore tipico
> Concludere dalla (a) che i dati riportati siano affidabili perché le medie coincidono. L'errore di ricordo non sposta la media, ma rende la spesa riportata più dispersa (la deviazione standard sale da ${{e01_04.sd_v|m}}$ a ${{e01_04.sd_r|m}}$) e questo basta a distorcere la pendenza. Un altro errore è pensare che un campione più grande risolva il problema.

> [!success] Risposta
> **(a)** La media della spesa riportata differisce da quella vera del ${{e01_04.dm|m}}\%$. **(b)** Il rapporto fra le pendenze del Modello R e del Modello V è ${{e01_04.r_pic|m}}$. **(c)** Il rapporto fra la pendenza del Modello G e $\beta$ è ${{e01_04.r_gr|m}}$. **(d)** Si rifiuta $H_0$: $\beta$ non è compatibile con la stima del campione grande. **(e)** No: un campione più grande rende più precisa la stima, ma non elimina la distorsione.

![A sinistra la spesa mensile contro la spesa vera e contro quella riportata, con le due rette: l'errore di misura rende più piatta la retta. A destra la pendenza stimata nei tre modelli con intervallo al 95\%: nel campione grande l'intervallo è stretto e non contiene il valore usato per generare i dati.]({{e01_04.fig.errore}}){width=85%}

{{testo:e01_05}}

> [!tip] Richiamo
> Una relazione fra $X$ e $Y$ si dice spuria quando è indotta da una variabile $Z$ che influisce su entrambe. Se $Z$ è omessa dal modello, la stima del coefficiente di $X$ coglie anche l'effetto di $Z$: è la prima delle tre cause di problemi nella stima, le variabili omesse. Se, controllando per $Z$, l'associazione fra $X$ e $Y$ si riduce a zero, è il sintomo di una relazione spuria. Una variazione $\Delta x$ comporta $\Delta y=\beta\,\Delta x$. Per verificare un valore $\beta_0$ si usa $t=(\hat\beta-\beta_0)/\widehat{\text{se}}(\hat\beta)$ e si rifiuta se $|t|>1{,}96$. Non si può dimostrare che una relazione sia causale: si possono confutare le spiegazioni alternative, e un test che non rifiuta $H_0$ non dimostra che $H_0$ sia vera.

> [!example] Svolgimento
> **Impostazione.** Si confrontano i due modelli, si controlla che la temperatura sia legata sia agli incidenti sia ai gelati e si verifica che il Modello 2 escluda l'effetto letto nel Modello 1.
>
> **(a)** Nel Modello 1 $t={{e01_05.t1|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_1=0$.
>
> **(b)** $\Delta\text{incidenti}=\hat\beta_1\times\Delta\text{gelati}={{e01_05.b1|m}}\times{{e01_05.dg|m}}={{e01_05.eff1|m}}$ incidenti ogni 100 mila bagnanti, se si leggesse il Modello 1 in senso causale.
>
> **(c)** Nel Modello 2 $t={{e01_05.t2|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0:\beta_1=0$.
>
> **(d)** $\Delta\text{incidenti}=\hat\beta_2\times\Delta\text{temperatura}={{e01_05.bT|m}}\times{{e01_05.dt|m}}={{e01_05.effT|m}}$ incidenti ogni 100 mila bagnanti, a parità di gelati.
>
> **(e)** Nella regressione ausiliaria $\hat\delta_1={{e01_05.dT|m}}$ con $t={{e01_05.tT|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\delta_1=0$. Più la temperatura è alta, più gelati si vendono.
>
> **(f)** Con $b={{e01_05.b1|m}}$ si ha $t=\dfrac{ {{e01_05.b2|m}}-{{e01_05.b1|m}} }{ {{e01_05.s2|m}} }={{e01_05.t_naive|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta_1=b$. Il Modello 2 esclude che l'effetto dei gelati sia quello letto nel Modello 1.
>
> **Lettura.** La temperatura influisce sugli incidenti (c'è più gente in acqua) e sui gelati: è una causa comune. Il Modello 1 la omette e l'associazione fra gelati e incidenti è spuria, indotta dalla variabile omessa.

> [!warning] Errore tipico
> Leggere la stima del Modello 1, ${{e01_05.b1|m}}$, come l'effetto causale dei gelati: coglie anche l'effetto della temperatura. Un secondo errore è concludere dalla (c) che l'effetto dei gelati sia dimostrato nullo: il test non rifiuta $H_0:\beta_1=0$, ma non lo dimostra. Ciò che i dati escludono, al 5\%, è il valore del Modello 1 (punto (f)): la confutazione di una spiegazione, non la dimostrazione dell'altra.

> [!success] Risposta
> **(a)** Si rifiuta $H_0$: nel Modello 1 i gelati sembrano significativi. **(b)** Letta in senso causale, la stima darebbe ${{e01_05.eff1|m}}$ incidenti in più ogni 100 mila bagnanti. **(c)** Non si rifiuta $H_0$: controllando per la temperatura i gelati non sono più significativi. **(d)** Con ${{e01_05.dt|m}}$ gradi in più gli incidenti aumentano in media di ${{e01_05.effT|m}}$, a parità di gelati. **(e)** Si rifiuta $H_0$: la temperatura influisce sui gelati. **(f)** Si rifiuta $H_0$: il Modello 2 esclude l'effetto del Modello 1. L'associazione del Modello 1 è spuria, indotta dalla temperatura omessa.

![A sinistra incidenti contro gelati con la retta del Modello 1, di pendenza ${{e01_05.b1|m}}$. A destra gli incidenti al netto dell'effetto stimato della temperatura, $\text{incidenti}-\hat\beta_2\,\text{temperatura}$, con la retta del Modello 2, di pendenza ${{e01_05.b2|m}}$: l'associazione sparisce.]({{e01_05.fig.controllo}}){width=85%}

{{testo:e01_06}}

> [!tip] Richiamo
> Per gli extra-rendimenti il CAPM prevede $E[R_t]=\beta\,E[R_{mt}]$, cioè $\alpha=0$ nella regressione $R_t=\alpha+\beta R_{mt}+\epsilon_t$, con $\beta=\text{Cov}(R_t,R_{mt})/\text{Var}(R_{mt})$ e $\text{Var}(R_t)=\beta^2\,\text{Var}(R_{mt})+\sigma^2$. Il modello si valida stimando la regressione con l'intercetta e verificando $H_0:\alpha=0$ con $t=\hat\alpha/\widehat{\text{se}}(\hat\alpha)$: se si rifiuta, il CAPM è confutato; se non si rifiuta, è compatibile con i dati ma non dimostrato. Con $\beta>1$ il fondo amplifica i movimenti del mercato ed è più rischioso. Per verificare $\beta=1$ si usa $t=(\hat\beta-1)/\widehat{\text{se}}(\hat\beta)$. Una variazione $\Delta R_m$ comporta $\Delta R=\beta\,\Delta R_m$. Il rischio idiosincratico si stima con $\hat\sigma=\sqrt{\text{SSR}/(n-2)}$. Una serie storica osserva un solo soggetto in istanti successivi.

> [!example] Svolgimento
> **Impostazione.** Un solo fondo è osservato mese dopo mese; si testano due ipotesi diverse, $\alpha=0$ e $\beta=1$, e si ricava il rischio dalla SSR.
>
> **(a)** Un solo soggetto, il fondo, osservato in mesi successivi: sì, è una serie storica.
>
> **(b)** $t=\hat\alpha/\widehat{\text{se}}(\hat\alpha)={{e01_06.ta|m}}$, in valore assoluto minore di $1{,}96$: non si rifiuta $H_0:\alpha=0$.
>
> **(c)** No. Non rifiutare $H_0:\alpha=0$ vuol dire che i dati non confutano l'intercetta nulla; il CAPM resta compatibile con i dati, ma non è dimostrato.
>
> **(d)** $t=\dfrac{ {{e01_06.b|m}}-1 }{ {{e01_06.sb|m}} }={{e01_06.tb|m}}$, in valore assoluto maggiore di $1{,}96$: si rifiuta $H_0:\beta=1$. L'intervallo di confidenza al 95\% $[{{e01_06.ic_lo|m}};\,{{e01_06.ic_hi|m}}]$ non contiene $1$ e sta sopra: $\beta>1$, il fondo è più rischioso del mercato.
>
> **(e)** $\Delta R=\hat\beta\times\Delta R_m={{e01_06.b|m}}\times{{e01_06.dm|m}}={{e01_06.eff|m}}$ punti percentuali.
>
> **(f)** $\hat\sigma=\sqrt{\dfrac{\text{SSR}}{n-2}}=\sqrt{\dfrac{ {{e01_06.ssr|m}} }{ {{e01_06.n|m}}-2 }}={{e01_06.sigma|m}}$ punti percentuali.

> [!warning] Errore tipico
> Verificare $H_0:\beta=0$ per giudicare se il fondo è più rischioso del mercato: quel test dà $t={{e01_06.t0|m}}$: per un fondo azionario come questo il test su $\beta=0$ rifiuta quasi sempre, ma non dice nulla sul confronto con $1$. Un altro errore è leggere il mancato rifiuto di $H_0:\alpha=0$ come la prova che il CAPM sia vero, invece di una mancata confutazione.

> [!success] Risposta
> **(a)** Sì: un fondo osservato nel tempo è una serie storica. **(b)** Non si rifiuta $H_0:\alpha=0$. **(c)** No: il CAPM non è confutato, ma non è dimostrato. **(d)** Si rifiuta $H_0:\beta=1$: $\hat\beta={{e01_06.b|m}}$ è significativamente maggiore di $1$ e il fondo è più rischioso del mercato. **(e)** Con il mercato $+{{e01_06.dm|m}}$ punti il fondo varia in media di ${{e01_06.eff|m}}$ punti. **(f)** Il rischio idiosincratico stimato è $\hat\sigma={{e01_06.sigma|m}}$.

![Extra-rendimenti mensili del fondo contro quelli del mercato, con la retta stimata e la retta di pendenza 1: la retta stimata è più ripida, il fondo amplifica i movimenti del mercato; l'intercetta stimata, ${{e01_06.a|m}}$, è vicina a zero.]({{e01_06.fig.capm}}){width=85%}
