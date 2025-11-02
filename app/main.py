from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import FastAPI

from app.core.config import get_settings
from app.core.container.provider import make_providers
from app.core.router import router

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)

container = make_async_container(*make_providers(settings), FastapiProvider())
setup_dishka(container, app)

app.include_router(router)
