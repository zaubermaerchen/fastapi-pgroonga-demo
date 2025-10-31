from logging import Logger

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession, logger: Logger):
        self.session = session
        self.logger = logger
