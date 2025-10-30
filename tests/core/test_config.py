from app.core.config import get_settings


def test_get_settings():
    settings = get_settings()

    assert settings.ENV == "test"
    assert settings.DEBUG is True
    assert (
        settings.DATABASE_URL
        == "postgresql+asyncpg://postgres:password@db:5432/postgres"
    )
