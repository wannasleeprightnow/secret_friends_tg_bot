from dataclasses import dataclass
from os import environ

from dotenv import load_dotenv

load_dotenv()

POSTGRES_PORT: int = environ.get("POSTGRES_PORT")
POSTGRES_USER: str = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD")
POSTGRES_DB: str = environ.get("POSTGRES_DB")
POSTGRES_HOST: str = environ.get("POSTGRES_HOST")
POSTGRES_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:\
{POSTGRES_PASSWORD}@{POSTGRES_HOST}:\
{POSTGRES_PORT}/{POSTGRES_DB}"


@dataclass
class Settings:
    api_prefix: str = "/api/v1"
    ALLOWED_ORIGINS: str = "0.0.0.0"
