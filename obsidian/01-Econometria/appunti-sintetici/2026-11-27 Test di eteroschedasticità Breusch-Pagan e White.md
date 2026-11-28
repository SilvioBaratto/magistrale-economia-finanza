---
corso: Econometria
data: 2026-11-27
fonte: Audio/econometria/econometria_2026-11-27.txt
tipo: appunti-sintetici
tags: [appunti-sintetici, econometria]
revisione: sintesi a punti degli appunti della stessa lezione
---

# Test di eteroschedasticità: Breusch-Pagan e White

## Gli esercizi di oggi

- Il docente fa esercizi che sono vecchi esami messi a disposizione, nella parte uno e due.

> [!tip] Esame
> Non ci sono le soluzioni online, così più o meno dovreste capire che tipo di risposta mi aspetto alle domande.

## Ripasso degli standard error robusti

- Ieri si è costruito lo standard error dei coefficienti insensibile all'ipotesi sulla varianza condizionata, quindi non serve più pensare a omoschedasticità o eteroschedasticità.
- È sempre conveniente usare la formula robusta (nel modello multiplo è quella dei lucidi) anziché quella che elimina il quadrato.
- Basta che gli stimatori di alfa e beta siano consistenti, cioè che valga l'esogenità, per n sufficientemente grande.
- In Gretl si spunta standard error robusti nella finestra del modello. ==Il mio consiglio: usateli sempre.==
- La statistica t ha il solito numeratore e al denominatore lo standard error robusto anziché lo standard error incerto.

> [!question] Da verificare: "standard error incerto"; probabilmente "naïve" (slide 10), ma non confermato.

- Anche il test F è costruito in automatico in versione coerente con gli standard error robusti.

> [!question] Da verificare: "in cavo"; probabilmente "in capo".

- Con standard error robusti t e F sono robuste in qualsiasi software di benchmarking e il problema non c'è più.

> [!question] Da verificare: "software di benchmarking"; il termine non è chiaro.

## A che cosa servono i test di eteroschedasticità

- Servono a validare l'ipotesi di eteroschedasticità, ma operativamente non serve sapere se è più probabile l'omoschedasticità o l'eteroschedasticità, perché l'omoschedasticità non è dimostrabile sulla base di test standard.
- Dicono come sono fatti i dati e perché la varianza cambia con x, per specificare meglio il modello.

## Un esempio: prezzi delle case e dimensione

- Si guarda se i prezzi delle case dipendono dalla dimensione e come cambia il residuo: piccolo per le case piccole, grande per le grandi.
- Le case piccole hanno più o meno lo stesso prezzo; le case grandi variano per molte altre caratteristiche, anche per le zone più pregiate.

> [!question] Da verificare: "la finestra migliore"; il termine non è chiaro.

- Con un beta positivo atteso, le caratteristiche omesse potrebbero dare endogeneità o spiegare la dispersione dei dati.

> [!question] Da verificare: "è contrario a quello che ho fatto"; il senso non è chiaro.

- È come l'esempio del reddito, il livello di istruzione, sul salario: con basso education i salari sono uguali, con alto livello di istruzione molto dispersi.
- Questa dispersione è eteroschedasticità e può indicare variabili mancanti; il problema statistico degli standard error è risolto a prescindere se il modello è ben specificato.

> [!question] Da verificare: "detto che comunque"; probabilmente "dato che comunque".

- Si approssima la varianza condizionale (il sigma quadro U) con un residuo al quadrato e si fa una regressione ausiliaria su x.
- Se b è positivo, con la dimensione aumenta l'eterogeneità delle case; se b è uguale a zero, la varianza condizionale approssimata non dipende dalla dimensione.
- I test non servono a capire se si è in un contesto omoschedastico o eteroschedastico, già risolto con gli standard error robusti, ma a capire quali variabili incidono sulla varianza condizionale, per interesse economico più che statistico.

> [!question] Da verificare: "questa roba qua mi serve per capire se sono in un contesto o nell'altro"; sembra mancare un "non".

