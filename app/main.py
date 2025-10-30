from fastapi import FastAPI

from app.api.router import router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)

app.include_router(router)
