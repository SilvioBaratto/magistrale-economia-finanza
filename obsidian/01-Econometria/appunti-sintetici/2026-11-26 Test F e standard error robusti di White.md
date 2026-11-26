---
corso: Econometria
data: 2026-11-26
fonte: Audio/econometria/econometria_2026-11-26.txt
# registrazione interrotta dall'allarme antincendio, unita in ordine (prima parte sopra, seconda parte sotto)
# fonte: Audio/econometria/econometria_2026-11-26-2.txt
tipo: appunti-sintetici
tags: [appunti-sintetici, econometria]
revisione: sintesi a punti degli appunti della stessa lezione
---

# Test F e standard error robusti di White

## Ripasso: test su più parametri

- Si riprendono i test su più di un parametro, con due esempi.

### Combinazione lineare di due coefficienti

- ==calcolatevi sempre tutte le casistiche, quando avete le dummy, 0, 1, tutti i casi che vi servono==.
- Si comparano spesso due gruppi con la differenza delle due regressioni: sposati black contro sposati non black dà $\beta_6 - \beta_8$.

> [!tip] Esame: nel compito, con le dummy, calcolarsi sempre tutte le casistiche.

*(slide 4)*

- Mettendo le stime nella combinazione si ottiene un numero, ma serve un test di significatività per capire se è distinguibile da 0.
- Si può usare la statistica t, perché lo stimatore è gaussiano e la differenza di due gaussiane è gaussiana.
- Il problema è lo standard error: la radice della varianza di un coefficiente più la varianza dell'altro, meno due volte la covarianza.
- La covarianza non è immediata da un output standard; con cinque parametri combinati vanno calcolate tutte le covarianze ed è facile sbagliare.
- Si può fare, ma è incasinato.

> [!question] Da verificare: la trascrizione riporta "perché vanno le ipotesi"; probabilmente "valgono".

*(slide 5)*

### Significatività congiunta di più regressori

- Il primo esempio è una combinazione lineare con una sola restrizione.
- Il secondo, con tre regressori, verifica se almeno uno è utile per prevedere la Y, cioè $\beta_1 = 0$, $\beta_2 = 0$, $\beta_3 = 0$ tutti insieme, non uno alla volta.
- La strategia naïf è una sequenza di tre statistiche t: se nessuna rifiuta vale la nulla globale, se almeno una rifiuta esiste un coefficiente diverso da 0 e si rifiuta la nulla.

> [!question] Da verificare: la trascrizione riporta "La strategia che Nair" e "verrà la nulla globale"; si adottano "naïf" (slide 7) e "vale".

*(slide 7)*

### Perché la sequenza di test t non funziona

- Ogni test t fissa la probabilità di sbagliare, per esempio all'1% o al 5%, cioè rispetto all'errore del primo tipo non si sbaglia il 95% delle volte; la probabilità congiunta di errore non è più il 5%, può essere tre volte tanto, o quasi, anche con tre test indipendenti, e in realtà non lo sono.
- Non si sa più quante volte si sbaglia, se il 30%, il 99% o cosa, quindi il test è inaffidabile.
- Serve un test unico con la probabilità di sbagliare fissata, che non cambia al cambiare della complessità dell'ipotesi nulla.

> [!question] Da verificare: la trascrizione riporta "questa probabilità non sbaglia al cambiare"; probabilmente "non cambia".

*(slide 8)*

### Restrizioni lineari

- Entrambi gli esempi sono una o più combinazioni lineari di parametri.
- Esempio 1: $\beta_6 - \beta_8$ è $0 \cdot \beta_1 + 0 \cdot \beta_2 + 1 \cdot \beta_6 + 0 \cdot \beta_7 - 1 \cdot \beta_8$, e avanti così, posta uguale a 0, con pesi noti a priori 0, 0, 1, 0, meno 1, 0 e il resto 0.
- Il vettore dei pesi per il vettore dei parametri $\beta$ dà $\beta_6 - \beta_8$: è una restrizione lineare, e vale anche per il sistema di ipotesi.

> [!question] Da verificare: la trascrizione riporta "beta 1, beta 2, beta 3, beta... conterranno, facciamo che siano beta 9"; "conterranno" è reso con "e così via".

