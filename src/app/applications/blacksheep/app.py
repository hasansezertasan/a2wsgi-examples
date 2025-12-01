from blacksheep.server.responses import json
from blacksheep.scribe import send_asgi_response

# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
async def app(scope, receive, send):  # type: ignore[override]
    """ASGI shim that responds using BlackSheep's response helper."""
    if scope["type"] != "http":
        raise RuntimeError("BlackSheep demo only supports HTTP.")

    response = json({"message": "Hello blacksheep"})
    await send_asgi_response(response, send)
