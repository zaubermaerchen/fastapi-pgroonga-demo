from pydantic import BaseModel, ConfigDict, Field


class Item(BaseModel):
    id: int = Field(title="🆔")
    name: str = Field(title="アイテム名")
    description: str = Field(title="アイテム説明")
    price: int = Field(title="価格")

    model_config = ConfigDict(from_attributes=True)
