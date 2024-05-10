from pydantic_settings import BaseSettings


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


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    ALLOWED_ORIGINS: str = "127.0.0.1"


database_settings = DatabaseSettings()
settings = Settings()
