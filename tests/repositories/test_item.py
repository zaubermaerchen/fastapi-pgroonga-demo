import pytest
import pytest_asyncio
from dishka import AsyncContainer, Scope

from app.repositories.item import ItemRepositoryInterface


@pytest_asyncio.fixture
async def item_repository(container: AsyncContainer):
    async with container(scope=Scope.REQUEST) as c:
        yield await c.get(ItemRepositoryInterface)


@pytest.mark.asyncio
async def test_find(item_repository: ItemRepositoryInterface):
    item = await item_repository.find(1)
    assert item is not None
    assert item.name == "オートライブPASS"
    assert item.description == "オートライブを行うことができるアイテム"

    item = await item_repository.find(2)
    assert item is not None
    assert item.name == "レッスンチケット SSR"
    assert item.description == "カードのレッスンで使用するアイテム"

    item = await item_repository.find(99)
    assert item is None
