# Test di ingresso EMR20 — domande e soluzioni

La banca di **647 domande a risposta multipla** della prova di verifica della personale
preparazione (Laurea magistrale in Economia e Finanza, EMR20), composta con lo stesso
template delle dispense. Due PDF, in `esami/test-ingresso/` alla radice del repository:

| PDF | Che cosa | Pagine |
|---|---|---|
| `EMR20_Prereq_Test-Completo_Esame.pdf` | solo le domande, quattro alternative ciascuna | 141 |
| `EMR20_Prereq_Test-Completo_Soluzioni.pdf` | risposta corretta evidenziata, spiegazione, chiave delle risposte per materia | 215 |

## Sorgenti

I sorgenti Markdown (`EMR20_Prereq_Test-Completo_{Esame,Soluzioni}.md`) stanno nella
raccolta originale, fuori da questo repository: qui ci sono solo i PDF. Copiati in
`Moodle/00-Test-di-Ingresso/` alla radice del repository, si ricompilano con:

```bash
python3 build_esami.py --corso test-ingresso --all
```

`quiz_markdown()` in `build_esami.py` adatta il formato della banca alla pipeline:

| Nel sorgente | Nel PDF |
|---|---|
| `## Materia N: ...` | capitolo |
| `### argomento` | sezione |
| `**N.** domanda` + `- a) ...` … `- d) ...` | blocco domanda, numero in blu, opzioni a)–d) mai spezzate fra due pagine |
| opzione con ✅ | opzione in blu neretto con ✓ |
| `> **Risposta: X.** ...` | blocco *Risposta: X.* |
| `Chiave rapida: 1=B · 2=B · ...` | sezione non numerata *Chiave delle risposte*, griglia a 10 colonne |

Titolo, indice e totale in testa ai file sono sostituiti da frontespizio e indice del PDF.
Le etichette ripetute nel testo di alcune opzioni (`a) A) ...`) vengono tolte; i pedici
scritti alla TeX fuori dalle formule (`t_{n−1}`) diventano pedici veri. Una riga che non
rientra in nessuna di queste forme interrompe il build con il numero di riga.

`macros.tex` contiene l'unica differenza di impaginazione rispetto agli altri corsi: il
blocco domanda non si spezza fra due pagine. Non c'è volume unico: domande e soluzioni sono
già due raccolte complete.
