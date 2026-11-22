---
title: "Econometria — formulario"
subtitle: "Formule, quando usarle e come leggere un output"
coursecode: "EM0004"
disclaimer: "Formulario personale a fini di studio (Econometria EM0004, prof. Davide Raggi), costruito sulle note verificate del corso. Non è materiale ufficiale del docente."
---

# Come usare il formulario

L'esame è scritto, circa 90 minuti, circa dieci domande. Si chiede di **interpretare** grafici e tabelle di output e di fare inferenza con quelli: non si chiede di eseguire le stime. Quindi servono due cose: sapere *quale* test serve per la domanda posta e saper *leggere* ogni cella dell'output.

Il formulario serve anche per svolgere le **esercitazioni** (moduli 00-07 e appelli simulati), che partono dalle fondamenta di probabilità e statistica e arrivano alla cointegrazione. Per questo contiene i richiami di statistica di base, i calcoli a mano (stima OLS da medie e covarianze, test $F$ da SSR, errore standard di una combinazione lineare) e le convenzioni degli esercizi. Nelle esercitazioni i valori critici sono dati dal testo, salvo i quantili della normale: $1{,}96$ (5% bilaterale), $1{,}64$ (5% unilaterale), $2{,}57$ (1% bilaterale). L'ECM si scrive con il coefficiente di aggiustamento $\lambda<0$, come nei testi d'esame.

Ogni voce ha la stessa forma: **Quando** si usa, **Formula**, **Come si decide**, **Trappola**. Il simbolo † segna una formula standard o ricavata che le slide non enunciano ma che un tema può richiedere. Dove la nota del corso corregge le slide, l'ultimo capitolo elenca le differenze.

Notazione: $n$ osservazioni, $k$ regressori esclusa la costante, $s$ numero di vincoli di un'ipotesi, $T$ lunghezza di una serie storica, $\alpha$ livello di significatività (5% se non detto altrimenti).

# Dal testo alla formula

| Il testo chiede | Strumento | Capitolo |
|---|---|---|
| media, varianza, covarianza, correlazione di variabili o di una somma | momenti e loro proprietà | Richiami di probabilità e statistica |
| intervallo o test su una media, una proporzione, due gruppi, dati appaiati | $z$ o $t$ sulla media | Richiami di probabilità e statistica |
| tabella di contingenza, indipendenza fra due variabili | distribuzioni condizionali | Richiami di probabilità e statistica |
| dati cross-section, serie storiche o panel; «è causale?» | criteri di causalità | Causalità e tipi di dato |
| «calcola $\hat\alpha$ e $\hat\beta$ da medie e covarianza» | OLS dai momenti campionari | Regressione lineare |
| «$\beta$ è significativo?», «$X$ ha effetto?» | test $t$, oppure $0\notin$ IC | Inferenza su un coefficiente |
| «l'affermazione del testo è compatibile con i dati?» | H0 e H1 dall'affermazione, $t$ o IC | Inferenza su un coefficiente |
| «il modello è nel complesso significativo?», «$X_1$ e $X_2$ insieme?» | test $F$ | Inferenza su più coefficienti |
| «i due coefficienti sono uguali?» | test $F$ con $s=1$ | Inferenza su più coefficienti |
| «di quanto cambia $Y$ se $X$ aumenta di…?» | effetto marginale | Regressione lineare, Forme funzionali |
| «la stima è distorta / consistente?» | ipotesi OLS, variabile omessa, errore di misura | Ipotesi OLS, Endogeneità |
| «i regressori sono troppo correlati?» | VIF, perfetta collinearità | Collinearità |
| «gli errori sono omoschedastici?» | Breusch-Pagan, White | Eteroschedasticità |
| «gli standard error sono affidabili?» | errori standard robusti | Eteroschedasticità |
| «i residui sono autocorrelati?» | ACF, Ljung-Box | Serie storiche |
| «che processo è?» | firma di ACF e PACF | Serie storiche |
| «c'è un cambiamento strutturale?» | Chow (data nota), QLR (data ignota) | Break strutturali |
| «la serie è stazionaria?», «c'è una radice unitaria?» | Dickey-Fuller, ADF | Non stazionarietà |
| «c'è una relazione di lungo periodo fra serie non stazionarie?» | Engle-Granger, DOLS | Cointegrazione |
| «quanto velocemente si torna all'equilibrio?» | coefficiente di aggiustamento dell'ECM/VECM | Cointegrazione |

# Richiami di probabilità e statistica

Servono come base di tutto il resto: gli errori standard di OLS, i test e gli intervalli sono questi stessi strumenti applicati a $\hat\beta$.

## Variabile casuale, covarianza e correlazione

**Quando.** Calcolare media e varianza da una tabella di probabilità, o di una trasformazione o somma di variabili.

$$E[X]=\sum_x x\,P(X=x)\qquad\mathrm{Var}(X)=\sum_x(x-\mu)^2P(X=x)=E[X^2]-\mu^2$$

$$E[aX-c]=aE[X]-c\qquad\mathrm{Var}(aX-c)=a^2\,\mathrm{Var}(X)$$

$$s_{xy}=\frac1n\sum_i(x_i-\bar x)(y_i-\bar y)=\frac1n\sum_ix_iy_i-\bar x\bar y\qquad\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{s_X\,s_Y}\in[-1,1]$$

$$\mathrm{Cov}(aX,bY)=ab\,\mathrm{Cov}(X,Y)\qquad\mathrm{Cov}(a+X,b+Y)=\mathrm{Cov}(X,Y)\qquad\mathrm{Cov}(X,X)=\mathrm{Var}(X)$$

$$E[X\pm Y]=E[X]\pm E[Y]\qquad\mathrm{Var}(X\pm Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\pm2\,\mathrm{Cov}(X,Y)$$

**Come si legge.** La varianza di una somma non è la somma delle varianze: serve la covarianza. Variabili indipendenti hanno covarianza nulla (l'indipendenza implica l'incorrelazione, non il contrario). Sommare una costante non cambia la covarianza; moltiplicare per $a$ e $b$ la moltiplica per $ab$.

**Valore atteso condizionale ed esogeneità.** Se $E[\epsilon\mid X=x]=0$ per ogni $x$, allora $E[\epsilon]=0$, $\mathrm{Cov}(X,\epsilon)=0$ e $E[Y\mid X]=\alpha+\beta X$. Non vale il contrario: un errore può essere incorrelato con $X$ ed avere media condizionale non nulla (dipendenza non lineare); allora $\Delta E[Y\mid X]=\beta\Delta X+\Delta E[\epsilon\mid X]$.

## Campione casuale e media campionaria

**Quando.** Stimare una media $\mu$ di popolazione da un campione di $n$ osservazioni.

In un campione casuale semplice le $Y_i$ sono indipendenti con la distribuzione della popolazione: $E[Y_i]=\mu$, $\mathrm{Var}(Y_i)=\sigma^2$, $\mathrm{Cov}(Y_i,Y_j)=0$ per $i\neq j$.

$$E[\bar Y]=\mu\ \ (\text{corretta})\qquad\mathrm{Var}(\bar Y)=\frac{\sigma^2}{n}\qquad\mathrm{se}(\bar Y)=\frac{\sigma}{\sqrt n}\ \text{stimato da}\ \frac{s}{\sqrt n}$$

$$\frac{\bar Y-\mu}{\sigma/\sqrt n}\ \approx\ N(0,1)\ \ (\text{CLT, anche se }Y\text{ non è normale})$$

La varianza tende a zero al crescere di $n$: $\bar Y$ è consistente (legge dei grandi numeri).

**Trappola: osservazioni correlate.** Se ogni coppia ha correlazione $\rho$, $\mathrm{Cov}(Y_i,Y_j)=\rho\sigma^2$ e

$$\mathrm{Var}(\bar Y)=\frac{\sigma^2}{n}\,\big[1+(n-1)\rho\big]$$

La media resta corretta, ma l'errore standard cresce di $\sqrt{1+(n-1)\rho}$: osservazioni correlate valgono meno di osservazioni indipendenti e trattarle da indipendenti fa rifiutare troppo.

## Intervallo di confidenza e test sulla media

**Quando.** Una domanda sul valore di $\mu$: «è compatibile con $\mu_0$?», «tra quali valori sta?».

$$\text{IC}=\bar y\pm z\,\frac{s}{\sqrt n}\ \ (z=1{,}64\ \text{al 90\%},\ 1{,}96\ \text{al 95\%},\ 2{,}57\ \text{al 99\%})\qquad t=\frac{\bar y-\mu_0}{s/\sqrt n}$$

| Alternativa $H_1$ | Si rifiuta $H_0:\mu=\mu_0$ se | p-value |
|---|---|---|
| $\mu<\mu_0$ | $t<-1{,}64$ | $P(Z\le t^{obs})$ |
| $\mu>\mu_0$ | $t>1{,}64$ | $P(Z\ge t^{obs})$ |
| $\mu\neq\mu_0$ | $\lvert t\rvert>1{,}96$ | $2\,P(Z\ge\lvert t^{obs}\rvert)$ |

Rifiutare $H_0$ al 5% bilaterale equivale ad avere $\mu_0$ fuori dall'IC al 95%. Si rifiuta quando il p-value è minore del livello. Il p-value è la probabilità, sotto $H_0$, di un risultato almeno così contrario a $H_0$ come quello osservato: non è la probabilità che $H_0$ sia vera. L'errore di primo tipo è rifiutare una $H_0$ vera (la sua probabilità è il livello); l'errore di secondo tipo è non rifiutare una $H_0$ falsa.

**Piccoli campioni.** Se la popolazione è normale e $n$ è piccolo (sotto 25-30), $t$ ha distribuzione $t$ di Student con $n-1$ gradi di libertà: code più pesanti, valore critico più grande, IC più largo di quello con $1{,}96$. Con $n$ grande si torna alla normale.

**Trappola.** Il 95% riguarda i campioni ripetuti (il 95% degli intervalli contiene $\mu$): non è la quota di dati dentro l'intervallo.

## Proporzioni

**Quando.** La variabile è un sì/no. Una proporzione è la media di variabili di Bernoulli: $\hat\pi=x/n$, media $\pi$, varianza $\pi(1-\pi)/n$.

$$\text{IC}=\hat\pi\pm1{,}96\sqrt{\frac{\hat\pi(1-\hat\pi)}{n}}\qquad z=\frac{\hat\pi-\pi_0}{\mathrm{se}_0},\ \ \mathrm{se}_0=\sqrt{\frac{\pi_0(1-\pi_0)}{n}}$$

Nel **test** l'errore standard si calcola sotto $H_0$ (con $\pi_0$); nell'**IC** non si assume nulla e si usa $\hat\pi$.

**Due proporzioni.** Sotto $H_0:\pi_1=\pi_2$ si usa la proporzione combinata:

$$\hat\pi=\frac{x_1+x_2}{n_1+n_2}\qquad z=\frac{\hat\pi_1-\hat\pi_2}{\mathrm{se}_0},\ \ \mathrm{se}_0=\sqrt{\hat\pi(1-\hat\pi)\Big(\frac1{n_1}+\frac1{n_2}\Big)}$$

L'IC per $\pi_1-\pi_2$ usa errori standard separati: $\hat\pi_1-\hat\pi_2\pm1{,}96\sqrt{\hat\pi_1(1-\hat\pi_1)/n_1+\hat\pi_2(1-\hat\pi_2)/n_2}$.

## Confronto fra due medie e dati appaiati

**Due campioni indipendenti.** $\mathrm{Cov}(\bar Y_1,\bar Y_2)=0$, quindi

$$\mathrm{se}(\bar y_1-\bar y_2)=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}\qquad t=\frac{\bar y_1-\bar y_2}{\mathrm{se}}\quad(\lvert t\rvert>1{,}96\Rightarrow\text{si rifiuta }H_0:\mu_1=\mu_2)$$

