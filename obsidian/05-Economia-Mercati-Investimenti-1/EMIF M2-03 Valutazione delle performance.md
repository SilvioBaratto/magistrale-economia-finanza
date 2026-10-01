---
title: "Valutazione della Performance di Portafoglio"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M2-03_Valutazione-delle-performance.pdf"
pages: 58
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione

- Se i mercati sono efficienti, gli investitori devono essere in grado di misurare la performance della gestione patrimoniale.
- Due modi comuni per misurare il rendimento medio di portafoglio:
  1. rendimenti ponderati nel tempo;
  2. rendimenti ponderati per l'ammontare investito.
- I rendimenti devono essere corretti per il rischio.

*(slide 2)*

## Rendimenti ponderati nel tempo e per l'ammontare investito

> [!abstract] Definizione
> **Rendimenti ponderati nel tempo**
>
> - La media geometrica è una media ponderata nel tempo.
> - Il rendimento di ciascun periodo ha lo stesso peso.
>
> $$(1+r_G) = [(1+r_1)\times(1+r_2)\times\cdots\times(1+r_n)]^{1/n}$$
> $$r_G = [(1+r_1)\times(1+r_2)\times\cdots\times(1+r_n)]^{1/n} - 1$$
>
> **Rendimenti ponderati per l'ammontare investito**
>
> - È il tasso interno di rendimento (IRR) che considera i flussi di cassa da e verso l'investimento.
> - I rendimenti sono ponderati per l'importo investito in ciascun periodo:
>
> $$PV = \frac{C_1}{(1+r)} + \frac{C_2}{(1+r)^2} + \cdots + \frac{C_n}{(1+r)^n}$$

*(slide 3–4)*

## Esempio: rendimenti multi-periodali

> [!example] Esempio
> Un investitore acquista azioni in due momenti successivi:
>
> | Tempo | Esborso / Incasso |
> |---|---|
> | 0 | $50 per acquistare la prima azione |
> | 1 | $53 per acquistare una seconda azione un anno dopo |
> | | **Incassi** |
> | 1 | $2 di dividendo dall'azione acquistata inizialmente |
> | 2 | $4 di dividendo dalle 2 azioni detenute nel secondo anno, più $108 ottenuti dalla vendita di entrambe le azioni a $54 ciascuna |
>
> **Rendimento ponderato per l'ammontare investito (IRR):**
>
> $$-50 + \frac{-51}{(1+r)} + \frac{112}{(1+r)^2} = 0$$
> $$r = 7.117\%$$
>
> **Rendimento ponderato nel tempo:**
>
> $$r_1 = \frac{53-50+2}{50} = 10\%\qquad r_2 = \frac{54-53+2}{53} = 5.66\%$$
>
> Media geometrica:
>
> $$r_G = [(1.10)\times(1.0566)]^{1/2} - 1 = 7.81\%$$
>
> La media ponderata per l'ammontare investito è inferiore alla media ponderata nel tempo perché nel secondo anno è investita una somma maggiore, quando il rendimento è stato più basso.
>
> **Nota pratica:** le famiglie dovrebbero mantenere un foglio di calcolo dei flussi di cassa datati (in entrata e in uscita) per determinare il tasso di rendimento effettivo per qualunque periodo dato.

*(slide 5–8)*

## Esempio: il costo di un cattivo market timing

> [!example] Esempio
> Un investitore inizia con $10,000 in un fondo al tempo $t=0$.
>
> | Anno | Rendimento del Fondo | Flusso di Cassa a Inizio Anno | Saldo (finale) |
> |---|---|---|---|
> | 1 | +50% | $10,000 investiti | $15,000 |
> | 2 | −20% | $90,000 aggiunti ⇒ $105,000 | $84,000 |
>
> **Rendimento ponderato nel tempo** (valuta il gestore):
>
> $$r_G = [(1.50)(0.80)]^{1/2} - 1 = 9.54\%$$
>
> **Rendimento ponderato per l'ammontare investito** (valuta l'esperienza dell'investitore):
>
> $$-10{,}000 + \frac{-90{,}000}{1+r} + \frac{84{,}000}{(1+r)^2} = 0 \implies r \approx -8.46\%$$
>
> Il gestore ha generato una performance positiva, ma l'investitore ha perso denaro aggiungendo capitale proprio prima della fase di ribasso.
>
> **Figura — Cattivo Timing, intuizione grafica.** Un grafico a barre mostra il capitale esposto: $10,000 nell'anno buono (+50%) contro $105,000 nell'anno cattivo (−20%). L'investitore aveva solo $10,000 investiti durante l'anno buono, ma $105,000 durante l'anno cattivo: il rendimento ponderato per l'ammontare investito cattura questa penalizzazione da timing.

