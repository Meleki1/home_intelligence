from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


DATABASE_URL = "......"

class Settings(BaseSettings):
    """
    Application Settings

    All environment variables are loaded here.
    """

    APP_NAME: str = "Home Intelligence Platform"

    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"

    DEBUG: bool = True

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()