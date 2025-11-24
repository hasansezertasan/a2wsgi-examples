"""Schema definitions for the application."""

import enum


class Applications(str, enum.Enum):
    """Enum for supported applications."""

    FLASK = "flask"
    DJANGO = "django"
    FASTAPI = "fastapi"
    STARLETTE = "starlette"
    LITESTAR = "litestar"
    BOTTLE = "bottle"
    GRADIO = "gradio"
    PYWEBIO = "pywebio"
    AIOHTTP = "aiohttp"
    QUART = "quart"
    SANIC = "sanic"
    TORNADO = "tornado"
    FLET = "flet"
