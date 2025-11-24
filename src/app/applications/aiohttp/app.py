from aiohttp import web
from aiohttp.web_app import Application


async def handler(request: web.Request) -> web.Response:
    """Handle aiohttp request.

    Args:
        request (web.Request): The incoming request.
    Returns:
        web.Response: The response to be sent back.
    """
    return web.Response(text="Hello aiohttp")


app: Application = web.Application()
app.add_routes(routes=[web.get(path="/", handler=handler)])
