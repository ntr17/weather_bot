"""
Trade logging — now delegates to core.storage.append_trade (SQLite).

This module exists only for backward compatibility with imports.
"""

from core.storage import append_trade  # noqa: F401
