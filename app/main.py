from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.api.router import router
from app.core.config import get_settings
from app.core.container import make_container

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)

setup_dishka(make_container(settings), app)

app.include_router(router)
