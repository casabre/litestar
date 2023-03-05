from __future__ import annotations

try:
    import sqlalchemy

    if sqlalchemy.__version__.startswith("2."):
        collect_ignore_glob = ["*"]
except ImportError:
    collect_ignore_glob = ["*"]