from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    return web.Response(text="Hello world")


app = web.Application()
app.add_routes([web.get("/", handler)])
