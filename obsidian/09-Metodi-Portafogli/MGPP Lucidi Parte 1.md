---
title: "Metodi per la Gestione dei Portafogli Personali — Parte 1: Introduzione alla Teoria del Portafoglio"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-1.pdf"
pages: 61
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione: perché serve un'economia finanziaria

*Corso: Metodi per la Gestione dei Portafogli Personali — Marco Corazza, Dipartimento di Economia, Università Ca' Foscari di Venezia.*

**Domanda.** Perché serve un'economia finanziaria, cioè un'economia della finanza?

**Risposta.** Si parte dal ben noto problema di scelta del consumatore, nella sua forma più semplice:

$$\max_{q_1,\dots,q_N} u(q_1,\dots,q_N) \quad \text{s.t.} \quad \begin{cases} \sum_{i=1}^{N} q_i p_i = M \\ q_i \geq 0,\ i=1,\dots,N \end{cases}$$

dove:
- $q_1,\dots,q_N$: le quantità del primo, ..., dell'$N$-esimo bene/servizio da acquistare;
- $u(\cdot,\dots,\cdot)$: la funzione di utilità del consumatore;
- $M$: il reddito del consumatore;
- $p_1>0,\dots,p_N>0$: il prezzo del primo, ..., dell'$N$-esimo bene/servizio.

**Figura** — Curve di indifferenza $U_0<U_1<U_2<U_3$ nel piano $(q_1,q_2)$, con vincolo di bilancio rappresentato dal segmento $AB$ e punto di ottimo $E$, dato dalla tangenza tra la retta di bilancio e la curva di indifferenza più alta raggiungibile. La figura illustra graficamente la soluzione del problema di massimizzazione vincolata sopra formalizzato.

**Domanda.** Qual è l'ipotesi implicita del modello sottostante?

**Risposta.** Dato l'istante temporale $t$ in cui è definita la parte di economia considerata, l'ipotesi implicita consiste nell'idea che tale parte di economia nasca, viva e muoia in $t$, senza alcuna relazione con le parti della stessa economia definite in istanti temporali futuri.

In generale questa ipotesi implicita non è realistica: molti consumatori non utilizzano tutto il proprio reddito corrente $M$ per consumi correnti, ma trasferiscono a istanti futuri la parte rimanente di tale reddito per consumi futuri.

> «[In termini generali,] un consumatore affronta tipicamente due importanti decisioni economiche. Primo, come allocare il proprio consumo corrente tra beni e servizi. Secondo, come investire tra vari asset. Questi due problemi del consumatore o della famiglia, tra loro correlati, sono noti come la decisione di consumo–risparmio e la decisione di selezione di portafoglio.»
> — Constantinides G.M. e Malliaris A.G., in Jarrow R.A., Maksimovic V. e Ziemba W.T. (a cura di), *Finance*, 1995 (pag. 1)

**Nota.** La necessità di investire, cioè di trasferire ricchezza corrente a istanti futuri, è la ragione per cui serve un'economia finanziaria.

Il corso si concentra sulla seconda decisione economica ("come investire tra vari asset"). Si noti che:
- l'investimento tra vari asset ha lo scopo di trasferire ricchezza dal periodo corrente a quello futuro;
- il futuro è più o meno sconosciuto.

Pertanto, investire è un'attività rischiosa.

**Domanda.** Che tipo di rischiosità deve affrontare il consumatore/investitore?

**Figura** — Valori giornalieri dell'indice azionario Dow Jones Industrial Average (DJIA), con riferimenti temporali evidenziati: 19.10.1987, 25.08.1987, 04.01.1988, 01.07.1988, 03.01.1989, 03.07.1989, 09.10.1989. Il grafico mostra un andamento fortemente irregolare, incluso il crollo dell'ottobre 1987, tipico di una dinamica di tipo random walk.

**Risposta.** Più o meno, la rischiosità affrontata dal consumatore/investitore è del tipo coinvolto in un random walk.

**Nota.** Pertanto, l'economia finanziaria fornisce la teoria, i metodi, gli strumenti... con cui trasferire ricchezza corrente a istanti futuri gestendo l'incertezza.

