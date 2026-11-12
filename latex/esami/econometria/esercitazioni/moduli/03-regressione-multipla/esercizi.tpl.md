<!-- ex e03_01 -->
# Esercizio 1 — Il rendimento dell'istruzione *(livello base)*

> [!abstract] Dati
> Su $n = {{e03_01.n}}$ lavoratori si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \epsilon ,$$
>
> dove `istr` sono gli anni di istruzione ed `esper` gli anni di esperienza. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e03_01.tab.ols}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, il salario per un anno di istruzione in più? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$ (cioè se l'istruzione ha un effetto significativo sul salario).
<!-- /ex -->

<!-- ex e03_02 -->
# Esercizio 2 — Prezzo delle case e inquinamento *(livello base)*

> [!abstract] Dati
> Su $n = {{e03_02.n}}$ distretti si è stimato il modello
>
> $$\log(\text{prezzo}) = \beta_0 + \beta_1\,\log(\text{nox}) + \beta_2\,\log(\text{dist}) + \epsilon ,$$
>
> dove `prezzo` è il prezzo mediano delle case, `nox` la concentrazione di ossidi di azoto (una misura dell'inquinamento) e `dist` la distanza dai centri lavorativi. Nella tabella `l_nox` e `l_dist` sono i logaritmi di `nox` e di `dist`. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\log(z)\approx\Delta z/z$. Le stime OLS sono le seguenti.
>
> {{e03_02.tab.ols}}

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** **(a)** Qual è l'elasticità del prezzo rispetto all'inquinamento? **(b)** Di quanto varia in percentuale il prezzo atteso se `nox` aumenta del ${{e03_02.var}}\%$? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$.
<!-- /ex -->

<!-- ex e03_03 -->
# Esercizio 3 — Il reddito e il suo quadrato: i VIF *(livello base)*

> [!abstract] Dati
> Su $n = {{e03_03.n}}$ famiglie si è stimato il modello
>
> $$\log(\text{consumi}) = \beta_0 + \beta_1\,\text{reddito} + \beta_2\,\text{reddito}^2 + \beta_3\,\text{famiglia} + \beta_4\,\text{eta} + \beta_5\,\text{proprieta} + \epsilon ,$$
>
> dove `reddito` è misurato in decine di migliaia di dollari, `sq_reddito` è il suo quadrato, `famiglia` è il numero di componenti, `eta` l'età del capofamiglia e `proprieta` vale 1 se la famiglia possiede l'abitazione. Le stime OLS sono le seguenti.
>
> {{e03_03.tab.ols}}
>
> I fattori di inflazione della varianza sono $\text{VIF}(j)=1/(1-R_j^2)$, dove $R_j^2$ è l'$R^2$ della regressione di $x_j$ sugli altri regressori.
>
> {{e03_03.tab.vif}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Si usi la soglia 10 per il VIF. **(a)** Quanti regressori presentano un VIF superiore alla soglia? **(b)** Rispetto al caso in cui i regressori fossero indipendenti fra loro, di quante volte ci si aspetta che sia gonfiato l'errore standard del coefficiente di `reddito`? **(c)** La non significatività del coefficiente di `reddito` al 5\% può dipendere dalla quasi-collinearità? Si risponda sì o no.
<!-- /ex -->

<!-- ex e03_04 -->
# Esercizio 4 — Salario, istruzione e stato civile: percentuali e dollari *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_04.n}}$ lavoratori si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{sposato} + \epsilon ,$$
>
> dove `salario` è il salario mensile in dollari, `istr` ed `esper` sono gli anni di istruzione e di esperienza e `sposato` vale 1 per i lavoratori sposati e 0 per gli altri. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e03_04.tab.ols}}

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** Di quanti anni deve aumentare l'istruzione perché il salario atteso cresca del ${{e03_04.obiettivo}}\%$, a parità di esperienza e di stato civile? **(b)** Di quanto è più alto in percentuale, in media, il salario di un lavoratore sposato rispetto a quello di un single con le stesse altre caratteristiche? **(c)** Un single guadagna ${{e03_04.w0}}$ dollari al mese: di quanti dollari in più guadagna in media uno sposato con le stesse altre caratteristiche? **(d)** Un collega sostiene che uno sposato guadagna in media ${{e03_04.riv}}$ dollari al mese in più di un single che ne guadagna ${{e03_04.w0}}$. Al livello del 5\%, l'affermazione è compatibile con i dati? Si risponda sì o no.
<!-- /ex -->

<!-- ex e03_05 -->
# Esercizio 5 — Ricchezza e logaritmo del reddito *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_05.n}}$ famiglie si è stimato il modello
>
> $$\text{rich} = \beta_0 + \beta_1\,\log(\text{red}) + \beta_2\,\text{eta} + \epsilon ,$$
>
> dove `rich` è la ricchezza netta e `red` il reddito annuo, entrambi in migliaia di dollari, ed `eta` è l'età del capofamiglia. Nella tabella `l_red` è il logaritmo di `red`. Per una variazione relativa del reddito si usi l'approssimazione $\Delta\log(\text{red})\approx\Delta\text{red}/\text{red}$. Le stime OLS sono le seguenti.
>
> {{e03_05.tab.ols}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Di quanti dollari varia in media la ricchezza se il reddito aumenta del ${{e03_05.var}}\%$, a parità di età? **(b)** Di quanto deve aumentare in percentuale il reddito perché la ricchezza attesa cresca di ${{e03_05.obiettivo}}$ dollari? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(d)** Una famiglia ha un reddito di ${{e03_05.ra}}$ e un'altra di ${{e03_05.rb}}$ (migliaia di dollari). La variazione attesa di ricchezza per un aumento del ${{e03_05.var}}\%$ del reddito è la stessa nei due casi? Si risponda sì o no.
<!-- /ex -->

<!-- ex e03_06 -->
# Esercizio 6 — Esperienza e salario: una relazione non lineare *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_06.n}}$ lavoratori si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{esper}^2 + \epsilon ,$$
>
> dove `esper2` è il quadrato di `esper`. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e03_06.tab.ols}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$. **(b)** Si calcoli l'effetto marginale dell'esperienza, in percentuale, per un lavoratore con $\text{esper} = {{e03_06.x0}}$ anni. **(c)** A quale livello di esperienza l'effetto marginale dell'esperienza si annulla?
<!-- /ex -->

<!-- ex e03_07 -->
# Esercizio 7 — Salario, istruzione e ore lavorate *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_07.n}}$ lavoratori si è stimato, per $\log(\text{salario})$, il Modello 1
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \epsilon$$
>
> {{e03_07.tab.m1}}
>
> e il Modello 2, che aggiunge `ore`, le ore lavorate a settimana:
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{ore} + \epsilon$$
>
> {{e03_07.tab.m2}}
>
> Si è stimata infine la regressione ausiliaria $\text{ore} = \delta_0 + \delta_1\,\text{istr} + \delta_2\,\text{esper} + u$.
>
> {{e03_07.tab.aux}}

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** Si indichi con $\tilde\beta_1$ la stima di $\beta_1$ nel Modello 1 e con $\hat\beta_1$ quella nel Modello 2. **(a)** Quanto vale, in punti percentuali, $100\,(\tilde\beta_1-\hat\beta_1)$? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_3=0$ nel Modello 2. **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta_1=0$ nella regressione ausiliaria. **(d)** Al livello del 5\%, il Modello 1 soffre di distorsione da variabile omessa dovuta a `ore`? Si risponda sì o no.
<!-- /ex -->

<!-- ex e03_08 -->
# Esercizio 8 — Il reddito dichiarato *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_08.n}}$ famiglie i consumi $y$ dipendono dal reddito vero $x$ secondo il modello $y=\alpha+\gamma\,x+\epsilon$, con $\gamma={{e03_08.gamma|m}}$ (dati simulati). Il reddito vero non è osservabile: si osserva solo il reddito dichiarato $x^*=x+u$, dove $u$ è un errore di misura incorrelato con $x$ e con $\epsilon$. Le varianze valgono $\text{Var}(x)={{e03_08.sx2|m}}$ e $\text{Var}(u)={{e03_08.su2|m}}$. Con il reddito vero (`red`) si otterrebbe
>
> {{e03_08.tab.vero}}
>
> mentre con il reddito dichiarato (`red_dich`) si ottiene
>
> {{e03_08.tab.dich}}

> [!question] Testo della domanda
> **Domanda 8 *(3 punti)*.** **(a)** Quanto vale il rapporto $\lambda=\text{Var}(x)/\bigl(\text{Var}(x)+\text{Var}(u)\bigr)$? **(b)** Quale valore ci si aspetta, al limite per $n\to\infty$, per il coefficiente di `red_dich`? **(c)** Si scriva il modello in funzione di $x^*$, $y=\alpha+\gamma\,x^*+\epsilon^*$: quanto vale $\text{Cov}(x^*,\epsilon^*)$? **(d)** L'intervallo di confidenza al 95\% per il coefficiente di `red_dich` contiene il valore vero $\gamma$? Si risponda sì o no. **(e)** Si spieghi perché l'errore di misura rende $x^*$ endogeno anche se $u$ ha media nulla.
<!-- /ex -->

<!-- ex e03_09 -->
# Esercizio 9 — Classe e reddito: il teorema di Frisch-Waugh-Lovell *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e03_09.n}}$ distretti scolastici si vuole stimare il modello
>
> $$\text{punteggio} = \beta_0 + \beta_1\,\text{classe} + \beta_2\,\text{reddito} + \epsilon ,$$
>
> dove `classe` è il numero medio di studenti per insegnante e `reddito` il reddito medio del distretto. L'output della regressione completa non è disponibile: si hanno solo i tre passi seguenti.
>
> **Passo (1).** Regressione di `classe` su `reddito`; $u_{\text{classe}}$ indica i suoi residui.
>
> {{e03_09.tab.passo1}}
>
> **Passo (2).** Regressione di `punteggio` su `reddito`; $u_{\text{punteggio}}$ indica i suoi residui.
>
> {{e03_09.tab.passo2}}
>
> **Passo (3).** Regressione di $u_{\text{punteggio}}$ su $u_{\text{classe}}$ (nella tabella `u_classe`).
>
> {{e03_09.tab.passo3}}

> [!question] Testo della domanda
> **Domanda 9 *(3 punti)*.** **(a)** Quanto vale la stima di $\beta_1$ nella regressione completa di `punteggio` su `classe` e `reddito`? **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(c)** Quanto vale il VIF di `classe` nella regressione completa, con $\text{VIF}(j)=1/(1-R_j^2)$ e $R_j^2$ l'$R^2$ della regressione di $x_j$ sugli altri regressori? **(d)** Si spieghi perché la costante del passo (3) è nulla.
<!-- /ex -->

<!-- ex e03_10 -->
# Esercizio 10 — Reddito e spesa: non linearità, punto di svolta e dollari *(livello appello)*

> [!abstract] Dati
> Su $n = {{e03_10.n}}$ famiglie si è stimato il modello
>
> $$\log(\text{spesa}) = \beta_0 + \beta_1\,\text{red} + \beta_2\,\text{red}^2 + \beta_3\,\text{eta} + \epsilon ,$$
>
> dove `red` è il reddito in decine di migliaia di dollari (`red` $=1$ corrisponde a ${{e03_10.unita}}$ dollari), `sq_red` è il suo quadrato ed `eta` l'età del capofamiglia. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti; la covarianza stimata fra $\hat\beta_1$ e $\hat\beta_2$ vale ${{e03_10.cov|m}}$.
>
> {{e03_10.tab.ols}}

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(b)** L'effetto marginale del reddito è decrescente? Si risponda sì o no. **(c)** Per quale reddito, espresso in dollari, l'effetto marginale del reddito si annulla? **(d)** Si calcoli l'effetto marginale del reddito (la derivata di $\log(\text{spesa})$ rispetto a `red`), in percentuale, per una famiglia con $\text{red}={{e03_10.x0}}$. **(e)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi che tale effetto marginale sia nullo, $H_0:\beta_1+2\times{{e03_10.x0}}\times\beta_2=0$, contro l'alternativa bilaterale.
<!-- /ex -->

<!-- ex e03_11 -->
# Esercizio 11 — Affitti: superficie e distanza dal centro *(livello appello)*

> [!abstract] Dati
> Su $n = {{e03_11.n}}$ appartamenti in affitto si è stimato il modello
>
> $$\log(\text{affitto}) = \beta_0 + \beta_1\,\log(\text{mq}) + \beta_2\,\text{km} + \beta_3\,\text{ascensore} + \epsilon ,$$
>
> dove `affitto` è il canone mensile in euro, `mq` la superficie in metri quadrati (nella tabella `l_mq` è il suo logaritmo), `km` la distanza dal centro in chilometri e `ascensore` vale 1 se l'edificio ha l'ascensore. Le variazioni percentuali si calcolano con le approssimazioni $\Delta\%\,y\approx 100\,\Delta\log(y)$ e $\Delta\log(x)\approx\Delta x/x$. Le stime OLS sono le seguenti.
>
> {{e03_11.tab.ols}}

> [!question] Testo della domanda
> **Domanda 11 *(4 punti)*.** **(a)** Di quanto varia in percentuale l'affitto atteso se la superficie aumenta del ${{e03_11.ds}}\%$, a parità del resto? **(b)** E se l'appartamento è ${{e03_11.dkm}}$ chilometri più lontano dal centro? **(c)** Di quanto, in percentuale, deve aumentare la superficie perché l'affitto atteso non cambi, nonostante i ${{e03_11.dkm}}$ chilometri in più? **(d)** Un'agenzia sostiene che un aumento della superficie del ${{e03_11.ds}}\%$ fa salire l'affitto del ${{e03_11.riv}}\%$. Al livello del 5\%, l'affermazione è compatibile con i dati? Si risponda sì o no.
<!-- /ex -->

<!-- ex e03_12 -->
# Esercizio 12 — Esperienza e anzianità: collinearità o variabile omessa? *(livello appello)*

> [!abstract] Dati
> Su $n = {{e03_12.n}}$ lavoratori si è stimato, per $\log(\text{salario})$, il Modello 1
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{anz} + \epsilon ,$$
>
> dove `esper` sono gli anni di esperienza complessiva e `anz` gli anni di anzianità nell'azienda attuale.
>
> {{e03_12.tab.m1}}
>
> I VIF del Modello 1, con $\text{VIF}(j)=1/(1-R_j^2)$, sono
>
> {{e03_12.tab.vif}}
>
> Eliminando `anz` si è stimato il Modello 2.
>
> {{e03_12.tab.m2}}

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** Si usi la soglia 10 per il VIF. **(a)** I VIF indicano la presenza di quasi-collinearità? Si risponda sì o no. **(b)** Rispetto al caso in cui i regressori fossero indipendenti fra loro, di quante volte ci si aspetta che sia gonfiato l'errore standard del coefficiente di `esper` nel Modello 1? **(c)** Quante volte l'errore standard di `esper` nel Modello 1 è più grande di quello nel Modello 2? **(d)** Al livello del 5\%, nel Modello 1 si decida se rifiutare o non rifiutare $H_0:\beta_2=0$. **(e)** Lo stesso nel Modello 2. **(f)** Di quanti punti percentuali sale la stima del coefficiente di `esper` passando dal Modello 1 al Modello 2, cioè quanto vale $100\times(\text{stima nel Modello 2}-\text{stima nel Modello 1})$? **(g)** Eliminare `anz` è una soluzione corretta al problema? Si motivi.
<!-- /ex -->

<!-- ex e03_13 -->
# Esercizio 13 — Salario, istruzione e abilità *(livello appello)*

> [!abstract] Dati
> Su $n = {{e03_13.n}}$ lavoratori si è stimato, per $\log(\text{salario})$, il Modello 1
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \epsilon$$
>
> {{e03_13.tab.m1}}
>
> e il Modello 2, che aggiunge `abil`, un punteggio standardizzato di abilità:
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{abil} + \epsilon$$
>
> {{e03_13.tab.m2}}
>
> Si è stimata infine la regressione ausiliaria $\text{abil} = \delta_0 + \delta_1\,\text{istr} + \delta_2\,\text{esper} + u$.
>
> {{e03_13.tab.aux}}

> [!question] Testo della domanda
> **Domanda 13 *(4 punti)*.** Si indichi con $\tilde\beta_1$ la stima di $\beta_1$ nel Modello 1 e con $\hat\beta_1$ quella nel Modello 2. **(a)** Quanto vale, in punti percentuali, $100\,(\tilde\beta_1-\hat\beta_1)$? **(b)** Si dica, al livello del 5\%, se il Modello 1 soffre di distorsione da variabile omessa. Si risponda sì o no. **(c)** Si calcoli, in punti percentuali, $100\,\hat\beta_3\,\hat\delta_1$ con i numeri delle tabelle e lo si confronti con la risposta (a). **(d)** Il Modello 1 sovrastima il rendimento dell'istruzione rispetto al Modello 2? Si risponda sì o no.
<!-- /ex -->