*(slide 9–10)*

## Correzione dei rendimenti per il rischio: il benchmark

- Il modo più semplice per correggere per il rischio consiste nel confrontare il rendimento del portafoglio con i rendimenti di un universo di confronto.
- L'universo di confronto è chiamato **benchmark**.
- È composto da un gruppo di fondi o portafogli con caratteristiche di rischio simili.

**Figura 24.1** — Universe comparison, periods ending December 31, 2022. Un box-plot mostra, per gli orizzonti 1 Quarter, 1 Year, 3 Years e 5 Years, la distribuzione dei rendimenti (Rate of Return %) dell'universo di confronto (The Markowill Group), con il rendimento medio dell'universo (rombo) e il rendimento dell'S&P 500 (quadrato) sovrapposti. Il confronto permette di collocare la performance di un singolo gestore rispetto alla distribuzione dei suoi pari e rispetto al mercato.

*(slide 11–12)*

## Misure classiche di performance corretta per il rischio: Sharpe, Treynor, Jensen

> [!abstract] Definizione
> **1. Indice di Sharpe** — remunerazione per ogni unità di rischio (volatilità totale):
>
> $$S_p = \frac{\bar r_p - \bar r_f}{\sigma_p}$$
>
> dove $\bar r_p$ = rendimento medio del portafoglio, $\bar r_f$ = tasso medio privo di rischio, $\sigma_p$ = deviazione standard del rendimento del portafoglio.
>
> **2. Misura di Treynor** — remunerazione per ogni unità di rischio sistematico:
>
> $$T_p = \frac{\bar r_p - \bar r_f}{\beta_p}$$
>
> dove $\beta_p$ = beta medio ponderato del portafoglio.
>
> **3. Misura di Jensen** — remunerazione extra oltre alla remunerazione per il rischio:
>
> $$\alpha_p = \bar r_p - [\bar r_f + \beta_p(\bar r_m - \bar r_f)]$$
>
> dove $\alpha_p$ = alpha del portafoglio, $\bar r_m$ = rendimento medio del portafoglio indice di mercato.

*(slide 13–15)*

## Esempio: l'alpha è statisticamente significativo?

> [!example] Esempio
> Un fondo riporta i seguenti dati su 36 mesi ($r_f = 0.3\%$/mese, $\bar r_m = 1.0\%$/mese):
>
> | | $\hat\alpha$ | $\hat\beta$ | $SE(\hat\alpha)$ |
> |---|---|---|---|
> | Fondo X | 0.40%/mese | 1.10 | 0.50%/mese |
> | Fondo Y | 0.25%/mese | 0.85 | 0.10%/mese |
>
> Statistiche $t$:
>
> $$t_X = \frac{0.40}{0.50} = 0.80 \qquad t_Y = \frac{0.25}{0.10} = 2.50$$
>
> Al livello del 5% ($t_{crit} \approx 2.03$):
>
> - Fondo X: $\alpha$ non è significativo, nonostante sia maggiore in valore assoluto.
> - Fondo Y: $\alpha$ è significativo — evidenza genuina di abilità.
>
> **Lezione:** un alpha elevato non significa nulla senza controllare il rumore di stima.

*(slide 16)*

## Information Ratio

> [!abstract] Definizione
> **4. Information Ratio** — remunerazione per ogni unità di rischio idiosincratico:
>
> $$IR = \frac{\alpha_p}{\sigma(e_p)}$$
>
> - L'information ratio divide l'alpha del portafoglio per il rischio non sistematico.
> - Il rischio non sistematico potrebbe, in teoria, essere eliminato tramite diversificazione.

*(slide 17)*

## Misura $M^2$

> [!abstract] Definizione
> Sviluppata da Modigliani e Modigliani:
>
> - Si costruisce un portafoglio corretto $P^*$ che combina $P$ con Treasury Bills.
> - Si impone che $P^*$ abbia la stessa deviazione standard dell'indice di mercato.
> - Si confrontano poi i rendimenti del mercato e di $P^*$:
>
> $$M^2 = r_{P^*} - r_M$$

*(slide 18)*

## Esempio: misura $M^2$

> [!example] Esempio
> - Portafoglio gestito $P$: $r_P = 35\%$, $\sigma_P = 42\%$.
> - Portafoglio di mercato: $r_M = 28\%$, $\sigma_M = 30\%$.
> - Rendimento dei T-bill = 6%.
>
> Portafoglio $P^*$: 30/42 = 0.714 in $P$ e 0.286 in T-bills:
>
> $$r_{P^*} = (0.714)(0.35) + (0.286)(0.06) = 26.7\%$$
>
> $r_{P^*} < r_M \Rightarrow$ il portafoglio gestito ha sottoperformato.
>
> **Figura 24.2** — $M^2$ of portfolio $P$. Nel piano $(\sigma, E(r))$ sono tracciate la Capital Market Line (CML) e la Capital Allocation Line del portafoglio $P$ (CAL($P$)), con i punti $F$ (risk-free), $M$ (mercato), $P^*$ (portafoglio corretto, sulla stessa $\sigma_M$) e $P$. La distanza verticale tra $P^*$ e $M$ sulla CML rappresenta $M^2$: mostra graficamente che $P^*$ giace sotto la CML, cioè sotto la retta del mercato a parità di rischio.

