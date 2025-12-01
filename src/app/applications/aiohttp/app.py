# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
from aiohttp import web

async def app(scope, receive, send):  # type: ignore[override]
    """ASGI shim that responds using aiohttp's response helpers."""
    if scope["type"] != "http":
        raise RuntimeError("aiohttp demo only supports HTTP.")

    # Build the response with aiohttp's json_response for consistency.
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
