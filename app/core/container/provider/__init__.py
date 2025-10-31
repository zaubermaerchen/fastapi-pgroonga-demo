from dishka.provider import BaseProvider

from app.core.config import Settings

from .database import DatabaseProvider
from .logger import LoggerProvider


def make_providers(settings: Settings) -> list[BaseProvider]:
    return [
        LoggerProvider(settings),
        DatabaseProvider(settings),
    ]