*(slide 19–20)*

## Esempio: $M^2$ con due fondi

> [!example] Esempio
> | | $\bar r$ | $\sigma$ | $\beta$ |
> |---|---|---|---|
> | Fondo A (aggressivo) | 18% | 30% | 1.40 |
> | Fondo B (conservativo) | 13% | 15% | 0.70 |
> | Mercato | 12% | 20% | 1.00 |
> | Tasso privo di rischio | 3% | — | — |
>
> Indici di Sharpe:
>
> $$S_A = \frac{18-3}{30} = 0.50 \qquad S_B = \frac{13-3}{15} = 0.667 \qquad S_M = \frac{12-3}{20} = 0.45$$
>
> Il Fondo A ha un rendimento lordo più elevato, ma il Fondo B ha un indice di Sharpe più alto.
>
> **Correzione del Fondo A** (riduzione della leva fino a $\sigma_M = 20\%$):
>
> $$w_A = \frac{\sigma_M}{\sigma_A} = \frac{20}{30} = 0.667 \;\Rightarrow\; r_{A^*} = 0.667\times18\% + 0.333\times3\% = 13.0\%$$
>
> **Correzione del Fondo B** (aumento della leva fino a $\sigma_M = 20\%$):
>
> $$w_B = \frac{\sigma_M}{\sigma_B} = \frac{20}{15} = 1.333 \;\Rightarrow\; r_{B^*} = 1.333\times13\% - 0.333\times3\% = 16.3\%$$
>
> | | Rendimento Corretto ($\sigma = 20\%$) | $M^2 = r^* - r_M$ |
> |---|---|---|
> | Fondo A$^*$ | 13.0% | +1.0% |
> | Fondo B$^*$ | 16.3% | +4.3% |
>
> **Lezione:** a parità di volatilità, il Fondo B domina. Rendimenti elevati ottenuti con rischio elevato possono essere fuorvianti — $M^2$ elimina proprio questo effetto.

*(slide 21–22)*

## Quale misura è appropriata?

Dipende dalle ipotesi di investimento:

1. Se $P$ è **non diversificato**, si usa la misura di **Sharpe**, perché misura il premio per il rischio totale.
2. Se $P$ è **diversificato**, il rischio non sistematico è trascurabile e la metrica appropriata è quella di **Treynor**, che misura il rendimento in eccesso rispetto al beta.

| Misura | Definizione | Applicazione |
|---|---|---|
| Sharpe | Rendimento in eccesso / Deviazione standard | Scelta tra portafogli per il portafoglio complessivo rischioso |
| Treynor | Rendimento in eccesso / Beta | Classifica di portafogli per formare il portafoglio complessivo rischioso |
| Info. Ratio | Alpha / Dev. std. residua | Valutazione di un portafoglio da combinare con il benchmark |

*(slide 23)*

## Esempio: inversione del ranking — Sharpe vs Treynor

> [!example] Esempio
> Due fondi con $r_f = 3\%$ e premio di mercato = 8%:
>
> | | $\bar r$ | $\sigma$ | $\beta$ | $\sigma(e)$ | Sharpe | Treynor |
> |---|---|---|---|---|---|---|
> | Fondo C (concentrato) | 14% | 25% | 0.80 | 15% | 0.44 | 13.75 |
> | Fondo D (diversificato) | 16% | 22% | 1.50 | 3% | 0.591 | 8.67 |
> | Mercato | 11% | 18% | 1.00 | 0% | 0.444 | 8.00 |
>
> **Classifiche:**
>
> | | Classifica Sharpe | Classifica Treynor |
> |---|---|---|
> | Fondo C | 2° | 1° |
> | Fondo D | 1° | 2° |
>
> **Perché le classifiche non coincidono?** Il Fondo C ha un rischio totale elevato ($\sigma = 25\%$) ma un rischio sistematico basso ($\beta = 0.80$). Gran parte della sua volatilità è idiosincratica (specifica del titolo).
>
> - Sharpe penalizza il Fondo C per il rischio totale ⇒ vince il Fondo D.
> - Treynor considera solo il rischio beta ⇒ il basso beta del Fondo C lo fa apparire eccellente per unità di esposizione al mercato.
>
> **Regola pratica:**
>
> - Se il fondo è il tuo *intero portafoglio* ⇒ usa Sharpe (sopporti tutto il rischio).
> - Se il fondo è *una componente* di un portafoglio diversificato ⇒ usa Treynor (il rischio idiosincratico verrà diversificato).

