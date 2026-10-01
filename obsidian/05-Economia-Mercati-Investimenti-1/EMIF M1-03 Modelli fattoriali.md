---
title: "Modelli fattoriali"
tags:
  - corso/economia-mercati-investimenti-1
  - tipo/lezione
corso: "[[Economia Mercati Investimenti 1]]"
source: "EMIF_Slide_M1-03_Modelli-fattoriali.pdf"
pages: 77
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione

Corso: *Economia dei mercati ed investimenti finanziari (EM5002)* — Modulo su **Modelli fattoriali**. Docente: Stefano Colonnello, Università Ca' Foscari Venezia.

**Outline della lezione:**
1. Motivazione
2. Modelli a un fattore
3. Modelli multifattoriali
4. Implementazione dei modelli fattoriali
5. Frontiera efficiente con modelli fattoriali
6. Strategie smart beta
7. Appendice: regolarizzazione (ridge, LASSO)

*(slide 1–2)*

## Motivazione: il numero di input nel modello di Markowitz

Per calcolare la **frontiera efficiente** nel modello di Markowitz occorrono, per $N$ titoli:
- rendimento atteso per $N$ titoli;
- volatilità per $N$ titoli;
- correlazioni tra tutti i titoli.

**Domanda:** supponendo che un fondo segua 150 società (tipicamente tra 150 e 250 titoli), quanti input sono necessari?

**Conteggio:**
- 150 rendimenti attesi e 150 volatilità;
- correlazione $\rho_{ij}$ per ogni coppia $i,j$, con $i=N=150$, $j=N-1=149$ (poiché $i\neq j$);
- si richiedono quindi $\dfrac{N(N-1)}{2} = 11.175$ termini di correlazione (matrice simmetrica) come input;
- in totale: $150+150+11.175 = 11.475$ input.

In generale, nel modello di Markowitz (covarianza completa) il numero di parametri è:
$$\#\text{parametri} = 2N + \frac{N(N-1)}{2} = \frac{N(N+3)}{2}$$

**Perché è problematico?**
- Tali parametri devono essere stimati; storicamente ciò ha rappresentato un forte onere computazionale.
- La gestione di un numero elevato di parametri risulta complessa per gli analisti finanziari (umani, non IA).
- Stimare un numero elevato di correlazioni può rendere la **matrice di covarianza mal condizionata** (ad esempio varianza negativa del portafoglio), a causa di:
  - errore di stima;
  - arrotondamenti.

*(slide 3–5)*

## Esempio: matrice di covarianza mal condizionata

> [!example] Esempio
> Si considerino tre titoli rischiosi con:
> - Volatilità: $\sigma_1=20\%$, $\sigma_2=25\%$, $\sigma_3=30\%$
> - Correlazioni a coppie: $\rho_{12}=0,9$, $\rho_{13}=0,9$, $\rho_{23}=-0,9$
>
> Matrice di correlazione:
> $$R = \begin{pmatrix} 1 & 0,9 & 0,9 \\ 0,9 & 1 & -0,9 \\ 0,9 & -0,9 & 1 \end{pmatrix}$$
>
> Si ha $\det(R) = -2,888 < 0 \Rightarrow R$ **non** è semidefinita positiva.
>
> La matrice varianza–covarianza è $\Sigma = DRD$, con $D=\text{diag}(\sigma_1,\sigma_2,\sigma_3)$:
> $$\Sigma = \begin{pmatrix} 0,04 & 0,045 & 0,054 \\ 0,045 & 0,0625 & -0,0675 \\ 0,054 & -0,0675 & 0,09 \end{pmatrix}$$
>
> Si considerino pesi di portafoglio (vendita allo scoperto ammessa):
> $$w = (-1,\,1,\,1), \qquad \sum_i w_i = 1$$
>
> La varianza del portafoglio è:
> $$\sigma_p^2 = w'\Sigma w = 0,04+0,0625+0,09-0,09-0,108-0,135 = -0,1405$$
>
> Poiché $\sigma_p^2<0$, il risultato è economicamente privo di senso. Una matrice semidefinita positiva assicura invece che tutte le combinazioni $w'\Sigma w$ diano varianza positiva: correlazioni stimate singolarmente **non** garantiscono una matrice di covarianza congiuntamente valida.
>
> Si tratta di un problema cruciale nell'implementazione del modello di Markowitz:
> - l'ottimizzazione può diventare instabile;
> - i portafogli "ottimali" possono implicare varianza negativa.
>
> $\Rightarrow$ Si semplifica il problema mediante **modelli fattoriali**.

*(slide 6–7)*

## Modelli fattoriali: idea generale

> [!abstract] Definizione
> I **modelli fattoriali** assumono che i rendimenti dei titoli si muovano congiuntamente perché determinati da un numero (ridotto) di **fattori comuni**. Costituiscono il fondamento dell'APT (Arbitrage Pricing Theory).
>
> Invece di modellare direttamente le correlazioni, si modellano le **fonti del co-movimento**. Questa struttura riduce drasticamente il numero di parametri e produce tipicamente una matrice di covarianza più stabile.
>
> Si parte dal caso a un fattore.
>
> **Modello generale a un fattore.** Si modellano i rendimenti in eccesso:
> $$r_i^e = a_i + \beta_i f$$
> dove:
> - $r_i^e = r_i - r_f$ è il rendimento in eccesso del titolo $i$;
> - $f$ è un fattore comune (espresso tipicamente in forma di rendimento in eccesso se traded);
> - $\beta_i$ misura l'esposizione al fattore;
> - $a_i$ è una componente specifica del titolo.
>
> Se $f$ è **traded** (negoziabile), rappresenta il rendimento in eccesso di un portafoglio ed è prezzato direttamente da $E[f]$ (esempi: rendimento di mercato $r_M-r_f$, fattori Fama–French SMB o HML).
>
> Se $f$ è **non-traded**, il premio per il rischio deve essere inferito da vincoli di equilibrio cross-section (esempi: shock alla crescita dei consumi, innovazioni del PIL).

*(slide 9–10)*

## Single-index model: definizione e ipotesi

