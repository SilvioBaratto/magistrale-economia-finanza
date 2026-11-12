<!-- ex e00_01 -->
# Esercizio 1 — Titolo di studio e opinione sullo smart working *(livello base)*

> [!abstract] Dati
> In un'azienda si sono intervistati dipendenti diplomati e laureati sulla possibilità di lavorare da casa (smart working). La tabella riporta il numero di intervistati per titolo di studio e opinione.
>
> {{e00_01.tab.cont}}
>
> Due variabili categoriche sono statisticamente indipendenti se la distribuzione condizionale dell'una è la stessa in ogni categoria dell'altra. Qui i dati si considerano incompatibili con l'indipendenza se, per almeno un'opinione, le percentuali dei due gruppi differiscono di più di ${{e00_01.soglia|m}}$ punti percentuali.

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Fra i laureati, quale percentuale è favorevole? **(b)** Fra i dipendenti favorevoli, quale percentuale è laureata? **(c)** Secondo il criterio indicato, titolo di studio e opinione risultano associati? Si risponda sì o no. **(d)** Se opinione e titolo di studio fossero statisticamente indipendenti, quanti laureati favorevoli ci si aspetterebbe, a parità di numerosità dei due gruppi e di totale dei favorevoli?
<!-- /ex -->

<!-- ex e00_02 -->
# Esercizio 2 — Ore di studio e voto: la covarianza *(livello base)*

> [!abstract] Dati
> Per $n = {{e00_02.n}}$ studenti si sono rilevati il numero $X$ di ore di studio settimanali e il voto $Y$ all'esame, in trentesimi.
>
> {{e00_02.tab.dati}}
>
> La covarianza campionaria è $s_{xy}=\dfrac{1}{n}\sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y)$, con divisore $n$. La covarianza di $X$ con se stessa si calcola con la stessa formula.

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** Quanto vale la covarianza campionaria $s_{xy}$? **(b)** Le ore vengono espresse in minuti, $X'={{e00_02.scala}}\,X$, e a ogni voto si aggiungono ${{e00_02.bonus}}$ punti, $Y'=Y+{{e00_02.bonus}}$. Quanto vale la covarianza campionaria fra $X'$ e $Y'$? **(c)** Quanto vale la covarianza campionaria di $X$ con $X$? **(d)** Ore di studio e voto tendono a muoversi nello stesso senso? Si risponda sì o no.
<!-- /ex -->

<!-- ex e00_03 -->
# Esercizio 3 — Il reddito di una famiglia: media e varianza di una somma *(livello base)*