*(slide 1–11)*

## Richiami di matematica: le scelte di investimento stocastiche

> [!abstract] Definizione
> **La matematica necessaria: un richiamo.**
>
> Sia $\mathbb{X}=\{X_1,\dots,X_N\}$ un insieme di $N$ scelte di investimento stocastiche. Ciascuna di queste variabili aleatorie è caratterizzata da esiti negativi/positivi con probabilità date.
>
> **Esempio.** Nel caso in cui $X_i$, con $i\in\{1,\dots,N\}$, sia una variabile aleatoria discreta, si ha
>
> $$X_i = \{(x_{i,1},p_{i,1}),\dots,(x_{i,j},p_{i,j}),\dots,(x_{i,M_i},p_{i,M_i})\},$$
>
> dove:
> - $x_{i,j}$, con $j=1,\dots,M_i$, è la $j$-esima realizzazione di $X_i$;
> - $p_{i,j}$, con $j=1,\dots,M_i$, è la probabilità di occorrenza di $x_{i,j}$, con $0\le p_{i,j}\le 1$ per ogni $j$ e $\sum_{j=1}^{M_i} p_{i,j}=1$.
>
> **Domanda.** Come individuare le scelte di investimento stocastiche ottimali dal punto di vista dell'investitore?
>
> **Risposta.** Dipende dall'attitudine dell'investitore verso l'aleatorietà. In generale:
> - l'investitore "razionale" preferisce di più a meno;
> - l'investitore "razionale" è avverso al rischio (risk-avers).

*(slide 12–13)*

## Definizione di portafoglio finanziario

> [!abstract] Definizione
> **Definizione — (Financial) portfolio.** Sia $W$ una data ricchezza e sia $\mathbb{X}=\{X_1,\dots,X_N\}$ un insieme di $N$ scelte di investimento (ad es. un mercato azionario). Si definisce come (finanziario) portafoglio un $N$-vettore
>
> $$\mathbf{x}' = (x_1,\dots,x_N)$$
>
> tale che il suo generico elemento $x_i$, con $i=1,\dots,N$, indica la percentuale di $W$ investita in $X_i$, con $\sum_{i=1}^{N} x_i = 1$. $\square$
>
> > «[In termini generali,] un portafoglio [è lo strumento tecnico] che "trasferisce" ricchezza da un periodo al successivo.»
> > — Ingersoll J.E. jr., *Theory of Financial Decision Making*, 1987 (pag. 46)
>
> **Esempio.** Sia $\mathbb{X}=\{X_{\text{Eni}}, X_{\text{Fiat}}, X_{\text{Generali}}, X_{\text{Mediaset}}, X_{\text{Telecom IT}}\}$ un insieme di 5 titoli azionari. Un possibile portafoglio finanziario è il seguente 5-vettore
>
> $$\mathbf{x}' = (x_{\text{Eni}}=0.10,\ x_{\text{Fiat}}=0.20,\ x_{\text{Generali}}=0.15,\ x_{\text{Mediaset}}=0.00,\ x_{\text{Telecom IT}}=0.55).$$
>
> Si noti che $x_{\text{Eni}}+x_{\text{Fiat}}+x_{\text{Generali}}+x_{\text{Mediaset}}+x_{\text{Telecom IT}}=1$.

*(slide 14–16)*

## Misura della performance single-period: rendimento percentuale e rendimento logaritmico

