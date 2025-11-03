from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.repositories.item import ItemRepositoryInterface
from app.schemas.item import Item

router = APIRouter(prefix="/items", tags=["items"])


@router.get(
    "/{item_id}",
    response_model=Item,
    operation_id="get_item",
    summary="アイテム情報取得",
)
@inject
async def get(item_id: int, item_repository: FromDishka[ItemRepositoryInterface]):
    item = await item_repository.find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item is not found")

    return item
