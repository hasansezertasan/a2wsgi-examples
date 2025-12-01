"""Schema definitions for the application."""

import enum


class Applications(str, enum.Enum):
    """Enum for supported applications."""

    BLACKSHEEP = "blacksheep"
    FLASK = "flask"
    DJANGO = "django"
    FASTAPI = "fastapi"
    STARLETTE = "starlette"
    LITESTAR = "litestar"
    BOTTLE = "bottle"
    GRADIO = "gradio"
    HUG = "hug"
    PYWEBIO = "pywebio"
    AIOHTTP = "aiohttp"
    QUART = "quart"
    SANIC = "sanic"
    FALCON = "falcon"
    PYRAMID = "pyramid"
    TORNADO = "tornado"
    ROBYN = "robyn"
    WEBAPP2 = "webapp2"
    FLET = "flet"
