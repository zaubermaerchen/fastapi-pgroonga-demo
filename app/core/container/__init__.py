from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from app.core.config import Settings

from .provider.database import DatabaseProvider
from .provider.logger import LoggerProvider


def make_container(settings: Settings):
    return make_async_container(
        LoggerProvider(settings), DatabaseProvider(settings), FastapiProvider()
    )
