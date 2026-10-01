---
title: "Arbitrage Pricing Theory (APT)"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-05_APT.pdf"
pages: 42
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione all'Arbitrage Pricing Theory

**Corso:** Economia dei mercati ed investimenti finanziari (EM5002) — Stefano Colonnello, Università Ca' Foscari Venezia. Argomento: **APT** (Arbitrage Pricing Theory).

- La Arbitrage Pricing Theory (APT) è stata sviluppata da **Stephen Ross (1976)**. La teoria inizia con un'analisi di come vengono costruiti portafogli efficienti.
- Viene proposta una nuova interpretazione dei prezzi dei titoli: si afferma che il rendimento di qualsiasi titolo rischioso è una **combinazione lineare di diversi fattori macroeconomici** (non specificati dalla teoria).
- In modo analogo al CAPM, si assume che gli investitori siano completamente diversificati e che il rischio sistematico sia la forza rilevante nel lungo periodo.
- A differenza del CAPM, l'APT specifica una relazione lineare **multipla** tra rendimenti e diversi fattori di rischio, per cui un portafoglio può avere diversi gradi di sensibilità ai vari fattori.

*(slide 1–2)*

## APT vs. CAPM: motivazioni, ipotesi e differenze concettuali

**Perché una teoria alternativa al CAPM**

- Il CAPM è criticato per la difficoltà nel selezionare una proxy per il portafoglio di mercato.
- È stata quindi sviluppata una teoria alternativa con meno ipotesi: l'APT afferma che i rendimenti sono determinati da più fattori distinti.
- Chen, Roll e Ross (1986), ad esempio, mostrano che il rendimento di lungo periodo di un titolo dipende da variazioni in:
  - Inflazione
  - Produzione industriale
  - Pendenza della struttura a termine dei tassi di interesse

**Fondamento: equilibrio vs. assenza di arbitraggio**

- Il CAPM si basa su condizioni di equilibrio:
  - Massimizzazione dell'utilità
  - Domanda = Offerta
- L'APT, invece, non richiede condizioni di equilibrio, ma solo l'assenza di arbitraggio, il cosiddetto **principio di non arbitraggio**.

**Cosa l'APT non richiede e non implica**

L'APT *non richiede*:
- Paradigma media-varianza
- Condizioni di equilibrio (a livello di mercato e individuale)

L'APT *non implica*:
- Che il portafoglio di mercato contenente tutti i titoli rischiosi sia il portafoglio efficiente in senso media-varianza

*(slide 3–5)*

## Le ipotesi dell'APT

> [!abstract] Definizione
> L'APT poggia sulle seguenti ipotesi:
>
> - I rendimenti dei titoli sono coerenti con una **struttura lineare dei fattori** e possono essere descritti da un **modello fattoriale**.
> - Non esistono **opportunità di arbitraggio** nei mercati finanziari.
> - Il numero di titoli è molto elevato, tale da permettere l'applicazione della **legge dei grandi numeri** e la costruzione di portafogli che **diversificano il rischio specifico**.
> - I **fattori** sono osservabili o stimabili dagli investitori (Wei, 1988).

*(slide 6)*

## Arbitraggio e legge del prezzo unico

> [!abstract] Definizione
> - Si ha un'opportunità di **arbitraggio** quando è possibile ottenere un profitto certo senza sostenere un investimento netto.
> - Un esempio semplice si verifica quando lo stesso titolo è scambiato a prezzi diversi su mercati differenti.
> - La **legge del prezzo unico** afferma che due titoli equivalenti sotto ogni aspetto economicamente rilevante devono avere lo stesso prezzo.
> - Tale legge è garantita dagli arbitraggisti: in presenza di violazioni, si acquista il titolo sottovalutato e si vende quello sopravvalutato fino all'eliminazione dell'opportunità.

*(slide 7)*

## Modello fattoriale a un fattore per portafogli ben diversificati

