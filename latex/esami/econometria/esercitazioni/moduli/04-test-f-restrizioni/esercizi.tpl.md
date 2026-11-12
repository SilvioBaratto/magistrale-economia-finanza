<!-- ex e04_01 -->
# Esercizio 1 — Ruolo e salario dei giocatori *(livello base)*

> [!abstract] Dati
> Su $n = {{e04_01.n}}$ giocatori di pallacanestro si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{guardia} + \beta_2\,\text{ala} + \beta_3\,\text{punti} + \beta_4\,\text{esper} + \epsilon ,$$
>
> dove `salario` è il compenso annuale, `guardia` e `ala` sono due variabili dummy che valgono 1 per i giocatori di quel ruolo e 0 per gli altri, `punti` sono i punti segnati per partita ed `esper` gli anni da professionista. Ogni giocatore è una guardia, un'ala o un centro. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e04_01.tab.ols}}

> [!question] Testo della domanda
> **Domanda 1 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, il salario passando da un centro a una guardia con gli stessi punti e la stessa esperienza? **(b)** E passando da una guardia a un centro? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2=0$ contro $H_1:\beta_2\neq 0$. **(d)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$. **(e)** Si spieghi perché nella tabella non compare la dummy del centro e che cosa misurano $\beta_1$ e $\beta_2$.
<!-- /ex -->

<!-- ex e04_02 -->
# Esercizio 2 — Balcone e box: un test $F$ da calcolare *(livello base)*

> [!abstract] Dati
> Su $n = {{e04_02.n}}$ appartamenti in vendita si è stimato il modello completo
>
> $$\log(\text{prezzo}) = \beta_0 + \beta_1\,\log(\text{mq}) + \beta_2\,\text{eta} + \beta_3\,\text{ascensore} + \beta_4\,\text{balcone} + \beta_5\,\text{box} + \epsilon ,$$
>
> dove `mq` è la superficie in metri quadrati (nella tabella `l_mq` è il suo logaritmo), `eta` gli anni dell'edificio e `ascensore`, `balcone` e `box` sono dummy che valgono 1 se l'appartamento ha quella caratteristica.
>
> {{e04_02.tab.completo}}
>
> Si vuole verificare se `balcone` e `box`, congiuntamente, influenzano il prezzo: $H_0:\beta_4=\beta_5=0$ contro $H_1$: almeno uno dei due è diverso da zero. Il modello ristretto, che impone $H_0$, esclude le due variabili.
>
> {{e04_02.tab.ristretto}}
>
> Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà di questo test è ${{e04_02.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 2 *(3 punti)*.** Sia $k$ il numero di regressori del modello completo, costante esclusa. **(a)** Quante restrizioni $s$ impone $H_0$? **(b)** Quanti sono i gradi di libertà $n-k-1$ del denominatore? **(c)** Quanto vale $F=\dfrac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-k-1)}$, con $\text{SSR}_r$ e $\text{SSR}_c$ le somme dei quadrati dei residui del modello ristretto e del completo? **(d)** Quanto vale la stessa statistica calcolata con gli $R^2$, $F=\dfrac{(R^2_c-R^2_r)/s}{(1-R^2_c)/(n-k-1)}$? **(e)** Al livello del 5\%, confrontando $F$ con il valore critico, si decida se rifiutare o non rifiutare $H_0$.
<!-- /ex -->

<!-- ex e04_03 -->
# Esercizio 3 — Rendimenti di scala *(livello base)*

> [!abstract] Dati
> Su $n = {{e04_03.n}}$ imprese manifatturiere si è stimata la funzione di produzione
>
> $$\log(Q) = \beta_0 + \beta_1\,\log(K) + \beta_2\,\log(L) + \beta_3\,\text{esporta} + \epsilon ,$$
>
> dove $Q$ è il valore della produzione, $K$ lo stock di capitale, $L$ le ore lavorate (nella tabella `l_cap` e `l_lav` sono i logaritmi di $K$ e di $L$) ed `esporta` vale 1 se l'impresa esporta. I rendimenti di scala sono costanti quando $\beta_1+\beta_2=1$: se capitale e lavoro crescono entrambi dell'1\%, la produzione cresce dell'1\%. Le stime OLS sono le seguenti; la covarianza stimata fra $\hat\beta_1$ e $\hat\beta_2$ vale ${{e04_03.cov|m}}$.
>
> {{e04_03.tab.ols}}