> [!abstract] Definizione
> **Domanda.** Come misurare la performance (single-period) di una scelta di investimento?
>
> **Risposta.** Dipende dalla legge scelta per descrivere la dinamica del prezzo della data scelta di investimento.
>
> **Rendimento percentuale netto (matematica finanziaria).**
>
> $$P_t = P_{t-\Delta t}(1+R_{\%,\Delta t}) - D_{(t-\Delta t,t]}$$
>
> dove:
> - $P_t$ è il prezzo in $t$;
> - $D_{(t-\Delta t,t]}\ge 0$ è il dividendo pagato in $(t-\Delta t,t]$;
> - $R_{\%,\Delta t}$ è il rendimento percentuale netto (single-period) da $t-\Delta t$ a $t$.
>
> Da questa dinamica si ottiene (facilmente):
>
> $$R_{\%,\Delta t} = \frac{P_t + D_{(t-\Delta t,t]} - P_{t-\Delta t}}{P_{t-\Delta t}}.$$
>
> **Nota.** Se $R_{\%,\Delta t} < D_{(t-\Delta t,t]}/P_{t-\Delta t} - 1$, con $P_{t-\Delta t}>0$, allora $P_t<0$.
>
> **Rendimento logaritmico netto (finanza matematica).**
>
> $$P_t = P_{t-\Delta t}\,e^{R_{\ln,\Delta t}} - D_{(t-\Delta t,t]}$$
>
> dove $P_t$, $D_{(t-\Delta t,t]}$ sono definiti come sopra e $R_{\ln,\Delta t}$ è il rendimento logaritmico netto (single-period) da $t-\Delta t$ a $t$.
>
> Da questa dinamica si ottiene:
>
> $$R_{\ln,\Delta t} = \ln\left(\frac{P_t + D_{(t-\Delta t,t]}}{P_{t-\Delta t}}\right).$$
>
> **Nota.**
> - Se $D_{(t-\Delta t,t]}=0$ e $P_{t-\Delta t}>0$, allora $P_t>0$ per qualsiasi $R_{\ln,\Delta t}$.
> - Se $R_{\ln,\Delta t} < \ln\left(D_{(t-\Delta t,t]}/P_{t-\Delta t}\right)$, con $D_{(t-\Delta t,t]}>0$ e $P_{t-\Delta t}>0$, allora $P_t<0$.

*(slide 17–21)*

## Equivalenza asintotica e (non) additività dei rendimenti percentuale e logaritmico

