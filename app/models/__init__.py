from pathlib import Path

modules = []
for p in Path(__file__).parent.iterdir():
    if not p.is_file() or p.suffix != ".py":
        continue  # pragma: no cover

    if p.name in {"__init__.py", "base.py"}:
        continue

    modules.append(p.stem)

__all__ = modules  # pyright: ignore[reportUnsupportedDunderAll]
