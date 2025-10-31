from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from app.core.config import Settings

from .provider.database import DatabaseProvider


def make_container(settings: Settings):
    return make_async_container(DatabaseProvider(settings), FastapiProvider())
