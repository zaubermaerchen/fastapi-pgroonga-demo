from logging import Logger, getLogger

from dishka import Provider, Scope, provide

from app.core.config import Settings


class LoggerProvider(Provider):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

    @provide(scope=Scope.APP)
    def logger(self) -> Logger:
        return getLogger("uvicorn.app")
