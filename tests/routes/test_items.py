from typing import Any

import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)

from app.schemas.item import CreateItemRequest


@pytest.mark.asyncio
async def test_create(client: AsyncClient):
    request_body = CreateItemRequest(
        name="新アイテム", description="新しいアイテムの説明", price=500
    )
    response = await client.post("/items/", content=request_body.model_dump_json())
    assert response.status_code == HTTP_201_CREATED

    response_body: dict[str, Any] = response.json()
    assert response_body["name"] == "新アイテム"
    assert response_body["description"] == "新しいアイテムの説明"
    assert response_body["price"] == 500


@pytest.mark.asyncio
async def test_get(client: AsyncClient):
    response = await client.get("/items/1")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "name": "オートライブPASS",
        "description": "オートライブを行うことができるアイテム",
        "price": 100,
    }

    response = await client.get("/items/2")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "id": 2,
        "name": "レッスンチケット SSR",
        "description": "カードのレッスンで使用するアイテム",
        "price": 10000,
    }

    response = await client.get("/items/99")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "item is not found"}


@pytest.mark.asyncio
async def test_delete(client: AsyncClient):
    response = await client.delete("/items/1")
    assert response.status_code == HTTP_204_NO_CONTENT

    response = await client.delete("/items/99")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "item is not found"}
