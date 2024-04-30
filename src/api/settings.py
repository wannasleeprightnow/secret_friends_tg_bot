from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "127.0.0.1"


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    ALLOWED_ORIGINS: str = "127.0.0.1"


database_settings = DatabaseSettings()
settings = Settings()
