"""FastAPI router for the root application."""

from typing import Annotated

from fastapi import APIRouter, Path
from fastapi.responses import RedirectResponse

from app.schemas import Applications

router = APIRouter()


@router.get(path="/")
async def index() -> dict[str, str]:
    """Handle the root request.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    return {
        "message": "Hello World",
    }


@router.get(path="/application-redirection/{application}")
async def application_redirection(
    application: Annotated[
        Applications,
        Path(
            title="Application",
            description="Application to redirect to",
            examples=[Applications.FLASK],
        ),
    ],
) -> RedirectResponse:
    """Redirect to the selected application.

    Returns:
        RedirectResponse: A redirect to the selected application.
    """
    return RedirectResponse(
        url=f"/{application.value}",
        status_code=302,
    )
