# Struttura delle tabelle

La cartella `tables/` è organizzata esclusivamente per **bioma/ambiente**. La struttura non cambia in base al gioco, manuale o supplemento da cui proviene il contenuto.

Ogni bioma può contenere quattro famiglie standard di tabelle:

- `<bioma>_mostri.json`
- `<bioma>_png.json`
- `<bioma>_eventi_divini.json`
- `<bioma>_pericoli.json`

Esempi:

- `tables/deserto/deserto_mostri.json`
- `tables/deserto/deserto_png.json`
- `tables/citta/citta_eventi_divini.json`

La provenienza del contenuto (`Lex Arcana 2e - Aegyptus`, `Manuale Base`, `Britannia`, `Dacia/Tracia`, ecc.) è un **metadato delle singole voci** e non determina la gerarchia delle cartelle.

## Eventi Divini

Le tabelle `*_eventi_divini.json` contengono **Presagi** inviati dagli dèi. Il risultato è un segno, fenomeno o manifestazione che i Custodes possono interpretare o decifrare mediante Rituali. Non è quindi una normale tabella di incontri casuali.

## Interfaccia del Demiurgo

Il bot dovrà presentare la scelta secondo la gerarchia:

**Bioma → Tipo di tabella → Risultato**

Il Demiurgo seleziona quindi il bioma e, all'interno di esso, la tabella desiderata. Il sistema non deve richiedere la conoscenza della fonte editoriale.
