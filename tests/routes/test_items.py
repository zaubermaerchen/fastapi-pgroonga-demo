import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)

from app.schemas.item import CreateItemRequest, CreateItemResponse


@pytest.mark.asyncio
async def test_create(client: AsyncClient):
    request_body = CreateItemRequest(
        name="新アイテム", description="新しいアイテムの説明", price=500
    )
    response = await client.post("/items/", content=request_body.model_dump_json())
    assert response.status_code == HTTP_201_CREATED

    response_body = CreateItemResponse.model_validate(response.json())
    assert response_body.name == "新アイテム"
    assert response_body.description == "新しいアイテムの説明"
    assert response_body.price == 500


@pytest.mark.asyncio
async def test_search(client: AsyncClient):
    response = await client.get("/items/search", params={"query": "オートライブ"})
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "results": [
            {
                "id": 1,
                "name": "オートライブPASS",
                "description": "オートライブを行うことができるアイテム",
                "price": 100,
            }
        ],
        "count": 1,
    }

    response = await client.get("/items/search", params={"query": "レッスンチケット"})
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "results": [
            {
                "id": 2,
                "name": "レッスンチケット SSR",
                "description": "カードのレッスンで使用するアイテム",
                "price": 10000,
            },
            {
                "id": 3,
                "name": "レッスンチケット SR",
                "description": "カードのレッスンで使用するアイテム",
                "price": 5000,
            },
            {
                "id": 4,
                "name": "レッスンチケット R",
                "description": "カードのレッスンで使用するアイテム",
                "price": 1000,
            },
            {
                "id": 5,
                "name": "レッスンチケット N",
                "description": "カードのレッスンで使用するアイテム",
                "price": 500,
            },
        ],
        "count": 4,
    }

    response = await client.get(
        "/items/search", params={"query": "レッスンチケット", "limit": 2, "offset": 1}
    )
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "results": [
            {
                "id": 3,
                "name": "レッスンチケット SR",
                "description": "カードのレッスンで使用するアイテム",
                "price": 5000,
            },
            {
                "id": 4,
                "name": "レッスンチケット R",
                "description": "カードのレッスンで使用するアイテム",
                "price": 1000,
            },
        ],
        "count": 4,
    }

    response = await client.get(
        "/items/search", params={"query": "レッスンチケット OR スパークドリンク"}
    )
    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "results": [
            {
                "id": 2,
                "name": "レッスンチケット SSR",
                "description": "カードのレッスンで使用するアイテム",
                "price": 10000,
            },
            {
                "id": 3,
                "name": "レッスンチケット SR",
                "description": "カードのレッスンで使用するアイテム",
                "price": 5000,
            },
            {
                "id": 4,
                "name": "レッスンチケット R",
                "description": "カードのレッスンで使用するアイテム",
                "price": 1000,
            },
            {
                "id": 5,
                "name": "レッスンチケット N",
                "description": "カードのレッスンで使用するアイテム",
                "price": 500,
            },
            {
                "id": 6,
                "name": "スパークドリンクMAX",
                "description": "元気を、最大元気と同じ値だけ回復する",
                "price": 200,
            },
            {
                "id": 7,
                "name": "スパークドリンク10",
                "description": "元気を10回復できる",
                "price": 10,
            },
            {
                "id": 8,
                "name": "スパークドリンク20",
                "description": "元気を20回復できる",
                "price": 50,
            },
            {
                "id": 9,
                "name": "スパークドリンク30",
                "description": "元気を30回復できる",
                "price": 100,
            },
        ],
        "count": 8,
    }


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
