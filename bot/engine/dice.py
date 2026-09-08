import random
import re

DICE_RE = re.compile(r"(?i)(?P<count>\d*)d(?P<sides>\d+)(?P<modifier>[+-]\d+)?")


class DiceError(ValueError):
    pass


def roll_expression(expression: str, rng: random.Random | None = None) -> int:
    rng = rng or random
    expression = expression.strip().replace(" ", "")
    match = re.fullmatch(DICE_RE, expression)
    if not match:
        raise DiceError(f"Invalid dice expression: {expression}")

    count = int(match.group("count") or 1)
    sides = int(match.group("sides"))
    modifier = int(match.group("modifier") or 0)
    if count < 1 or count > 1000 or sides < 1 or sides > 100000:
        raise DiceError("Dice values are outside the supported limits")

    return sum(rng.randint(1, sides) for _ in range(count)) + modifier


def resolve_dice(text: str, rng: random.Random | None = None) -> str:
    rng = rng or random
    return DICE_RE.sub(lambda m: str(roll_expression(m.group(0), rng)), text)