> [!note] Dimostrazione
> **Domanda.** Che tipo di rendimento usare?
>
> **Risposta.** Se $R_{\%,\Delta t}\in(-1,1)=(-100\%,100\%)$ allora $R_{\%,\Delta t}\simeq R_{\ln,\Delta t}$.
>
> **Dimostrazione.** Infatti:
>
> $$\begin{aligned}
> R_{\ln,\Delta t} &= \ln\left(\frac{P_t+D_{(t-\Delta t,t]}}{P_{t-\Delta t}}\right) \\
> &= \ln\left(1+\frac{P_t+D_{(t-\Delta t,t]}}{P_{t-\Delta t}}-1\right) \\
> &= \ln\left(1+\frac{P_t+D_{(t-\Delta t,t]}-P_{t-\Delta t}}{P_{t-\Delta t}}\right) \\
> &= \ln(1+R_{\%,\Delta t}).
> \end{aligned}$$
>
> Ricordando che lo sviluppo in serie di Taylor della funzione $\ln(1+x)$ è $\sum_{i=1}^{+\infty}(-1)^{i-1}\dfrac{x^i}{i}$ per $x\in(-1,1)$, si ha:
>
> $$R_{\ln,\Delta t} = \ln(1+R_{\%,\Delta t}) = R_{\%,\Delta t} - \frac{R_{\%,\Delta t}^2}{2} + \frac{R_{\%,\Delta t}^3}{3} - \frac{R_{\%,\Delta t}^4}{4} + \dots$$
>
> per $R_{\%,\Delta t}\in(-100\%,100\%)$. $\blacksquare$
>
> **Domanda.** Quando $R_{\%,\Delta t}\in(-100\%,100\%)$?
>
> **Risposta.** Generalmente, quando $\Delta t$ è sufficientemente piccolo ($\Delta t=1$ giorno, $\Delta t=1$ settimana, $\Delta t=1$ mese, ...).
>
> **Nota.** Ciò nonostante, $R_{\%,\Delta t}$ non è additivo nel tempo, mentre $R_{\ln,\Delta t}$ lo è.
>
> **Esempio (caso generale).** Si consideri quanto segue:
>
> | $t$ | Prezzo | $R_{\%,1}$ | $R_{\%,2}$ | $R_{\ln,1}$ | $R_{\ln,2}$ |
> |---|---|---|---|---|---|
> | 0 | $P_0$ | | | | |
> | 1 | $P_1$ | $\dfrac{P_1-P_0}{P_0}$ | | $\ln\left(\dfrac{P_1}{P_0}\right)$ | |
> | 2 | $P_2$ | $\dfrac{P_2-P_1}{P_1}$ | $\dfrac{P_2-P_0}{P_0}$ | $\ln\left(\dfrac{P_2}{P_1}\right)$ | $\ln\left(\dfrac{P_2}{P_0}\right)$ |
>
> da cui:
>
> $$R_{\%,(0,1]}+R_{\%,(1,2]} = \dots = \frac{P_1^2-2P_0P_1+P_0P_1}{P_0P_1} \neq R_{\%,(0,2]} = \frac{P_2-P_0}{P_0};$$
>
> $$R_{\ln,(0,1]}+R_{\ln,(1,2]} = \dots = \ln\left(\frac{P_2}{P_0}\right) = R_{\ln,(0,2]} = \ln\left(\frac{P_2}{P_0}\right).$$
>
> Si conferma dunque analiticamente che il rendimento percentuale a un periodo non è additivo, mentre quello logaritmico lo è.
>
> **Esempio numerico.** Si consideri la seguente esemplificazione numerica:
>
> | $t$ | Prezzo | $R_{\%,1}$ | $R_{\%,2}$ | $R_{\ln,1}$ | $R_{\ln,2}$ |
> |---|---|---|---|---|---|
> | 0 | 100 | | | | |
> | 1 | 125 | 25.00% | | 22.31% | |
> | 2 | 100 | −20.00% | 0.00% | −22.31% | 0.00% |
> | **Sum** | | 5.00% | 0.00% | 0.00% | 0.00% |
>
> La somma dei rendimenti percentuali a un periodo ($25.00\%-20.00\%=5.00\%$) non coincide con il rendimento percentuale a due periodi ($0.00\%$), mentre la somma dei rendimenti logaritmici a un periodo ($22.31\%-22.31\%=0.00\%$) coincide con il rendimento logaritmico a due periodi ($0.00\%$), confermando numericamente quanto dimostrato sopra.

*(slide 22–28)*

## La selezione di portafoglio in condizioni di incertezza: impostazione single-period

