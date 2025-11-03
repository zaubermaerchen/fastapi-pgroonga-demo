from fastapi import APIRouter

from app.routes import items, root

router = APIRouter()

router.include_router(root.router)
router.include_router(items.router)
