from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_ENV: Literal["dev", "test", "prod"] = "dev"
    PROJECT_NAME: str = "Stack from Scratch"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str
    SECRET_KEY: str

    CORS_ORIGINS: list[str] = []
    LOG_LEVEL: str = "INFO"

    @property
    def docs_url(self):
        return None if self.APP_ENV == "prod" else "/docs"

    @property
    def redoc_url(self):
        return None if self.APP_ENV == "prod" else "/redoc"

settings = Settings()
