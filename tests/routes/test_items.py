import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    response = await client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "オートライブPASS",
        "description": "オートライブを行うことができるアイテム",
        "price": 100,
    }

    response = await client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "レッスンチケット SSR",
        "description": "カードのレッスンで使用するアイテム",
        "price": 10000,
    }

    response = await client.get("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "item is not found"}
