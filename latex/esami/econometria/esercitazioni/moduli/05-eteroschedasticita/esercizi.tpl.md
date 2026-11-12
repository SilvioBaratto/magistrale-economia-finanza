<!-- ex e05_01 -->
# Esercizio 1 — Due grafici dei residui *(livello base)*

> [!abstract] Dati
> Per due modelli di regressione lineare semplice, $y=\beta_0+\beta_1\,x+\epsilon$, stimati con OLS su $n={{e05_01.n}}$ osservazioni ciascuno, la figura rappresenta i residui $\hat\epsilon$ contro i valori predetti $\hat y$. Il Modello A spiega la spesa per consumi con il reddito, il Modello B la resa di un impianto con l'irraggiamento. I due grafici hanno la stessa scala verticale.

![Residui contro valori predetti: Modello A (a sinistra) e Modello B (a destra).]({{e05_01.fig.residui}}){width=85%}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** Si risponda sì o no. **(a)** Il grafico del Modello A è coerente con l'ipotesi di omoschedasticità? **(b)** Il grafico del Modello B è coerente con l'ipotesi di omoschedasticità? **(c)** Per il Modello A, gli errori standard usuali dell'OLS, calcolati assumendo l'omoschedasticità, sono affidabili per costruire i test $t$?
<!-- /ex -->

<!-- ex e05_02 -->
# Esercizio 2 — Il test di Breusch-Pagan *(livello base)*

> [!abstract] Dati
> Su $n={{e05_02.n}}$ appartamenti si è stimato il modello
>
> $$\text{prezzo}=\beta_0+\beta_1\,\text{sup}+\beta_2\,\text{dist}+\beta_3\,\text{eta}+\epsilon ,$$
>
> dove `prezzo` è in migliaia di euro, `sup` è la superficie in metri quadrati, `dist` la distanza dal centro in chilometri ed `eta` l'età dell'edificio in anni. Le stime OLS sono le seguenti.
>
> {{e05_02.tab.ols}}
>
> Per il test di Breusch-Pagan si è poi stimata la regressione ausiliaria $\hat\epsilon^2=\delta_0+\delta_1\,\text{sup}+\delta_2\,\text{dist}+\delta_3\,\text{eta}+u$, dove la variabile dipendente `res_sq` contiene i quadrati dei residui del modello precedente.
>
> {{e05_02.tab.aus}}
>
> Sotto $H_0:\delta_1=\delta_2=\delta_3=0$ (omoschedasticità) la statistica $LM=nR^2$, con $R^2$ della regressione ausiliaria, ha distribuzione approssimata $\chi^2_k$, con $k={{e05_02.k}}$ regressori. Il valore critico della $\chi^2_{k}$ al livello del 5\% è ${{e05_02.crit|m}}$.

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** Quanto vale la statistica $LM=nR^2$? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta_1=\delta_2=\delta_3=0$ contro $H_1$: almeno un $\delta_j\neq 0$. **(c)** Alla luce del risultato, conviene calcolare i test $t$ del modello con errori standard robusti? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_03 -->
# Esercizio 3 — Errori standard usuali e robusti *(livello base)*

