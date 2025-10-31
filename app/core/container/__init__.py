from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from app.core.config import Settings


def make_container(_: Settings):
    return make_async_container(FastapiProvider())
