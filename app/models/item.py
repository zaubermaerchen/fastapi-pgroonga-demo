from sqlalchemy import Column, Index, Integer, String, Text

from app.models.base import BaseModel, TimestampMixin


class Item(BaseModel, TimestampMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False, default=0)


Index("idx_title", Item.name, postgresql_using="pgroonga")
