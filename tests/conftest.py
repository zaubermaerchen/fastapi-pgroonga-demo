from pathlib import Path

import pytest
import pytest_asyncio
from alembic import command
from alembic.config import Config
from dishka import AsyncContainer, make_async_container
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from app.core.config import get_settings
from app.core.container.provider import make_providers
from app.models.item import Item


@pytest.fixture(scope="session", autouse=True)
def db_migration():
    path = Path(__file__).parent.parent.joinpath("alembic.ini")
    config = Config(path)

    command.downgrade(config, "base")
    command.upgrade(config, "head")


@pytest_asyncio.fixture(scope="session")
async def container():
    settings = get_settings()
    container = make_async_container(*make_providers(settings))
    try:
        yield container
    finally:
        await container.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def db_setup(container: AsyncContainer):
    engine = await container.get(AsyncEngine)
    async with AsyncSession(engine) as session:
        async with session.begin():
            session.add_all(
                [
                    Item(
                        name="オートライブPASS",
                        description="オートライブを行うことができるアイテム",
                        price=100,
                    ),
                    Item(
                        name="レッスンチケット SSR",
                        description="カードのレッスンで使用するアイテム",
                        price=10000,
                    ),
                    Item(
                        name="レッスンチケット SR",
                        description="カードのレッスンで使用するアイテム",
                        price=5000,
                    ),
                    Item(
                        name="レッスンチケット R",
                        description="カードのレッスンで使用するアイテム",
                        price=1000,
                    ),
                    Item(
                        name="レッスンチケット N",
                        description="カードのレッスンで使用するアイテム",
                        price=500,
                    ),
                    Item(
                        name="スパークドリンクMAX",
                        description="元気を、最大元気と同じ値だけ回復する",
                        price=200,
                    ),
                    Item(
                        name="スパークドリンク10",
                        description="元気を10回復できる",
                        price=10,
                    ),
                    Item(
                        name="スパークドリンク20",
                        description="元気を20回復できる",
                        price=50,
                    ),
                    Item(
                        name="スパークドリンク30",
                        description="元気を30回復できる",
                        price=100,
                    ),
                ]
            )
