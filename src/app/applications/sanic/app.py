# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
"""Minimal Sanic-powered ASGI response."""

from sanic.response import json as sanic_json


async def app(scope, receive, send):  # type: ignore[override]
    """Return a Sanic-style JSON response via ASGI."""
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
