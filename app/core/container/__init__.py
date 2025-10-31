from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from app.core.config import Settings

from .provider import make_providers


def make_container(settings: Settings):
    return make_async_container(
        *make_providers(settings),
        FastapiProvider(),
    )
