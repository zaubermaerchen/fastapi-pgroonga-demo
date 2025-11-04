from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.repositories.item import ItemRepositoryInterface
from app.schemas.item import CreateItemRequest, CreateItemResponse, GetItemResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.post(
    "/",
    response_model=CreateItemResponse,
    operation_id="create_item",
    summary="アイテム情報登録",
    status_code=HTTP_201_CREATED,
)
@inject
async def create(
    item: CreateItemRequest, item_repository: FromDishka[ItemRepositoryInterface]
):
    return await item_repository.create(item.name, item.description, item.price)


@router.get(
    "/{item_id}",
    response_model=GetItemResponse,
    operation_id="get_item",
    summary="アイテム情報取得",
)
@inject
async def get(item_id: int, item_repository: FromDishka[ItemRepositoryInterface]):
    item = await item_repository.find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item is not found")

    return item


@router.delete(
    "/{item_id}",
    operation_id="delete_item",
    summary="アイテム情報削除",
    status_code=HTTP_204_NO_CONTENT,
)
@inject
async def delete(item_id: int, item_repository: FromDishka[ItemRepositoryInterface]):
    result = await item_repository.delete(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="item is not found")