*(slide 24–25)*

## Esempio: performance di portafoglio P vs Q

> [!example] Esempio
> | | Portafoglio P | Portafoglio Q | Mercato |
> |---|---|---|---|
> | Beta | 0.90 | 1.60 | 1.0 |
> | Rendimento in eccesso ($\bar r - \bar r_f$) | 11% | 19% | 10% |
> | Alpha | 2% | 3% | 0 |
>
> $$\text{Alpha} = \text{Rendimento in eccesso} - (\text{Beta}\times\text{Rendimento in eccesso del mercato})$$
>
> **Figura 24.3** — Treynor's measure. Nel piano (Beta, Excess Return) sono tracciate le rette $T_P$ Line e $T_Q$ Line (che passano per l'origine e per i punti P e Q rispettivamente) e la SML; si osserva che la retta $T_Q$ è più ripida di $T_P$, cioè Q offre un rendimento in eccesso maggiore per unità di beta.
>
> **Statistiche di Performance:**
>
> | | Portafoglio P | Portafoglio Q | Portafoglio M |
> |---|---|---|---|
> | Indice di Sharpe | 0.43 | 0.49 | 0.19 |
> | $M^2$ | 2.16 | 2.66 | 0.00 |
> | **Statistiche di regressione SCL** | | | |
> | Alpha | 1.63 | 5.26 | 0.00 |
> | Beta | 0.70 | 1.40 | 1.00 |
> | Treynor | 3.97 | 5.38 | 1.64 |
> | $T^2$ | 2.34 | 3.74 | 0.00 |
> | $\sigma(e)$ | 2.02 | 9.81 | 0.00 |
> | Information ratio | 0.81 | 0.54 | 0.00 |
> | $R$-quadrato | 0.91 | 0.64 | 1.00 |
>
> **Interpretazione:**
>
> - Se P o Q rappresentano l'intero investimento, Q è migliore grazie al suo indice di Sharpe più elevato e a un miglior $M^2$.
> - Se P e Q competono per il ruolo di uno tra vari sottoportafogli, Q domina ancora perché la sua misura di Treynor è più elevata.
> - Se cerchiamo un portafoglio attivo da combinare con un portafoglio indice, P è migliore grazie al suo information ratio più elevato.

*(slide 26–29)*

## Il ruolo dell'alpha nelle misure di performance

> [!tip] Teorema
> | | Treynor ($T_p$) | Sharpe ($S_p$) | Info. Ratio |
> |---|---|---|---|
> | Relazione | $\dfrac{E(r_p)-r_f}{\beta_p} = \dfrac{\alpha_p}{\beta_p} + T_M$ | $\dfrac{E(r_p)-r_f}{\sigma_p} = \dfrac{\alpha_p}{\sigma_p} + \rho S_M$ | $\dfrac{\alpha_p}{\sigma(e_p)}$ |
> | Miglioramento | $T_p - T_M = \dfrac{\alpha_p}{\beta_p}$ | $S_p - S_M = \dfrac{\alpha_p}{\sigma_p} - (1-\rho)S_M$ | $\dfrac{\alpha_p}{\sigma(e_p)}$ |
>
> La tabella mostra come, in ciascuna misura, il rendimento in eccesso del portafoglio si scomponga in una componente legata al mercato (proporzionale a $T_M$ o $S_M$) e in una componente di miglioramento dovuta esclusivamente all'alpha del gestore.

*(slide 30)*

## Misurazione della performance per gli hedge fund

> [!abstract] Definizione
> Quando l'hedge fund è combinato in modo ottimale con il portafoglio di base, il miglioramento dell'indice di Sharpe è determinato dal suo information ratio:
>
> $$S_P^2 = S_M^2 + \left[\frac{\alpha_H}{\sigma(e_H)}\right]^2$$

*(slide 31)*

## Esempio: quanto vale un information ratio?

> [!example] Esempio
> Due fondi attivi sono candidati a essere combinati con un fondo indice S&P 500 ($S_M = 0.45$):
>
> | | $\alpha$ (%/anno) | $\sigma(e)$ (%/anno) | $IR = \alpha/\sigma(e)$ |
> |---|---|---|---|
> | Fondo E | 3.0 | 6.0 | 0.50 |
> | Fondo F | 4.0 | 5.0 | 0.80 |
>
> Indice di Sharpe risultante del portafoglio combinato in modo ottimale:
>
> $$S_P^2 = S_M^2 + IR^2$$
> $$S_{P,E} = \sqrt{0.45^2+0.50^2} = \sqrt{0.4525} = 0.673$$
> $$S_{P,F} = \sqrt{0.45^2+0.80^2} = \sqrt{0.8425} = 0.918$$
>
> L'IR più elevato del Fondo F aumenta l'indice di Sharpe combinato da 0.45 a 0.92 — più che raddoppiandolo. Il Fondo E lo porta solo a 0.67.

