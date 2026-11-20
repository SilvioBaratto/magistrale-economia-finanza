---
corso: Econometria
data: 2026-11-20
fonte: Materiali/audio/econometria/econometria_2026-11-20.txt
tipo: appunti-lezione
tags: [appunti, econometria]
revisione: trascrizione gpt-transcribe riscritta in stile accademico (humanizer)
integrato: 2026-11-20
---

# Collinearità, quasi collinearità e test su più parametri

## Collinearità perfetta con le variabili dummy

Nel modello di regressione multipla si ha collinearità perfetta quando due o più regressori sono correlati in modo esatto, cioè quando uno si può prevedere esattamente conoscendo l'altro. L'esempio visto il giorno precedente introduce due variabili qualitative, dette variabili dummy o variabili categoriali, che di solito identificano l'appartenenza a una categoria: genere maschile e genere femminile. Chi è di genere maschile non è di genere femminile, e viceversa. Ci si chiede che cosa succede se si inseriscono nel modello entrambe le variabili.

Il modello di partenza ha quattro parametri. Esiste una parametrizzazione del tutto equivalente con tre parametri. Rispetto a quella originale, l'intercetta del modello a tre parametri è una combinazione di due parametri, l'intercetta originale e il coefficiente della variabile $M$, cioè $\alpha + \beta_2$. Il coefficiente della variabile $F$ è una combinazione lineare degli altri, $\beta_3 - \beta_2$. Il coefficiente $\beta_1$ del livello di istruzione resta invariato.

Dal punto di vista operativo si consideri un software che stima il modello. Al software non interessa che cosa siano la costante o il coefficiente angolare della variabile $F$: riceve in input alcune variabili, più la costante, e restituisce una stima per ciascun coefficiente. Con il modello a tre parametri le stime sono tre numeri.

> [!question] Da verificare: a proposito della costante, la trascrizione riporta "che mi serve per recuperare l'informazione sul parametro verità certa"; il passaggio non è leggibile.

Poiché i due modelli sono equivalenti, si vorrebbe poter passare dalle stime dei tre coefficienti a quelle dei quattro coefficienti $\alpha, \beta_1, \beta_2, \beta_3$. Il sistema che lo permetterebbe ha quattro incognite e tre equazioni, quindi ha infinite soluzioni. Il software non sa quale scegliere e non si può più passare da un modello all'altro, anche se i modelli sono identici.

La causa sostanziale è che l'aggiunta di $F$ o di $M$ (una vale l'altra, perché sono intercambiabili) introduce un parametro in più senza dare al modello alcuna informazione nuova: conoscendo $F$ si ottiene automaticamente $M$, e viceversa. Sono dati finti, e le informazioni non bastano per identificare tutti i coefficienti.

La collinearità è però un problema logico più che matematico, come già detto il giorno precedente. L'effetto marginale è l'impatto di una variazione di $x_1$ tenendo fisse $x_2, x_3, x_4$ e tutte le altre variabili. Se due variabili sono perfettamente correlate non è possibile modificarne una lasciando ferma l'altra, perché si muovono contemporaneamente e senza incertezza.

### Eliminare uno dei due coefficienti

Per risolvere il problema logico basta osservare che una delle due variabili è in più e non serve. Operativamente significa che uno tra $\beta_2$ e $\beta_3$ si può eliminare, cioè fissare a zero. Il sistema ha infinite soluzioni: se si fissa uno dei quattro parametri, gli altri si ottengono di conseguenza e la soluzione è unica. Non si può fissare $\beta_1$, che serve e non è coinvolto nella relazione esatta; si fissa quindi $\beta_2$ o $\beta_3$, e il valore più semplice è zero. Qualsiasi software lo fa in automatico, tranne R, che secondo il docente non lo fa.

> [!question] Da verificare: la differenza di comportamento attribuita a R rispetto agli altri software è riportata come detta in aula; va confrontata con il software usato.

Eliminare un regressore dal modello non significa eliminare quella categoria di persone dal database: si elimina soltanto il parametro che la rappresenta, e il gruppo resta rappresentato in modo diverso. Per vederlo si riprende il modello dei salari

$$
\text{wage} = \alpha + \beta_1\,\text{education} + \beta_2 M + \beta_3 F + \varepsilon
$$

con $M$ e $F$ definite come il giorno precedente (1 e 0, oppure 0 e 1, a seconda del genere). Si pone $\beta_2 = 0$, e il modello diventa

$$
\text{wage} = \alpha + \beta_1\,\text{education} + \beta_3 F + \varepsilon .
$$

### Interpretazione dei parametri nel modello ristretto

Il modello descrive il salario atteso per persone con certe caratteristiche. Si considerino le lavoratrici, per cui $F = 1$, con un livello di istruzione fissato a un valore generico. La regressione per questo gruppo è

$$
\alpha + \beta_1\,\text{education} + \beta_3 \cdot 1 ,
$$

assumendo che la media dell'errore condizionata ai regressori sia nulla.

> [!question] Da verificare: la trascrizione riporta "assumo che la media di y dato x, cioè la covarianza tra y e x, è uguale a zero"; con ogni probabilità si riferisce all'errore ($E[\varepsilon \mid x] = 0$) e non a $y$.

L'intercetta è $\alpha + \beta_3$, cioè la combinazione dei parametri che non moltiplicano alcun regressore, mentre il coefficiente angolare è $\beta_1$, che moltiplica il livello di istruzione. Questa è la retta di regressione per le donne.

Il salario atteso per gli uomini si calcola anche se la variabile $M$ non compare nel modello. Se $M = 1$ allora $F = 0$, quindi basta calcolare la regressione con $F = 0$ e un livello di istruzione qualsiasi. Si ottiene

$$
\alpha + \beta_1\,\text{education} + \beta_3 \cdot 0 = \alpha + \beta_1\,\text{education},
$$

perché il termine in $\beta_3$ sparisce. Si hanno così due diversi valori attesi condizionali, uno per ciascun genere.

Nel grafico con il livello di istruzione in ascissa e il salario in ordinata, la retta per il gruppo $M$ ha pendenza $\beta_1$, che ci si attende positiva, e intercetta $\alpha$. Questo parametro si può stimare, perché ora il sistema ha tre equazioni e tre incognite.

Per le donne il coefficiente angolare è ancora $\beta_1$, mentre cambia l'intercetta, che è $\alpha + \beta_3$. Il parametro $\beta_3$ può essere positivo o negativo. Nelle analisi empiriche che si vedranno con il professor Peruzzi risulta tipicamente negativo e, purtroppo, piuttosto grande: la retta di regressione delle donne sta quindi un po' sotto quella degli uomini, con la stessa pendenza $\beta_1$.

