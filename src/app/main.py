"""Application."""

from typing import TYPE_CHECKING, cast

from a2wsgi import WSGIMiddleware
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.types import ASGIApp

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
from app.applications.pywebio.app import app as pywebio_app
from app.applications.quart.app import app as quart_app
from app.applications.robyn.app import app as robyn_app
from app.applications.sanic.app import app as sanic_app
from app.applications.starlette.app import app as starlette_app
from app.applications.tornado.app import app as tornado_app
from app.applications.webapp2.app import app as webapp2_app

if TYPE_CHECKING:
    from a2wsgi.wsgi_typing import WSGIApp


def _asgi(application: object) -> ASGIApp:
    """Assert that a mounted framework app satisfies the ASGI interface.

    The mounted apps are valid ASGI callables at runtime, but their static
    signatures do not match Starlette's strict ``ASGIApp`` protocol, so this
    cast bridges the gap that type checkers cannot prove.

    Returns:
        The same application, typed as ``ASGIApp``.
    """
    return cast("ASGIApp", application)


def _wsgi(application: object) -> ASGIApp:
    """Wrap a WSGI app as ASGI for mounting.

    Frameworks expose slightly different WSGI callable signatures than the one
    ``a2wsgi`` declares, so the input is cast to ``WSGIApp`` before wrapping and
    the result is bridged to ``ASGIApp`` (see :func:`_asgi`).

    Returns:
        The WSGI application wrapped as an ``ASGIApp``.
    """
    return cast("ASGIApp", WSGIMiddleware(cast("WSGIApp", application)))


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
app.add_middleware(
    SessionMiddleware,
    secret_key="demo-secret-key-not-for-production",  # ruff:ignore[hardcoded-password-func-arg]
)
app.mount(
    path="/aiohttp",
    app=_asgi(aiohttp_app),
    name="aiohttp",
)
app.mount(
    path="/fastapi",
    app=_asgi(fastapi_app),
    name="fastapi",
)
app.mount(
    path="/blacksheep",
    app=_asgi(blacksheep_app),
    name="blacksheep",
)
app.include_router(
    router=fastapi_router,
    tags=["Default"],
)
app.mount(
    path="/flask",
    app=_wsgi(flask_app),
    name="flask",
)
app.mount(
    path="/flet",
    app=_asgi(flet_app),
    name="flet",
)
app.mount(
    path="/django",
    app=_wsgi(django_application),
    name="django",
)
app.mount(
    path="/bottle",
    app=_wsgi(bottle_app),
    name="bottle",
)
app.mount(
    path="/falcon",
    app=_wsgi(falcon_app),
    name="falcon",
)
app.mount(
    path="/connexion",
    app=_asgi(connexion_app),
    name="connexion",
)
app.mount(
    path="/litestar",
    app=_asgi(litestar_app),
    name="litestar",
)
app.mount(
    path="/gradio",
    app=_asgi(gradio_app),
    name="gradio",
)
app.mount(
    path="/hug",
    app=_wsgi(hug_app),
    name="hug",
)
app.mount(
    path="/robyn",
    app=_wsgi(robyn_app),
    name="robyn",
)
app.mount(
    path="/webapp2",
    app=_wsgi(webapp2_app),
    name="webapp2",
)
app.mount(
    path="/pywebio",
    app=_asgi(pywebio_app),
    name="pywebio",
)
app.mount(
    path="/quart",
    app=_asgi(quart_app),
    name="quart",
)
app.mount(
    path="/sanic",
    app=_asgi(sanic_app),
    name="sanic",
)
app.mount(
    path="/pyramid",
    app=_wsgi(pyramid_app),
    name="pyramid",
)
app.mount(
    path="/tornado",
    app=_wsgi(tornado_app),
    name="tornado",
)
app.mount(
    path="/starlette",
    app=_asgi(starlette_app),
    name="starlette",
)
