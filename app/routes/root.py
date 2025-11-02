from logging import Logger

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
@inject
async def root(logger: FromDishka[Logger]):
    logger.info("Root endpoint called")
    return {"message": "Hello World"}