> [!abstract] Definizione
> Il caso più rilevante del modello a un fattore è il **single-index model**, in cui il mercato è il fattore che genera la comovimentazione.
>
> **Idea centrale:** tutti i titoli si muovono congiuntamente perché esposti a un fattore comune, il mercato. Ogni titolo presenta una componente sistematica (legata al mercato) e una componente specifica (legata all'impresa).
>
> **Intuizione:** quando il mercato è in fase rialzista, il prezzo della maggior parte dei titoli aumenta $\Rightarrow$ correlazione positiva con un fattore comune.
>
> Rappresentazione statistica dei rendimenti:
> $$r_i^e = a_i + \beta_i r_m^e$$
> dove $a_i$ è la componente specifica del titolo, indipendente dal mercato; $r_m^e$ è il rendimento di mercato in eccesso; $\beta_i$ è il coefficiente che misura la variazione attesa di $r_i$ al variare di $r_m^e$.
>
> Si può scomporre $a_i$ in due parti:
> $$a_i = \alpha_i + e_i$$
> dove $\alpha_i$ è il valore atteso di $a_i$ ed $e_i$ è la componente casuale (errore stocastico) con valore atteso nullo. L'equazione può quindi essere riscritta come:
> $$r_i^e = \alpha_i + \beta_i r_m^e + e_i$$
>
> **Ipotesi del modello** (si aggiunge struttura alla rappresentazione statistica; nota: **non** si tratta di un modello di equilibrio):
> - Media del termine di errore: $E(e_i)=0$
> - Correlazioni nei termini di errore: la correlazione tra titoli passa esclusivamente attraverso il fattore, $E(e_ie_j)=0$ per $i\neq j$
> - Assenza di correlazione con il fattore di mercato: $E(e_i(r_m^e-E(r_m^e)))=0$
> - Per definizione: varianza di $e_i$, $\sigma_{e_i}^2=E(e_i^2)$; varianza di $r_m^e$, $\sigma_m^2=E\left[(r_m^e-E(r_m^e))^2\right]$

*(slide 11–14)*

## Single-index model: rendimento atteso, varianza e covarianza

> [!tip] Teorema
> **Rendimento atteso.** È composto da due parti:
> $$E(r_i^e) = \alpha_i + \beta_i E(r_m^e)$$
> con componente specifica $\alpha_i$ e componente sistematica $\beta_i E(r_m^e)$.
>
> **Varianza.** La varianza del rendimento del titolo $i$ è:
> $$\sigma_i^2 = \text{Var}(\alpha_i+\beta_i r_m^e+e_i) = \beta_i^2\sigma_m^2 + \sigma_{e_i}^2 + 2\beta_i\,\text{Cov}(r_m^e,e_i)$$
> Poiché $\text{Cov}(r_m^e,e_i)=0$, si ottiene:
> $$\sigma_i^2 = \beta_i^2\sigma_m^2 + \sigma_{e_i}^2$$
>
> **Covarianza.** La covarianza tra i rendimenti dei titoli $i$ e $j$, con $i\neq j$, è:
> $$\sigma_{ij} = \text{Cov}(\alpha_i+\beta_i r_m^e+e_i,\ \alpha_j+\beta_j r_m^e+e_j) = \beta_i\beta_j\text{Var}(r_m^e) + \beta_i\text{Cov}(r_m^e,e_j) + \beta_j\text{Cov}(r_m^e,e_i) + \text{Cov}(e_i,e_j)$$
> Per ipotesi, gli ultimi tre termini sono nulli, quindi:
> $$\sigma_{ij} = \beta_i\beta_j\sigma_m^2 \qquad (i\neq j)$$
>
> Questi risultati permettono di ricostruire l'intera matrice varianza–covarianza nel single-index model.

*(slide 15–16)*

## Costruzione della matrice varianza–covarianza nel single-index model

> [!tip] Teorema
> Unendo i risultati precedenti:
> - Elementi diagonali: $\Sigma_{ii} = \beta_i^2\sigma_m^2+\sigma_{e_i}^2$
> - Elementi fuori diagonale: $\Sigma_{ij} = \beta_i\beta_j\sigma_m^2$ per $i\neq j$
>
> In forma compatta:
> $$\Sigma = \sigma_m^2\,\beta\beta' + \text{diag}\left(\sigma_{e_1}^2,\dots,\sigma_{e_N}^2\right)$$
> dove $\beta = (\beta_1,\dots,\beta_N)'$.
>
> In forma estesa:
> $$\Sigma = \sigma_m^2 \begin{pmatrix} \beta_1^2 & \beta_1\beta_2 & \cdots & \beta_1\beta_N \\ \beta_2\beta_1 & \beta_2^2 & \cdots & \beta_2\beta_N \\ \vdots & \vdots & \ddots & \vdots \\ \beta_N\beta_1 & \beta_N\beta_2 & \cdots & \beta_N^2 \end{pmatrix} + \begin{pmatrix} \sigma_{e_1}^2 & 0 & \cdots & 0 \\ 0 & \sigma_{e_2}^2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \sigma_{e_N}^2 \end{pmatrix}$$
>
> **Interpretazione:**
> - $\sigma_m^2\beta\beta'$ rappresenta la covarianza comune legata al mercato;
> - $\text{diag}(\sigma_{e_i}^2)$ rappresenta il rischio specifico (assenza di covarianza tra titoli).
>
> Il risultato vale anche nel caso generale a un fattore, purché si mantengano le stesse ipotesi sulle correlazioni degli errori.

*(slide 17)*

## Numero di parametri: covarianza completa vs single-index model

**Matrice di covarianza completa (Markowitz):**
$$\frac{N(N-1)}{2}\text{ covarianze} + N\text{ varianze} + N\text{ rendimenti attesi} = \frac{N(N+3)}{2}$$
Ordine $O(N^2)$.

**Single-index model:**
$$N\text{ beta} + N\text{ varianze idios.} + 1\text{ varianza di mercato} + N\text{ rendimenti attesi} = 3N+1$$
Ordine $O(N)$.

Il single-index model riduce la dimensionalità da $O(N^2)$ a $O(N)$. Di conseguenza, fornisce una matrice $\Sigma$ che è tipicamente più stabile e meglio condizionata.

*(slide 18)*

## Single-index model e diversificazione

> [!note] Dimostrazione
> Si consideri un portafoglio ampio ed equipesato ($w_i=1/N$), il cui rendimento è:
> $$r_p^e = \sum_{i=1}^N w_i r_i^e = \sum_{i=1}^N w_i(\alpha_i+\beta_i r_m^e+e_i) = \sum_{i=1}^N w_i\alpha_i + \left(\sum_{i=1}^N \frac{1}{N}\beta_i\right) r_m^e + \sum_{i=1}^N \frac{1}{N}e_i$$
>
> Si ottiene quindi:
> $$r_p^e = \alpha_p + \beta_p r_m^e + e_p$$
> con
> $$\alpha_p = \sum_{i=1}^N \frac{1}{N}\alpha_i, \qquad \beta_p = \sum_{i=1}^N \frac{1}{N}\beta_i, \qquad e_p = \sum_{i=1}^N \frac{1}{N}e_i$$
>
> La varianza del portafoglio è $\sigma_p^2 = \beta_p^2\sigma_m^2 + \sigma_{e_p}^2$, dove:
> $$\sigma^2(e_p) = \sum_{i=1}^N \left(\frac{1}{N}\right)^2 \sigma^2(e_i) = \frac{1}{N}\bar\sigma^2(e)$$
>
> Poiché gli errori $e_i$ non sono correlati tra loro, se $N$ aumenta la componente di varianza idiosincratica tende a zero. La componente di rischio non diversificabile è quindi $\beta_p^2\sigma_m^2$.
>
> **Figura (pag. 20)** — Grafico di $\sigma_p^2$ in funzione del numero di titoli $N$ in portafoglio: la curva decresce da $\sigma^2(e_i)$ verso l'asintoto orizzontale $\beta_p^2\sigma_m^2$. L'area sopra l'asintoto rappresenta il *rischio diversificabile* (diversifiable risk), che si riduce all'aumentare di $N$; l'area sotto l'asintoto rappresenta il *rischio sistematico* (systematic risk), che resta costante. Conclusione: aumentando il numero di titoli in portafoglio, il rischio idiosincratico si annulla ma il rischio di mercato $\beta_p^2\sigma_m^2$ permane.

*(slide 19–20)*

## Fattori centrati

> [!abstract] Definizione
> Un fattore $f$ è **centrato** se $E[f]=0$. Dato un fattore con media $\mu_f=E[f]$, si definisce:
> $$\tilde f = f - \mu_f \qquad \Rightarrow \qquad E[\tilde f] = 0$$
>
> Nel modello a un fattore $r_i^e = \alpha_i+\beta_i f+e_i$, sostituendo $f=\tilde f+\mu_f$ si ottiene:
> $$r_i^e = (\alpha_i+\beta_i\mu_f)+\beta_i\tilde f+e_i = \tilde\alpha_i+\beta_i\tilde f+e_i$$
>
> Questa trasformazione modifica l'intercetta ma non altera $\beta_i$.
>
> **Perché centrare i fattori?**
>
> *Interpretazione in termini di shock:*
> - $f-E[f]$ isola la componente inattesa;
> - $\tilde f$ rappresenta lo shock del fattore;
> - i premi per il rischio compensano l'esposizione a tali movimenti inattesi.
>
> *Covarianze e scomposizione del rischio* — la covarianza non cambia con la trasformazione:
> $$\text{Cov}(r_i^e,f) = \text{Cov}(r_i^e,f-\mu_f)$$
> e i beta restano invariati:
> $$\beta_i = \frac{\text{Cov}(r_i^e,f)}{\text{Var}(f)} = \frac{\text{Cov}(r_i^e,\tilde f)}{\text{Var}(\tilde f)}$$
>
> *Interpretazione di asset pricing* (single-index model, CAPM): spesso si utilizza $f=r_m-r_f$ senza trasformarlo poiché $E[r_m-r_f]$ rappresenta il premio per il rischio di mercato. Mantenere il fattore non centrato rende immediata la relazione sui rendimenti attesi:
> $$E[r_i^e] = \alpha_i+\beta_i E[r_m-r_f]$$
> Se centrato, il premio per il rischio viene assorbito nell'intercetta.
>
> **Criterio operativo:**
> - si centrano i fattori per enfatizzare l'interpretazione in termini di shock;
> - non si centrano quando si vuole evidenziare il premio per il rischio (fattori traded).

*(slide 21–23)*

## Perché andare oltre il modello a un fattore?

Il single-index model riduce efficacemente la dimensionalità del problema:
$$\Sigma = \sigma_m^2\,\beta\beta' + \text{diag}(\sigma_{e_1}^2,\dots,\sigma_{e_N}^2)$$

Tuttavia, nei dati i titoli si muovono insieme per più di una ragione:
- settori (banche, utility, ecc.);
- stili di investimento (dimensione, value, momentum);
- shock macroeconomici (tassi, inflazione, cambi, materie prime).

Un solo fattore può lasciare **correlazione sezionale residua** nei termini $e_i$. Si passa dunque al modello **multifattoriale**.

*(slide 25)*

## Modello a due fattori: fattori non correlati e correlati

> [!example] Esempio
> **Caso: fattori non correlati (traded).** Si consideri un modello con due fattori: fattore di mercato $r_m^e$ e fattore di liquidità $r_l^e$:
> $$r_i^e = \alpha_i + \beta_{im}r_m^e + \beta_{il}r_l^e + e_i$$
> Ipotesi di base: $\text{Cov}(e_i,e_j)=0$ per $i\neq j$; $\text{Cov}(r_m^e,e_i)=\text{Cov}(r_l^e,e_i)=0$; fattori non correlati: $\text{Cov}(r_m^e,r_l^e)=0$.
>
> Varianza del titolo $i$:
> $$\text{Var}(r_i^e) = \beta_{im}^2\sigma_m^2 + \beta_{il}^2\sigma_l^2 + \sigma_{e_i}^2$$
> Covarianza tra i titoli $i$ e $j$:
> $$\text{Cov}(r_i^e,r_j^e) = \beta_{im}\beta_{jm}\sigma_m^2 + \beta_{il}\beta_{jl}\sigma_l^2$$
> La varianza riflette rischi sistematici indipendenti e rischio specifico; la covarianza tra titoli è interamente dovuta alle esposizioni ai fattori comuni.
>
> **Caso: fattori correlati.** Stesso modello, ma con $\text{Cov}(r_m^e,r_l^e)=\sigma_{ml}\neq 0$ (mantenendo le altre ipotesi). Varianza del titolo $i$:
> $$\text{Var}(r_i^e) = \beta_{im}^2\sigma_m^2 + \beta_{il}^2\sigma_l^2 + 2\beta_{im}\beta_{il}\sigma_{ml} + \sigma_{e_i}^2$$
> Covarianza tra i titoli $i$ e $j$:
> $$\text{Cov}(r_i^e,r_j^e) = \beta_{im}\beta_{jm}\sigma_m^2 + \beta_{il}\beta_{jl}\sigma_l^2 + (\beta_{im}\beta_{jl}+\beta_{il}\beta_{jm})\sigma_{ml}$$
> I termini di interazione riflettono la correlazione tra rischi sistematici: il rischio sistematico dipende sia dalle esposizioni ad esso sia dalla correlazione tra fattori.

*(slide 26–27)*

## Modello generale a K fattori

> [!abstract] Definizione
> Generalizzando il caso a due fattori, il modello con $K$ fattori è:
> $$r_i^e = \alpha_i + \beta_i' \mathbf{f} + e_i, \qquad \mathbf{f} = (f_1,\dots,f_K)'$$
>
> In forma matriciale:
> $$\mathbf{r}^e = \alpha + B\mathbf{f} + \mathbf{e}, \qquad B\in\mathbb{R}^{N\times K}$$
>
> Struttura della covarianza:
> $$\Sigma = B\Sigma_f B' + \Sigma_e, \qquad \Sigma_e = \text{diag}(\sigma_{e_1}^2,\dots,\sigma_{e_N}^2)$$
> dove $\Sigma_f = \text{Cov}(\mathbf{f})$ è la **matrice di covarianza fattoriale**, che riassume interamente il rischio sistematico.

*(slide 28)*

## Scomposizione della covarianza nel modello multifattoriale

> [!tip] Teorema
> $$\Sigma = B\Sigma_f B' + \Sigma_e$$
>
> - $B\Sigma_fB'$ ha rango al più pari a $K$: il rischio sistematico giace in un sottospazio di dimensione $K$ in $\mathbb{R}^N$; i titoli si muovono congiuntamente attraverso le esposizioni $\beta_i$.
> - $\Sigma_e$ è diagonale: il rischio idiosincratico è specifico del titolo e non genera covarianza tra titoli.
>
> **Interpretazione geometrica:** i rendimenti sono governati da $K$ fattori/direzioni comuni; la struttura impone una componente sistematica a rango ridotto. Se $K\ll N$, la maggior parte del co-movimento è spiegata da pochi fattori.
>
> **Varianza del titolo $i$:**
> $$\text{Var}(r_i^e) = \beta_i'\Sigma_f\beta_i + \sigma_{e_i}^2$$
>
> Se i fattori sono **non correlati**, $\Sigma_f$ è diagonale:
> $$\text{Var}(r_i^e) = \sum_{k=1}^K \beta_{ik}^2\,\text{Var}(f_k) + \sigma_{e_i}^2, \qquad \text{Cov}(r_i^e,r_j^e) = \sum_{k=1}^K \beta_{ik}\beta_{jk}\,\text{Var}(f_k)$$
>
> Se i fattori sono **correlati**:
> $$\text{Var}(r_i^e) = \sum_{k=1}^K \beta_{ik}^2\,\text{Var}(f_k) + \sum_{m\neq n}\beta_{im}\beta_{in}\,\text{Cov}(f_m,f_n) + \sigma_{e_i}^2$$
> $$\text{Cov}(r_i^e,r_j^e) = \sum_{k=1}^K \beta_{ik}\beta_{jk}\,\text{Var}(f_k) + \sum_{m=1}^K\sum_{\substack{n=1\\ n\neq m}}^K \beta_{im}\beta_{jn}\,\text{Cov}(f_m,f_n)$$
>
> Il rischio sistematico si comporta come un **portafoglio di fattori** con pesi pari ai beta.

*(slide 29–31)*

## Esempio numerico: scomposizione della covarianza a due fattori

> [!example] Esempio
> Modello:
> $$r_A^e = 0,02 + 2f_1 + 1f_2 + e_A$$
> $$r_B^e = 0,01 + 3f_1 + 2f_2 + e_B$$
>
> **Caso 1: fattori non correlati** — $\text{Cov}(f_1,f_2)=0$:
> $$\text{Cov}(r_A^e,r_B^e) = 6\sigma_1^2 + 2\sigma_2^2$$
>
> **Caso 2: fattori correlati** — $\text{Cov}(f_1,f_2)=\sigma_{12}$:
> $$\text{Cov}(r_A^e,r_B^e) = 6\sigma_1^2 + 2\sigma_2^2 + 7\sigma_{12}$$

*(slide 32)*

## Numero di parametri: covarianza completa vs modello a K fattori

**Matrice di covarianza completa (Markowitz):**
$$\frac{N(N-1)}{2}\text{ covarianze} + N\text{ varianze} + N\text{ rendimenti attesi} = \frac{N(N+3)}{2}, \qquad O(N^2)$$

**Modello a $K$ fattori con fattori non correlati:**
$$NK\text{ beta} + N\text{ varianze idios.} + K\text{ varianze dei fattori} + N\text{ rendimenti attesi} = N(K+2)+K, \qquad O(NK)$$

**Modello a $K$ fattori con fattori correlati:**
$$NK\text{ beta} + N\text{ varianze idios.} + \frac{K(K+1)}{2}\text{ elementi di }\Sigma_f + N\text{ rendimenti attesi} = N(K+2)+\frac{K(K+1)}{2}, \qquad O(NK+K^2)$$

Se $K\ll N$, la dimensionalità si riduce da $O(N^2)$ a circa $O(NK)$.

**Esempio numerico:**
- Covarianza completa, $N=500$: $\dfrac{500(503)}{2}=125.750$
- Modello a $K$ fattori non correlati, $N=500$, $K=5$: $500(7)+5=3.505$
- Modello a $K$ fattori correlati, $N=500$, $K=5$: $500(7)+\dfrac{5\cdot 6}{2}=3.515$
- Riduzione: $125.750 \to \approx 3.500$

*(slide 33–35)*

## Beta di portafoglio nei modelli fattoriali

> [!tip] Teorema
> Il rendimento in eccesso di un portafoglio in un modello multifattoriale è:
> $$r_p^e = \alpha_p + \beta_p'\mathbf{f} + e_p$$
> che deriva da $r_p^e = \sum_{i=1}^N w_i r_i^e$.
>
> I **beta di portafoglio** sono medie ponderate:
> $$\beta_{pk} = \sum_{i=1}^N w_i\beta_{ik}$$
>
> Con un modello lineare:
> - i beta di portafoglio sono medie ponderate dei beta individuali;
> - $E[r_p^e]$ è la media ponderata dei rendimenti attesi;
> - $e_p = \sum w_i e_i$.
>
> La struttura multifattoriale si preserva a livello di portafoglio.

*(slide 36)*

## Dalla teoria all'implementazione

Finora i modelli fattoriali sono stati utilizzati per semplificare la rappresentazione della struttura dei rendimenti e della matrice di covarianza. Resta da chiedersi come specificare e stimare i modelli fattoriali empiricamente.

**Idea chiave:**
- approccio economico e/o statistico per selezionare i fattori;
- i modelli fattoriali possono essere stimati tramite regressione lineare;
- i parametri sono tipicamente ottenuti tramite metodo dei minimi quadrati (OLS).

Si parte dal modello generale a $K$ fattori per poi concentrarsi sul single-index model.

*(slide 38)*

## Specificazione dei fattori

Andando oltre il single-index model, occorre identificare le fonti sistematiche di rischio nei modelli multifattoriali. Esempi:

- **Fattori macroeconomici** (Chen, Roll, Ross, 1986): produzione industriale; inflazione attesa/inattesa; term spread e default spread.
- **Fattori legati alle caratteristiche delle imprese** (ad esempio modello a tre fattori di Fama-French):
$$r_{it}^e = \alpha_i + \beta_{im}r_{mt}^e + \beta_{iSMB}SMB_t + \beta_{iHML}HML_t + e_{it}$$
  - SMB = Small minus Big (dimensione)
  - HML = High minus Low (rapporto valore contabile/prezzo)

**Panoramica sulla specificazione dei fattori:**

| Metodo | Vantaggi | Svantaggi |
|---|---|---|
| Analisi fattoriale | Tecnica puramente statistica, nessun fattore predeterminato | Fattori non unici, no interpretazione economica immediata |
| Variabili macroeconomiche | Utilizzo di serie storiche macro, interpretazione economica | Difficoltà di misurazione |
| Caratteristiche delle imprese | Utilizzo di caratteristiche come la dimensione per costruire portafogli, più intuitivo | Utilizza caratteristiche associate ad anomalie passate |

*(slide 39–40)*

## Estrazione statistica dei fattori: PCA e regolarizzazione

**Analisi delle componenti principali (PCA):**
- estrae la variazione comune direttamente da dati longitudinali su rendimenti;
- trova combinazioni lineari che spiegano la massima varianza;
- produce fattori statistici ortogonali;
- nessuna struttura economica imposta.

**Regolarizzazione** (ad esempio LASSO):
- seleziona un insieme sparso di regressori rilevanti;
- penalizza la complessità del modello;
- evita overfitting quando esistono molti fattori candidati ("zoo dei fattori").

**Figura (pag. 41)** — Illustrazione dello "zoo dei fattori": una serie di animali di dimensioni crescenti rappresenta metaforicamente la proliferazione di fattori candidati proposti in letteratura, motivando l'uso di tecniche di regolarizzazione per selezionare i regressori davvero rilevanti.

**Trade-off:** efficienza statistica vs. interpretabilità economica.

*(slide 41)*

## PCA sui rendimenti: costruzione statistica e interpretazione

Si osservano serie storiche dei rendimenti in eccesso di $N$ titoli:
$$\mathbf{r}^e = (r_1^e,\dots,r_N^e)'$$
Si calcola la matrice di covarianza $\Sigma = \text{Cov}(\mathbf{r}^e)$. La PCA **diagonalizza** $\Sigma$:
$$\Sigma = V\Lambda V'$$
dove le colonne di $V$ sono direzioni ortogonali nello spazio dei rendimenti (autovettori) e la matrice diagonale $\Lambda$ contiene la varianza spiegata lungo ciascuna direzione (autovalori).

**Intuizione geometrica:** i rendimenti formano una nube di punti in uno spazio a $N$ dimensioni; la PCA individua gli assi ortogonali di massima dispersione; le componenti sono ordinate per varianza spiegata; si considerano le prime $K$ componenti principali per ridurre la dimensione, con $K\ll N$.

**Figura (pag. 43)** — *Scree plot* della varianza spiegata (individuale e cumulata) dalle componenti principali estratte dai rendimenti mensili in eccesso dei titoli dell'S&P 500 dal 2016 in poi ($r_f$ dal sito di Kenneth French). La prima componente spiega da sola circa il 30% della varianza totale; le componenti successive contribuiscono in misura via via minore, con la varianza cumulata che raggiunge circa il 50% con le prime cinque componenti.

**Prima vs seconda componente principale:**
- Prima componente: $f_{1t}=v_1'r_t^e$ — direzione di massima variazione comune, spesso stesso segno (positivo) per la maggior parte dei titoli, economicamente simile a un fattore di mercato ampio.
- Seconda componente: $f_{2t}=v_2'r_t^e$ — ortogonale alla prima, spiega la maggiore variazione residua, spesso contrappone gruppi di titoli, può assomigliare a un portafoglio di "stile", settore, durata, ecc.

**Interpretazione:** la prima componente cattura il comovimento aggregato; la seconda cattura la struttura sezionale; le componenti successive spiegano dispersione progressivamente più idiosincratica.

**Figura (pag. 45)** — Serie storiche standardizzate delle prime cinque componenti principali (PC1–PC5) confrontate con i rendimenti standardizzati di SPY (l'ETF che replica l'S&P 500, SPDR S&P 500 ETF Trust). Il grafico mostra che una delle componenti (tipicamente la prima) segue da vicino l'andamento di SPY, confermando l'interpretazione della prima componente principale come un fattore di mercato ampio.

*(slide 42–45)*

## PCA vs fattori motivati economicamente

**Modelli fattoriali motivati economicamente:**
- fattori scelti sulla base della teoria o dell'evidenza empirica;
- esempi: mercato, "dimensione", "valore", momentum, liquidità;
- interpretazione chiara.

**Fattori PCA:**
- estratti sulla base delle proprietà statistiche dei rendimenti;
- massimizzano la varianza spiegata;
- nessuna interpretazione economica a priori.

**Differenze chiave:**
- nei modelli economici la struttura è imposta prima e poi stimata;
- nella PCA la struttura emerge dai dati;
- i fattori PCA possono cambiare tra campioni.

Entrambi gli approcci riducono $\Sigma$ a una struttura più trattabile.

*(slide 46)*

## Stima OLS di un modello a K fattori e del single-index model

> [!note] Dimostrazione
> **Modello a $K$ fattori.** Specificazione multifattoriale:
> $$r_{it}^e = \alpha_i + \beta_i'\mathbf{f}_t + e_{it}$$
> dove $\mathbf{f}_t$ è un vettore $K\times 1$ delle realizzazioni dei fattori e $\beta_i$ è il vettore $K\times 1$ delle esposizioni ai fattori.
>
> In forma matriciale (regressione su serie storiche): $\mathbf{r}_i^e = X\theta_i + \mathbf{e}_i$, con $X=[\mathbf{1},F]$. Lo **stimatore OLS** è:
> $$\hat\theta_i = (X'X)^{-1}X'\mathbf{r}_i^e$$
> con primo elemento $\hat\alpha_i$ ed elementi restanti $\hat\beta_i$.
>
> **Single-index model.** Specificazione: $r_{it}^e = \alpha_i+\beta_i r_{mt}^e+e_{it}$. Gli stimatori OLS sono:
> $$\hat\beta_i = \frac{\text{Cov}(r_i^e,r_m^e)}{\sigma_m^2} = \frac{\sum_{t=1}^T (r_{it}^e-\bar r_i^e)(r_{mt}^e-\bar r_m^e)}{\sum_{t=1}^T (r_{mt}^e-\bar r_m^e)^2}$$
> $$\hat\alpha_i = \bar r_i^e - \hat\beta_i\bar r_m^e$$
>
> Implicazione per il rendimento atteso (poiché $E[e_i]=0$):
> $$E[r_i^e] = \alpha_i + \beta_i E[r_m^e]$$

*(slide 47–48)*

## Esempio di stima OLS del single-index model

> [!example] Esempio
> **Setup.** Rendimenti mensili di JPMorgan Chase & Co. (JPM) vs. ETF su S&P 500 (SPY). La pendenza nel grafico di dispersione rappresenta $\hat\beta_{JPM}$. L'uso dei rendimenti in eccesso facilita l'interpretazione dei coefficienti.
>
> **Figura (pag. 49)** — Due grafici: (a) serie storiche dei rendimenti mensili di SPY e JPM sovrapposte nel tempo; (b) scatterplot dei rendimenti mensili di JPM contro SPY con retta di regressione. Il grafico mostra una relazione lineare positiva tra i rendimenti di JPM e quelli di mercato, con pendenza pari al beta stimato.
>
> **Risultati della regressione** per JPM e altre quattro grandi società (in parentesi le statistiche t):
>
> | | AAPL | JNJ | JPM | MSFT | XOM |
> |---|---|---|---|---|---|
> | $\hat\alpha_i$ | 0,0093 (1,61) | 0,0027 (0,66) | 0,0039 (0,86) | 0,0082 (1,94) | 0,0003 (0,04) |
> | $\hat\beta_i$ | 1,1279 (9,03) | 0,4857 (5,54) | 1,1213 (11,44) | 0,9012 (9,92) | 0,8591 (6,00) |
> | Osservazioni | 120 | 120 | 120 | 120 | 120 |
> | $R^2$ | 0,4086 | 0,2064 | 0,5257 | 0,4545 | 0,2336 |

*(slide 49–50)*

## Problemi nella stima dei beta e correzione di Blume

I coefficienti beta sono stimati tramite regressione, con conseguente termine di errore. Più il coefficiente si discosta da 1, maggiore è la probabilità di forti errori di stima. I coefficienti possono inoltre variare nel tempo. Empiricamente, il beta stimato si muove, in media, attorno a 1 (Blume, 1975).

**La tecnica di Blume.** Blume misura l'aggiustamento verso il beta medio di 1 e assume che gli aggiustamenti passati siano buoni proxy di quanto potrebbe accadere nel periodo successivo. Calcola il beta in due periodi diversi ($t_1$ e $t_2$) e regredisce il beta del primo periodo su quello del secondo, ottenendo una retta che misura la tendenza del beta a muoversi verso 1:
$$\beta_{i,2} = 0,67\,\beta_{i,1} + 0,33$$

**Esempio (schermata di Bloomberg).** Aggiustamento riportato nella schermata di Bloomberg per un titolo con beta grezzo (raw beta) pari a $0,743$:
$$\beta^{adj} = 0,67\cdot 0,743 + 0,33 = 0,828$$

**Figura (pag. 53)** — Schermata Bloomberg (Historical Beta) che mostra lo scatterplot del titolo rispetto all'indice S&P 500 con retta di regressione, il *raw beta* ($0,743$) e l'*adjusted beta* ($0,828$), insieme a statistiche quali R², errore standard, t-test e p-value. Illustra come Bloomberg applichi l'aggiustamento di Blume in automatico.

L'aggiustamento di Blume è di fatto una tecnica di **shrinkage** (si veda l'appendice sulla regolarizzazione).

*(slide 51–53)*

## Frontiera efficiente con modelli fattoriali: motivazione e scelta del modello

Si vogliono confrontare le frontiere efficienti ottenute sotto diverse ipotesi sulla matrice di covarianza, per valutare l'impatto della struttura del modello sulla costruzione del portafoglio.

**Benchmark:** approccio a covarianza completa (Markowitz) — si stima la matrice di covarianza campionaria completa $N\times N$; massima flessibilità, ma elevato errore di stima quando $N$ è grande rispetto a $T$.

**Domanda chiave:** imponendo una struttura fattoriale si migliora la stabilità e l'efficienza media-varianza (MV)?

**Scelta del modello fattoriale:**
- **Single-index model** — un fattore sistematico comune (il mercato); covarianza governata dall'esposizione al mercato; si assume che il rischio residuo sia idiosincratico.
- **Modelli multifattoriali** — diverse fonti di rischio sistematico, che catturano ad esempio rischi di stile, macro, settoriali. Due specificazioni:
  - *Fattori non correlati*: matrice di covarianza dei fattori diagonale $\Sigma_f$, assumendo separazione delle fonti di rischio sistematico;
  - *Fattori correlati*: matrice di covarianza dei fattori completa $\Sigma_f$, permettendo interazione tra i rischi sistematici.

*(slide 55–56)*

## Costruzione delle frontiere: esempio con cinque titoli

> [!example] Esempio
> Si considerano i cinque titoli visti in precedenza:
> - **AAPL** — Apple Inc. — elettronica di consumo / tecnologia
> - **JNJ** — Johnson & Johnson — prodotti farmaceutici / salute
> - **JPM** — JPMorgan Chase & Co. — banche / servizi finanziari
> - **MSFT** — Microsoft Corporation — software / cloud computing
> - **XOM** — Exxon Mobil Corporation — petrolio e gas / energia
>
> e i **fattori di Fama-French a tre fattori**: Mercato, HML, SMB.
>
> Si confrontano tre approcci: **Covarianza completa** (Markowitz) vs. **single-index model** (SIM) vs. **modello FF3 con fattori correlati** (FF3). Numero di parametri:
> $$\frac{N(N+3)}{2} = 20 \quad\text{vs.}\quad 3N+1 = 16 \quad\text{vs.}\quad N(K+2)+\frac{K(K+1)}{2} = 31$$
>
> Si stimano i beta usando rendimenti in eccesso basati su $r_f$ fornito da Fama-French.
>
> **Rendimento medio in eccesso** (rendimenti mensili, Markowitz):
>
> | | AAPL | MSFT | XOM | JPM | JNJ |
> |---|---|---|---|---|---|
> | Rendimento medio in eccesso | 2,21% | 1,84% | 1,00% | 1,66% | 0,82% |
>
> **Figura (pag. 58)** — Heatmap della matrice di correlazione completa (Markowitz) tra i cinque titoli, con valori numerici sovrapposti; mostra correlazioni positive più marcate tra alcune coppie (ad es. tecnologiche) rispetto ad altre.
>
> **Figura (pag. 59)** — Grafico rendimento medio vs deviazione standard che confronta le frontiere efficienti e le Capital Allocation Line (CAL) ottenute sotto Markowitz, SIM e FF3, insieme ai rispettivi portafogli GMVP e di tangenza. Le tre frontiere risultano molto simili nella parte centrale, con lievi divergenze verso destra (alta volatilità), a conferma che la struttura fattoriale approssima bene la frontiera a covarianza completa.

*(slide 57–59)*

## Confronto tra portafogli: Markowitz, SIM e FF3

> [!example] Esempio
> **Tabella — Confronto tra portafogli** (pesi, rendimento atteso, volatilità e Sharpe ratio di GMVP e portafoglio di Tangenza per ciascun modello):
>
> | Portafoglio | Markowitz GMVP | Markowitz Tangenza | SIM GMVP | SIM Tangenza | FF3 GMVP | FF3 Tangenza |
> |---|---|---|---|---|---|---|
> | AAPL | -1,69% | 20,29% | 0,52% | 27,99% | 4,09% | 21,99% |
> | MSFT | 35,09% | 38,07% | 26,41% | 45,21% | 32,87% | 41,27% |
> | XOM | 5,58% | 4,78% | 9,26% | -1,57% | 7,39% | 2,13% |
> | JPM | 7,51% | 18,28% | 10,47% | 9,56% | 5,90% | 19,66% |
> | JNJ | 53,51% | 18,58% | 53,33% | 18,81% | 49,74% | 14,95% |
> | $E(r_p)$ | 1,40% | 1,79% | 1,38% | 1,88% | 1,44% | 1,85% |
> | $\sigma_p$ | 3,95% | 4,57% | 4,14% | 4,94% | 4,11% | 4,81% |
> | $SR_p$ | 30,93% | 35,30% | 28,99% | 34,46% | 30,88% | 34,73% |
>
> **Interpretazione dei risultati.** Gli indici di Sharpe sono simili nei tre modelli: 35,30% (Markowitz), 34,46% (SIM), 34,73% (FF3) per il portafoglio di tangenza — la struttura fattoriale cattura la maggior parte del comovimento sistematico.
>
> Osservazioni principali:
> - Markowitz è il più flessibile;
> - i modelli fattoriali riducono la dimensione con impatto limitato sulla performance;
> - la struttura fattoriale comporta piccole perdite di efficienza a fronte di maggiore robustezza;
> - errori cumulativi nel modello di Markowitz possono portare a un portafoglio effettivamente inferiore rispetto a quello ottenuto con i modelli fattoriali.

*(slide 60–61)*

## Dai modelli fattoriali alle strategie smart beta

I modelli fattoriali scompongono i rendimenti in fattori sistematici (mercato, dimensione, valore, liquidità, ecc.) e rischio idiosincratico. L'evidenza empirica mostra che alcuni fattori sono associati a **premi per il rischio persistenti**.

Le **strategie smart beta** sono strategie di investimento progettate per:
- orientare intenzionalmente i portafogli verso fattori specifici;
- catturare i premi per il rischio dei fattori in modo trasparente e basato su regole precise.

In sintesi:
- indicizzazione tradizionale (beta tradizionale) $\to$ esposizione al fattore di mercato (o a un indice specifico);
- smart beta $\to$ esposizione mirata a uno o più fattori.

**Esempi di fattori smart beta:** Valore (titoli economici vs. titoli costosi), Dimensione (bassa vs. alta capitalizzazione), Momentum (vincitori passati vs. perdenti), ecc.

**Implementazione:** pesi di portafoglio determinati da caratteristiche fattoriali; ribilanciamento sistematico basato su procedure predeterminate.

**Collegamento ai modelli fattoriali:** i portafogli smart beta sono portafogli con beta intenzionalmente non nulli rispetto ai fattori selezionati; la performance può essere valutata con modelli multifattoriali.

*(slide 63–64)*

## Smart beta come esposizione mirata ai fattori: formalizzazione

> [!abstract] Definizione
> Rappresentazione multifattoriale dei rendimenti:
> $$r_i^e = \alpha_i + \beta_i'\mathbf{f} + e_i$$
> dove $\mathbf{f}$ è un vettore $K\times 1$ di fattori. Il rendimento atteso secondo il modello fattoriale è:
> $$E[r_i^e] = \alpha_i + \beta_i'\lambda$$
> dove $\lambda$ è il vettore dei premi per il rischio dei fattori (si veda la lezione su APT).
>
> Per un portafoglio con pesi $w$:
> $$r_p^e = w'\mathbf{r}^e = \alpha_p + \beta_p'\mathbf{f} + e_p, \qquad \text{con } \beta_p = w'B$$
>
> **Strategia smart beta:** scegliere $w$ in modo che $\beta_p$ sia orientato verso i fattori selezionati.
>
> **Costruzione di un portafoglio smart beta.** Obiettivo su un fattore specifico $k$:
> $$\max_w \beta_{p,k} \quad \text{sub} \quad \mathbf{1}'w=1$$
>
> Oppure ottimizzazione media–varianza con struttura fattoriale:
> $$\max_w w'B\lambda - \frac{\gamma}{2}w'\Sigma w, \qquad \text{con } \Sigma = B\Sigma_f B' + \Sigma_e$$
>
> **Esempio:** criterio basato su "valore" (value investing): $w_i \propto f(B/M_i)$, dove $B/M_i$ è il rapporto valore contabile/prezzo di mercato del titolo $i$.
>
> **Valutazione della performance** tramite regressione:
> $$r_p^e = \alpha_p + \beta_p'\mathbf{f} + e_p$$
> dove $\alpha_p$ misura la performance anomala e $\beta_p$ mostra le esposizioni ai fattori.

*(slide 65–66)*

## Smart beta nella pratica

> [!example] Esempio
> È possibile investire in ETF smart beta, ad esempio **VLUE** (iShares MSCI USA Value Factor ETF) e **VOOG** (Vanguard S&P 500 Growth Index Fund ETF).
>
> **Figura (pag. 67)** — Due grafici: (a) rendimenti cumulati di SPY, VLUE e VOOG nel tempo; (b) rendimenti mensili degli stessi tre strumenti. Mostrano come i due ETF smart beta (orientati rispettivamente al fattore valore e al fattore crescita) abbiano traiettorie di performance diverse tra loro e rispetto al benchmark di mercato SPY, illustrando concretamente l'esposizione mirata ai fattori.

*(slide 67)*

## Appendice — Regolarizzazione: il problema dell'overfitting

OLS minimizza l'errore di training, ma un modello che riproduce perfettamente i dati di training può comportarsi male su nuovi dati (**overfitting**). Due forze determinano l'errore di previsione su dati non osservati:

- **Bias**: errore dovuto all'approssimazione di una relazione complessa con un modello più semplice; meno variabili o shrinkage più forte $\Rightarrow$ bias più alto.
- **Varianza**: sensibilità delle stime al particolare campione di training; più variabili o predittori correlati $\Rightarrow$ varianza più alta.

Il trade-off bias–varianza è tale per cui:
$$\text{Errore di previsione atteso} = \underbrace{\text{Bias}^2}_{\text{troppo semplice}} + \underbrace{\text{Varianza}}_{\text{troppo complesso}} + \underbrace{\sigma_e^2}_{\text{irriducibile}}$$

La **regolarizzazione** introduce deliberatamente una piccola quantità di bias (vincolando $\beta$) in cambio di una forte riduzione della varianza, spesso migliorando la previsione al di fuori del campione (out of sample).

Ci possono essere molti fattori, alle volte altamente correlati; la regolarizzazione aiuta a prevenire modelli troppo complessi che fanno overfitting o diventano instabili. Introduce un vincolo sulla dimensione del vettore dei coefficienti $\beta$ quando si minimizza la somma dei quadrati degli errori:
$$\mathbf{e} = \mathbf{r}^e - \alpha - F\beta$$

La regressione regolarizzata risolve:
$$\min_\beta \mathbf{e}'\mathbf{e} \quad \text{sotto un vincolo su } \beta$$
per diverse scelte di vincolo: ridge (L2), LASSO (L1).

Poiché la regolarizzazione confronta la grandezza dei coefficienti, le variabili devono essere su scale confrontabili: è dunque necessario **standardizzare** i dati prima di applicare la regolarizzazione.

*(slide 69–70)*

## Appendice — Regressione ridge

> [!abstract] Definizione
> La regressione ridge impone un vincolo $L_2$ sul vettore dei coefficienti:
> $$\min_\beta \mathbf{e}'\mathbf{e} \quad \text{sub} \quad \|\beta\|_2 \le t$$
> Questa è la forma vincolata della regolarizzazione: i coefficienti sono vincolati a rimanere all'interno di un intorno circolare $L_2$ di raggio $t$ (norma euclidea).
>
> In alternativa, lo stesso problema può essere scritto in **forma lagrangiana** (con penalità):
> $$\min_\beta \mathbf{e}'\mathbf{e} + \lambda\|\beta\|_2^2$$
> dove $\lambda\ge 0$ controlla l'intensità della penalità. Esiste una corrispondenza biunivoca tra $t$ (ampiezza del vincolo) e $\lambda$ (intensità della penalità): $t$ più piccolo $\Leftrightarrow \lambda$ più grande; la corrispondenza esatta dipende dai dati e non è derivabile in forma chiusa. In pratica si usa la forma lagrangiana perché è più semplice per l'ottimizzazione numerica e per la validazione.
>
> **L'idea.** Con OLS si minimizza la somma dei quadrati dei residui:
> $$RSS = \sum_{t=1}^T \left(r_{it}^e - \alpha_i - \sum_{k=1}^K \beta_{ik}f_{kt}\right)^2$$
> Problema: OLS non impone vincoli sul valore assoluto dei coefficienti. Quando le variabili sono correlate, lo stimatore OLS sfrutta questa libertà e produce coefficienti grandi e instabili.
>
> L'intuizione ridge è aggiungere un costo per coefficienti grandi:
> $$\underbrace{\sum_{t=1}^T \left(r_{it}^e - \alpha_i - \sum_{k=1}^K \beta_{ik}f_{kt}\right)^2}_{\text{Fittare bene i dati}} + \underbrace{\lambda\sum_{k=1}^K \beta_{ik}^2}_{\text{Produrre coefficienti contenuti}}, \qquad \lambda\ge 0$$
> Il parametro $\lambda$ controlla la forza della penalità e si può interpretare come un vincolo di bilancio sui valori dei coefficienti.
>
> **Interpretazione del termine di penalità:**
> 1. *Penalità $\lambda\beta_k^2$*: ogni coefficiente $\beta_k$ contribuisce con $\lambda\beta_k^2$ al costo totale. Se $\beta_k=10$, il costo è $100\lambda$; se $\beta_k=1$, il costo è $\lambda$ $\Rightarrow$ i coefficienti grandi sono penalizzati molto più di quelli piccoli (crescita quadratica).
> 2. *Intercetta non penalizzata*: la penalità somma da $k=1$ a $K$; non include $\alpha$. Poiché l'intercetta sposta la previsione verso l'alto o verso il basso, penalizzarla introdurrebbe una distorsione non desiderabile nella media di $r_{it}^e$.

*(slide 71–73)*

## Appendice — Ridge: comportamento al variare di λ

> [!tip] Teorema
> $$\hat\beta^{ridge}(\lambda) = \arg\min_\beta \left\{ RSS + \lambda\sum_{k=1}^K \beta_k^2 \right\}$$
>
> **Caso 1: $\lambda=0$ (nessuna penalità).** La penalità scompare e si torna a OLS: $\hat\beta^{ridge}=\hat\beta^{OLS}$.
>
> **Caso 2: $\lambda\to\infty$ (penalità infinita).** La penalità domina e l'unico modo per mantenere finito il costo è $\hat\beta^{ridge}\to 0$: tutti i coefficienti vengono ridotti a zero.
>
> **Caso 3: $0<\lambda<\infty$ (intervallo utile).** Ridge bilancia capacità esplicativa e dimensione dei coefficienti: i coefficienti sono ridotti verso zero, ma non vengono portati esattamente a zero.
>
> $\lambda$ è un **iperparametro** scelto tramite cross-validazione: non viene mai stimato dai dati di training usati per determinare $\hat\beta$.

*(slide 74)*

## Appendice — Regressione LASSO e confronto con ridge

> [!abstract] Definizione
> **LASSO** è l'acronimo di *Least Absolute Shrinkage and Selection Operator*. Mentre ridge aggiunge alla funzione obiettivo OLS una costante moltiplicata per la somma dei coefficienti al quadrato, LASSO aggiunge una costante moltiplicata per la somma dei **valori assoluti** dei coefficienti. La regressione LASSO minimizza:
> $$\sum_{t=1}^T \left(r_{it}^e - \alpha_i - \sum_{k=1}^K \beta_{ik}f_{kt}\right)^2 + \lambda\sum_{k=1}^K |\beta_{ik}|$$
>
> Non esiste una soluzione in forma chiusa: si risolve numericamente (ad esempio con algoritmi di "coordinate descent"). LASSO è detto anche regolarizzazione $L_1$ perché usa la norma $L_1$ (valore assoluto):
> $$\|\beta_i\|_1 = |\beta_{i1}| + \cdots + |\beta_{iK}|$$
>
> LASSO tende a portare esattamente a zero i coefficienti delle variabili trascurabili, esercitando di fatto una **selezione delle variabili**. La regressione ridge riduce i coefficienti ma di solito non li azzera. Con molte variabili, LASSO può identificare un sottoinsieme più piccolo e più interpretabile di predittori per il modello.
>
> **Riepilogo: ridge vs. LASSO**
>
> | | Ridge (L2) | LASSO (L1) |
> |---|---|---|
> | Termine di penalità | $\lambda\sum\beta_j^2$ | $\lambda\sum\lvert\beta_j\rvert$ |
> | Forma del vincolo | Cerchio | Rombo |
> | Forma chiusa | Sì | No (coordinate descent) |
> | Coefficienti | Ridotti, mai a zero | Ridotti, possono essere zero |
> | Selezione variabili | No | Sì |
> | Ideale per... Ridge | Molti fattori correlati, tutti potenzialmente rilevanti | |
> | Ideale per... LASSO | | Molti fattori, solo pochi veramente importanti |
>
> Ridge riduce tutto in modo proporzionale; LASSO applica una trasformazione che può portare i coefficienti meno rilevanti esattamente a zero.

*(slide 75–77)*