Questo modello rappresenta entrambi i generi e permette anche di confrontarli. Le due rette sono parallele, quindi il differenziale tra i gruppi è la distanza tra le intercette e non dipende dal livello di istruzione: il gap tra genere maschile e genere femminile è $\beta_3$. Se $\beta_3$ fosse di 5 dollari all'ora, a qualsiasi livello di istruzione le donne guadagnerebbero 5 dollari in meno degli uomini; se fosse 0,5, la differenza sarebbe di 50 centesimi.

Il problema della collinearità è dunque apparente. Si risolve a monte, oppure lo si lascia risolvere al software in modo standard, ma il modello va poi interpretato di conseguenza. La variabile omessa per risolvere il problema individua il gruppo di riferimento, e il coefficiente dell'altra variabile di genere ($\beta_3$) misura la deviazione dell'altro gruppo rispetto a quello di riferimento.

### La scelta del gruppo di riferimento è arbitraria

La soluzione del problema della collinearità non è unica. Nel caso svolto è stata tolta la variabile $M$, ma si sarebbe potuta togliere $F$. I dati identificano comunque le stesse due intercette, una per il genere maschile e una per il genere femminile; cambia soltanto il modo di esprimere questi due punti in funzione dei parametri. Se si toglie $F$ anziché $M$, l'intercetta del modello stimato identifica il punto del genere femminile, mentre il punto del genere maschile è dato da $\alpha$ più il coefficiente della variabile $M$.

Nell'output l'unica differenza è il segno del coefficiente di genere: se nel primo modello è negativo, nel secondo è positivo con lo stesso valore. Se fosse $-0{,}3$ nel primo, sarebbe $+0{,}3$ nel secondo. Il coefficiente di education resta uguale, così come l'$R^2$, gli standard error e ogni altra statistica descrittiva. La scelta è quindi arbitraria.

Alla domanda se esiste una differenza di salario tra genere maschile e genere femminile, in un modello di questo tipo si risponde verificando se il coefficiente $\beta_3$ è uguale a zero o diverso da zero, cioè con un test di significatività. Se la domanda fosse se la differenza di genere implica una variazione di salario del 30%, si verificherebbe se quel coefficiente corrisponde al 30% oppure è diverso. Qualsiasi batteria di test si può eseguire in modo abbastanza standard.

### Mantenere entrambe le variabili e togliere la costante

Un altro modo di risolvere la collinearità è mantenere sia $M$ sia $F$ e togliere un'altra cosa, in modo che il modello resti stimabile senza problemi numerici, cioè senza sistemi che il computer non può risolvere. Il docente chiede se qualcuno abbia un'idea e se le variabili dummy siano già state viste nei corsi precedenti; gli studenti rispondono che forse sì. Si passa quindi a rivedere la casistica.

La relazione lineare esatta tra le due variabili è $M + F = 1$, equivalente a $M = 1 - F$ e a $F = 1 - M$. Oltre ai regressori $M$ e $F$ interviene quindi un terzo regressore, la costante 1. Anche la costante è un regressore: per stimare il parametro $\alpha$ serve un regressore associato, e poiché $\alpha \cdot x = \alpha$ questo regressore è $x = 1$. È il regressore speciale che permette di ottenere l'informazione sulla costante del modello. La relazione di collinearità coinvolge perciò $M$, $F$ e il regressore associato ad $\alpha$.

Togliere $\alpha$ risolve il problema. Nel primo esercizio era stata tolta $M$ e restavano le altre due variabili; nel secondo, descritto solo a voce, era stata tolta $F$; togliendo la costante si possono mantenere $M$ e $F$. Il modello diventa

$$
\text{wage} = \beta_1\,\text{education} + \beta_2 M + \beta_3 F + \varepsilon .
$$

Per un lavoratore di genere maschile ($M = 1$, quindi $F = 0$) il salario atteso è $\beta_2 + \beta_1\,\text{education}$, perché il termine in $F$ sparisce. Per il genere femminile, calcolando il valore atteso di wage dato $F = 1$, si ottiene $\beta_3 + \beta_1\,\text{education}$. Si hanno così due rette di regressione.

Stimando questo modello dopo i due precedenti si osserva che la stima di $\beta_2$ coincide con l'intercetta del gruppo $M$ calcolata prima, cioè con $\alpha$ del primo modello, e la stima di $\beta_3$ coincide con l'intercetta del genere femminile calcolata prima. Numericamente, qualunque sia la variabile tolta, i dati identificano gli stessi due punti; cambia soltanto il nome dei parametri con cui li si indica. Nel modello senza $M$ i due punti sono $\alpha$ e $\alpha + \beta_3$ di quel modello; nell'ultimo modello sono $\beta_2$ e $\beta_3$ dell'ultimo modello. Il differenziale è sempre lo stesso numero. Questi casi si vedranno meglio durante le esercitazioni.

Indipendentemente da come si risolve la collinearità, i risultati sono equivalenti: cambia soltanto l'interpretazione dei differenziali. Uno dei problemi principali dell'ultima parametrizzazione riguarda il test sulla differenza sostanziale tra genere maschile e genere femminile: non basta un test sul parametro che descrive il differenziale.

Per verificare se i due gruppi hanno lo stesso livello di salario occorre testare l'uguaglianza dei due parametri, cioè $\beta_2 - \beta_3 = 0$.

> [!question] Da verificare: la trascrizione riporta "beta 1 è uguale a beta 2"; nel modello senza costante i due parametri dei gruppi sono $\beta_2$ e $\beta_3$, e il docente stesso li cita più avanti.

Il test non è del tutto banale, perché non coinvolge un solo parametro ma una combinazione lineare di parametri. Si può comunque calcolare una statistica $t$ su questa combinazione. Si può dimostrare, e il risultato sarà discusso meglio più avanti, che lo stimatore di ciascun parametro si distribuisce asintoticamente come una normale. La differenza di due stimatori normali è normale, quindi per campioni grandi $\hat\beta_2 - \hat\beta_3$ è ben approssimata da una normale, la cui media sotto l'ipotesi nulla è zero.

Per la statistica $t$ serve la varianza di questa differenza, che è

$$
\operatorname{Var}(\hat\beta_2) + \operatorname{Var}(\hat\beta_3) - 2\operatorname{Cov}(\hat\beta_2, \hat\beta_3).
$$

La covarianza non compare nella tabella di output del modello di regressione. Il software la calcola, ma bisogna andarla a cercare, ed è una seccatura. Essendo la distribuzione normale, il test si può fare, ma è più laborioso del test sull'uguaglianza a zero di $\beta_2$ o $\beta_3$, che è standard e non richiede alcun ragionamento. Questa parametrizzazione ha però un vantaggio intuitivo: i due parametri rappresentano già le intercette dei due gruppi, quindi numericamente non servono trasformazioni. Il docente presenta tutte le alternative e lascia la scelta agli studenti.

