# Magister Arcanus

Bot Discord per tabelle casuali creato per il GdR Lex Arcana.

## Permessi: Demiurgo

Magister Arcanus **non** vincola l'autorizzazione alla persona che ha creato il bot.
Ogni server Discord possiede il proprio permesso **univoco** di "Demiurgo".

- L'autorizzazione è rappresentata dal ruolo Discord `Demiurgo`.
- Solo un membro alla volta può detenere questo ruolo.
- Il primo Demiurgo viene nominato da un amministratore del server.
- Successivamente, solo il Demiurgo in carica può trasferire il permesso a un altro membro.
- I comandi amministrativi del bot sono riservati esclusivamente al Demiurgo in carica.
- La rimozione del ruolo "Demiurgo" da un membro comporta la revoca del permesso.
- Il bot non utilizza mai l'account GitHub, il proprietario dell'applicazione o variabili d'ambiente per determinare chi sia autorizzato a gestirlo..

Il sistema crea automaticamente il ruolo al momento della nomina del primo Demiurgo. Il bot deve disporre dei permessi Discord necessari per la gestione dei ruoli e il suo ruolo deve trovarsi al di sopra del ruolo  `Demiurgo` nella gerarchia dei ruoli del server.