> [!abstract] Definizione
> **Modello a un fattore**
>
> Si consideri un modello a un fattore con fattore macroeconomico centrato $\tilde f$ (cioè $E(\tilde f) = 0$) per un portafoglio $p$:
>
> $$r_p^e = \underbrace{E(r_p^e)}_{=\alpha_p + \beta_p \mu_f} + \beta_p \tilde f + e_p$$
>
> dove
> $$r_p^e = \sum_{i=1}^{N} w_i r_i^e, \qquad \alpha_p = \sum_{i=1}^{N} w_i \alpha_i, \qquad \beta_p = \sum_{i=1}^{N} w_i \beta_i, \qquad e_p = \sum_{i=1}^{N} w_i e_i, \qquad \tilde f = f - \mu_f$$
>
> - $\mu_f$ rappresenta la media del fattore non centrato $f$. Se il fattore è espresso come rendimento in eccesso, $\mu_f$ rappresenta il **premio per il rischio del fattore**, indicato con $\lambda_f$.
> - Il termine costante rappresenta il **rendimento atteso in eccesso** del portafoglio.
>
> **Rischio diversificabile e non diversificabile**
>
> - Per costruzione si ha $E(e_p) = 0$ e, per un portafoglio ben diversificato ($w_i \approx 0\ \forall i$ quando $N \to \infty$), si ha $\sigma_{e_p}^2 \to 0$ (si veda la lezione sui modelli fattoriali).
> - Quindi, per un portafoglio ben diversificato, si ottiene
>
> $$r_p^e = E(r_p^e) + \beta_p \tilde f$$
>
> **Esempio grafico: portafoglio ben diversificato vs. singolo titolo**
>
> Si considerino i rendimenti in eccesso realizzati di un portafoglio ben diversificato $A$ (riquadro A) e di un singolo titolo $S$ (riquadro B) rispetto alle realizzazioni del fattore macroeconomico $\tilde f$.
>
> **Figura (pag. 10)** — Due scatterplot "Excess return (%)" vs $\tilde f$: nel riquadro A (portafoglio ben diversificato $A$) i punti giacciono quasi esattamente su una retta con intercetta 10%; nel riquadro B (singolo titolo $S$) i punti sono dispersi attorno a una retta con la stessa pendenza. La figura mostra che la diversificazione elimina il rischio idiosincratico ($e_p \to 0$), lasciando solo la relazione lineare col fattore.
>
> Assumendo $\beta_A = 1$, si ha
>
> $$r_A^e = \underbrace{E(r_A^e)}_{=10\%} + \underbrace{1{,}0}_{\text{Pendenza}} \times \tilde f$$
>
> Un portafoglio con un beta più basso presenterebbe una retta più piatta, quindi più stabile intorno a $E(r_p^e)$ e, di conseguenza, un premio per il rischio inferiore.

*(slide 8–10)*

## Condizione di non arbitraggio: esempio con due portafogli a beta uguale

> [!example] Esempio
> - Fin qui è stato specificato soltanto un modello fattoriale per un portafoglio ben diversificato. Si consideri ora il secondo elemento fondamentale dell'APT: la **condizione di non arbitraggio**.
> - Domanda: i portafogli $A$ e $B$ possono coesistere con lo stesso beta fattoriale ma premi per il rischio differenti (cioè rendimenti attesi in eccesso differenti)?
>
> **Figura (pag. 11)** — Grafico "Excess return (%)" vs $\tilde f$ con due rette parallele (stesso beta = pendenza), $A$ con intercetta 10 e $B$ con intercetta 8. Mostra due portafogli con identica sensibilità al fattore ma premio per il rischio diverso: una situazione che, come si dimostra di seguito, non può sussistere in equilibrio senza generare arbitraggio.
>
> **Strategia di arbitraggio**
>
> $$(0{,}10 + 1{,}0 \times \tilde f) \times \$1\text{ milione} \quad \text{da una posizione lunga in } A$$
> $$-(0{,}08 + 1{,}0 \times \tilde f) \times \$1\text{ milione} \quad \text{da una posizione corta in } B$$
> $$\overline{0{,}02 \times \$1\text{ milione} = \$20.000} \quad \text{provento netto}$$
>
> La componente casuale ($1{,}0 \times \tilde f$) si cancella tra posizione lunga e corta, lasciando un profitto certo di $20.000 senza investimento netto: è un'opportunità di arbitraggio, che non può sussistere in equilibrio.

