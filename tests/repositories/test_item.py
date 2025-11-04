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
async def test_create(item_repository: ItemRepositoryInterface):
    item = await item_repository.create("新アイテム", "新しいアイテムの説明", 500)
    assert item.id == 10
    assert item.name == "新アイテム"
    assert item.description == "新しいアイテムの説明"
    assert item.price == 500


@pytest.mark.asyncio
async def test_delete(item_repository: ItemRepositoryInterface):
    result = await item_repository.delete(1)
    assert result is True
    item = await item_repository.find(1)
    assert item is None

    result = await item_repository.delete(99)
    assert result is False


@pytest.mark.asyncio
async def test_search(item_repository: ItemRepositoryInterface):
    items, count = await item_repository.search("オートライブ")
    assert len(items) == 1
    assert count == 1
    assert items[0].id == 1
    assert items[0].name == "オートライブPASS"
    assert items[0].description == "オートライブを行うことができるアイテム"

    items, count = await item_repository.search("レッスンチケット")
    assert count == 4
    assert len(items) == 4
    assert [item.id for item in items] == [2, 3, 4, 5]

    items, count = await item_repository.search("レッスンチケット", 2, 1)
    assert count == 4
    assert len(items) == 2
    assert [item.id for item in items] == [3, 4]

    items, count = await item_repository.search("レッスンチケット OR スパークドリンク")
    assert count == 8
    assert len(items) == 8
    assert [item.id for item in items] == [2, 3, 4, 5, 6, 7, 8, 9]

    items, count = await item_repository.search("存在しないアイテム")
    assert count == 0
    assert len(items) == 0
