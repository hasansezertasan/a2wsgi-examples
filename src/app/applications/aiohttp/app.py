from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    """Handle aiohttp request."""
    return web.Response(text="Hello aiohttp")


app = web.Application()
app.add_routes(routes=[web.get("/", handler)])
