from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config


@pytest.fixture(scope="session", autouse=True)
def db_migration():
    path = Path(__file__).parent.parent.joinpath("alembic.ini")
    config = Config(path)

    command.downgrade(config, "base")
    command.upgrade(config, "head")