*(slide 32)*

## Esempio: IR e peso ottimale del fondo attivo (Treynor–Black)

> [!example] Esempio
> Il peso ottimale nel fondo attivo:
>
> $$w^* = \frac{\alpha/\sigma(e)^2}{E(r_M-r_f)/\sigma_M^2}$$
>
> Supponiamo $E(r_M-r_f) = 8\%$, $\sigma_M = 18\%$:
>
> $$w_E^* = \frac{3.0/36}{8.0/324} = \frac{0.0833}{0.0247} = 3.37 \;\Rightarrow\; \text{aumentare la leva}$$
> $$w_F^* = \frac{4.0/25}{8.0/324} = \frac{0.16}{0.0247} = 6.48 \;\Rightarrow\; \text{ancora di più}$$
>
> Nella pratica, i vincoli limitano questi pesi. Il punto chiave: un IR più elevato ⇒ una maggiore inclinazione ottimale verso il gestore attivo ⇒ un maggior miglioramento del portafoglio.

*(slide 33)*

## Misurazione della performance con composizione di portafoglio variabile

- Abbiamo bisogno di un periodo di osservazione molto lungo per misurare la performance con una qualche precisione, anche se la distribuzione dei rendimenti è stabile con media e varianza costanti.
- E se media e varianza non fossero costanti? Dobbiamo tenere traccia dei cambiamenti di portafoglio. Lo faremo con la Style Analysis nei corsi futuri.

*(slide 34)*

## Active Share vs Tracking Error: classificazione dei fondi

> [!example] Esempio
> **Figura** — Active Share (%) vs Tracking Error (% annuo), basata su Cremers & Petajisto (2009, *RFS*). Lo scatterplot divide il piano in quattro quadranti tramite soglie orizzontale e verticale: in alto a sinistra gli **Stock picker diversificati** (Active Share alto, Tracking Error basso), in alto a destra gli **Stock picker concentrati** (Active Share alto, Tracking Error alto), in basso a sinistra i **Closet indexer** (entrambi bassi) e nell'angolo estremo i **Fondi indicizzati**, in basso a destra le **Scommesse su fattori** (Active Share basso, Tracking Error alto). Active Share e Tracking Error, usati congiuntamente, classificano il tipo di gestione attiva di un fondo.

*(slide 35)*

## Fondi attivi vs benchmark: SPIVA U.S. Scorecard (dic. 2024)

> [!example] Esempio
> **Figura** — % di fondi attivi che sottoperformano il benchmark, per categoria (Large-Cap, Mid-Cap, Small-Cap) e orizzonte temporale (1-Yr, 3-Yr, 5-Yr, 10-Yr, 15-Yr), con una linea di riferimento al 50%.
>
> Fonte: S&P Dow Jones Indices, SPIVA U.S. Scorecard di fine 2024. I tassi di sottoperformance aumentano con l'orizzonte temporale; su 15 anni, nessuna categoria azionaria ha avuto una maggioranza di gestori attivi in grado di sovraperformare.

*(slide 36)*

## Manipolazione della performance e MRAR

- Ipotesi: i tassi di rendimento sono indipendenti e tratti dalla stessa distribuzione.
- I gestori possono adottare strategie che migliorano la performance a scapito degli investitori.
- Lo studio di Ingersoll, Spiegel, Goetzmann e Welch conduce al **MPPM** (Manipulation-Proof Performance Measure).
- Uso della leva per aumentare i rendimenti potenziali.
- Il **MRAR** soddisfa i requisiti dell'MPPM.

*(slide 37)*

## Rendimento corretto per il rischio Morningstar (MRAR)

> [!abstract] Definizione
> $$MRAR(\gamma) = \left[\frac{1}{T}\sum_{t=1}^{T}\left(\frac{1+r_t}{1+r_{ft}}\right)^{1-\gamma}\right]^{\frac{12}{1-\gamma}} - 1$$
>
> dove:
>
> - $\gamma$ = avversione al rischio dell'investitore;
> - $t = 1,2,\dots,T$ = osservazioni mensili.

*(slide 38)*

## Punteggi MRAR con e senza manipolazione

