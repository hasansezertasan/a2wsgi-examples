"""Sanic sub-application mounted via ASGI.

Sanic manages its own event loop and cannot be mounted as a sub-app inside
another ASGI server. This provides a minimal ASGI shim that uses Sanic's
response helpers for consistent serialization.
"""

from collections.abc import Awaitable, Callable

from sanic.response import json as sanic_json


async def app(
    scope: dict[str, object],
    receive: object,
    send: Callable[..., Awaitable[None]],
) -> None:
    """ASGI shim — Sanic cannot be mounted as a sub-app.

    Raises:
        RuntimeError: If the ASGI scope type is not ``http``.
    """
    if scope["type"] != "http":
        msg = "Sanic demo only supports HTTP."
        raise RuntimeError(msg)

    response = sanic_json({"message": "Hello sanic"})
    headers = [
        (b"content-type", response.content_type.encode("latin-1")),  # type: ignore[union-attr]  # pyright: ignore[reportOptionalMemberAccess]  # pyrefly: ignore  # ty: ignore[unresolved-attribute]
    ]
    await send(
        {
            "type": "http.response.start",
            "status": response.status,
            "headers": headers,
        },
    )
    await send(
        {
            "type": "http.response.body",
            "body": response.body,
            "more_body": False,
        },
    )
