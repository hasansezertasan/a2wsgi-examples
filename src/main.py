from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.wsgi import WSGIMiddleware

from src.applications.django.app import application as django_application
from src.applications.fastapi.app import app as fastapi_app
from src.applications.fastapi.router import router as fastapi_router
from src.applications.flask.app import app as sub_app
from src.applications.gradio.app import app as gradio_app
from src.applications.pywebio.app import app as pywebio_app
from src.applications.starlette.app import app as starlette_app
from src.applications.tornado.app import app as tornado_app

app = FastAPI(
    title="FastAPI Mount Examples",
    description="The goal of this project is to provide examples of how to mount sub applications written in different frameworks to FastAPI. \n Available sub applications: \n - FastAPI \n - Flask \n - Django \n - Tornado \n - Starlette \n - Gradio \n - PyWebIO",
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
    path="/fastapi",
    app=fastapi_app,
    name="fastapi",
)
app.mount(
    path="/flask",
    app=WSGIMiddleware(sub_app),
    name="flask",
)
app.mount(
    path="/django",
    app=WSGIMiddleware(django_application),
    name="django",
)
app.mount(
    path="/tornado",
    app=WSGIMiddleware(tornado_app),
    # app=tornado_app,
    name="tornado",
)
app.mount(
    path="/starlette",
    app=starlette_app,
    name="starlette",
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
app.include_router(
    router=fastapi_router,
    tags=["Default"],
)


@app.middleware("http")
async def middleware(request: Request, call_next):
    print("I am a fastapi middleware before request.")
    response = await call_next(request)
    print(request.cookies.items())
    print(request.session.items())
    print("I am a fastapi middleware after request.")
    return response