> [!example] Esempio
> **Figura** — Due scatterplot mettono in relazione l'indice di Sharpe e l'MRAR di un campione di fondi: il pannello A ("No Manipulation") mostra la relazione base tra Sharpe e MRAR, mentre il pannello B ("Manipulation") mostra la stessa relazione dopo l'introduzione di strategie di manipolazione della performance (uso della leva/opzioni per gonfiare artificialmente l'indice di Sharpe). Nel pannello con manipolazione la nuvola di punti si sposta verso MRAR più bassi a parità di Sharpe: l'indice di Sharpe può essere manipolato senza che il rischio economico effettivo migliori, mentre l'MRAR — costruito per essere manipulation-proof — rivela il deterioramento della qualità della performance.

*(slide 39)*

## Market timing: i modelli di Treynor–Mazuy e Henriksson–Merton

> [!abstract] Definizione
> Nella sua forma pura, il market timing consiste nello spostare fondi tra un portafoglio indice di mercato e un'attività sicura.
>
> **Treynor e Mazuy:**
>
> $$r_p - r_f = a + b(r_M-r_f) + c(r_M-r_f)^2 + e_p$$
>
> **Henriksson e Merton:**
>
> $$r_p - r_f = a + b(r_M-r_f) + c(r_M-r_f)D + e_p$$
>
> **Figura 24.8** — Characteristic lines. **Panel A**: nessun market timing, il beta è costante (retta con pendenza $= 0.6$). **Panel B**: market timing, il beta aumenta con il rendimento in eccesso atteso del mercato (pendenza crescente in modo continuo — curva del modello Treynor–Mazuy). **Panel C**: market timing con soli due valori di beta (due tratti rettilinei di pendenza $b$ e $b+c$ — struttura del modello Henriksson–Merton).

*(slide 40–41)*

## Esempio: market timing — esercizio di regressione

> [!example] Esempio
> I rendimenti mensili in eccesso di un fondo su 12 mesi, insieme a quelli del mercato:
>
> | Mese | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | $r_M - r_f$ (%) | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> | $r_P - r_f$ (%) | −1.8 | −1.5 | −1.0 | −0.3 | 0.1 | 0.8 | 1.8 | 2.9 | 4.2 | 5.8 | 7.5 | 9.6 |
>
> Si noti come i rendimenti del fondo accelerino al crescere del mercato — questa curvatura suggerisce capacità di market timing.
>
> **Figura — grafico a dispersione.** Nel piano $(r_M-r_f, r_P-r_f)$ i punti mostrano una curvatura verso l'alto rispetto a un fit lineare: viene sovrapposta sia la retta di regressione lineare semplice ("Fit lineare") sia la curva quadratica del modello Treynor–Mazuy ("Quadratica T&M"), che meglio si adatta ai dati. Il fondo amplifica i guadagni e attenua le perdite.
>
> **Regressione Treynor–Mazuy** (errori standard tra parentesi):
>
> $$r_P - r_f = \underset{(0.12)}{0.15} + \underset{(0.08)}{0.75}(r_M-r_f) + \underset{(0.03)}{0.10}(r_M-r_f)^2 + e_P$$
>
> Il coefficiente $c = 0.10$ con $t = 0.10/0.03 = 3.33$ è significativo.
>
> **Regressione Henriksson–Merton** ($D=1$ se $r_M - r_f > 0$):
>
> $$r_P - r_f = \underset{(0.15)}{-0.05} + \underset{(0.10)}{0.48}(r_M-r_f) + \underset{(0.14)}{0.62}(r_M-r_f)\cdot D + e_P$$
>
> Il coefficiente $c = 0.62$ con $t = 0.62/0.14 = 4.43$: anch'esso significativo.
>
> **Conclusione:** entrambi i modelli rilevano capacità di timing. Il gestore ha aumentato con successo il beta nei mercati in rialzo.

*(slide 42–44)*

## Tasso di rendimento di un perfetto market timer

> [!example] Esempio
> Investimento iniziale = $1.
>
> | Strategia | Bills | Azioni | Perfetto Market Timer |
> |---|---|---|---|
> | Valore terminale | $20 | $3,997 | $534,649 |
> | Media aritmetica | 3.47% | 11.53% | 16.54% |
> | Deviazione standard | 3.15% | 20.27% | 13.56% |
> | Media geometrica | 3.42% | 9.77% | 15.97% |
> | Massimo | 14.71% | 57.35% | 57.35% |
> | Minimo | −0.02% | −44.04% | 0.00% |
> | Asimmetria | 1.00 | −0.40 | 0.74 |
> | Curtosi | 0.93 | 0.03 | −0.12 |
> | LPSD | 0.00% | 13.28% | 0.00% |
>
> **Figura 24.9** — Rate of return of a perfect market timer as a function of the rate of return on the market index. Il grafico mostra una retta spezzata: piatta (pari a $r_f$) per rendimenti di mercato inferiori a $r_f$, e crescente con pendenza 1 per rendimenti di mercato superiori a $r_f$ — un profilo identico a quello di un'opzione call sul mercato. Il perfetto market timer ottiene sempre il maggiore tra il rendimento del mercato e quello dei bills, il che spiega il valore terminale enormemente superiore e il minimo pari a 0%.

