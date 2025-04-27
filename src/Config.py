from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