- Esempio 2: $H_0$ è $\beta_1 = \beta_2 = \beta_3 = 0$, cioè tre restrizioni, ciascuna con peso 1 per un parametro e 0 per gli altri, uguale a 0.
- In forma matriciale è la matrice dei pesi, con la costante $\alpha$ nella prima colonna (0, 0, 0) e poi 1, 0, 0, 0, 1, 0, 0, 0, 1:

$$R = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

> [!question] Da verificare: la trascrizione riporta "scrivere A, qua mi sono dimenticato la costante"; "A" è reso con "la matrice dei pesi".

- Moltiplicando $R$ per il vettore dei parametri $\alpha$, $\beta_1$, $\beta_2$ e $\beta_3$ si ottiene una combinazione lineare multivariata uguale a un vettore di zero.
- Non serve che sia sempre zero: $R\beta = 0$ è il caso dell'esempio, in generale $q$ è una sequenza di numeri che mi possono interessare.
- Se l'ipotesi nulla è scrivibile come una o più combinazioni lineari di parametri si usa il test F, che verifica in blocco tutte le sottoipotesi in un unico step, senza perdere il controllo della probabilità di errore.

### Confronto tra modello ristretto e modello completo

- Si confronta il modello sotto l'ipotesi nulla (qui i tre parametri uguali a 0) con il modello completo, sotto l'alternativa.
- Se i dati sono coerenti con la nulla i due modelli devono dare lo stesso risultato qualitativo; serve un numero che identifichi la performance, per esempio la differenza tra l'$R^2$ del modello completo e quello del modello non completo.
- Differenza grande: imporre la nulla peggiora tanto (non può migliorare, matematicamente parlando), i dati non sono coerenti e la si rifiuta.
- Differenza piccola: i dati sono già coerenti con la nulla e non la si rifiuta.
- Questa strategia si chiama statistica F.

*(slide 10)*

- $R^2_c$ è l'$R^2$ del modello completo, $R^2_r$ quello del modello ristretto, ipotizzando vera la nulla; la statistica chiave è la differenza.
- ==se la differenza è piccola mi aspetto che la nulla sia credibile perché imponendo o non imponendo il vincolo ottengo lo stesso risultato==.

### La distribuzione della statistica F

- Serve una distribuzione di probabilità per dire se un numero è grande o piccolo: una t uguale a 0,7 si confronta con le code della normale, più o meno 1,96, più o meno 1,64.
- Per la differenza degli $R^2$ non è nota, ma tenendo il numeratore e dividendo per costanti positive si ottiene la distribuzione F, credo per Fisher.
- Il numeratore è la differenza di performance diviso $s$, il numero di restrizioni: 1 nell'esempio 1, 3 nell'esempio 2.
- La formula la calcola il software; ==è importante capire qual è la filosofia che ci sta alla base==.

> [!tip] Esame: non serve ricordare a memoria la formula della statistica F, conta capire la filosofia.

- Il denominatore è 1 meno l'$R^2$ del modello completo, positivo perché l'$R^2$ è tra 0 e 1, e $n-k-1$, osservazioni meno regressori meno la costante, anch'esso positivo: servono solo a standardizzare la differenza, quindi la F è grande se la parte rossa è grande.

> [!question] Da verificare: la trascrizione riporta "quel diviso 6"; si adotta "$s$" come nella slide 11.

*(slide 11)*

- La distribuzione ha un grafico reso da ChatGPT.

> [!question] Da verificare: la trascrizione riporta "nella versione vecchia delle luci"; probabilmente "dei lucidi".

*(slide 13)*

- È definita solo sull'asse positiva, perché l'$R^2$ del modello senza vincoli deve essere migliore per forza dell'$R^2$ del modello senza vincoli, quindi la differenza è sempre positiva.

> [!question] Da verificare: la trascrizione riporta "senza vincoli" due volte; probabilmente il secondo è "con vincoli".

### Soglia, regola di decisione e p-value

