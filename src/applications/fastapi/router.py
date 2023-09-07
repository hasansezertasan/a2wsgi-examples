import enum

from fastapi import APIRouter, Path
from fastapi.responses import RedirectResponse

router = APIRouter()


class Applications(str, enum.Enum):
    FLASK = "flask"
    DJANGO = "django"
    FASTAPI = "fastapi"
    STARLETTE = "starlette"
    LITESTAR = "litestar"
    BOTTLE = "bottle"
    GRADIO = "gradio"
    PYWEBIO = "pywebio"


@router.get("/")
async def index():
    return {
        "message": "Hello World",
    }


@router.get("/application-redirection/{application}")
async def application_redirection(
    application: Applications = Path(
        ...,
        title="Application",
        description="Application to redirect to",
        example=Applications.FLASK,
    )
):
    return RedirectResponse(
        url=f"/{application.value}",
        status_code=302,
    )