## Il test di Breusch-Pagan

- Dato un modello di regressione multipla, si chiede se la varianza condizionale dipende dalle x, potenzialmente tutti i fattori inclusi.

### Una regressione sulla varianza condizionale

- La varianza condizionale è potenzialmente un modello di regressione, una combinazione lineare di variabili.

*(slide 29)*

- In pratica non è stimabile: la varianza condizionale non si osserva, manca la Y a sinistra dell'uguale e in Gretl non ci sono numeri.
- La risposta di uno studente ("Non siamo certi se le variabili X sono condizionate...") può essere, dice il docente, ma il problema è più pratico.

> [!question] Da verificare: "Non siamo certi se le variabili X sono condizionate..."; l'attribuzione a uno studente è dedotta.

> [!question] Da verificare: "Il problema che starò io non osservo"; "starò" non è chiaro.

### Che cosa dice l'ipotesi nulla

- Se tutti i coefficienti da $\delta_1$ a $\delta_k$ sono nulli ($\delta_0$ no, perché serve), la varianza condizionale non dipende dalla x ed è una costante che coincide con questo parametrino; se almeno uno è diverso da zero, c'è eteroschedasticità.

> [!question] Da verificare: "pensate alla ... di esclusione"; probabilmente "restrizione".

- È un'ipotesi molto restrittiva, perché non si sa come è fatta la varianza condizionale; vale l'omoschedasticità se e solo se tutti i coefficienti da $\delta_1$ a $\delta_k$ sono identicamente nulli.
- Si fa un test tipo F ponendo a zero tutti i coefficienti da 1 a k.

*(slide 30)*

### Non rifiutare l'ipotesi nulla

- Domanda al pubblico: non rifiutando che $\delta_1$ e $\delta_k$ sono tutti uguali a zero, si è nell'ambito dell'omoschedasticità?
- Il test è eteroschedasticità di un tipo specifico contro non quel tipo, non omoschedasticità contro eteroschedasticità: ==non rifiutare nulla, non vuol dire omoschedasticità==.
- I software dicono H0 omoschedasticità, H1 eteroschedasticità, ma H0 è: non c'è questa forma di eteroschedasticità.
- Il test serve a capire se i coefficienti sono positivi o negativi e come varia la varianza condizionale con x, per costruire un modello migliore e ridurre il problema delle variabili mancanti.

### Come stimare la regressione sulla varianza

- La variabile dipendente non c'è, ma su un campione sufficientemente grande l'errore al quadrato è approssimabile dal residuo al quadrato, che approssima anche $\sigma_i^2$, la varianza condizionale al quadrato.
- Si stima la regressione con il residuo alla seconda, quello con il cappellino, al posto di $\epsilon^2$, e si fa un test tipo F.
- Se si rifiuta la nulla, almeno quella forma di eteroschedasticità c'è; se non si rifiuta, non si può dire che c'è omoschedasticità, solo che non c'è l'eteroschedasticità del tipo di Breusch-Pagan.
- ==a me non interessa sapere se c'è omoschedasticità, perché non lo saprò mai==; interessa sapere perché c'è eteroschedasticità.

### Il test di Breusch-Pagan in Gretl

- In Gretl, dopo la regressione: menu test, sottomenu test di eteroschedasticità (LM test), Breusch-Pagan; LM sta per moltiplicatore di Lagrange, la tecnica usata per calcolarlo.
- Il software mostra anche le stime dei parametri, forse la parte più interessante.

> [!question] Da verificare: "Scegliete Browse, paga"; la slide 32 riporta "Breush-Pagan" e si adotta "Breusch-Pagan".

- Nell'esempio la statistica test è 30, è tipo una statistica F, con p-value circa zero: test tipo F unilaterale a destra, si rifiuta la nulla e si esclude l'omoschedasticità.
- È almeno un controesempio che diagnostica eteroschedasticità, quindi l'omoschedasticità è impossibile, più o meno.

