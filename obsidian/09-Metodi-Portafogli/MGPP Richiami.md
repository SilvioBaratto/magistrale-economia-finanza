---
title: "Richiami di Ottimizzazione Vincolata — Metodo dei Moltiplicatori di Lagrange (condizioni sufficienti, più variabili e più vincoli)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Richiami.pdf"
pages: 10
text_layer: false
verified: true
generated: 2026-07-10
---

## Esercizi conclusivi sul §14.4 (metodo di Lagrange: condizioni necessarie)

Prima di introdurre le condizioni sufficienti, il testo propone alcuni esercizi di chiusura sul metodo di Lagrange visto come condizione necessaria (§14.4).

**Problema 2.** Il seguente brano, tratto da un libro di matematica per il management, contiene *gravi* errori. Individuarli: "Si consideri il problema generale di trovare i punti estremi di $z = f(x,y)$ soggetto al vincolo $g(x,y) = 0$. Chiaramente i punti estremi devono soddisfare la coppia di equazioni $f'_x(x,y) = 0$, $f'_y(x,y) = 0$ oltre al vincolo $g(x,y) = 0$. Quindi ci sono tre equazioni che devono essere soddisfatte dalla coppia di incognite $x, y$. Poiché ci sono più equazioni che incognite, il sistema si dice sovradeterminato e, in generale, è difficile da risolvere. Per facilitare il calcolo..." (segue una descrizione del metodo di Lagrange). L'errore concettuale è che il vincolo $g(x,y)=0$ è esso stesso un'equazione che coinvolge $x,y$: il sistema $f'_x=0, f'_y=0, g=0$ non è quindi sovradeterminato nel senso indicato, perché nel metodo di Lagrange si introduce un moltiplicatore $\lambda$ aggiuntivo, ottenendo tre equazioni ($\mathcal{L}'_x=0,\mathcal{L}'_y=0$, più il vincolo) in tre incognite ($x,y,\lambda$).

**Problemi più difficili.**

**Problema 3.** Si consideri il problema $\max f(x,y) = 2x+3y$ soggetto a $g(x,y)=\sqrt{x}+\sqrt{y}=5$.

(a) Mostrare che il metodo dei moltiplicatori di Lagrange suggerisce la soluzione errata $(x,y)=(9,4)$ (si noti che $f(9,4)=30$, eppure $f(25,0)=50$).

(b) Risolvere il problema studiando le curve di livello di $f(x,y)=2x+3y$ insieme al grafico dell'equazione di vincolo.

(c) Quale ipotesi del Teorema 14.4.1 viene violata?

**Problema 4.** Le funzioni $f$ e $g$ sono definite da
$$f(x,y) = (x+2)^2 + y^2 \qquad \text{e} \qquad g(x,y) = y^2 - x(x+1)^2$$
Trovare il valore minimo di $f(x,y)$ soggetto a $g(x,y)=0$. Mostrare che il metodo dei moltiplicatori di Lagrange non riesce a individuare questo minimo. (Suggerimento: disegnare il grafico di $g(x,y)=0$; notare in particolare che $g(-1,0)=0$.)

*(slide 2)*

## §14.5 — Introduzione alle condizioni sufficienti

Sotto le ipotesi del Teorema 14.4.1, il metodo dei moltiplicatori di Lagrange per il problema
$$\max(\min)\ f(x,y) \quad \text{soggetto a} \quad g(x,y) = c \tag{1}$$
fornisce condizioni **necessarie** per la soluzione. Per confermare che la soluzione sia stata effettivamente trovata è però necessario un controllo più accurato.

Gli esempi e i problemi della Sezione 14.3 hanno interpretazioni geometriche che suggeriscono fortemente di aver trovato la soluzione. In effetti, se l'insieme di vincolo è chiuso e limitato, il teorema di Weierstrass (Teorema 13.6.2) garantisce che una funzione continua raggiunga sia un massimo sia un minimo su tale insieme. Un caso concreto è l'Esempio 14.3.1, dove l'insieme di vincolo è chiuso e limitato (Fig. 14.3.1), per cui la funzione continua $f(x,y)=x^2+y^2$ raggiunge sia un valore massimo sia un valore minimo sull'insieme di vincolo. Poiché ci sono 4 punti che soddisfano le condizioni del primo ordine, resta solo da controllare quale di essi dia a $f$ il valore più alto e quale il più basso.

Infine, in alcuni casi si possono usare metodi ad hoc, come quello illustrato alla fine dell'Esempio 14.3.1.

