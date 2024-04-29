from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    database_settings: DatabaseSettings = DatabaseSettings()


settings = Settings()
