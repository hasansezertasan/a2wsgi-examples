from fastapi import FastAPI
from pywebio.input import input
from pywebio.output import put_text
from pywebio.platform.fastapi import webio_routes


def task_func():
    name = input("Enter your name")
    put_text("Hello", name)


app = FastAPI(routes=webio_routes(task_func))
