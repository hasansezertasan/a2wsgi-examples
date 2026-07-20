"""BlackSheep sub-application mounted via ASGI.

BlackSheep's Application requires its own startup lifecycle and cannot be
directly mounted as a sub-app. This provides a minimal ASGI shim that uses
BlackSheep's response helpers for consistent serialization.
"""

from collections.abc import Awaitable, Callable

from blacksheep.scribe import send_asgi_response
from blacksheep.server.responses import json


async def app(
    scope: dict[str, object],
    receive: object,
    send: Callable[..., Awaitable[None]],
) -> None:
    """ASGI shim — BlackSheep requires its own lifecycle to mount as sub-app.

    Raises:
        RuntimeError: If the ASGI scope type is not ``http``.
    """
    if scope["type"] != "http":
        msg = "BlackSheep demo only supports HTTP."
        raise RuntimeError(msg)

    response = json({"message": "Hello blacksheep"})
    await send_asgi_response(response, send)