> [!abstract] Dati
> Su $n={{e05_03.n}}$ case in vendita si è stimato il modello
>
> $$\text{prezzo}=\beta_0+\beta_1\,\text{sup}+\beta_2\,\text{giardino}+\beta_3\,\text{camere}+\epsilon ,$$
>
> dove `prezzo` è in migliaia di euro, `sup` è la superficie in metri quadrati, `giardino` l'area del giardino in centinaia di metri quadrati e `camere` il numero di camere. Si riportano le stime OLS con gli errori standard usuali e con gli errori standard robusti all'eteroschedasticità di White (variante HC1).
>
> *Errori standard usuali:*
>
> {{e05_03.tab.ols}}
>
> *Errori standard robusti (HC1):*
>
> {{e05_03.tab.rob}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Si consideri il coefficiente $\beta_2$ di `giardino`. **(a)** Quanto vale il rapporto fra l'errore standard robusto e quello usuale? **(b)** Al livello del 5\%, con gli errori standard usuali, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(c)** Al livello del 5\%, con gli errori standard robusti, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(d)** I coefficienti stimati cambiano passando dagli errori standard usuali a quelli robusti? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_04 -->
# Esercizio 4 — Residui al quadrato e valori predetti *(livello intermedio)*

> [!abstract] Dati
> Su $n={{e05_04.n}}$ studenti si è stimato il modello
>
> $$\text{punteggio}=\beta_0+\beta_1\,\text{ore}+\beta_2\,\text{media}+\epsilon ,$$
>
> dove `punteggio` è il risultato di una prova, `ore` le ore di studio e `media` la media dei voti precedenti. Le stime OLS sono le seguenti.
>
> {{e05_04.tab.ols}}
>
> La figura qui sotto rappresenta i residui del modello contro i valori predetti. Si è poi stimata la regressione ausiliaria $\hat\epsilon^2=a+b\,\hat y+u$ dei residui al quadrato sui valori predetti (`y_pred`).
>
> {{e05_04.tab.aus}}

![Residui contro valori predetti.]({{e05_04.fig.residui}}){width=85%}

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** La dispersione dei residui aumenta al crescere dei valori predetti? Si risponda sì o no. **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:b=0$ contro $H_1:b\neq 0$. **(c)** Si interpreti il valore stimato di $\hat\epsilon^2$ come varianza dei residui: qual è la deviazione standard stimata dei residui per un valore predetto $\hat y={{e05_04.y0}}$? **(d)** Alla luce del risultato, conviene calcolare i test $t$ del modello con errori standard robusti? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_05 -->
# Esercizio 5 — Breusch-Pagan e White: due test, due esiti *(livello intermedio)*

> [!abstract] Dati
> Su $n={{e05_05.n}}$ lavoratori si è stimato il modello
>
> $$\text{salario}=\beta_0+\beta_1\,\text{istr}+\beta_2\,\text{esper}+\beta_3\,\text{ore}+\beta_4\,\text{anz}+\epsilon ,$$
>
> dove `salario` è il salario orario, `istr` ed `esper` sono gli anni di istruzione e di esperienza, `ore` le ore lavorate a settimana e `anz` l'anzianità aziendale in anni. Per verificare l'omoschedasticità si sono eseguiti due test sui residui, entrambi con ipotesi nulla l'omoschedasticità e alternativa l'eteroschedasticità. Il test di Breusch-Pagan usa come regressori ausiliari i regressori del modello; il test di White usa anche i loro quadrati e i loro prodotti.
>
> {{e05_05.tab.bp}}
>
> {{e05_05.tab.white}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** Al livello del 5\%: **(a)** si decida se rifiutare o non rifiutare l'ipotesi nulla di omoschedasticità con il test di Breusch-Pagan; **(b)** si decida lo stesso con il test di White; **(c)** il fatto che il test di White non rifiuti permette di concludere che il modello è omoschedastico? Si risponda sì o no. **(d)** Alla luce dei due test, conviene usare errori standard robusti? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_06 -->
# Esercizio 6 — Che cosa resta valido con errori eteroschedastici *(livello intermedio)*

> [!abstract] Dati
> Si simula il modello $y=1+\beta_1\,x+\epsilon$ con $\beta_1={{e05_06.beta|m}}$ (il valore vero), $x\sim N(0,\,1)$ ed errori $\epsilon\mid x\sim N(0,x^2)$: hanno media condizionale nulla, $E[\epsilon\mid x]=0$, ma varianza che dipende da $x$, quindi sono eteroschedastici. Per ciascuna delle numerosità $n$ della tabella si generano ${{e05_06.R}}$ campioni; in ognuno si stima $\beta_1$ con OLS, con l'errore standard usuale e con quello robusto (HC1), e si verifica $H_0:\beta_1={{e05_06.beta|m}}$ (vera) rifiutandola se $|t|>1{,}96$. L'errore di simulazione della media è la deviazione standard delle stime divisa per $\sqrt{ {{e05_06.R}} }$.
>
> {{e05_06.tab.mc}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Lo stimatore OLS di $\beta_1$ risulta distorto? Si consideri distorta una media delle stime che dista dal valore vero più di due volte il suo errore di simulazione, per almeno una delle tre numerosità; si risponda sì o no. **(b)** Per $n={{e05_06.n3}}$, quanto vale il rapporto fra la deviazione standard delle stime e la media dell'errore standard usuale? **(c)** Per $n={{e05_06.n3}}$, la frequenza di rifiuto della $H_0$ vera con il $t$ usuale è entro ${{e05_06.tol|m}}$ punti percentuali dal 5\%? Si risponda sì o no. **(d)** Per $n={{e05_06.n3}}$, la frequenza di rifiuto della $H_0$ vera con il $t$ robusto è entro ${{e05_06.tol|m}}$ punti percentuali dal 5\%? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_07 -->
# Esercizio 7 — Quando gli errori standard robusti sono più piccoli *(livello intermedio)*

> [!abstract] Dati
> Su $n={{e05_07.n}}$ appezzamenti si è stimato il modello
>
> $$\text{resa}=\beta_0+\beta_1\,\text{azoto}+\beta_2\,\text{scarto}+\beta_3\,\text{irrig}+\epsilon ,$$
>
> dove `resa` è il raccolto in quintali per ettaro, `azoto` l'azoto distribuito in chilogrammi per ettaro, `scarto` lo scarto della temperatura stagionale dalla sua media in gradi e `irrig` vale 1 se il terreno è irrigato. Si riportano le stime con gli errori standard usuali e con quelli robusti all'eteroschedasticità di White (variante HC1).
>
> *Errori standard usuali:*
>
> {{e05_07.tab.ols}}
>
> *Errori standard robusti (HC1):*
>
> {{e05_07.tab.rob}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** Si consideri il coefficiente $\beta_2$ di `scarto`. **(a)** Quanto vale il rapporto fra l'errore standard robusto e quello usuale? **(b)** Al livello del 5\%, con gli errori standard usuali, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(c)** Al livello del 5\%, con gli errori standard robusti, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(d)** Qual è l'estremo inferiore dell'intervallo di confidenza $\hat\beta_2\pm 1{,}96\,\widehat{\text{se}}$, costruito con l'errore standard robusto?
<!-- /ex -->

<!-- ex e05_08 -->
# Esercizio 8 — Un grafico pulito non basta *(livello appello)*

> [!abstract] Dati
> Su $n={{e05_08.n}}$ imprese si è stimato il modello
>
> $$\text{prod}=\beta_0+\beta_1\,\text{capitale}+\beta_2\,\text{formazione}+\beta_3\,\text{anzianita}+\epsilon ,$$
>
> dove `prod` è la produttività del lavoro, `capitale` il capitale per addetto, `formazione` le ore annue di formazione per addetto e `anzianita` l'anzianità media degli addetti in anni. Le stime con gli errori standard usuali sono le seguenti.
>
> {{e05_08.tab.ols}}
>
> Le stime con gli errori standard robusti all'eteroschedasticità di White (variante HC1) sono le seguenti.
>
> {{e05_08.tab.rob}}
>
> Il test di Breusch-Pagan per l'eteroschedasticità, con ipotesi nulla l'omoschedasticità, ha dato il risultato seguente. La figura qui sotto rappresenta i residui del modello contro i valori predetti.
>
> {{e05_08.tab.bp}}

![Residui contro valori predetti.]({{e05_08.fig.residui}}){width=85%}

> [!question] Testo della domanda
> **Domanda 8 *(4 punti)*.** **(a)** Il grafico dei residui contro i valori predetti è coerente con l'ipotesi di omoschedasticità? Si risponda sì o no. **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi nulla di omoschedasticità con il test di Breusch-Pagan. **(c)** Dal grafico si può escludere la necessità di errori standard robusti? Si risponda sì o no. **(d)** Quanto vale il rapporto $t$ robusto del coefficiente $\beta_2$ di `formazione`? **(e)** Al livello del 5\%, con gli errori standard robusti, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$.
<!-- /ex -->

<!-- ex e05_09 -->
# Esercizio 9 — Il test $F$ con errori standard usuali e robusti *(livello appello)*

> [!abstract] Dati
> Su $n={{e05_09.n}}$ imprese si è stimato il modello
>
> $$\text{prod}=\beta_0+\beta_1\,\text{capitale}+\beta_2\,\text{formazione}+\beta_3\,\text{ricerca}+\epsilon ,$$
>
> dove `prod` è la produttività del lavoro, `capitale` il capitale per addetto, `formazione` le ore annue di formazione per addetto e `ricerca` la spesa in ricerca e sviluppo per addetto. Le stime OLS, con gli errori standard usuali, sono le seguenti.
>
> {{e05_09.tab.ols}}
>
> Il test di White per l'eteroschedasticità, con ipotesi nulla l'omoschedasticità, ha dato il risultato seguente.
>
> {{e05_09.tab.white}}
>
> Si vuole verificare $H_0:\beta_2=\beta_3=0$ ($q={{e05_09.q}}$ vincoli) contro $H_1$: almeno uno dei due coefficienti è diverso da zero. Il modello ristretto, senza `formazione` e `ricerca`, ha le stime seguenti.
>
> {{e05_09.tab.rid}}
>
> Il valore critico della $F_{ {{e05_09.q}},\,{{e05_09.gl}} }$ al livello del 5\% è ${{e05_09.crit|m}}$. Con gli errori standard robusti il software fornisce direttamente:
>
> {{e05_09.tab.frob}}

> [!question] Testo della domanda
> **Domanda 9 *(4 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi nulla di omoschedasticità con il test di White. **(b)** Quanto vale la statistica $F=\dfrac{(\text{SSR}_R-\text{SSR}_U)/q}{\text{SSR}_U/(n-k-1)}$ con gli errori standard usuali, calcolata con le somme dei quadrati dei residui delle due tabelle? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2=\beta_3=0$ con la statistica $F$ usuale. **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2=\beta_3=0$ con la statistica $F$ robusta. **(e)** La conclusione sul vincolo congiunto cambia usando gli errori standard robusti? Si risponda sì o no.
<!-- /ex -->

<!-- ex e05_10 -->
# Esercizio 10 — Eteroschedasticità non è endogeneità *(livello appello)*

> [!abstract] Dati
> Si simula il modello $y=1+\beta_1\,x+\epsilon$ con $\beta_1={{e05_10.beta|m}}$ (il valore vero) in tre scenari. Per ciascuno si generano ${{e05_10.R}}$ campioni di $n={{e05_10.n}}$ osservazioni; in ognuno si stima $\beta_1$ con OLS, con l'errore standard usuale e con quello robusto (HC1), e si verifica $H_0:\beta_1={{e05_10.beta|m}}$ (vera) rifiutandola se $|t|>1{,}96$. L'errore di simulazione della media è la deviazione standard delle stime divisa per $\sqrt{ {{e05_10.R}} }$.
>
> - *Scenario I:* $x\sim N(0,\,1)$ ed $\epsilon\mid x\sim N(0,\,1)$.
> - *Scenario II:* $x\sim N(0,\,1)$ ed $\epsilon\mid x\sim N(0,x^2)$.
> - *Scenario III:* $x=\rho\,w+\sqrt{1-\rho^2}\,v$ ed $\epsilon=\gamma\,w+\sqrt{1-\gamma^2}\,u$, con $w$, $v$, $u$ indipendenti e $N(0,\,1)$, $\rho={{e05_10.rho|m}}$ e $\gamma={{e05_10.gamma|m}}$. Il termine $w$ è una variabile omessa correlata con $x$.
>
> {{e05_10.tab.mc}}
>
> In un campione dello scenario II, con $n={{e05_10.n}}$, il test di White per l'eteroschedasticità ha dato il risultato seguente.
>
> {{e05_10.tab.white}}

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** **(a)** Nello scenario II lo stimatore OLS di $\beta_1$ risulta distorto? Si consideri distorta una media delle stime che dista dal valore vero più di due volte il suo errore di simulazione; si risponda sì o no. **(b)** Nello scenario III, quanto vale la distorsione media, cioè la media delle stime meno $\beta_1$? **(c)** Nello scenario III, la frequenza di rifiuto della $H_0$ vera con il $t$ robusto è entro ${{e05_10.tol|m}}$ punti percentuali dal 5\%? Si risponda sì o no. **(d)** Il test di White rifiuta l'omoschedasticità nel campione dello scenario II. Si può concluderne che $E[\epsilon\mid x]\neq 0$? Si risponda sì o no.
<!-- /ex -->