- F vicina allo zero: più probabile la nulla; F grande: più probabile l'alternativa, perché i due $R^2$ sono molto diversi.
- Esempio con tre gradi di libertà e 60, cioè $s = 3$, $n-k-1 = 60$, numeri che si calcolano.
- Sotto la nulla tutte le F seguono quella distribuzione; si fissa una soglia tale che la probabilità oltre la soglia sia l'$\alpha$ per cento, 5%, l'area rossa; una F oltre la soglia porta a rifiutare la nulla, anche se non è impossibile che provenga dalla curva blu.
- ==non può mai capitarvi qualcosa che non sia un test unilaterale a destra==.
- Se la F è maggiore della soglia si rifiuta la nulla, sennò si vota per la nulla; la probabilità massima di sbagliare è $\alpha$ per cento e non dipende da quanti vincoli ci sono: $\beta_1 = 0$, $\beta_2 = 0$, $\beta_3 = 0$ è un unico step, non tre sottotest.
- Il p-value è di un test unilaterale a destra: oltre la soglia è minore di $\alpha$ per costruzione, prima della soglia è maggiore dell'$\alpha$ per cento.
- La decisione è sempre la stessa: F a sinistra o a destra della soglia, oppure p-value più grande o più basso del livello imposto; la soglia è il valore critico.

> [!question] Da verificare: la trascrizione riporta "maggiore di questa soglia" mentre il docente indica un punto della coda, cioè il valore osservato.

*(slide 14)*

- I software calcolano la soglia e normalmente direttamente il p-value, la stessa cosa; il vantaggio è risolvere il problema di test multipli in modo standardizzato con un'ipotesi nulla credibile.

### Il test t come caso particolare del test F

- Una statistica t standard si scrive come test F con un'unica restrizione di uguaglianza.
- Una statistica F con un grado di libertà e $n-k-1$ gradi di libertà è matematicamente una statistica $t$ alla seconda.
- Con un unico vincolo il test F deve dare lo stesso p-value del test t, anche se si basa su distribuzioni completamente diverse.

### Il test F in Gretl: sposati black e non black

- Esempio al volo col software, ==se vi do un output dal software dovreste riuscire a capire come leggere l'output==.

> [!tip] Esame: nel compito può esserci un output del software da saper leggere.

- Il modello è tra persone sposate e non sposate, stimato dal menu Modello con i minimi quadrati ordinari, i soli modelli lineari del corso.
- La variabile dipendente è il logaritmo del salario; i regressori sono le quattro dummy, education, experience, tenure, south e urban.

> [!question] Da verificare: la trascrizione riporta "il devessore deve andare"; nel testo "si deve andare".

- Il software elimina single non black per la perfetta collinearità; toglierne una o un'altra è la stessa cosa, cambia solo l'interpretazione dei coefficienti.
- Dal menu Test, Vincoli lineari, il test F è un test in cui l'ipotesi nulla è una sequenza di uno o più vincoli lineari; qui $\beta_6 - \beta_8$ posta uguale a zero.

> [!question] Da verificare: la trascrizione riporta "una sequenza di v o più vincoli lineari"; nel testo "uno o più".

- In Gretl un parametro si seleziona con b e il nome della variabile tra parentesi quadre: `b[marr_black]` meno b di married non black definisce $\beta_6 - \beta_8$, uguale a zero.

> [!question] Da verificare: la trascrizione riporta "med black"; si adotta la forma "b[marr_black] - b[marr_nonblack] = 0" della slide 18.

- L'output riporta l'ipotesi nulla e il test, F con 1 e 926 gradi di libertà, valore 19,59 (la differenza degli $R^2$ riscalata) e p-value $1{,}06 \cdot 10^{-5}$, praticamente zero.

> [!question] Da verificare: la slide 18 riporta F(1, 926) = 19,60 e p-value 0.000; il docente legge 19,59 e 1,06 per 10 alla meno 5.

- Si rifiuta la nulla: quella restrizione non è diversa da zero, i due gruppi sono statisticamente distinguibili, uno guadagna di più e l'altro di meno a parità di tutte le altre condizioni.
- Il software riporta anche il modello sotto la nulla, con i coefficienti di married black e married non black uguali; il resto è automatico, basta capire la filosofia.

> [!question] Da verificare: la trascrizione riporta "Quella restrizione non è diversa da zero", mentre la nulla è rifiutata; segue una frase lasciata a metà.

