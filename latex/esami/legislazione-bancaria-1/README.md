# Legislazione Bancaria 1 (EM2101) — tracce per la prova orale

Domande d'esame e risposte da esporre a voce, sui **punti 1-7** del programma, cioè la
**prova intermedia** orale. Un PDF per sezione più il volume unico.

Il modulo 2 (punti 8-11) sta in `../legislazione-bancaria-2/`. I sorgenti stanno
qui; i PDF escono in `esami/legislazione-bancaria-1/` alla radice del repository.

## Perché queste tracce sono fatte così

Il programma ufficiale (AF 728603, ultima modifica 14/07/2026) dice:

> La verifica dell'apprendimento avviene attraverso una prova finale esclusivamente orale
> volta ad accertare la conoscenza e la comprensione degli argomenti oggetto del programma,
> la capacità di esporli in maniera appropriata, nonché l'attitudine a consultare le fonti
> normative.

Tre criteri, e ognuno ha lasciato un segno nella struttura delle risposte. *Conoscenza e
comprensione* → ogni argomento del materiale ha almeno una domanda. *Capacità di esporli in
maniera appropriata* → le risposte sono scritte in prosa discorsiva, come si parla, non come si
prendono appunti. *Attitudine a consultare le fonti normative* → ogni risposta finisce con gli
articoli da citare, e ogni articolo è stato verificato sul testo della norma.

La graduazione dei voti aggiunge, per la fascia 27-30 e per la lode, la «capacità di raccogliere
e interpretare i dati formulando giudizi autonomi». Di qui i riquadri *Attenzione* (la
distinzione che il docente pretende, l'errore che fa perdere punti) e i *Rilanci* (le domande di
approfondimento che si innestano sulla risposta).

## Il vincolo che rende utile questa cartella

Chi supera la prova intermedia può completare l'esame sui punti 8-11 **solo al primo o al
secondo appello della sessione invernale**. Chi non la supera rifà tutto l'esame, orale, su tutti
e undici i punti. La prova intermedia non è quindi un anticipo facoltativo: è la scelta che
decide quanto programma si porterà all'orale finale.

## Che cosa c'è

| PDF | Punto | Domande | Pagine |
|---|---|---|---|
| `LEGB1_Orale_01_Evoluzione-Storica-e-Fonti.pdf` | 1 | 8 | 12 |
| `LEGB1_Orale_02_Autorita-Creditizie.pdf` | 2 | 8 | 13 |
| `LEGB1_Orale_03_Unione-Bancaria-e-SSM.pdf` | 2 | 9 | 14 |
| `LEGB1_Orale_04_Attivita-e-Soggetti.pdf` | 3 | 9 | 14 |
| `LEGB1_Orale_05_Accesso-al-Mercato.pdf` | 4 | 12 | 16 |
| `LEGB1_Orale_06_Assetti-Proprietari.pdf` | 5 | 10 | 15 |
| `LEGB1_Orale_07_Esponenti-Aziendali.pdf` | 6 | 9 | 15 |
| `LEGB1_Orale_08_Banche-Popolari.pdf` | 7 | 9 | 14 |
| `LEGB1_Orale_09_BCC-e-Gruppo-Cooperativo.pdf` | 7 | 9 | 14 |
| `LEGB1_Orale_10_Abusivismo-e-Giurisprudenza.pdf` | 3 e 7 | 9 | 14 |
| `LEGB1_Orale_11_Temi-Trasversali.pdf` | 1-7 | 8 | 12 |
| **`LEGB1_Orale_Completo.pdf`** | **1-7** | **100** | **135** |

Il punto 2 è diviso in due sezioni (autorità nazionali, Unione Bancaria) e il punto 7 in altre
due (banche popolari, BCC), perché in entrambi i casi le due metà hanno fonti e logiche distinte.
La sezione 10 raccoglie l'abusivismo e la giurisprudenza del corso, che il programma distribuisce
fra i punti 3 e 7. La sezione 11 è la rete di sicurezza: FinTech, seminari, e gli argomenti che
non hanno una collocazione propria altrove.

## Com'è fatta ogni domanda

Tre blocchi, ciascuno con la sua testa nel PDF:

| Blocco | Callout nel sorgente | Che cosa contiene |
|---|---|---|
| **Domanda** | `> [!question] Domanda` | come la porrebbe il docente, in una o due frasi |
| **Risposta da dare** | `> [!success] Risposta da dare` | le prime frasi da pronunciare: definizione o tesi centrale, già ancorata all'articolo. È quello che salva i primi trenta secondi |
| **Spiegazione** | `> [!info] Spiegazione` | 250-600 parole di prosa, quella che si espone in due-quattro minuti, con gli articoli citati nel corpo del discorso |

`verifica_orale.py` segnala ogni domanda a cui manca uno dei tre blocchi.

Questa è la **versione da studiare**: cento domande per modulo, la domanda, la risposta da
dare e la sua spiegazione, nient'altro. I riquadri *Fonti da citare*, *Attenzione* e *Rilancio* della versione
estesa sono stati tolti per far stare il volume in un numero di pagine leggibile.

## La versione estesa