*(slide 11–12)*

## Premi per il rischio e beta: relazione di proporzionalità

> [!example] Esempio
> - Si vogliono ricavare implicazioni sui premi per il rischio dall'APT: si consideri la relazione tra rendimenti attesi ($= r_f + $ premio per il rischio) e beta fattoriali.
> - Che cosa implica l'APT per portafogli con beta differenti? **I premi per il rischio devono essere proporzionali ai beta.**
>
> **Esempio numerico**
>
> - Il tasso privo di rischio è $r_f = 4\%$.
> - Il portafoglio $C$, con beta pari a 0.7 e rendimento atteso pari a 11%, si trova al di sotto della retta che unisce il portafoglio $A$ e $r_f$.
> - Si consideri un portafoglio $D$, con peso del 70% in $A$ e del 30% in $r_f$:
>   - Ha lo stesso beta di $C$, ma un rendimento atteso più elevato.
>   - Opportunità di arbitraggio: posizione corta in $C$, acquisto di $0{,}3 r_f + 0{,}7A$.
> - Sotto la condizione di non arbitraggio, tutti i portafogli ben diversificati devono trovarsi sulla retta blu.
>
> **Figura (pag. 14)** — Grafico "Expected Return (%)" vs $\beta$: retta blu che parte da $r_f=4$ e passa per $A$ (beta 1, rendimento 14), con il punto $C$ (beta 0.7, rendimento 11) sotto la retta e il punto $D$ (stesso beta di $C$, ma sulla retta, rendimento 10 nel disegno) sopra $C$; l'area tra $C$ e $D$ è etichettata "Risk Premium". Mostra che $C$ è sottoprezzato rispetto alla retta di non arbitraggio: comprando $D=0{,}3r_f+0{,}7A$ e vendendo $C$ si ottiene un profitto senza rischio.

*(slide 13–14)*

## Derivazione della SML dall'APT (modello a un fattore)

> [!note] Dimostrazione
> **Obiettivo:** ottenere la consueta Security Market Line (SML) a partire dall'APT.
>
> Si consideri il modello generale a un fattore:
>
> $$r_p^e = \underbrace{E(r_p^e)}_{=\alpha_p + \beta_p \mu_f} + \beta_p \tilde f + e_p \quad \Rightarrow \quad E(r_p^e) = \alpha_p + \beta_p \mu_f$$
>
> Si specifichi il fattore macroeconomico $f$ (non centrato) come $r_m^e$, cioè il **rendimento di mercato in eccesso**, ossia un fattore *traded* e non centrato:
>
> $$\mu_f = E(r_m^e) = E(r_m - r_f)$$
>
> Si ottiene allora:
>
> $$E(r_p^e) = \alpha_p + \beta_p E(r_m^e)$$
>
> Imponendo la **condizione di non arbitraggio**, si ha $\alpha_p = 0$ per i portafogli ben diversificati. Si ottiene quindi una SML per tali portafogli:
>
> $$E(r_p^e) = \beta_p E(r_m^e) \qquad \text{oppure} \qquad E(r_p) = r_f + \beta_p E(r_m - r_f)$$
>
> **Figura (pag. 16)** — Grafico "Expected Return (%)" vs $\beta$: retta che parte da $r_f$ e passa per il punto $m$ (portafoglio di mercato, $\beta=1$, rendimento $E(r_m)$), con la differenza $E(r_p)-r_f$ indicata come segmento verticale. Illustra la SML standard, qui derivata senza le ipotesi di equilibrio del CAPM.
>
> **Conclusioni della derivazione**
>
> - Si è ottenuta una relazione SML equivalente a quella del CAPM, ma **senza le ipotesi restrittive del CAPM**.
> - Questa derivazione dipende da tre ipotesi:
>   1. Un modello fattoriale che descriva i rendimenti dei titoli.
>   2. Un numero sufficiente di titoli per formare portafogli ben diversificati.
>   3. L'assenza di opportunità di arbitraggio.
> - Nonostante le sue ipotesi restrittive, la conclusione principale del CAPM, cioè la relazione SML tra rendimento atteso e beta, dovrebbe essere almeno approssimativamente valida.
> - A differenza del CAPM, l'APT non richiede che il portafoglio di riferimento nella SML sia il vero portafoglio di mercato. **Qualsiasi portafoglio ben diversificato che giaccia sulla SML** può fungere da portafoglio di riferimento.

