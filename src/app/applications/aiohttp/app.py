"""aiohttp sub-application mounted via ASGI.

aiohttp does not natively support ASGI mounting. This provides a minimal
ASGI app that uses aiohttp's json_response for consistent serialization.
"""

from collections.abc import Awaitable, Callable

from aiohttp import web


async def app(
    scope: dict[str, object],
    receive: object,
    send: Callable[..., Awaitable[None]],
) -> None:
    """ASGI shim — aiohttp has no native ASGI adapter for sub-app mounting.

    Raises:
        RuntimeError: If the ASGI scope type is not ``http``.
    """
    if scope["type"] != "http":
        msg = "aiohttp demo only supports HTTP."
        raise RuntimeError(msg)

    response = web.json_response({"message": "Hello aiohttp"})

    headers = [
        (name.encode("latin-1"), value.encode("latin-1"))
        for name, value in response.headers.items()
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
