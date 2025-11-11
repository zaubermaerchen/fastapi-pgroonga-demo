# fastapi-pgroonga-demo

FastAPIによる全文検索APIデモプロジェクトです。

## 特徴

- Dev Containerと[uv](https://docs.astral.sh/uv/), [Ruff](https://docs.astral.sh/ruff/)を使った開発環境
- PostgreSQL+[PGroonga](https://pgroonga.github.io/)による多言語に対応した全文検索機能
- DIコンテナとして[Dishka](https://dishka.readthedocs.io/)を採用
- [Alembic](https://alembic.sqlalchemy.org/)を使ったDBマイグレーション機能
- [Pytest](https://docs.pytest.org/)を使ったユニットテスト機能

## usage

```
$ docker compose up -d
$ docker compose exec app uv run alembic upgrade head
```
