from fastapi import APIRouter

from app.routes import root

router = APIRouter()

router.include_router(root.router)