*(slide 15–17)*

## APT e titoli individuali: limiti di applicabilità

- L'APT si applica ai **portafogli ben diversificati** e non necessariamente ai singoli titoli.
- Se, per esempio, un solo titolo viola la relazione tra rendimento atteso e beta, l'effetto di tale violazione su un portafoglio ben diversificato sarà troppo piccolo per avere rilevanza pratica e non emergeranno opportunità di arbitraggio significative.
- Con l'APT è quindi possibile che alcuni singoli titoli siano prezzati erroneamente (**mispricing**), cioè non si trovino sulla SML.
- Se però **molti** titoli violano la relazione tra rendimento atteso e beta, allora tale relazione non varrà più per i portafogli ben diversificati ed emergeranno opportunità di arbitraggio.
- Di conseguenza, la relazione tra rendimento atteso e beta vale per tutti i titoli, salvo eventualmente per un numero limitato di essi.

*(slide 18)*

## APT vs. CAPM: confronto sintetico e problema del portafoglio di mercato

**Confronto APT / CAPM**

| APT | CAPM |
|---|---|
| L'equilibrio coincide con l'assenza di opportunità di arbitraggio | Il modello si basa su un portafoglio di "mercato" intrinsecamente non osservabile |
| L'equilibrio dell'APT viene ripristinato rapidamente anche se solo pochi investitori riconoscono un'opportunità di arbitraggio | Si fonda sull'efficienza media-varianza |
| La relazione tra rendimento atteso e beta può essere derivata senza utilizzare il vero portafoglio di mercato | Le azioni di molti piccoli investitori ristabiliscono l'equilibrio del CAPM |
| | Il CAPM descrive l'equilibrio per tutti i titoli |

**Il problema del portafoglio di mercato**

- Il portafoglio di mercato del CAPM è difficile da costruire:
  - In teoria dovrebbero esservi inclusi tutti i titoli e tutte le attività (immobili, oro, ecc.).
  - In pratica si utilizza una proxy, come per esempio l'indice S&P 500.
- L'APT richiede invece la specificazione dei **fattori macroeconomici rilevanti**.

*(slide 19–20)*

## APT multifattoriale

> [!abstract] Definizione
> - L'APT può essere estesa a **modelli multifattoriali**.
> - Esempio: in un'economia a due fattori, il rendimento atteso di un titolo è dato dalla somma di:
>   1. Il tasso privo di rischio.
>   2. La sensibilità al rischio del PIL (beta del PIL) moltiplicata per il premio per il rischio del PIL ($\lambda_{GDP}$).
>   3. La sensibilità al rischio di tasso di interesse (beta del tasso di interesse) moltiplicata per il relativo premio per il rischio ($\lambda_{IR}$).
>
> $$E(r_i) = r_f + \beta_i^{GDP} RP_{GDP} + \beta_i^{IR} RP_{IR}$$
>
> - Si pensi alla dispersione sezionale di $\beta_i^{GDP}$ e $\beta_i^{IR}$ (per esempio beni durevoli vs. non durevoli, finanziari vs. non finanziari, utilities vs. altri settori).
> - Si generalizzi ora la SML ottenuta in precedenza a $K$ fattori.

*(slide 21)*

## Portafogli di replicazione in un modello a K fattori