### Test F con due restrizioni

- Si vuole vedere se l'effetto marginale di education ed experience è congiuntamente uguale a zero: due restrizioni, il coefficiente di experience uguale a zero e b di tenure uguale a zero.
- ==ogni riga fa riferimento a un test diverso==: i due vincoli vanno su righe diverse, sennò dà errore, almeno nelle versioni più vecchie.

> [!question] Da verificare: la trascrizione riporta "education ed experience"; i vincoli enunciati dopo riguardano experience e tenure.

- Il primo grado di libertà è 2, non più 1, perché i vincoli sono due; il p-value è sempre zero, si rifiuta la nulla.
- Almeno uno dei due coefficienti è diverso da zero, e in realtà lo sono tutti e due; il software stima anche il modello con i due parametri fissati a zero.

> [!question] Da verificare: la trascrizione riporta "la virgola non è credibile"; nel testo "la nulla non è credibile", e la prima parte della frase non è riportata.

### Test F con tre restrizioni, anche diverse da zero

- Un test con tre vincoli, due di esclusione e uno con una combinazione lineare qualsiasi, urban meno south più quattro per b di education, uguale a 0.6, non a zero; numeri a caso.
- La configurazione è mezza in inglese e mezza in italiano: negli output la virgola è il separatore decimale, nel comando bisogna mettere il punto.
- I gradi di libertà sono 3, la statistica F è 21 e il modello è stimato in modo che valga la nulla: urban meno south più quattro volte education viene esattamente 0,6.
- Si calcola l'$R^2$ di quel modello e lo si compara con quello originale; col computer conta capire che test fare e come interpretarlo.
- ==Dovete solo capire che non si possono fare test t ripetuti, perché non potete più controllare l'errore== e serve una procedura alternativa.

> [!question] Da verificare: la trascrizione riporta "tre indici" e "il coefficiente di alpha, meno il coefficiente di sau"; letti "tre vincoli", "urban" e "south".

## Eteroschedasticità

- Si torna al modello di regressione per gestire l'ultimo problema rimasto.

### Perché l'omoschedasticità non è credibile

- Finora si ipotizzavano dati omoschedastici, ma già nell'esempio dei salari e del livello di istruzione la dispersione delle osservazioni cresce con l'istruzione, quindi non era credibile.
- L'omoschedasticità semplifica i risultati analitici; l'eteroschedasticità è solo una complicazione formale, con una soluzione semplice che funziona in entrambi i casi.
- L'omoschedasticità proprio non esiste e se esiste non siamo in grado di dimostrare che esista, quindi tanto vale ipotizzare sistematicamente l'eteroschedasticità.
- ==nel dubbio pensate sempre che il mondo sia eteroschedastico, funziona uguale, se avete un campione abbastanza grande==.

> [!question] Da verificare: la trascrizione riporta "l'espressione delle osservazioni tende a crescere"; probabilmente "la dispersione".

### Che cosa cambia senza omoschedasticità

- L'omoschedasticità serviva per i test e per lo standard error: la formula della varianza dello stimatore era calcolata ipotizzando omoschedasticità.
- Indipendentemente dall'ipotesi lo stimatore dei minimi quadrati è non distorto e, se $n$ è sufficientemente grande, converge al vero valore: non distorsione e consistenza restano.
- Esempio: prezzo di case negli Stati Uniti su `sqrft` (dimensione della casa), `lotsize` (dimensione del lotto), `bdrms` (numero di stanze) e la costante, stimato con omoschedasticità e con eteroschedasticità.

> [!question] Da verificare: la trascrizione riporta "sqft", "lot size", "vdrms"; si adottano "sqrft", "lotsize", "bdrms" come nella slide 6.

