from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class DatabaseSettings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

    @property
    def postgres_dsn(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:\
{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:\
{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def alembic_dsn(self):
        return f"postgresql+psycopg://{self.POSTGRES_USER}:\
{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:\
{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env")


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    ALLOWED_ORIGINS: str = "127.0.0.1"


database_settings = DatabaseSettings()
settings = Settings()