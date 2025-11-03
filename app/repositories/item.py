from abc import ABC, abstractmethod

from sqlalchemy import asc, func, select, text

from app.models.item import Item

from .base import BaseRepository


class ItemRepositoryInterface(ABC):
    @abstractmethod
    async def find(self, item_id: int) -> Item | None:
        pass

    @abstractmethod
    async def search(
        self, query: str, limit: int = 10, offset: int = 0
    ) -> tuple[list[Item], int]:
        pass


class ItemRepository(BaseRepository, ItemRepositoryInterface):
    async def find(self, item_id: int) -> Item | None:
        statement = select(Item).where(Item.id == item_id)
        result = await self.session.execute(statement)
        return result.scalar()

    async def search(
        self, query: str, limit: int = 10, offset: int = 0
    ) -> tuple[list[Item], int]:
        # 総件数取得
        statement = (
            select(func.count(Item.id).label("total"))
            .where(text("name &@~ :query"))
            .params(query=query)
        )
        result = await self.session.execute(statement)
        count = result.scalar_one()
        if count == 0:
            return [], 0

        # 対象位置のデータ取得
        statement = (
            select(Item)
            .where(text("name &@~ :query"))
            .limit(limit)
            .offset(offset)
            .order_by(asc(Item.id))
            .params(query=query)
        )
        result = await self.session.execute(statement)
        return list(result.scalars().all()), count
