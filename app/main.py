from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)


@app.get("/")
async def root():
    return {"message": "Hello World"}
