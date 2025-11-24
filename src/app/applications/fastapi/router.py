from typing import Annotated

from fastapi import APIRouter, Path
from fastapi.responses import RedirectResponse

from app.schemas import Applications

router = APIRouter()


@router.get(path="/")
async def index() -> dict[str, str]:
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
    return RedirectResponse(
        url=f"/{application.value}",
        status_code=302,
    )
