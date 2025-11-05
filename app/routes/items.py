from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.repositories.item import ItemRepositoryInterface
from app.schemas.item import (
    CreateItemRequest,
    CreateItemResponse,
    GetItemResponse,
    Item,
    SearchItemsResponse,
)

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
    item_repository: FromDishka[ItemRepositoryInterface],
    request: CreateItemRequest,
):
    return await item_repository.create(
        request.name, request.description, request.price
    )


@router.get(
    "/search",
    response_model=SearchItemsResponse,
    operation_id="search_items",
    summary="アイテム情報検索",
)
@inject
async def search(
    item_repository: FromDishka[ItemRepositoryInterface],
    query: str,
    limit: int = 10,
    offset: int = 0,
):
    items, count = await item_repository.search(query, limit, offset)

    return SearchItemsResponse(
        results=[Item.model_validate(item) for item in items],
        count=count,
    )


@router.get(
    "/{item_id}",
    response_model=GetItemResponse,
    operation_id="get_item",
    summary="アイテム情報取得",
)
@inject
async def get(
    item_repository: FromDishka[ItemRepositoryInterface],
    item_id: int,
):
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
async def delete(
    item_repository: FromDishka[ItemRepositoryInterface],
    item_id: int,
):
    result = await item_repository.delete(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="item is not found")