La covarianza tra gli stimatori si può recuperare da una parte particolare dell'output di Gretl, come si vedrà nelle esercitazioni. Se la combinazione lineare coinvolgesse cinque parametri, servirebbero tutte le covarianze possibili tra gli stimatori e i calcoli diventerebbero complicati. Il docente osserva che in quel caso sbaglierebbe e ne sconsiglia l'uso.

La collinearità perfetta si risolve dunque eliminando la variabile ridondante.

> [!tip] Esame
> Variabili di questo tipo capitano spesso, e il docente chiederà spesso di stabilire se si appartiene a un gruppo o a un altro, cioè se c'è una differenza oppure no. Non conviene imparare a memoria le formule scritte alla lavagna: conviene dedicare 30 secondi del tempo d'esame a rifare i passaggi. Il valore atteso condizionato con la dummy uguale a 1 è una certa espressione, con la dummy uguale a 0 un'altra; facendo le differenze si ottengono le formule necessarie per costruire i test. Le formule dipendono dalla parametrizzazione usata alla lavagna, e all'esame il docente potrebbe usarne un'altra: bisogna essere abbastanza flessibili da passare da una parametrizzazione all'altra e fare il test in funzione di quella data. Il passaggio in più riduce drasticamente la probabilità di errore.

## Distribuzione asintotica dello stimatore OLS nella regressione multipla

Valgono le solite ipotesi del modello di regressione: assenza di collinearità perfetta, dati osservati in modo indipendente dalla popolazione, esogeneità e alcune condizioni sui momenti delle variabili, cioè code delle distribuzioni non troppo pesanti, che altrimenti potrebbero distorcere le stime e la precisione dell'OLS. In queste condizioni si possono dimostrare vari risultati, tra cui la distribuzione asintotica dello stimatore. Se $n$ è sufficientemente grande e vale l'esogeneità, lo stimatore dei minimi quadrati di qualsiasi parametro $\beta_j$ si distribuisce come una normale centrata sul vero valore del parametro, con uno standard error dato da una formula calcolabile, che verrà discussa tra poco. Sono gli stessi risultati ottenuti nel modello di regressione semplice, con formule un po' più complicate: tutti i possibili risultati ottenuti da campioni diversi si distribuiscono come una normale con questa media e con una varianza calcolabile.

La dimostrazione richiede un po' di algebra lineare, che viene risparmiata. L'intuizione è quella del modello di regressione semplice: si applicano il teorema del limite centrale e la legge dei grandi numeri. L'ipotesi di dati indipendenti e quella sui momenti permettono di applicare la legge dei grandi numeri e il teorema del limite centrale, e quindi di ottenere il risultato. L'esogeneità permette di affermare che la media dello stimatore è il vero valore del parametro. L'omoschedasticità, con la sua alternativa, l'eteroschedasticità, è soltanto un'ipotesi di comodo e sarà trattata in dettaglio martedì prossimo.

### Quale distribuzione usare nei test

Per un test d'ipotesi su un qualsiasi parametro del modello si può usare la distribuzione per campioni finiti, cioè la $t$ di Student, oppure la distribuzione asintotica, cioè la normale. Per comodità il docente usa sempre la normale: con meno di 30 osservazioni in un modello di regressione multipla l'interpretazione dei risultati è comunque un po' a caso, per l'eccessiva incertezza dovuta al campione troppo piccolo. La $t$ di Student e la normale sono sovrapponibili oltre 30 gradi di libertà, senza differenza sostanziale. Il docente riconosce che non è un modo di dire elegante, ma va bene così.

Lo stimatore si distribuisce esattamente come una $t$ di Student solo se si ipotizza che il termine d'errore sia gaussiano, e tale ipotesi va anche giustificata prima di fare i calcoli. L'approssimazione asintotica funziona anche senza questa ipotesi, ed è quindi più flessibile: per questo il docente preferisce la distribuzione asintotica a quella per campioni finiti, perché richiede molte meno ipotesi.

Le ipotesi necessarie per la distribuzione asintotica si possono indebolire ulteriormente rispetto a quelle appena enunciate. Quando si passerà a lavorare con dati in serie storica, che non sono indipendenti ma dipendenti tra loro, la distribuzione per campioni finiti non si può calcolare, mentre quella asintotica sì. Ci sono quindi molte buone ragioni per ragionare sempre come se il campione fosse abbastanza grande: non occorre l'ipotesi di indipendenza, molto spesso basta una forma di esogeneità più debole di quella stretta e, soprattutto, non occorre ipotizzare che il termine d'errore sia gaussiano. L'errore non è osservabile, quindi non si può affermare che lo sia. Inoltre, se la variabile può assumere valori negativi, non è difficile pensare che l'errore sia definito su tutta la retta reale.

> [!question] Da verificare: la trascrizione riporta "se la variabile può assumere valori negativi, neanche è difficile pensare che l'errore possa essere definito su tutta la retta reale"; nel contesto dell'argomento contro l'errore gaussiano il senso atteso sarebbe l'opposto (se la variabile non può assumere valori negativi, è difficile pensarlo).

## Stima dei parametri e teorema di Frisch-Waugh-Lovell

Il passo successivo è la stima dei parametri, senza tutti i passaggi. Stimare i parametri equivale a minimizzare la dispersione delle osservazioni di $y$ rispetto al modello di regressione, cioè quanto $y$ si distanzia in media dalla retta (o dal piano) di regressione. L'esempio è un modello con due regressori, generalizzabile a qualsiasi numero di regressori. Si calcolano le derivate rispetto all'intercetta, a $b_1$ e a $b_2$, si pongono tutte uguali a zero e si risolve il sistema di tre equazioni in tre incognite. Il risultato è una formula, che è lo stimatore.

Il problema è che già nel modello di regressione semplice serve una pagina di algebra, noiosissima e senza alcuna utilità; con due regressori le pagine diventano due, con un altro regressore quattro, e così via. Trovare una formula che leghi il parametro ai dati è quindi molto complesso, a meno di usare l'algebra lineare e le matrici, che rendono tutto più facile.

Esiste però un modo alternativo di stimare qualsiasi parametro del modello di regressione, e il docente lo considera uno dei risultati più curiosi incontrati in econometria. Lo stimatore dei minimi quadrati del parametro $j$-esimo si ottiene da una regressione in cui la $y$ è la stessa e al posto di $x_j$ compare un regressore indicato con $\hat u_j$ (con il cappello). Applicando questa regressione ai dati si ottiene esattamente lo stesso numero della minimizzazione standard dei minimi quadrati, che è ciò che fa il computer. È una conseguenza di uno dei teoremi più utili dell'econometria, il teorema di Frisch-Waugh-Lovell. Anche la dimostrazione richiede un po' di algebra lineare e viene omessa; il funzionamento verrà mostrato con dati reali.

