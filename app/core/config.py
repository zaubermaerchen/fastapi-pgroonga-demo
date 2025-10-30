import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = os.getenv("ENV", "production")
    DEBUG: bool = False

    model_config = {
        "env_file": [".env", f".env.{ENV}", ".env.local", f".env.{ENV}.local"]
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