*(slide 45–46)*

## Valutare il market timing come un'opzione call

> [!abstract] Definizione
> Il perfetto market timer replica il payoff di un'opzione call sul mercato con strike $X$ combinata con un investimento in bills:
>
> | | $S_T < X$ | $S_T \ge X$ |
> |---|---|---|
> | Bills | $S_0(1+r_f)$ | $S_0(1+r_f)$ |
> | Call | 0 | $S_T - X$ |
> | **Totale** | $S_0(1+r_f)$ | $S_T$ |
>
> Quando il mercato è sotto lo strike, il valore totale coincide con l'investimento in bills capitalizzato; quando il mercato è sopra lo strike, il valore totale coincide con il valore del mercato stesso — esattamente il comportamento del perfetto market timer.

*(slide 47)*

## Procedure di attribuzione della performance

Un comune sistema di attribuzione scompone la performance in tre componenti:

1. scelte di allocazione tra ampie classi di attivo;
2. scelta dell'industria o del settore all'interno di ciascun mercato;
3. selezione dei titoli all'interno di ciascun settore.

**Impostare un portafoglio "Bogey":**

- selezionare un portafoglio indice benchmark per ciascuna asset class;
- scegliere i pesi sulla base delle aspettative di mercato;
- scegliere un portafoglio di titoli all'interno di ciascuna classe tramite analisi dei titoli.

*(slide 48)*

## Formule per l'attribuzione

> [!abstract] Definizione
> $$r_B = \sum_{i=1}^{n} w_{Bi}\,r_{Bi} \qquad r_p = \sum_{i=1}^{n} w_{pi}\,r_{pi}$$
>
> $$r_p - r_B = \sum_{i=1}^{n} w_{pi}\,r_{pi} - \sum_{i=1}^{n} w_{Bi}\,r_{Bi}$$
>
> dove $B$ è il portafoglio bogey e $p$ è il portafoglio gestito.

*(slide 49)*

## Attribuzione della performance della i-esima asset class

> [!abstract] Definizione
> **Figura 24.10** — Attribuzione della performance della $i$-esima asset class. Nel piano (Peso nell'Asset Class, Rendimento dell'Asset Class) sono evidenziate tre aree rettangolari: il **Rendimento Bogey** ($=r_{Bi}\cdot w_{Bi}$), l'area **Aggiunto dalla Selezione** (dovuta alla differenza $r_{Pi}-r_{Bi}$ al peso benchmark $w_{Bi}$), l'area di **Allocazione** (dovuta alla differenza di peso $w_{Pi}-w_{Bi}$ al rendimento benchmark $r_{Bi}$) e un'area di **Origine mista** (attribuita convenzionalmente alla selezione), generata dal prodotto incrociato tra la differenza di rendimento e la differenza di peso. La figura illustra visivamente come il contributo totale della classe si scomponga in effetto di allocazione ed effetto di selezione.

*(slide 50)*

## Esempio: mini-caso di attribuzione della performance

> [!example] Esempio
> Un gestore di un fondo pensione utilizza un semplice benchmark a due asset:
>
> | Asset Class | Peso Benchmark | Rendimento dell'Indice |
> |---|---|---|
> | Azioni | 60% | 4.0% |
> | Obbligazioni | 40% | 2.0% |
>
> Rendimento bogey: $0.60\times4.0 + 0.40\times2.0 = 3.20\%$
>
> Il gestore si è discostato dal benchmark:
>
> | | Peso Effettivo | Rendimento del Portafoglio |
> |---|---|---|
> | Azioni | 50% | 5.0% |
> | Obbligazioni | 50% | 2.5% |
>
> Rendimento di portafoglio: $0.50\times5.0 + 0.50\times2.5 = 3.75\%$
>
> Eccesso totale: $3.75\% - 3.20\% = +55$ bp. Da dove deriva?
>
> **Passo 1 — effetto di allocazione:**
>
> $$= \sum_i (w_{pi}-w_{Bi})\times r_{Bi}$$
>
> | | Peso in Eccesso ($w_p - w_B$) | Rend. indice $r_B$ | Contributo |
> |---|---|---|---|
> | Azioni | −0.10 | 4.0% | −0.40% |
> | Obbligazioni | +0.10 | 2.0% | +0.20% |
> | **Effetto di allocazione** | | | **−0.20%** |
>
> L'allocazione è stata negativa: il gestore ha sottopesato l'asset con rendimento migliore (le azioni).
>
> **Passo 2 — effetto di selezione:**
>
> $$= \sum_i w_{pi}\times(r_{pi}-r_{Bi})$$
>
> | | Peso portaf. $w_p$ | Performance in eccesso ($r_p - r_B$) | Contributo |
> |---|---|---|---|
> | Azioni | 0.50 | 1.0% | +0.50% |
> | Obbligazioni | 0.50 | 0.5% | +0.25% |
> | **Effetto di selezione** | | | **+0.75%** |
>
> Totale: $-0.20 + 0.75 = +0.55\%$ ✓ Lo stock-picking del gestore ha più che compensato la cattiva allocazione.

