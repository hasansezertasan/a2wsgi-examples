from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request) -> JSONResponse:  # noqa: ARG001
    """Handle Starlette request."""
    return JSONResponse(
        {
            "message": "Hello starlette",
        },
    )


app = Starlette(
    debug=False,
    routes=[
        Route(path="/", endpoint=homepage),
    ],
)
