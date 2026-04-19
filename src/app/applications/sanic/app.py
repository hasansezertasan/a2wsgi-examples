"""Sanic sub-application mounted via ASGI.

Sanic manages its own event loop and cannot be mounted as a sub-app inside
another ASGI server. This provides a minimal ASGI shim that uses Sanic's
response helpers for consistent serialization.
"""

from sanic.response import json as sanic_json


async def app(scope, receive, send):  # type: ignore[override]
    """ASGI shim — Sanic cannot be mounted as a sub-app."""
    if scope["type"] != "http":
        raise RuntimeError("Sanic demo only supports HTTP.")

    response = sanic_json({"message": "Hello sanic"})
    headers = [
        (b"content-type", response.content_type.encode("latin-1")),
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
