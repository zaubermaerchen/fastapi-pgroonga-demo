from collections.abc import AsyncGenerator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from app.core.config import Settings


class DatabaseProvider(Provider):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

    @provide(scope=Scope.APP)
    async def engine(self) -> AsyncGenerator[AsyncEngine]:
        engine = create_async_engine(
            self.settings.DATABASE_URL,
            echo=self.settings.DEBUG,
            future=True,
            pool_pre_ping=True,
            poolclass=NullPool,
        )
        try:
            yield engine
        finally:
            await engine.dispose(True)

    @provide(scope=Scope.APP)
    def session_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
        )

    @provide(scope=Scope.REQUEST)
    async def session(
        self, session_pool: async_sessionmaker[AsyncSession]
    ) -> AsyncGenerator[AsyncSession]:
        async with session_pool() as session:
            yield session