*(slide 2)*

## Teorema 14.5.1 — Lagrangiana concava/convessa

> [!tip] Teorema
> **Lagrangiana concava/convessa.** Se $(x_0,y_0)$ risolve il problema (1), allora la Lagrangiana
> $$\mathcal{L}(x,y) = f(x,y) - \lambda\big(g(x,y)-c\big)$$
> è stazionaria in $(x_0,y_0)$, ma $\mathcal{L}$ non ha necessariamente un massimo (minimo) in $(x_0,y_0)$.
>
> Si supponga tuttavia che $\mathcal{L}(x,y)$ raggiunga un massimo **globale** in $(x_0,y_0)$, ossia che $(x_0,y_0)$ massimizzi $\mathcal{L}(x,y)$ tra **tutti** gli $(x,y)$. Allora
> $$\mathcal{L}(x_0,y_0) = f(x_0,y_0) - \lambda(g(x_0,y_0)-c) \ \ge\ \mathcal{L}(x,y) = f(x,y) - \lambda(g(x,y)-c) \tag{*}$$
> per ogni $(x,y)$. Se $(x_0,y_0)$ soddisfa anche il vincolo $g(x_0,y_0)=c$, allora da $(*)$ si conclude che $f(x_0,y_0) \ge f(x,y)$ per ogni $(x,y)$ tale che $g(x,y)=c$. Quindi $(x_0,y_0)$ risolve davvero il problema di massimo (1).
>
> Un risultato analogo si ottiene per il problema di minimo in (1), purché $\mathcal{L}(x,y)$ raggiunga un minimo globale in $(x_0,y_0)$.
>
> Ricordando (Teorema 13.2.1 e Nota 13.2.2) che un punto stazionario $(x_0,y_0)$ per una funzione concava (convessa) massimizza (minimizza) davvero la funzione, si ottiene il seguente risultato:
>
> **TEOREMA 14.5.1 (LAGRANGIANA CONCAVA/CONVESSA).** Si consideri il problema (1) e si supponga che $(x_0,y_0)$ sia un punto stazionario per la Lagrangiana $\mathcal{L}(x,y) = f(x,y) - \lambda(g(x,y)-c)$.
>
> (A) Se la Lagrangiana è concava, allora $(x_0,y_0)$ risolve il problema di massimo.
>
> (B) Se la Lagrangiana è convessa, allora $(x_0,y_0)$ risolve il problema di minimo.
>
> **Esempio 1.** Si consideri un'impresa che utilizza input positivi $K$ e $L$ di capitale e lavoro, rispettivamente, per produrre un unico output $Q$ secondo la funzione di produzione Cobb–Douglas $Q = F(K,L) = AK^aL^b$, dove $A, a, b$ sono parametri positivi che soddisfano $a+b \le 1$. Si supponga che i prezzi di capitale e lavoro siano $r>0$ e $w>0$, rispettivamente. Gli input $K$ e $L$ che minimizzano i costi devono risolvere il problema
> $$\min\ rK + wL \quad \text{soggetto a} \quad AK^aL^b = Q$$
> Si spieghi perché la Lagrangiana è convessa, cosicché un punto stazionario della Lagrangiana deve minimizzare i costi.
>
> *Soluzione.* La Lagrangiana è $\mathcal{L} = rK + wL - \lambda(AK^aL^b - Q)$, e le condizioni del primo ordine sono $r = \lambda A a K^{a-1}L^b$ e $w = \lambda A b K^a L^{b-1}$, il che implica $\lambda > 0$. Dal Problema 13.2.8 si vede che $-\mathcal{L}$ è concava, quindi $\mathcal{L}$ è convessa.

*(slide 3)*

## Condizioni del secondo ordine locali — Teorema 14.5.2

