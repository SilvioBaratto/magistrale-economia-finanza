---
title: "Introduzione alla Teoria dell'Utilità Attesa"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Introduzione-alla-teoria-dell-utilita-attesa-lucidi.pdf"
pages: 15
text_layer: true
verified: true
generated: 2026-07-10
---

## Utilità degli importi certi e utilità attesa: motivazione

L'"importanza" di un importo/rendimento certo (che nel seguito verrà indicato, talvolta impropriamente, con il termine *ricchezza*) non dipende direttamente dal suo valore nominale, ma piuttosto dall'utilità che tale valore nominale ha per il suo fruitore.

Questa è l'idea di fondo della teoria dell'utilità attesa: due individui che ricevono lo stesso importo monetario possono trarne un "beneficio" psicologico/economico diverso, e le scelte in condizioni di incertezza vanno quindi valutate non sui valori monetari nominali ma sulla loro utilità.

*(slide 1)*

## Funzione di utilità della moneta (importi certi)

> [!abstract] Definizione
> Una **funzione di utilità della moneta**
> $$u(x): M \to \mathbb{R},$$
> dove $x$ indica l'importo certo ed $M$ indica l'insieme degli importi certi, è una funzione tale che per ogni coppia $x_1, x_2 \in M$ si ha che
> $$u(x_1) > u(x_2) \iff x_1 > x_2$$
> e
> $$u(x_1) = u(x_2) \iff x_1 = x_2.$$
>
> Ovvero, $u(\cdot)$ deve preservare (essere strettamente crescente rispetto a) l'ordinamento naturale degli importi certi.
>
> Tuttavia, frequentemente gli importi non sono certi: occorre quindi uno strumento per confrontare importi/rendimenti aleatori, ossia l'utilità attesa (o utilità media).

*(slide 2)*

## Utilità attesa (o utilità media) di un importo/rendimento aleatorio

> [!abstract] Definizione
> Data una variabile casuale (v.c.) $X$ che rappresenta un importo/rendimento aleatorio, e data una funzione di utilità della moneta $u(\cdot)$, l'**utilità attesa** (o **utilità media**) di $X$ si definisce come segue.
>
> **V.c. discreta finita** (con $N$ possibili esiti $x_i$ aventi probabilità $p_i$):
> $$E(u(X)) = \sum_{i=1}^{N} u(x_i)\, p_i.$$
>
> **V.c. continua** (con funzione di densità di probabilità $f_X(\cdot)$):
> $$\int_{-\infty}^{+\infty} u(t)\, f_X(t)\, dt,$$
> dove $f_X(\cdot)$ indica la funzione di densità di probabilità di $X$.

*(slide 3)*

## Proprietà della funzione di utilità della ricchezza

