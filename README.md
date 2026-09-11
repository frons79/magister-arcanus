# Magister Arcanus

Bot Discord per tabelle casuali creato per il GdR Lex Arcana.

## Avvio locale

1. Crea un ambiente virtuale Python 3.12+.
2. Installa le dipendenze con `pip install -r requirements.txt`.
3. Copia `.env.example` in `.env` e imposta `DISCORD_TOKEN` con il token del bot Discord.
4. Avvia con `python -m bot.main`.

Il token non deve mai essere inserito nel repository GitHub.

## Deployment cloud

Il progetto include un `Dockerfile` pronto per un deployment containerizzato. Il bot mantiene una connessione persistente al Gateway Discord, quindi il servizio cloud deve eseguire un processo worker sempre attivo e non un normale endpoint HTTP con scale-to-zero.

### Google Cloud

Google Cloud è supportato. Per una prima installazione di test, la soluzione più semplice è una piccola VM **Compute Engine** Linux:

1. Crea una VM.
2. Installa Docker.
3. Clona questo repository.
4. Costruisci l'immagine con `docker build -t magister-arcanus .`.
5. Avvia il container passando `DISCORD_TOKEN` come variabile d'ambiente.
6. Configura il riavvio automatico del container (`--restart unless-stopped`).

Per una gestione più strutturata è possibile usare un container registry e un servizio worker di Google Cloud, mantenendo il processo Discord sempre attivo.

## Permessi: Demiurgo

Magister Arcanus **non** vincola l'autorizzazione alla persona che ha creato il bot.
Ogni server Discord possiede il proprio permesso **univoco** di "Demiurgo".

- L'autorizzazione è rappresentata dal ruolo Discord `Demiurgo`.
- Solo un membro alla volta può detenere questo ruolo.
- Il primo Demiurgo viene nominato da un amministratore del server.
- Successivamente, il Demiurgo in carica può trasferire il permesso a un altro membro.
- I comandi amministrativi del bot sono riservati esclusivamente al Demiurgo in carica.
- La rimozione del ruolo `Demiurgo` da un membro comporta la revoca del permesso.
- Il bot non utilizza l'account GitHub, il proprietario dell'applicazione o variabili d'ambiente per determinare chi sia autorizzato a gestirlo.

Il sistema crea automaticamente il ruolo al momento della nomina del primo Demiurgo. Il bot deve disporre dei permessi Discord necessari per la gestione dei ruoli e il suo ruolo deve trovarsi al di sopra del ruolo `Demiurgo` nella gerarchia dei ruoli del server.
