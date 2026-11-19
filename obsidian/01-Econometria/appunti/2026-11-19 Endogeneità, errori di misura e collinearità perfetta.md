---
corso: Econometria
data: 2026-11-19
fonte: Materiali/audio/econometria/econometria_2026-11-19.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-19
---

# Endogeneità, errori di misura e collinearità perfetta

## Casi di endogeneità e struttura logica della regressione multipla

La lezione approfondisce alcune casistiche specifiche in cui si presenta l'endogeneità, già anticipata nella lezione precedente. Conoscerle serve perché un modello in presenza di endogeneità può fornire stime non adeguate. L'endogeneità non è verificabile direttamente, quindi riconoscerla è un compito complicato. Se però si conoscono le sue possibili cause, si può lavorare a priori, dal punto di vista logico, su quelle cause e poi cercare di capire se il problema è effettivamente presente.

Si riprende il problema della regressione multipla in cui interagiscono tre fattori: l'esempio dei bambini californiani, con la loro performance scolastica, la dimensione della classe e l'effetto del reddito. La domanda è se una struttura logica di questo tipo si possa affrontare con un modello di regressione.

### Il confronto tra distretti ricchi e poveri

Per capire se la variazione del punteggio dipende dal reddito o dalla dimensione della classe, si era impostato un esperimento. La popolazione dei distretti scolastici viene divisa in due parti: i distretti ricchi e i distretti poveri. Si vuole capire se la relazione tra performance e dimensione della classe dipende dal reddito, cioè se è il reddito a guidare le stime.

Si usano i dati dei distretti ad alto reddito, che sono omogenei tra loro, e si stima la regressione

$$\text{punteggio}_i = \alpha_A + \beta_A \, \text{size}_i + \varepsilon_i,$$

dove $\beta_A$ è il coefficiente dei distretti ad alto reddito. Lo stesso esercizio si fa per i distretti a basso reddito:

$$\text{punteggio}_i = \alpha_B + \beta_B \, \text{size}_i + \varepsilon_i.$$

I termini d'errore sono diversi perché riguardano sottopopolazioni diverse. All'interno di ciascun sottogruppo le stime non dipendono dal reddito, perché il reddito è omogeneo. Per analogia: se tutti fossero alti due metri, la probabilità di schiacciare a basket non dipenderebbe dall'altezza, ma da altre caratteristiche, per esempio l'elasticità muscolare. Si elimina così l'effetto della variabile confondente, che qui è il reddito: essendo uguale per tutti, una variazione del punteggio non può dipenderne e deve dipendere da altro. Per semplificare la trattazione si suppone inoltre che in queste regressioni $\varepsilon$ non abbia un effetto sistematico, cioè che non vi siano altre variabili rilevanti.

Se la stima di $\beta$ nei due sottocampioni non è influenzata dal reddito, il reddito non ha impatto sulla stima della correlazione tra le variabili chiave. Se invece la stima cambia, il reddito ha importanza. Interessa stimare $\beta$ perché è una misura di correlazione: è dato dalla covarianza divisa per la varianza, quindi esprime la relazione tra $X$ e $Y$. L'idea mostrata nella prima lezione è questa, scritta ora nella forma di un modello di regressione.

### Da due sottocampioni a un unico modello

Dividere il campione in due parti e stimare i due sottocampioni si può scrivere in modo più generale con un unico modello. La divisione in due pezzi si può cioè fare in una sola operazione, e lo strumento è il modello di regressione multipla, presentato nell'ultima parte della lezione di due giorni prima.

> [!tip] Esame
> Il docente chiede se ci sono dubbi sui test trattati nella lezione precedente, che gli studenti hanno visto anche nelle esercitazioni. Non vengono poste domande. La statistica di base verrà molto usata nel compito: senza una conoscenza almeno pratica di quegli argomenti tutto diventa più difficile, perché si accumulano le difficoltà di statistica e quelle di econometria. Chi ha dubbi può chiarirli subito, oppure andare a ricevimento, scrivere un'email o collegarsi su Zoom.

Questa struttura logica potrebbe essere candidata a una relazione causale, potenzialmente migliore di quella con sole due variabili. Si può scrivere come modello di regressione, ma non con il modello di regressione semplice: bisogna aggiungere variabili nella definizione della media condizionale. Il valore atteso condizionale di $Y$ dato $X$ dipende allora da più di un fattore: $X_1$ è la dimensione della classe e $X_2$ è il fattore confondente, il reddito.

### Variabili di interesse e variabili di controllo

Studiando un modello di regressione ha senso considerare più variabili insieme, perché il mondo è complesso e considerare le variabili a coppie è troppo poco. Tuttavia, in un problema economico, biologico o di altro genere affrontabile con un modello matematico o statistico, interessa di solito la relazione tra due variabili specifiche, non tra tutte. Le variabili che definiscono il valore atteso condizionale si dividono quindi in due sottogruppi: le variabili di interesse, o di policy, e le variabili di controllo.

Un responsabile della didattica in California è interessato alla dimensione della classe, non al reddito, che non rientra nei suoi scopi. Se però il reddito non è nel modello, la previsione dell'impatto di una riduzione della classe sulla performance dei bambini può essere sbagliata. L'interesse è dunque solo sul parametro del primo fattore, $\beta_1$. Per stimarlo bene occorre considerare anche altre variabili, ma il valore di $\beta_2$ non interessa: la variabile 2, il reddito, serve soltanto a stimare bene $\beta_1$, mentre l'effetto del reddito sulla performance è un altro problema. Le variabili di interesse sono quelle di cui si vuole l'effetto marginale in modo preciso. Le altre servono a ripulire il termine d'errore dagli effetti collaterali, e lo si fa aggiungendo il loro termine alla media condizionale.

### Specificazione del modello

A parte il maggior numero di variabili, il modello di regressione multipla è definito esattamente come quello di regressione semplice. Esso lega le osservazioni $y_i$, $x_{1i}$ e $x_{2i}$ dell'unità statistica $i$-esima, per esempio il distretto 57 (Orange County, il docente dice di non sapere quale sia), tramite il termine d'errore $\varepsilon_i$. Anche qui l'errore rappresenta tutte le caratteristiche del distretto che non sono né la variabile 1 né la variabile 2, come la percentuale di non madrelingua o la qualità delle scuole: tutto ciò che non è reddito né dimensione della classe. Nel modello di regressione semplice $y$ conteneva anche il fattore reddito, perché non figurava nella media condizionale e doveva stare da qualche altra parte, cioè nell'errore. L'errore va pensato come il bidone della spazzatura in cui finisce tutto ciò che non compare nella parte sistematica.

### Interpretazione di $\beta_1$ e $\beta_2$

Nel modello di regressione semplice il parametro $\beta$ rappresenta la correlazione tra $x$ e $y$. Ci si chiede se nel modello multiplo sia ancora così. Non lo è del tutto: $\beta_1$ e $\beta_2$ sono ancora correlazioni, ma non correlazioni marginali tra due variabili.