> [!question] Testo della domanda
> **Domanda 3 *(3 punti)*.** Si verifichi, al livello del 5\%, $H_0:\beta_1+\beta_2=1$ (rendimenti di scala costanti) contro $H_1:\beta_1+\beta_2\neq 1$. **(a)** Quanto vale la stima di $\beta_1+\beta_2$? **(b)** Quanto vale l'errore standard di $\hat\beta_1+\hat\beta_2$? **(c)** Quanto vale il rapporto $t=(\hat\beta_1+\hat\beta_2-1)/\widehat{\text{se}}(\hat\beta_1+\hat\beta_2)$? **(d)** Si decida se rifiutare o non rifiutare $H_0$. **(e)** Con una sola restrizione ($s=1$) la statistica $F$ è il quadrato di $t$: quanto vale $F$?
<!-- /ex -->

<!-- ex e04_04 -->
# Esercizio 4 — Titolo di studio: il sistema d'ipotesi del test $F$ *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e04_04.n}}$ lavoratori si è stimato il modello completo
>
> $$\log(\text{salario}) = \alpha + \delta_1\,\text{obbligo} + \delta_2\,\text{diploma} + \beta_1\,\text{esper} + \beta_2\,\text{anz} + \epsilon ,$$
>
> dove `obbligo` vale 1 per i lavoratori con la sola scuola dell'obbligo e 0 per gli altri, `diploma` vale 1 per i diplomati e 0 per gli altri, ed `esper` e `anz` sono gli anni di esperienza e di anzianità in azienda. Ogni lavoratore ha la sola scuola dell'obbligo, un diploma o una laurea.
>
> {{e04_04.tab.completo}}
>
> Per verificare se il titolo di studio ha rilevanza nel modello si è stimato anche il modello ristretto, senza le due dummy; i due modelli hanno la stessa variabile dipendente.
>
> {{e04_04.tab.ristretto}}
>
> Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà di questo test è ${{e04_04.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 4 *(3 punti)*.** **(a)** Qual è la categoria di riferimento? Che cosa misurano $\delta_1$ e $\delta_2$, e perché la dummy dei laureati non compare nel modello? **(b)** Si scriva il sistema d'ipotesi del test $F$ con cui si verifica se il titolo di studio ha rilevanza nel modello. **(c)** Quante restrizioni $s$ impone $H_0$? **(d)** Quanti sono i gradi di libertà $n-k-1$ del denominatore, con $k$ il numero di regressori del modello completo, costante esclusa? **(e)** Quanto vale $F=\dfrac{(R^2_c-R^2_r)/s}{(1-R^2_c)/(n-k-1)}$? **(f)** Al livello del 5\%, confrontando $F$ con il valore critico, si decida se rifiutare o non rifiutare $H_0$. **(g)** Se come categoria di riferimento si scegliesse il diploma anziché la laurea, la statistica $F$ cambierebbe? Si risponda sì o no.
<!-- /ex -->

<!-- ex e04_05 -->
# Esercizio 5 — Il rendimento dell'istruzione dipende dal genere *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e04_05.n}}$ lavoratori si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{donna} + \beta_3\,\text{esper} + \beta_4\,(\text{donna}\times\text{istr}) + \epsilon ,$$
>
> dove `istr` ed `esper` sono gli anni di istruzione e di esperienza, `donna` vale 1 per le donne e 0 per gli uomini e `d_istr` è il prodotto `donna`$\times$`istr`. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti.
>
> {{e04_05.tab.ols}}

> [!question] Testo della domanda
> **Domanda 5 *(3 punti)*.** **(a)** Di quanto varia in percentuale, in media, il salario di un uomo per un anno di istruzione in più, a parità di esperienza? **(b)** E quello di una donna? **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$ (cioè se il rendimento dell'istruzione dipende dal genere). **(d)** Di quanto differisce in percentuale il salario atteso di una donna da quello di un uomo (donna meno uomo) con la stessa esperienza e ${{e04_05.e0|m}}$ anni di istruzione? **(e)** Il coefficiente $\beta_2$ misura il divario di salario fra donne e uomini a qualunque livello di istruzione? Si risponda sì o no.
<!-- /ex -->

<!-- ex e04_06 -->
# Esercizio 6 — Due lavoratori a confronto *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e04_06.n}}$ lavoratori, ciascuno appartenente a uno e uno solo di quattro gruppi (single o sposati, laureati o non laureati), si è stimato il modello
>
> $$\log(\text{salario}) = \alpha + \delta_1\,\text{sp\_nl} + \delta_2\,\text{si\_l} + \delta_3\,\text{sp\_l} + \beta\,\text{esper} + \epsilon ,$$
>
> dove `sp_nl`, `si_l` e `sp_l` valgono 1 rispettivamente per gli sposati non laureati, i single laureati e gli sposati laureati, e 0 altrimenti, ed `esper` sono gli anni di esperienza. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti; la covarianza stimata fra $\hat\delta_3$ e $\hat\beta$ vale ${{e04_06.cov|m}}$.
>
> {{e04_06.tab.ols}}

> [!question] Testo della domanda
> **Domanda 6 *(3 punti)*.** Si considerino due lavoratori: A è sposato e laureato con ${{e04_06.ea|m}}$ anni di esperienza, B è single e non laureato con ${{e04_06.eb|m}}$ anni di esperienza. **(a)** Qual è la categoria di riferimento del modello? Si scriva la differenza attesa di $\log(\text{salario})$ fra A e B (A meno B) in funzione dei coefficienti. **(b)** Di quanto differisce in percentuale, in media, il salario di A da quello di B? **(c)** Quanto vale l'errore standard di tale differenza, in punti percentuali? **(d)** Qual è l'estremo inferiore dell'intervallo di confidenza al 95\% per la differenza, in percentuale? **(e)** E l'estremo superiore? **(f)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi che i due lavoratori abbiano lo stesso salario atteso, contro l'alternativa bilaterale.
<!-- /ex -->

<!-- ex e04_07 -->
# Esercizio 7 — Tre test $t$ non bastano: la significatività congiunta *(livello intermedio)*

> [!abstract] Dati
> Su $n = {{e04_07.n}}$ neolaureati si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{p\_mat} + \beta_2\,\text{p\_logica} + \beta_3\,\text{p\_lingua} + \epsilon ,$$
>
> dove `p_mat`, `p_logica` e `p_lingua` sono i punteggi ottenuti in tre test di ingresso (matematica, logica, lingua), che misurano in buona parte la stessa abilità e sono quindi molto correlati fra loro. Le stime OLS sono le seguenti.
>
> {{e04_07.tab.ols}}
>
> Per il test di significatività congiunta il modello ristretto contiene la sola costante, quindi $R^2_r=0$. Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà di questo test è ${{e04_07.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 7 *(3 punti)*.** **(a)** Quanti dei tre coefficienti sono significativamente diversi da zero al livello del 5\%, con un test $t$ bilaterale per ciascuno? **(b)** Si verifichi ora congiuntamente $H_0:\beta_1=\beta_2=\beta_3=0$ contro $H_1$: almeno un $\beta_j$ è diverso da zero. Quante restrizioni $s$ impone $H_0$? **(c)** Quanti sono i gradi di libertà $n-k-1$ del denominatore, con $k$ il numero di regressori, costante esclusa? **(d)** Quanto vale $F=\dfrac{(R^2_c-R^2_r)/s}{(1-R^2_c)/(n-k-1)}$? **(e)** Al livello del 5\%, confrontando $F$ con il valore critico, si decida se rifiutare o non rifiutare $H_0$. **(f)** Se i tre test $t$ fossero indipendenti, ciascuno al livello del 5\%, quale sarebbe la probabilità di rifiutare almeno una delle tre ipotesi $\beta_j=0$ quando sono tutte vere? Si risponda con quattro decimali.
<!-- /ex -->

<!-- ex e04_08 -->
# Esercizio 8 — Istruzione ed esperienza: l'interazione fra due regressori *(livello appello)*

> [!abstract] Dati
> Su $n = {{e04_08.n}}$ lavoratori si è stimato il modello
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,(\text{istr}\times\text{esper}) + \beta_4\,\text{donna} + \epsilon ,$$
>
> dove `istr` ed `esper` sono gli anni di istruzione e di esperienza, `istr_esp` è il prodotto `istr`$\times$`esper` e `donna` vale 1 per le donne e 0 per gli uomini. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti; la covarianza stimata fra $\hat\beta_1$ e $\hat\beta_3$ vale ${{e04_08.cov|m}}$.
>
> {{e04_08.tab.ols}}

> [!question] Testo della domanda
> **Domanda 8 *(4 punti)*.** **(a)** Si scriva l'effetto marginale dell'istruzione, cioè la variazione attesa di $\log(\text{salario})$ per un anno di istruzione in più, e si dica da che cosa dipende. **(b)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_3=0$ contro $H_1:\beta_3\neq 0$ (cioè se l'effetto dell'istruzione dipende dall'esperienza). **(c)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1=0$ contro $H_1:\beta_1\neq 0$, e si dica a quale lavoratore si riferisce $\beta_1$. **(d)** Di quanto varia in percentuale il salario atteso per un anno di istruzione in più, per un lavoratore con ${{e04_08.x0|m}}$ anni di esperienza? **(e)** Quanto vale l'errore standard di tale effetto, in punti percentuali? **(f)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_1+{{e04_08.x0|m}}\,\beta_3=0$ contro l'alternativa bilaterale.
<!-- /ex -->

<!-- ex e04_09 -->
# Esercizio 9 — Promozione e pubblicità: due negozi a confronto *(livello appello)*

> [!abstract] Dati
> Su $n = {{e04_09.n}}$ negozi si è stimato il modello
>
> $$\log(\text{vendite}) = \beta_0 + \beta_1\,\text{promo} + \beta_2\,\text{pub} + \beta_3\,(\text{pub}\times\text{promo}) + \epsilon ,$$
>
> dove `vendite` sono le vendite mensili, `promo` vale 1 se nel negozio è in corso una promozione e 0 altrimenti, `pub` è la spesa in pubblicità in migliaia di euro e `pub_promo` è il prodotto `pub`$\times$`promo`. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti. Le covarianze stimate fra gli stimatori valgono $\text{Cov}(\hat\beta_2,\hat\beta_3)={{e04_09.c_pp|m}}$, $\text{Cov}(\hat\beta_1,\hat\beta_2)={{e04_09.c_ap|m}}$ e $\text{Cov}(\hat\beta_1,\hat\beta_3)={{e04_09.c_ai|m}}$.
>
> {{e04_09.tab.ols}}

> [!question] Testo della domanda
> **Domanda 9 *(4 punti)*.** **(a)** Di quanto variano in percentuale, in media, le vendite di un negozio con promozione per mille euro in più di pubblicità? **(b)** Un consulente sostiene che, in un negozio con promozione, ogni mille euro in più di pubblicità fa crescere le vendite del 2\%, cioè $\beta_2+\beta_3={{e04_09.kappa|m}}$. Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\beta_2+\beta_3={{e04_09.kappa|m}}$ contro l'alternativa bilaterale. Si considerino ora il negozio A, con promozione e ${{e04_09.pa|m}}$ mila euro di pubblicità, e il negozio B, senza promozione e con ${{e04_09.pb|m}}$ mila euro di pubblicità. **(c)** Di quanto differiscono in percentuale, in media, le vendite di A da quelle di B (A meno B)? **(d)** Quanto vale l'errore standard di tale differenza, in punti percentuali? **(e)** Al livello del 5\%, si decida se rifiutare o non rifiutare l'ipotesi che i due negozi abbiano le stesse vendite attese, contro l'alternativa bilaterale.
<!-- /ex -->

<!-- ex e04_10 -->
# Esercizio 10 — Zone senza costante: livelli, vincoli e riferimento *(livello appello)*

> [!abstract] Dati
> Su $n = {{e04_10.n}}$ abitazioni si è stimato il modello, senza costante,
>
> $$\log(\text{prezzo}) = \delta_1\,\text{zona1} + \delta_2\,\text{zona2} + \delta_3\,\text{zona3} + \delta_4\,\text{zona4} + \beta_1\,\text{crime} + \beta_2\,\text{rooms} + \epsilon ,$$
>
> dove `zona1`, ..., `zona4` sono dummy che valgono 1 se l'abitazione si trova in quella zona e 0 altrimenti (ogni abitazione appartiene a una e una sola zona, quindi $\text{zona1}+\text{zona2}+\text{zona3}+\text{zona4}=1$), `crime` è il tasso di criminalità e `rooms` il numero medio di stanze. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$.
>
> {{e04_10.tab.completo}}
>
> Per verificare se la zona ha rilevanza nel livello dei prezzi si è stimato anche il modello ristretto, con una sola costante comune a tutte le zone. Nessuno dei due modelli stampa l'$R^2$, ma entrambi hanno la stessa variabile dipendente.
>
> {{e04_10.tab.ristretto}}
>
> Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà di questo test è ${{e04_10.fcrit|m}}$.

> [!question] Testo della domanda
> **Domanda 10 *(4 punti)*.** **(a)** Si spieghi perché nel modello completo non è stata eliminata nessuna dummy e che cosa misura ciascun $\delta_j$. **(b)** Si scriva il sistema d'ipotesi del test $F$ con cui si verifica se la zona ha rilevanza nel livello dei prezzi. **(c)** Quante restrizioni $s$ impone $H_0$? **(d)** Quanti sono i gradi di libertà del denominatore, cioè $n$ meno il numero di parametri stimati nel modello completo? **(e)** Quanto vale $F=\dfrac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-p)}$, con $p$ il numero di parametri del modello completo? **(f)** Al livello del 5\%, confrontando $F$ con il valore critico, si decida se rifiutare o non rifiutare $H_0$. Si stimi ora lo stesso modello con una costante e le dummy `zona1`, `zona2` e `zona3`, quindi con la zona 4 come categoria di riferimento. **(g)** Quanto vale la stima della costante? **(h)** Quanto vale la stima del coefficiente di `zona1`, in percentuale?
<!-- /ex -->

<!-- ex e04_11 -->
# Esercizio 11 — Cambiare la categoria di riferimento *(livello appello)*

> [!abstract] Dati
> Su $n = {{e04_11.n}}$ famiglie si è stimato il modello
>
> $$\log(\text{reddito}) = \alpha + \delta_1\,\text{nord} + \delta_2\,\text{sud} + \beta_1\,\text{istr} + \beta_2\,\text{eta} + \epsilon ,$$
>
> dove `nord` e `sud` valgono 1 per le famiglie residenti in quell'area e 0 altrimenti (le famiglie del Centro sono la categoria di riferimento), `istr` sono gli anni di istruzione e `eta` l'età del capofamiglia. Le variazioni percentuali si calcolano con l'approssimazione $\Delta\%\,y\approx 100\,\Delta\log(y)$. Le stime OLS sono le seguenti; la covarianza stimata fra $\hat\delta_1$ e $\hat\delta_2$ vale ${{e04_11.cov|m}}$.
>
> {{e04_11.tab.ols}}

> [!question] Testo della domanda
> **Domanda 11 *(4 punti)*.** **(a)** Al livello del 5\%, si decida se rifiutare o non rifiutare $H_0:\delta_1=0$ contro $H_1:\delta_1\neq 0$ (Nord contro Centro). **(b)** Lo stesso per $H_0:\delta_2=0$ (Sud contro Centro). Si riscriva ora il modello scegliendo il Sud come categoria di riferimento, con le dummy `centro` e `nord`:
> $\log(\text{reddito}) = \alpha' + \delta_1'\,\text{centro} + \delta_2'\,\text{nord} + \beta_1\,\text{istr} + \beta_2\,\text{eta} + \epsilon$. **(c)** Quanto vale la stima di $\delta_1'$, in percentuale? **(d)** Quanto vale la stima di $\delta_2'$, in percentuale? **(e)** Quanto vale l'errore standard di $\hat\delta_2'$, in punti percentuali? **(f)** Al livello del 5\%, nel nuovo modello si decida se rifiutare o non rifiutare $H_0:\delta_2'=0$ contro $H_1:\delta_2'\neq 0$. **(g)** Il test $F$ per $H_0$: «l'area non ha rilevanza» cambierebbe passando dal Centro al Sud come categoria di riferimento? Si risponda sì o no.
<!-- /ex -->

<!-- ex e04_12 -->
# Esercizio 12 — Due restrizioni insieme: riscrivere il modello *(livello appello)*

> [!abstract] Dati
> Su $n = {{e04_12.n}}$ lavoratori si è stimato il modello completo
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,\text{istr} + \beta_2\,\text{esper} + \beta_3\,\text{anz} + \beta_4\,\text{donna} + \epsilon ,$$
>
> dove `istr`, `esper` e `anz` sono gli anni di istruzione, di esperienza e di anzianità in azienda e `donna` vale 1 per le donne e 0 per gli uomini.
>
> {{e04_12.tab.completo}}
>
> Si vuole verificare congiuntamente che un anno di istruzione e un anno di esperienza abbiano lo stesso effetto e che l'anzianità non abbia effetto: $H_0:\beta_1=\beta_2$ e $\beta_3=0$, contro $H_1$: almeno una delle due condizioni non vale. Sotto $H_0$ il modello diventa
>
> $$\log(\text{salario}) = \beta_0 + \beta_1\,(\text{istr}+\text{esper}) + \beta_4\,\text{donna} + \epsilon ,$$
>
> che si è stimato con il regressore `istr_esper` $=$ `istr` $+$ `esper`.
>
> {{e04_12.tab.ristretto}}
>
> Il valore critico al 5\% della distribuzione $F$ con i gradi di libertà di questo test è ${{e04_12.fcrit|m}}$. La covarianza stimata fra $\hat\beta_1$ e $\hat\beta_2$ nel modello completo vale ${{e04_12.cov|m}}$.

> [!question] Testo della domanda
> **Domanda 12 *(4 punti)*.** Sia $k$ il numero di regressori del modello completo, costante esclusa. **(a)** Quante restrizioni $s$ impone $H_0$? **(b)** Quanti sono i gradi di libertà $n-k-1$ del denominatore? **(c)** Quanto vale $F=\dfrac{(\text{SSR}_r-\text{SSR}_c)/s}{\text{SSR}_c/(n-k-1)}$? **(d)** Al livello del 5\%, confrontando $F$ con il valore critico, si decida se rifiutare o non rifiutare $H_0$. **(e)** Si consideri ora la sola restrizione $H_0:\beta_1=\beta_2$ ($s=1$), per cui $F=t^2$ con $t=\dfrac{\hat\beta_1-\hat\beta_2}{\widehat{\text{se}}(\hat\beta_1-\hat\beta_2)}$: quanto vale $F$? **(f)** Al livello del 5\%, con la stessa $t$, si decida se rifiutare o non rifiutare $H_0:\beta_1=\beta_2$ contro $H_1:\beta_1\neq\beta_2$. **(g)** Si spieghi come si ottiene il modello ristretto da quello completo.
<!-- /ex -->
