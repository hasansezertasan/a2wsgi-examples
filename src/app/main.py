"""Application."""

from collections.abc import Awaitable, Callable

from a2wsgi import ASGIMiddleware, WSGIMiddleware
from fastapi import FastAPI, Request, Response
from starlette.middleware.sessions import SessionMiddleware

from app.applications.aiohttp.app import app as aiohttp_app
from app.applications.bottle.app import app as bottle_app
from app.applications.django.app import application as django_application
from app.applications.fastapi.app import app as fastapi_app
from app.applications.fastapi.router import router as fastapi_router
from app.applications.flask.app import app as flask_app
from app.applications.flet.app import app as flet_app
from app.applications.gradio.app import app as gradio_app
from app.applications.litestar.app import app as litestar_app
from app.applications.pywebio.app import app as pywebio_app
from app.applications.starlette.app import app as starlette_app

app = FastAPI(
    title="FastAPI Mount Examples",
    description="The goal of this project is to provide examples of how to mount "
    "sub applications written in different frameworks to FastAPI. ",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    terms_of_service="http://fastapi.tiangolo.com/terms/",
    responses={
        404: {
            "description": "Not found",
        }
    },
    contact={
        "name": "Hasan Sezer Taşan",
        "url": "http://www.hasansezertasan.com",
        "email": "hasansezertasan@gmail.com",
    },
)
app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")
app.mount(
    path="/aiohttp",
    app=ASGIMiddleware(aiohttp_app),
    name="aiohttp",
)
app.mount(
    path="/fastapi",
    app=fastapi_app,
    name="fastapi",
)
app.include_router(
    router=fastapi_router,
    tags=["Default"],
)
app.mount(
    path="/flask",
    app=WSGIMiddleware(flask_app),
    name="flask",
)
app.mount(
    path="/flet",
    app=flet_app,
    name="flet",
)
app.mount(
    path="/django",
    app=WSGIMiddleware(django_application),
    name="django",
)
app.mount(
    path="/bottle",
    app=WSGIMiddleware(bottle_app),
    name="bottle",
)
app.mount(
    path="/litestar",
    app=litestar_app,
    name="litestar",
)
app.mount(
    path="/gradio",
    app=gradio_app,
    name="gradio",
)
app.mount(
    path="/pywebio",
    app=pywebio_app,
    name="pywebio",
)
app.mount(
    path="/starlette",
    app=starlette_app,
    name="starlette",
)


@app.middleware("http")
async def middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    """Middleware for FastAPI application.

    Args:
        request: The incoming request.
        call_next: The next middleware or route handler.

    Returns:
        The response after processing.
    """
    print("I am a fastapi middleware before request.")
    response = await call_next(request)
    print(request.cookies.items())
    print(request.session.items())
    print("I am a fastapi middleware after request.")
    return response
