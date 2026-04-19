"""Test configuration for the application."""

import pytest


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """Set the async backend for tests.

    Returns:
        The async backend for tests.
    """
    return "asyncio"