*(slide 51–53)*

## Esempio esteso di attribuzione della performance

> [!example] Esempio
> **Benchmark a tre asset class:**
>
> | Componente | Peso Benchmark | Rendimento Indice (%) |
> |---|---|---|
> | Azioni (S&P 500) | 0.60 | 5.81 |
> | Obbligazioni (Barclays Agg.) | 0.30 | 1.45 |
> | Liquidità (money market) | 0.10 | 0.48 |
>
> Bogey $= (0.60\times5.81) + (0.30\times1.45) + (0.10\times0.48) = 3.97\%$
>
> | | |
> |---|---|
> | Rendimento del portafoglio gestito | 5.34% |
> | − Rendimento del portafoglio bogey | 3.97% |
> | **Rendimento in eccesso del portafoglio gestito** | **1.37%** |
>
> **Contributo dell'asset allocation:**
>
> | Mercato | Peso effettivo | Peso bench. | Peso in eccesso | Rend. indice (%) | Contrib. (%) |
> |---|---|---|---|---|---|
> | Azioni | 0.70 | 0.60 | 0.10 | 5.81 | 0.5810 |
> | Reddito fisso | 0.07 | 0.30 | −0.23 | 1.45 | −0.3335 |
> | Liquidità | 0.23 | 0.10 | 0.13 | 0.48 | 0.0624 |
> | **Contributo dell'asset allocation** | | | | | **0.3099** |
>
> **Contributo della selezione all'interno dei mercati:**
>
> | Mercato | Perf. portaf. (%) | Perf. indice (%) | Perf. in eccesso (%) | Peso portaf. | Contrib. (%) |
> |---|---|---|---|---|---|
> | Azioni | 7.28 | 5.81 | 1.47 | 0.70 | 1.03 |
> | Reddito fisso | 1.89 | 1.45 | 0.44 | 0.07 | 0.03 |
> | **Contributo della selezione all'interno dei mercati** | | | | | **1.06** |
>
> **Attribuzione della performance: allocazione settoriale (componente azionaria):**
>
> | Settore | Portafoglio | S&P 500 | Peso attivo (%) | Rend. settore (%) | Contrib. |
> |---|---|---|---|---|---|
> | Materie prime di base | 1.96 | 8.3 | −6.34 | 6.9 | −0.4375 |
> | Servizi alle imprese | 7.84 | 4.1 | 3.74 | 7.0 | 0.2618 |
> | Beni capitali | 1.87 | 7.8 | −5.93 | 4.1 | −0.2431 |
> | Consumi ciclici | 8.47 | 12.5 | −4.03 | 8.8 | 0.3546 |
> | Consumi non ciclici | 40.37 | 20.4 | 19.97 | 10.0 | 1.9970 |
> | Sensibili al credito | 24.01 | 21.8 | 2.21 | 5.0 | 0.1105 |
> | Energia | 13.53 | 14.2 | −0.67 | 2.6 | −0.0174 |
> | Tecnologia | 1.95 | 10.9 | −8.95 | 0.3 | −0.0269 |
> | **TOTALE** | | | | | **1.2898** |
>
> **Sintesi dell'attribuzione della performance:**
>
> | Componente | Contributo (bp) |
> |---|---|
> | 1. Asset allocation | 31 |
> | 2. Selezione | |
> | &nbsp;&nbsp;a. Rendimento in eccesso azionario | |
> | &nbsp;&nbsp;&nbsp;&nbsp;i. Allocazione settoriale | 129 |
> | &nbsp;&nbsp;&nbsp;&nbsp;ii. Selezione dei titoli | 18 |
> | &nbsp;&nbsp;&nbsp;&nbsp;147 × 0.70 (peso di portafoglio) = | 102.9 |
> | &nbsp;&nbsp;b. Rendimento in eccesso del reddito fisso: 44 × 0.07 = | 3.1 |
> | **Rendimento totale in eccesso del portafoglio** | **137.0** |
>
> - Una buona performance deriva dal sovrappesare i settori con performance elevate.
> - Una buona performance deriva anche dal sottopesare i settori con performance deboli.

*(slide 54–58)*
