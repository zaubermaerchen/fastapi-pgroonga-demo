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
    assert item.price == 100

    item = await item_repository.find(2)
    assert item is not None
    assert item.name == "レッスンチケット SSR"
    assert item.description == "カードのレッスンで使用するアイテム"
    assert item.price == 10000

    item = await item_repository.find(99)
    assert item is None


@pytest.mark.asyncio
async def test_search(item_repository: ItemRepositoryInterface):
    items = await item_repository.search("オートライブ")
    assert len(items) == 1
    assert items[0].id == 1
    assert items[0].name == "オートライブPASS"
    assert items[0].description == "オートライブを行うことができるアイテム"

    items = await item_repository.search("レッスンチケット")
    assert len(items) == 4
    item_ids = [item.id for item in items]
    assert item_ids == [2, 3, 4, 5]

    items = await item_repository.search("レッスンチケット", 2, 1)
    assert len(items) == 2
    item_ids = [item.id for item in items]
    assert item_ids == [3, 4]

    items = await item_repository.search("レッスンチケット OR スパークドリンク")
    assert len(items) == 8
    item_ids = [item.id for item in items]
    assert item_ids == [2, 3, 4, 5, 6, 7, 8, 9]
