from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    token: str
    authorized_user_id: int


def load_config() -> Config:
    token = os.getenv("DISCORD_TOKEN")
    user_id = os.getenv("AUTHORIZED_USER_ID")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not configured")
    if not user_id:
        raise RuntimeError("AUTHORIZED_USER_ID is not configured")
    try:
        authorized_user_id = int(user_id)
    except ValueError as exc:
        raise RuntimeError("AUTHORIZED_USER_ID must be a Discord user ID") from exc
    return Config(token=token, authorized_user_id=authorized_user_id)
