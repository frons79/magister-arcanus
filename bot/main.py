from __future__ import annotations

import os
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands

from .config import load_config
from .engine.tables import Table, load_tables
from .security import appoint_demiurge, can_bootstrap_demiurge, is_demiurge

TABLES_ROOT = Path(__file__).resolve().parent.parent / "tables"


class MagisterArcanus(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)
        self.tables: dict[str, Table] = {}

    async def setup_hook(self) -> None:
        self.tables = load_tables(TABLES_ROOT)
        await self.tree.sync()
        print(f"Magister Arcanus online. Tabelle caricate: {len(self.tables)}")


bot = MagisterArcanus()
tabella = app_commands.Group(name="tabella", description="Estrae risultati dalle tabelle di Magister Arcanus")


def find_table(name: str) -> Table | None:
    return bot.tables.get(name.casefold())


def table_names() -> list[str]:
    return sorted(table.name for table in bot.tables.values())


@tabella.command(name="incontri", description="Estrae uno o più risultati dalla tabella Incontri")
@app_commands.describe(numero="Numero di risultati da estrarre (1-20)")
async def incontri(interaction: discord.Interaction, numero: app_commands.Range[int, 1, 20] = 1) -> None:
    matches = [t for t in bot.tables.values() if t.category.casefold() == "incontri" and "incontri" in t.name.casefold()]
    if not matches:
        await interaction.response.send_message("Nessuna tabella Incontri disponibile.", ephemeral=True)
        return
    table = matches[0]
    results = [f"**{i}.** {table.roll()}" for i in range(1, numero + 1)]
    await interaction.response.send_message(f"**{table.name}**\n" + "\n".join(results), ephemeral=True)


@tabella.command(name="estrai", description="Estrae uno o più risultati da una tabella specifica")
@app_commands.describe(nome="Nome esatto della tabella", numero="Numero di risultati da estrarre (1-20)")
async def estrai(interaction: discord.Interaction, nome: str, numero: app_commands.Range[int, 1, 20] = 1) -> None:
    table = find_table(nome)
    if table is None:
        await interaction.response.send_message("Tabella non trovata. Usa /tabelle per vedere quelle disponibili.", ephemeral=True)
        return
    results = [f"**{i}.** {table.roll()}" for i in range(1, numero + 1)]
    await interaction.response.send_message(f"**{table.name}**\n" + "\n".join(results), ephemeral=True)


@bot.tree.command(name="tabelle", description="Elenca tutte le tabelle disponibili")
async def tabelle(interaction: discord.Interaction) -> None:
    names = table_names()
    text = "\n".join(f"• `{name}`" for name in names) if names else "Nessuna tabella caricata."
    await interaction.response.send_message(f"**Tabelle disponibili ({len(names)})**\n{text}", ephemeral=True)


@bot.tree.command(name="tabellainfo", description="Mostra informazioni su una tabella")
@app_commands.describe(nome="Nome esatto della tabella")
async def tabellainfo(interaction: discord.Interaction, nome: str) -> None:
    table = find_table(nome)
    if table is None:
        await interaction.response.send_message("Tabella non trovata.", ephemeral=True)
        return
    await interaction.response.send_message(
        f"**{table.name}**\nCategoria: `{table.category}`\n{table.description}\nVoci: `{len(table.entries)}`",
        ephemeral=True,
    )


@bot.tree.command(name="demiurgo", description="Gestione iniziale del Demiurgo")
@app_commands.describe(membro="Membro da nominare come Demiurgo")
async def demiurgo(interaction: discord.Interaction, membro: discord.Member) -> None:
    if interaction.guild is None or not isinstance(interaction.user, discord.Member):
        await interaction.response.send_message("Questo comando può essere usato solo in un server.", ephemeral=True)
        return
    current = await discord.utils.maybe_coroutine(is_demiurge, interaction.user)
    if not current and not can_bootstrap_demiurge(interaction.user):
        await interaction.response.send_message("Solo un amministratore può nominare il primo Demiurgo; in seguito il trasferimento spetta al Demiurgo in carica.", ephemeral=True)
        return
    await appoint_demiurge(interaction.guild, membro)
    await interaction.response.send_message(f"{membro.mention} è ora il **Demiurgo** del server.", ephemeral=True)


bot.tree.add_command(tabella)


@bot.event
async def on_ready() -> None:
    print(f"Connesso come {bot.user} (ID: {bot.user.id if bot.user else 'n/d'})")


if __name__ == "__main__":
    config = load_config()
    bot.run(config.token)