**Domanda.** Come effettuare la selezione di portafoglio sotto incertezza (in un'economia a singolo periodo)?

**Risposta.**

> «In generale, le due decisioni non possono essere prese in modo indipendente. Tuttavia, molti dei risultati importanti della teoria di portafoglio possono essere derivati più facilmente in un ambiente a singolo periodo, dove l'allocazione consumo–risparmio ha un impatto sostanziale limitato sui risultati.»
> — Constantinides G.M. e Malliaris A.G., in Jarrow R.A., Maksimovic V. e Ziemba W.T. (a cura di), *Finance*, 1995 (pag. 1)

Quindi, in un'economia a singolo periodo, si può formalizzare direttamente il problema di selezione di portafoglio senza prestare attenzione a quello di consumo–risparmio.

**Nota.**

> «La metodologia del calcolo deterministico è adeguata per la decisione di massimizzare l'utilità di un consumatore soggetta a un vincolo di bilancio. La selezione di portafoglio implica prendere una decisione sotto incertezza.»
> — Constantinides G.M. e Malliaris A.G., in Jarrow R.A., Maksimovic V. e Ziemba W.T. (a cura di), *Finance*, 1995 (pag. 1)

Si individuano tre passi:

1. **Primo**, identificare uno strumento con cui "misurare" l'incertezza associata a una data scelta di investimento;
2. **Secondo**, definire un criterio di efficienza con cui «dividere tutte le possibili scelte di investimento in due insiemi mutuamente esclusivi — un insieme efficiente e un insieme inefficiente» (Szegö G.P., *Portfolio Theory. With Application to Bank Asset Management*, 1980, pag. 8);
3. **Terzo**, specificare un approccio di ottimizzazione appropriato per individuare la scelta di investimento ottimale tra quelle efficienti. In particolare:
   - dato un limite superiore per il rischio della scelta di investimento, massimizzare il rendimento di tale scelta;
   - dato un limite inferiore per il rendimento della scelta di investimento, minimizzare il rischio di tale scelta;
   - ottimizzare un opportuno indice di sintesi basato su rendimento e rischio della scelta di investimento (ad es. massimizzare "rendimento $-\lambda\cdot$rischio", in cui $\lambda>0$ è una qualche misura dell'avversione al rischio dell'agente economico);
   - massimizzare una funzione di utilità di von Neumann–Morgenstern;
   - ...

**Domanda.** Cosa significa che una scelta di investimento è efficiente rispetto a un dato criterio di dominanza?

**Risposta.** Significa che tale scelta di investimento non è dominata da nessun'altra scelta di investimento nel senso del criterio di dominanza dato.

**Esempio.** Selezionare un portafoglio efficiente è (più o meno) come scegliere una pizza da un menù:
- incertezza = varietà degli ingredienti nella pizza;
- criterio di efficienza = presenza del pomodoro (nel caso del docente);
- quantità da ottimizzare = spessore della pasta, da minimizzare, ed equilibrio dei sapori, da massimizzare (nel caso del docente).

*(slide 29–34)*

## Media e varianza come strumenti di misura del rendimento e del rischio

> [!abstract] Definizione
> **Lo strumento.** Si considera come strumento stocastico con cui "misurare" l'incertezza associata alla $i$-esima scelta di investimento, con $i=1,\dots,N$ (e al portafoglio), una coppia di indici statistici relativi alla variabile aleatoria identificata dal rendimento single-period della $i$-esima scelta di investimento stessa:
> - la **media** di questo rendimento single-period;
> - la **varianza** di questo rendimento single-period.
>
> > «Consideriamo la regola secondo cui l'investitore considera (o dovrebbe considerare) il rendimento atteso una cosa desiderabile e la varianza del rendimento una cosa indesiderabile.»
> > — Markowitz H., *Portfolio selection*, The Journal of Finance, 1952 (pag. 77)
>
> > «La principale innovazione introdotta da Markowitz fu misurare il rischio di un portafoglio tramite la distribuzione congiunta (multivariata) dei rendimenti di tutti gli asset. Le distribuzioni multivariate sono caratterizzate dalle proprietà statistiche (marginali) di tutte le variabili aleatorie componenti e dalla loro struttura di dipendenza. Markowitz descrisse le prime tramite i primi due momenti delle distribuzioni univariate — i rendimenti degli asset — e la seconda tramite il coefficiente di correlazione lineare (di Pearson) tra ciascuna coppia di rendimenti aleatori [...].»
> > — Szegö G., *Measures of risk*, European Journal of Operational Research, 2005 (pag. 5)
>
> **Media di $R$: $\mathbb{E}(R)=r$**
>
> - In termini generali, la media di una variabile aleatoria è un indice statistico di posizione.
> - Dal punto di vista finanziario, si considera la media del rendimento di una scelta di investimento come misura della redditività della scelta di investimento stessa.
> - Qualsiasi momento dispari del rendimento può essere considerato come misura di redditività.
>
> Sia $X$ una variabile aleatoria discreta, cioè
>
> $$X=\{(x_1,p_1),\dots,(x_i,p_i),\dots,(x_M,p_M)\},$$
>
> dove $x_i$, con $i=1,\dots,M$, è l'$i$-esima realizzazione di $X$; $p_i$, con $i=1,\dots,M$, è la probabilità di occorrenza di $x_i$, con $0\le p_i\le 1$ per ogni $i$ e $\sum_{i=1}^M p_i=1$. Allora
>
> $$\mathbb{E}(X) = \sum_{i=1}^{M} x_i p_i.$$
>
> Sia $X$ una variabile aleatoria continua caratterizzata da una funzione di distribuzione cumulata $F_X(\cdot)$ e/o da una funzione di densità di probabilità $f_X(\cdot)$. Allora
>
> $$\mathbb{E}(X) = \int_{-\infty}^{+\infty} t\,dF(t) \quad \text{e/o} \quad \mathbb{E}(X) = \int_{-\infty}^{+\infty} t f(t)\,dt.$$
>
> **Nota.** Nel caso di variabile aleatoria continua, $\mathbb{E}(X)$ potrebbe non esistere.
>
> **Varianza di $R$: $\mathbb{Var}(R)=\sigma^2$**
>
> - In termini generali, la varianza di una variabile aleatoria è un indice statistico di variabilità.
> - Dal punto di vista finanziario, si considera la varianza del rendimento di una scelta di investimento come misura del rischio della scelta di investimento stessa.
> - Qualsiasi momento pari del rendimento può essere considerato come misura di rischio.
>
> Caso discreto:
>
> $$\mathbb{Var}(X) = \sum_{i=1}^{M} (x_i-\mathbb{E}(x))^2 p_i.$$
>
> Caso continuo:
>
> $$\mathbb{Var}(X) = \int_{-\infty}^{+\infty} (t-\mathbb{E}(X))^2\,dF(t) \quad \text{e/o} \quad \mathbb{Var}(X) = \int_{-\infty}^{+\infty} (t-\mathbb{E}(X))^2 f(t)\,dt.$$
>
> **Nota.** Nel caso di variabile aleatoria continua, $\mathbb{Var}(X)$ potrebbe non esistere.
>
> **Domanda.** La media e la varianza di una variabile aleatoria sono in grado di caratterizzarla pienamente?
>
> **Risposta.** In generale, no!

*(slide 35–44)*

## Un limite della varianza come misura di rischio: semi-varianza e deviazione media assoluta

> [!example] Esempio
> **Domanda.** La varianza del rendimento di una scelta di investimento è una "buona" misura del rischio della scelta di investimento stessa?
>
> **Risposta.** In generale, no! Si illustra un limite della varianza come misura di rischio tramite l'esempio seguente.
>
> **Esempio.** Sia $R$ il seguente rendimento aleatorio discreto di una scelta di investimento:
>
> $$R = \left\{\left(1\%,\frac14\right),\left(3\%,\frac15\right),\left(9\%,\frac14\right),\left(10\%,\frac15\right),\left(12\%,\frac{1}{10}\right)\right\}.$$
>
> La media di $R$ è:
>
> $$\mathbb{E}(R) = 1\%\cdot\frac14 + 3\%\cdot\frac15 + 9\%\cdot\frac14 + 10\%\cdot\frac15 + 12\%\cdot\frac{1}{10} = 6.3\%.$$
>
> La varianza di $R$ è:
>
> $$\begin{aligned}
> \mathbb{Var}(R) &= [(1-6.3)\%]^2\frac14 + [(3-6.3)\%]^2\frac15 + \\
> &\quad + [(9-6.3)\%]^2\frac14 + [(10-6.3)\%]^2\frac15 + \\
> &\quad + [(12-6.3)\%]^2\frac{1}{10} = (4.124318\%)^2 = 17.01\%^2.
> \end{aligned}$$
>
> Si considerano ora gli scarti delle realizzazioni di $R$ dalla sua media:
>
> | Scarto | Valore | Segno |
> |---|---|---|
> | $(1-6.3)\%$ | $-5.3\%$ | $<0\%$ |
> | $(3-6.3)\%$ | $-3.3\%$ | $<0\%$ |
> | $(9-6.3)\%$ | $1.7\%$ | $>0\%$ |
> | $(10-6.3)\%$ | $2.7\%$ | $>0\%$ |
> | $(12-6.3)\%$ | $5.7\%$ | $>0\%$ |
>
> **Domanda.** Le ultime tre differenze sono rischiose?
>
> **Risposta.** Non lo sono! Sono scostamenti positivi rispetto alla media (l'investimento rende più del valore atteso), ma la varianza, elevando al quadrato tutti gli scarti, li penalizza esattamente come gli scostamenti negativi. Questo è un limite intrinseco della varianza come misura di rischio.
>
> **Misura alternativa: la semi-varianza.** Se $R$ è un rendimento aleatorio discreto:
>
> $$\text{semi-}\mathbb{Var}(R) = \sum_{i=1}^{M} (\min\{0, x_i-\mathbb{E}(R)\})^2 p_i;$$
>
> se $R$ è un rendimento aleatorio continuo:
>
> $$\text{semi-}\mathbb{Var}(R) = \int_{-\infty}^{+\infty} (\min\{0,t-\mathbb{E}(R)\})^2\,dF_R(t) \quad \text{e/o} \quad \text{semi-}\mathbb{Var}(R) = \int_{-\infty}^{+\infty} (\min\{0,t-\mathbb{E}(R)\})^2 f_R(t)\,dt.$$
>
> Nell'esempio, la semi-varianza di $R$ è:
>
> $$\begin{aligned}
> \text{semi-}\mathbb{Var}(R) &= (-5.3\%)^2\frac14 + (-3.3\%)^2\frac15 + (0\%)^2\frac14 + \\
> &\quad + (0\%)^2\frac15 + (0\%)^2\frac{1}{10} \\
> &= (3.03323259905995\%)^2 = 9.2005\%^2 < 17.01\%^2 = \mathbb{Var}(R).
> \end{aligned}$$
>
> **Un'altra misura alternativa: la deviazione media assoluta (MAD).** Se $R$ è un rendimento aleatorio discreto:
>
> $$\text{MAD}(R) = \sum_{i=1}^{M} |x_i-\mathbb{E}(R)|\,p_i;$$
>
> se $R$ è un rendimento aleatorio continuo:
>
> $$\text{MAD}(R) = \int_{-\infty}^{+\infty} |t-\mathbb{E}(R)|\,dF_R(t) \quad \text{e/o} \quad \text{MAD}(R) = \int_{-\infty}^{+\infty} |t-\mathbb{E}(R)|\,f_R(t)\,dt.$$
>
> Nell'esempio, la deviazione media assoluta di $R$ è:
>
> $$\begin{aligned}
> \text{MAD}(R) &= |{-5.3\%}|\frac14 + |{-3.3\%}|\frac15 + |1.7\%|\frac14 + \\
> &\quad + |2.7\%|\frac15 + |5.7\%|\frac{1}{10} = 3.52\%.
> \end{aligned}$$
>
> **Nota.** La deviazione media assoluta non è direttamente confrontabile con la varianza, ma il suo quadrato lo è:
>
> $$\text{MAD}^2(R) = (3.52\%)^2 = 12.3904\%^2 < 17.01\%^2 = \mathbb{Var}(R).$$
>
> **Osservazioni.** Ad ogni modo, semi-$\mathbb{Var}(\cdot)$ e $\text{MAD}(\cdot)$ non sono misure di rischio migliori di $\mathbb{Var}(\cdot)$.
>
> > «D'altro canto la varianza gode di vantaggi analitici che altre misure di variabilità non hanno.»
> > — Bortot P., Magnani U., Olivieri G., Rossi F.A. e Torrigiani M., *Matematica Finanziaria*, 1993 (pag. 444).

*(slide 45–53)*

## Il criterio di dominanza media-varianza

> [!abstract] Definizione
> **Il criterio di efficienza.** Si considera come criterio di efficienza con cui «dividere tutte le possibili scelte di investimento in due insiemi mutuamente esclusivi — un insieme efficiente e un insieme inefficiente» (Szegö G.P., *Portfolio Theory. With Application to Bank Asset Management*, 1980, pag. 8) il seguente, basato sui concetti di media e varianza.
>
> **Definizione — Criterio di dominanza media-varianza.** Siano $X_1$ e $X_2$ due variabili aleatorie (ad es. rendimenti di portafoglio). Si dice che $X_1$ **domina** $X_2$, ovvero che $X_1$ è preferita a $X_2$, nel senso della dominanza media-varianza se
>
> $$\mathbb{E}(X_1) \geq \mathbb{E}(X_2) \quad \text{e} \quad \mathbb{Var}(X_1) \leq \mathbb{Var}(X_2)$$
>
> e almeno una delle due disuguaglianze è soddisfatta in forma stretta. $\square$
>
> **Notazione.**
> - $X_1\succ_{MV}X_2$: $X_1$ domina $X_2$ nel senso della dominanza media-varianza;
> - $X_1\sim_{MV}X_2$ oppure $X_1=_{MV}X_2$: $X_1$ è indifferente a $X_2$ nel senso della dominanza media-varianza;
> - $X_1\succeq_{MV}X_2$: $X_1$ domina o è indifferente a $X_2$ nel senso della dominanza media-varianza.
>
> **Esempio.** Sia $\mathbb{X}=\{X_1,X_2,X_3\}$ un insieme di scelte di investimento. Le medie e le varianze dei rendimenti di $X_1$, $X_2$ e $X_3$ sono rispettivamente:
>
> $$\mathbb{E}(R_1)=4 \text{ e } \mathbb{Var}(X_1)=3,\qquad \mathbb{E}(R_2)=2 \text{ e } \mathbb{Var}(X_2)=7,\qquad \mathbb{E}(R_3)=6 \text{ e } \mathbb{Var}(X_3)=5.$$
>
> Quindi:
>
> $$X_1\succ_{MV}X_2,\qquad X_1 \mathbin{?}_{MV} X_3,\qquad X_2\prec_{MV}X_3.$$
>
> ($X_1$ ha media maggiore di $X_3$ ma anche varianza minore: nessuna delle due domina l'altra secondo il criterio media-varianza — sono non confrontabili.)
>
> **Figura** — Piano $(\mathbb{Var}(X),\mathbb{E}(X))$ suddiviso in quadranti a partire da un punto dato. Nel quadrante in alto a destra (varianza maggiore e media maggiore rispetto al punto dato) e in quello in basso a sinistra (varianza minore e media minore) compare un punto interrogativo: la dominanza in questi quadranti non è determinabile con il solo criterio media-varianza. La figura mostra graficamente perché il criterio di dominanza media-varianza produce solo un **ordinamento parziale** delle scelte di investimento.
>
> **Nota.** Probabilmente il modo più "naturale" (dal punto di vista finanziario) di utilizzare il criterio di dominanza media-varianza consiste nell'indurre un ordinamento in un dato insieme di scelte di investimento, cioè
>
> $$\mathbb{X}=\{X_1,\dots,X_N\} \ \xrightarrow{\ MV\ }\ X_i\succ_{MV}X_j,\ X_j \mathbin{?}_{MV} X_k,\ X_k\sim_{MV}X_k,\ \dots$$
>
> **Figura** — Piano $(\mathbb{Var}(X),\mathbb{E}(X))$ con una retta orizzontale tratteggiata al livello $\bar r$: rappresenta l'insieme delle scelte di investimento aventi tutte la stessa media attesa $\bar r$ ma varianza diversa. Tra queste, il criterio media-varianza individua come scelta dominante quella indicata con $\mathbf{x}$, cioè quella a varianza minima: a parità di rendimento atteso, l'investitore razionale (avverso al rischio) preferisce la varianza più bassa.
>
> **Figura** — Piano $(\mathbb{Var}(X),\mathbb{E}(X))$ con due rette orizzontali tratteggiate ai livelli $\bar r_1 > \bar r_2$. Su ciascun livello di rendimento atteso sono rappresentate le scelte di investimento disponibili; per ciascun livello si individua la scelta a varianza minima: $\mathbf{x}_1$ sul livello $\bar r_1$ e $\mathbf{x}_2$ sul livello $\bar r_2$. Ripetendo questo procedimento per tutti i possibili livelli di rendimento atteso si costruisce, punto per punto, l'insieme delle scelte di investimento efficienti nel senso media-varianza — anticipando così la costruzione della frontiera efficiente di Markowitz.

*(slide 54–61)*
