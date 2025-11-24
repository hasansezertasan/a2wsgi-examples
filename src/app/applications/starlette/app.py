from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request) -> JSONResponse:
    """Homepage view for Starlette application.

    Args:
        request (Request): The incoming HTTP request.
    Returns:
        JSONResponse: A JSON response with a greeting message.
    """
    return JSONResponse(
        {
            "message": "Hello Starlette",
        },
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
    ],
)
