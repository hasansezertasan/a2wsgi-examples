# [Running Flet with FastAPI | Flet](https://flet.dev/docs/guides/python/deploying-web-app/running-flet-with-fastapi/)
# [Flet for FastAPI | Flet](https://flet.dev/blog/flet-for-fastapi/)
# [flet/sdk/python/packages/flet-fastapi at main · flet-dev/flet](https://github.com/flet-dev/flet/tree/main/sdk/python/packages/flet-fastapi)
# [flet/sdk/python/pyproject.toml at main · flet-dev/flet](https://github.com/flet-dev/flet/blob/main/sdk/python/pyproject.toml)
# [flet-dev/flet-fastapi-example: Example of a Flet + FastAPI App published using Dockup](https://github.com/flet-dev/flet-fastapi-example)

import flet as ft


def main(page: ft.Page) -> None:
    page.add(ft.Text(value="Hello, Flet!"))


app = ft.app(target=main, export_asgi_app=True)
