from functools import lru_cache
from os import getenv

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn


@lru_cache(maxsize=2000)
def get_settings() -> Settings:
    settings = Settings()
    if getenv("POSTGRES_DB") is not None:
        db = getenv("POSTGRES_DB")
        settings.database_url = PostgresDsn.build(
            scheme="postgresql",
            user=settings.database_url.user,
            password=settings.database_url.password,
            host=settings.database_url.host,
            port=settings.database_url.port,
            path=f"/{db}",
        )
    return settings