*(slide 32)*

> [!question] Da verificare: "un'illaterale a destra"; probabilmente "unilaterale a destra"; il docente dice "tipo F", la slide 32 riporta una statistica LM con P(Chi-quadro(3) > 30,0227), e si riporta ciò che ha detto il docente.

## Il test di White

- Il modello di Breusch-Pagan è forse troppo semplice: la varianza potrebbe dipendere dal quadrato delle x, dalla varianza della x (più la x è variabile, più la y è variabile) e dai prodotti incrociati, il prodotto tra x e y.

> [!question] Da verificare: "La varianza a un momento secondo"; probabilmente "la varianza è un momento secondo".

> [!question] Da verificare: "il prodotto tra x e y"; probabilmente il prodotto tra due regressori, ma non è certo.

### L'intuizione sulla varianza di una combinazione lineare

- Con $y = \alpha + \beta_1 x_1 + \beta_2 x_2 + \epsilon$, la varianza di y dato x è la varianza di $\alpha + \beta_1 x_1 + \beta_2 x_2$ più qualcos'altro, supposto irrilevante.
- Dà $\beta_1^2$ per la varianza di $x_1$, più $\beta_2^2$ per la varianza di $x_2$, più $\beta_1$ per $\beta_2$ due volte la covarianza tra $x_1$ e $x_2$.

> [!question] Da verificare: "supponiamo che la y non sia così importante"; probabilmente il termine d'errore, ma non è certo.

- Le varianze fanno riferimento ai quadrati di $x_1$ e $x_2$ e la covarianza al prodotto incrociato, quindi nella regressione ausiliaria hanno senso le variabili al quadrato e il prodotto incrociato.

### La regressione ausiliaria di White

- White aggiunge a Breusch-Pagan tutte le variabili al quadrato più tutti i prodotti incrociati possibili: un modello molto più generale, che dovrebbe descrivere tutte le forme di eteroschedasticità in un modello lineare.

*(slide 33)*

- Il test è sempre lo stesso: se tutti i coefficienti sono congiuntamente nulli è più probabile l'omoschedasticità; se almeno uno è diverso da zero c'è eteroschedasticità.
- I momenti di ordine superiore, x alla terza e x alla quarta, non servono perché le varianze sono momenti secondi.

### Il problema dei troppi regressori

- Con tre regressori va bene; con dieci regressori, dieci più dieci più tutti i prodotti incrociati, si arriva a quaranta, cinquanta regressori.
- Con troppi regressori, quasi tutti nulli, il test è estremamente impreciso: non per l'errore del primo tipo, che è sempre l'alfa percento, ma per la potenza.

> [!question] Da verificare: "costruisco un sacco di regressioni, la maggior parte dei quali non spiega nulla"; probabilmente "regressori".

- Dell'errore del secondo tipo il docente dice "non rifiuto la nulla quando l'alternativa è vera, scusate, sono sempre un po' confuso"; qui è molto grande e si rischia di non rifiutare la nulla troppo spesso.
- Dei due test, uno è conservativo e senza problemi di potenza ma potrebbe non descrivere la varianza condizionale perché ha troppi pochi regressori; White è metodologicamente più corretto ma impreciso; guardandoli insieme ci si può fare un'idea precisa.
- ==a me non interessa neanche tanto sapere se vale più l'omoschedasticità contro l'eteroschedasticità, ma sapere eventualmente perché c'è eteroschedasticità==, perché aiuta a specificare il modello sulla media condizionale.

### Il test di White in Gretl

- Il test di White è in linea di massima di tipo F con restrizioni lineari, dal menu test della regressione; nell'esempio il p-value è circa zero, quindi si conferma l'eteroschedasticità.

*(slide 35)*

## Che cosa si può dire dopo i test

- Se almeno uno dei test conferma l'eteroschedasticità, almeno quella forma di eteroschedasticità c'è.

> [!question] Da verificare: "vuol dire che siamo in un contesto omoschedastico, eteroschedastico"; la frase è incoerente e il senso non è determinabile.

