# Legislazione Bancaria 2 (EM2101) — tracce per la prova orale

Domande d'esame e risposte da esporre a voce, sui **punti 8-11** del programma, cioè la
**seconda prova** orale. Un PDF per sezione più il volume unico.

Il modulo 1 (punti 1-7) sta in `../legislazione-bancaria-1/`. I sorgenti stanno
qui; i PDF escono in `esami/legislazione-bancaria-2/` alla radice del repository.

## Perché queste tracce sono fatte così

Il programma ufficiale (AF 728602, ultima modifica 01/04/2026) dice:

> La verifica dell'apprendimento avviene attraverso una prova finale esclusivamente orale
> volta ad accertare la conoscenza e la comprensione degli argomenti oggetto del programma,
> la capacità di esporli in maniera appropriata, nonché l'attitudine a consultare le fonti
> normative.

Tre criteri, e ognuno ha lasciato un segno nella struttura delle risposte. *Conoscenza e
comprensione* → ogni argomento del materiale ha almeno una domanda. *Capacità di esporli in
maniera appropriata* → le risposte sono scritte in prosa discorsiva, come si parla, non come
si prendono appunti. *Attitudine a consultare le fonti normative* → ogni risposta finisce con
gli articoli da citare, e ogni articolo è stato verificato sul testo della norma.

La graduazione dei voti aggiunge, per la fascia 27-30 e per la lode, la «capacità di
raccogliere e interpretare i dati formulando giudizi autonomi». Di qui i riquadri *Attenzione*
(la distinzione che il docente pretende, l'errore che fa perdere punti) e i *Rilanci* (le
domande di approfondimento che si innestano sulla risposta).

## Vincolo temporale sulla seconda prova

Chi ha superato la prova intermedia sui punti 1-7 può completare l'esame sulla parte rimanente
**solo al primo o al secondo appello della sessione invernale**. Oltre quel termine si rifà
tutto l'esame, orale, su tutti e undici i punti. È il motivo per cui conviene che le due
cartelle dei due moduli siano allineate e utilizzabili insieme.

## Che cosa c'è

| PDF | Punto | Domande | Pagine |
|---|---|---|---|
| `LEGB2_Orale_01_Basilea-e-Quadro-Prudenziale.pdf` | premessa all'8 | 8 | 12 |
| `LEGB2_Orale_02_Vigilanza-Informativa.pdf` | 8 | 8 | 11 |
| `LEGB2_Orale_03_Centrale-Rischi-e-Giurisprudenza.pdf` | 8 | 8 | 13 |
| `LEGB2_Orale_04_Adeguatezza-Patrimoniale-e-Rischi.pdf` | 8 | 8 | 13 |
| `LEGB2_Orale_05_Partecipazioni-Detenibili.pdf` | 8 | 7 | 13 |
| `LEGB2_Orale_06_Governo-Societario-e-Controlli.pdf` | 8 | 9 | 14 |
| `LEGB2_Orale_07_Poteri-di-Intervento.pdf` | 8 | 7 | 11 |
| `LEGB2_Orale_08_Vigilanza-Ispettiva.pdf` | 8 | 7 | 11 |
| `LEGB2_Orale_09_Disciplina-Sanzionatoria.pdf` | 8 | 7 | 11 |
| `LEGB2_Orale_10_Concorrenza-e-Altre-Vigilanze.pdf` | 9 | 8 | 12 |
| `LEGB2_Orale_11_Gruppi-e-Vigilanza-Consolidata.pdf` | 10 | 8 | 14 |
| `LEGB2_Orale_12_Crisi-Amministrazione-Straordinaria-e-LCA.pdf` | 11 | 8 | 14 |
| `LEGB2_Orale_13_Risoluzione-e-BRRD.pdf` | 11 | 7 | 13 |
| **`LEGB2_Orale_Completo.pdf`** | **8-11** | **100** | **141** |

Il punto 8 è diviso in otto sezioni perché è il più esteso del programma: vi confluiscono la
cornice di Basilea, le tre forme di vigilanza, i poteri di intervento e l'apparato
sanzionatorio.

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

- Le note del vault, `../../../obsidian/04-Legislazione-Bancaria-2/` — 12 note generate dalla
  `pipeline` dagli appunti di lezione.
- Le fonti normative, lette nel testo quando `../Normativa/` era ancora nel repository: TUB consolidato al 22.01.2026, CRR,
  CRD IV/V, Reg. (UE) n. 1024/2013, Circolari Banca d'Italia 115, 139, 154, 229, 262, 263,
  269, 272, 285 e 302, d.l. 99/2017, provvedimenti su sanzioni e piani di risanamento.
- Le slide in `.ppt`/`.pptx` che la `pipeline` non processa (Crisi bancarie Aloia-Spina,
  Ca' Foscari 2022, Anna Scarpa, Camillo La Gioia): estratte a parte.
- Le due sentenze sulla Centrale dei Rischi, allora in `../Casi-Giurisprudenza/`, che sono scansioni
  senza livello di testo e sono state **lette pagina per pagina**, non dedotte.

**Ogni articolo, soglia, percentuale e data citati sono stati verificati sul testo della
norma**, non ripresi dal materiale didattico. Non è pedanteria: in più punti il materiale del
corso è superato dalla normativa vigente, e le tracce lo segnalano invece di propagarlo —
l'art. 54 TUB nella versione anteriore al d.lgs. 182/2021, per fare un esempio, che gli
appunti e la stessa Circolare 285 riportano ancora nella formulazione vecchia.

## Che cosa non copre

- **I manuali.** Il programma indica pagine precise di CAPRIGLIONE (a cura di), *Manuale di
  diritto bancario e finanziario*, 3a ed. 2024, **oppure** di BRESCIA MORRA, *Il diritto delle
  banche*, 4a ed. 2025. Nessuno dei due è nel repository: queste tracce **non li sostituiscono**
  e nessuna affermazione è loro attribuita. Il programma indica per i punti 8-11 le pp. 144-149,
  160-185, 415-421, 499-524, 525-566 di Capriglione (per le sole parti sulle banche) oppure le
  pp. 141-167, 225-227, 231-271, 284-336 di Brescia Morra.
- `LEGB2_Normativa_TUB-2007-ridotto.pdf`, tenuto come riferimento storico, e la versione
  inglese delle slide per studenti, che duplica quella italiana.

## Ricompilare

Dalla cartella `latex/`, con lo stesso template e gli stessi filtri delle dispense
(`template/dispensa.latex`, `filters/esami.lua`, `filters/callouts.lua`):

```bash
python3 verifica_orale.py --corso legislazione-bancaria-2 --rinumera   # formato e completezza
python3 build_esami.py --corso legislazione-bancaria-2 --list          # che cosa c'è e quante domande
python3 build_esami.py --corso legislazione-bancaria-2 --all           # un PDF per sezione
python3 build_esami.py --corso legislazione-bancaria-2 --volume        # il volume unico
python3 build_esami.py --corso legislazione-bancaria-2 --exam 05       # una sola sezione
python3 build_esami.py --corso legislazione-bancaria-2 --all --keep    # conserva i .tex per il debug
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
