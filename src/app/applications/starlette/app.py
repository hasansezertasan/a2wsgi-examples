"""Starlette example application."""

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request) -> JSONResponse:
    """Handle Starlette request.

    Returns:
        JSONResponse: The response to be sent back.
    """
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