> [!abstract] Dati
> Su un campione di famiglie si osservano il reddito mensile del marito $X$ e quello della moglie $Y$, in migliaia di euro. Il reddito della famiglia è $Z=X+Y$. Le statistiche descrittive sono nella tabella; la covarianza campionaria fra $X$ e $Y$ vale ${{e00_03.cov|m}}$. Varianze e covarianza usano lo stesso divisore.
>
> {{e00_03.tab.stat}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** **(a)** Quanto vale la media del reddito familiare $Z=X+Y$? **(b)** Quanto vale la varianza di $Z$? **(c)** Quanto vale il coefficiente di correlazione fra $X$ e $Y$? **(d)** Quanto vale la varianza di $X-Y$? **(e)** Se $X$ e $Y$ fossero indipendenti, la varianza di $Z$ sarebbe minore di quella ottenuta in (b)? Si risponda sì o no.
<!-- /ex -->

<!-- ex e00_04 -->
# Esercizio 4 — Rendimento di un fondo con leva *(livello base)*

> [!abstract] Dati
> Il rendimento mensile $X$ di un fondo, in punti percentuali, è una variabile casuale con la distribuzione seguente.
>
> {{e00_04.tab.distr}}
>
> Un investitore che prende a prestito parte del capitale ottiene il rendimento $Y={{e00_04.a}}\,X-{{e00_04.c}}$, dove ${{e00_04.c}}$ è un costo fisso.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** Quanto vale il valore atteso $E[X]$? **(b)** Quanto vale la varianza $\text{Var}(X)$? **(c)** Quanto vale $E[Y]$? **(d)** Quanto vale $\text{Var}(Y)$?
<!-- /ex -->

<!-- ex e00_05 -->
# Esercizio 5 — Tempo di attesa al pronto soccorso: intervalli di confidenza *(livello base)*

> [!abstract] Dati
> Un pronto soccorso rileva il tempo di attesa, in minuti, di un campione casuale semplice di pazienti. Il campione ha dato i risultati seguenti.
>
> {{e00_05.tab.stat}}
>
> Per la media $\mu$ si usa l'intervallo $\bar y\pm z\,s/\sqrt{n}$, con $z=1{,}96$ al 95\% e $z=2{,}57$ al 99\%.

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Quanto vale l'errore standard della media campionaria, $s/\sqrt{n}$? **(b)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per il tempo medio di attesa $\mu$? **(c)** E l'estremo superiore? **(d)** Quanto è ampio l'intervallo di confidenza al 99\% (differenza fra estremo superiore e inferiore)? **(e)** Il direttore sostiene che il tempo medio di attesa sia di ${{e00_05.mu0}}$ minuti. Al livello del 5\%, usando l'intervallo di confidenza al 95\%, si decida se rifiutare o non rifiutare $H_0:\mu={{e00_05.mu0}}$ contro $H_1:\mu\neq{{e00_05.mu0}}$. **(f)** Circa il 95\% dei singoli tempi di attesa dei pazienti cade nell'intervallo calcolato in (b)–(c)? Si risponda sì o no.
<!-- /ex -->

<!-- ex e00_06 -->
# Esercizio 6 — Peso delle confezioni: i tre test sulla media *(livello base)*

> [!abstract] Dati
> Un produttore dichiara che le sue confezioni di pasta pesano in media $\mu_0={{e00_06.mu0}}$ grammi. Un'associazione di consumatori pesa un campione casuale di confezioni e ottiene i risultati seguenti.
>
> {{e00_06.tab.stat}}
>
> La statistica test è $t=\dfrac{\bar y-\mu_0}{s/\sqrt{n}}$, approssimativamente $N(0,\,1)$ sotto $H_0:\mu=\mu_0$. Per il test contro $H_1:\mu<\mu_0$ il programma di calcolo riporta il p-value ${{e00_06.p_sx|m}}$.

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Quanto vale la statistica $t$? Nelle domande seguenti si usi il livello del 5\%, con valore critico $1{,}64$ per i test unilaterali e $1{,}96$ per quello bilaterale. **(b)** Si decida se rifiutare o non rifiutare $H_0$ contro $H_1:\mu<\mu_0$ (si rifiuta se $t<-1{,}64$). **(c)** Si decida se rifiutare o non rifiutare $H_0$ contro $H_1:\mu>\mu_0$ (si rifiuta se $t>1{,}64$). **(d)** Si decida se rifiutare o non rifiutare $H_0$ contro $H_1:\mu\neq\mu_0$ (si rifiuta se $|t|>1{,}96$). **(e)** Quanto vale il p-value del test bilaterale di (d)? **(f)** Il p-value di (e) è la probabilità che $H_0$ sia vera? Si risponda sì o no.
<!-- /ex -->

<!-- ex e00_07 -->
# Esercizio 7 — Il reddito medio di un campione casuale *(livello intermedio)*

> [!abstract] Dati
> In una popolazione il reddito annuo $Y$, in migliaia di euro, ha media $\mu={{e00_07.mu}}$ e deviazione standard $\sigma={{e00_07.sigma}}$; la distribuzione è asimmetrica, con una lunga coda a destra. Si estrae un campione casuale semplice di $n={{e00_07.n}}$ persone, $Y_1,\dots,Y_n$, e si indica con $\bar Y$ la media campionaria.

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Quanto vale $\text{Var}(Y_1+Y_2)$, con $Y_1$ e $Y_2$ le prime due osservazioni del campione? **(b)** $\bar Y$ è uno stimatore corretto di $\mu$, cioè $E[\bar Y]=\mu$? Si risponda sì o no. **(c)** Quanto vale l'errore standard di $\bar Y$? **(d)** Quale numerosità campionaria serve perché l'errore standard di $\bar Y$ sia ${{e00_07.obiettivo}}$? **(e)** Per il teorema del limite centrale $\bar Y$ è approssimativamente normale: quanto vale $c$ nell'intervallo $[\mu-c,\ \mu+c]$ che contiene $\bar Y$ con probabilità circa del 95\% (si usi $1{,}96$)? **(f)** Un campione di $n={{e00_07.n}}$ persone ha dato $\bar y={{e00_07.ybar|m}}$: cade nell'intervallo $[\mu-c,\ \mu+c]$? Si risponda sì o no.
<!-- /ex -->

<!-- ex e00_08 -->
# Esercizio 8 — Sondaggio: la maggioranza è favorevole? *(livello intermedio)*

> [!abstract] Dati
> In un sondaggio su un campione casuale di $n={{e00_08.n}}$ elettori, $x={{e00_08.x}}$ si dichiarano favorevoli a un provvedimento. Sia $\pi$ la proporzione di favorevoli nella popolazione e $\hat\pi=x/n$ la sua stima, che è la media di variabili di Bernoulli. L'errore standard stimato di $\hat\pi$ è $\sqrt{\hat\pi(1-\hat\pi)/n}$. Il campione è abbastanza grande per usare l'approssimazione normale.

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Quanto vale l'errore standard stimato di $\hat\pi$? **(b)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\pi$ (con $z=1{,}96$)? **(c)** E l'estremo superiore? Si vuole ora verificare, al livello del 5\%, se la maggioranza è favorevole: $H_0:\pi={{e00_08.pi0|m}}$ contro $H_1:\pi>{{e00_08.pi0|m}}$, con valore critico $1{,}64$. **(d)** Quanto vale l'errore standard di $\hat\pi$ calcolato sotto $H_0$, $\text{se}_0=\sqrt{\pi_0(1-\pi_0)/n}$? **(e)** Quanto vale la statistica $z=(\hat\pi-\pi_0)/\text{se}_0$? **(f)** Si decida se rifiutare o non rifiutare $H_0$.
<!-- /ex -->

<!-- ex e00_09 -->
# Esercizio 9 — Quattro misure: la distribuzione $t$ di Student *(livello intermedio)*

> [!abstract] Dati
> Una macchina dovrebbe riempire flaconi da $\mu_0={{e00_09.mu0|m}}$ ml. Si misura il contenuto di $n={{e00_09.n|m}}$ flaconi scelti a caso e si assume che il contenuto abbia distribuzione normale.
>
> {{e00_09.tab.dati}}
>
> Con un campione così piccolo la statistica $t=\dfrac{\bar y-\mu_0}{s/\sqrt{n}}$ segue una $t$ di Student con $n-1$ gradi di libertà. Il quantile della $t$ che lascia il 5\% complessivo nelle due code, per il numero di gradi di libertà di questo campione, vale ${{e00_09.qt|m}}$.

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Quanto vale la statistica $t$? **(b)** Quanti sono i gradi di libertà? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\mu=\mu_0$ contro $H_1:\mu\neq\mu_0$, con il valore critico della $t$ dato sopra. **(d)** Si decida se rifiutare o non rifiutare $H_0$ usando, impropriamente, il valore critico normale $1{,}96$. **(e)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\mu$ costruito con il quantile della $t$? **(f)** E l'estremo superiore?
<!-- /ex -->

<!-- ex e00_10 -->
# Esercizio 10 — Due servizi di assistenza: confronto fra medie *(livello intermedio)*

> [!abstract] Dati
> Un'azienda confronta il tempo di risposta, in secondi, di due servizi di assistenza, misurato su due campioni indipendenti di richieste.
>
> {{e00_10.tab.gruppi}}
>
> Siano $\mu_1$ e $\mu_2$ le medie dei due servizi. Lo stimatore della differenza è $\bar Y_1-\bar Y_2$, con $\text{Var}(\bar Y_1-\bar Y_2)=\text{Var}(\bar Y_1)+\text{Var}(\bar Y_2)-2\,\text{Cov}(\bar Y_1,\bar Y_2)$; i campioni sono indipendenti, quindi $\text{Cov}(\bar Y_1,\bar Y_2)=0$. L'intervallo di confidenza al 95\% di ciascuna media è $\bar y_i\pm1{,}96\,s_i/\sqrt{n_i}$.

> [!question] Testo della domanda
> **Domanda 10 *(3 punti)*.** **(a)** Quanto vale l'errore standard di $\bar Y_1-\bar Y_2$, cioè $\sqrt{s_1^2/n_1+s_2^2/n_2}$? **(b)** Quanto vale la statistica $t=(\bar y_1-\bar y_2)/\text{se}$? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\mu_1=\mu_2$ contro $H_1:\mu_1\neq\mu_2$ (valore critico $1{,}96$). **(d)** Gli intervalli di confidenza al 95\% delle due medie si sovrappongono? Si risponda sì o no. **(e)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\mu_1-\mu_2$? **(f)** E l'estremo superiore?
<!-- /ex -->

<!-- ex e00_11 -->
# Esercizio 11 — Due offerte promozionali: confronto fra proporzioni *(livello intermedio)*

> [!abstract] Dati
> Una banca propone due offerte, A e B, a due campioni indipendenti di clienti. La tabella riporta il numero di clienti e quanti hanno accettato.
>
> {{e00_11.tab.offerte}}
>
> Sia $\hat\pi_1=x_1/n_1$ la quota di accettazioni dell'offerta A e $\hat\pi_2=x_2/n_2$ quella di B. Per il test di $H_0:\pi_1=\pi_2$ i due campioni hanno, sotto $H_0$, la stessa proporzione, stimata con la proporzione combinata $\hat\pi=(x_1+x_2)/(n_1+n_2)$; l'errore standard sotto $H_0$ è $\text{se}_0=\sqrt{\hat\pi(1-\hat\pi)\,(1/n_1+1/n_2)}$ e la statistica è $z=(\hat\pi_1-\hat\pi_2)/\text{se}_0$. Per l'intervallo di confidenza della differenza, dove non si assume $H_0$, si usa $\text{se}=\sqrt{\hat\pi_1(1-\hat\pi_1)/n_1+\hat\pi_2(1-\hat\pi_2)/n_2}$.

> [!question] Testo della domanda
> **Domanda 11 *(3 punti)*.** **(a)** Quanto vale la proporzione combinata $\hat\pi$? **(b)** Quanto vale $\text{se}_0$? **(c)** Quanto vale la statistica $z$? **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\pi_1=\pi_2$ contro $H_1:\pi_1\neq\pi_2$ (valore critico $1{,}96$). **(e)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per $\pi_1-\pi_2$? **(f)** E l'estremo superiore?
<!-- /ex -->

<!-- ex e00_12 -->
# Esercizio 12 — Prima e dopo il corso: dati appaiati e covarianza *(livello appello)*

> [!abstract] Dati
> Per $n={{e00_12.n}}$ operai si è misurata la produttività (pezzi all'ora) prima e dopo un corso di formazione. Le due misure riguardano gli stessi operai (dati appaiati). Le statistiche descrittive sono nella tabella; la covarianza campionaria fra le due misure vale ${{e00_12.cov|m}}$. Varianze e covarianza usano lo stesso divisore, $n-1$.
>
> {{e00_12.tab.stat}}
>
> Sia $D=\text{dopo}-\text{prima}$, con media $\bar d=\bar y_{\text{dopo}}-\bar y_{\text{prima}}$ e varianza $s_d^2=s_{\text{dopo}}^2+s_{\text{prima}}^2-2\,s_{\text{dopo},\text{prima}}$. La statistica è $t=\bar d/(s_d/\sqrt{n})$, approssimativamente $N(0,\,1)$ perché $n$ è grande.

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** **(a)** Quanto vale $\bar d$? **(b)** Quanto vale il coefficiente di correlazione fra le due misure? **(c)** Quanto vale la deviazione standard $s_d$ delle differenze? **(d)** Quanto vale la statistica $t$? **(e)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\mu_D=0$ contro $H_1:\mu_D>0$ (il corso aumenta la produttività), con valore critico $1{,}64$. **(f)** Un collega tratta le due misure come campioni indipendenti, cioè pone la covarianza uguale a zero, e calcola la statistica $t$ con $s_d^2=s_{\text{dopo}}^2+s_{\text{prima}}^2$: quanto vale la sua $t$? **(g)** Con la statistica di (f), si decida se rifiutare o non rifiutare $H_0$ contro $H_1:\mu_D>0$ (valore critico $1{,}64$).
<!-- /ex -->

<!-- ex e00_13 -->
# Esercizio 13 — Errore e media condizionale: l'incorrelazione non basta *(livello appello)*

> [!abstract] Dati
> Si considera il modello $Y=\alpha+\beta X+\epsilon$ con $\alpha={{e00_13.alpha|m}}$ e $\beta={{e00_13.beta|m}}$ (valori veri). La variabile $X$ ha la distribuzione della tabella. Per l'errore $\epsilon$ si confrontano due modelli, P e Q, che differiscono solo per la media condizionale $E[\epsilon\mid X=x]$.
>
> {{e00_13.tab.distr}}
>
> Le medie condizionali permettono di calcolare $E[\epsilon]=\sum_x P(X=x)\,E[\epsilon\mid X=x]$ e $E[X\epsilon]=\sum_x x\,P(X=x)\,E[\epsilon\mid X=x]$; poi $\text{Cov}(X,\epsilon)=E[X\epsilon]-E[X]\,E[\epsilon]$. La pendenza della retta di regressione nella popolazione è $\text{Cov}(X,Y)/\text{Var}(X)$.

> [!question] Testo della domanda
> **Domanda 13 *(4 punti)*.** Nel modello P: **(a)** quanto vale $E[\epsilon]$? **(b)** Quanto vale $\text{Cov}(X,\epsilon)$? **(c)** L'errore ha media condizionale nulla, $E[\epsilon\mid X=x]=0$ per ogni $x$? Si risponda sì o no. **(d)** Di quanto varia $E[Y\mid X]$ quando $X$ passa da ${{e00_13.xa}}$ a ${{e00_13.xb}}$? Nel modello Q: **(e)** quanto vale $\text{Cov}(X,\epsilon)$? **(f)** Quanto vale la differenza $\text{Cov}(X,Y)/\text{Var}(X)-\beta$?
<!-- /ex -->

<!-- ex e00_14 -->
# Esercizio 14 — Alunni della stessa classe: osservazioni non indipendenti *(livello appello)*

> [!abstract] Dati
> Un insegnante vuole sapere se il punteggio medio $\mu$ della sua scuola in un test differisce dalla media nazionale $\mu_0={{e00_14.mu0|m}}$. Misura $n={{e00_14.n|m}}$ alunni della stessa classe, invece di alunni scelti a caso in tutta la scuola. Ogni punteggio $Y_i$ ha deviazione standard $\sigma={{e00_14.sigma|m}}$ e due alunni qualsiasi della stessa classe hanno punteggi con correlazione $\rho={{e00_14.rho|m}}$ (effetto classe). La media del campione è $\bar y={{e00_14.ybar|m}}$. Si consideri $\bar Y$ approssimativamente normale.

> [!question] Testo della domanda
> **Domanda 14 *(4 punti)*.** **(a)** Se i punteggi fossero un campione casuale semplice, cioè indipendenti, quanto varrebbe l'errore standard di $\bar Y$, $\sigma/\sqrt{n}$? **(b)** Con la correlazione $\rho$, $\bar Y$ è ancora uno stimatore corretto di $\mu$? Si risponda sì o no. **(c)** Quanto vale $\text{Var}(Y_1+\dots+Y_n)$ con correlazione $\rho$ fra ogni coppia di alunni? **(d)** Quanto vale l'errore standard di $\bar Y$ con la correlazione? **(e)** Al livello del 5\%, con $H_0:\mu=\mu_0$ contro $H_1:\mu\neq\mu_0$ e valore critico $1{,}96$, si decida se rifiutare o non rifiutare $H_0$ usando l'errore standard di (a). **(f)** Si decida se rifiutare o non rifiutare $H_0$, alle stesse condizioni, usando l'errore standard di (d).
<!-- /ex -->