Equivalente: la differenza $\pm1{,}96\,\mathrm{se}$ non contiene lo zero. Due IC delle medie che si sovrappongono sono solo un'indicazione: la differenza può essere significativa lo stesso, perché $\mathrm{se}<\mathrm{se}_1+\mathrm{se}_2$.

**Dati appaiati** (stesse unità prima e dopo). Si lavora sulle differenze $d_i=\text{dopo}_i-\text{prima}_i$:

$$\bar d=\bar y_{dopo}-\bar y_{prima}\qquad s_d^2=s_{dopo}^2+s_{prima}^2-2\,s_{dopo,prima}\qquad t=\frac{\bar d}{s_d/\sqrt n}$$

La covarianza positiva (stessa unità osservata due volte) riduce $s_d^2$ e quindi l'errore standard. Trattare le due misure come indipendenti usa una varianza troppo grande e fa perdere potenza.

## Tabelle di contingenza e indipendenza

**Quando.** Due variabili categoriche in una tabella di frequenze.

$$P(A\mid B)=\frac{n(A\cap B)}{n(B)}\qquad\text{in generale }P(A\mid B)\neq P(B\mid A)$$

La distribuzione condizionale si ottiene dividendo ogni cella per il totale della riga (o colonna) su cui si condiziona. Se $A$ e $B$ sono indipendenti, $P(A\mid B)=P(A)$ per ogni $B$: le distribuzioni condizionali coincidono con quella complessiva e il numero atteso di unità in $A\cap B$ è $n(B)\,P(A)$. Si confrontano le **percentuali di riga**, non i conteggi, quando i gruppi hanno numerosità diverse.

# Causalità e tipi di dato

**Causalità.** Si parla di relazione causale $X\to Y$ solo se valgono **insieme** tre criteri: (1) associazione, (2) ordine logico o temporale, (3) esclusione di spiegazioni alternative. L'associazione è simmetrica: la correlazione di $X$ con $Y$ è quella di $Y$ con $X$, quindi non dice quale variabile preceda l'altra. Se il verso non è chiaro c'è **causalità inversa**, e il regressore risulta correlato con l'errore.

**Relazione spuria.** Un legame fra $X$ e $Y$ indotto da una terza variabile $Z$ che influisce su entrambe. Se $Z$ è omessa, la stima del coefficiente di $X$ coglie anche l'effetto di $Z$ (variabile omessa). Se, controllando per $Z$, l'associazione sparisce, la relazione era spuria. Non si può dimostrare che una relazione sia causale: si confutano le spiegazioni alternative, e un test che non rifiuta $H_0$ non dimostra che $H_0$ sia vera.

**Tre cause di problemi nella stima.** Informazioni omesse dal modello (variabili omesse), causalità non chiara (inversa), errori di misura nei dati: tutte e tre rendono $X$ correlato con l'errore, cioè endogeno.

| Tipo di dato | Struttura |
|---|---|
| cross-section | molti soggetti in un solo periodo |
| serie storica | un solo soggetto in molti periodi; il tempo ne definisce l'ordine |
| panel | gli stessi soggetti in più periodi; con $N$ soggetti e $T$ periodi, senza dati mancanti, $N\times T$ osservazioni |

Se in ogni periodo compaiono soggetti diversi non è un panel, ma una sequenza di cross-section.

# Regressione lineare

## Modello ed effetto marginale

**Quando.** Si descrive la media condizionale di $Y$ con una funzione lineare nei parametri.

$$E[Y\mid X]=\alpha+\beta X\qquad\qquad E[Y\mid X_1,\dots,X_k]=\alpha+\beta_1X_1+\dots+\beta_kX_k$$

$$Y_i=E[Y\mid X_i]+\epsilon_i\qquad\Delta Y=\beta_j\,\Delta X_j\ \ (\text{le altre variabili costanti})$$

**Come si legge.** $\beta_j$ è la variazione attesa di $Y$ per un'unità in più di $X_j$, a parità delle altre variabili. È un effetto *causale* solo se $X_j$ è esogeno (capitolo Ipotesi OLS).

**Trappola.** $R^2$ alto e coefficiente significativo non dicono nulla sulla causalità.

## Stima OLS

**Quando.** Per ottenere i coefficienti: si minimizza la somma dei residui al quadrato.

$$\hat\beta=\frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(X)}\qquad\hat\alpha=\bar Y-\hat\beta\bar X\ \dagger\qquad\hat\epsilon_i=Y_i-\hat Y_i,\quad \hat Y_i=\hat\alpha+\hat\beta X_i$$

Caso multiplo, in forma matriciale:

$$\hat\beta=(\mathbf X'\mathbf X)^{-1}\mathbf X'\mathbf Y$$

**Frisch-Waugh-Lovell.** $\hat\beta_j$ si ottiene regredendo $Y$ sul residuo $\hat u_j$ di $X_j$ regredita sugli altri regressori:

$$\hat\beta_j=\frac{\sum_i\hat u_{j,i}\,Y_i}{\sum_i\hat u_{j,i}^2}$$

**Quando serve.** Per spiegare perché $\hat\beta_j$ misura l'effetto di $X_j$ «al netto» degli altri regressori. Si ottiene in tre passi: (1) regredire $X_1$ su $X_2$ e prendere i residui $u_1$; (2) regredire $Y$ su $X_2$ e prendere i residui $u_Y$; (3) regredire $u_Y$ su $u_1$. La pendenza del passo 3 coincide con $\hat\beta_1$ della regressione multipla.

## Stima dai momenti campionari (regressione semplice)

**Quando.** L'esercizio dà medie, varianze e covarianza campionarie e chiede la retta.

$$\hat\beta=\frac{s_{xy}}{s_x^2}=r_{xy}\,\frac{s_y}{s_x}\ \dagger\qquad\hat\alpha=\bar y-\hat\beta\,\bar x\qquad\hat y(x_0)=\hat\alpha+\hat\beta\,x_0$$

**Come si usa.** Il divisore ($n$ oppure $n-1$) è lo stesso in covarianza e varianza e si semplifica nel rapporto. La retta passa per il punto delle medie $(\bar x,\bar y)$. Il segno di $\hat\beta$ è quello della covarianza. Per $\Delta X$ unità in più, la variazione attesa di $Y$ è $\hat\beta\,\Delta X$.

**Pendenze invertite** ($\dagger$). Regredendo $x$ su $y$ invece di $y$ su $x$, $R^2$ e $t$ restano uguali (la correlazione è simmetrica), le pendenze cambiano e il loro prodotto è $R^2=r_{xy}^2$. Una correlazione non dice quale variabile sia la causa.

## Bontà di adattamento e lettura della tabella ANOVA

**Scomposizione della devianza.**

$$SST=\sum_i(y_i-\bar y)^2=SSE+SSR\qquad SSE=\sum_i(\hat y_i-\bar y)^2\qquad SSR=\sum_i(y_i-\hat y_i)^2$$

$$R^2=\mathrm{Corr}^2(Y,\hat Y)=\frac{SSE}{SST}=1-\frac{SSR}{SST}\qquad \bar R^2=1-(1-R^2)\frac{n-1}{n-k-1}\ \dagger$$

Qui $SSE$ è la devianza spiegata (nell'output $SS_{model}$) e $SSR$ quella residua ($SS_{res}$). Nella regressione semplice $R^2=r_{xy}^2$ e la correlazione ha il segno di $\hat\beta$. $R^2$ dice quanta variabilità di $y$ è spiegata da $x$: un $R^2$ basso non dice che la pendenza sia nulla.

| Cella dell'output | Come si ricava |
|---|---|
| $df$ residui | $n-k-1$ |
| $df$ totali | $n-1$ |
| $MS$ | $SS/df$ |
| Root MSE | $\hat\sigma=\sqrt{MS_{res}}$ |
| $F(k,\,n-k-1)$ | $MS_{model}/MS_{res}$ |
| $\bar R^2$ | $1-MS_{res}/MS_{total}$ ($\dagger$) |

**Trappola.** $R^2$ non decresce mai aggiungendo regressori, per questo si guarda anche $\bar R^2$. Un $R^2$ basso non esclude una relazione causale plausibile.

# Ipotesi OLS e proprietà dello stimatore

**Quando.** Domande del tipo «OLS dà una stima affidabile?», «quale ipotesi è violata?».

Le ipotesi:

1. **Linearità**: $E[Y\mid X]=\alpha+\beta_1X_1+\dots+\beta_kX_k$ (lineare nei parametri, non necessariamente nelle variabili).
2. **Esogeneità**: $E[\epsilon\mid X]=0$, da cui $\mathrm{Cov}(X_j,\epsilon)=0$. È l'ipotesi cruciale: senza, niente funziona.
3. **I.I.D.**: le osservazioni $(X_i,Y_i)$ sono indipendenti e identicamente distribuite.
4. **Momenti quarti finiti** (serve per CLT e legge dei grandi numeri).
5. **Omoschedasticità**: $\mathrm{Var}(\epsilon\mid X)=\sigma^2$.
6. **Assenza di perfetta collinearità** (regressione multipla).

| Proprietà | Condizione |
|---|---|
| $\hat\beta$ non distorto | ipotesi 1-2 |
| $\hat\beta$ consistente | ipotesi 1-4 |
| $\hat\beta$ **BLUE** (Gauss-Markov) | tutte, in particolare omoschedasticità |
| $\hat\beta$ normale, $t$ valida | normalità di $\epsilon$ (esatta) oppure CLT con $n$ grande (asintotica) |

$$\hat\beta=\beta+\sum_i\omega_i\epsilon_i,\quad \omega_i=\frac{X_i-\bar X}{\sum_i(X_i-\bar X)^2}\qquad\mathrm{Var}(\hat\beta\mid X)=\frac{\sigma^2}{\sum_i(X_i-\bar X)^2}$$

**Trappola.** Violare l'esogeneità rende $\hat\beta$ distorto *e* non consistente. Violare l'omoschedasticità lascia $\hat\beta$ non distorto e consistente ma fa perdere BLUE e rende sbagliati gli standard error. $E[\epsilon\mid X]=0$ implica $\mathrm{Cov}(X,\epsilon)=0$, non il contrario.

# Inferenza su un coefficiente

**Quando.** Per dire se $X_j$ ha un effetto, o se $\beta_j$ vale un certo numero $\kappa$.

$$\hat\sigma^2=\frac{\sum_i\hat\epsilon_i^2}{n-k-1}\quad(n-2\text{ nel caso semplice})\qquad \hat\sigma_{\hat\beta}=\sqrt{\frac{\hat\sigma^2}{\sum_i(X_i-\bar X)^2}}$$

$$\hat\sigma_{\hat\beta_j}=\sqrt{\frac{\hat\sigma^2}{\sum_i(X_{ij}-\bar X_j)^2\,(1-R_j^2)}}\qquad(R_j^2:\ X_j\text{ regredita sugli altri regressori})$$

$$t=\frac{\hat\beta_j-\kappa}{\hat\sigma_{\hat\beta_j}}\sim t_{n-k-1}\ \ (\text{asintoticamente }N(0,1))\qquad \text{IC}_{95\%}=\hat\beta_j\pm1{,}96\,\hat\sigma_{\hat\beta_j}$$

**Come si decide.**

| Alternativa $H_1$ | p-value | Si rifiuta $H_0$ se |
|---|---|---|
| $\beta\neq\kappa$ | $2\,P(t>\lvert t^{obs}\rvert)$ | $\lvert t^{obs}\rvert>1{,}96$ o p-value $<\alpha$ |
| $\beta>\kappa$ | $P(t>t^{obs})$ | $t^{obs}>1{,}64$ ($\dagger$, 5%) o p-value $<\alpha$ |
| $\beta<\kappa$ | $P(t<t^{obs})$ | $t^{obs}<-1{,}64$ ($\dagger$) o p-value $<\alpha$ |

Con l'IC: si rifiuta $H_0:\beta=\kappa$ al 5% se $\kappa$ **non** sta nell'IC al 95%.

**Ricostruire una cella dell'output.**

$$t=\frac{\text{Coef.}}{\text{Std. Err.}}\qquad\text{Std. Err.}=\frac{\text{Coef.}}{t}\qquad \text{IC}=\text{Coef.}\pm1{,}96\times\text{Std. Err.}$$

**Trappola.** Il «95%» riguarda la procedura (su campioni ripetuti il 95% degli intervalli contiene $\beta$), non la probabilità che $\beta$ cada in *questo* intervallo. Il p-value dell'output è bilaterale: per un'alternativa unilaterale con il segno giusto va dimezzato.

**Errore standard dell'intercetta e t dalla correlazione.**

$$\hat\sigma_{\hat\alpha}=\sqrt{\frac{\hat\sigma^2\,\frac1n\sum_iX_i^2}{\sum_i(X_i-\bar X)^2}},\quad\sum_iX_i^2=\sum_i(X_i-\bar X)^2+n\bar X^2\qquad t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}\ \dagger$$

La seconda formula vale nella regressione semplice per $H_0:\beta=0$: $t$ e $R^2=r^2$ dipendono dai dati solo tramite la correlazione campionaria $r$. Nel test $F$ della regressione semplice, $F=\dfrac{SSE/1}{SSR/(n-2)}=t^2$.

## Come scrivere $H_0$ e $H_1$ da un'affermazione del testo

**Quando.** Il testo dice «$X$ vale almeno…», «una presenza in più fa crescere il salario di più del…», «un anno vale 500 euro».

1. **Esprimere l'affermazione sul coefficiente**, nelle unità del modello (vedi le conversioni sotto).
2. **Scegliere la forma.** Un'uguaglianza («vale», «è pari a») dà $H_0:\beta=\kappa$ contro $H_1:\beta\neq\kappa$. Una disuguaglianza **larga** («almeno», «non meno di») è l'ipotesi nulla: $H_0:\beta\ge\kappa$ contro $H_1:\beta<\kappa$. Una disuguaglianza **stretta** («più di», «meno di») è l'ipotesi che si vuole affermare, cioè $H_1$: «più di» dà $H_0:\beta\le\kappa$ contro $H_1:\beta>\kappa$, «meno di» dà $H_0:\beta\ge\kappa$ contro $H_1:\beta<\kappa$.
3. **Statistica** $t=(\hat\beta-\kappa)/\hat\sigma_{\hat\beta}$ e regola della tabella sopra (a una coda: soglia $1{,}64$).
4. **Conclusione.** Si può affermare $H_1$ solo se $H_0$ è rifiutata: una stima puntuale oltre la soglia non basta. Se $H_0$ non è rifiutata, l'affermazione è compatibile con i dati, non dimostrata.

**Conversioni nelle unità del modello.**

| Affermazione | Coefficiente |
|---|---|
| $\Delta X$ anni in più valgono $c$ euro (modello lineare) | $\beta=c/\Delta X$ |
| con $Y$ in log: $\Delta x$ unità fanno variare $Y$ del $p\%$ | $\beta=p/(100\,\Delta x)$ |
| con $Y$ in log: «perdere il $c\%$» con $\Delta x$ unità | $\beta=-c/(100\,\Delta x)$ |
| multiplo di un coefficiente, $H_0:k\beta=q$ | $t=(k\hat\beta-q)/(k\,\hat\sigma_{\hat\beta})$ |
| effetto di $\Delta x$ unità, IC al 95% | $\Delta x\,\big(\hat\beta\pm1{,}96\,\hat\sigma_{\hat\beta}\big)$ (e $\times100$ se è una variazione percentuale) |

**Differenza di due stime da campioni indipendenti** (per esempio lo stesso modello su Nord e Sud). La covarianza è nulla:

$$\mathrm{se}(\hat\beta_N-\hat\beta_S)=\sqrt{\mathrm{se}_N^2+\mathrm{se}_S^2}<\mathrm{se}_N+\mathrm{se}_S$$

L'IC della differenza è $(\hat\beta_N-\hat\beta_S)\pm1{,}96\,\mathrm{se}$; è significativa al 5% se lo zero ne sta fuori.

**Test CAPM †.** Nel modello $r_t-r_f=\alpha+\beta(r_{mt}-r_f)+\epsilon_t$: $\beta<1$ indica un titolo meno rischioso del mercato, $\beta>1$ amplifica i suoi movimenti. $H_0:\alpha=0$ (Jensen) si verifica con la $t$ di $\hat\alpha$: se si rifiuta il CAPM è confutato, se non si rifiuta è compatibile con i dati ma non dimostrato; $H_0:\beta=1$ con $t=(\hat\beta-1)/\hat\sigma_{\hat\beta}$.

$$\mathrm{Var}(R_t)=\beta^2\,\mathrm{Var}(R_{mt})+\sigma^2\qquad R^2=\frac{\hat\beta^2\hat\sigma_M^2}{\hat\sigma_i^2}\qquad\beta=\frac{\mathrm{Cov}(R_t,R_{mt})}{\mathrm{Var}(R_{mt})}$$

Il primo termine è il rischio sistematico, $\sigma^2$ quello idiosincratico (stimato con $\hat\sigma=\sqrt{SSR/(n-2)}$). $R^2$ è la quota di rischio sistematico sul rischio totale.

# Inferenza su più coefficienti: il test F

**Quando.** Per un'ipotesi che coinvolge **più restrizioni insieme**: significatività congiunta ($\beta_1=\beta_2=\beta_3=0$), uguaglianza di coefficienti ($\beta_6=\beta_8$), esclusione di un gruppo di variabili.

Si stimano il modello **completo** (non vincolato) e il modello **ristretto** (con l'ipotesi nulla imposta).

$$F_{s;\,n-k-1}=\frac{(R_c^2-R_r^2)/s}{(1-R_c^2)/(n-k-1)}\qquad F=\frac{(SS_{res,r}-SS_{res,c})/s}{SS_{res,c}/(n-k-1)}\ \dagger$$

La seconda forma serve quando i due modelli hanno variabili dipendenti diverse. Per la significatività congiunta di tutti i regressori il modello ristretto è $Y=\alpha+\epsilon$, quindi $R_r^2=0$:

$$F=\frac{R^2/k}{(1-R^2)/(n-k-1)}$$

**Come si decide.** $F$ è sempre $\ge0$ e il test è **unilaterale destro**: si rifiuta $H_0$ solo se $F^{obs}$ è grande, cioè se $F^{obs}>$ valore critico oppure p-value $=P(F>F^{obs})<\alpha$. Non si divide $\alpha$ per 2. Esempio di tavola: $F_{3,60}$ al 5% vale $2{,}76$.

**Numero di vincoli $s$.** È il numero di uguaglianze scritte in $H_0$ (3 per $\beta_1=\beta_2=\beta_3=0$; 1 per $\beta_6-\beta_8=0$).

**Combinazione lineare.** Per $H_0:\beta_a-\beta_b=0$ si può usare la $t$:

$$t=\frac{\hat\beta_a-\hat\beta_b}{\mathrm{se}(\hat\beta_a-\hat\beta_b)}\qquad \mathrm{Var}(\hat\beta_a-\hat\beta_b)=\mathrm{Var}(\hat\beta_a)+\mathrm{Var}(\hat\beta_b)-2\,\mathrm{Cov}(\hat\beta_a,\hat\beta_b)$$

La covarianza non compare nell'output, quindi di solito si usa il test $F$ con $s=1$ (oppure si riparametrizza il modello, oppure la covarianza è data dal testo). Con $s=1$ vale $F=t^2$ ($\dagger$).

**Combinazione lineare in generale** ($\theta=\sum_iw_i\beta_i$, per esempio la differenza attesa fra due profili o l'effetto marginale in un punto):

$$\hat\theta=\sum_iw_i\hat\beta_i\qquad\widehat{\mathrm{Var}}(\hat\theta)=\sum_iw_i^2\,\widehat{\mathrm{Var}}(\hat\beta_i)+2\sum_{i<j}w_iw_j\,\widehat{\mathrm{Cov}}(\hat\beta_i,\hat\beta_j)\qquad t=\frac{\hat\theta-q}{\sqrt{\widehat{\mathrm{Var}}(\hat\theta)}}$$

Come si impostano: **(1)** scrivere le due medie condizionali e sottrarle (la costante e i termini uguali si elidono): il risultato è la combinazione, con i pesi $w_i$; **(2)** stima puntuale; **(3)** varianza con la formula, usando varianze e covarianze della tabella o del testo; **(4)** $t$ contro $1{,}96$ oppure IC $\hat\theta\pm1{,}96\,\mathrm{se}$. Con due soli termini: $\mathrm{Var}(\hat\beta_1+\hat\beta_2)=\mathrm{Var}(\hat\beta_1)+\mathrm{Var}(\hat\beta_2)+2\,\mathrm{Cov}(\hat\beta_1,\hat\beta_2)$.

**Come si costruisce il modello ristretto.** Si impone $H_0$ nel modello completo e si riscrive. Con $\beta_2=\beta_1$ e $\beta_3=0$ il termine $\beta_1X_1+\beta_2X_2+\beta_3X_3$ diventa $\beta_1(X_1+X_2)$ e $X_3$ sparisce. Con un solo vincolo lineare $\beta_1=\beta_2$, $F=t^2$ con $t=(\hat\beta_1-\hat\beta_2)/\mathrm{se}$.

**Modello senza costante.** Se il modello completo non ha la costante, o i due modelli non la hanno entrambi, l'$R^2$ non è calcolato rispetto alla media e non è confrontabile: si usano le **SSR**,

$$F=\frac{(SSR_r-SSR_c)/s}{SSR_c/(n-p)}\qquad(p=\text{numero di parametri del modello completo})$$

**Relazione con il chi-quadro.** Con $n$ grande $s\,F\approx\chi^2_s$ (le slide scrivono $F\approx\chi^2_s$, valido per $s=1$).

**Perché non basta una sequenza di test $t$.** Con tre test al 5% separati la probabilità di non rifiutare mai, sotto $H_0$, è $0{,}95^3=0{,}857$ e quella di rifiutare almeno una volta è $1-0{,}857=14{,}3\%\neq5\%$. In più i regressori sono correlati, e un test $t$ non vede l'effetto congiunto.

**Trappola.** Un $F$ congiunto significativo con tutte le $t$ singole non significative segnala di solito collinearità (capitolo Collinearità).

# Forme funzionali †

**Quando.** Il modello ha logaritmi, dummy, quadrati o interazioni, e la domanda chiede «di quanto cambia $Y$».

| Modello | Interpretazione di $\beta_1$ |
|---|---|
| lin-lin $Y=\beta_0+\beta_1X$ | $\Delta Y=\beta_1\Delta X$ |
| log-lin $\log Y=\beta_0+\beta_1X$ | $\%\Delta Y\approx100\,\beta_1\Delta X$; esatto $100\,(e^{\beta_1\Delta X}-1)$ |
| log-log $\log Y=\beta_0+\beta_1\log X$ | elasticità: $\%\Delta Y\approx\beta_1\,\%\Delta X$ |
| lin-log $Y=\beta_0+\beta_1\log X$ | $\Delta Y\approx(\beta_1/100)\,\%\Delta X$ |
| quadratica $Y=\beta_0+\beta_1X+\beta_2X^2$ | $\partial Y/\partial X=\beta_1+2\beta_2X$; punto di svolta $X^*=-\beta_1/(2\beta_2)$ |
| interazione $Y=\dots+\beta_1X_1+\beta_2X_2+\beta_3X_1X_2$ | $\partial Y/\partial X_1=\beta_1+\beta_3X_2$ |
| dummy $D$ in un modello log | $\%\Delta Y\approx100\,\beta_D$; esatto $100\,(e^{\beta_D}-1)$ |

**Dummy.** Con $g$ categorie mutuamente esclusive e la costante si includono $g-1$ dummy: la categoria omessa è il **gruppo di riferimento** e ogni coefficiente è lo scostamento della media del proprio gruppo da quello, a parità del resto. La differenza fra due gruppi inclusi è la differenza dei coefficienti ($\beta_6-\beta_8$); invertendo il confronto il segno cambia.

**Cambiare la categoria di riferimento.** Il modello non cambia (stesse SSR, stessi valori stimati), cambia solo la lettura. Con la costante e le dummy nord e sud (riferimento: centro) le medie sono $\alpha$, $\alpha+\delta_1$, $\alpha+\delta_2$. Con il sud come riferimento e le dummy centro e nord:

$$\alpha'=\alpha+\delta_2\qquad\delta_1'=-\delta_2\qquad\delta_2'=\delta_1-\delta_2$$

Il test $F$ sull'irrilevanza del fattore (che confronta con un modello senza dummy) non dipende dal riferimento. Senza costante e con $G$ dummy che sommano a 1, ogni $\delta_j$ è il **livello** del gruppo $j$ e nessuna dummy va eliminata. La rilevanza del fattore è $H_0:\delta_1=\dots=\delta_G$, cioè $G-1$ restrizioni indipendenti. Per un fattore con $g$ categorie e la costante: $H_0:\delta_1=\dots=\delta_{g-1}=0$, $s=g-1$.

## Effetti, interazioni e unità di misura

**Interazione con una dummy.** Con $\beta_4(\text{donna}\times\text{istr})$: l'effetto di un anno di istruzione è $\beta_1$ per gli uomini e $\beta_1+\beta_4$ per le donne, in percentuale $100\times$ questi valori (dipendente in log). Dipende dal genere solo se $\beta_4\neq0$, che si verifica con $H_0:\beta_4=0$.

**Interazione fra due variabili.** L'effetto marginale è $\beta_1+\beta_3X_2$ e dipende dal livello di $X_2$. A $X_2=x_0$ è una combinazione lineare con errore standard

$$\mathrm{Var}(\hat\beta_1+x_0\hat\beta_3)=\mathrm{Var}(\hat\beta_1)+x_0^2\,\mathrm{Var}(\hat\beta_3)+2x_0\,\mathrm{Cov}(\hat\beta_1,\hat\beta_3)$$

Se una variabile compare **centrata** ($X_2-c$), l'effetto a $X_2=c$ è semplicemente $\beta_1$: il secondo termine si annulla.

**Quadratica.** Con $x$ e $x^2$ l'effetto marginale è $\beta_1+2\beta_2x$ (con $Y$ in log, in percentuale $100(\beta_1+2\beta_2x)$): decrescente se $\beta_2<0$, crescente se $\beta_2>0$. La non linearità si verifica con $H_0:\beta_2=0$. Si annulla in $x^*=-\beta_1/(2\beta_2)$: con $\beta_2<0$ è positivo prima e negativo dopo. Se $x^*$ cade fuori dal campo osservato, è un'estrapolazione. L'errore standard dell'effetto in $x_0$ è quello di una combinazione lineare:

$$\mathrm{Var}(\hat\beta_1+2x_0\hat\beta_2)=\mathrm{Var}(\hat\beta_1)+4x_0^2\,\mathrm{Var}(\hat\beta_2)+4x_0\,\mathrm{Cov}(\hat\beta_1,\hat\beta_2)$$

**Unità di misura e scala.** Prima di confrontare un'affermazione del testo con un coefficiente, portarla nelle unità del modello.

| Caso | Regola |
|---|---|
| $Y$ in log, regressore in livello | $\Delta Y/Y\approx\beta\,\Delta x$: è una variazione **relativa**. Per ottenere $\Delta x$ da una variazione relativa $p/100$: $\Delta x=(p/100)/\beta$. Per una dummy $\Delta x=1$ |
| $Y$ in log, importo in unità di $Y$ | $\Delta Y\approx\beta\,y_0\,\Delta x$ (moltiplicare per il livello di partenza $y_0$); un'affermazione in unità di $Y$ si divide per $y_0$ prima di confrontarla con $\beta$ |
| $Y$ in livello, regressore in log | $\Delta Y\approx\beta\,m/100$ per un aumento relativo del $m\%$ di $x$: è in unità di $Y$, **non** una percentuale di $Y$, e non dipende dal livello di partenza |
| $Y$ e $x$ in log | $\Delta Y/Y\approx\beta\,\Delta x/x$: un $m\%$ in più di $x$ fa variare $Y$ di $\beta m\%$. «$x$ aumenta del $m\%$ e $Y$ del $p\%$» equivale a un'elasticità $p/m$ |
| $x$ misurato in unità di $u$ dollari | $x^*$ del punto di svolta va moltiplicato per $u$ per averlo in dollari |
| punti percentuali e punti base | $1\ \text{punto base}=0{,}01$ punti percentuali: portare tutto alla stessa unità |

**Trappola.** Con coefficienti grandi l'approssimazione $100\beta$ è inutilizzabile: usare la forma esatta. Sulle serie, $100\,\Delta\log Y_t\approx100\,\Delta Y_t/Y_{t-1}$ è la variazione percentuale.

# Endogeneità: variabile omessa ed errore di misura

## Variabile omessa

**Quando.** Il modello corretto ha $X_2$ ma lo si stima senza.

$$\tilde\beta_1=\beta_1+\beta_2\,\frac{\mathrm{Cov}(X_1,X_2)}{\mathrm{Var}(X_1)}\qquad\text{distorsione}=\beta_2\,\frac{\mathrm{Cov}(X_1,X_2)}{\mathrm{Var}(X_1)}$$

**Come si decide.** Il segno della distorsione è il segno di $\beta_2$ per il segno di $\mathrm{Cov}(X_1,X_2)$. Non c'è distorsione se $\beta_2=0$ oppure se $X_1$ e $X_2$ sono incorrelati. La distorsione non sparisce con $n$ grande: $\hat\beta_1$ **non è consistente**.

**Confronto fra due stime nel campione** (modello completo con $X_1,X_2$ contro modello ristretto senza $X_2$). Nel campione vale un'identità esatta:

$$\tilde\beta_1=\hat\beta_1+\hat\beta_2\,\hat\delta_1\qquad(\hat\delta_1:\ \text{coefficiente di }X_1\text{ nella regressione di }X_2\text{ sui regressori inclusi})$$

La distorsione c'è soltanto se valgono **entrambe** le condizioni: $X_2$ conta ($\beta_2\neq0$) e $X_2$ è correlato con $X_1$ ($\delta_1\neq0$). Se ne manca una, omettere $X_2$ non distorce $\beta_1$. Per giudicarla si guarda quanto cambia la stima di $\beta_1$ aggiungendo $X_2$.

**Endogeneità nel modello semplice.** Se $\mathrm{Cov}(X,\epsilon)\neq0$:

$$\hat\beta\ \xrightarrow{p}\ \beta+\frac{\mathrm{Cov}(X,\epsilon)}{\mathrm{Var}(X)}$$

Aumentare $n$ restringe la distribuzione attorno al valore sbagliato: lo stimatore non è consistente.

## Errore di misura nel regressore

**Quando.** Si osserva $X^*=X+u$ invece di $X$, con $\mathrm{Cov}(X,u)=0$.

$$\hat\beta\ \xrightarrow{p}\ \beta\,\frac{\mathrm{Var}(X)}{\mathrm{Var}(X)+\mathrm{Var}(u)}$$

**Come si decide.** Il fattore è minore di 1: la stima è **attenuata** verso zero. Il termine d'errore del modello stimato contiene $-\beta u$ ed è correlato con $X^*$, quindi $X^*$ è endogeno:

$$Y=\alpha+\gamma X+\epsilon\ \Rightarrow\ Y=\alpha+\gamma X^*+\epsilon^*,\ \ \epsilon^*=\epsilon-\gamma u\qquad\mathrm{Cov}(X^*,\epsilon^*)=-\gamma\,\mathrm{Var}(u)\neq0$$

**Trappola.** L'errore di misura è un'endogeneità anche se $u$ ha media nulla e anche se la media campionaria resta corretta. La distorsione non è una fluttuazione campionaria e non scompare con $n$ grande: un campione più grande rende solo più precisa una stima sbagliata.

# Collinearità

**Perfetta collinearità.** Un regressore è combinazione lineare esatta degli altri: i coefficienti non sono identificabili e OLS non si calcola. Caso tipico, la **trappola della dummy**: costante più tutte le dummy di una variabile categorica. Si risolve togliendo una dummy (la categoria di riferimento) o la costante.

**Quasi-collinearità.** I coefficienti restano non distorti e consistenti, ma gli standard error si gonfiano.

$$\mathrm{VIF}_j=\frac{1}{1-R_j^2}\ \dagger\qquad\hat\sigma_{\hat\beta_j}=\sqrt{\frac{\hat\sigma^2}{\sum_i(X_{ij}-\bar X_j)^2}}\cdot\sqrt{\mathrm{VIF}_j}$$

**Come si legge.** $R_j^2$ alto significa $X_j$ ben spiegato dagli altri regressori: $\hat\sigma_{\hat\beta_j}$ cresce di $\sqrt{\mathrm{VIF}_j}$ (non di $\mathrm{VIF}_j$). Segni tipici: $F$ congiunto significativo, $t$ singole non significative, coefficienti instabili al variare del campione. Soglia pratica $\mathrm{VIF}>10$ ($\dagger$, convenzione).

**Diagnosi nei temi d'esame.** La quasi-collinearità spiega la non significatività di un coefficiente solo se il VIF **di quel** regressore è alto: si calcola $\mathrm{VIF}_j=1/(1-R_j^2)$ con l'$R^2$ della regressione di $X_j$ sugli altri regressori, oppure si confrontano gli errori standard fra due modelli (con e senza il regressore correlato). Rispetto ai regressori incorrelati ($R_j^2=0$, fattore 1) la **varianza** è moltiplicata per il VIF e l'**errore standard** per $\sqrt{\mathrm{VIF}_j}$ (per esempio $\mathrm{VIF}=4$ raddoppia l'errore standard). La quasi-collinearità non distorce gli stimatori: ne gonfia gli errori standard e abbassa le $t$. Omettere invece un regressore rilevante e correlato con uno incluso distorce (capitolo Endogeneità).

# Eteroschedasticità

**Quando.** La dispersione degli errori dipende da $X$: $\mathrm{Var}(\epsilon\mid X)=\sigma^2(X)$ al posto di $\sigma^2$.

**Conseguenze (risposta da dare).**

1. $\hat\beta$ resta non distorto e consistente.
2. $\hat\beta$ **non è più BLUE** (non è il più efficiente).
3. Gli standard error calcolati con la formula usuale sono **sbagliati**, quindi $t$, $F$, IC e p-value non sono validi.

**Diagnosi grafica.** Residui (o residui al quadrato) contro $\hat Y$ o contro $X$: con omoschedasticità si vede una fascia orizzontale di ampiezza costante attorno allo zero; una dispersione che cambia con il livello indica eteroschedasticità. Il grafico è solo indicativo: guarda una sola combinazione dei regressori ($\hat Y$). Se la varianza dipende da un regressore che pesa poco su $\hat Y$, il grafico sembra omogeneo ma Breusch-Pagan rifiuta.

**Varianza vera e varianza usuale** ($\sigma_i^2=\mathrm{Var}(\epsilon_i\mid x_i)$, modello semplice):

$$\mathrm{Var}(\hat\beta\mid X)=\frac{\sum_i(x_i-\bar x)^2\,\sigma_i^2}{\left[\sum_i(x_i-\bar x)^2\right]^2}\qquad\text{contro}\qquad\frac{\hat\sigma^2}{\sum_i(x_i-\bar x)^2}$$

La formula usuale non converge alla varianza vera nemmeno con $n$ grande: l'errore standard usuale può essere sistematicamente sotto o sopra quello vero, e i test che lo usano rifiutano troppo o troppo poco.

## Errori standard robusti (White, Huber-Eicker)

**Quando.** Rimedio di default: si tengono i coefficienti OLS e si correggono gli standard error. Nessuna ipotesi sulla forma dell'eteroschedasticità.

$$\widehat{\mathrm{Var}}(\hat\beta\mid X)=\frac{\sum_i(X_i-\bar X)^2\,\hat\epsilon_i^2}{\left[\sum_i(X_i-\bar X)^2\right]^2}\qquad \widehat{\mathrm{Var}}(\hat\beta_j\mid X)=\frac{\sum_i\hat r_{ij}^2\,\hat\epsilon_i^2}{\left[\sum_i\hat r_{ij}^2\right]^2}$$

($\hat r_{ij}$: residuo della regressione di $X_j$ sugli altri regressori.) In forma matriciale $\mathrm{Var}(\hat\beta\mid X)=(\mathbf X'\mathbf X)^{-1}\mathbf X'\Sigma\mathbf X(\mathbf X'\mathbf X)^{-1}$ con $\hat\sigma_i^2=\hat\epsilon_i^2$ sulla diagonale di $\Sigma$.

**Come si decide.** La $t$ robusta ha la stessa forma, cambia solo il denominatore: $t=(\hat\beta-\text{valore sotto }H_0)/\text{se robusto}$. I **coefficienti non cambiano**, cambiano errori standard, $t$, IC e p-value: si confrontano le due colonne di errori standard e si dice se la decisione cambia. Il software usa di solito la variante HC1, che moltiplica la varianza per $n/(n-k-1)$.

**Test $F$ robusto.** La $F$ usuale $\dfrac{(SSR_R-SSR_U)/q}{SSR_U/(n-k-1)}$ non è affidabile sotto eteroschedasticità. La versione robusta è una statistica di Wald, $F=\tfrac1q(R\hat\beta)'\big(R\hat V_{rob}R'\big)^{-1}(R\hat\beta)$, che non si calcola con le SSR: la fornisce il software e si confronta con lo stesso valore critico.

**Trappola.** Gli standard error robusti non rendono $\hat\beta$ BLUE e non correggono la distorsione di $\hat\beta$ (eteroschedasticità ed endogeneità sono questioni distinte: la prima riguarda $E[\epsilon^2\mid X]$, la seconda $E[\epsilon\mid X]$; un test di White che rifiuta non dice che $E[\epsilon\mid X]\neq0$). Con omoschedasticità danno quasi lo stesso risultato, quindi un grafico pulito non basta a escluderli. Se i residui grandi stanno dove $\hat r_{ij}^2$ è piccolo (osservazioni centrali del regressore), l'errore standard robusto è più piccolo di quello usuale.

## Test per l'eteroschedasticità

**Quando.** Per verificare formalmente se serve correggere. $H_0$ è l'omoschedasticità: i test **non accettano** $H_0$, al più la rifiutano.

Si stima il modello, si salvano i residui $\hat\epsilon$ e si regredisce $\hat\epsilon^2$ su una forma ausiliaria. Sia $R^2_{\hat\epsilon^2}$ l'$R^2$ della regressione ausiliaria.

| Test | Ausiliaria | Statistica | Distribuzione sotto $H_0$ |
|---|---|---|---|
| Breusch-Pagan ($F$) | $\hat\epsilon^2$ su $X_1,\dots,X_k$ | $F=\dfrac{R^2_{\hat\epsilon^2}/k}{(1-R^2_{\hat\epsilon^2})/(n-k-1)}$ | $F_{k,\,n-k-1}$ |
| Breusch-Pagan (LM) | idem | $T_{BP}=n\,R^2_{\hat\epsilon^2}$ | $\chi^2_k$ |
| White | $\hat\epsilon^2$ su regressori, **quadrati e interazioni** | $T_W=n\,R^2_{\hat\epsilon^2}$ | $\chi^2_{\#\text{vincoli}}$ |

$H_0:\delta_1=\dots=\delta_k=0$ nella relazione $\hat\epsilon^2=\delta_0+\delta_1X_1+\dots+\delta_kX_k+u$. Si rifiuta se la statistica è grande o il p-value è piccolo. Con $k=3$ l'ausiliaria di White ha 9 regressori (3 livelli, 3 quadrati, 3 interazioni), quindi $\chi^2_9$. Breusch-Pagan cerca una dipendenza lineare dai regressori, White anche non lineare: stessa $H_0$, alternative diverse, e due test possono dare esiti diversi. Se uno rifiuta, si usano errori standard robusti.

**Regressione ausiliaria su $\hat Y$.** Si stima $\hat\epsilon^2=a+b\,\hat Y+u$ e si verifica $H_0:b=0$ con $t=\hat b/\mathrm{se}(\hat b)$: se $\lvert t\rvert>1{,}96$ c'è eteroschedasticità. Il segno di $\hat b$ dà la direzione ($\hat b>0$: la varianza cresce con $\hat Y$) e la varianza stimata in $y_0$ è $\hat a+\hat b\,y_0$.

## WLS e FGLS

**Quando.** Si conosce (WLS) o si può stimare (FGLS) la forma della varianza, $\sigma_i^2=\sigma^2\tilde\sigma_i^2$. Si dividono tutte le variabili per $\tilde\sigma_i$ e si applica OLS: gli errori diventano omoschedastici e lo stimatore è BLUE.

FGLS, con $\epsilon^2=\sigma^2\exp\{\delta_0+\delta_1Z_1+\dots+\delta_mZ_m\}\,\nu$:

1. Regredire $Y$ su $X_1,\dots,X_k$ e salvare $\hat\epsilon$.
2. Calcolare $\log(\hat\epsilon^2)$.
3. Regredire $\log(\hat\epsilon^2)$ su $Z_1,\dots,Z_m$.
4. Calcolare $\hat g$ (valore predetto) e $\hat\sigma_i=\exp\{\hat g/2\}$.
5. Applicare WLS con pesi $1/\hat\sigma_i$.

**Scelta pratica.** Errori robusti se non si vuole specificare la forma della varianza; FGLS/WLS solo se la forma è credibile.

# Serie storiche: autocorrelazione e modelli

## Notazione

$$\Delta Y_t=Y_t-Y_{t-1}\qquad100\,\Delta\log Y_t\approx100\,\frac{\Delta Y_t}{Y_{t-1}}$$

La differenza prima, o il passaggio ai logaritmi, serve a togliere un trend stocastico o a stabilizzare la varianza.

## Autocorrelazione, ACF e PACF

$$\rho_j=\frac{\mathrm{Cov}(Y_t,Y_{t-j})}{\sqrt{\mathrm{Var}(Y_t)\,\mathrm{Var}(Y_{t-j})}}$$

**Come si legge il correlogramma.** Le bande tratteggiate sono $\pm1{,}96/\sqrt T$: un'autocorrelazione campionaria fuori banda è significativa al 5%. Sotto $H_0:\rho_j=0$ si ha $\sqrt T\,\hat\rho_j\to N(0,1)$. La **PACF** misura la dipendenza da $Y_{t-j}$ al netto dei ritardi intermedi.

**Test di Ljung-Box.** Quando si vuole testare congiuntamente $H_0:\rho_1=\dots=\rho_j=0$.

$$Q_{LB}(j)=T(T+2)\sum_{i=1}^{j}\frac{\hat\rho_i^2}{T-i}\ \sim\ \chi^2_j$$

Si rifiuta $H_0$ (c'è autocorrelazione) se $Q_{LB}$ è grande, cioè se il p-value è piccolo: test unilaterale destro. Nell'output una colonna di p-value tutti piccoli significa autocorrelazione fino a quel ritardo.

## Riconoscere il processo dalle firme

| Processo | ACF | PACF |
|---|---|---|
| White noise | tutta nulla | tutta nulla |
| MA($q$) | si annulla **dopo $q$ ritardi** | decade |
| AR($p$) | decade verso zero | si annulla **dopo $p$ ritardi** |
| Random walk | decade lentissimamente, vicino a 1 | un picco al primo ritardo |

**Come si legge.** L'ordine è il ritardo dopo il quale si annulla la funzione che si interrompe di colpo: l'ACF per un MA, la PACF per un AR. Un'ACF che rientra nella banda al crescere del ritardo è compatibile con la stazionarietà; un'ACF che resta vicina a 1 anche a ritardi alti, con una PACF a un solo picco vicino a 1 al ritardo 1, indica radice unitaria: si differenzia e il modello si identifica sulla serie differenziata.

**Residui di una relazione di lungo periodo.** Se l'ACF esce dalle bande $\pm1{,}96/\sqrt n$ solo nei primi ritardi e poi rientra, i residui sono stazionari (cointegrazione). Se scende lentissimamente con quasi tutti i ritardi fuori banda, hanno una radice unitaria (nessuna cointegrazione). Un $R^2$ alto e una $t$ molto grande non provano la cointegrazione: fra due serie integrate non cointegrate sono la norma (regressione spuria).

## White noise, MA, AR, ADL

$$\text{WN: }E[\epsilon_t]=0,\ E[\epsilon_t\epsilon_s]=\begin{cases}\sigma^2&t=s\\0&t\neq s\end{cases}$$

**MA(1)** $Y_t=\alpha+\epsilon_t+\theta\epsilon_{t-1}$:

$$E[Y_t]=\alpha\quad\mathrm{Var}(Y_t)=(1+\theta^2)\sigma^2\quad\mathrm{Cov}(Y_t,Y_{t-1})=\theta\sigma^2\quad\rho_1=\frac{\theta}{1+\theta^2}\ \dagger\quad\rho_j=0\ (j\ge2)$$

**MA($q$)**: $\mathrm{Var}(Y_t)=\sigma^2(1+\theta_1^2+\dots+\theta_q^2)$, autocorrelazioni nulle oltre $q$.

**Dal $\hat\rho_1$ al parametro $\theta$ ($\dagger$).** Uguagliando $\rho_1=\theta/(1+\theta^2)$ a $\hat\rho_1$ si ottiene $\hat\rho_1\theta^2-\theta+\hat\rho_1=0$, con soluzioni $\theta=\big(1\pm\sqrt{1-4\hat\rho_1^2}\big)/(2\hat\rho_1)$. Il loro prodotto è 1: una sola ha $\lvert\theta\rvert<1$ (quella invertibile). Servono $\lvert\hat\rho_1\rvert\le0{,}5$.

**AR(1)** $Y_t=\beta_0+\beta_1Y_{t-1}+\epsilon_t$, stazionario se $\lvert\beta_1\rvert<1$:

$$E[Y_t]=\frac{\beta_0}{1-\beta_1}\ \dagger\qquad\mathrm{Var}(Y_t)=\frac{\sigma^2}{1-\beta_1^2}\qquad\rho_s=\beta_1^s$$

**AR($p$)** e previsione a un passo: $\hat Y_{T+1\mid T}=\hat\beta_0+\hat\beta_1Y_T+\dots+\hat\beta_pY_{T-p+1}$.

**ADL($p,q$)**: $Y_t=\beta_0+\sum_{i=1}^p\beta_iY_{t-i}+\sum_{j=0}^q\delta_jX_{t-j}+\epsilon_t$. Quando si vuole un effetto causale con dinamica, non solo una previsione.

**Modello statico** $Y_t=\beta_0+\beta_1X_t+\epsilon_t$: relazione contemporanea, di lungo periodo; $\Delta Y_t=\beta_1\Delta X_t$.

## Esogeneità nei modelli dinamici

L'**esogeneità stretta non vale** in un AR: $E[\epsilon_tY_t]=E[\epsilon_t^2]\neq0$ con $Y_t$ regressore al passo successivo. Quindi OLS è in generale **distorto in campioni finiti**, ma resta **consistente** se la serie è stazionaria e l'errore non è autocorrelato.

**Trappola.** Con dipendente ritardata *e* errore autocorrelato ($\epsilon_t=\rho\epsilon_{t-1}+\upsilon_t$, $\rho\neq0$), $Y_{t-1}$ è correlato con $\epsilon_t$ e OLS **non è consistente**.

## Stazionarietà debole

Media costante $E[Y_t]=\mu$, varianza costante $\mathrm{Var}(Y_t)=\sigma^2$, covarianza che dipende solo dalla distanza $\mathrm{Cov}(Y_s,Y_t)=\gamma_{t-s}$. Nei modelli dinamici sostituisce l'ipotesi I.I.D. e permette ancora CLT e legge dei grandi numeri.

# Break strutturali

**Quando.** Si sospetta che i parametri cambino nel tempo (crisi, riforma).

## Chow: data $\tau$ nota

Si crea $D_t(\tau)=0$ se $t\le\tau$, $1$ se $t>\tau$ e si interagisce con **intercetta e regressori**. Per un ADL(1,1):

$$Y_t=\beta_0+\beta_1Y_{t-1}+\delta_0X_t+\delta_1X_{t-1}+\gamma_0D_t+\gamma_1D_tY_{t-1}+\gamma_2D_tX_t+\gamma_3D_tX_{t-1}+\epsilon_t$$

$H_0:\gamma_0=\gamma_1=\gamma_2=\gamma_3=0$ (nessun break). Si usa un test $F$ con tanti vincoli quanti sono i $\gamma$. Dopo $\tau$ i parametri sono $\beta_0+\gamma_0$, $\beta_1+\gamma_1$, ecc.

**Chow con le SSR.** Il modello vincolato è quello sull'intero campione, il non vincolato è la coppia dei modelli sui due sottocampioni:

$$F=\frac{(SSR_1-SSR_2-SSR_3)/k}{(SSR_2+SSR_3)/(T-2k)}\ \sim\ F(k,\,T-2k)$$

Il modello 1 è sull'intero campione, i modelli 2 e 3 sui due sottocampioni, e $k$ è il numero di parametri del modello (costante e pendenza: $k=2$, quindi numeratore diviso 2 e $T-4$ gradi di libertà al denominatore). Si rifiuta $H_0$ (parametri uguali nei due sottocampioni) se $F$ supera il valore critico.

## QLR: data ignota

$$QLR=\max\{F(\tau_0),\dots,F(\tau_1)\}$$

Si calcola il test di Chow per ogni data candidata e si prende il massimo, escludendo il **15%** iniziale e finale del campione. La distribuzione **non è una $F$**: si usano valori critici propri, più alti. Esempio del corso (titolo Exelon, 2 vincoli): valore critico al 5% pari a $5{,}86$; il massimo osservato è $F(2,115)=7{,}6702$, alla data 1998:04. Supera il valore critico: si rifiuta l'assenza di break e la data stimata del break è 1998:04.

**Come si decide.** Si rifiuta se $QLR>$ valore critico. In caso di rifiuto la data più plausibile è quella del massimo; poi si stima il modello nei due sottocampioni.

**Trappola.** Chow richiede $\tau$ scelto *prima* di guardare i dati. Se la data si sceglie guardando i dati, usare QLR. Un break può mascherare una relazione sull'intero campione: se la pendenza ha segni opposti nei due regimi, la stima sull'intero campione può risultare vicina a zero e non descrive nessuno dei due regimi. Se il QLR rifiuta, i break sono un problema per la regressione sull'intero campione.

# Non stazionarietà e radici unitarie

## Trend deterministico e stocastico

Una serie si scrive $Y_t=TD_t+Y_t^*$. Un **trend deterministico** si toglie con una retta. Un **trend stocastico** (random walk) si toglie differenziando.

$$\text{Random walk: }Y_t=Y_{t-1}+\epsilon_t=Y_0+\sum_{j=1}^{t}\epsilon_j\qquad\mathrm{Var}(Y_t)=t\sigma^2\ \dagger\ (\text{non stazionario})$$

$$\text{RW con drift: }Y_t=\delta+Y_{t-1}+\epsilon_t=Y_0+\delta t+\sum_{j=1}^t\epsilon_j$$

## Regressione spuria

**Quando.** Due serie indipendenti e non stazionarie, regredite una sull'altra in livelli.

**Cosa succede.** $\hat\beta_1$ non converge a 0 (converge a una variabile casuale non gaussiana), la $t$ ha una distribuzione lontana da $N(0,1)$ e rifiuta $H_0:\beta_1=0$ troppo spesso, l'$R^2$ converge a una variabile casuale non degenere che può essere alta. Le $t$ e gli $R^2$ non sono interpretabili. Si differenzia, oppure si verifica la cointegrazione (capitolo Cointegrazione).

## Test di Dickey-Fuller (DF)

**Quando.** Per verificare se una serie ha una radice unitaria (è un random walk) o è stazionaria.

$$Y_t=\beta_0+\beta_1Y_{t-1}+\epsilon_t\ \Longleftrightarrow\ \Delta Y_t=\beta_0+\delta Y_{t-1}+\epsilon_t,\quad\delta=\beta_1-1$$

$$H_0:\delta=0\ \text{(radice unitaria)}\qquad H_1:\delta<0\ \text{(stazionaria)}\qquad t=\frac{\hat\delta}{\hat\sigma_{\hat\delta}}$$

**Come si decide.** Test **unilaterale sinistro** con distribuzione **non standard** (mai $\pm1{,}96$): si rifiuta $H_0$ se $t$ è molto negativa, cioè se il p-value è piccolo. Rifiutare significa **stazionarietà**. Valori critici di tavola al 5% ($\dagger$): senza costante circa $-1{,}95$, con costante circa $-2{,}86$, con costante e trend circa $-3{,}41$. In esame di norma si usa il p-value dell'output.

## Test aumentato (ADF)

**Quando.** Gli errori sono autocorrelati, quindi il DF semplice non è valido. Si aggiungono ritardi delle differenze.

$$\Delta Y_t=\beta_0^*+\delta Y_{t-1}+\beta_1^*\Delta Y_{t-1}+\dots+\beta_{p-1}^*\Delta Y_{t-p+1}+\epsilon_t,\qquad\delta=\beta_1+\dots+\beta_p-1$$

$H_0:\delta=0$ contro $H_1:\delta<0$, stessa regola del DF. Con trend deterministico si aggiunge $\alpha_1t$ (e al limite $\alpha_2t^2$): cambia la distribuzione, non la logica.

**Dall'AR($p$) alla regressione ADF.** Per un AR(3) $y_t=\beta_0+\beta_1y_{t-1}+\beta_2y_{t-2}+\beta_3y_{t-3}+\epsilon_t$, sottraendo $y_{t-1}$:

$$\Delta y_t=\beta_0+\delta\,y_{t-1}+\psi_1\Delta y_{t-1}+\psi_2\Delta y_{t-2}+\epsilon_t,\quad\delta=\beta_1+\beta_2+\beta_3-1,\ \ \psi_1=-(\beta_2+\beta_3),\ \ \psi_2=-\beta_3$$

La regressione aumentata di un AR($p$) ha $p-1$ ritardi della differenza. **Lettura dell'output:** la statistica del test è il rapporto $t$ della **sola riga di $y_{t-1}$**, non quelle degli altri regressori; si confronta con il valore critico dato dal testo (coda sinistra): si rifiuta se $t$ è minore, oppure se il p-value è minore di $0{,}05$. Il valore critico dipende dalla specificazione ed è più negativo con il trend. Omettere un trend che c'è sposta la statistica verso lo zero e fa non rifiutare la radice unitaria.

**Quale versione.** Serie senza andamento tendenziale: solo costante. Serie con trend lineare: costante **e** trend (sotto $H_0$ è un random walk con drift, sotto $H_1$ una serie stazionaria attorno a una retta).

**Ordine di integrazione.** Si testa il livello; se non si rifiuta, si differenzia e si ripete il test sulla differenza: se è stazionaria, la serie è I(1). Una serie è integrata di ordine $d$ se servono $d$ differenze per renderla stazionaria. Se non si rifiuta $H_0$ la serie va trattata come non stazionaria, cioè differenziata.

**Trappola.** Non rifiutare $H_0$ non prova che la serie abbia una radice unitaria: lascia i dati compatibili con essa, e il test ha poca potenza. Se la serie è I(1), si lavora in differenze, oppure si controlla la cointegrazione.

# Cointegrazione e correzione dell'errore

## Definizione ed Engle-Granger

$Y_t$ e $X_t$ non stazionarie sono **cointegrate** se esiste $\theta$ tale che $\epsilon_t=Y_t-\theta X_t$ è stazionaria: le due serie condividono lo stesso trend stocastico e non si allontanano per sempre.

**Procedura (scheletro della risposta d'esame).**

1. ADF su $Y_t$ e su $X_t$: entrambe non stazionarie, cioè I(1) (non si rifiuta $H_0$).
2. Stima della relazione di lungo periodo $Y_t=\beta_0+\beta_1X_t+\epsilon_t$ (OLS o DOLS) e calcolo dei residui $\hat\epsilon_t=Y_t-\hat\theta X_t$.
3. Test di radice unitaria sui residui (statistica **CDF**). $H_0$: radice unitaria nei residui, cioè **nessuna cointegrazione**. Si rifiuta se il p-value è piccolo: **c'è cointegrazione**.

**Trappola.** La distribuzione della CDF è diversa da quella dei test DF classici e dipende dalla presenza dell'intercetta nella relazione di lungo periodo: si usa il p-value del software.

## Stima in livelli con variabili cointegrate

**Superconsistenza.** $\hat\beta_1$ converge a $\beta_1$ più in fretta del solito, quindi la **stima puntuale** è affidabile. Però la distribuzione di $\hat\beta_1$ **non è gaussiana** e la $t$ non è valida: **non si fa inferenza** con la OLS in livelli.

**DOLS (Stock-Watson).** Per fare inferenza si aggiungono anticipi e ritardi delle differenze di $X$:

$$Y_t=\beta_0+\beta_1X_t+\sum_{j=-\ell}^{\ell}\gamma_j\,\Delta X_{t+j}+\epsilon_t^*$$

Il parametro di interesse è $\beta_1$; gli altri termini eliminano l'effetto dell'autocorrelazione di $X$. I residui restano autocorrelati: si usano standard error **HAC (Newey-West)**, e con quelli la $t$ è $N(0,1)$.

## Modello a correzione dell'errore (ECM)

**Quando.** Per descrivere insieme la dinamica di breve periodo e il ritorno all'equilibrio di lungo periodo fra serie cointegrate.

Dall'ADL(1,1) $Y_t=\kappa+\alpha_1Y_{t-1}+\beta_0X_t+\beta_1X_{t-1}+\epsilon_t$:

$$\Delta Y_t=\beta_0\,\Delta X_t+(\alpha_1-1)\big(Y_{t-1}-a-bX_{t-1}\big)+\epsilon_t,\qquad a=\frac{\kappa}{1-\alpha_1},\ \ b=\frac{\beta_0+\beta_1}{1-\alpha_1}$$

| Elemento | Significato |
|---|---|
| $\beta_0$ | effetto di breve periodo di $\Delta X_t$ su $\Delta Y_t$ |
| $b$ | effetto di **lungo periodo** (moltiplicatore di lungo periodo) |
| $Y_{t-1}-a-bX_{t-1}$ | disequilibrio a $t-1$ |
| $\alpha_y=\alpha_1-1$ | coefficiente di **aggiustamento**: quota del disequilibrio corretta per periodo |

**Stima a due passi.** (1) Stimare la relazione di lungo periodo e salvare i residui $\hat u_t$. (2) Regredire $\Delta Y_t$ su $\Delta X_t$ e $\hat u_{t-1}$: i regressori sono stazionari, quindi la $t$ usuale è valida. Il coefficiente di $\hat u_{t-1}$ deve essere **negativo e significativo** (in modulo tra 0 e 1).

**Ritorno all'equilibrio.** Con $X$ costante e senza shock, un disequilibrio iniziale $z_{t-1}=Y_{t-1}-bX_{t-1}$ evolve così:

$$z_{t+j}=(1+\alpha_y)^{j+1}z_{t-1}\qquad \Delta Y_{t+j}=\alpha_y\,(1+\alpha_y)^{j}\,z_{t-1}$$

Esempio dal corso: $\hat\alpha_y=-0{,}0658$ significa che circa il 6,6% del disequilibrio viene assorbito ogni mese. Tempo per recuperare una quota $s$ del disequilibrio ($\dagger$): $h^*=\left\lceil\ln(1-s)/\ln(1+\alpha_y)\right\rceil$.

## ECM negli esercizi: come si scrive e come si legge

**Forma dei testi.** Con $\mathrm{ecm}_{t-1}=y_{t-1}-\hat\alpha-\hat\beta x_{t-1}$ (residuo ritardato della relazione di lungo periodo):

$$\Delta y_t=\gamma_0+\gamma_1\,\Delta x_t+\lambda\,\mathrm{ecm}_{t-1}+\epsilon_t\qquad(\lambda\ \text{stimato negativo})$$

$\lambda$ è il coefficiente $\alpha_y=\alpha_1-1$ delle pagine precedenti (non la convenzione $-\alpha$ del VECM). $\gamma_1$ è l'effetto di breve periodo.

**Quota del disequilibrio assorbita** (con $\Delta x=0$, shock e costante nulli, quindi $\Delta y_t=\lambda z_{t-1}$ e $z_t=(1+\lambda)z_{t-1}$, il primo periodo è $t$). Dopo $k$ periodi il disequilibrio residuo è $(1+\lambda)^kz_{t-1}$ e la quota assorbita è $1-(1+\lambda)^k$. Il minimo $k$ che assorbe almeno la quota $q$ soddisfa $(1+\lambda)^k\le1-q$:

$$k=\left\lceil\frac{\ln(1-q)}{\ln(1+\lambda)}\right\rceil\qquad(\text{entrambi i logaritmi sono negativi se }-1<\lambda<0)$$

**Direzione dell'aggiustamento.** La variazione attesa al periodo successivo è $E[\Delta y_{t+1}]=\gamma_0+\gamma_1\Delta x_{t+1}+\lambda\,\mathrm{ecm}_t$. Con $\lambda<0$ un disequilibrio **positivo** ($y$ sopra la relazione di lungo periodo) **riduce** la crescita attesa di $y$ rispetto al caso di equilibrio, un disequilibrio negativo la aumenta. La variazione può restare positiva se la componente di breve periodo $\gamma_1\Delta x_{t+1}$ è più grande in valore assoluto.

**Quando l'ECM è ben definito (bilanciato).** Tutti i termini devono essere stazionari: (1) $y$ e $x$ sono $I(1)$ (ADF non rifiuta sui livelli), così $\Delta y$ e $\Delta x$ sono stazionari; (2) sono cointegrate (Engle-Granger rifiuta), così $\mathrm{ecm}_{t-1}$ è stazionario; (3) $\hat\lambda$ è negativo e significativo ($t$ contro $1{,}96$), altrimenti non c'è un meccanismo che riporti il sistema all'equilibrio. Senza cointegrazione $\mathrm{ecm}_{t-1}$ ha una radice unitaria, il modello non è bilanciato e la $t$ di $\lambda$ non ha la distribuzione usuale: la sua significatività non è evidenza di correzione dell'errore.

**Residui dell'ECM.** Devono essere incorrelati. Se l'autocorrelazione è concentrata nei primi ritardi (ACF e PACF con il valore più alto al primo ritardo, fuori dalle bande $\pm1{,}96/\sqrt n$, e poi dentro), manca dinamica di breve periodo: si aggiungono ritardi di $\Delta y$ e di $\Delta x$. La relazione di lungo periodo va rivista solo se la cointegrazione non regge ($\hat\lambda$ non negativo e significativo, o Engle-Granger non rifiuta) o se l'ACF decade lentamente come in una radice unitaria. Con ACF e PACF nelle bande non serve ri-specificare.

**Relazione di lungo periodo ben definita.** Una regressione fra livelli ha senso solo se le variabili sono tutte stazionarie, oppure tutte $I(1)$ e cointegrate. Se $y$ è stazionaria e $x$ ha una radice unitaria, $y-\alpha-\beta x$ eredita la radice unitaria di $x$ per ogni $\beta\neq0$. Engle-Granger può rifiutare anche solo perché $y$ è già stazionaria: prima si classificano le serie con ADF, poi si legge il test sui residui. Si parla di cointegrazione se i p-value ADF delle serie sono maggiori di $0{,}05$ e quello di Engle-Granger è minore di $0{,}05$.

**Inferenza sul coefficiente di lungo periodo.** Con il DOLS e gli errori HAC, $t=(\hat\beta-\beta_0)/\mathrm{se}_{HAC}$ è approssimativamente normale standard (quantili normali). L'effetto atteso di una variazione $\Delta x$ è $\theta=\Delta x\cdot\beta$, stimato da $\Delta x\cdot\hat\beta$ con errore standard $\Delta x\cdot\mathrm{se}(\hat\beta)$ e intervallo al 95% $\Delta x\,\big(\hat\beta\pm1{,}96\,\mathrm{se}(\hat\beta)\big)$.

**Superconsistenza.** $\hat\beta$ converge più in fretta di $\sqrt T$. Raddoppiando $T$ la deviazione standard si riduce di un fattore vicino a $1/2$ con variabili cointegrate e vicino a $1/\sqrt2$ con variabili stazionarie. L'intervallo costruito con l'errore standard usuale ha però copertura inferiore a quella nominale, perché ignora l'autocorrelazione dei residui di lungo periodo: per questo serve il DOLS con errori HAC.

## VECM

Per due variabili entrambe corrette dal disequilibrio, con $\beta$ coefficiente di cointegrazione comune:

$$\Delta X_t=\delta_x-\alpha_x\,(Y_{t-1}-\beta X_{t-1})+\epsilon_{x,t}\qquad\Delta Y_t=\delta_y-\alpha_y\,(Y_{t-1}-\beta X_{t-1})+\epsilon_{y,t}$$

Qui il segno meno è già scritto fuori: $\alpha_y>0$ significa che $Y$ **corregge** il disequilibrio. Se $X$ non reagisce ($\alpha_x=0$, $\Delta X_t=\epsilon_{x,t}$), $Y$ si aggiusta da solo e il disequilibrio evolve come $(1-\alpha_y)^j$:

$$Y_t-\beta X_t=(1-\alpha_y)(Y_{t-1}-\beta X_{t-1})\qquad\Delta Y_{t+1}=-\alpha_y(1-\alpha_y)(Y_{t-1}-\beta X_{t-1})$$

**Come si decide.** Aggiustamento monotono se $0<\alpha_y<1$; oscillante se $1<\alpha_y<2$ ($\dagger$). Se $\alpha_y=0$ la variabile non corregge il disequilibrio.

**Trappola sul segno.** Nell'ECM il coefficiente è $\alpha_1-1<0$ e il fattore è $(1+\alpha_y)$; nel VECM scritto con $-\alpha_y$ il coefficiente è positivo e il fattore è $(1-\alpha_y)$. Controllare sempre come è scritta l'equazione.

# Prontuario: test, ipotesi nulla e regola di rifiuto

| Test | $H_0$ | Statistica | Si rifiuta $H_0$ se |
|---|---|---|---|
| $z$ o $t$ sulla media | $\mu=\mu_0$ | $(\bar y-\mu_0)/(s/\sqrt n)$ | $\lvert t\rvert>1{,}96$ (bilaterale), $1{,}64$ (una coda); $t_{n-1}$ se $n$ è piccolo |
| $z$ su una proporzione | $\pi=\pi_0$ | $(\hat\pi-\pi_0)/\sqrt{\pi_0(1-\pi_0)/n}$ | $\lvert z\rvert>1{,}96$, $1{,}64$ una coda |
| due medie indipendenti | $\mu_1=\mu_2$ | $(\bar y_1-\bar y_2)/\sqrt{s_1^2/n_1+s_2^2/n_2}$ | $\lvert t\rvert>1{,}96$ |
| dati appaiati | $\mu_d=0$ | $\bar d/(s_d/\sqrt n)$ | $\lvert t\rvert>1{,}96$ |
| $t$ su $\beta_j$ | $\beta_j=\kappa$ | $(\hat\beta_j-\kappa)/\hat\sigma_{\hat\beta_j}$ | $\lvert t\rvert>1{,}96$, p-value $<\alpha$ |
| $F$ su $s$ vincoli | le $s$ restrizioni valgono | $F_{s,\,n-k-1}$ | $F$ grande, p-value $<\alpha$ |
| $t$ robusta | come la $t$ | se robusto (White) | come la $t$ |
| Breusch-Pagan | omoschedasticità | $nR^2_{\hat\epsilon^2}\sim\chi^2_k$ | statistica grande |
| White | omoschedasticità | $nR^2_{\hat\epsilon^2}\sim\chi^2_{\#}$ | statistica grande |
| Autocorrelazione singola | $\rho_j=0$ | $\sqrt T\,\hat\rho_j\sim N(0,1)$ | $\lvert\sqrt T\hat\rho_j\rvert>1{,}96$ |
| Ljung-Box | $\rho_1=\dots=\rho_j=0$ | $Q_{LB}\sim\chi^2_j$ | $Q$ grande, p-value piccolo |
| Chow | $\gamma_0=\dots=0$ | $F$ sui $\gamma$, oppure da SSR: $F(k,T-2k)$ | $F$ grande, p-value piccolo |
| QLR | nessun break | $\max F$ | $>$ valore critico QLR (non $F$) |
| DF / ADF | $\delta=0$, radice unitaria | $t$ su $\delta$ | $t$ molto negativa (**sinistra**), distribuzione non standard |
| Engle-Granger (CDF) | nessuna cointegrazione | ADF sui residui | statistica molto negativa, p-value piccolo |
| $t$ sul coefficiente dell'ECM | $\alpha=0$, nessuna correzione | $t$ usuale | p-value $<\alpha$, con $\hat\alpha<0$ |
| $t$ su $\beta_1$ in DOLS | $\beta_1=\beta_1^0$ | $t$ con errori HAC | $\lvert t\rvert>1{,}96$ |

**Regole trasversali.**

1. Il test $F$ è unilaterale destro: non si divide $\alpha$ per 2.
2. I test di radice unitaria sono unilaterali **sinistri** e con tavole non standard.
3. Rifiutare in DF/ADF significa stazionarietà; rifiutare in Engle-Granger significa cointegrazione.
4. I test con $H_0$ = omoschedasticità o assenza di autocorrelazione non confermano $H_0$ quando non la rifiutano: mostrano solo che non c'è evidenza contro.
5. Con trend stocastico le $t$ usuali non sono confrontabili con $N(0,1)$.
6. Valori critici ricorrenti: $1{,}96$ (normale, 5% bilaterale), $1{,}64$ (normale, 5% unilaterale), $2{,}57$ (normale, 1% bilaterale; $2{,}58$ con più cifre), $\pm1{,}96/\sqrt T$ (bande dell'ACF).

# Dove le slide scrivono altro

La nota del corso corregge le slide in questi punti. L'esame segue le slide: ricordare entrambe le versioni.

| Argomento | Le slide | Versione corretta (usata sopra) |
|---|---|---|
| Esogeneità | da $\mathrm{Cov}(X,\epsilon)=0$ segue $E[\epsilon\mid X]=0$ | l'implicazione va nell'altro senso: $E[\epsilon\mid X]=0\Rightarrow\mathrm{Cov}=0$ |
| Teorema di Gauss-Markov | «il regressore non è correlato con l'errore» | serve $E[\epsilon\mid X]=0$ |
| Gradi di libertà, regressione multipla | $n-k$ | $n-k-1$ con $k$ regressori esclusa la costante (le slide valgono solo se $k$ conta anche l'intercetta) |
| Limite di $(n-1)\big/\sum_i(X_i-\bar X)^2$ | $1/\sigma^2$ | $1/\sigma_X^2$, varianza di $X$, non dell'errore |
| Varianza di MA(1) | $(1+\theta)\sigma^2$ | $(1+\theta^2)\sigma^2$ |
| $R^2$ della regressione spuria | tende a 1 | converge a un limite non degenere (Phillips 1986) |
| Parametro $\delta$ dell'ADF | $\delta=\beta_1-1$ | $\delta=\beta_1+\dots+\beta_p-1$ (vale come nelle slide solo per $p=1$) |
| Estremi del QLR | $F(1),\dots,F(T)$ | massimo su un intervallo che esclude il 15% iniziale e finale |
| Relazione $F$-chi-quadro | $F(k_1,k_2)\approx\chi^2_{k_1}$ | $F\approx\chi^2_{k_1}/k_1$ |
| Test $t$ in campioni finiti | denominatore $\sqrt{\mathrm{Var}(\hat\beta\mid X)}$ | errore standard stimato $\hat\sigma_{\hat\beta}$; con $\sigma^2$ noto la statistica sarebbe $N(0,1)$ |
| Ritorno all'equilibrio nell'ECM | disequilibrio a $t+j-1$ | il fattore $(1+\alpha_y)^j$ moltiplica il disequilibrio iniziale a $t-1$ |
| Aggiustamento oscillante nel VECM | etichetta del grafico non coerente con il modello | rapporto $1-\alpha_y=-0{,}5$ corrisponde a $\alpha_y=1{,}5$; con $\alpha_y=2$ l'oscillazione non si smorzerebbe |
| Nome dello stimatore robusto | «Huber-Heicker» | Eicker-Huber-White |
| Modello statico | «$X$ causerà $Y$» | OLS misura un'associazione, non prova il nesso causale |