> [!abstract] Definizione
> Una funzione di utilità della moneta $u(x)$ è una funzione tale che (almeno):
>
> - **$u(x)$ è crescente**, ovvero dati $x_1 < x_2$ si ha
>  $$u(x_1) < u(x_2)$$
>  (questo perché l'agente economico è un massimizzatore dell'importo/rendimento);
>
> - **$u(x)$ è crescente in maniera meno che proporzionale**, ovvero dati $x_1 < x_2$ e data una variazione di importo monetario $\Delta x$, si ha
>  $$u(x_1 + \Delta x) - u(x_1) > u(x_2 + \Delta x) - u(x_2)$$
>  (questo perché l'agente economico è avverso al rischio).
>
> Questa seconda proprietà equivale a richiedere la concavità della funzione di utilità: un incremento di ricchezza $\Delta x$ genera un incremento di utilità tanto più piccolo quanto più elevato è il livello di ricchezza di partenza.
>
> **Figura — Funzione di utilità della ricchezza.** Il grafico riporta in ascissa l'importo/rendimento certo (da 1 a 1501) e in ordinata la corrispondente utilità (da 0 a 8). La curva è crescente ma con pendenza decrescente (concava): sale rapidamente per importi piccoli e si appiattisce progressivamente per importi elevati, illustrando graficamente le due proprietà sopra esposte (funzione crescente e crescente meno che proporzionalmente, cioè avversione al rischio).

*(slide 4–5)*

## Esiste la funzione di utilità della ricchezza?

La questione chiave è: esiste una funzione di utilità della ricchezza tale da indurre in $M$ un ordinamento secondo la relazione di preferenza debole del fruitore?

La risposta a tale questione è, assunte opportune ipotesi, **affermativa**. Le sezioni seguenti introducono gli strumenti necessari (mistura di variabili casuali, ipotesi sulla relazione di preferenza) per arrivare al teorema che fonda il criterio di scelta basato sul principio dell'utilità attesa.

*(slide 6)*

## Mistura di variabili casuali secondo un evento aleatorio

> [!abstract] Definizione
> **Definizione.** Dato un evento aleatorio $A$ la cui probabilità di verificarsi è $\alpha$, e date due v.v.c.c. (discrete)
> $$X_1 = \{(x_{11}, p_{11}), \ldots, (x_{1N}, p_{1N})\}$$
> che si può verificare se si verifica $A$, e
> $$X_2 = \{(x_{21}, p_{21}), \ldots, (x_{2M}, p_{2M})\}$$
> che si può verificare se non si verifica $A$, si definisce **mistura di $X_1$ e $X_2$ secondo $A$** (che si indica con $X_1 \alpha X_2$) una nuova v.c. tale che
> $$X_1 \alpha X_2 = \{(x_{11}, p_{11}\alpha), \ldots, (x_{1N}, p_{1N}\alpha), (x_{21}, p_{21}(1-\alpha)), \ldots, (x_{1M}, p_{1M}(1-\alpha))\}.$$
>
> In relazione a questa definizione si osservi:
>
> - che $0 \le p_{1i}\alpha \le 1$ con $i = 1, \ldots, N$ e $0 \le p_{2j}(1-\alpha) \le 1$ con $j = 1, \ldots, M$;
> - che le probabilità della mistura sommano correttamente a 1:
> $$p_{1i}\alpha + \ldots + p_{1N}\alpha + p_{2j}(1-\alpha) + \ldots + p_{2M}(1-\alpha) =$$
> $$= (p_{1i} + \ldots + p_{1N})\alpha + (p_{2j} + \ldots + p_{2M})(1-\alpha) = 1 \cdot \alpha + 1 \cdot (1-\alpha) = 1.$$
>
> ### Esempio
>
> Esemplifichiamo la definizione di mistura di v.v.c.c. secondo un evento aleatorio:
>
> - $\alpha = \dfrac{1}{10}$;
> - $X_1 = \left\{\left(-10, \dfrac{3}{4}\right), \left(30, \dfrac{1}{4}\right)\right\}$ e $X_2 = \left\{\left(-5, \dfrac{1}{2}\right), \left(0, \dfrac{1}{4}\right), \left(2, \dfrac{1}{4}\right)\right\}$,
>
> da cui
> $$X_1 \tfrac{1}{10} X_2 = \left\{\left(-10, \tfrac{3}{4}\cdot\tfrac{1}{10}\right), \left(30, \tfrac{1}{4}\cdot\tfrac{1}{10}\right), \left(-5, \tfrac{1}{2}\cdot\tfrac{9}{10}\right), \left(0, \tfrac{1}{4}\cdot\tfrac{9}{10}\right), \left(2, \tfrac{1}{4}\cdot\tfrac{9}{10}\right)\right\} =$$
> $$= \left\{\left(-10, \tfrac{3}{40}\right), \left(-5, \tfrac{9}{20}\right), \left(0, \tfrac{9}{40}\right), \left(2, \tfrac{9}{40}\right), \left(30, \tfrac{1}{40}\right)\right\}.$$

*(slide 7–8)*

## Ipotesi sulla relazione di preferenza

> [!abstract] Definizione
> Una relazione $R$, definita sull'insieme $X$, può godere di varie proprietà, fra le quali:
>
> - **proprietà di riflessività**: per ogni $X_i \in X$ si ha $X_i \succeq X_i$;
> - **proprietà di transitività**: per ogni tripla $X_h, X_i, X_j \in X$, se $X_h \succeq X_i$ e $X_i \succeq X_j$, allora $X_h \succeq X_j$;
> - **proprietà di completezza**: per ogni coppia $X_i, X_j \in X$, si ha $X_j \succeq X_i$ oppure $X_i \succeq X_j$;
>
> (N.B. — Se $R$ gode di tutte queste prime tre proprietà è una relazione di preferenza debole totale, che si indica con $\succeq$.)
>
> A queste si aggiungono due ulteriori proprietà:
>
> - **proprietà di archimedeità**: per ogni tripla $X_h, X_i, X_j \in X$ tale che $X_h \succeq X_i \succeq X_j$, esistono delle probabilità $\alpha$ e $\beta$ per le quali si ha
> $$X_h \alpha X_j \succeq X_i \succeq X_j \beta X_h;$$
> - **proprietà di sostituzione**: per ogni coppia $X_i, X_j \in X$ tale che $X_i \succeq X_j$, allora
> $$X_i \alpha X_h \succeq X_j \alpha X_h$$
> per ogni $X_h \in X$ e per ogni probabilità $\alpha$.
>
> Queste cinque proprietà (riflessività, transitività, completezza, archimedeità, sostituzione) sono le ipotesi che, se soddisfatte dalla relazione di preferenza del fruitore, garantiscono l'esistenza di una funzione di utilità coerente con il principio dell'utilità attesa (si veda il teorema seguente).

*(slide 9–10)*

## Teorema del criterio di scelta basato sul principio dell'utilità attesa

> [!tip] Teorema
> **Teorema.** Data una relazione $R$, definita sull'insieme $M$, che gode delle proprietà di riflessività, di transitività, di completezza, di archimedeità e di sostituzione, e date due v.v.c.c. discrete $X_1$ e $X_2$, allora:
>
> - esiste una funzione $u(x): M \to \mathbb{R}$ tale che $X_1$ domina $X_2$ secondo il principio dell'utilità attesa (che si indica con $X_1 \overset{UA}{\succeq} X_2$) se e solo se
> $$E(u(X_1)) \ge E(u(X_2));$$
> - la funzione $u(x): M \to \mathbb{R}$ è unica a meno di una trasformazione del tipo
> $$a + b \cdot u(x), \quad \text{con } a \in \mathbb{R} \text{ e } b > 0.$$
>
> In altre parole: se la relazione di preferenza del fruitore soddisfa le cinque ipotesi (riflessività, transitività, completezza, archimedeità, sostituzione), allora esiste sempre una funzione di utilità $u(x)$ che rappresenta tale preferenza tramite il confronto delle utilità attese, ed essa è determinata univocamente a meno di trasformazioni affini crescenti (cambio di origine $a$ e di scala positiva $b$).

*(slide 11)*

## Esempio numerico di calcolo dell'utilità attesa (utilità logaritmica)

> [!example] Esempio
> Data la funzione di utilità
> $$u(x) = \ln(x), \quad \text{con } x > 0,$$
> l'utilità attesa della posizione patrimoniale
> $$X = \left\{\left(1, \tfrac{1}{4}\right), \left(3, \tfrac{1}{4}\right), \left(7, \tfrac{1}{2}\right)\right\}$$
> è
> $$E(u(X)) = \ln(1)\cdot\tfrac{1}{4} + \ln(3)\cdot\tfrac{1}{4} + \ln(7)\cdot\tfrac{1}{2} = 1{,}247608\ldots$$

*(slide 12)*

## Alcune funzioni di utilità della moneta

> [!example] Esempio
> Vengono presentate tre famiglie classiche di funzioni di utilità della moneta, ciascuna verificata rispetto alle due proprietà richieste: **non sazietà** ($u'(x) > 0$, funzione crescente) e **avversione al rischio** ($u''(x) < 0$, funzione concava).
>
> ### Funzione di utilità logaritmica
>
> $$u(x) = \ln(x), \quad \text{con } x > 0;$$
>
> - $u'(x) = \dfrac{1}{x} > 0$ per costruzione perché $x > 0$ (non sazietà);
> - $u''(x) = -\dfrac{1}{x^2} < 0$ per costruzione perché $x > 0$ (avversione al rischio).
>
> ### Funzione di utilità quadratica
>
> $$u(x) = x - \dfrac{a}{2}x^2, \quad \text{con } a > 0;$$
>
> - $u'(x) = 1 - ax > 0$ se $a < \dfrac{1}{x}$ (o equivalentemente $x < \dfrac{1}{a}$) (non sazietà);
> - $u''(x) = -a < 0$ per costruzione perché $a > 0$ (avversione al rischio).
>
> Si noti che la condizione di non sazietà della funzione quadratica vale solo per $x < 1/a$: a differenza della logaritmica, la quadratica non è monotona crescente su tutto il dominio positivo, ma solo su un intervallo limitato dal parametro $a$.
>
> ### Funzione di utilità esponenziale
>
> $$u(x) = 1 - e^{-ax} = 1 - \exp(-ax), \quad \text{con } a > 0;$$
>
> - $u'(x) = a e^{-ax} = a\exp(-ax) > 0$ per costruzione perché $a > 0$ e perché $e^{(\cdot)} = \exp(\cdot) > 0$ (non sazietà);
> - $u''(x) = -a^2 e^{-ax} = -a^2\exp(-ax) < 0$ per costruzione perché $a > 0$ e perché $e^{(\cdot)} = \exp(\cdot) > 0$ (avversione al rischio).
>
> A differenza della quadratica, la funzione esponenziale soddisfa la non sazietà su tutto il dominio (per ogni $x$), non solo su un intervallo limitato.

*(slide 13–15)*
