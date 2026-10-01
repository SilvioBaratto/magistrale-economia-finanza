---
title: "La valutazione delle operazioni di integrazione (crescita esterna e valore)"
tags:
  - corso/finanza-strategica
  - tipo/lezione
corso: "[[Finanza Strategica]]"
source: "FSTR_Slide_12_Valutazione-Operazioni-di-Integrazione.pdf"
pages: 12
text_layer: true
verified: true
generated: 2026-08-30
---

## Introduzione e riferimenti

**Strategie di investimento** — Crescita esterna e valore delle operazioni di integrazione. La valutazione delle operazioni di integrazione.

Letture di riferimento: Capitolo 9, Testo BBS.

*(slide 1)*

## Le sinergie: tre effetti sul valore

> [!abstract] Definizione
> Le sinergie generate da un'operazione di integrazione (fusione o acquisizione) possono essere ricondotte a tre effetti distinti sul valore dell'impresa risultante:
>
> A. **Differenziale di quantità** → impatto sui flussi (di cassa)
>
> B. **Differenziale di qualità** → impatto sul rischio
>
> C. **Differenziale di struttura finanziaria** → impatto sul debt/equity ratio obiettivo

*(slide 2)*

## Il modello di stratificazione del valore

> [!abstract] Definizione
> La quantificazione delle sinergie si può effettuare tramite il **modello di stratificazione del valore**, che presuppone a sua volta l'utilizzo del **valore attuale modificato (steady state)**. Ipotizzando due imprese A e B, il valore delle sinergie si scompone in tre componenti, elencate in ordine di crescente difficoltà di stima:
>
> 1. **Valore dei flussi incrementali**
> $$V_{Flussi} = \frac{\Delta FCFO_A}{r_{0,A+B}} + \frac{\Delta FCFO_B}{r_{0,A+B}}$$
>
> 2. **Valore del debito incrementale** (maggiore scudo fiscale)
> $$V_{TS} = \Delta D \cdot t_c$$
>
> 3. **Valore della modifica del costo del capitale**
> $$V_{c.cap.} = \frac{FCFO_A+FCFO_B}{r_{0,A+B}} - \left(\frac{FCFO_A}{r_{0,A}}+\frac{FCFO_B}{r_{0,B}}\right)$$
>
> Il valore complessivo delle sinergie è dato dalla somma delle tre componenti:
> $$\text{VALORE SINERGIE} = V_{Flussi} + V_{TS} + V_{c.cap.}$$
>
> La freccia "DIFFICOLTÀ' STIMA" che accompagna lo schema indica che la stima diventa progressivamente più complessa man mano che si passa dal valore dei flussi incrementali al valore del debito incrementale, fino al valore della modifica del costo del capitale.

*(slide 3)*

## Esempio numerico: valutazione stand-alone e levered di A e B

> [!example] Esempio
> Si considerino due imprese: l'impresa acquirente (A) e l'impresa-target (B).
>
> | | Impresa acquirente (A) | Impresa-*target* (B) |
> |---|---|---|
> | A) Flusso di cassa operativo al netto delle imposte (FCFO) | 4 000 | 3 000 |
> | B) Costo del capitale unlevered: ($K_{eu}$) | 20% | 15% |
> | C) Valore unlevered: $W_U=(a/b)$ | 20 000 | 20 000 |
> | D) Indebitamento finanziario netto: (D) | 10 000 | 8 000 |
> | E) Aliquota dell'imposta societaria | 37% | 37% |
> | F) Valore levered: $W_L=(c+d\times e)$ | 23 700 | 22 960 |
> | G) Valore dell'equity: $W_E$ | 13 700 | 14 960 |
>
> È stato calcolato che gli impatti dell'acquisizione saranno:
>
> $$\Delta FCFO = 1.000 \qquad \Delta Debito = 6.000 \qquad R_0 = K_{eu} = 16\%$$

*(slide 4)*

## La determinazione del valore di acquisizione

> [!example] Esempio
> A partire dai dati dell'esempio precedente si scompone il valore di acquisizione nelle sue quattro componenti:
>
> **Valore riferibile alla differenza di struttura finanziaria** (maggiori scudi fiscali generati dal debito incrementale):
> $$W_{diff.\ strutt.\ finanz.} = 6\,000 \times 0{,}37 = 2\,220$$
>
> **Valore riferibile alla riduzione del rischio**:
> $$W_{diff.\ rischio} = \frac{3\,000+4\,000}{0{,}16} - \frac{3\,000}{0{,}15} - \frac{4\,000}{0{,}20} = 3\,750$$
>
> **Valore dei flussi operativi incrementali**:
> $$W_{diff.\ flussi} = \frac{1\,000}{0{,}16} = 6\,250$$
>
> **Valore stand alone dell'impresa-target**: 14 960
>
> Sommando le quattro componenti si ottiene il valore di acquisizione:
> $$2\,220 + 3\,750 + 6\,250 + 14\,960 = 27.180 = \text{TOTALE} = \text{valore di acquisizione}$$

*(slide 5)*

## Valore stand alone e valore di acquisizione: il premio massimo

**Figura** — Schema a blocchi: alla base il blocco grigio "EV del target" (= "Valore stand alone"); sopra di esso si impilano tre blocchi che rappresentano rispettivamente le sinergie fiscali, le sinergie operative e le sinergie finanziarie, fino a un limite segnato da un segnale di stop con l'etichetta "Premio massimo!"; a fianco un blocco giallo "Premio per l'acquisizione" copre lo spazio tra il valore stand alone e il livello del premio massimo.