> [!tip] Teorema
> A volte interessano condizioni sufficienti affinché $(x_0,y_0)$ sia un punto estremo **locale** di $f(x,y)$ soggetto a $g(x,y)=c$.
>
> Si parte dall'espressione di $dz/dx$ data dalla (14.4.5). La condizione $dz/dx = 0$ è necessaria per l'ottimalità locale. Se inoltre $d^2z/dx^2 < 0$, allora un punto stazionario della Lagrangiana deve risolvere il problema di massimo locale. La derivata $d^2z/dx^2$ è semplicemente la derivata totale di $dz/dx$ rispetto a $x$.
>
> Assumendo che $f$ e $g$ siano funzioni $C^2$, e ricordando che $y$ è funzione di $x$, dalla (14.4.5) si ottiene:
> $$\frac{d^2z}{dx^2} = f''_{11} + f''_{12}y' - (f''_{21}+f''_{22}y')\frac{g'_1}{g'_2} - f'_2\frac{(g''_{11}+g''_{12}y')g'_2 - (g''_{21}+g''_{22}y')g'_1}{(g'_2)^2}$$
>
> Ma $f$ e $g$ sono funzioni $C^2$, quindi $f''_{12}=f''_{21}$ e $g''_{12}=g''_{21}$. Inoltre $y' = -g'_1/g'_2$. Anche $f'_1 = \lambda g'_1$ e $f'_2 = \lambda g'_2$, poiché queste sono le condizioni del primo ordine. Usando queste relazioni per eliminare $y'$ e $f'_2$, e con qualche passaggio algebrico elementare, si ottiene:
> $$\frac{d^2z}{dx^2} = \frac{1}{(g'_2)^2}\Big[(f''_{11}-\lambda g''_{11})(g'_2)^2 - 2(f''_{12}-\lambda g''_{12})g'_1g'_2 + (f''_{22}-\lambda g''_{22})(g'_1)^2\Big]$$
>
> Si vede che $d^2z/dx^2 < 0$ a condizione che l'espressione tra parentesi quadre sia $< 0$. Si ha quindi il seguente risultato:
>
> **TEOREMA 14.5.2 (CONDIZIONI DEL SECONDO ORDINE LOCALI).** Si consideri il problema
> $$\text{local } \max(\min)\ f(x,y) \quad \text{soggetto a} \quad g(x,y)=c$$
> e si supponga che $(x_0,y_0)$ soddisfi le condizioni del primo ordine $f'_1(x,y) = \lambda g'_1(x,y)$, $f'_2(x,y) = \lambda g'_2(x,y)$. Si definisca
> $$D(x,y,\lambda) = (f''_{11}-\lambda g''_{11})(g'_2)^2 - 2(f''_{12}-\lambda g''_{12})g'_1g'_2 + (f''_{22}-\lambda g''_{22})(g'_1)^2$$
>
> (A) Se $D(x_0,y_0,\lambda) < 0$, allora $(x_0,y_0)$ risolve il problema di massimo locale.
>
> (B) Se $D(x_0,y_0,\lambda) > 0$, allora $(x_0,y_0)$ risolve il problema di minimo locale.
>
> Le condizioni sul segno di $D(x_0,y_0,\lambda)$ si chiamano condizioni del secondo ordine (locali).

*(slide 3–4)*

## Esempio 2 — applicazione del Teorema 14.5.2

> [!example] Esempio
> Si consideri il problema
> $$\text{local }\max(\min)\ f(x,y) = x^2+y^2 \quad \text{soggetto a}\quad g(x,y) = x^2+xy+y^2 = 3$$
>
> Nell'Esempio 14.3.1 le condizioni del primo ordine danno i punti $(1,1)$ e $(-1,-1)$ con $\lambda = 2/3$, oltre a $(\sqrt{3},-\sqrt{3})$ e $(-\sqrt{3},\sqrt{3})$ con $\lambda = 2$. Si usi il Teorema 14.5.2 per verificare le condizioni del secondo ordine locali in questo caso.
>
> *Soluzione.* Si trova che $f''_{11}=2$, $f''_{12}=0$, $f''_{22}=2$, $g''_{11}=2$, $g''_{12}=1$, e $g''_{22}=2$. Quindi
> $$D(x,y,\lambda) = (2-2\lambda)(x+2y)^2 + 2\lambda(2x+y)(x+2y) + (2-2\lambda)(2x+y)^2$$
>
> Dunque $D(1,1,\tfrac{2}{3}) = D(-1,-1,\tfrac{2}{3}) = 24$ e $D(\sqrt{3},-\sqrt{3},2) = D(-\sqrt{3},\sqrt{3},2) = -24$.
>
> Dai segni di $D$ si conclude che $(1,1)$ e $(-1,-1)$ sono punti di minimo locale, mentre $(\sqrt{3},-\sqrt{3})$ e $(-\sqrt{3},\sqrt{3})$ sono punti di massimo locale. (Nell'Esempio 14.3.1 si era in realtà dimostrato che questi punti erano punti estremi globali.)

*(slide 4)*

## Hessiano orlato: forma matriciale di D

> [!abstract] Definizione
> Per chi ha familiarità con i determinanti $3\times 3$ (Sezione 16.2), l'espressione piuttosto lunga di $D(x,y,\lambda)$ può essere scritta in una forma simmetrica più facile da ricordare. Infatti,
> $$D(x,y,\lambda) = -\begin{vmatrix} 0 & g'_1(x,y) & g'_2(x,y) \\ g'_1(x,y) & \mathcal{L}''_{11}(x,y) & \mathcal{L}''_{12}(x,y) \\ g'_2(x,y) & \mathcal{L}''_{21}(x,y) & \mathcal{L}''_{22}(x,y) \end{vmatrix} \tag{2}$$
>
> Si noti che la matrice $2\times 2$ in basso a destra della (2) è l'Hessiano della Lagrangiana (Sezione 11.6). Perciò il determinante è chiamato in modo naturale **Hessiano orlato**; i suoi bordi nella prima riga e nella prima colonna, a parte l'elemento $0$ nella posizione in alto a sinistra, sono le derivate parziali del primo ordine di $g$.

*(slide 5)*

## Problemi per la sezione 14.5

**Problema 1.** Usare il Teorema 14.5.1 per verificare che la soluzione ottima trovata nel Problema 14.1.3(a) sia effettivamente tale.

**Problema 2.** Si consideri il problema di massimizzazione dell'utilità $\max \ln x + \ln y$ soggetto a $px+qy=m$. Calcolare $D(x,y,\lambda)$ del Teorema 14.5.2 in questo caso, e verificare che la condizione del secondo ordine del teorema sia soddisfatta. (Si noti che la Lagrangiana è in realtà concava, come si verifica facilmente, quindi l'unica soluzione $(x,y)=(m/p, m/2q)$ delle condizioni del primo ordine è in realtà un massimo vincolato globale per questo problema.)

**Problema 3.** Calcolare $D(x,y,\lambda)$ del Teorema 14.5.2 per il Problema 14.2.3(a). Conclusione?

**Problema 4.** Dimostrare che $U(x,y) = x^a + y^a$, con $a \in (0,1)$, è concava per $x>0, y>0$. Risolvere il problema di domanda del consumatore
$$\max\ x^a+y^a \quad \text{soggetto a}\quad px+qy=m$$

*(slide 5)*

## §14.6 — Metodo di Lagrange con più variabili

> [!abstract] Definizione
> I problemi di ottimizzazione vincolata in economia coinvolgono di solito più di due sole variabili. Il tipico problema con $n$ variabili può essere scritto nella forma
> $$\max(\min)\ f(x_1,\dots,x_n) \quad \text{soggetto a}\quad g(x_1,\dots,x_n)=c \tag{1}$$
>
> Il metodo dei moltiplicatori di Lagrange presentato nelle sezioni precedenti si generalizza facilmente. Come prima, si associa un moltiplicatore di Lagrange $\lambda$ al vincolo e si forma la Lagrangiana
> $$\mathcal{L}(x_1,\dots,x_n) = f(x_1,\dots,x_n) - \lambda\big(g(x_1,\dots,x_n)-c\big) \tag{2}$$
>
> Si trovano quindi tutte le derivate parziali del primo ordine di $\mathcal{L}$ e si eguagliano a zero, cosicché
> $$\mathcal{L}'_1 = f'_1(x_1,\dots,x_n) - \lambda g'_1(x_1,\dots,x_n) = 0$$
> $$\vdots$$
> $$\mathcal{L}'_n = f'_n(x_1,\dots,x_n) - \lambda g'_n(x_1,\dots,x_n) = 0 \tag{3}$$
>
> Queste $n$ equazioni, insieme al vincolo, formano $n+1$ equazioni che vanno risolte simultaneamente per determinare le $n+1$ incognite $x_1,\dots,x_n$ e $\lambda$.
>
> **Nota 1.** Questo metodo fallisce (in generale) nel dare condizioni necessarie corrette se tutte le derivate parziali del primo ordine di $g(x_1,\dots,x_n)$ si annullano nel punto stazionario della Lagrangiana. Altrimenti, la dimostrazione è una facile generalizzazione dell'argomento analitico della Sezione 14.4 per le condizioni del primo ordine. Se, ad esempio, $\partial g/\partial x_n \neq 0$, si "risolve" $g(x_1,\dots,x_n)=c$ per $x_n$ vicino al punto stazionario, riducendo così il problema a un problema di estremo non vincolato nelle rimanenti $n-1$ variabili $x_1,\dots,x_{n-1}$.

*(slide 5–6)*

## Esempio 1 (§14.6) — problema di domanda del consumatore con tre beni

> [!example] Esempio
> Risolvere il problema di domanda del consumatore
> $$\max\ U(x,y,z) = x^2y^3z \quad \text{soggetto a}\quad x+y+z=12$$
>
> *Soluzione.* Con $\mathcal{L}(x,y,z) = x^2y^3z - \lambda(x+y+z-12)$, le condizioni del primo ordine sono
> $$\mathcal{L}'_1 = 2xy^3z - \lambda = 0,\qquad \mathcal{L}'_2 = 3x^2y^2z - \lambda = 0,\qquad \mathcal{L}'_3 = x^2y^3 - \lambda = 0 \tag{*}$$
>
> Se una qualsiasi delle variabili $x,y,z$ è $0$, allora $x^2y^3z=0$, che *non* è il valore massimo. Si supponga quindi che $x,y,z$ siano tutti positivi. Dalle prime due equazioni in $(*)$ si ha $2xy^3z = 3x^2y^2z$, quindi $y = 3x/2$. La prima e la terza equazione in $(*)$ implicano allo stesso modo che $z = x/2$. Inserendo $y=3x/2$ e $z=x/2$ nel vincolo si ottiene $x + 3x/2 + x/2 = 12$, quindi $x=4$. Allora $y=6$ e $z=2$. Pertanto l'unica soluzione possibile è $(x,y,z) = (4,6,2)$.

*(slide 6)*

## Esempio 2 (§14.6) — distanza minima da un paraboloide

> [!example] Esempio
> Risolvere il problema
> $$\text{minimizzare}\quad f(x,y,z) = (x-4)^2+(y-4)^2+\Big(z-\tfrac12\Big)^2 \quad \text{soggetto a}\quad x^2+y^2=z$$
> È possibile fornire un'interpretazione geometrica del problema?
>
> *Soluzione.* La Lagrangiana è $\mathcal{L}(x,y,z) = (x-4)^2+(y-4)^2+(z-\tfrac12)^2 - \lambda(x^2+y^2-z)$, e le condizioni del primo ordine sono:
> $$\mathcal{L}'_1(x,y,z) = 2(x-4) - 2\lambda x = 0 \tag{i}$$
> $$\mathcal{L}'_2(x,y,z) = 2(y-4) - 2\lambda y = 0 \tag{ii}$$
> $$\mathcal{L}'_3(x,y,z) = 2\Big(z-\tfrac12\Big) + \lambda = 0 \tag{iii}$$
> $$x^2+y^2 = z \tag{iv}$$
>
> Dalla (i) si vede che $x=0$ è impossibile. La (i) dà quindi $\lambda = 1 - 4/x$. Inserendo questa espressione in (ii) e (iii) si ottiene $y=x$ e $z=2/x$. Usando questi risultati, la (iv) si riduce a $2x^2 = 2/x$, cioè $x^3=1$, quindi $x=1$. Ne segue che $(x,y,z)=(1,1,2)$ è l'unica soluzione candidata al problema.
>
> L'espressione $(x-4)^2+(y-4)^2+(z-1/2)^2$ misura il quadrato della distanza dal punto $(4,4,1/2)$ al punto $(x,y,z)$. L'insieme dei punti $(x,y,z)$ che soddisfano $z=x^2+y^2$ è una superficie nota come **paraboloide**, una parte della quale è mostrata nella Figura 1. Il problema di minimizzazione consiste quindi nel trovare il punto sul paraboloide che ha la minima distanza (al quadrato) da $(4,4,1/2)$. È "geometricamente ovvio" che questo problema abbia soluzione. D'altra parte, il problema di trovare la massima distanza da $(4,4,1/2)$ a un punto del paraboloide non ha soluzione, perché la distanza può essere resa grande a piacere.
>
> **Figura 1** — Il paraboloide $z=x^2+y^2$ in $\mathbb{R}^3$, con gli assi $x,y,z$ e i valori $4$ segnati sugli assi $x$ e $y$. Il grafico mostra la superficie a forma di "coppa" del paraboloide su cui giace il punto candidato soluzione $(1,1,2)$, il più vicino al punto esterno $(4,4,1/2)$.

*(slide 6–7)*

## Esempio 3 (§14.6) — problema generale del consumatore e funzioni di domanda

> [!example] Esempio
> Il problema generale di ottimizzazione del consumatore con $n$ beni è
> $$\max_{x_1,\dots,x_n}\ U(x_1,\dots,x_n) \quad \text{soggetto a}\quad p_1x_1+\dots+p_nx_n=m \tag{4}$$
> dove $U$ è definita per $x_1\ge 0,\dots,x_n\ge 0$. La Lagrangiana è
> $$\mathcal{L}(x_1,\dots,x_n) = U(x_1,\dots,x_n) - \lambda(p_1x_1+\dots+p_nx_n-m)$$
>
> Le condizioni del primo ordine sono
> $$\mathcal{L}'_i(x_1,\dots,x_n) = U'_i(x_1,\dots,x_n) - \lambda p_i = 0,\qquad i=1,\dots,n$$
>
> Scrivendo $\mathbf{x} = (x_1,\dots,x_n)$, si ha
> $$\frac{U'_1(\mathbf{x})}{p_1} = \frac{U'_2(\mathbf{x})}{p_2} = \dots = \frac{U'_n(\mathbf{x})}{p_n} = \lambda \tag{5}$$
>
> A parte l'ultima uguaglianza, che serve solo a determinare il moltiplicatore di Lagrange $\lambda$, si hanno $n-1$ equazioni. (Per $n=2$ c'è un'equazione; per $n=3$ ce ne sono due; e così via.) In più deve valere il vincolo. Si hanno quindi $n$ equazioni per determinare i valori $x_1,\dots,x_n$. Dalla (5) segue anche che
> $$\frac{U'_j(\mathbf{x})}{U'_k(\mathbf{x})} = \frac{p_j}{p_k} \qquad \text{per ogni coppia di beni } j \text{ e } k \tag{6}$$
>
> Il membro sinistro è il saggio marginale di sostituzione (MRS) del bene $k$ rispetto al bene $j$, mentre il membro destro è il loro rapporto di prezzo, ossia il tasso di scambio del bene $k$ per il bene $j$. La condizione (6) eguaglia dunque il MRS di ogni coppia di beni al corrispondente rapporto di prezzo.
>
> Si considerino le equazioni in (5), insieme al vincolo di bilancio. Supponendo che questo sistema venga risolto per $x_1,\dots,x_n$ e $\lambda$ in funzione di $p_1,\dots,p_n$ e $m$, si ottiene $x_i = D_i(p_1,\dots,p_n,m)$, per $i=1,\dots,n$. Allora $D_i(p_1,\dots,p_n,m)$ dà la quantità del bene $i$-esimo domandata dall'individuo quando i prezzi sono $p_1,\dots,p_n$ e il reddito è $m$. Per questo motivo $D_1,\dots,D_n$ si chiamano **funzioni di domanda (individuali)**. Con lo stesso argomento dell'Esempio 14.1.3, le funzioni di domanda sono omogenee di grado $0$. Come verifica che le funzioni di domanda trovate siano corrette, è buona norma controllare che siano effettivamente omogenee di grado $0$ e che soddisfino il vincolo di bilancio.
>
> **Caso Cobb–Douglas.** Quando il consumatore ha una funzione di utilità Cobb–Douglas, il problema di massimizzazione vincolata è
> $$\max\ A x_1^{a_1}\cdots x_n^{a_n} \quad \text{soggetto a}\quad p_1x_1+\dots+p_nx_n=m \tag{*}$$
> dove si assume che ogni parametro di "gusto" $a_i>0$. Allora le funzioni di domanda sono
> $$D_i(p_1,\dots,p_n,m) = \frac{a_i}{a_1+\dots+a_n}\cdot \frac{m}{p_i}, \qquad i=1,\dots,n \tag{**}$$
>
> Si osserva come il modello a due variabili dell'Esempio 14.1.3 si ripeta: una frazione costante del reddito $m$ è spesa su ciascun bene, indipendentemente da tutti i prezzi. Si noti inoltre che la domanda per ogni bene $i$ non è affatto influenzata dai cambiamenti nel prezzo di qualunque altro bene. Questo è un argomento contro l'uso delle funzioni di utilità Cobb–Douglas, poiché ci si aspetta che funzioni di domanda realistiche dipendano dai prezzi degli altri beni, che siano complementi o sostituti.

*(slide 7–8)*

## Vincoli multipli: generalizzazione del metodo di Lagrange

> [!abstract] Definizione
> Talvolta gli economisti devono considerare problemi di ottimizzazione con più di un vincolo di uguaglianza (sebbene sia molto più comune avere molti vincoli di disuguaglianza). Il corrispondente problema generale di Lagrange è
> $$\max(\min)\ f(x_1,\dots,x_n) \quad \text{soggetto a}\quad \begin{cases} g_1(x_1,\dots,x_n)=c_1 \\ \ \ \vdots \\ g_m(x_1,\dots,x_n)=c_m \end{cases} \tag{7}$$
>
> Il metodo dei moltiplicatori di Lagrange si estende per trattare il problema (7). Per farlo, si associa un moltiplicatore di Lagrange a ciascun vincolo, e si forma la Lagrangiana somma
> $$\mathcal{L}(x_1,\dots,x_n) = f(x_1,\dots,x_n) - \sum_{j=1}^m \lambda_j\big(g_j(x_1,\dots,x_n)-c_j\big) \tag{8}$$
>
> Salvo casi speciali, questa Lagrangiana deve essere stazionaria in ogni punto ottimo, cioè la sua derivata parziale rispetto a ciascuna variabile $x_i$ deve annullarsi. Quindi,
> $$\frac{\partial \mathcal{L}}{\partial x_i} = \frac{\partial f(x_1,\dots,x_n)}{\partial x_i} - \sum_{j=1}^m \lambda_j \frac{\partial g_j(x_1,\dots,x_n)}{\partial x_i} = 0, \qquad i=1,2,\dots,n \tag{9}$$
>
> Insieme agli $m$ vincoli di uguaglianza, queste $n$ equazioni formano un totale di $n+m$ equazioni nelle $n+m$ incognite $x_1,\dots,x_n,\lambda_1,\dots,\lambda_m$.

*(slide 8)*

## Esempio 4 (§14.6) — minimizzazione con due vincoli lineari

> [!example] Esempio
> Risolvere il problema
> $$\min\ x^2+y^2+z^2 \quad \text{soggetto a}\quad \begin{cases} x+2y+z=30 \quad \text{(i)} \\ 2x-y-3z=10 \quad \text{(ii)} \end{cases}$$
>
> *Soluzione.* La Lagrangiana è
> $$\mathcal{L}(x,y,z) = x^2+y^2+z^2 - \lambda_1(x+2y+z-30) - \lambda_2(2x-y-3z-10)$$
>
> Le condizioni del primo ordine (9) richiedono che
> $$\frac{\partial \mathcal{L}}{\partial x} = 2x-\lambda_1-2\lambda_2 = 0 \tag{iii}$$
> $$\frac{\partial \mathcal{L}}{\partial y} = 2y-2\lambda_1+\lambda_2 = 0 \tag{iv}$$
> $$\frac{\partial \mathcal{L}}{\partial z} = 2z-\lambda_1+3\lambda_2 = 0 \tag{v}$$
>
> Vi sono quindi cinque equazioni, da (i) a (v), per determinare le cinque incognite $x,y,z,\lambda_1,\lambda_2$.
>
> Risolvendo (iii) e (iv) simultaneamente per $\lambda_1$ e $\lambda_2$ si ottiene
> $$\lambda_1 = \tfrac{2}{5}x + \tfrac{4}{5}y, \qquad \lambda_2 = \tfrac{4}{5}x - \tfrac{2}{5}y$$
>
> Inserendo queste espressioni di $\lambda_1$ e $\lambda_2$ nella (v) e riordinando si ottiene
> $$x - y + z = 0 \tag{vi}$$
>
> Questa equazione, insieme a (i) e (ii), costituisce un sistema di tre equazioni lineari nelle incognite $x,y,z$. Risolvendo questo sistema per eliminazione si ottiene $(x,y,z) = (10,10,0)$. I valori corrispondenti dei moltiplicatori sono $\lambda_1=12$ e $\lambda_2=4$.
>
> **Argomento geometrico.** Ognuno dei due vincoli rappresenta un piano in $\mathbb{R}^3$, e i punti che soddisfano entrambi i vincoli giacciono quindi sulla retta in cui i due piani si intersecano. Ora $x^2+y^2+z^2$ misura (il quadrato del)la distanza dall'origine a un punto su questa retta, distanza che si vuole rendere minima scegliendo il punto sulla retta più vicino all'origine. Non può esistere una distanza massima, ma è geometricamente ovvio che esiste una distanza minima, e che essa viene raggiunta in questo punto più vicino.
>
> **Metodo alternativo più semplice.** Un metodo alternativo più semplice per risolvere questo particolare problema consiste nel ridurlo a un problema di ottimizzazione in una sola variabile, usando (i) e (ii) per ottenere $y=20-x$ e $z=x-10$, le equazioni della retta di intersezione dei due piani. Allora il quadrato della distanza dall'origine è
> $$x^2+y^2+z^2 = x^2+(20-x)^2+(x-10)^2 = 3(x-10)^2+200$$
> e si vede facilmente che questa funzione ha un minimo per $x=10$.

*(slide 8–9)*

## Problemi per la sezione 14.6

**Problema 1.** Si consideri il problema $\min x^2+y^2+z^2$ soggetto a $x+y+z=1$.

(a) Scrivere la Lagrangiana per questo problema e trovare l'unico punto $(x,y,z)$ che soddisfa le condizioni necessarie.

(b) Fornire un argomento geometrico per l'esistenza di una soluzione. Il corrispondente problema di massimizzazione ha soluzione?

**Problema 2.** Usare il risultato $(**)$ dell'Esempio 3 per risolvere il problema di massimizzazione dell'utilità
$$\max\ 10\,x^{1/2}y^{1/3}z^{1/4} \quad \text{soggetto a}\quad 4x+3y+6z=390$$

**Problema 3.** Le domande $x,y,z$ di un consumatore per tre beni sono scelte per massimizzare la funzione di utilità
$$U(x,y,z) = x + \sqrt{y} - \frac{1}{z} \qquad (x\ge 0,\ y>0,\ z>0)$$
soggetta al vincolo di bilancio $px+qy+rz=m$, dove $p,q,r>0$ e $m \ge \sqrt{pr}+p^2/4q$.

(a) Scrivere le condizioni del primo ordine per un massimo vincolato.

(b) Trovare le domande che massimizzano l'utilità per tutti e tre i beni in funzione delle quattro variabili $(p,q,r,m)$.

(c) Mostrare che l'utilità massimizzata è data dalla funzione di utilità indiretta
$$U^*(p,q,r,m) = \frac{m}{p} + \frac{p}{4q} - 2\sqrt{\frac{r}{p}}$$

(d) Trovare $\partial U^*/\partial m$ e commentare il risultato.

**Problema 4.** Ogni settimana un individuo consuma quantità $x$ e $y$ di due beni, e lavora per $l$ ore. Queste tre quantità sono scelte per massimizzare la funzione di utilità
$$U(x,y,l) = \alpha\ln x + \beta \ln y + (1-\alpha-\beta)\ln(L-l)$$
definita per $0 \le l < L$ e per $x,y>0$. Qui $\alpha$ e $\beta$ sono parametri positivi che soddisfano $\alpha+\beta<1$. L'individuo affronta il vincolo di bilancio $px+qy=wl$, dove $w$ è il salario orario. Definendo $\gamma = (\alpha+\beta)/(1-\alpha-\beta)$, trovare le domande $x^*, y^*$ dell'individuo e l'offerta di lavoro $l^*$ in funzione di $p,q,w$.

**Problema 5.** Si consideri il problema dell'Esempio 4, e si ponga $(x,y,z)=(10+h,10+k,l)$. Mostrare che se $(x,y,z)$ soddisfa entrambi i vincoli, allora $k=-h$ e $l=h$. Mostrare quindi che $x^2+y^2+z^2 = 200+3h^2$. Conclusione?

**Problema 6.** Un problema statistico richiede di risolvere
$$\min\ a_1^2x_1^2+a_2^2x_2^2+\dots+a_n^2x_n^2 \quad \text{soggetto a}\quad x_1+x_2+\dots+x_n=1$$
dove tutte le costanti $a_i$ sono non nulle. Risolvere il problema, dando per scontato che il valore minimo esista. Qual è la soluzione se uno degli $a_i$ è zero?

**Problema 7.** Risolvere il problema:
$$\max(\min)\ x+y \quad \text{soggetto a}\quad \begin{cases} x^2+2y^2+z^2=1 \\ x+y+z=1 \end{cases}$$

**Problema più difficile 8.** Si consideri il problema di ottimizzazione del consumatore dell'Esempio 3. Trovare le funzioni di domanda quando:

(a) $U(x_1,\dots,x_n) = Ax_1^{a_1}\cdots x_n^{a_n}$   $(A>0,\ a_1>0,\dots,a_n>0)$

(b) $U(x_1,\dots,x_n) = x_1^a+\dots+x_n^a$   $(0<a<1)$

*(slide 9–10)*
