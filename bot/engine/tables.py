from dataclasses import dataclass
import json
from pathlib import Path
import random

from .dice import resolve_dice


@dataclass(frozen=True)
class TableEntry:
    text: str
    weight: int = 1


@dataclass(frozen=True)
class Table:
    name: str
    category: str
    description: str
    entries: tuple[TableEntry, ...]

    def roll(self, rng: random.Random | None = None) -> str:
        if not self.entries:
            raise ValueError(f"Table '{self.name}' has no entries")
        rng = rng or random
        entry = rng.choices(self.entries, weights=[e.weight for e in self.entries], k=1)[0]
        return resolve_dice(entry.text, rng)


def load_table(path: Path) -> Table:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = tuple(
        TableEntry(text=str(item["text"]), weight=int(item.get("weight", 1)))
        for item in data.get("entries", [])
    )
    return Table(
        name=str(data["name"]),
        category=str(data.get("category", "")),
        description=str(data.get("description", "")),
        entries=entries,
    )


def load_tables(root: Path) -> dict[str, Table]:
    tables: dict[str, Table] = {}
    if not root.exists():
        return tables
    for path in root.rglob("*.json"):
        table = load_table(path)
        tables[table.name.casefold()] = table
    return tables
