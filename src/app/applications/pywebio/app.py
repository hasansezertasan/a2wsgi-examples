"""PyWebIO example application."""

from fastapi import FastAPI
from pywebio.input import (  # type: ignore[import-untyped]
    input,  # ruff:ignore[builtin-import-shadowing]
)
from pywebio.output import put_text  # type: ignore[import-untyped]
from pywebio.platform.fastapi import webio_routes  # type: ignore[import-untyped]


def task_func() -> None:
    """Prompt for a name and greet the user."""
    name = input("Enter your name")
    put_text("Hello", name)


app = FastAPI(routes=webio_routes(applications=task_func))  # pyrefly: ignore