La quantità $\hat u_j$ è il residuo di una regressione speciale, quella del regressore associato a $\beta_j$ su tutti gli altri regressori del modello. Con due regressori, $\hat u_2$ è il residuo della regressione di $x_2$ su $x_1$ e $\hat u_1$ è il residuo della regressione di $x_1$ su $x_2$. Con dieci regressori, per $x_5$ si calcola la regressione del quinto regressore su tutti gli altri nove, dal primo al decimo escluso il quinto, e lo stesso si può fare per ciascuno. La quantità è dunque il residuo tra il valore del regressore e la previsione di quel regressore ottenuta con gli altri regressori.

### Il residuo come parte non prevedibile

Per capire l'intuizione conviene usare il modello di regressione semplice, più rapido da scrivere, ma il ragionamento vale anche per la regressione multipla. Nel modello $y = \alpha + \beta x + \varepsilon$ l'informazione contenuta in $y$ si divide in due parti: una completamente prevedibile dalle altre informazioni del modello, cioè da $x$, e una non prevedibile. Ogni osservazione si può pensare come la combinazione di questi due segnali. Il residuo è la differenza tra $y$ e la parte prevedibile, una volta fissati i parametri nel modo migliore consentito dalle stime. Rappresenta quindi l'informazione contenuta in $y$ che non è prevedibile da $x$. In generale ogni variabile si può decomporre in due segnali: quanto è prevedibile usando certe informazioni e quanto non lo è.

Si torna ora alla regressione di $y$ su $\hat u_j$. L'informazione usata per prevedere $y$ è quella del regressore $x_j$ che non dipende da tutti gli altri regressori: il residuo indica il contributo di $x_j$ indipendente dalle altre variabili del modello. Nell'esempio con due variabili, $\hat u_2$ è l'informazione contenuta in $x_2$ non prevedibile con $x_1$, e $\hat u_1$ è la componente di $x_1$ non prevedibile con $x_2$.

### Il coefficiente come correlazione parziale

Nel modello di regressione semplice il coefficiente $\beta$ rappresenta il legame tra le due variabili: è la covarianza divisa per la varianza, di fatto una correlazione. Si tratta di una correlazione marginale tra $x$ e $y$, perché non ci sono altre variabili e l'errore non conta. Nella regressione di $y$ su $\hat u_j$ il parametro è invece la correlazione tra $y$ e $\hat u_j$, cioè con l'informazione di $x_j$ non spiegabile con $x_i$. Il parametro è quindi la correlazione tra $y$ e $x_j$ una volta tolto l'effetto di $x_i$, con $i \neq j$. È lo stimatore del modello di regressione semplice applicato a quella regressione, in cui $\hat u_j$ è il regressore.

Il parametro si calcola come una correlazione marginale, ma su variabili già ripulite dall'effetto della terza variabile. Il suo nome statistico è correlazione parziale. Il risultato è coerente con quanto detto sull'effetto marginale, che era appunto una correlazione parziale.

Se si fissa il reddito (income) e si osserva che cosa succede alla performance quando cambia la dimensione della classe, si misura la correlazione tra due variabili tenendo fissa la terza. Ne segue che ogni coefficiente del modello di regressione multipla si può ancora interpretare come una correlazione, ma non come una correlazione marginale tra due variabili, indipendente da ciò che accade nel resto del mondo: è una correlazione parziale, calcolata dopo aver ripulito $x_j$ dell'effetto prevedibile tramite $x_i$. Dal punto di vista concettuale è il legame tra statistica ed economia, e a renderlo possibile è il teorema di Frisch-Waugh-Lovell.

### Procedura del teorema

Si considerino tre variabili, $Y$, $X_1$ e $X_2$; il teorema vale per qualsiasi numero di regressori. Per calcolare $\beta_1$, il parametro associato al primo regressore, si procede così. Prima si regredisce $Y$ su tutti i regressori diversi dal primo ($x_2, x_3, x_4$, quanti sono) e si salvano i residui. Poi si regredisce $x_1$, il regressore di interesse (la dimensione della classe), su tutti gli altri regressori e si salvano i residui: è la variabile $\hat u$ introdotta prima. A questo punto $\beta_1$ è il coefficiente della regressione semplice tra i residui del primo passo e i residui del secondo.

Il primo passo non è indispensabile per recuperare $\beta_j$, e lo si può dimostrare, ma senza di esso non si capisce il significato di $\beta_j$.

> [!question] Da verificare: la trascrizione riporta "se lo fate non capite niente a beta j"; il senso atteso è "se non lo fate", come conferma poco dopo l'osservazione che si può usare $y$ direttamente.

La dimostrazione richiede quattro righe, ma servirebbe una settimana di notazione di algebra lineare, e non è importante.

### Verifica numerica

L'uguaglianza non è approssimata: i due metodi danno esattamente lo stesso numero. Si consideri la regressione multipla della performance dei bambini a scuola sulla dimensione della classe, sul reddito e sulla costante. Il coefficiente di interesse, stimato con i minimi quadrati standard, è $-0{,}6487401$. Applicando la procedura di Frisch-Waugh-Lovell, si regredisce $x_1$ su $x_2$ e si salvano i residui, chiamati `ustr` (il nome è arbitrario). Poi si regredisce $y$ su $x_2$ e si salvano i residui. L'output di queste due regressioni non interessa. Infine si regredisce la nuova $y$ sulla nuova $x$, cioè i residui della seconda regressione su `ustr`. Il risultato coincide con il coefficiente di prima a qualsiasi decimale: è lo stesso numero dal punto di vista matematico.

I software non applicano questa procedura, perché richiede più tempo di una stima in blocco di tutti i parametri. Il risultato è però utile in teoria: in una regressione semplice il coefficiente è la correlazione tra due variabili, e qui le variabili sono già ripulite dall'effetto di tutte le altre. Si ha dunque una correlazione al netto di tutti gli effetti collaterali immaginabili.

Il risultato numerico non cambia se, invece dei residui della regressione di $y$ su $x_2$, si usa direttamente $y$. Cambiano eventualmente gli standard error, ma per stimare il parametro la procedura è quella. Per ora il risultato non ha utilità operativa, ma lo avrà a breve. Dal punto di vista teorico permette di dare un nome statistico, correlazione parziale, all'effetto marginale, che è un concetto puramente economico. Si era già visto fissando il reddito e osservando che cosa succede cambiando le altre variabili; ora c'è anche una giustificazione formale.

## Standard error dello stimatore nella regressione multipla

Interessa stimare non solo il parametro ma anche il coefficiente di precisione associato alla stima, cioè lo standard error. Nel modello di regressione semplice $y = \alpha + \beta x + \varepsilon$ era facile da calcolare:

$$
\hat\sigma_{\hat\beta} = \sqrt{\frac{\hat\sigma^2}{n\,\widehat{\operatorname{Var}}(x)}},
$$