*(slide 10, mazzo sull'eteroschedasticità)*

- La prima colonna è OLS e identica nei due modelli; cambia la seconda, gli standard error, che servono per le statistiche t, gli intervalli di confidenza ed eventualmente la statistica F.
- Per `lotsize` con omoschedasticità la stima è 0,002, lo standard error 0,0006, la statistica t 3,22, il p-value 0,02%: si rifiuta la nulla, il coefficiente è diverso da zero.
- Con eteroschedasticità la t si riduce da 3,22 a 1,65 e il p-value è 10%: il coefficiente non è significativo, con la stessa stima ma una decisione completamente diversa.
- Il problema dell'eteroschedasticità non diagnosticata è che ==utilizzo una formula sbagliata per calcolare gli standard error e di conseguenza ho problemi a fare i test==.
- Il problema non è nella stima dei parametri, il bottone è sempre lo stesso, ma nel calcolo del denominatore della statistica t e della statistica F.

> [!question] Da verificare: la trascrizione riporta "il p-value è 0,02%"; la slide 10 riporta 0.002 (0,2%) e più avanti il docente dice "dallo 0,2%".

### Il teorema di Gauss-Markov

- Con errori omoschedastici lo stimatore dei minimi quadrati è il più efficiente, cioè ha gli standard error più piccoli; senza omoschedasticità non lo è più.
- Conta solo nei campioni finiti: asintoticamente gli standard error collassano a zero perché lo stimatore è consistente.

> [!question] Da verificare: la trascrizione riporta "delle mosche d'asticità"; si adotta "omoschedasticità" come nella slide 3.

*(slide 3)*

- La soluzione è ipotizzare sempre l'eteroschedasticità e stimare gli standard error con una formula corretta rispetto all'omoschedasticità: con un campione abbastanza grande la perdita di precisione non è rilevante.
- Non si è mai in grado di dire se c'è omoschedasticità: i test usati normalmente non sono abbastanza precisi.

### La varianza dello stimatore con errori omoschedastici ed eteroschedastici

- Nella regressione semplice (nella multipla funziona uguale, con algebra più difficile) lo stimatore è il vero $\beta$ più un termine, e questo vale sempre:

$$\hat\beta = \beta + \frac{\sum_{i=1}^n \epsilon_i (x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2}$$

*(slide 20)*

- Per la non distorsione si è usato solo il momento primo, ipotizzando la media di Y dato X uguale a zero; la varianza condizionale di Y serve per la varianza dello stimatore, ingrediente base dello standard error.

> [!question] Da verificare: la trascrizione riporta "la media di Y dato X è uguale a zero, cioè Y è incorrelato con X"; forse intende l'errore.

- Con le X costanti la varianza dello stimatore è:

$$\mathrm{Var}(\hat\beta \mid X) = \frac{\sum_{i=1}^n (x_i - \bar{x})^2 \, \mathrm{Var}(Y_i \mid X)}{\left[\sum_{i=1}^n (x_i - \bar{x})^2\right]^2}$$

- Con l'omoschedasticità la varianza condizionale è costante, uguale a $\sigma^2$, si porta fuori dalla sommatoria e la formula si semplifica.
- Con l'eteroschedasticità la varianza di $y$ dato $x$ cambia per ogni osservazione, per esempio chi ha studiato zero anni è concentrato intorno alla media e chi ne ha studiati 18 è dispersissimo; si scrive $\sigma_i^2$ con pedice $i$:

$$\mathrm{Var}(\hat\beta \mid X) = \frac{\sum_{i=1}^n (x_i - \bar{x})^2 \, \sigma_i^2}{\left[\sum_{i=1}^n (x_i - \bar{x})^2\right]^2}$$

- Questa formula non è comprimibile, perché $\sigma$ non si separa più dalla sommatoria delle $x$ al numeratore: sotto eteroschedasticità non si può usare la formula originale, e sono diverse.

*(slide 21)*

- Se nei dati i $\sigma_i$ sono più o meno tutti uguali, per esempio 0,75, il software semplifica implicitamente e ci si riconduce alla formula precedente, anche se analiticamente non si può fare a priori.
- Nell'output con due tabelle, la prima ha gli standard error con la formula omoschedastica, la seconda con una formula più simile a quella eteroschedastica.

> [!question] Da verificare: la trascrizione riporta "sotto omoschedasticità e sopra eteroschedasticità"; nella slide 10 il modello con errori standard normali sta sopra e quello corretto sotto.

### Come calcolare lo standard error con errori eteroschedastici

- Con eteroschedasticità i $\sigma_i$ sono tutti diversi e non noti, quindi non si sa dove piazzarli nella formula dello standard error.
- Con omoschedasticità $\sigma^2$ si stima con 1 fratto $n-1$ della somma dei residui al quadrato, nella regressione semplice, uno stimatore non distorto; nella multipla la filosofia è la stessa.

> [!question] Da verificare: la trascrizione riporta "1 fratto n meno 1"; il fattore non è confermato dalle slide.

- Con eteroschedasticità non si può usare la media dei residui al quadrato, perché ogni residuo è coerente con una varianza diversa.
- Bisogna sostituire $\sigma_i^2$ con qualcosa di calcolabile; la soluzione è carina in teoria, ma non servirà.

### Il residuo come approssimazione dell'errore

- Le $X$ sono il dataset, $\sigma_i^2$ non è noto: si vuole uno stimatore della varianza consistente, che converga alla vera varianza.

> [!question] Da verificare: la trascrizione riporta "come calcolare il piicamente con la formula"; nel testo "la varianza".

- Con esogeneità, il residuo è $y_i$ meno $y_i$ stimato, cioè $\alpha + \beta x_i + \epsilon_i$ meno la previsione $\hat\alpha + \hat\beta x_i$:

$$\hat\epsilon_i = y_i - \hat{y}_i = \alpha + \beta x_i + \epsilon_i - (\hat\alpha + \hat\beta x_i)$$

- Raccogliendo le $x_i$ si ottiene:

$$\hat\epsilon_i = (\alpha - \hat\alpha) + (\beta - \hat\beta)\, x_i + \epsilon_i$$

> [!question] Da verificare: la trascrizione riporta "raccolgo i c i" e "il residuo, y i del mio modello", resi con "le $x_i$" e "il residuo $i$-esimo".

*(slide 22)*

- Con esogeneità, per $n$ sufficientemente grande lo stimatore collassa sul vero valore, la distanza tra $\beta$ e il suo stimatore e tra $\alpha$ e il suo stimatore va a zero se $n$ tende a infinito, questa è la consistenza: il residuo è una buona approssimazione del termine d'errore.
- Il termine d'errore è la distanza tra la retta nella popolazione e ogni osservazione, il residuo quella tra la retta stimata col campione e l'osservazione; con $n$ che tende a infinito le due rette convergono e le distanze coincidono.
- È un risultato asintotico, il doppio simbolo vuol dire più o meno uguali.

> [!question] Da verificare: la trascrizione riporta "Che sigma è sufficientemente grande" e "sene"; si adotta "n" come nella slide 22.

- Se $x$ e $y$ sono simili lo sono anche $x^2$ e $y^2$, e moltiplicando per la stessa costante resta la più o meno uguaglianza: vale per ogni individuo, quindi anche per la media, per $n$ grande:

$$\frac{1}{n}\sum_{i=1}^n \hat\epsilon_i^2 (x_i - \bar{x})^2 \approx \frac{1}{n}\sum_{i=1}^n \epsilon_i^2 (x_i - \bar{x})^2$$

> [!question] Da verificare: la trascrizione riporta "Se y sono uguali a zero sono simili" e "per sigma meno xi alla seconda"; si adottano "$x$ e $y$ sono simili" e $(x_i - \bar{x})^2$ come nella slide 23.

*(slide 23)*

- La media a sinistra si calcola perché i residui si calcolano; quella a destra no, perché $\epsilon$ è una variabile casuale non nota: per $n$ grande sono simili, primo pezzo della dimostrazione.
- Lo scopo è la sommatoria di $\sigma_i^2$ per $(x_i - \bar{x})^2$, ma le due medie hanno $\epsilon^2$ e il residuo al quadrato, non $\sigma_i^2$: serve un passaggio aggiuntivo.
- Si definisce $z$, il residuo al quadrato per gli scarti al quadrato delle $x$, calcolabile, e per l'ipotesi di eteroschedasticità si conosce la sua media condizionata a $x$.

> [!question] Da verificare: la trascrizione riporta "la sommatoria di sigma i quadro per x i meno y assegnato alla seconda"; si adotta $(x_i - \bar{x})^2$ come nella slide 21.

### Dalla legge dei grandi numeri allo stimatore di White

- Gli $z$ non sono indipendenti perché funzioni di $x$, ma non si sa se sono identicamente distribuiti, perché ogni $z$ potrebbe avere una varianza diversa; hanno però tutti la stessa media, perché a $z$ si toglie la sua media condizionale, sempre zero.

> [!question] Da verificare: la trascrizione riporta "gli z non sono indipendenti"; il "ma" che segue fa pensare a "sono indipendenti".

- Una legge dei grandi numeri dice che per osservazioni indipendenti con la stessa media, anche non identicamente distribuite, la sommatoria converge alla media comune, qui zero: $z$ meno la sua media condizionale converge a zero, per una legge diversa da quella vista finora.
- Esplicitamente:

$$z_i - E[z_i \mid X] = \left(\epsilon_i^2 - \sigma_i^2\right)(x_i - \bar{x})^2$$

- Gli elementi della sommatoria convergono a zero per $n$ grande, quindi la media degli $\epsilon_i^2$ è più o meno uguale alla media dei $\sigma_i^2$ pesati per $(x_i - \bar{x})^2$.

> [!question] Da verificare: la trascrizione riporta "se paro gli elementi dentro quella sommatoria, che questa, non è questo"; nel testo "gli elementi dentro quella sommatoria".

- Già dimostrato che la media dei residui al quadrato per le $x$ è più o meno uguale alla media degli $\epsilon_i^2$ per le $x$, e ora che questa è asintoticamente equivalente alla media dei $\sigma^2$; per la proprietà transitiva, per $n$ grande la media dei residui al quadrato pesata è uguale alla media dei $\sigma_i^2$, il numeratore della varianza dello stimatore dei minimi quadrati con eteroschedasticità: al posto di $\sigma_i^2$ si può mettere il residuo al quadrato, tutto il resto rimane uguale.
- La consistenza dei coefficienti dà la prima approssimazione, la legge dei grandi numeri la seconda; si calcola la formula con il residuo al quadrato, non quella con $\sigma_i^2$.
- Si ottiene uno stimatore della varianza di $\beta$ con il residuo al quadrato al posto di $\sigma^2$: la formula di White, Huber-White per l'eteroschedasticità.

### Lo stimatore robusto all'eteroschedasticità

- Non si è fatta l'ipotesi di omoschedasticità o eteroschedasticità, solo di esogeneità: serviva solo che gli stimatori di $\alpha$ e $\beta$ fossero consistenti, quindi per $n$ grande la formula funziona in entrambi i casi.
- Se i residui al quadrato sono più o meno uguali si semplifica, se sono diversi c'è eteroschedasticità ma lo stimatore funziona lo stesso: si chiama stimatore robusto per l'eteroschedasticità, uno stimatore consistente degli standard error, e per $n$ sufficientemente grande il denominatore della statistica t è corretto.
- La formula per l'omoschedasticità funziona solo con omoschedasticità: nell'esempio il p-value passa dallo 0,2% al 10 e qualcosa per cento e cambia la decisione; non è grave se passa dall'1 al 3%, lo è se cambia di 10 punti percentuali.
- ==siccome per calcolare questa formula non ho fatto ipotesi sull'eteroschedasticità o sull'omoschedasticità, questa vale sempre==, si chiama stimatore robusto, e si può sempre utilizzare.
- ==Se non sapete decidere tra omoschedasticità ed eteroschedasticità, allora tanto vale usare quella formula per calcolare gli standard error==, perché vale sempre, se $n$ è sufficientemente grande, con uno stimatore consistente.
- Potrebbe essere un po' più precisa rispetto all'altra se i dati sono omoschedastici, ma non si sa mai se lo sono, perché i test per validare l'omoschedasticità contro l'eteroschedasticità sono locali; la prossima volta si vedranno i test, non conclusivi.

> [!question] Da verificare: "Potrebbe essere un po' più precisa rispetto all'altra": il soggetto non è chiaro e la slide 28 dice che in caso di omoschedasticità gli errori standard robusti sono inefficienti.

> [!question] Da verificare: la trascrizione riporta "sono locali"; il termine non è confermato dalle slide.