Le tracce integrali — tutte le domande di ogni sezione, con *Fonti da citare*, *Attenzione* e
*Rilancio* — restano nei sorgenti in `src-completo/`. Non sono compilate in PDF. Usano il
formato precedente (la risposta breve si chiama *Attacco* e la spiegazione non ha un blocco
proprio): per tornare alla versione lunga va sostituito il contenuto di `src/` con quello di
`src-completo/`, avvolta la prosa di ogni domanda in un callout `> [!info] Spiegazione` e
ricompilato. `.bozze-precedenti/` conserva le bozze di lavorazione anteriori.

## Su che cosa sono costruite

- Le note del vault, `../../../obsidian/03-Legislazione-Bancaria-1/` — 9 note generate dalla
  `pipeline` dagli appunti di lezione.
- Le fonti normative, lette nel testo quando `../Normativa/` era ancora nel repository: TUB consolidato al 22.01.2026,
  Circolari Banca d'Italia 229 e 285, Reg. (UE) n. 1024/2013, D.M. 169/2020, d.lgs. 208/2025,
  d.l. 3/2015 e d.l. 18/2016, provvedimenti Banca d'Italia, Bollettini di Vigilanza, artt. 41,
  47 e 117 Cost.
- Le slide in `.ppt`/`.pptx` che la `pipeline` non processa (Morassut sulle popolari, Banking
  Union/SSM, Pistritto, zona di competenza territoriale delle BCC): estratte a parte.
- Le sentenze allora in `../Casi-Giurisprudenza/` — Romanelli (Tribunale, Appello, Cassazione 2009) e
  Giuffrè (Tribunale, Appello) — che sono scansioni senza livello di testo e sono state **lette
  pagina per pagina**, non dedotte.

**Ogni articolo, soglia, percentuale e data citati sono stati verificati sul testo della norma**,
non ripresi dal materiale didattico. Il caso che mostra perché: la soglia dell'attivo oltre la
quale una banca popolare deve trasformarsi in s.p.a. è oggi di **sedici** miliardi (art. 18,
comma 1, l. 5 marzo 2024, n. 21), ma gli appunti, le slide **e la stessa Circolare 285 al 50°
aggiornamento** riportano ancora otto. Le tracce citano la cifra vigente e segnalano il
disallineamento fra norma primaria e secondaria — che all'orale vale come esercizio di
consultazione delle fonti, uno dei tre criteri espliciti del programma.

## Che cosa non copre

- **I manuali.** Il programma indica pagine precise di CAPRIGLIONE (a cura di), *Manuale di
  diritto bancario e finanziario*, 3a ed. 2024, **oppure** di BRESCIA MORRA, *Il diritto delle
  banche*, 4a ed. 2025. Nessuno dei due è nel repository: queste tracce **non li sostituiscono**
  e nessuna affermazione è loro attribuita. Per i punti 1-7 il programma indica le pp. 3-56,
  62-75, 87-98, 107-125, 127-144, 149-160, 205-239, 383-414, 423-436 di Capriglione oppure le
  pp. 21-53, 56-81, 83-84, 88, 113-140, 167-203, 205-225, 227-231 di Brescia Morra.
- **Le registrazioni delle lezioni.** L'audio del 3 ottobre 2025 e la sua trascrizione
  automatica non sono mai stati riversati in queste tracce, e non sono più nel repository.
- Le versioni superate del TUB tenute come riferimento storico (`TUB-2007-03-01_Libretto.tif`,
  `TUB-2025-03.pdf`), rimpiazzate dal consolidato al 22.01.2026.
- `LEGB1_Normativa_RegUE1024-2013_agg-2025-09-23.pdf` non ha livello di testo: è uno "stampa su
  PDF" da immagine. Il Regolamento MVU è stato verificato sull'altra copia, che ha lo stesso
  testo e la stessa numerazione degli articoli.

## Ricompilare

Dalla cartella `latex/`, con lo stesso template e gli stessi filtri delle dispense
(`template/dispensa.latex`, `filters/esami.lua`, `filters/callouts.lua`):

```bash
python3 verifica_orale.py --corso legislazione-bancaria-1 --rinumera   # formato e completezza
python3 build_esami.py --corso legislazione-bancaria-1 --list          # che cosa c'è e quante domande
python3 build_esami.py --corso legislazione-bancaria-1 --all           # un PDF per sezione
python3 build_esami.py --corso legislazione-bancaria-1 --volume        # il volume unico
python3 build_esami.py --corso legislazione-bancaria-1 --exam 05       # una sola sezione
python3 build_esami.py --corso legislazione-bancaria-1 --all --keep    # conserva i .tex per il debug
```

Servono `pandoc`, `xelatex` e `latexmk` (TeX Live). Le tracce compilate stanno in `src/`; le
versioni integrali, non compilate, in `src-completo/`.

`verifica_orale.py` controlla due cose. Il **formato**, cioè quello che romperebbe la compilazione:
front matter, una sola intestazione di capitolo, domande numerate in sequenza, callout con riga
vuota prima e dopo, niente intestazioni di livello 3 o wikilink. E la **completezza**: confronta
ogni sorgente con la bozza corrispondente in `.bozze/` e segnala `TRONCATO` se ha perso domande.
Il secondo controllo esiste perché è un guasto che non si vede: un file troncato compila
benissimo e produce un PDF dall'aria perfetta con metà del contenuto.

## Avvertenza

Preparazione personale a fini di studio. Non è materiale ufficiale del docente e non è stata
verificata da lui. Le fonti normative vanno sempre ricontrollate nella versione vigente al
momento dell'esame: il diritto bancario cambia spesso, e queste tracce fotografano il TUB al
22 gennaio 2026.