dove $\hat\sigma^2$ è la stima della varianza dell'errore, più o meno la media dei quadrati dei residui del modello stimato, e $\widehat{\operatorname{Var}}(x)$ è la varianza di $x$ calcolata sul dataset.

> [!question] Da verificare: nel modello semplice la trascrizione parla di "n meno 1" per la varianza di $x$, mentre per il modello multiplo parla di "n volte la varianza"; si assume $n$ in entrambi i casi.

Gli ingredienti sono due: $\sigma^2$, la varianza del termine d'errore, e la varianza di $x$. Quanto più le $x$ sono disperse, cioè quanto più grande è la varianza di $x$, tanto più preciso è lo stimatore. Quanto più piccola è $\sigma^2$, tanto meglio è per lo stimatore. Questa formula serviva a ricordare come si calcola la seconda colonna della tabella di output di un modello di regressione.

Nella regressione multipla la formula non vale più, perché intervengono gli effetti collaterali degli altri regressori. Con l'algebra standard si ottiene

$$
\hat\sigma_{\hat\beta_j} = \sqrt{\frac{\hat\sigma^2}{n\,\widehat{\operatorname{Var}}(x_j)\,(1 - R_j^2)}}.
$$

La formula è un po' complicata, ma ci si può fidare. Il numeratore è come prima la varianza del termine d'errore, stimata con la media dei quadrati dei residui. Il denominatore contiene $n$ volte la varianza della variabile associata al coefficiente $j$-esimo, come nel modello semplice, a cui si aggiunge il fattore $1 - R_j^2$.

L'$R^2$ è un coefficiente di bontà di adattamento. L'$R_j^2$, con il pedice $j$, misura il grado di associazione tra la variabile $j$ e tutte le altre, ed è quello che si otterrebbe stimando il modello di $x_j$ su $x_1, x_2, \ldots, x_{j-1}, x_{j+1}, \ldots$ e tutte le altre. Indica quindi il livello di legame tra la variabile di cui si stima il parametro e le altre variabili del modello, esclusa ovviamente $y$.

Il docente chiede quale valore ci si aspetti per $R_j^2$ in caso di collinearità perfetta. La collinearità perfetta significa che un regressore è perfettamente legato agli altri, quindi la regressione darebbe $R_j^2 = 1$.

Nella regressione di $x_j$ sugli altri regressori la componente d'errore è nulla, quindi $R_j^2$ è esattamente uguale a 1. Il denominatore della formula dello standard error diventa zero, e la varianza esplode: è infinita. Con la collinearità l'imprecisione dello stimatore è quindi infinita e qualsiasi numero va bene. In un test d'ipotesi non si potrebbe mai rifiutare nessuna ipotesi nulla, e un intervallo di confidenza andrebbe da meno infinito a più infinito.

> [!question] Da verificare: nella trascrizione la frase "Quindi di fatto il modello diventa" è interrotta da caratteri illeggibili e non ha conclusione.

### Quasi collinearità e variance inflation factor

Gli ingredienti che determinano la precisione dello stimatore sono ora tre. Il primo è la varianza dell'errore, supponendo sempre valida l'omoschedasticità. Il secondo è la variabilità del regressore di interesse. Il terzo è il legame tra quel regressore e tutti gli altri: se è troppo forte, $R_j^2$ tende a 1, il fattore $1 - R_j^2$ diventa molto piccolo e la varianza risulta artificialmente aumentata.

Il calcolo di $1/(1 - R_j^2)$ serve a diagnosticare i casi di collinearità non esatta. Nel caso di collinearità esatta il problema viene risolto a priori dal software; la quantità permette invece di capire che cosa succede quando le variabili sono quasi collineari, cioè quando la loro correlazione è alta ma non tanto da diventare patologica. È comunque un problema. Con variabili correlate al 99%, la regressione che dà $R_j^2$ produce un numero molto vicino a 1, quindi il denominatore è molto piccolo, anche se non nullo. Gli standard error tendono a esplodere e gli intervalli di confidenza della stima diventano enormi, con grande incertezza nell'inferenza. L'intervallo non va da meno infinito a più infinito, ma magari da $-100$ a $+100$ quando la scala del parametro è 10, per cui la capacità di usare il modello è scarsa.

Un problema pratico è che, anche con un campione molto grande, lo zero potrebbe cadere nell'intervallo. Si potrebbe quindi concludere che un parametro non è statisticamente significativo soltanto perché si sono inseriti regressori non perfettamente collineari, ma quasi. Si sono aggiunte informazioni quasi inutili, e quel "quasi" crea un problema.

Per riconoscere un problema di quasi collinearità, i software calcolano il rapporto $1/(1 - R_j^2)$, chiamato variance inflation factor. Secondo il docente indica di quanto aumenta lo standard error rispetto al caso ideale in cui i regressori $x_1, x_2, x_3$ sono tutti indipendenti tra loro, caso che peraltro non è interessante.

> [!question] Da verificare: dalla formula presentata, il fattore $1/(1 - R_j^2)$ moltiplica la varianza dello stimatore; il docente parla di aumento dello standard error.

Se il valore supera 10 o 12 si ritiene che ci sia un problema di quasi collinearità e che l'aumento artificiale degli standard error cominci a essere problematico. È una regola empirica, non un teorema. Questa rappresentazione dello standard error permette dunque di stabilire quando c'è troppa correlazione tra regressori, un problema particolarmente sottile e di non facile soluzione, che si vedrà la prossima volta durante l'esercitazione.

Martedì prossimo la lezione della mattina non sarà tenuta dal docente ma dal ricercatore, che la terrà anche nel pomeriggio; le ore del martedì mattina sono state scambiate. Si farà l'applicazione al modello di regressione multipla e, probabilmente, alcuni esercizi. Il docente tornerà a fare lezione verso dicembre, per un giorno di quattro ore. Tutto è già nel calendario didattico online.

> [!question] Da verificare: la trascrizione dell'inciso sul calendario è confusa ("farò quattro ore", "poi sono tre, in realtà", "esercizi di poesare"); fa fede il calendario didattico online.

> [!tip] Esame
> Il docente consiglia di venire alla lezione di martedì, perché con esempi si vedrà che cosa succede quando $R_j^2$ è molto grande e come si calcola. È un problema utile da conoscere.

Uno studente chiede quale sia la regressione che definisce $R_j^2$. Il docente risponde che è quella tra $x_j$ e tutte le altre variabili, qualunque ne sia il numero. Nell'esempio, con $j$ uguale alla variabile 1 (la dimensione della classe), $R_j^2$ è l'$R^2$ della regressione in cui la dimensione della classe è la variabile dipendente e il reddito è il regressore. Con dieci variabili, tra cui oltre al reddito anche la percentuale di madrelingua nel distretto e altre informazioni, $R_j^2$ sarebbe l'$R^2$ tra la dimensione della classe e tutti gli altri regressori. Un $R_j^2$ alto significa che le altre variabili spiegano il regressore, cioè che si stanno aggiungendo al modello variabili ridondanti, o quasi ridondanti.

