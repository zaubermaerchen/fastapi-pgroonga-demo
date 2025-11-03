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
                        id=1,
                        name="オートライブPASS",
                        description="オートライブを行うことができるアイテム",
                    ),
                    Item(
                        id=2,
                        name="レッスンチケット SSR",
                        description="カードのレッスンで使用するアイテム",
                    ),
                    Item(
                        id=3,
                        name="レッスンチケット SR",
                        description="カードのレッスンで使用するアイテム",
                    ),
                    Item(
                        id=4,
                        name="レッスンチケット R",
                        description="カードのレッスンで使用するアイテム",
                    ),
                    Item(
                        id=5,
                        name="レッスンチケット N",
                        description="カードのレッスンで使用するアイテム",
                    ),
                    Item(
                        id=6,
                        name="スパークドリンクMAX",
                        description="元気を、最大元気と同じ値だけ回復する",
                    ),
                    Item(
                        id=7,
                        name="スパークドリンク10",
                        description="元気を10回復できる",
                    ),
                    Item(
                        id=8,
                        name="スパークドリンク20",
                        description="元気を20回復できる",
                    ),
                    Item(
                        id=9,
                        name="スパークドリンク30",
                        description="元気を30回復できる",
                    ),
                ]
            )
