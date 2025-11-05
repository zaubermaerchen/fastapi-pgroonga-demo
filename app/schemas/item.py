from pydantic import BaseModel, ConfigDict, Field


class Item(BaseModel):
    id: int = Field(title="🆔")
    name: str = Field(title="アイテム名")
    description: str = Field(title="アイテム説明")
    price: int = Field(title="価格")

    model_config = ConfigDict(from_attributes=True)


class GetItemResponse(Item):
    pass


class CreateItemRequest(BaseModel):
    name: str = Field(title="アイテム名")
    description: str = Field(title="アイテム説明")
    price: int = Field(title="価格")


class CreateItemResponse(Item):
    pass


class SearchItemsResponse(BaseModel):
    results: list[Item] = Field(title="検索結果")
    count: int = Field(title="総件数")
