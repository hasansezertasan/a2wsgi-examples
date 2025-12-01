"""Application."""

from collections.abc import Awaitable, Callable

from a2wsgi import WSGIMiddleware
from fastapi import FastAPI, Request, Response
from starlette.middleware.sessions import SessionMiddleware

from app.applications.aiohttp.app import app as aiohttp_app
from app.applications.blacksheep.app import app as blacksheep_app
from app.applications.bottle.app import app as bottle_app
from app.applications.connexion.app import app as connexion_app
from app.applications.django.app import application as django_application
from app.applications.falcon.app import app as falcon_app
from app.applications.fastapi.app import app as fastapi_app
from app.applications.fastapi.router import router as fastapi_router
from app.applications.flask.app import app as flask_app
from app.applications.flet.app import app as flet_app
from app.applications.gradio.app import app as gradio_app
from app.applications.hug.app import app as hug_app
from app.applications.litestar.app import app as litestar_app
from app.applications.pyramid.app import app as pyramid_app
from app.applications.quart.app import app as quart_app
from app.applications.pywebio.app import app as pywebio_app
from app.applications.robyn.app import app as robyn_app
from app.applications.sanic.app import app as sanic_app
from app.applications.starlette.app import app as starlette_app
from app.applications.tornado.app import app as tornado_app
from app.applications.webapp2.app import app as webapp2_app

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
    app=aiohttp_app,
    name="aiohttp",
)
app.mount(
    path="/fastapi",
    app=fastapi_app,
    name="fastapi",
)
app.mount(
    path="/blacksheep",
    app=blacksheep_app,
    name="blacksheep",
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
    path="/falcon",
    app=WSGIMiddleware(falcon_app),
    name="falcon",
)
app.mount(
    path="/connexion",
    app=connexion_app,
    name="connexion",
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
    path="/hug",
    app=WSGIMiddleware(hug_app),
    name="hug",
)
app.mount(
    path="/robyn",
    app=WSGIMiddleware(robyn_app),
    name="robyn",
)
app.mount(
    path="/webapp2",
    app=WSGIMiddleware(webapp2_app),
    name="webapp2",
)
app.mount(
    path="/pywebio",
    app=pywebio_app,
    name="pywebio",
)
app.mount(
    path="/quart",
    app=quart_app,
    name="quart",
)
app.mount(
    path="/sanic",
    app=sanic_app,
    name="sanic",
)
app.mount(
    path="/pyramid",
    app=WSGIMiddleware(pyramid_app),
    name="pyramid",
)
app.mount(
    path="/tornado",
    app=WSGIMiddleware(tornado_app),
    name="tornado",
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