- Se tutti i test non rifiutano la nulla, con Breusch-Pagan con p-value grande, 25%, e White con p-value grande, non si è nell'ambito dell'omoschedasticità.
- Breusch-Pagan potrebbe non descrivere la varianza condizionale: se dipende da $x^2$ e non da $x$, non ha $x^2$ nel modello e non dirà contagio.

> [!question] Da verificare: "non dirà contagio"; il termine non è chiaro.

- White ha le variabili al quadrato, ma con troppi regressori è scarso sull'errore del secondo tipo, quindi non è troppo preciso.

> [!question] Da verificare: "se avete il modello sufficientemente ragionevole per descrivere i dati, non funziona tanto bene" e "a livello grande"; frasi non chiare, lasciate come dette.

- ==Voi quando fate un test non accettate mai l'ipotesi nulla, la rifiutate o non la rifiutate.==
- Non si può accettare l'omoschedasticità: i dati sono abbastanza coerenti o non abbastanza coerenti con essa, senza risposta definitiva, perché non si sa qual è il vero modello della varianza condizionale.
- Con p-value grande potrebbe esserci un'altra forma plausibile di eteroschedasticità, oppure il test non è abbastanza preciso; sotto la nulla il software dice che quel tipo di eteroschedasticità non è presente, non l'omoschedasticità in generale.

## Come usare davvero i test di eteroschedasticità

- Usare sempre gli standard error robusti, sperando che il campione sia abbastanza grande; con pochi dati i risultati sono comunque imprecisi.
- I test servono a capire perché c'è eteroschedasticità per costruire un modello migliore, niente di più; mai a decidere tra omoschedasticità ed eteroschedasticità, perché non sono abbastanza precisi.
- Servirebbero infiniti test con tutte le forme di eteroschedasticità, ma è impossibile perché si dovrebbero ottimare infiniti modelli.

> [!question] Da verificare: "dovrei ottimare infiniti modelli"; probabilmente "stimare".

- L'utilità è storica e metodologica (dimostrare le proprietà dei test è interessante come meccanismo scientifico, tra virgolette); soprattutto serve a capire come la varianza dipende dai regressori.
- Nella vita reale si usano sempre gli standard error robusti; tutto il resto è ausiliario.

## Gli esercizi di riepilogo

- Si passa a esercizi di riepilogo su compiti vecchi.

> [!tip] Esame
> Compito del 2023: un esercizio dà l'output di una regressione e chiede di ottenere dei risultati, e cambia pochissimo da un compito all'altro.

### L'appello del 2023: i dati e il modello

- Il docente ha la soluzione per avere i numeri; appello di giugno 2023.

> [!question] Da verificare: "Giugno 2013"; il testo dell'appello riporta 15 giugno 2023 (e il docente ha detto "2023" poco prima) e si adotta "giugno 2023".

- La regressione descrive i prezzi delle case in una zona degli Stati Uniti, in scala logaritmica, in funzione di NOX (fattore inquinante, qualità dell'aria, in scala logaritmica), del tasso di criminalità (indice: più è grande, peggio è), del numero di stanze e del numero di stanze al quadrato.
- ddist è la dummy uguale a uno se la casa è lontana dai centri di interesse e zero altrimenti: zero è una zona comoda e uno è una zona scomoda.

> [!question] Da verificare: "DIST"; il testo dell'appello del 15/06/2023 riporta `ddist` (dummy uguale a 1 se il distretto è lontano dai centri lavorativi principali) e si adotta questa forma.

- È inclusa una variabile prodotto incrociato tra una variabile dummy e il fattore inquinante, riscalato rispetto a uno per evitare qualche problema di collinearità, come visto a lezione con Antonio; il docente richiama il genre per il livello di istruzione, che non funzionava, e si sceglieva la media.

> [!question] Da verificare: "il genre per il livello di istruzione" e "qualche linearità"; probabilmente "gender" e "collinearità", ma non confermati.
