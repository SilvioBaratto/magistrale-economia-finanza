---
title: "Le ipotesi della Modern Portfolio Theory (versione base)"
tags:
  - corso/metodi-portafogli
  - tipo/lezione
corso: "[[Metodi Portafogli]]"
source: "MGPP_Slide_Nota-sulle-ipotesi.pdf"
pages: 3
text_layer: true
verified: true
generated: 2026-07-10
---

## Introduzione

*A cura di Marco Corazza, Dipartimento di Economia, Università Ca' Foscari Venezia.*

Questa nota presenta e commenta brevemente le ipotesi sulle quali si fonda la versione base del modello di selezione (statica) della **Modern Portfolio Theory (MPT)**, cioè quella versione che permette le vendite allo scoperto delle attività finanziarie. Si tratta di ipotesi concettualmente non difficili da comprendere, anche se, in linea generale, non tutte risultano particolarmente realistiche.

*(slide 1)*

## Le sei ipotesi del modello base

> [!abstract] Definizione
> - **Ipotesi 1**: Non esistono costi associati all'acquisto ed alla vendita delle attività finanziarie;
> - **Ipotesi 2**: Non esiste tassazione sui guadagni derivanti dall'acquisto e dalla vendita delle attività finanziarie;
> - **Ipotesi 3**: Ogni attività rischiosa è perfettamente divisibile;
> - **Ipotesi 4**: Sono ammesse le vendite allo scoperto di ogni attività rischiosa;
> - **Ipotesi 5**: Gli agenti economici conoscono i momenti primi ed i momenti secondi dei rendimenti di ogni attività finanziaria;
> - **Ipotesi 6**: Le azioni degli agenti economici di acquisto e di vendita delle attività finanziarie non influenzano le distribuzioni di probabilità dei rendimenti delle attività finanziarie.

*(slide 1)*

## Ipotesi 1-3: il "mercato privo di frizioni"

Le ipotesi 1, 2 e 3 sono congiuntamente note come ipotesi del **"mercato privo di frizioni"**. È quasi superfluo porre in evidenza il loro poco realismo, in particolare delle ipotesi 1 e 2.

Comunque, è da porre in evidenza che negli ultimi decenni la possibilità di poter effettuare investimenti mediante intermediari operanti su Internet ha ridotto di molto almeno i costi associati all'acquisto/alla vendita delle attività finanziarie, spesso avvicinandoli allo zero.

Per quanto riguarda l'ipotesi 3, di fatto non è sempre possibile acquistare/vendere quantità a piacere di attività finanziarie, ad esempio frazioni di una attività. Infatti, in generale è possibile acquistare/vendere solo numeri interi di lotti di attività finanziarie costituiti a loro volta da un prefissato numero intero delle medesime attività (con linguaggio tecnico si dice "**lotto minimo**"). Ad esempio, il lotto minimo di molte azioni trattate nel mercato azionario italiano è costituito da una sola azione (ma non meno).

Si osserva che qualificare come frizioni — cioè come elementi tralasciabili se opportunamente trattati — aspetti che invece sono generalmente strutturali in ambito economico, può portare a sottovalutare pericolosamente l'impatto di questi stessi elementi sul processo di selezione (statica) di portafoglio.

*(slide 1)*

## Ipotesi 4: assenza di restrizioni istituzionali

L'ipotesi 4 è nota come ipotesi dell'**"assenza di restrizioni istituzionali"**. Generalmente questa ipotesi può risultare realistica in quanto in molti mercati finanziari sono permesse le vendite allo scoperto delle attività finanziarie.

È solo da porre in evidenza che, in alcuni periodi di particolare tensione economica e/o finanziaria, le varie Autorità nazionali per la vigilanza dei mercati finanziari (ad esempio la CONSOB per l'Italia, il Bundesanstalt für Finanzdienstungsaufsicht per la Germania, la SEC per gli Stati Uniti d'America, ...) possono sospendere la possibilità di vendere allo scoperto.

*(slide 2)*

## Ipotesi 5: conoscenza dei momenti primi e secondi dei rendimenti

Le ipotesi 5 e 6 sono relative al comportamento degli agenti economici che acquistano e/o vendono attività finanziarie, cioè gli investitori. L'ipotesi 5 è meno innocua di quanto possa sembrare, per almeno i seguenti motivi:

- Intanto, l'ipotesi 5 presuppone implicitamente anche che le distribuzioni di probabilità dei rendimenti delle attività finanziarie siano pienamente descritte solo dai loro momenti primo e secondo, cioè, in altri termini, che queste distribuzioni siano asimmetriche e normocurtiche. Un naturale candidato per tale tipologia di distribuzioni è la gaussiana;
- Poi, è da porre in evidenza che conoscere i momenti primi ed i momenti secondi dei rendimenti di ogni attività finanziaria vuol dire conoscere, oltre che la media e la varianza dei vari rendimenti, anche tutte le covarianze fra tali rendimenti, in quanto anche queste ultime sono momenti secondi (misti, per la precisione);
- Ancora, gli agenti economici non potranno mai conoscere i "veri" momenti primi e secondi delle attività finanziarie. Piuttosto, dovranno accontentarsi di qualche loro stima, la qual cosa implica che gli agenti economici posseggano risorse sufficienti per effettuare tali stime;
- Infine, l'ipotesi 5 presuppone implicitamente che esistano il momento primo ed il momento secondo di ogni attività finanziaria. Quest'assunzione implicita non è poi così scontata. Infatti, nell'ambito della finanza quantitativa i rendimenti delle attività finanziarie sono frequentemente modellizzati mediante distribuzioni di probabilità il cui momento secondo non è finito e quindi non esiste. Ad esempio, questo è il caso delle distribuzioni di probabilità **Pareto-Lévy stabili**.

*(slide 2)*

## Ipotesi 6: l'investitore price-taker

Quest'ultima ipotesi è nota come ipotesi dell'**"investitore price-taker"**. Essa sostanzialmente afferma che le quantità di attività finanziarie acquistate/vendute dagli investitori sono così piccole da non poter influenzare i prezzi di queste stesse attività — e quindi i rendimenti che dei prezzi sono funzione. In altri termini, l'ipotesi 6 afferma che tutti gli investitori coinvolti nelle attività di acquisto/vendita sono piccoli investitori.

Anche questa ipotesi, come le ipotesi 1, 2 e 3, è poco realistica data la costante presenza nei mercati finanziari di investitori di medie e di grandi dimensioni che sono piuttosto "**investitori price-maker**", ovvero in grado di influenzare i prezzi mediante l'acquisto/la vendita di grandi quantità di attività finanziarie.

*(slide 2)*

## Riferimenti bibliografici

Alcuni riferimenti bibliografici per approfondimenti su quanto sopra sono [Elton et al., 2007] e [Merton, 1992].

**Riferimenti**

- [Barucci, 2003] Barucci E. (2003): *Financial markets theory. Equilibrium, efficiency, information*. Springer.
- [Elton et al., 2007] Elton E. J., Gruber M. J., Brown S. J., Goetzmann (2007): *Teorie di portafoglio e analisi degli investimenti*. Apogeo.
- [Merton, 1992] Merton R. C. (1992): *Continuous-time finance*. Wiley-Blackwell.
- [Piccolo e Vitale, 1984] Piccolo D., Vitale C. (1984): *Metodi statistici per l'analisi economica*. Il Mulino.

*(slide 3)*