Se sono perfettamente ridondanti, il software segnala un problema di collinearità perfetta: un problema matematico, con infinite soluzioni, nei minimi quadrati. Un'equazione delle condizioni del primo ordine dell'ottimizzazione è un doppione di un'altra. Nel caso di un quasi doppione il software calcola tutto, e il "quasi" inganna: ce ne si accorge solo indirettamente, perché aggiungendo una variabile gli standard error aumentano di tre, quattro, cinque o sei volte e ciò che prima era significativo non lo è più.

### Esempio: il differenziale salariale tra uomini e donne

L'esempio che si vedrà con il professor Peruzzi è il seguente. Nella prima parte dell'esercitazione si stima un modello per capire il differenziale di salario tra uomini e donne. Una serie di modelli più o meno standard mostra che, a meno di qualche variabilità, la differenza è di circa il 30% in termini di salari, statisticamente significativa. Si aggiunge poi un regressore di interesse pratico, una specie di dummy che interagisce con una variabile continua (lo si vedrà). Automaticamente il coefficiente della variabile di genere $female$ risulta non significativo: la stima è più o meno la stessa, 27% anziché 30%, qualitativamente sempre un numero gigante, ma non è significativo. Anche la variabile aggiunta non è significativa. Si è quindi aggiunto qualcosa di inutile e, per un parametro di cui si era quasi certi, non si ha più la correlazione parziale.

Passando dal modello senza problemi al modello con problemi, gli standard error aumentano di cinque o sei volte. Nel test $t$ il denominatore gigante comprime la statistica, quindi non si rifiuta l'ipotesi nulla. Il software non segnala nulla, fa solo i calcoli, e ce ne si deve accorgere da soli, in generale confrontando le tabelle dei due modelli. La diagnosi consiste nel riconoscere che lo standard error è una combinazione di tre ingredienti, non più due.

Per la precisione dello stimatore non contano quindi soltanto la varianza della variabile e quella dell'errore, ma anche il modo in cui la variabile si rapporta a tutte le altre in termini di correlazione. Questi indicatori si calcolano con il software, senza stimare la regressione a mano: premendo il comando giusto compare una tabella con questi numeri per ogni regressore del modello, e basta leggerli. La regola è che un valore maggiore di 10 o 12 segnala un potenziale problema. Questa è la parte teorica più complessa; l'importante è coglierne l'intuizione.

## Previsione, residui e bontà di adattamento

