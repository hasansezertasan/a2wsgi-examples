"""BlackSheep sub-application mounted via ASGI.

BlackSheep's Application requires its own startup lifecycle and cannot be
directly mounted as a sub-app. This provides a minimal ASGI shim that uses
BlackSheep's response helpers for consistent serialization.
"""

from blacksheep.server.responses import json
from blacksheep.scribe import send_asgi_response


async def app(scope, receive, send):  # type: ignore[override]
    """ASGI shim — BlackSheep requires its own lifecycle to mount as sub-app."""
    if scope["type"] != "http":
        raise RuntimeError("BlackSheep demo only supports HTTP.")

    response = json({"message": "Hello blacksheep"})
    await send_asgi_response(response, send)
