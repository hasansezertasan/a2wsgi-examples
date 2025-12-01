from litestar import Litestar, get


@get(path="/")
async def index() -> dict[str, str]:
    """Handle litestar request.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    return {"message": "Hello, Litestar!"}


app: Litestar = Litestar(route_handlers=[index])
