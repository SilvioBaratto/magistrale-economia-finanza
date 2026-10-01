---
title: "Metodi per la Gestione dei Portafogli Personali – Metaeuristiche e Particle Swarm Optimization (PSO)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Lucidi-Parte-6-Elementi-sulla-PSO.pdf"
pages: 82
text_layer: true
verified: true
generated: 2026-07-10
---

## Presentazione del corso e indice

Lezione del corso *Metodi per la gestione dei portafogli personali*, dedicata a **Metaheuristics and PSO** (Particle Swarm Optimization), tenuta da Marco Corazza, Dipartimento di Economia, Università Ca' Foscari di Venezia — A.y. 2024/2025.

Indice della lezione:
- Introduction
- Heuristics and Metaheuristics
- Particle Swarm Optimization
- A simple application

*(slide 1–2)*

## Introduzione: il problema dell'ottimizzazione globale

> [!abstract] Definizione
> «L'obiettivo dell'ottimizzazione globale è trovare la soluzione globalmente migliore di modelli (possibilmente non lineari), in presenza (possibile o nota) di molteplici ottimi locali. Formalmente, l'ottimizzazione globale cerca la/le soluzione/i globale/i di un modello di ottimizzazione vincolato. I modelli non lineari sono onnipresenti in molte applicazioni, ad esempio nella progettazione ingegneristica avanzata, nella biotecnologia, nell'analisi dei dati, nella gestione ambientale, nella pianificazione finanziaria, nel controllo di processo, nella gestione del rischio, nella modellazione scientifica e altro. La loro soluzione richiede spesso un approccio di ricerca globale.» [https://mathworld.wolfram.com/GlobalOptimization.html]
>
> «Per formulare il problema dell'ottimizzazione globale, si assume che la funzione obiettivo $f$ e i vincoli $g$ siano funzioni continue, che i limiti componente per componente $x_l$ e $x_u$ relativi al vettore delle variabili decisionali $\boldsymbol{x}$ siano finiti, e che l'insieme ammissibile $D$ sia non vuoto. Queste ipotesi garantiscono che il modello di ottimizzazione globale sia ben posto poiché [...] l'insieme delle soluzioni del modello di ottimizzazione globale è non vuoto.» [https://mathworld.wolfram.com/GlobalOptimization.html]
>
> I punti di minimo/massimo globale sono in generale difficili da individuare. Esempio (slide, p. 5):
> $$f(x) = \begin{cases} 2x & 0 \le x < 1 \\ 3 & x = 1 \\ -x+3 & 1 < x \le 2 \\ -(x-3)^3+2 & 2 < x \le 3 \end{cases}$$
>
> **Figura (p. 5)** — Grafico della funzione $f(x)$ definita sopra, con frecce che indicano il punto $(0,0)$ e il punto limite per $x\to 1^-$. Il grafico mostra come le discontinuità (il salto a $x=1$, dove $f(1)=3$ mentre $\lim_{x\to1^-}f(x)=2$) rendano ambigua o difficile l'individuazione algoritmica dei punti di minimo/massimo globale: la funzione non è continua e presenta punti esclusi (cerchi vuoti) e punti inclusi (cerchi pieni).

*(slide 3–5)*

## Selezione di portafoglio: il problema base

> [!abstract] Definizione
> La selezione di portafoglio consiste nel ripartire un capitale iniziale tra varie attività rischiose i cui rendimenti futuri sono incerti, al fine di ottimizzare un profilo rischio-rendimento del portafoglio. Data l'incertezza sui rendimenti futuri, un ruolo cruciale è svolto dalla misurazione del rischio associato a tali rendimenti. L'approccio classico rappresenta i rendimenti futuri in termini di variabili aleatorie.
>
> «Consideriamo la regola secondo cui l'investitore considera (o dovrebbe considerare) il rendimento atteso una cosa desiderabile e la varianza del rendimento una cosa indesiderabile.» [Markowitz H.: "Portfolio selection", The Journal of Finance, 1952]
>
> **Problema base di selezione di portafoglio.** Siano $N \ge 2$ attività rischiose,
> $$\boldsymbol{V}=\begin{pmatrix} \sigma_1^2 & \cdots & \sigma_{1,N} \\ \vdots & \ddots & \vdots \\ \sigma_{N,1} & \cdots & \sigma_N^2 \end{pmatrix}$$
> la matrice di varianza-covarianza dei rendimenti delle attività rischiose, $\boldsymbol{r}' = (r_1,\dots,r_N)$ il vettore dei rendimenti attesi delle attività rischiose, $\pi$ il rendimento atteso che l'investitore desidera dal portafoglio, $\boldsymbol{e}' = (1,\dots,1)$.
>
> Il problema base (e più semplice) di selezione di portafoglio è:
> $$\min_{\boldsymbol{x}} \boldsymbol{x}'\boldsymbol{V}\boldsymbol{x} \qquad \text{s.t.} \begin{cases} \boldsymbol{x}'\boldsymbol{r} = \pi \\ \boldsymbol{x}'\boldsymbol{e} = 1 \end{cases}$$
> dove $\boldsymbol{x}' = (x_1,\dots,x_N)$ è il vettore delle percentuali da investire nelle attività rischiose. Questo problema di selezione di portafoglio è **quadratico-lineare**.
>
> **Soluzione in forma chiusa:**
> $$\boldsymbol{x}^{*} = \frac{(\gamma \boldsymbol{V}^{-1}\boldsymbol{r} - \beta \boldsymbol{V}^{-1}\boldsymbol{e})\pi + (\alpha \boldsymbol{V}^{-1}\boldsymbol{e} - \beta \boldsymbol{V}^{-1}\boldsymbol{r})}{\alpha\gamma - \beta^2}$$
> dove
> $$\alpha = \boldsymbol{r}' \boldsymbol{V}^{-1} \boldsymbol{r}, \qquad \beta = \boldsymbol{r}'\boldsymbol{V}^{-1}\boldsymbol{e} = \boldsymbol{e}' \boldsymbol{V}^{-1}\boldsymbol{r}, \qquad \gamma = \boldsymbol{e}'\boldsymbol{V}^{-1}\boldsymbol{e}.$$

*(slide 6–9)*

## Selezione di portafoglio: il problema complesso

> [!abstract] Definizione
> **Problema complesso di selezione di portafoglio:**
> $$\min_{\boldsymbol{x},\boldsymbol{z}} \; a\|\max\{0,\boldsymbol{x}'\boldsymbol{r} - E(\boldsymbol{x}'\boldsymbol{r})\}\|_1 + (1-a)\|\max\{0, E(\boldsymbol{x}'\boldsymbol{r})-\boldsymbol{x}'\boldsymbol{r}\}\|_p - E(\boldsymbol{x}'\boldsymbol{r})$$
> $$\text{s.t.} \begin{cases} \boldsymbol{x}'\boldsymbol{r} \ge \pi \\ \boldsymbol{x}'\boldsymbol{e} = 1 \\ k_d \le \boldsymbol{z}'\boldsymbol{e} \le k_u \\ z_i d \le x_i \le z_i u \;\; \forall i \\ z_i \in \{0,1\} \;\; \forall i \end{cases}$$
> dove
> - $\boldsymbol{z}' = (z_1,\dots,z_N)$ è un vettore di variabili binarie; $z_i=0$ significa che l'$i$-esima attività non è selezionata, $z_i=1$ che è selezionata;
> - $k_d$ e $k_u$ sono rispettivamente il numero minimo e massimo di attività in cui investire;
> - $d$ e $u$ sono rispettivamente la percentuale minima e massima di capitale iniziale da investire nell'$i$-esima attività, se selezionata;
> - $\|\boldsymbol{x}\|_s = \left(\sum_{i=1}^{N} |x_i|^s\right)^s$.
>
> Questo problema di selezione di portafoglio è **fortemente non lineare, non differenziabile e a variabili miste (intere/continue)**.
>
> La funzione obiettivo
> $$a\|\max\{0,\boldsymbol{x}'\boldsymbol{r} - E(\boldsymbol{x}'\boldsymbol{r})\}\|_1 + (1-a)\|\max\{0, E(\boldsymbol{x}'\boldsymbol{r}) -\boldsymbol{x}'\boldsymbol{r}\}\|_p - E(\boldsymbol{x}'\boldsymbol{r})$$
> non è una funzione continua, e i vincoli
> $$k_d \le \boldsymbol{z}'\boldsymbol{e}, \qquad \boldsymbol{z}'\boldsymbol{e} \le k_u, \qquad z_i \in \{0,1\}$$
> non sono funzioni continue.
>
> **Come risolvere il problema complesso di selezione di portafoglio?** In generale, le procedure risolutive necessarie dipendono fortemente dalle caratteristiche peculiari del problema stesso. Perciò, occorre sviluppare procedure risolutive *ad hoc* per ogni problema considerato.

*(slide 10–13)*

## Euristiche

> [!abstract] Definizione
> Quando le soluzioni ottime non possono essere ottenute in modo efficiente, l'unica possibilità è scambiare l'ottimalità con l'efficienza. Gli algoritmi approssimati chiamati **metodi euristici** o **euristiche** cercano di ottenere soluzioni quasi-ottime (*near-optimal solutions*) a un costo computazionale relativamente basso.
>
> «'Heuristic' deriva dal verbo greco *heuriskein* [...] che significa "trovare", mentre il suffisso *meta* significa "oltre, a un livello superiore".» [Blum C. e Roli A.: "Metaheuristics in combinatorial optimization: Overview and conceptual comparison", ACM Computing Surveys, 2003]
>
> «Un'euristica è una tecnica progettata per risolvere un problema più rapidamente quando i metodi classici sono troppo lenti, oppure per trovare una soluzione approssimata quando i metodi classici non riescono a trovare alcuna soluzione esatta. Questo si ottiene scambiando ottimalità, completezza, accuratezza o precisione con la velocità. In un certo senso, può essere considerata una scorciatoia.» [http://www.mit.edu/~moshref/Heuristics.html]
>
> Nel contesto dell'ottimizzazione, un'euristica è un approccio formale che cerca di trovare una soluzione quasi-ottima a un problema utilizzando metodi semplici ed efficienti, piuttosto che una ricerca esaustiva o un'ottimizzazione matematica esatta. Il suo obiettivo è trovare rapidamente una buona soluzione, sufficientemente vicina a quella ottima; le euristiche per l'ottimizzazione comportano spesso un compromesso (*trade-off*) tra efficienza computazionale e qualità della soluzione.
>
> **Possibile flowchart:**
> ```
> Generazione casuale della/e soluzione/i iniziale/i
> while stopping_criterion = false do
>     Regola intelligente 1
>     Regola intelligente 2
>     ⋮
>     Regola intelligente z
> end while
> ```

*(slide 14–17)*

## Metaeuristiche: definizione, principi e classificazione

> [!abstract] Definizione
> Le **metaeuristiche** sono state proposte in letteratura a partire dal 1980 per superare i limiti delle euristiche.
>
> «Una metaeuristica è formalmente definita come un processo di generazione iterativo che guida un'euristica subordinata combinando in modo intelligente diversi concetti per esplorare e sfruttare lo spazio di ricerca; strategie di apprendimento vengono utilizzate per strutturare le informazioni al fine di trovare in modo efficiente soluzioni quasi-ottime.» [Osman I.H., Laporte G.: "Metaheuristics: A bibliography", Annals of Operations Research, 1996]
>
> «L'esplorazione (*exploration*) è la capacità di un algoritmo di ricerca di esplorare diverse regioni dello spazio di ricerca al fine di individuare un buon ottimo. Lo sfruttamento (*exploitation*), d'altra parte, è la capacità di concentrare la ricerca attorno a un'area promettente al fine di raffinare una soluzione candidata.» [Engelbrecht A.P.: "Computational Intelligence. An Introduction", John Wiley & Sons, 2007]
>
> **Figura (p. 19)** — Schema con un insieme di particelle ("I") disposte attorno a un obiettivo centrale ("Goal"): frecce etichettate *Exploration* mostrano particelle che si allontanano verso nuove regioni dello spazio di ricerca, frecce etichettate *Exploitation* mostrano particelle che convergono verso il goal. Il disegno illustra il bilanciamento tra ricerca di nuove aree e raffinamento attorno a una soluzione promettente.
>
> Una metaeuristica è un framework algoritmico generale applicabile a diversi problemi di ottimizzazione con relativamente poche modifiche. In generale, le metaeuristiche:
> - non sono specifiche per un particolare problema di ottimizzazione;
> - sono in grado di rilevare ed esplorare in modo efficiente le aree più promettenti dello spazio delle soluzioni;
> - sono metodi risolutivi approssimati;
> - sono metodi risolutivi stocastici;
> - possono essere in grado di evitare le trappole dei minimi locali;
> - possono incorporare una qualche forma di memoria per migliorare la ricerca.
>
> **Figura (p. 21)** — Schema di classificazione: dal nodo centrale "MAs" (Metaheuristic Algorithms) si diramano, lungo l'asse "Number of solutions", gli "Population based algorithms" e i "Trajectory-based algorithms"; lungo l'asse "Inspiration type", gli "Evolutionary algorithms", i "Physics-based algorithms", gli "Human-based algorithms" e gli "Swarm-based algorithms". [Nassef A.M., Abdelkareem M.A., Maghrabie H.M. e Baroutaji A.: "Review of metaheuristic optimization algorithms for power systems problems", Sustainability, 2023]
>
> **Metaeuristiche population-based vs. a punto singolo.** Dipende dal numero di soluzioni (approssimate) usate contemporaneamente dalla metaeuristica: molte, cioè una metaeuristica *population-based*; una sola, cioè una metaeuristica *trajectory-based*.
>
> **Metaeuristiche nature-inspired vs. non nature-inspired.** Gli esagoni possiedono il più alto rapporto superficie/perimetro tra tutti i poligoni: questo suggerisce che le api costruiscono le celle a forma esagonale per minimizzare l'uso di materiale (figura: un'ape su un favo esagonale). Si tratta di una classificazione debole, poiché esistono metaeuristiche ibride.
>
> **Metaeuristiche evolutive vs. non evolutive.** «L'evoluzione biologica è l'ottimizzazione della capacità di un organismo di sopravvivere in ambienti dinamicamente mutevoli e competitivi.» [Erwin K. e Engelbrecht A.: "Meta-heuristics for portfolio optimization", Soft Computing, 2023] Il termine "evolutivo" denota tipicamente una categoria di metaeuristiche ispirate ai principi dell'evoluzione biologica: in questi algoritmi, un insieme designato di soluzioni (*pool*) è impiegato in ogni iterazione del processo risolutivo con l'obiettivo di migliorarlo, cioè far evolvere questo insieme di soluzioni tramite operatori che modificano le soluzioni stesse.
>
> **Metaeuristiche memory-less vs. memory-usage.** L'assenza di memoria nelle metaeuristiche comporta la perdita delle informazioni acquisite nelle iterazioni precedenti: tali metaeuristiche non hanno alcuna consapevolezza della propria storia riguardo alle soluzioni scoperte in precedenza.

*(slide 18–25)*

## Particle Swarm Optimization (PSO): idea e principi

> [!abstract] Definizione
> «[La *Swarm Intelligence*] è definita come la cooperazione di individui all'interno di un gruppo per risolvere un obiettivo scambiando informazioni disponibili localmente.» [Erwin K. e Engelbrecht A.: "Meta-heuristics for portfolio optimization", Soft Computing, 2023]
>
> La **PSO** è una metaeuristica *nature-inspired*, iterativa, *population-based*, con uso di memoria (*memory-usage*), evolutiva, *derivative-free*, per la soluzione di problemi di ottimizzazione globale non vincolata.
>
> L'idea della PSO è replicare il comportamento degli stormi di uccelli quando cooperano per ottimizzare la ricerca di cibo. A tale scopo, ogni membro, cioè ogni particella dello sciame, esplora l'area di ricerca mantenendo memoria della propria miglior posizione raggiunta finora. Questa informazione viene poi scambiata con i vicini nello sciame. Così, l'intero sciame è supposto convergere infine verso la miglior posizione globale raggiunta dai membri dello sciame.
>
> **Figura (p. 28)** — Due immagini affiancate: "Flocks of birds" (uno stormo di storni in volo che forma una nuvola scura e sinuosa nel cielo) e "Shoal of fishes" (un banco di pesci che nuota in cerchio attorno a una formazione corallina). Le immagini illustrano il comportamento collettivo di sciame (*swarm*) da cui la PSO trae ispirazione.
>
> Nella sua controparte matematica, il paradigma di uno stormo in volo può essere formulato come segue. Dato un problema di minimizzazione/massimizzazione:
> 1. ogni membro dello sciame rappresenta una possibile soluzione del problema di minimizzazione/massimizzazione;
> 2. ogni particella è inizialmente posizionata in modo casuale nell'insieme ammissibile del problema;
> 3. a ogni particella viene inoltre assegnata inizialmente una velocità casuale, usata per determinare la sua direzione iniziale di movimento.

*(slide 26–29)*

## PSO: formalizzazione matematica e topologie di vicinato

> [!abstract] Definizione
> Per una descrizione formale dell'algoritmo PSO, si consideri il seguente problema di ottimizzazione globale:
> $$\min_{\boldsymbol{x}\in\mathbb{R}^d} f(\boldsymbol{x}), \qquad f:\mathbb{R}^d \to \mathbb{R}.$$
>
> Si assuma che siano considerate $M$ particelle (cioè soluzioni). Al passo $k$-esimo dell'algoritmo PSO, tre vettori sono associati alla $j$-esima particella:
> - $\boldsymbol{x}_j^k \in \mathbb{R}^d$: posizione al passo $k$ della $j$-esima particella;
> - $\boldsymbol{v}_j^k \in \mathbb{R}^d$: velocità al passo $k$ della $j$-esima particella;
> - $\boldsymbol{p}_j \in \mathbb{R}^d$: miglior posizione visitata finora dalla $j$-esima particella ($pbest_j = f(\boldsymbol{p}_j)$).
>
> Inoltre, $\boldsymbol{p}_{g,nei} \in \mathbb{R}^d$ indica la miglior posizione visitata finora dai membri dello sciame appartenenti a un dato vicinato (*neighborhood*) $nei$ di una qualsiasi particella. La $\boldsymbol{p}_{g,nei}$ associata a ciascuna particella dipende dalla **topologia** del vicinato a cui la particella appartiene: il termine "topologia" si riferisce alla struttura delle connessioni tra le particelle dello sciame, attraverso le quali le particelle scambiano informazioni e si influenzano reciprocamente durante il processo di ottimizzazione.
>
> **Figura (p. 33)** — Tre schemi di grafo che rappresentano altrettante tipologie di vicinato: **Fully connected neighborhood** (ogni particella è collegata a tutte le altre), **von Neumann neighborhood** (collegamenti incrociati parziali tra le particelle) e **Ring neighborhood** (le particelle sono disposte in anello, ciascuna collegata solo alle vicine adiacenti). La figura mostra come topologie diverse determinino quali sottoinsiemi di particelle condividono l'informazione sulla miglior posizione trovata.

*(slide 30–33)*

## PSO: l'algoritmo con peso d'inerzia

> [!abstract] Definizione
> L'algoritmo PSO (nella versione con peso d'inerzia, *inertia weight*) è:
> 1. Poni $k=1$ e valuta $f(\boldsymbol{x}_j^k)$ per $j=1,\dots,M$. Poni $pbest_j = +\infty$.
> 2. Ripeti finché un criterio di arresto non è soddisfatto:
>    - se $f(\boldsymbol{x}_j^k) < pbest_j$ allora poni $\boldsymbol{p}_j = \boldsymbol{x}_j^k$ e $pbest_j = f(\boldsymbol{x}_j^k)$;
>    - se $f(\boldsymbol{x}_j^k) < gbest$ allora poni $\boldsymbol{p}_g = \boldsymbol{x}_j^k$ e $gbest = f(\boldsymbol{x}_j^k)$;
>    - aggiorna posizione e velocità della $j$-esima particella come
> $$\begin{cases} \boldsymbol{v}_j^{k+1} = w^{k+1}\boldsymbol{v}_j^k + \boldsymbol{U}_{\phi_1}\otimes(\boldsymbol{p}_j - \boldsymbol{x}_j^k) + \boldsymbol{U}_{\phi_2}\otimes(\boldsymbol{p}_g - \boldsymbol{x}_j^k) \\ \boldsymbol{x}_j^{k+1} = \boldsymbol{x}_j^k + \boldsymbol{v}_j^{k+1} \end{cases}$$
>      dove $\boldsymbol{U}_{\phi_1}$ e $\boldsymbol{U}_{\phi_2}$ sono distribuiti uniformemente in $[0,\phi_1]$ e $[0,\phi_2]$ rispettivamente, e $\otimes$ indica il prodotto componente per componente;
> 3. aggiorna $k=k+1$ e torna al punto 2.
>
> I valori di $\phi_1$ e $\phi_2$ influenzano la performance dell'algoritmo. Per ottenere la convergenza dello sciame, $\phi_1$ e $\phi_2$ devono essere impostati in accordo con il valore del peso d'inerzia $w^k$.
>
> $w^k$ è generalmente linearmente decrescente col numero di passi, cioè
> $$w^k = w_{max} + \frac{w_{min}-w_{max}}{K}k,$$
> dove $w_{min}$ e $w_{max}$ sono di solito $0.4$ e $0.9$ rispettivamente, e $K$ indica il numero massimo di passi consentiti.
>
> $w^k$ può anche essere costante,
> $$w^k = w = 0.7298.$$
> In questo scenario è opportuno stabilire un limite superiore per $\boldsymbol{v}_j^k$, con $j=1,\dots,M$ e $k=0,\dots,K$, per prevenire comportamenti divergenti durante il processo di ottimizzazione.
>
> **Figura (p. 37)** — Schema che illustra l'aggiornamento della posizione di una particella: dalla posizione corrente $x_i(t)$ (punto rosso) si compongono il moto corrente/inerzia $v_i(t)$, l'accelerazione cognitiva $c_1 r_1[\hat{x}_i(t)-x_i(t)]$ diretta verso la miglior soluzione individuale $\hat{x}_i(t)$ (punto verde) e l'accelerazione sociale $c_2 r_2[g(t)-x_i(t)]$ diretta verso la miglior soluzione candidata globale $g(t)$ (punto blu). La combinazione vettoriale di questi tre contributi produce la nuova velocità $v_i(t+1)$ e la posizione aggiornata $x_i(t+1)$ (punto nero). La figura mostra visivamente come la formula di aggiornamento combini inerzia, componente cognitiva e componente sociale.

*(slide 34–37)*

## PSO: risultato di convergenza

> [!tip] Teorema
> «I nostri risultati mostrano che la SPSO (*Standard PSO*) raggiunge l'ottimo globale **in probabilità**.» [Xu G. e Yu G.: "On convergence analysis of particle swarm optimization algorithm", Journal of Computational and Applied Mathematics, 2018]

*(slide 38)*

## GA e PSO per l'ottimizzazione vincolata: il metodo di penalizzazione esatta

> [!tip] Teorema
> Gli algoritmi genetici (GA) e la PSO sono metaeuristiche per la soluzione di problemi di ottimizzazione globale **non vincolata**. Possono essere utilizzati per risolvere problemi di ottimizzazione globale **vincolata**?
> $$\min_{\boldsymbol{x}\in\mathbb{R}^d} f(\boldsymbol{x}) \qquad \text{s.t.} \begin{cases} g_r(\boldsymbol{x}) = a_r, & \text{con } r=1,\dots,R \\ h_s(\boldsymbol{x}) \ge b_s, & \text{con } s=1,\dots,S \end{cases}$$
> dove $f(\cdot), g_r(\cdot), h_s(\cdot): \mathbb{R}^d \to \mathbb{R}$.
>
> Un problema di ottimizzazione globale vincolata può essere affrontato usando un **metodo di penalizzazione esatta** (*Exact Penalty Method*):
>
> 1. Si riformula il problema vincolato come segue:
> $$\min_{\boldsymbol{x}\in\mathbb{R}^d} f(\boldsymbol{x}) + \frac{1}{\varepsilon}\left[\sum_{r=1}^{R} |g_r(\boldsymbol{x})-a_r| + \sum_{s=1}^{S} \max(0,b_s-h_s(\boldsymbol{x}))\right]$$
> dove $\varepsilon$ è il cosiddetto **fattore di penalizzazione**; $|g_r(\boldsymbol{x})-a_r|$ funge da misura della violazione dei vincoli espressi in forma di uguaglianza; $\max(0,b_s-h_s(\boldsymbol{x}))$ funge da misura della violazione dei vincoli espressi in forma di disuguaglianza.
> 2. È possibile dimostrare che, per valori appropriati di $\varepsilon$, la/le soluzione/i del problema di ottimizzazione globale vincolato e di quello non vincolato coincidono.

*(slide 39–41)*

## PSO per vincoli complessi (variabili binarie)

> [!abstract] Definizione
> Nel caso di vincoli complessi, come quelli su variabili binarie, si può definire una misura di violazione ad hoc:
>
> | Vincolo | Violazione del vincolo |
> |---|---|
> | $z_i \in \{0,1\}$ | $z_i(1-z_i)$ |
> | $\vdots$ | $\vdots$ |
>
> Questa violazione è nulla se e solo se $z_i \in \{0,1\}$, ed è positiva per qualunque altro valore reale di $z_i$, permettendo di inglobarla nella funzione di penalizzazione del metodo visto in precedenza.

*(slide 42)*

## Applicazione semplice: il problema base di selezione di portafoglio (versione in inglese)

> [!example] Esempio
> **Dati.** Problema base di selezione di portafoglio con
> $$\boldsymbol{V} = \begin{pmatrix} 0.000748044 & -0.000238393 & -0.000234123 \\ -0.000238393 & 0.000841507 & 0.000053341 \\ -0.000234123 & 0.000053341 & 0.000707590 \end{pmatrix}, \qquad \boldsymbol{r}' = (0.046492,\ 0.050035,\ 0.047376).$$
>
> **Formulazione vincolata:**
> $$\min_{\boldsymbol{x}} \boldsymbol{x}'\boldsymbol{V}\boldsymbol{x} \qquad \text{s.t.} \begin{cases} \boldsymbol{x}'\boldsymbol{r} = \pi \\ \boldsymbol{x}'\boldsymbol{e} = 1\end{cases}$$
>
> **Formulazione non vincolata via metodo di penalizzazione esatta:**
> $$\min_{\boldsymbol{x}} \boldsymbol{x}'\boldsymbol{V}\boldsymbol{x} + \frac{1}{\varepsilon}(|\boldsymbol{x}'\boldsymbol{r} - \pi| + |\boldsymbol{x}'\boldsymbol{e} - 1|)$$
>
> **Figura (p. 45)** — Grafico a dispersione della frontiera efficiente ottenuta risolvendo il problema per 9 diversi valori di $\pi$ (scenari numerati da 1 a 9, punti blu collegati da una linea), con una freccia che indica, per confronto, un punto interno non efficiente (marcatori a croce e quadrato rosso). Il grafico mostra la tipica forma "a parabola rovesciata" della frontiera media-varianza, con SQMP sull'asse orizzontale e RP sull'asse verticale.
>
> **Risultati per $\pi = 0.049149$ (scenario 7):**
>
> | Method | $x_1$ | $x_2$ | $x_3$ | $\boldsymbol{x}'\boldsymbol{V}\boldsymbol{x}$ | $\boldsymbol{x}'\boldsymbol{r}$ | $\boldsymbol{x}'\boldsymbol{e}$ |
> |---|---|---|---|---|---|---|
> | Exact | 0.161 | 0.721 | 0.118 | 0.000411 | 0.049149 | 1.000000 |
> | PSO | 0.156 | 0.716 | 0.128 | 0.000409 | 0.049142 | 1.000000 |
>
> La soluzione trovata dalla PSO è molto vicina alla soluzione esatta, sia in termini di composizione del portafoglio sia in termini di varianza e rendimento realizzati, con il vincolo di budget $\boldsymbol{x}'\boldsymbol{e}=1$ soddisfatto esattamente.

*(slide 43–46)*

## Applicazione complessa: riferimento bibliografico

Per il problema complesso di selezione di portafoglio
$$\min_{\boldsymbol{x},\boldsymbol{z}} a\|\max\{0,\boldsymbol{x}'\boldsymbol{r} - E(\boldsymbol{x}'\boldsymbol{r})\}\|_1 + (1-a)\|\max\{0, E(\boldsymbol{x}'\boldsymbol{r}) -\boldsymbol{x}'\boldsymbol{r}\}\|_p - E(\boldsymbol{x}'\boldsymbol{r})$$
$$\text{s.t.} \begin{cases} \boldsymbol{x}'\boldsymbol{r} \ge \pi \\ \boldsymbol{x}'\boldsymbol{e} = 1 \\ k_d \le \boldsymbol{z}'\boldsymbol{e} \le k_u \\ z_i d \le x_i \le z_i u \;\; \forall i \\ z_i \in \{0,1\} \;\; \forall i \end{cases}$$
si rimanda a: Corazza M., Fasano G., Gusso R.: "Particle Swarm Optimization with non-smooth penalty reformulation, for a complex portfolio selection problem", Applied Mathematics and Computation, 224, 611-624, 2013.

*(slide 47)*

## Un'applicazione alla selezione di portafoglio alla Markowitz: dati e soluzioni esatte

> [!example] Esempio
> Si considerano $D = 3$ attività azionarie rischiose.
>
> **Vettore dei rendimenti attesi:**
>
> | | R |
> |---|---|
> | Titolo 1 | 4,6492% |
> | Titolo 2 | 5,0035% |
> | Titolo 3 | 4,7376% |
>
> **Matrice di varianza-covarianza:**
>
> | | Titolo 1 | Titolo 2 | Titolo 3 |
> |---|---|---|---|
> | Titolo 1 | 0,000748044 | -0,000238393 | -0,000234123 |
> | Titolo 2 | -0,000238393 | 0,000841507 | 0,000053341 |
> | Titolo 3 | -0,000234123 | 0,000053341 | 0,000707590 |
>
> **Portafogli esatti alla Markowitz**, ottenuti dalla soluzione in forma chiusa al variare di $\pi$ (9 scenari):
>
> | Scenari | RP | x1 | x2 | x3 | VP | SQMP |
> |---|---|---|---|---|---|---|
> | 1 | 0,046492 | 0,610106 | -0,129612 | 0,519506 | 0,000366 | 0,019122 |
> | 2 | 0,046935 | 0,535320 | 0,012081 | 0,452599 | 0,000243 | 0,015604 |
> | 3 | 0,047377 | 0,460534 | 0,153773 | 0,385693 | 0,000173 | 0,013161 |
> | 4 | 0,047756 | 0,396629 | 0,274850 | 0,328521 | 0,000154 | 0,012420 |
> | 5 | 0,048263 | 0,310962 | 0,437158 | 0,251880 | 0,000188 | 0,013722 |
> | 6 | 0,048706 | 0,236176 | 0,578851 | 0,184974 | 0,000274 | 0,016543 |
> | 7 | 0,049149 | 0,161389 | 0,720543 | 0,118067 | 0,000411 | 0,020272 |
> | 8 | 0,049592 | 0,086603 | 0,862236 | 0,051161 | 0,000600 | 0,024497 |
> | 9 | 0,050035 | 0,011817 | 1,003928 | -0,015746 | 0,000841 | 0,029003 |
>
> dove RP è il rendimento del portafoglio, VP la varianza e SQMP lo scarto quadratico medio (radice della varianza).

*(slide 48–49)*

## Impostazione dell'algoritmo PSO per l'applicazione

> [!example] Esempio
> **Portafogli approssimati alla PSO — parametri utilizzati:**
> - Numero di particelle: 15, 20, 25 e 30.
> - Topologia di intorno utilizzata: *fully connected*.
> - Valori attribuiti al peso d'inerzia e ai due parametri $c_1$ e $c_2$: $w^k = 0.85$; $c_1 = 0.5$; $c_2 = 0.7$.
> - Criterio di arresto: raggiungimento di un prefissato numero massimo di iterazioni, $k_{max} = 8000$.
> - Inizializzazione delle posizioni: valori uniformemente distribuiti appartenenti all'intervallo $[0,1)$, opportunamente normalizzati.
> - Inizializzazione delle velocità: valori uniformemente distribuiti appartenenti all'intervallo $[0,1)$.

*(slide 50–51)*

## Obiettivi degli esperimenti numerici

- **Esperimento 1**: stabilire sperimentalmente un valore "buono" del parametro di penalizzazione $\varepsilon$.
- **Esperimento 2**: descrivere le problematiche concernenti una "cattiva" inizializzazione.
- **Esperimenti 3, 4, 5 e 6**: stabilire sperimentalmente un valore "buono" del numero $N$ di particelle, analizzando la convergenza della soluzione della PSO al variare del numero di queste ultime.
- **Esperimento 7**: determinati i valori "ottimi" di $\varepsilon$ e di $N$, analizzare i portafogli selezionati dalla PSO.

*(slide 52)*

## Esperimento 1 — Il parametro di penalizzazione ε

> [!example] Esempio
> Valori considerati di $\varepsilon$: $1,\ 0.1,\ 0.01,\ 0.001,\ 0.0001$. Scenario di riferimento: 7.
>
> | Scenario | RP | x1 | x2 | x3 | VP | SQMP |
> |---|---|---|---|---|---|---|
> | 7 | 0,049149 | 0,161389 | 0,720543 | 0,118067 | 0,000411 | 0,020272 |
>
> Per ciascun valore di $\varepsilon$ sono state condotte 20 simulazioni PSO sullo scenario 7. "Som." è la somma dei pesi del portafoglio ($x_1+x_2+x_3$, sempre pari a 1).
>
> **ε = 1**
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 7 | 1 | 0,000455 | 0,091143 | 0,680362 | 0,228495 | 0,000410 | 0,049104 | 0,020247 | 1 |
> | 7 | 2 | 0,000444 | 0,054203 | 0,682965 | 0,262832 | 0,000438 | 0,049144 | 0,020939 | 1 |
> | 7 | 3 | 0,000413 | 0,185686 | 0,728669 | 0,085645 | 0,000412 | 0,049149 | 0,020310 | 1 |
> | 7 | 4 | 0,000847 | 0,031564 | 0,500800 | 0,467636 | 0,000377 | 0,048679 | 0,019418 | 1 |
> | 7 | 5 | 0,000528 | 0,175325 | 0,658324 | 0,166351 | 0,000350 | 0,048971 | 0,018716 | 1 |
> | 7 | 6 | 0,000415 | 0,156031 | 0,716338 | 0,127630 | 0,000409 | 0,049142 | 0,020216 | 1 |
> | 7 | 7 | 0,000422 | 0,218578 | 0,738024 | 0,043398 | 0,000417 | 0,049145 | 0,020432 | 1 |
> | 7 | 8 | 0,000635 | 0,110127 | 0,592253 | 0,297620 | 0,000339 | 0,048853 | 0,018420 | 1 |
> | 7 | 9 | 0,000419 | 0,103761 | 0,701386 | 0,194854 | 0,000419 | 0,049149 | 0,020477 | 1 |
> | 7 | 10 | 0,000634 | 0,195116 | 0,608327 | 0,196557 | 0,000305 | 0,048821 | 0,017477 | 1 |
> | 7 | 11 | 0,000438 | 0,058473 | 0,686202 | 0,255325 | 0,000437 | 0,049149 | 0,020916 | 1 |
> | 7 | 12 | 0,000476 | 0,095694 | 0,669656 | 0,234650 | 0,000399 | 0,049072 | 0,019972 | 1 |
> | 7 | 13 | 0,000415 | 0,156897 | 0,716750 | 0,126353 | 0,000409 | 0,049143 | 0,020218 | 1 |
> | 7 | 14 | 0,000683 | 0,044381 | 0,568836 | 0,386783 | 0,000383 | 0,048849 | 0,019571 | 1 |
> | 7 | 15 | 0,000435 | 0,140874 | 0,700552 | 0,158575 | 0,000400 | 0,049114 | 0,019999 | 1 |
> | 7 | 16 | 0,000423 | 0,229610 | 0,743222 | 0,027168 | 0,000423 | 0,049149 | 0,020559 | 1 |
> | 7 | 17 | 0,000749 | 0,077554 | 0,539411 | 0,383035 | 0,000341 | 0,048741 | 0,018476 | 1 |
> | 7 | 18 | 0,000418 | 0,194731 | 0,728955 | 0,076314 | 0,000411 | 0,049142 | 0,020272 | 1 |
> | 7 | 19 | 0,000550 | 0,123680 | 0,635531 | 0,240790 | 0,000357 | 0,048956 | 0,018901 | 1 |
> | 7 | 20 | 0,000933 | 0,189185 | 0,468795 | 0,342021 | 0,000239 | 0,048455 | 0,015460 | 1 |
>
> **ε = 0,1**
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 7 | 1 | 0,001590 | 0,159651 | 0,674045 | 0,166304 | 0,000369 | 0,049027 | 0,019214 | 1 |
> | 7 | 2 | 0,000444 | 0,086747 | 0,694992 | 0,218262 | 0,000424 | 0,049147 | 0,020600 | 1 |
> | 7 | 3 | 0,000599 | 0,088711 | 0,689622 | 0,221667 | 0,000419 | 0,049131 | 0,020464 | 1 |
> | 7 | 4 | 0,000461 | 0,201335 | 0,732021 | 0,066644 | 0,000413 | 0,049144 | 0,020323 | 1 |
> | 7 | 5 | 0,006516 | 0,113791 | 0,470642 | 0,415567 | 0,000291 | 0,048526 | 0,017072 | 1 |
> | 7 | 6 | 0,001047 | 0,150479 | 0,692160 | 0,157360 | 0,000388 | 0,049083 | 0,019710 | 1 |
> | 7 | 7 | 0,000443 | 0,047681 | 0,682743 | 0,269576 | 0,000443 | 0,049149 | 0,021059 | 1 |
> | 7 | 8 | 0,000517 | -0,002782 | 0,667382 | 0,335400 | 0,000480 | 0,049153 | 0,021900 | 1 |
> | 7 | 9 | 0,000413 | 0,187714 | 0,729268 | 0,083018 | 0,000413 | 0,049149 | 0,020314 | 1 |
> | 7 | 10 | 0,004569 | 0,223356 | 0,579766 | 0,196879 | 0,000277 | 0,048720 | 0,016657 | 1 |
> | 7 | 11 | 0,000423 | 0,216023 | 0,738516 | 0,045461 | 0,000418 | 0,049148 | 0,020451 | 1 |
> | 7 | 12 | 0,003132 | 0,043197 | 0,578063 | 0,378740 | 0,000388 | 0,048875 | 0,019695 | 1 |
> | 7 | 13 | 0,000427 | 0,082949 | 0,694465 | 0,222586 | 0,000426 | 0,049149 | 0,020650 | 1 |
> | 7 | 14 | 0,001169 | 0,025687 | 0,647996 | 0,326317 | 0,000440 | 0,049076 | 0,020973 | 1 |
> | 7 | 15 | 0,000427 | 0,105981 | 0,702417 | 0,191601 | 0,000419 | 0,049150 | 0,020468 | 1 |
> | 7 | 16 | 0,000459 | 0,065192 | 0,687600 | 0,247208 | 0,000433 | 0,049146 | 0,020821 | 1 |
> | 7 | 17 | 0,005664 | -0,078783 | 0,448082 | 0,630700 | 0,000525 | 0,048637 | 0,022920 | 1 |
> | 7 | 18 | 0,002288 | 0,139776 | 0,640560 | 0,219664 | 0,000352 | 0,048955 | 0,018761 | 1 |
> | 7 | 19 | 0,001221 | 0,099179 | 0,668834 | 0,231987 | 0,000396 | 0,049066 | 0,019901 | 1 |
> | 7 | 20 | 0,002250 | 0,298232 | 0,695505 | 0,006263 | 0,000374 | 0,048961 | 0,019347 | 1 |
>
> **ε = 0,01**
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 7 | 1 | 0,038309 | 0,219889 | 0,597012 | 0,183099 | 0,000290 | 0,048769 | 0,017031 | 1 |
> | 7 | 2 | 0,015167 | -0,037465 | 0,599226 | 0,438239 | 0,000486 | 0,049002 | 0,022034 | 1 |
> | 7 | 3 | 0,020493 | 0,069803 | 0,614524 | 0,315673 | 0,000382 | 0,048948 | 0,019541 | 1 |
> | 7 | 4 | 0,000597 | 0,048869 | 0,683717 | 0,267413 | 0,000443 | 0,049150 | 0,021053 | 1 |
> | 7 | 5 | 0,000496 | 0,140370 | 0,713240 | 0,146390 | 0,000412 | 0,049148 | 0,020292 | 1 |
> | 7 | 6 | 0,000416 | 0,205339 | 0,735153 | 0,059508 | 0,000416 | 0,049149 | 0,020391 | 1 |
> | 7 | 7 | 0,006243 | 0,136514 | 0,690274 | 0,173212 | 0,000393 | 0,049090 | 0,019821 | 1 |
> | 7 | 8 | 0,041137 | 0,024743 | 0,521873 | 0,453384 | 0,000389 | 0,048741 | 0,019721 | 1 |
> | 7 | 9 | 0,007307 | 0,107217 | 0,676549 | 0,216234 | 0,000397 | 0,049080 | 0,019925 | 1 |
> | 7 | 10 | 0,040899 | -0,001207 | 0,514250 | 0,486957 | 0,000418 | 0,048744 | 0,020436 | 1 |
> | 7 | 11 | 0,000610 | 0,029366 | 0,676070 | 0,294564 | 0,000454 | 0,049147 | 0,021317 | 1 |
> | 7 | 12 | 0,003214 | 0,000631 | 0,656782 | 0,342587 | 0,000470 | 0,049121 | 0,021674 | 1 |
> | 7 | 13 | 0,026752 | 0,004905 | 0,569514 | 0,425581 | 0,000425 | 0,048886 | 0,020607 | 1 |
> | 7 | 14 | 0,000603 | 0,069645 | 0,689399 | 0,240955 | 0,000432 | 0,049147 | 0,020776 | 1 |
> | 7 | 15 | 0,000767 | 0,016781 | 0,673609 | 0,309610 | 0,000464 | 0,049152 | 0,021548 | 1 |
> | 7 | 16 | 0,000412 | 0,142324 | 0,714205 | 0,143471 | 0,000412 | 0,049149 | 0,020295 | 1 |
> | 7 | 17 | 0,000430 | 0,075659 | 0,692044 | 0,232297 | 0,000429 | 0,049149 | 0,020723 | 1 |
> | 7 | 18 | 0,005664 | 0,080863 | 0,674023 | 0,245115 | 0,000412 | 0,049096 | 0,020299 | 1 |
> | 7 | 19 | 0,001821 | 0,051015 | 0,678650 | 0,270335 | 0,000438 | 0,049135 | 0,020925 | 1 |
> | 7 | 20 | 0,017494 | 0,019357 | 0,609137 | 0,371506 | 0,000425 | 0,048978 | 0,020624 | 1 |
>
> **ε = 0,001**
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 7 | 1 | 0,009715 | 0,021820 | 0,670665 | 0,307514 | 0,000458 | 0,049140 | 0,021393 | 1 |
> | 7 | 2 | 0,000651 | 0,102430 | 0,700857 | 0,196713 | 0,000420 | 0,049149 | 0,020485 | 1 |
> | 7 | 3 | 0,016240 | 0,007033 | 0,663299 | 0,329667 | 0,000467 | 0,049133 | 0,021615 | 1 |
> | 7 | 4 | 0,001769 | 0,137732 | 0,713189 | 0,149079 | 0,000413 | 0,049150 | 0,020318 | 1 |
> | 7 | 5 | 0,000895 | 0,251540 | 0,750337 | -0,001878 | 0,000431 | 0,049148 | 0,020765 | 1 |
> | 7 | 6 | 0,615775 | 0,112547 | 0,472838 | 0,414615 | 0,000293 | 0,048533 | 0,017116 | 1 |
> | 7 | 7 | 0,059246 | 0,015902 | 0,650068 | 0,334030 | 0,000450 | 0,049090 | 0,021225 | 1 |
> | 7 | 8 | 0,086443 | 0,030151 | 0,644570 | 0,325279 | 0,000434 | 0,049063 | 0,020825 | 1 |
> | 7 | 9 | 0,122246 | 0,050553 | 0,637879 | 0,311569 | 0,000411 | 0,049027 | 0,020284 | 1 |
> | 7 | 10 | 0,047044 | 0,075929 | 0,674598 | 0,249473 | 0,000416 | 0,049102 | 0,020395 | 1 |
> | 7 | 11 | 0,046373 | -0,070367 | 0,626264 | 0,444104 | 0,000539 | 0,049103 | 0,023208 | 1 |
> | 7 | 12 | 0,005630 | 0,112556 | 0,702353 | 0,185091 | 0,000415 | 0,049144 | 0,020378 | 1 |
> | 7 | 13 | 0,000436 | 0,135029 | 0,711771 | 0,153200 | 0,000413 | 0,049149 | 0,020315 | 1 |
> | 7 | 14 | 0,029153 | 0,106490 | 0,691483 | 0,202027 | 0,000409 | 0,049120 | 0,020235 | 1 |
> | 7 | 15 | 0,128791 | 0,111024 | 0,655508 | 0,233468 | 0,000379 | 0,049020 | 0,019465 | 1 |
> | 7 | 16 | 0,004210 | 0,089527 | 0,698078 | 0,212396 | 0,000425 | 0,049153 | 0,020618 | 1 |
> | 7 | 17 | 0,061528 | 0,118595 | 0,683327 | 0,198079 | 0,000396 | 0,049088 | 0,019900 | 1 |
> | 7 | 18 | 0,002177 | 0,147045 | 0,715110 | 0,137845 | 0,000411 | 0,049147 | 0,020269 | 1 |
> | 7 | 19 | 0,011736 | 0,040795 | 0,676208 | 0,282997 | 0,000445 | 0,049138 | 0,021084 | 1 |
> | 7 | 20 | 0,001001 | 0,144477 | 0,715143 | 0,140380 | 0,000412 | 0,049149 | 0,020295 | 1 |
>
> **ε = 0,0001**
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 7 | 1 | 4,202541 | 0,012315 | 0,512954 | 0,474731 | 0,000401 | 0,048729 | 0,020031 | 1 |
> | 7 | 2 | 4,584677 | 0,231172 | 0,571332 | 0,197495 | 0,000270 | 0,048690 | 0,016430 | 1 |
> | 7 | 3 | 0,427817 | 0,030394 | 0,660924 | 0,308682 | 0,000443 | 0,049106 | 0,021059 | 1 |
> | 7 | 4 | 0,003359 | 0,179173 | 0,726566 | 0,094261 | 0,000412 | 0,049149 | 0,020294 | 1 |
> | 7 | 5 | 0,340798 | 0,159958 | 0,707266 | 0,132776 | 0,000399 | 0,049115 | 0,019967 | 1 |
> | 7 | 6 | 2,139982 | 0,203114 | 0,653947 | 0,142939 | 0,000338 | 0,048935 | 0,018391 | 1 |
> | 7 | 7 | 0,111120 | 0,157167 | 0,714984 | 0,127848 | 0,000407 | 0,049138 | 0,020174 | 1 |
> | 7 | 8 | 0,000413 | 0,144419 | 0,714902 | 0,140679 | 0,000412 | 0,049149 | 0,020290 | 1 |
> | 7 | 9 | 4,007613 | 0,009413 | 0,519320 | 0,471267 | 0,000406 | 0,048748 | 0,020146 | 1 |
> | 7 | 10 | 0,000483 | 0,028372 | 0,676326 | 0,295303 | 0,000455 | 0,049149 | 0,021342 | 1 |
> | 7 | 11 | 0,331235 | 0,155577 | 0,706169 | 0,138254 | 0,000399 | 0,049116 | 0,019981 | 1 |
> | 7 | 12 | 4,784923 | 0,063029 | 0,507909 | 0,429062 | 0,000346 | 0,048670 | 0,018591 | 1 |
> | 7 | 13 | 0,634516 | 0,263132 | 0,730518 | 0,006349 | 0,000409 | 0,049085 | 0,020223 | 1 |
> | 7 | 14 | 0,000414 | 0,143281 | 0,714524 | 0,142195 | 0,000412 | 0,049149 | 0,020292 | 1 |
> | 7 | 15 | 0,000498 | 0,018144 | 0,672926 | 0,308930 | 0,000463 | 0,049149 | 0,021507 | 1 |
> | 7 | 16 | 0,053096 | 0,020113 | 0,671599 | 0,308288 | 0,000460 | 0,049144 | 0,021444 | 1 |
> | 7 | 17 | 0,838484 | 0,074950 | 0,660290 | 0,264760 | 0,000406 | 0,049065 | 0,020161 | 1 |
> | 7 | 18 | 0,009412 | 0,180852 | 0,726675 | 0,092474 | 0,000412 | 0,049148 | 0,020287 | 1 |
> | 7 | 19 | 0,122800 | 0,169515 | 0,727847 | 0,102638 | 0,000416 | 0,049161 | 0,020390 | 1 |
> | 7 | 20 | 3,767651 | 0,101344 | 0,558902 | 0,339754 | 0,000329 | 0,048772 | 0,018148 | 1 |
>
> **Figure (pp. 59-63)** — Per ciascuno dei cinque valori di $\varepsilon$ ($1$, $0.1$, $0.01$, $0.001$, $0.0001$) sono riportati due grafici a dispersione RP vs. SQMP: una vista d'insieme (con i 9 punti della frontiera di Markowitz) e uno zoom sui portafogli PSO relativi allo scenario 7. Al diminuire di $\varepsilon$ la penalizzazione delle violazioni dei vincoli diventa più stringente; tuttavia per $\varepsilon$ troppo piccolo (0.0001) l'algoritmo fatica a bilanciare la minimizzazione della varianza con il rispetto dei vincoli (si vedano i valori di *Fitness* molto elevati nella tabella corrispondente), mentre per $\varepsilon = 0.001$ la "nuvola" di portafogli PSO appare più concentrata attorno alla soluzione ottima alla Markowitz rispetto alle "nuvole" ottenute con gli altri valori di $\varepsilon$.

*(slide 53–63)*

## Esperimento 2 — L'inizializzazione

> [!example] Esempio
> Inizializzazione: $\boldsymbol{x}^i = [1,0,0]^T$ per tutte le particelle (tutto il capitale investito nel Titolo 1). Tutti gli scenari.
>
> **Figura (p. 65)** — Grafico a dispersione "Sull'inizializzazione": frontiera di Markowitz (linea blu con rombi) e portafogli PSO per ciascuno dei 9 scenari (S=1,...,9, marcatori colorati diversi). I punti PSO si concentrano in una fascia orizzontale con RP compreso circa tra 0,044 e 0,047, ben al di sotto della maggior parte dei punti della frontiera efficiente, con SQMP compreso tra circa 0,010 e 0,030.
>
> I portafogli selezionati **non** si dispongono particolarmente vicino alla frontiera, questo a causa di:
> - la lentezza della convergenza della PSO verso la soluzione ottima;
> - la "cattiva" inizializzazione della posizione iniziale (identica per tutte le particelle).

*(slide 64–66)*

## Esperimenti 3, 4, 5 e 6 — Il numero di particelle N

> [!example] Esempio
> $N = 15,\ 20,\ 25 \text{ e } 30$. Tutti gli scenari. All'aumentare di $N$ la "nuvola" di punti risulta più "addensata" intorno alla soluzione ottima alla Markowitz.
>
> **Figure (pp. 68-71)** — Quattro grafici "Fitness vs. Iterazioni" (0-8000+ iterazioni) relativi allo scenario 7, che confrontano l'andamento della funzione di fitness di tre simulazioni (Sim.1, Sim.2, Sim.3) con il valore di riferimento Markowitz (fitness pressoché nulla, linea piatta), per ciascun valore di $N$:
> - **N = 15 particelle** (scala fitness 0-1,20): le tre simulazioni convergono a valori di fitness finali relativamente elevati, rispettivamente circa 0,88 (Sim.1), 0,38 (Sim.2) e 0,10 (Sim.3);
> - **N = 20 particelle** (scala 0-0,25): i valori finali scendono a circa 0,157 (Sim.1), 0,0 (Sim.2) e 0,182 (Sim.3);
> - **N = 25 particelle** (scala 0-0,25): valori finali attorno a 0,014 (Sim.1), 0,0 (Sim.2) e 0,0 (Sim.3), con una discesa tardiva (attorno alla 4300ª iterazione) per Sim.3;
> - **N = 30 particelle** (scala 0-0,18): tutte e tre le simulazioni convergono rapidamente (entro le prime 3000 iterazioni) verso valori di fitness prossimi allo zero.
>
> La conclusione è che l'aumento del numero di particelle migliora sia la velocità sia la qualità della convergenza della PSO verso la soluzione ottima.

*(slide 67–71)*

## Esperimento 7 — Analisi dei portafogli selezionati dalla PSO

> [!example] Esempio
> $N = 15,\ 20,\ 25 \text{ e } 30$. Tutti gli scenari.
>
> **Scenario 1** — confronto tra soluzione esatta alla Markowitz (x1=0,610106; x2=-0,129612; x3=0,519506; VP=0,000366; RP=0,046492; SQMP=0,019122) e 20 simulazioni PSO:
>
> | S | Sim. | Fitness | x1PSO | x2PSO | x3PSO | VPSO | RPSO | SQMPSO | Som. |
> |---|---|---|---|---|---|---|---|---|---|
> | 1 | 1 | 0,414272 | 0,542729 | 0,003694 | 0,453576 | 0,000250 | 0,046906 | 0,015808 | 1,000000 |
> | 1 | 2 | 0,351631 | 0,685007 | 0,027411 | 0,287581 | 0,000310 | 0,046843 | 0,017601 | 1,000000 |
> | 1 | 3 | 0,026735 | 0,974321 | 0,001255 | 0,024424 | 0,000699 | 0,046518 | 0,026435 | 1,000000 |
> | 1 | 4 | 0,195861 | 0,672274 | -0,035410 | 0,363137 | 0,000328 | 0,046687 | 0,018114 | 1,000000 |
> | 1 | 5 | 0,021258 | 0,726821 | -0,082967 | 0,356146 | 0,000395 | 0,046513 | 0,019877 | 1,000000 |
> | 1 | 6 | 0,147434 | 0,656896 | -0,058736 | 0,401840 | 0,000332 | 0,046639 | 0,018227 | 1,000000 |
> | 1 | 7 | 0,217737 | 0,671717 | -0,027366 | 0,355649 | 0,000324 | 0,046709 | 0,017987 | 1,000000 |
> | 1 | 8 | 0,517233 | 0,443451 | 0,009415 | 0,547135 | 0,000244 | 0,047009 | 0,015619 | 1,000000 |
> | 1 | 9 | 0,239331 | 0,631931 | -0,032464 | 0,400533 | 0,000303 | 0,046731 | 0,017407 | 1,000000 |
> | 1 | 10 | 0,000404 | 0,717963 | -0,093761 | 0,375798 | 0,000395 | 0,046492 | 0,019873 | 1,000000 |
> | 1 | 11 | 0,000471 | 0,721636 | -0,092508 | 0,370872 | 0,000397 | 0,046492 | 0,019923 | 1,000000 |
> | 1 | 12 | 0,023920 | 0,597181 | -0,125047 | 0,527867 | 0,000358 | 0,046515 | 0,018922 | 1,000000 |
> | 1 | 13 | 0,001043 | 0,870385 | -0,042897 | 0,172512 | 0,000536 | 0,046492 | 0,023152 | 1,000000 |
> | 1 | 14 | 0,530056 | 0,552512 | 0,050498 | 0,396989 | 0,000228 | 0,047022 | 0,015105 | 1,000000 |
> | 1 | 15 | 0,479967 | 0,502259 | 0,014952 | 0,482789 | 0,000237 | 0,046971 | 0,015410 | 1,000000 |
> | 1 | 16 | 0,178834 | 0,689399 | -0,036125 | 0,346727 | 0,000340 | 0,046670 | 0,018447 | 1,000000 |
> | 1 | 17 | 0,417357 | 0,544996 | 0,005608 | 0,449396 | 0,000249 | 0,046909 | 0,015787 | 1,000000 |
> | 1 | 18 | 0,392207 | 0,610604 | 0,017954 | 0,371442 | 0,000266 | 0,046884 | 0,016312 | 1,000000 |
> | 1 | 19 | 0,583741 | 0,618846 | 0,092733 | 0,288421 | 0,000244 | 0,047075 | 0,015636 | 1,000000 |
> | 1 | 20 | 0,163386 | 0,951528 | 0,045085 | 0,003387 | 0,000657 | 0,046654 | 0,025633 | 1,000000 |
>
> **Figura (p. 75)** — Grafico a dispersione "30 particelle": frontiera di Markowitz e portafogli PSO per i 9 scenari (S=1,...,9). A differenza dell'Esperimento 2, con $N=30$ e inizializzazione casuale normalizzata i punti PSO relativi a ciascuno scenario si addensano molto vicino al corrispondente punto della frontiera di Markowitz.
>
> **Rispetto dei vincoli** (percentuali su 20 simulazioni per scenario):
>
> | Scen. | N° di sim. | x'(PSO)1 = 1 | x'(PSO)R = RP |
> |---|---|---|---|
> | 1 | 20 | 100% | 15% |
> | 2 | 20 | 100% | 70% |
> | 3 | 20 | 100% | 60% |
> | 4 | 20 | 100% | 70% |
> | 5 | 20 | 100% | 90% |
> | 6 | 20 | 100% | 60% |
> | 7 | 20 | 100% | 30% |
> | 8 | 20 | 100% | 50% |
> | 9 | 20 | 100% | 0% |
>
> Il vincolo di budget $\boldsymbol{x}'_{(PSO)}\boldsymbol{e} = 1$ è sempre soddisfatto esattamente (100% delle simulazioni per ogni scenario); il vincolo sul rendimento atteso $\boldsymbol{x}'_{(PSO)}\boldsymbol{r} = R_P$ è invece soddisfatto solo in una percentuale variabile di simulazioni, dallo 0% (scenario 9) al 90% (scenario 5).
>
> **Ottimizzazione della funzione obiettivo** (Fitness, VP e Fitness-VP, quest'ultima interpretabile come la quota di fitness dovuta alla penalizzazione dei vincoli):
>
> *Scenario 1:*
>
> | S | Sim. | Fitness | VP | Fitness-VP |
> |---|---|---|---|---|
> | 1 | 1 | 0,414272 | 0,000366 | 0,413906 |
> | 1 | 2 | 0,351631 | 0,000366 | 0,351265 |
> | 1 | 3 | 0,026735 | 0,000366 | 0,026369 |
> | 1 | 4 | 0,195861 | 0,000366 | 0,195495 |
> | 1 | 5 | 0,021258 | 0,000366 | 0,020892 |
> | 1 | 6 | 0,147434 | 0,000366 | 0,147068 |
> | 1 | 7 | 0,217737 | 0,000366 | 0,217372 |
> | 1 | 8 | 0,517233 | 0,000366 | 0,516867 |
> | 1 | 9 | 0,239331 | 0,000366 | 0,238965 |
> | 1 | 10 | 0,000404 | 0,000366 | 0,000038 |
> | 1 | 11 | 0,000471 | 0,000366 | 0,000105 |
> | 1 | 12 | 0,023920 | 0,000366 | 0,023554 |
> | 1 | 13 | 0,001043 | 0,000366 | 0,000677 |
> | 1 | 14 | 0,530056 | 0,000366 | 0,529690 |
> | 1 | 15 | 0,479967 | 0,000366 | 0,479602 |
> | 1 | 16 | 0,178834 | 0,000366 | 0,178468 |
> | 1 | 17 | 0,417357 | 0,000366 | 0,416991 |
> | 1 | 18 | 0,392207 | 0,000366 | 0,391841 |
> | 1 | 19 | 0,583741 | 0,000366 | 0,583375 |
> | 1 | 20 | 0,163386 | 0,000366 | 0,163020 |
>
> *Scenario 2:*
>
> | S | Sim. | Fitness | VP | Fitness-VP |
> |---|---|---|---|---|
> | 2 | 1 | 0,001178 | 0,000243 | 0,000935 |
> | 2 | 2 | 0,039899 | 0,000243 | 0,039655 |
> | 2 | 3 | 0,002380 | 0,000243 | 0,002136 |
> | 2 | 4 | 0,000244 | 0,000243 | 0,000000 |
> | 2 | 5 | 0,030919 | 0,000243 | 0,030676 |
> | 2 | 6 | 0,000244 | 0,000243 | 0,000000 |
> | 2 | 7 | 0,000244 | 0,000243 | 0,000000 |
> | 2 | 8 | 0,000303 | 0,000243 | 0,000059 |
> | 2 | 9 | 0,000270 | 0,000243 | 0,000027 |
> | 2 | 10 | 0,000518 | 0,000243 | 0,000274 |
> | 2 | 11 | 0,000659 | 0,000243 | 0,000415 |
> | 2 | 12 | 0,013086 | 0,000243 | 0,012843 |
> | 2 | 13 | 0,000346 | 0,000243 | 0,000103 |
> | 2 | 14 | 0,000286 | 0,000243 | 0,000043 |
> | 2 | 15 | 0,000284 | 0,000243 | 0,000041 |
> | 2 | 16 | 0,047081 | 0,000243 | 0,046837 |
> | 2 | 17 | 0,000385 | 0,000243 | 0,000142 |
> | 2 | 18 | 0,003999 | 0,000243 | 0,003755 |
> | 2 | 19 | 0,000320 | 0,000243 | 0,000077 |
> | 2 | 20 | 0,000400 | 0,000243 | 0,000156 |
>
> Nello scenario 2, per le simulazioni 4, 6 e 7 la quantità Fitness-VP è pari a 0,000000: la particella ha quindi rispettato (quasi) esattamente entrambi i vincoli, tanto che il valore di fitness coincide praticamente con la sola varianza del portafoglio VP.
>
> **Figura (p. 79)** — "Frontiera (dei portafogli efficienti ed inefficienti) di PSO": sovrapposizione tra la frontiera di Markowitz (blu) e la frontiera costruita usando, per ogni scenario, il portafoglio PSO con il valore minimo di fitness (rossa). Le due curve risultano pressoché sovrapposte lungo tutto il range di SQMP (0,010-0,030) e RP (0,047-0,0505), a conferma che, prendendo il miglior risultato su 20 simulazioni per scenario, la PSO riproduce fedelmente la frontiera efficiente esatta.

*(slide 72–79)*

## Variante del problema: vincolo di disuguaglianza sul rendimento

> [!example] Esempio
> Si considera una variante del problema in cui il vincolo sul rendimento è espresso come disuguaglianza:
> $$\boldsymbol{x}_{(PSO)}'\boldsymbol{R} \ge R_P$$
>
> con corrispondente funzione di fitness
> $$\boldsymbol{x}_{(PSO)}'\boldsymbol{V}\boldsymbol{x}_{(PSO)} + \frac{1}{\varepsilon}\left|\boldsymbol{x}_{(PSO)}'\boldsymbol{1} - 1\right| + \frac{1}{\varepsilon}\left|\max(0,\ R_P - \boldsymbol{x}_{(PSO)}'\boldsymbol{R})\right|.$$
>
> $N = 30$. Tutti gli scenari.
>
> **Figura (p. 81)** — Grafico a dispersione "Vincolo di disuguaglianza": frontiera di Markowitz e portafogli PSO per i 9 scenari. Rispetto al caso con vincolo di uguaglianza (Esperimento 7), i punti PSO si addensano in modo ancora più marcato lungo la frontiera di Markowitz, in particolare per gli scenari a rendimento intermedio (S=3,...,7): rilassare il vincolo sul rendimento da uguaglianza a disuguaglianza rende più agevole per la PSO individuare portafogli vicini alla frontiera efficiente, poiché la particella può eccedere liberamente il rendimento minimo richiesto senza essere penalizzata per questo.

*(slide 80–81)*
