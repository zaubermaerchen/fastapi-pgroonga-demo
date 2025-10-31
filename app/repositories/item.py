from abc import ABC, abstractmethod

from sqlalchemy import select

from app.models.item import Item

from .base import BaseRepository


class ItemRepositoryInterface(ABC):
    @abstractmethod
    async def find(self, item_id: int) -> Item | None:
        pass


class ItemRepository(BaseRepository, ItemRepositoryInterface):
    async def find(self, item_id: int) -> Item | None:
        statement = select(Item).where(Item.id == item_id)
        result = await self.session.execute(statement)
        return result.scalar()
