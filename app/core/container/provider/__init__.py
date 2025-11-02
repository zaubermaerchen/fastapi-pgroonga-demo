from dishka.provider import BaseProvider

from app.core.config import Settings

from .database import DatabaseProvider
from .logger import LoggerProvider
from .repository import make_repository_provider


def make_providers(settings: Settings) -> list[BaseProvider]:
    return [
        LoggerProvider(settings),
        DatabaseProvider(settings),
        make_repository_provider(settings),
    ]