> [!abstract] Definizione
> **Definizione e applicazioni**
>
> - In un modello con $K$ fattori, il **portafoglio di replicazione** di un dato titolo/portafoglio è un portafoglio che presenta la stessa sensibilità ($\beta$) rispetto a ciascuno dei $K$ fattori.
> - Applicazioni:
>   - Copertura e posizioni di arbitraggio per banche d'investimento.
>   - Copertura dei rischi a livello d'impresa.
>   - Stima del costo del capitale (tramite l'APT).
> - In un modello con $K$ fattori è in generale possibile trovare un portafoglio composto da $K+1$ asset che "replica qualsiasi insieme di $K$ beta".
> - Perché $K+1$ asset?
>   - $K$ asset per replicare i beta.
>   - 1 asset per imporre che i pesi del portafoglio sommino a 1.
>
> **Rappresentazione a K fattori**
>
> La rappresentazione a $K$ fattori del rendimento in eccesso di un portafoglio è
>
> $$r_p^e = E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \tilde f_k + e_p$$
>
> dove
> - $r_p^e$: rendimento in eccesso realizzato del portafoglio $p$
> - $E(r_p^e)$: rendimento in eccesso atteso (premio per il rischio)
> - $\beta_{kp}$: esposizione di $p$ al fattore $k$
> - $\tilde f_k$: innovazione del fattore $k$
> - $e_p$: componente idiosincratica (diversificabile)
>
> I fattori sono centrati: $E(\tilde f_k) = 0\ \forall k$.
>
> Se il portafoglio è ben diversificato, allora $e_p \approx 0$ e quindi
>
> $$r_p^e = E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \tilde f_k$$

*(slide 22–23)*

## Costruzione del portafoglio di replicazione e passaggio all'arbitraggio

> [!note] Dimostrazione
> **Passo 1 — Sostituzione dei fattori traded**
>
> Si parta dalla rappresentazione fattoriale (con $p$ ben diversificato):
>
> $$r_p^e = E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \tilde f_k$$
>
> Se i fattori sono *traded* (oppure costruiti come portafogli mimicking):
>
> $$\tilde f_k = r_k^e - E(r_k^e)$$
>
> Si sostituisce:
>
> $$r_p^e = E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \left(r_k^e - E(r_k^e)\right)$$
>
> **Passo 2 — Componente fissa e componente casuale**
>
> Riordinando:
>
> $$r_p^e = \underbrace{E(r_p^e) - \sum_{k=1}^{K} \beta_{kp} E(r_k^e)}_{\text{Componente fissa}} + \underbrace{\sum_{k=1}^{K} \beta_{kp} r_k^e}_{\text{Componente casuale}}$$
>
> Interpretazione:
> - Primo termine: costante (non casuale).
> - Secondo termine: portafoglio di rendimenti dei fattori (traded) — il **portafoglio di replicazione** — in cui ciascun fattore $k$ ha peso $\beta_{kp}$.
>
> Per avere pesi che sommano a uno nel portafoglio replicante, è necessario investire $1 - \sum_{k=1}^{K} \beta_{kp}$ nel titolo privo di rischio.
>
> **Passaggio chiave — dall'uguaglianza delle componenti casuali all'arbitraggio**
>
> - Finora si è costruito un portafoglio di rendimenti dei fattori tale che:
>   - La componente casuale di $r_p^e$ è esattamente replicata.
>   - Solo la componente fissa può differire.
> - Se le componenti fisse differiscono:
>   - Si assume una posizione lunga nel portafoglio con rendimento fisso più elevato.
>   - Si assume una posizione corta nel portafoglio con rendimento fisso più basso.
>   - Le componenti casuali si annullano esattamente.
>   - $\Rightarrow$ **Opportunità di arbitraggio**.

*(slide 24–26)*

## Definizione formale di strategia di arbitraggio

> [!abstract] Definizione
> Una **strategia di arbitraggio** soddisfa le seguenti condizioni:
>
> 1. Investimento netto nullo:
> $$\sum_{i=1}^{N} w_i = 0$$
>
> 2. Rischio nullo (nessuna esposizione ai fattori; il rischio idiosincratico è diversificato):
> $$\sum_{i=1}^{N} w_i \beta_{ki} = 0 \quad \forall k$$
>
> 3. Payoff atteso positivo:
> $$E\left(\sum_{i=1}^{N} w_i r_i^e\right) > 0$$

*(slide 27)*

## SML multifattoriale dalla condizione di non arbitraggio

> [!note] Dimostrazione
> Per escludere arbitraggi, le componenti fisse del portafoglio $p$ e del suo portafoglio replicante devono essere uguali:
>
> $$E(r_p) - \sum_{k=1}^{K} \beta_{kp} E(r_k) = \left(1 - \sum_{k=1}^{K} \beta_{kp}\right) r_f$$
>
> In termini di rendimento in eccesso:
>
> $$E(r_p^e) - \sum_{k=1}^{K} \beta_{kp} E(r_k^e) = 0$$
>
> Riordinando, si ottiene la **SML multifattoriale**:
>
> $$E(r_p^e) = \sum_{k=1}^{K} \beta_{kp} \underbrace{E(r_k^e)}_{\lambda_k}$$
>
> Interpretazione:
> - Il rendimento atteso in eccesso è una combinazione lineare dei premi per il rischio dei fattori.
> - $\lambda_k$ sono i **prezzi del rischio** dei fattori.
>
> Equivalentemente, si ottiene la SML in termini di rendimenti totali:
>
> $$E(r_p) = r_f + \sum_{k=1}^{K} \beta_{kp} \underbrace{\left[E(r_k) - r_f\right]}_{\lambda_k}$$

*(slide 28–29)*

## Portafogli fattoriali

> [!abstract] Definizione
> Un **portafoglio fattoriale** per il fattore $k$ è definito da:
> - Esposizione unitaria al fattore $k$.
> - Esposizione nulla a tutti gli altri fattori.
>
> Il suo rendimento soddisfa:
>
> $$r_k^e = E(r_k^e) + \tilde f_k + e_k$$
>
> Per portafogli fattoriali ben diversificati, $e_k \approx 0$. Quindi:
>
> $$r_k^e = E(r_k^e) + \tilde f_k$$
>
> Il **prezzo del rischio fattoriale** (premio per il rischio del fattore) è:
>
> $$\lambda_k = E(r_k^e)$$

*(slide 30)*

## Dai fattori traded ai portafogli di replicazione con asset esistenti

- La derivazione precedente utilizza i rendimenti dei fattori come se fossero portafogli traded. Tuttavia, questo non è necessario:
  - I fattori non devono essere necessariamente traded.
  - Possiamo costruire portafogli di titoli/portafogli esistenti che replicano le esposizioni ai fattori.
- In un modello a $K$ fattori:
  - $K+1$ asset sono sufficienti per generare tutti i rischi fattoriali.
  - Tali asset possono essere combinati per costruire portafogli che replicano i fattori.
- Implicazione: qualsiasi portafoglio ben diversificato può essere replicato usando:
  - Portafogli costruiti a partire da asset esistenti.
  - Senza bisogno che i fattori siano traded.
- $\Rightarrow$ Si passa ora alla costruzione esplicita di un portafoglio di replicazione (esempi numerici seguenti).

*(slide 31)*

## Esempio numerico: premi per il rischio dei portafogli fattoriali

> [!example] Esempio
> Si considerino tre portafogli generati da un modello a due fattori:
>
> $$r_A = 0{,}08 + 2\tilde f_1 + 3\tilde f_2$$
> $$r_B = 0{,}10 + 3\tilde f_1 + 2\tilde f_2$$
> $$r_C = 0{,}10 + 3\tilde f_1 + 5\tilde f_2$$
>
> Si costruiscano portafogli fattoriali (esposizioni target: $(1,0)$ e $(0,1)$, con pesi che sommano a 1):
>
> $$\left\{2, \tfrac{1}{3}, -\tfrac{4}{3}\right\}, \qquad \left\{3, -\tfrac{2}{3}, -\tfrac{4}{3}\right\}$$
>
> Dato $r_f = 5\%$, si ha:
>
> $$E(r_1^e) = 0{,}06 - 0{,}05 = 0{,}01, \qquad E(r_2^e) = 0{,}04 - 0{,}05 = -0{,}01$$
>
> Quindi:
>
> $$\lambda_1 = 0{,}01, \qquad \lambda_2 = -0{,}01$$

*(slide 32)*

## Esempio numerico: costruzione di un portafoglio di replicazione

> [!example] Esempio
> Si considerino tre titoli con rendimenti descritti da una struttura a due fattori:
>
> $$r_A^e = 0{,}03 + 1\tilde f_1 - 4\tilde f_2 + e_A$$
> $$r_B^e = 0{,}05 + 3\tilde f_1 + 2\tilde f_2 + e_B$$
> $$r_C^e = 0{,}10 + 1.5\tilde f_1 + 0\tilde f_2 + e_C$$
>
> Si costruisca un portafoglio con esposizioni obiettivo: $\beta_1 = 2$, $\beta_2 = 1$.
>
> Indicando con $w_A, w_B, w_C$ i pesi, si ha il sistema:
>
> $$w_A + w_B + w_C = 1$$
> $$1w_A + 3w_B + 1.5w_C = 2$$
> $$-4w_A + 2w_B + 0w_C = 1$$
>
> **Soluzione:**
>
> $$w_A = -0{,}1, \qquad w_B = 0{,}3, \qquad w_C = 0{,}8$$

*(slide 33)*

## Riepilogo: l'equazione di pricing dell'APT

- Se due portafogli:
  - hanno identiche esposizioni fattoriali $\{\beta_{ki}\}$;
  - sono ben diversificati (assenza di rischio residuo);

  $\Rightarrow$ hanno lo stesso rischio e devono avere lo stesso rendimento atteso. In caso contrario, emerge un'opportunità di arbitraggio.

- Qualsiasi portafoglio $p$ può essere replicato:
  - investendo $\beta_{kp}$ nei portafogli fattoriali;
  - investendo $1 - \sum_{k=1}^{K} \beta_{kp}$ nell'attività priva di rischio.

**Equazione di pricing dell'APT**

$$E(r_i) = r_f + \sum_{k=1}^{K} \beta_{ki} \lambda_k$$

- Può essere collegata alla rappresentazione tramite fattore di sconto stocastico (si veda la sezione seguente).
- Può coesistere con il CAPM nello stesso mercato dei capitali (si veda la sezione seguente).
- Le dimostrazioni relative si trovano nell'appendice (pp. 35-42).

*(slide 34)*

## Appendice — APT e fattore di sconto stocastico (SDF)

> [!note] Dimostrazione
> **Impostazione**
>
> Si parta dalla condizione di pricing del fattore di sconto stocastico (SDF) per i rendimenti in eccesso:
>
> $$E(m\, r_p^e) = 0$$
>
> Si assuma che i rendimenti in eccesso seguano una rappresentazione a $K$ fattori:
>
> $$r_p^e = E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \tilde f_k$$
>
> Si assuma inoltre che l'SDF sia lineare negli stessi fattori centrati:
>
> $$m = a - \sum_{k=1}^{K} b_k \tilde f_k$$
>
> I fattori sono centrati, quindi $E(\tilde f_k) = 0\ \forall k$.
>
> **Obiettivo:** sostituire entrambe le espressioni nella condizione di pricing con SDF e derivare il vincolo imposto sui rendimenti attesi.
>
> **Sviluppo**
>
> Si sostituiscano le due rappresentazioni in $E(m\, r_p^e) = 0$:
>
> $$E\left[\left(a - \sum_{k=1}^{K} b_k \tilde f_k\right)\left(E(r_p^e) + \sum_{k=1}^{K} \beta_{kp} \tilde f_k\right)\right] = 0$$
>
> Si ottiene:
>
> $$E(m r_p^e) = a\,E(r_p^e) + a\,E\left(\sum_{j=1}^{K} \beta_{jp} \tilde f_j\right) - E\left(\sum_{k=1}^{K} b_k \tilde f_k\right) E(r_p^e) - E\left(\sum_{k=1}^{K}\sum_{j=1}^{K} b_k \beta_{jp} \tilde f_k \tilde f_j\right)$$
>
> Poiché i fattori sono centrati ($E(\tilde f_k)=0$), i due termini centrali si annullano. La condizione dell'SDF diventa:
>
> $$a\,E(r_p^e) - \sum_{k=1}^{K}\sum_{j=1}^{K} b_k \beta_{jp}\, E(\tilde f_k \tilde f_j) = 0$$
>
> Quindi:
>
> $$a\,E(r_p^e) = \sum_{k=1}^{K}\sum_{j=1}^{K} b_k \beta_{jp}\, E(\tilde f_k \tilde f_j)$$
>
> Riordinando:
>
> $$E(r_p^e) = \sum_{j=1}^{K} \beta_{jp} \left[\sum_{k=1}^{K} \frac{b_k}{a}\, E(\tilde f_k \tilde f_j)\right]$$
>
> il che consente anche fattori correlati, cioè $E(\tilde f_k \tilde f_j) = \mathrm{Cov}(\tilde f_k, \tilde f_j) \neq 0$ per $k \neq j$.
>
> **Prezzo del rischio fattoriale**
>
> Si definisca il prezzo del rischio fattoriale:
>
> $$\lambda_j = \sum_{k=1}^{K} \frac{b_k}{a}\, E(\tilde f_k \tilde f_j)$$
>
> che, nel caso di fattori incorrelati, si riduce a $\lambda_j = \dfrac{b_j}{a}\, \mathrm{Var}(\tilde f_j)$.
>
> I rendimenti attesi in eccesso soddisfano allora:
>
> $$E(r_p^e) = \sum_{j=1}^{K} \beta_{jp} \lambda_j$$
>
> **Interpretazione**
>
> - Il pricing dell'APT è coerente con SDF lineare.
> - $\lambda_j$ riassume come il fattore $j$ venga prezzato.
> - È prezzato soltanto il rischio che covaria con l'SDF.

*(slide 35–39)*

## Appendice — Compatibilità tra APT e CAPM

> [!note] Dimostrazione
> **Premessa**
>
> - In precedenza si è visto che CAPM e APT forniscono la stessa implicazione di pricing in un modello a un fattore in cui il fattore è il rendimento di mercato in eccesso.
> - Si può mostrare che CAPM e APT sono compatibili anche per una specificazione **multifattoriale** dell'APT in cui il rendimento di mercato in eccesso non compare neppure tra i fattori (anche con fattori non traded).
> - Si assuma che valgano sia l'APT sia il CAPM e, per semplicità, si consideri una struttura a due fattori, indicati come 1 e 2.
>
> **Dimostrazione**
>
> Si considerino due portafogli fattoriali $p$ (con $\beta_{1p}=1$ e $\beta_{2p}=0$) e $q$ (con $\beta_{1q}=0$ e $\beta_{2q}=1$), per i quali vale l'APT e che forniscono i seguenti premi per il rischio:
>
> $$E(r_p) - r_f = \lambda_1, \qquad E(r_q) - r_f = \lambda_2$$
>
> Per gli stessi portafogli, vale anche il CAPM, il che implica:
>
> $$E(r_p) - r_f = \beta_{mp} E(r_m - r_f) = \lambda_1$$
> $$E(r_q) - r_f = \beta_{mq} E(r_m - r_f) = \lambda_2 \tag{1}$$
>
> dove, con una notazione un po' pesante, si distinguono i beta del CAPM da quelli dell'APT mediante il pedice $m$ (per "mercato").
>
> Si consideri ora un titolo $i$. L'APT implica:
>
> $$E(r_i) - r_f = \beta_{1i} \lambda_1 + \beta_{2i} \lambda_2$$
>
> Si sostituiscano le espressioni di $\lambda_1$ e $\lambda_2$ dall'equazione (1):
>
> $$E(r_i) - r_f = \beta_{1i}\left[\beta_{mp} E(r_m - r_f)\right] + \beta_{2i}\left[\beta_{mq} E(r_m - r_f)\right]$$
> $$= (\beta_{mp}\beta_{1i} + \beta_{mq}\beta_{2i}) E(r_m - r_f)$$
> $$= \beta_{mi} E(r_m - r_f)$$
>
> dove $\beta_{mi} = \beta_{mp}\beta_{1i} + \beta_{mq}\beta_{2i}$.
>
> **Conclusione**
>
> - Questa è precisamente la previsione del CAPM per il titolo $i$.
> - Di conseguenza, APT e CAPM possono valere nello stesso mercato dei capitali, ma **non devono necessariamente farlo** (l'APT è comunque più generale).

*(slide 40–42)*
