from dishka import Provider, Scope

from app.core.config import Settings
from app.repositories.item import ItemRepository, ItemRepositoryInterface


def make_repository_provider(_: Settings) -> Provider:
    provider = Provider()
    provider.provide(
        ItemRepository, provides=ItemRepositoryInterface, scope=Scope.REQUEST
    )
    return provider