La figura mostra che l'acquirente non dovrebbe mai pagare, come premio sopra il valore stand-alone (EV) del target, più del valore complessivo delle sinergie attese (fiscali + operative + finanziarie). Il "premio massimo" pagabile coincide quindi con la somma di EV del target e valore totale delle sinergie: oltre quel limite l'acquisizione distrugge valore per gli azionisti dell'acquirente.

*(slide 6)*

## NPV di investimenti e acquisizioni

> [!abstract] Definizione
> Il problema di valutazione è sempre lo stesso: verificare l'effetto dell'iniziativa (un investimento o un'acquisizione) sul valore d'impresa. Si può quindi definire il NPV creato da un investimento o da un'acquisizione come segue:
>
> $$NPV(\text{investimento}) = V.A.\ \text{lordo} - \text{Inv. Iniziale}$$
>
> $$NPV(\text{acquisizione}) = W_{\text{acquisizione}} - P_{\text{pagato}}$$
>
> dove $W_{acquisizione}$ è il valore complessivo generato dall'acquisizione (comprensivo delle sinergie, secondo il modello di stratificazione del valore visto in precedenza) e $P_{pagato}$ è il prezzo effettivamente corrisposto per l'operazione.

*(slide 7)*

## Il rapporto di concambio: RC massimo e RC minimo

> [!note] Dimostrazione
> Si ipotizza un'unione per incorporazione dell'impresa B nell'impresa A.
>
> **Definizione.** Il rapporto di concambio (RC) è il numero di azioni dell'incorporante (A) ottenuto per ogni azione dell'incorporata (B); si tratta di un prezzo negoziato tra le parti.
>
> **RC massimo, per gli azionisti dell'incorporante.**
> Condizione: la quota percentuale di ricchezza complessiva post-fusione spettante agli azionisti di A deve restare almeno pari alla loro ricchezza pre-fusione $W_A$, cioè $W\ complessivo\% = W_A$:
> $$W_{A+B}\,\frac{N_A}{N_A+N_B\,RC_{MAX}} = W_A$$
>
> Da cui, risolvendo per $RC_{MAX}$:
> $$RC_{MAX} = \frac{N_A}{N_B}\left(\frac{W_{A+B}-W_A}{W_A}\right)$$
>
> che si può riscrivere come:
> $$RC_{MAX} = \frac{N_A}{N_B}\frac{W_{A+B}}{W_A} - \frac{N_A}{N_B} = \frac{W_{A+B}}{N_B\dfrac{W_A}{N_A}} - \frac{N_A}{N_B}$$
>
> **RC minimo, per gli azionisti dell'incorporata.**
> Condizione analoga: la quota percentuale di ricchezza complessiva post-fusione spettante agli azionisti di B deve restare almeno pari a $W_B$, cioè $W\ complessivo\% = W_B$:
> $$W_{A+B}\,\frac{N_B\,RC_{MIN}}{N_A+N_B\,RC_{MIN}} = W_B$$
>
> Da cui:
> $$RC_{MIN} = \frac{W_B\,N_A}{N_B(W_{A+B}-W_B)}$$
>
> che si può riscrivere come:
> $$RC_{MIN} = \frac{\dfrac{W_B}{N_B}\,N_A}{W_{A+B}-W_B}$$
>
> Dove $N_A$, $N_B$ sono il numero di azioni in circolazione di A e B, e $W_A$, $W_B$, $W_{A+B}$ sono rispettivamente il valore stand-alone di A, il valore stand-alone di B e il valore dell'entità combinata post-fusione.

*(slide 8–9)*

## Validi motivi per una fusione

Le principali motivazioni economicamente valide per una fusione sono:

1. **Economie di scala**
   - Le imprese più grandi possono ridurre i costi medi unitari aumentando le quantità prodotte e distribuendo i costi fissi su un volume maggiore di produzione (riduzione delle inefficienze operative e amministrative).

2. **Economie di integrazione verticale**
   - Riducono i costi aumentando l'efficienza.
   - Possono essere verso l'alto (fornitura) o verso il basso (cliente finale).
   - Il controllo dei fornitori può ridurre i costi.
   - Soluzione migliore quando due attività sono strettamente collegate.

3. **Combinazione di risorse complementari**
   - La fusione può completare ciò che manca alle imprese coinvolte (ad es. un'impresa con un prodotto esclusivo ma scarse capacità distributive, e un'altra che ha la rete distributiva ma non il prodotto).
   - Le piccole imprese possono beneficiare dell'organizzazione delle grandi imprese già esistenti.

4. **Eccesso di fondi**
   - Nel caso di imprese mature (*cash cows*), con pochi progetti a VAN positivo, le acquisizioni (spesso per contante) possono essere una valida alternativa all'impiego di fondi all'interno dell'impresa.

*(slide 10–11)*

## Ragioni dubbie per una fusione: la diversificazione

Tra le ragioni comunemente addotte per una fusione, ma economicamente dubbie, vi è la **diversificazione**:

- La diversificazione in sé è positiva.
- Tuttavia è più facile da realizzare per l'azionista (individuo), che può diversificare autonomamente il proprio portafoglio, piuttosto che per l'impresa.
- Gli investitori non pagano un premio per le aziende diversificate: si osserva anzi il cosiddetto *discount* di gruppo.

*(slide 12)*