Una volta calcolata la stima, con il metodo standard o con il metodo dei momenti visto per la regressione semplice (utilizzabile anche qui, con un'algebra più complicata), il modello si può usare per fare previsioni. La previsione per un'osservazione, fissati certi regressori, si ottiene dalla definizione di media condizionata sostituendo ai veri parametri le stime.

Il docente usa lo stesso simbolo per la stima e per lo stimatore, e osserva di non averlo detto prima. La stima è il numero che compare nella tabella di output, lo stimatore è la formula che permette di ottenere quel numero. Si usa sempre il nome del parametro, e il contesto chiarisce il significato. Nella formula della previsione i simboli indicano le stime, cioè numeri; in una relazione che coinvolge variabili indicano lo stimatore, che è una variabile casuale. Si usa lo stesso simbolo per evitare simboli ridondanti.

La componente residuale è la differenza tra l'osservazione e la previsione. Sottraendo alla vera osservazione la previsione calcolata in questo modo si ottiene il residuo. È esattamente quanto visto nel modello di regressione semplice, con più variabili.

L'$R^2$, indicatore di bontà di adattamento, si può calcolare come il quadrato della correlazione tra la variabile $y$ e i valori predetti, cioè la $y$ come la prevede il modello. Si può calcolare anche come nei libri di testo, tramite il rapporto tra la somma dei quadrati dei residui e la variabilità totale di $y$, ma il docente preferisce questa lettura: è una correlazione, quindi un indicatore soltanto statistico, che non dice se il modello è buono dal punto di vista causale.

> [!question] Da verificare: nel descrivere la formula dei libri la trascrizione non cita il termine "1 meno" che compare nella definizione abituale di $R^2$.

Essendo una correlazione al quadrato, l'$R^2$ è compreso tra 0 e 1. Il valore 1 indica un buon adattamento: il modello si adatta molto bene ai dati e la previsione è molto vicina alla vera osservazione. Il valore 0 indica che i regressori non sono particolarmente utili per prevedere $y$, e lo sono dal punto di vista statistico, non causale o logico.

### R² aggiustato

Quando si stima un modello di regressione compaiono in realtà due $R^2$: quello appena descritto, cioè la correlazione al quadrato, e l'$R^2$ aggiustato. Il motivo è che l'$R^2$ non è molto utile per stabilire se un modello è buono, perché aumenta sempre quando si aggiungono variabili. Aggiungendo un regressore l'$R^2$ aumenta, è un fatto matematico senza alternative. Per confrontare due modelli che differiscono per uno, due o tre regressori, gli statistici vorrebbero un indicatore che dica, per esempio, che aggiungendo un regressore la bontà di adattamento aumenta del 5%. Ma poiché l'$R^2$ cresce sempre con il numero di variabili, non si sa se il 5% sia molto o poco.

La soluzione è sottrarre all'$R^2$ una penalità, un numero negativo che dipende dal numero di parametri. Si cerca così un compromesso: aggiungendo variabili migliora l'adattamento ma peggiora la penalità. L'$R^2$ corretto con la penalizzazione non è sempre crescente e, con troppi parametri, può anche peggiorare. Indica che il beneficio statistico dell'aggiunta di una variabile è in qualche modo compensato, o più che compensato, dall'aumento di complessità del modello. Il docente non ricorda la formula della penalizzazione, che è comunque una funzione del numero dei parametri. I due indicatori sono quindi l'$R^2$ puro, sempre crescente con i regressori, e l'$R^2$ meno una penalità, che può anche decrescere.

In generale si accetta di aggiungere una variabile al modello se l'$R^2$ aggiustato aumenta, perché al netto della penalizzazione è comunque un miglioramento. Dire che il miglioramento è significativo non è corretto, perché non si sta facendo un test e non è una procedura inferenziale, ma ci si muove in quella direzione. Il docente dichiara di non guardarlo, ma sostiene che bisogna saperlo.

## Intervalli di confidenza, test e teorema di Gauss-Markov

Una volta ottenuti gli stimatori e le formule degli standard error si può calcolare l'intervallo di confidenza per qualsiasi parametro, e i test si eseguono nel modo standard.

Anche in questo caso vale il teorema di Gauss-Markov. Se c'è omoschedasticità e valgono tutte le altre ipotesi, stimare i parametri con i minimi quadrati ordinari è il modo migliore di aggregare i dati, perché dà il livello massimo di precisione: fissati i dati, è il modo di calcolare il parametro che riduce lo standard error. Il teorema dimostra questo. Non è particolarmente importante, perché l'omoschedasticità, come si vedrà, di fatto non esiste.

## Notazione matriciale

L'ultima parte è quella che il docente risparmia in aula, ma suggerisce di darci un'occhiata perché può essere utile. Nei libri di testo quanto visto è quasi sempre rappresentato in termini di algebra lineare. Qui si mostra come tutto si possa scrivere con matrici e vettori.

Il modello di regressione si scrive con un vettore $y$ di $n$ righe e una colonna, che contiene tutta l'informazione sulla variabile $y$; una matrice $X$ dei regressori, che contiene tutti i dati sulle variabili; un vettore dei parametri e un vettore del termine d'errore. Applicando la derivata rispetto all'intero vettore dei parametri si ottiene che lo stimatore dei minimi quadrati si può sempre scrivere in forma matriciale, qualunque sia il numero dei regressori. In quella formula $(X^\top X)^{-1}$ non è altro che il denominatore.

> [!question] Da verificare: la formula scritta alla lavagna non è riportata nella trascrizione, che cita soltanto "x trasposto x alla meno uno" come denominatore.

Il prodotto $X^\top X$ è di fatto il quadrato di $X$. Nel modello di regressione semplice il denominatore è la somma degli $x$ al quadrato e il numeratore è la covarianza tra $x$ e $y$, cioè il prodotto incrociato tra $x$ e $y$. In generale, più come intuizione che come formalismo, al denominatore compaiono i momenti secondi empirici delle variabili $x$ e al numeratore il prodotto incrociato tra $x$ e $y$. La formula è comoda perché permette di scrivere qualsiasi stimatore dei minimi quadrati indipendentemente dalla dimensione del modello: con un regressore o con duemila è sempre la stessa. Tutto ciò che serve per stimare con i minimi quadrati si scrive in cinque righe, ricordando che le derivate rispetto ai vettori seguono regole precise.

Il docente suggerisce di dare un'occhiata a questa parte, soltanto per convincersi che l'algebra lineare è un modo furbo di scrivere tutto ciò che è stato fatto finora, senza niente di più e niente di meno. È comoda se ci si concentra sugli sviluppi teorici: per esempio, dimostrare il teorema di Frisch-Waugh-Lovell con le sommatorie è complicato, mentre con l'algebra matriciale il problema si risolve in tre righe. È solo una questione meccanica.

## Test su più parametri: stato civile ed etnia nel modello del salario

Finora, nel modello di regressione semplice e in quello multiplo, l'inferenza è stata fatta su un solo parametro. In un modello di regressione si può però voler fare un test su più parametri contemporaneamente o su combinazioni lineari di parametri. Si usa il materiale sulla verifica d'ipotesi con restrizioni multiple.

### Il modello

L'esempio è una variante del modello visto finora. Invece di una sola dummy qualitativa che divide il campione in genere maschile e genere femminile, si divide il campione in quattro gruppi, per vedere se esiste una relazione congiunta tra più caratteristiche: persone sposate o non sposate, e di una certa etnia. L'etnia è stilizzata, come persona di colore o non di colore: non è un esempio molto articolato, serve a dare l'idea.

Nell'economia del lavoro il matrimonio è considerato un'approssimazione del livello di impegno di lungo periodo di una persona, che può avere un impatto sulla relazione tra salario e lavoro. Chi è sposato potrebbe avere una visione di più lungo periodo di un altro, perché fa più fatica a licenziarsi e a spostarsi altrove, magari in un'altra parte del mondo, dovendo ragionare in contesti più complessi. Lo stato civile entra quindi nel modello come proxy del commitment, cioè dell'impegno di lungo periodo. È solo un'approssimazione.

La variabile dipendente è il logaritmo del salario, che permette di interpretare le variazioni in termini percentuali, come già visto. Il modello è

$$
\begin{aligned}
\log(\text{wage}) = {}& \alpha + \beta_1\,\text{educ} + \beta_2\,\text{exper} + \beta_3\,\text{tenure} + \beta_4\,\text{south} + \beta_5\,\text{urban} \\
& + \beta_6\,\text{marr\_black} + \beta_7\,\text{single\_black} + \beta_8\,\text{marr\_nonblack} + \beta_9\,\text{single\_nonblack} + \varepsilon .
\end{aligned}
$$

Accanto all'istruzione e all'esperienza compare la tenure: l'esperienza indica da quanti anni si lavora, la tenure da quanti anni si lavora nell'impiego attuale. Si può lavorare da dieci anni ma solo da cinque in una certa banca: la tenure è cinque e l'esperienza dieci. La variabile south indica se il lavoratore viene dal sud o dal nord degli Stati Uniti, e un'altra variabile se vive in una città oppure in campagna.

Le quattro dummy sono $\text{marr\_black}$, che vale 1 per un individuo sposato e di colore, $\text{single\_black}$ per non sposato e di colore, $\text{marr\_nonblack}$ per sposato e non di colore, $\text{single\_nonblack}$ per non sposato e non di colore. Le quattro categorie coprono tutte le persone del campione, senza che nessuno rimanga fuori e senza sovrapposizioni. C'è quindi un problema di collinearità: la somma di tutte le dummy è 1, perché per ogni persona una sola dummy vale 1 e le altre valgono 0. È un problema di collinearità esatta.

### La domanda di ricerca

A parità di altre caratteristiche (stesso livello di istruzione, stessa esperienza, stessa tenure, stesso luogo di residenza) ci si chiede se c'è una differenza statisticamente significativa tra i lavoratori sposati di colore e quelli sposati non di colore. In altri termini, a parità di stato civile, se c'è una differenza tra persone di colore e non di colore.

Dal punto di vista matematico occorre individuare quali parametri definiscono la differenza di valore atteso tra i due gruppi. Si stima prima il modello. Il software elimina automaticamente una delle dummy, perché la somma delle dummy è 1 e c'è un problema di perfetta collinearità, in una forma un po' più complicata rispetto a quella già vista. Come detto, eliminare un gruppo o un altro non cambia nulla dal punto di vista inferenziale: cambia soltanto l'interpretazione. Il software elimina in automatico il gruppo single, qui $\text{single\_black}$.

### Valori attesi dei quattro gruppi

Per calcolare i differenziali servono le aspettative del modello nei vari scenari, fissando le altre variabili.

- Sposati di colore: la dummy $\text{marr\_black}$ vale 1 e le altre dummy valgono 0, quindi il coefficiente $\beta_6$ è moltiplicato per 1 e l'intercetta di questo gruppo è $\alpha + \beta_6$.
- Sposati non di colore: $\text{marr\_nonblack}$ vale 1 e le altre dummy 0, quindi sopravvive il coefficiente $\beta_8$ e l'intercetta è $\alpha + \beta_8$.
- Non sposati di colore ($\text{married} = 0$, $\text{black} = 1$): la dummy corrispondente è quella eliminata dal software, e tutte le altre dummy valgono 0, quindi l'intercetta è soltanto $\alpha$.
- Non sposati non di colore: l'intercetta è $\alpha + \beta_9$.

> [!question] Da verificare: per il terzo gruppo la trascrizione riporta "beh, a volte 8, la variabile che il software mi ha tolto e di conseguenza l'intercetta è andata solo al 40"; il senso più probabile è che la dummy tolta sia quella dei non sposati di colore e che l'intercetta sia $\alpha$.

### Il differenziale tra sposati di colore e sposati non di colore

I due gruppi di interesse sono gli sposati di colore e gli sposati non di colore. Il differenziale di salario tra loro è la differenza delle due intercette, cioè $\beta_6 - \beta_8$. Il differenziale si può stimare, sottraendo la stima del coefficiente $\beta_8$ a quella del coefficiente $\beta_6$. Come al solito, però, resta da stabilire se quel numero, grande o piccolo, sia uguale a zero o diverso da zero, e per questo serve un test statistico.

Si potrebbe prendere lo stimatore del differenziale e calcolare un test $t$. Il problema è il denominatore, che non è immediato da calcolare, pur essendo possibile: bisogna cercare i vari pezzi, in particolare la covarianza tra $\hat\beta_6$ e $\hat\beta_8$. Lo standard error è infatti la radice quadrata della varianza di $\hat\beta_6$ più la varianza di $\hat\beta_8$ meno due volte la covarianza tra i due. I calcoli andrebbero fatti a mano. Il docente sa che gli studenti non li fanno e, per pigrizia, non vuole farli.

In linea di principio, dunque, il problema economico richiede una combinazione lineare di parametri e si vuole fare inferenza su di essa, cioè sapere se è statisticamente significativa. Non basta sapere che il differenziale è negativo, perché l'errore di stima potrebbe essere abbastanza grande da rendere il valore stimato non rilevante, al netto dell'errore campionario. Serve quindi una statistica, che per pigrizia è complicata ma si può calcolare. Questo è il primo esempio.

### Significatività congiunta di tre regressori

Il secondo esempio è un po' più complicato. Si consideri un modello di regressione con tre regressori (il numero è arbitrario). Ci si chiede se l'uso congiunto di quei tre regressori aiuti a prevedere $y$: un ragionamento puramente statistico, cioè se $x_1$, $x_2$ e $x_3$ siano utili complessivamente nel modello. Occorre verificare se i tre coefficienti sono tutti uguali a zero oppure se almeno uno è diverso da zero. È un'ipotesi composta, in cui tre ipotesi nulle su tre parametri si confrontano con l'alternativa che almeno un coefficiente sia diverso da zero.

Si confrontano di fatto due modelli. Sotto l'ipotesi nulla $\beta_1 = \beta_2 = \beta_3 = 0$ i termini corrispondenti si possono eliminare, perché sono zero moltiplicato per qualcosa, e si ottiene un modello in cui le $x$ non servono a niente. Il problema è come calcolare un test di questo tipo.

> [!question] Da verificare: la trascrizione dice che la scrittura è un modo compatto per dire "beta1 uguale a zero, oppure beta2 uguale a zero, oppure beta3 uguale a zero"; l'ipotesi nulla congiunta richiede però che valgano tutte e tre.

Sono tre test. L'idea ingenua è calcolare tre test $t$, uno su $\beta_1$, uno su $\beta_2$ e uno su $\beta_3$. Se in tutti e tre i casi non si rifiuta l'ipotesi nulla, i tre parametri sarebbero congiuntamente indistinguibili dallo zero. Se in anche uno solo dei tre test si rifiuta l'ipotesi nulla, esisterebbe almeno un coefficiente diverso da zero e quindi almeno una $x$ sarebbe utile per prevedere $y$. Il docente chiede agli studenti se la strategia suoni sensata come strategia generale, e afferma che non funziona.

### Perché tre test in sequenza non funzionano

Non funziona perché si perde il controllo sulla probabilità di errore. Un test d'ipotesi su un unico parametro, come il test $t$, fissa la probabilità dell'errore del primo tipo, cioè di dichiarare vera l'alternativa quando non lo è, per esempio al 5%. La probabilità di sbagliare in ciascun test è quindi il 5%, e nel 95% dei casi non si commette quell'errore.

Con una sequenza di test uguali si fa una semplificazione formale: i test su $\beta_1$, $\beta_2$ e $\beta_3$ si ipotizzano indipendenti. Non lo sono, perché per calcolare le tre statistiche si usa sempre la stessa $y$ negli stimatori, ma si finge che lo siano per rendere più chiara l'intuizione. Applicando in sequenza i tre test, ciascuno con probabilità 5% di sbagliare e 95% di non sbagliare, la probabilità di non sbagliare in nessuno dei tre è il prodotto delle probabilità di non sbagliare nel test 1, nel test 2 e nel test 3: $0{,}95 \cdot 0{,}95 \cdot 0{,}95$, circa 86%. La probabilità di errore complessiva è quindi circa 14%, o più.

In una sequenza di test, tutti con probabilità di errore tollerabile $\alpha$ pari al 5%, l'errore complessivo non è più il 5% ma 14%, 16% o simili.

> [!question] Da verificare: il docente osserva che il calcolo è una semplificazione e che "se il test fosse tollerabile forse è ancora peggio"; la frase non è chiara.

Guardando tre test singolarmente quando si vorrebbe un test congiunto si perde completamente il controllo sulla probabilità di errore che si è disposti a tollerare per prendere una decisione. Quando si decide non si sa quanto si sbaglia: di fatto si decide a caso, senza alcun benchmark a cui aggrapparsi. Serve quindi una strategia diversa, che non guardi tre test in sequenza ma produca un test congiunto.

### Il test F

Il test che risolve il problema è il test di tipo $F$, che il docente chiede se gli studenti hanno già visto, e che definisce molto semplice. Il test $F$ considera una o più combinazioni lineari di parametri e verifica se sono soddisfatte dai dati. Nel primo esempio la combinazione lineare è $\beta_6 - \beta_8$. Nel secondo il sistema di vincoli imposto nello spazio parametrico è $\beta_1 = 0$, $\beta_2 = 0$, $\beta_3 = 0$. Entrambi i casi si possono rappresentare come una o più combinazioni lineari nello spazio parametrico. Si cerca una strategia statistica che permetta di fare entrambi i tipi di test in modo univoco. Il tempo è finito: se ne parlerà giovedì prossimo. Il docente osserva che non è particolarmente complicato.
