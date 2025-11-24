from litestar import Litestar, get


@get("/")
async def index() -> dict:
    return {"message": "Hello, Litestar!"}


app = Litestar([index])