I parametri $\beta_1$ e $\beta_2$ misurano una **correlazione condizionale**, cioè la dipendenza tra due variabili al netto di una terza. Il motivo emerge dalla previsione della performance al test di un distretto con caratteristiche $x_1$ e $x_2$, dove la barra indica un valore qualsiasi tra quelli che possono assumere la dimensione della classe e il reddito. L'aspettativa condizionale si scrive come nel modello semplice, in forma solo leggermente più formalizzata:

$$E(Y \mid X_1 = \bar{x}_1, X_2 = \bar{x}_2) = \alpha + \beta_1 \bar{x}_1 + \beta_2 \bar{x}_2 + E(\varepsilon \mid X_1 = \bar{x}_1, X_2 = \bar{x}_2).$$

> [!question] Da verificare: la trascrizione riporta "performance a tela"; probabilmente "performance al test" (punteggio al test).

### Variazione della dimensione della classe a reddito fissato

Si mantiene fisso il livello di reddito e si osserva che cosa accade, per un distretto con quel reddito, se si implementa la policy. Si prendono due distretti identici dal punto di vista del reddito e si modifica leggermente la dimensione della classe in uno solo di essi, stanziando risorse solo per quel distretto. In questo modo il confronto è omogeneo e il reddito non è più un fattore discriminante: un distretto ricco è confrontato con un altro distretto ricco. Non si vuole invece confrontare un distretto ricco con uno povero applicando la policy a uno solo dei due.

Il valore atteso condizionale contiene un effetto dovuto al numero di bambini in classe, un effetto reddito che è lo stesso nei due scenari perché i distretti sono uguali per reddito, e un effetto medio del termine d'errore, che in linea di principio potrebbe dipendere da $X_1$ e da $X_2$. L'impatto di una modifica della dimensione della classe si ottiene come differenza tra il valore atteso nello scenario con la nuova dimensione e quello nello scenario di partenza. Per semplicità la differenza di valori attesi è indicata con $\Delta Y$, che è una definizione ($\equiv$) e serve solo a usare un simbolo più semplice:

$$\Delta Y \equiv E(Y \mid X_1 = \bar{x}_1 + \Delta x_1, X_2 = \bar{x}_2) - E(Y \mid X_1 = \bar{x}_1, X_2 = \bar{x}_2) = \beta_1 \Delta x_1 + \text{(differenza dell'effetto medio di } \varepsilon\text{ nei due scenari)}.$$

La variazione in media di $Y$ dipende dalla variazione di $X_1$, che è una scelta, e non da $X_2$, perché questa è costante. Dipende inoltre, eventualmente, dagli effetti collaterali, cioè dall'impatto di tutti gli altri fattori contenuti nel termine d'errore, che non sono né il reddito né la dimensione della classe, nei due scenari.

Se $X_1$ e $X_2$ sono incorrelate con $\varepsilon$, la parte che dipende dal valore atteso condizionale dell'errore è nulla, perché a una variazione di $X$ non corrisponde in media una variazione di $\varepsilon$. Questa condizione consente anche di dimostrare l'incorrelazione tra le $X$ e $\varepsilon$. In tal caso la variazione di $Y$ dipende soltanto dal termine $\beta_1 \Delta x_1$. Si tratta di una variazione attesa, non di una variazione numerica. Rispetto alla lezione della settimana precedente la presentazione è più formalizzata, ma il contenuto è lo stesso. Ipotizzare che in media $\varepsilon$ non conti niente si dice, in econometria, ipotizzare l'**esogeneità**: i fattori non inclusi nel modello non hanno un impatto sistematico sulle relazioni tra le variabili.

### Beta uno come correlazione parziale

Due punti sono da ricordare. Il primo riguarda il significato di $\beta_1$: indica quanto una variazione di $X_1$ incide in media su $Y$, quindi è una misura di associazione. Non è però la stessa correlazione stimata nel modello di regressione semplice, perché in questo caso si controlla per il reddito, che nel ragionamento precedente è assunto costante. $\beta_1$ è la correlazione tra $y$ e $x_1$ al netto di $x_2$: l'effetto di $x_2$ viene eliminato. Rappresenta cioè una correlazione condizionale, quella tra $y$ e $x_1$ una volta fissato $x_2$, ed è un concetto diverso e più preciso. Si chiama anche **correlazione parziale**.

È un'informazione utile perché dice di quanto aumenta la performance rispetto a una riduzione della dimensione della classe in distretti omogenei, cioè con lo stesso reddito. Questi distretti possono essere eterogenei per le altre caratteristiche, ma se si ipotizza che la media di $\varepsilon$, fissate le $x$, sia uguale a zero, esse non hanno un effetto sistematico e dal punto di vista pragmatico si possono trascurare.

Il secondo punto è che questo schema replica il ragionamento fatto in precedenza in forma grafica. Allora si fissava il reddito in modo più grezzo, prendendo i distretti sopra la mediana e quelli sotto la mediana e calcolando la correlazione in ciascun gruppo. Nel modello di regressione la correlazione parziale viene calcolata per qualsiasi livello di $x_2$, il reddito. Dal punto di vista intuitivo si fa esattamente la stessa cosa: il modello di regressione multipla riproduce lo schema intuitivo, che è l'intuizione, mentre il modello ne è la formalizzazione statistica.

Si ha quindi: $\beta_1$ non è più una correlazione semplice ma una correlazione parziale, e il modello permette di isolare gli effetti controllando per i fattori di controllo, cioè i fattori confondenti. Lo scopo dell'analisi resta però $\beta_1$. Ciò che accade a $\beta_2$ non è rilevante per chi si occupa della didattica in California: è un problema di chi si occupa, eventualmente, di servizi sociali.

Il modello di regressione multipla consente di controllare per i fattori purché siano inclusi esplicitamente nel modello. Non devono restare in $\varepsilon$, che non è osservabile: non se ne conosce la struttura né come reagisce, ed è questo il problema.

Il parametro $\beta_1$ viene chiamato **effetto marginale**: l'effetto di una variabile su $y$ al netto di tutte le altre. È soltanto un nome, ma il docente lo userà da qui in avanti. Qui $\beta_1$ è l'effetto della dimensione della classe una volta fissato il reddito, cioè eliminato l'effetto di $x_2$.

### Confronto numerico: regressione semplice e regressione multipla

Dal punto di vista operativo, si riprende il confronto della prima lezione. Nel modello di regressione che non controlla per il reddito, cioè con la sola correlazione tra punteggio e dimensione della classe, il coefficiente $\beta$ è circa $-2{,}27$. Il p-value è zero, quindi il coefficiente è statisticamente significativo, cioè diverso da zero. La correlazione non è irrilevante e, poiché ha anche senso dal punto di vista logico, potrebbe essere candidata a una relazione causa-effetto.

Si utilizza ora lo schema a tre variabili, legato al modello di regressione multipla. Il docente spiegherà in seguito come si stimano i parametri; per ora si suppone di riuscire a stimarli. La regressione, già vista la volta precedente, ha tre parametri. La prima riga riguarda la dimensione della classe (student-teacher ratio), la seconda l'average income, cioè il reddito medio.

> [!question] Da verificare: nella spiegazione compare "R-squared" accanto alla prima riga della tabella; la frase è fuori contesto e non permette di stabilire a che cosa si riferisca.

Il coefficiente di interesse, quello della dimensione della classe, non è più $-2{,}2$ ma $-0{,}64$, cioè meno di un terzo. È debolmente significativo: il p-value del test di significatività è 6,8%, quindi al livello del 5% non si rifiuta l'ipotesi nulla e non si può escludere che il parametro sia uguale a zero. Anche l'intervallo di confidenza lo conferma: il limite inferiore è negativo e il superiore positivo, quindi lo zero è un valore possibile e un candidato a essere il vero valore del parametro. L'effetto del reddito è 1,8, statisticamente significativo, con un intervallo di confidenza che assume valori solo positivi.

Il segno atteso del coefficiente del reddito è positivo. Giusto per inciso, conviene sommare in valore assoluto i due coefficienti $\beta_1$ e $\beta_2$. Il valore assoluto serve perché reddito e dimensione della classe hanno effetti di segno opposto sulla performance: per migliorarla bisogna ridurre di un'unità la dimensione della classe, oppure aumentare di un'unità il reddito. La somma in valore assoluto dà l'impatto totale al netto del segno delle due variabili. Qui $0{,}64 + 1{,}83$ è più o meno il $2{,}2$ stimato in precedenza, al netto del segno. Il docente non sa se sia un caso o se sia dimostrabile qualcosa di più profondo.

> [!question] Da verificare: la somma $0{,}64 + 1{,}83$ è $2{,}47$, non $2{,}2$ (o $2{,}27$, il valore del coefficiente della regressione semplice). Il docente dice "più o meno".

Ne risulta che il modello di regressione semplice non stima l'effetto della classe: stima la combinazione dell'effetto della classe e dell'effetto del reddito. Chi usa quel modello non lo sa, perché il reddito non è nel modello. Vedendo il coefficiente $-2{,}2$ gli si assegna mentalmente tutto il peso a una riduzione di un'unità della dimensione della classe, senza pensare al reddito. Aggiungere un regressore permette di scomporre gli effetti in modo esplicito.

### Quando il modello più complesso sostituisce quello semplice

Una relazione logica che aumenta la complessità del modello esclude di fatto quella più semplice, per tre ragioni. Lo schema a tre variabili ha senso dal punto di vista logico. Si può scrivere come modello di regressione. Il modello di regressione permette di valutare la relazione empiricamente sui dati. È quindi un modello sensato, stimabile e migliore del precedente dal punto di vista statistico e logico.

Se il coefficiente del reddito fosse risultato non significativo, l'effetto reddito sarebbe irrilevante e si sarebbe potuti restare nel modello più semplice. Qui interviene il rasoio di Occam: tra due spiegazioni, una complicata e una semplice, entrambe valide e senza controindicazioni interne, si preferisce la semplice. Il docente precisa che si tratta di un'idea filosofica su cui non si pronuncia. In questo caso però il modello più complicato cambia completamente le conclusioni rispetto a quello semplice. I due modelli non sono equivalenti e si è obbligati a usare il più complicato, perché porta a rifiutare il modello precedente. Ciò che si stima ora è più preciso.

Questo non significa che la relazione sia causale. Per arrivarci bisognerebbe continuare l'analisi, togliendo altri fattori dal termine d'errore e inserendoli nella media condizionale. Si ha comunque un'idea di come funziona il modello di regressione multipla: consiste nell'aggiungere fattori nella definizione della media condizionale. In generale si continuano ad aggiungere informazioni sensate dal punto di vista logico, e il modello deve restare coerente con un'idea teorica, economica, sociologica o pedagogica, a seconda dell'oggetto di studio.

Poiché interessa il parametro della dimensione della classe, su cui si investono i soldi, un'idea di lavoro è continuare a inserire variabili finché il parametro di interesse $\beta_1$ si stabilizza. Quando $\beta_1$ diventa insensibile all'aggiunta di nuove variabili, ciò che non viene inserito non ha più molta importanza per spiegarlo. Ciò che accade agli altri coefficienti di controllo non interessa: interessa soltanto se vale la pena investire 2 miliardi di dollari l'anno per attuare quell'idea pedagogica.

## Distorsione da variabile omessa: derivazione

Il docente passa a spiegare matematicamente perché la stima cambia in modo sostanziale. Si suppone che la vera relazione tra $X$ e $Y$ sia data dal modello con due variabili, cioè che il vero processo generatore dei dati sia

$$E(Y \mid X_1, X_2) = \alpha + \beta_1 X_1 + \beta_2 X_2,$$

eventualmente con altre variabili. In generale questo modello non è noto a priori, e si può solo approssimare la realtà con qualcosa di statistico. Si comincia con la cosa più semplice, un modello di regressione semplice, con $\tilde{\alpha}$, $\tilde{\beta}$ ed $\tilde{\varepsilon}$. La tilde indica che questi parametri e questo errore sono diversi da quelli del processo generatore:

$$y_i = \tilde{\alpha} + \tilde{\beta} x_{1i} + \tilde{\varepsilon}_i.$$

Il modello di regressione corretto da stimare, se il vero modello è quello a due variabili, sarebbe invece

$$y_i = \alpha + \beta_1 x_{1i} + \beta_2 x_{2i} + \varepsilon_i.$$

L'aspettativa condizionale e il modello di regressione sono la stessa cosa, con in più nel secondo il termine d'errore che fa coincidere le osservazioni con il valore atteso condizionato. Si vuole stimare $\tilde{\beta}$ nel modello semplice, quindi con

$$\tilde{\beta} = \frac{\text{Cov}(y, x_1)}{\text{Var}(x_1)},$$

come nelle lezioni precedenti. Questo stimatore è però basato sul modello sbagliato rispetto al vero modello. Si cerca allora la relazione tra $\tilde{\beta}$ e il vero $\beta_1$. Poiché $y$ è in realtà una combinazione di due variabili, bisogna calcolare come si comporta lo stimatore rispetto alla vera $y$:

$$\tilde{\beta} = \frac{\text{Cov}(\alpha + \beta_1 x_1 + \beta_2 x_2 + \varepsilon,\; x_1)}{\text{Var}(x_1)}.$$

Il numeratore si scompone in somma di covarianze con $x_1$. La covarianza di $\alpha$ con $x_1$ è zero, perché $\alpha$ è una costante. La covarianza tra $\beta_1 x_1$ e $x_1$ è $\beta_1 \text{Var}(x_1)$, perché la covarianza di una variabile con se stessa è la varianza. La covarianza tra $\beta_2 x_2$ e $x_1$ è $\beta_2 \text{Cov}(x_1, x_2)$. Resta la covarianza tra $\varepsilon$ e $x_1$. Si ottiene

$$\tilde{\beta} = \beta_1 + \beta_2 \frac{\text{Cov}(x_1, x_2)}{\text{Var}(x_1)} + \frac{\text{Cov}(\varepsilon, x_1)}{\text{Var}(x_1)}.$$

Nel vero modello $x_1$, $x_2$ ed $\varepsilon$ sono incorrelati, perché si è ipotizzato che valga l'esogeneità. L'ultima covarianza è quindi zero. Ne segue che lo stimatore di $\beta$ non è legato soltanto a $\beta_1$, ma anche alla struttura di correlazione tra $x_1$ e $x_2$. Il numero ottenuto dalla stima di $\beta_1$ è una combinazione di due fattori: una parte è il vero segnale, il $\beta_1$ che si vorrebbe stimare, e una parte è un effetto che dipende dalla correlazione tra le variabili, quella che si è tolta dal modello statistico ma che è presente nel modello teorico. Ciò che si ottiene non è il solo $\beta_1$ ma la somma dei due termini. Per esempio, un valore stimato di $-2{,}2$ potrebbe scomporsi in una somma di un termine più piccolo, come $-0{,}5$, e di un secondo termine, come $-1{,}8$.

> [!question] Da verificare: la trascrizione riporta "meno 2,2 è uguale a meno 0,5 più 1, meno 1,8" ed è illeggibile. Il docente la presenta come un esempio numerico indicativo ("una roba così"), non come valori stimati.

Se in un modello si inseriscono troppo poche variabili, quindi, ciò che si stima è una combinazione di effetti: da una parte l'effetto che si vorrebbe stimare, $\beta_1$, dall'altra la struttura di correlazione tra la variabile omessa, che dovrebbe essere nel modello ma non vi è inclusa per errore, e la variabile inclusa.

### Perché la variabile omessa produce endogeneità

Si tratta di un problema di endogeneità. Nel modello piccolo l'errore $\tilde{\varepsilon}$ è dato dal vero $\varepsilon$ del modello vero più $\beta_2 x_2$:

$$\tilde{\varepsilon}_i = \varepsilon_i + \beta_2 x_{2i}.$$

Tra il modello vero e il modello statistico l'unica differenza è un termine che viene tolto dalla parte sistematica e che quindi resta nell'errore. L'endogeneità nasce dal fatto che $x_2$ e $x_1$ potrebbero essere correlati. Se sono incorrelati, cioè se la loro covarianza è zero, l'effetto distorsivo si annulla e non si ha endogeneità. Lo stesso accade se $\beta_2 = 0$: il termine distorsivo è zero moltiplicato per qualcosa, quindi è zero. Escludere una variabile inutile non produce nulla, e lo stesso vale per una variabile incorrelata con la variabile di interesse. Non serve che la covarianza o $\beta_2$ siano esattamente zero: se sono molto piccoli, l'eventuale problema è trascurabile.

Una delle cause tipicamente più importanti di endogeneità è dunque considerare un modello statistico non coerente con il modello teorico astratto, che non è noto. Per accorgersi del problema, come detto, si può partire da un modello molto semplice e aggiungere i regressori un po' alla volta, togliendo i potenziali fattori confondenti che potrebbero rendere l'errore del modello statistico correlato con il regressore. Semplificando la struttura del termine d'errore la probabilità di endogeneità diminuisce. Altrimenti le stime sono distorte, perché si stima non solo $\beta$ ma $\beta$ più una correlazione.

Questo tipo di endogeneità è caratterizzato dall'uso di un modello troppo piccolo, che induce una distorsione delle stime. Escludendo variabili rilevanti da un modello statistico non si stima più $\beta$ ma $\beta$ più qualcosa. Nei testi di letteratura questa distorsione si chiama **distorsione da variabili omesse**.

### Valutare l'endogeneità dalle sue conseguenze

L'endogeneità non si può valutare a priori: non si può verificare direttamente se l'errore è correlato con le $X$. Si possono però osservare le sue conseguenze, cioè la distorsione. Se la stima di un parametro oscilla molto al variare del modello statistico, probabilmente l'oscillazione è dovuta a endogeneità, che distorce le stime e non permette di valutare correttamente il parametro di interesse.

La strategia consiste quindi nel non fermarsi al primo modello: si parte da un modello e si verifica se il parametro di interesse resta stabile al variare della specificazione. Se resta stabile dopo molti esperimenti, non si può dire di avere risolto il problema, ma si sta andando in quella direzione. È un metodo di lavoro più robusto.

La formalizzazione mostra che, stimando il modello sbagliato, si stima $\beta_1$ più un termine che dipende dalla correlazione tra la variabile inclusa e quella esclusa. Questo termine non sparisce al crescere di $n$. Con un campione più grande la combinazione si stima con maggiore precisione, ma con 10.000, 100.000 o un milione di osservazioni il termine non tende a zero: tende con precisione a un numero. Il risultato asintotico è che lo stimatore del modello sbagliato converge al vero parametro più una costante non calcolabile, che esiste anche se non si sa calcolarla. L'unica speranza è trovare un modello in cui la covarianza tra $x$ ed $\varepsilon$ sia davvero zero. La dimensione del campione non aiuta.

### Regressori in più rispetto al necessario

Un'osservazione non presente nelle slide riguarda il caso opposto. Se il vero modello ha due regressori e se ne stima uno con tre, i due importanti più un terzo, il problema non si pone: ci si aspetta che il terzo regressore abbia impatto nullo, quindi la sua stima sarà circa zero. Se un modello viene sovraparametrizzato, cioè con più regressori del necessario, le stime di $\beta_1$ e $\beta_2$ non cambiano. Al più gli errori standard tendono a diventare un po' più grandi, perché nella procedura di stima si aggiunge qualcosa di inutile: invece di fissare il coefficiente a zero, come dovrebbe essere, lo si fissa alla covarianza campionaria, che non è numericamente zero. Mettere più regressori del necessario non è un problema serio, mentre metterne troppo pochi è un problema sostanziale.

## Errori di misura nei regressori

Esistono altre cause di endogeneità, alcune delle quali saranno viste più avanti. Una seconda causa è più sottile. La prima riguardava un modello statistico con informazione insufficiente. Si suppone ora di avere studiato bene il problema, di avere isolato le variabili necessarie senza escluderne alcuna, e che il modello sia quindi perfetto sulla carta, il problema essendo solo la stima. Si suppone però che una variabile di interesse, il regressore, non si riesca a osservare con precisione: non si ottiene il suo vero valore ma una sua approssimazione.

Un esempio tipico è il consumo delle famiglie italiane come regressore. I dati si ottengono con sondaggi, ben fatti, dall'Istat o simili, ma pur sempre sondaggi. Il questionario contiene domande come: la settimana scorsa sei andato al supermercato, quanto hai speso? Una persona che ha speso 160 euro, senza lo scontrino in mano, non se lo ricorda con esattezza: ricorda più o meno 150, un ordine di grandezza. Se la volta dopo ha speso 140 riporta comunque 150, perché arrotonda. Non riporta il vero valore del regressore ma una sua approssimazione. L'approssimazione è onesta, nel senso che non distorce sistematicamente: qualche volta sovrastima e qualche volta sottostima. È semplice distrazione.

Il modello è corretto e dal punto di vista economico si è ragionato bene, ma i dati sono imprecisi. Ci si chiede se un setup di questo tipo sia un problema dal punto di vista statistico o econometrico. La risposta è che potrebbe esserlo.

Formalmente, il modello economico lega $y$ a $x$ ed è corretto, per cui $x$ ed $\varepsilon$ sono incorrelati.

> [!question] Da verificare: la trascrizione riporta "la correlazione tra y e x è zero, non c'è problema"; dal contesto si tratta della correlazione tra $x$ ed $\varepsilon$, assente se il modello è corretto.

Il problema è che $x$ non è osservata: si osserva una variabile $x^*$, pari al vero $x$ più un termine di distrazione $u$, che è una variabile casuale con media zero e una certa varianza:

$$x^*_i = x_i + u_i.$$

Per semplicità si ipotizza che il termine di distrazione non dipenda da fattori estranei, in particolare non dipenda da $\varepsilon$: è soltanto una distrazione.

Il termine di distrazione non dipende nemmeno da quanto si spende al supermercato: chi è impreciso al 10% lo sarà sempre. Si ipotizza quindi che la covarianza tra $x$ e $u$ sia zero e che la covarianza tra $u$ ed $\varepsilon$ sia zero. Dovrebbe bastare, e se emergono altre condizioni necessarie il docente le segnalerà.

### Il modello calcolabile con regressore impreciso

L'unica cosa che si può fare è stimare la regressione in cui, al posto di $x$, compaiono i dati disponibili, cioè quelli del foglio Excel. I veri valori di $x$ non sono noti e ci si deve fidare di quanto riferiscono i rispondenti. Per distinguere nettamente i due modelli, questo non viene scritto in funzione di $\alpha$ e $\beta$ ma di $\gamma_0$ e $\gamma_1$: $\alpha$ e $\beta$ sono i parametri del processo che genera i dati, $\gamma_0$ e $\gamma_1$ sono i parametri del modello statistico calcolabile, a differenza del modello del vero processo generatore dei dati, che non si può calcolare,

$$y_i = \gamma_0 + \gamma_1 x^*_i + \varepsilon_i.$$

Ci si chiede se $\gamma_1$ sia legato a $\beta$, cioè se il parametro stimato da questa regressione con regressore impreciso fornisca informazioni su $\beta$.

> [!warning] Correzione
> Nelle slide la lettera $u$ è usata due volte, sia per il termine di distrazione sia per l'errore della regressione. Il docente dichiara l'errore di notazione, dice che correggerà le slide e rinomina qui l'errore della regressione $\varepsilon$, mentre $u$ resta il termine di distrazione. Si tratta in ogni caso di termini d'errore, a cui si può assegnare la lettera che si preferisce.

### Calcolo dello stimatore con errore di misura

Lo stimatore dei minimi quadrati di $\gamma_1$ è la covarianza tra $y$ e $x^*$ divisa per la varianza di $x^*$. Per definizione $x^* = x + u$. Per trovare la relazione tra $\gamma_1$ e il vero $\beta$ si riscrive $y$ in funzione del vero $x$ e del vero $\beta$. Calcolare la covarianza rispetto ai veri dati equivale a calcolarla rispetto al data generating process, cioè al processo che genera i dati:

$$\gamma_1 = \frac{\text{Cov}(y, x + u)}{\text{Var}(x + u)} = \frac{\text{Cov}(y, x) + \text{Cov}(y, u)}{\text{Var}(x + u)}.$$

Sostituendo $y = \alpha + \beta x + \varepsilon$ e sviluppando le covarianze con il solito metodo, cioè scrivendo la covarianza di una combinazione come combinazione di covarianze:

$$\gamma_1 = \frac{\beta \,\text{Var}(x)}{\text{Var}(x + u)} + \frac{\text{Cov}(x, \varepsilon)}{\text{Var}(x + u)} + \frac{\text{Cov}(y, u)}{\text{Var}(x + u)}.$$

Per ipotesi il modello corretto, quello con il vero $x$, è perfetto: $x$ è esogeno rispetto a $\varepsilon$ e la covarianza tra $x$ ed $\varepsilon$ è zero. Si ipotizza inoltre che il livello di imprecisione non dipenda da $y$, quindi anche la covarianza tra $y$ e $u$ è zero. È un'ipotesi semplificatrice: la covarianza potrebbe essere diversa da zero. Al denominatore, dato che $x$ e $u$ sono incorrelati, la varianza della somma è la somma delle varianze, perché il doppio prodotto della covarianza si annulla. Resta

$$\gamma_1 = \beta \, \frac{\text{Var}(x)}{\text{Var}(x) + \text{Var}(u)}.$$

Stimando il modello di regressione con errore di misura non si stima quindi $\beta$, ma $\beta$ moltiplicato per un rapporto minore di uno. Il rapporto è minore di uno per costruzione, perché il denominatore è sempre maggiore del numeratore. Se la varianza di $u$ è piccola, cioè la precisione nel riportare i dati è alta e gli errori sono di pochi centesimi, il rapporto tende a uno e $\gamma_1$ e $\beta$ sono di fatto uguali. Se la variabilità di $u$ è grande si ha un problema. Se la varianza di $u$ è uguale alla varianza di $x$, il rapporto vale $1/2$ e si stima $\beta$ per un mezzo.

### Simulazione

Il docente mostra con dati simulati che cosa accade. Si generano $200$ osservazioni dal modello di regressione semplice, quindi con il processo generatore noto, con $\varepsilon$ normale $N(0,1)$ e $x$ normale $N(0,1)$. I veri valori sono $3$ per l'intercetta e $1{,}5$ per il coefficiente di $x$. La stima restituisce $3{,}07$ per la costante e $1{,}42$ per il coefficiente di $x$. Il valore vero $3$ cade nel rispettivo intervallo di confidenza, così come $1{,}5$ in quello del coefficiente: il modello funziona e i dati restituiscono ciò che ci si aspetta. È un esperimento di laboratorio, quindi si sa che cosa aspettarsi.

Si stima poi la regressione di $y$ su $x^*$, dove $x^*$ è $x$ dei dati precedenti più un termine d'errore normale con media zero e varianza uno. La varianza di $x$ è uno, e servirà a breve. L'intercetta è stimata a $3{,}13$, con intervallo di confidenza da $2{,}93$ a $3{,}33$, che contiene il vero valore. Il problema riguarda $\beta$, stimato a $0{,}7$ contro il vero valore $1{,}5$. Un test di ipotesi sulla coerenza di $0{,}7$ con $1{,}5$ potrebbe non rifiutare se la precisione della stima fosse sufficientemente scarsa, cioè se i dati fossero molto dispersi e l'intervallo molto ampio, tale da contenere $1{,}5$. Qui invece l'intervallo di confidenza, che unisce stima e precisione, va da circa $0{,}55$ a $0{,}85$, e $1{,}5$ non vi cade neanche vicino. Si ottiene sistematicamente un risultato diverso dalla verità. Nel modello precedente tutto aveva funzionato bene, quindi il campione non è troppo piccolo.

Il valore $0{,}7$ non è il vero $\beta$: è $1{,}5$ per un mezzo. Poiché la varianza di $x$ è uno per costruzione e la varianza di $u$ è uno, con i dati imprecisi si stima $\beta$ moltiplicato per un mezzo. Se ci si aspetta un $\beta$ positivo, la stima risulta circa la metà.

### Attenuation bias

Il fatto che, con $\beta$ positivo, un modello di questo tipo dia stime sistematicamente più basse di quelle desiderate si chiama **attenuation bias**: in un contesto del genere il parametro di interesse viene sottostimato in modo regolare. La distorsione è la differenza tra $\beta$ e $\beta/2$, cioè tra il vero valore del parametro e il coefficiente stimato, pari a un mezzo di $\beta$.

La distorsione è circa $0{,}75$, cioè la differenza tra $1{,}5$ e $0{,}75$.

> [!question] Da verificare: la trascrizione riporta "la distorsione è circa 0,75, la metà di un mezzo". Con $\beta = 1{,}5$ e fattore di attenuazione $1/2$ la distorsione è $\beta - \beta/2 = 0{,}75$, cioè la metà di $\beta$.

Il docente osserva di avere scelto per caso un esempio in cui la distorsione e il coefficiente di attenuazione, un mezzo, coincidono. Rifarà gli esempi con una varianza di $u$ diversa da quella di $x$, in modo che il fattore di riduzione della stima non sia esattamente un mezzo e i numeri siano meno simmetrici. L'idea resta la stessa: anche con il modello perfetto in mente, se i dati sono imprecisi, per esempio perché ottenuti da un campionamento fatto male, la stima è inadeguata.

### Errori di misura in finanza

In finanza questo problema è frequente, perché molte procedure di stima si basano su stime ripetute: da una prima regressione si stimano dei coefficienti, poi si fa una regressione in cui i coefficienti stimati in precedenza sono usati come regressori. Si procede così, tipicamente, per validare dal punto di vista statistico modelli come il CAPM, cioè per verificare se sono credibili sui dati. I coefficienti stimati sono variabili approssimate: non sono il vero valore del parametro ma il vero valore al netto di un errore di stima, un errore campionario. Ciò può creare endogeneità e problemi collegati.

Un altro esempio è l'inserimento della volatilità di un investimento in un modello di regressione che spieghi la performance. La volatilità non è osservabile direttamente e può solo essere stimata. Nel modello entra quindi la volatilità stimata, che non è un indicatore esatto della volatilità oggettiva ma la migliore approssimazione disponibile. Usarla come regressore crea endogeneità, e gli stimatori tendono a sottostimare il vero valore del parametro.

### Ridurre l'errore di misura con osservazioni ripetute

Istituti che fanno professionalmente questo lavoro, come l'Istat o la Banca d'Italia, o istituti di ricerca che lavorano bene, cercano di correggere il problema. Se i dati sono scadenti c'è poco da fare: si può pensare al modello migliore, ma la stima resta scadente. Uno schema possibile è osservare una famiglia non una sola volta, cioè non solo quanto ha speso la settimana scorsa, ma per un periodo abbastanza lungo, per esempio dieci settimane. Per la famiglia $i$-esima si hanno allora dieci osservazioni, $x_{i1}, x_{i2}, \dots, x_{i,10}$, la spesa della settimana uno, due, fino a dieci. Il livello di precisione di ogni singola osservazione è dato dall'errore $u$, e la varianza di ciascuna osservazione è la varianza di $u$: è l'imprecisione fisiologica.

Se la varianza di $u$ è grande, il modello di regressione ha un problema. Si possono però aggregare i dati: invece dei dieci numeri se ne calcola la media aritmetica. In generale, con $n$ osservazioni per la famiglia $i$:

$$\bar{x}_i = \frac{1}{n} \sum_{j=1}^{n} x_{ij}.$$

Questa media diventa il regressore per quella famiglia. Ha senso perché, per le proprietà dello stimatore media aritmetica, che è uno stimatore della media della popolazione, la sua varianza è $\frac{1}{n} \text{Var}(u)$, supponendo che le osservazioni siano indipendenti. I passaggi sono nelle slide dei richiami di statistica. Con dieci informazioni per famiglia e un livello di precisione del 10%, la varianza della media è $\frac{1}{10} \cdot 10\% = 1\%$ circa, molto più piccola. Il rapporto $\text{Var}(x) / (\text{Var}(x) + \text{Var}(u))$ diventa praticamente uno. Più grande è $n$, cioè il numero di osservazioni per la stessa unità statistica, più piccolo è l'effetto dell'imprecisione. Un modo rapido di risolvere il problema è quindi, invece di un'unica intervista sulla spesa della settimana, chiederla quattro o cinque volte e fare la media: la media è molto più precisa di ogni singola osservazione, perché la sua varianza è la varianza dell'imprecisione di ogni osservazione divisa per il numero di osservazioni.

Esistono metodi più sofisticati, anche perché chiedere la stessa informazione dieci volte per dieci settimane è costoso. Il punto è che il problema va risolto a monte. Con regressioni su dati di una survey fatta su internet in modo rapido, gli errori di misura rischiano di non essere considerati seriamente, e le stime possono essere fortemente distorte anche se il modello è corretto.

### Errore di misura come secondo caso di endogeneità

Questo è un secondo caso di endogeneità. Si può fare poco, ma chi sa a monte che i dati potrebbero avere un errore di misura deve automaticamente pensare all'endogeneità. Nel caso precedente la si era riconosciuta perché lo stimatore era distorto: se c'è endogeneità c'è distorsione.

> [!tip] Esame
> La formalizzazione dell'endogeneità da errore di misura è nelle slide e il docente dice che non è così importante.

La formalizzazione mostra che, nella regressione stimata, la covarianza tra il regressore e il termine d'errore è proporzionale alla varianza dell'errore di misura. È la stessa cosa vista prima da un altro punto di vista: prima si è osservato che cosa accade allo stimatore con dati imprecisi, ora si vede che nella regressione stimata esiste una correlazione tra il regressore e il termine d'errore implicito del modello. Questo termine dipende dalla varianza di $u$ e non è comprimibile.

In un'applicazione finanziaria che inserisca la volatilità nel modello di regressione, si deve sapere che la volatilità è uno stimatore e quindi contiene un errore di misura, cioè lo standard error della stima. Bisogna perciò interpretare i risultati con attenzione, perché le stime del modello potrebbero essere distorte.

Nelle applicazioni finanziarie più recenti si risolve tipicamente usando dati ad alta frequenza per calcolare la volatilità di un giorno. I dati ad alta frequenza sono osservati a intervalli di pochi secondi: in un giorno possono esserci 100.000 osservazioni sulle variazioni di prezzo dello Standard & Poor's. Queste microvariazioni servono a stimare la volatilità dell'intera giornata, e l'indicatore è molto preciso perché si mediano molte osservazioni nel corso della giornata. Con un modello di tipo ARCH, tipico dell'analisi finanziaria, la stima della volatilità si basa invece su un'unica osservazione, il rendimento di quel giorno specifico. La stima è buona in media, ma non molto precisa.

> [!question] Da verificare: la trascrizione riporta prima "100.000 osservazioni" e poi "4-500 osservazioni" nella stessa giornata, e "Si è usato un modello di tipo ARCH", che qui è reso come contrasto con i dati ad alta frequenza.

L'idea è dunque usare più dati per stimare un parametro. I dati intragiornalieri possono essere utili, con alcuni accorgimenti: in quel contesto usare troppi dati potrebbe comunque essere problematico, e se ne parlerà più avanti.

## Riepilogo dei due casi di endogeneità

Sono stati presentati due concetti di endogeneità. L'endogeneità è un concetto astratto, una covarianza: il problema è capire quando quella covarianza è diversa da zero. Nel primo caso il modello ha troppo poche variabili. Per correggerlo si provano ad aggiungerne altre, in modo sensato, perché bisogna preservare la logica del modello e non inserire variabili a caso. Si osserva poi se l'effetto distorsivo sul parametro persiste o sparisce, e questo è l'unico modo per vedere se c'è endogeneità. Concettualmente è il caso più semplice: si aggiunge informazione al modello finché la stima del parametro di interesse si stabilizza. Il problema dell'errore di misura è più sottile perché non dipende da chi stima: anche con il modello migliore del mondo, se i dati sono poveri le stime sono sbagliate. Bisogna affidarsi a dataset sufficientemente affidabili e standardizzati, e sapere comunque che il problema esiste.

> [!question] Da verificare: il docente dice "Finisco il quarto oggi" senza precisare a che cosa si riferisca (probabilmente il quarto argomento o capitolo del programma).

### Errore di misura sulla variabile dipendente

Un'osservazione non presente nelle slide, che si dimostra facilmente: finora si è considerato l'errore di misura sulla $x$. Se l'errore fosse sulla $y$, ci si potrebbe aspettare una situazione ancora peggiore, ma non è così: non cambia nulla. Gli errori standard di tutti i coefficienti diventano più grandi, perché l'errore di misura entra nel termine d'errore. Poiché però è incorrelato con $x$ e con qualsiasi altra variabile, non crea alcun problema di distorsione. Lo si verifica ripetendo il ragionamento precedente con $y + u$ al posto di $y$: $x$ non ha problemi e il $\gamma$ stimato risulta uguale a $\beta$. Cambia la varianza del termine d'errore, ma non c'è distorsione.

> [!question] Da verificare: la trascrizione riporta "ancora è correlato con x"; dal ragionamento si tratta di un errore di misura incorrelato con $x$.

Uno studente pone una domanda su $\gamma$, di cui la trascrizione riporta solo l'inizio ("Perché hai detto che gamma..."). Il docente risponde che il segno meno compare nel calcolo della varianza e si trasferisce nel risultato. Aggiunge di avere saltato oggi i passaggi algebrici perché la vede in modo più intuitivo con il ragionamento fatto sopra: la distorsione è $\beta$ meno un termine più piccolo, quindi è in senso negativo.

> [!question] Da verificare: la domanda dello studente e la risposta sono incomplete nella trascrizione. Il riferimento al "segno meno" non permette di stabilire a quale formula si riferisca.

Per concludere questa parte introduttiva, il modello di regressione multipla è la stessa cosa del modello di regressione semplice con più variabili. Sono stati spiegati due casi in cui si può avere endogeneità. Almeno un altro caso sarà visto prima della fine del corso, ma solo nell'ambito delle serie storiche. Esistono anche altri casi non trattabili nell'ambito di questi modelli, quando non si è in grado di stabilire se è $X$ a causare $Y$ o viceversa. Si presentano specificamente nei modelli macroeconomici, quindi chi non è interessato alla macroeconomia non li incontrerà.

## Ipotesi del modello di regressione multipla

Per stimare un modello di regressione le ipotesi sono sintetizzate nelle slide. Il modello deve essere lineare nei parametri, cioè combinazione lineare di parametri per variabili. Può essere non lineare nelle variabili: come visto nella lezione precedente, si possono usare variabili in scala logaritmica, che implicano una relazione non lineare tra $X$ e $Y$. L'ipotesi richiede solo che $\beta$ moltiplichi la variabile $X$, qualunque essa sia: un logaritmo, un polinomio o altro. Le ipotesi sono le seguenti:

- la covarianza tra ogni $X$ del modello ed $\varepsilon$ è zero, cioè vale l'esogeneità, la condizione importante;
- i dati sono campionati in modo indipendente dalla popolazione, almeno in questa parte del corso: ogni unità statistica è campionata indipendentemente, quindi le sue caratteristiche sono indipendenti dalle realizzazioni delle altre unità;
- le variabili $X$ e $Y$ hanno momenti finiti fino all'ordine quarto, un'ipotesi tecnica necessaria per applicare il teorema del limite centrale e la legge dei grandi numeri e fare inferenza asintotica;
- al momento si ipotizza l'omoschedasticità, perché è più comodo, e si vedrà poi che cosa accade con l'eteroschedasticità;
- nel modello di regressione multipla si aggiunge, rispetto al modello semplice, l'assenza di perfetta collinearità tra i regressori.

### Momenti finiti e code della distribuzione

Il tema dei momenti di ordine superiore non era stato trattato a lungo nelle lezioni precedenti. Averli finiti significa che la dispersione della distribuzione non può essere troppo grande: le code della distribuzione di probabilità di $X$ e $Y$, di cui qui non si ipotizza la forma, non possono essere troppo pesanti. Deve essere possibile calcolare la media teorica nella popolazione di quelle variabili casuali. Con una variabile Cauchy, o una t di Student con tre gradi di libertà, potrebbe esserci un problema, perché non si hanno i momenti. Se i dati hanno code troppo pesanti è un problema.

Come esempio mentale, si supponga di dovere calcolare il reddito medio delle persone che vivono in Texas. Non si vuole che nel campione ci siano troppe persone troppo povere o troppo ricche, perché la probabilità di estrarre qualcuno come Elon Musk diventerebbe alta. Il docente precisa di non avercela con lui. Il problema è statistico: se nel campione compare una persona con un reddito annuo o un patrimonio di miliardi di dollari, la media risulta distorta al rialzo, e si otterrebbe un reddito medio del Texas di 60 milioni di dollari, che non è un indicatore sensato. Intuitivamente si vuole evitare che le osservazioni siano troppo estreme rispetto alla media e che nella popolazione ci siano troppi outlier, perché altrimenti estrarre a caso unità con quelle caratteristiche sbilancia i calcoli e distorce tutte le stime. In termini tecnici, i momenti fino al quarto ordine sono finiti: non ci sono varianze troppo grandi né esplosive.

### Perfetta collinearità

Il docente chiede se il concetto di perfetta collinearità sia già noto, e lo spiega perché non tutti sembrano conoscerlo. In un modello di regressione multipla le variabili $X$ sono correlate tra loro: come visto, il reddito è correlato con la dimensione della classe. Ci si chiede che cosa accade quando la correlazione tra due variabili incluse nel modello è troppo grande, o meglio è massima, cioè uguale a uno. Se due variabili hanno correlazione esatta, conoscendone una si può prevedere esattamente l'altra.

Come esempio, si consideri il modello del salario in funzione del livello di istruzione, a cui si aggiunge il genere, per capire se esistano distorsioni salariali, per esempio tra uomini e donne, a parità di istruzione. Se dal modello risultasse un effetto sistematicamente distorsivo dei salari, indipendente dal livello di istruzione e dalla capacità, sarebbe un problema serio.

> [!question] Da verificare: la frase della trascrizione è sintatticamente confusa ("è un problema serio, perché il problema serio mi dice che c'è un effetto sistematicamente distorsivo dei salari"); è riportata nella lettura più probabile, con valore ipotetico.

Un effetto sistematico dei salari legato al genere sarebbe un problema gravissimo. Per verificarlo si vuole inserire nel modello una variabile che tenga conto del genere delle persone. Si suppone che i generi siano soltanto due, maschio e femmina, e si costruisce il modello

$$\text{salario}_i = \alpha + \beta_1 \,\text{istruzione}_i + \beta_2 M_i + \beta_3 F_i + \varepsilon_i,$$

dove $M$ ed $F$ sono due variabili etichetta. $M$ vale uno se il lavoratore è maschio e zero se è femmina, mentre $F$ vale zero per un lavoratore maschio e uno per una lavoratrice.

> [!question] Da verificare: la trascrizione riporta la definizione di $F$ in forma confusa; la lettura è ricavata dal seguito ("se $M$ è uno, $F$ è zero, e se $M$ è zero, $F$ è uno").

Le due variabili $M$ ed $F$ sono correlatissime: se $M$ è uno, $F$ è zero, e se $M$ è zero, $F$ è uno. Dato $M$ si prevede esattamente $F$, quindi la correlazione tra $M$ e $F$ è esattamente uno.

### Effetto marginale non definibile

Alla luce di ciò che è stato detto prima sull'effetto marginale, ci si chiede se un modello di questo tipo abbia senso dal punto di vista logico. Il parametro $\beta_2$ rappresenta l'effetto di essere maschio sul salario al netto delle altre variabili. Nell'esempio delle scuole l'effetto marginale si calcolava modificando la variabile di interesse e tenendo fisse le altre: si fissava il reddito e si modificava la dimensione della classe. Qui non si può farlo. Se si prendono due lavoratori del tutto equivalenti e si modifica la caratteristica $M$, automaticamente si modifica anche $F$, perché le due variabili sono perfettamente correlate. Non si può fissare una variabile e osservare l'effetto dell'altra, perché a una variazione di una corrisponde sempre una variazione dell'altra. Non è un problema di campione: è sistematico e deterministico.

I regressori $M$ ed $F$ sono perfettamente collineari, e si dice che il modello statistico non è correttamente specificato. Dal punto di vista matematico, stimare quel modello richiederebbe quattro parametri, $\alpha$, $\beta_1$, $\beta_2$ e $\beta_3$, ma il modello non è utilizzabile perché non permette di identificare gli effetti marginali: se non si possono fissare le altre variabili mentre una cambia, ogni variazione di una variabile riequilibra anche l'altra.

### Riparametrizzazione e problema di identificazione

La relazione tra le due variabili è $M = 1 - F$. Imponendo questa identità, che ricostruisce semplicemente la natura dei dati, il modello si riscrive come

$$\text{salario}_i = \alpha + \beta_1 \,\text{istruzione}_i + \beta_2 (1 - F_i) + \beta_3 F_i + \varepsilon_i.$$

I due modelli sono assolutamente equivalenti, perché si è soltanto imposta un'identità. Ordinando i termini, l'intercetta è $\alpha + \beta_2$, cioè $\alpha$ più $\beta_2$ moltiplicato per uno, il coefficiente di istruzione è $\beta_1$ e il coefficiente di $F$ raccoglie $\beta_3$ e $-\beta_2$:

$$\text{salario}_i = (\alpha + \beta_2) + \beta_1 \,\text{istruzione}_i + (\beta_3 - \beta_2) F_i + \varepsilon_i.$$

> [!warning] Correzione
> Alla lavagna il docente dice prima che il coefficiente di $F$ è $\beta_2 + \beta_3$. Uno studente osserva che dovrebbe essere diverso, e il docente riconosce di avere saltato un passaggio: da $\beta_2 (1 - F)$ resta $-\beta_2 F$, che si raccoglie con $\beta_3 F$ e dà $\beta_3 - \beta_2$. Lo studente aveva ragione. Nel seguito il docente continua a dire "beta due più beta tre"; qui il coefficiente è riportato nella forma corretta.

Il problema è che il primo modello si aspetta un output con quattro righe, quattro parametri, mentre il secondo ne ha tre: come già visto con Peruzzi, il numero di parametri stimati è uguale al numero di regressori inseriti nel modello, cioè la costante, istruzione e $F$. Stimando il secondo modello si ottengono un $\hat{\alpha}$ che è $\alpha + \beta_2$, un $\hat{\beta}_1$ uguale a $\beta_1$ e un coefficiente della variabile femmina dato dalla combinazione di $\beta_2$ e $\beta_3$. Il docente precisa che questa scrittura è un po' impropria e non formalmente corretta. L'intercetta stimata è la combinazione di due parametri del modello sopra, e il coefficiente di $F$ è la combinazione di $\beta_2$ e $\beta_3$.

Se non ci fossero problemi, da queste tre stime si dovrebbero ricavare $\alpha$, $\beta_1$, $\beta_2$ e $\beta_3$ del modello originale. Ma le stime sono tre numeri: si ha un sistema di tre equazioni in quattro incognite, che ha infinite soluzioni. Dalle stime del modello semplificato non si possono quindi ricostruire, cioè identificare, i parametri del modello originale. Si ha un **problema di identificazione**. Aggiungere $F$ o $M$ ha aggiunto un parametro al modello senza aggiungere informazione per la stima: il modello è più complicato, ma la statistica non è in grado di dare informazioni su tutti i parametri.

### Fissare un parametro a zero

Poiché le soluzioni sono infinite, dal punto di vista operativo si può ricondursi a un caso in cui il sistema sia stimabile, passando da un modello all'altro. I due modelli sottolineati sono identici dal punto di vista matematico, perché si è soltanto applicata un'identità. Si può scegliere una soluzione specifica, la più semplice: fissare $\beta_3 = 0$. Con questa scelta il coefficiente stimato di $F$ coincide con $\beta_2$ e l'intercetta con $\alpha + \beta_2$, dove $\beta_2$ è noto.

> [!question] Da verificare: la trascrizione riporta "la mia stima coincide con beta 2 e l'alfa coincide con l'alfa". Con la forma corretta del coefficiente di $F$ ($\beta_3 - \beta_2$), fissando $\beta_3 = 0$ il coefficiente è $-\beta_2$.

Ci si chiede se porre $\beta_3 = 0$ crei un problema di interpretazione. Il docente dice che ne parlerà il giorno successivo, ma anticipa la risposta: ipotizzare che il coefficiente della variabile femmina sia zero non crea alcun problema di interpretabilità del modello. Porre $\beta_3 = 0$ non significa togliere le donne dal campione, ma togliere il coefficiente del regressore femmina, cioè un regressore ridondante. Come si interpreta il modello di regressione in questo contesto sarà spiegato nella lezione successiva.

Quando i dati sono esattamente correlati non si riesce più a identificare. Il punto intuitivamente più importante è il problema logico: non si possono più fissare tutte le variabili e muoverne una per calcolare l'effetto marginale. Dal punto di vista matematico ci si riduce a risolvere un sistema di tre equazioni in quattro incognite, il che è impossibile. Si fissa quindi un parametro a un valore standard, zero: se il parametro è zero, si toglie il regressore corrispondente e si osserva che cosa accade alle altre variabili.

### Domande a fine lezione

Il docente chiede se ci sono domande su quanto visto nella lezione. Uno studente chiede dei termini $\beta_2$ e $\beta_3$ nel coefficiente di $F$. Il docente riconosce l'errore, spiegato nella correzione sopra, e ringrazia. La lezione continua il giorno successivo, con una spiegazione più approfondita.
