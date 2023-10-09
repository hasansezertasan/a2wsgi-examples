# [Running Flet with FastAPI | Flet](https://flet.dev/docs/guides/python/deploying-web-app/running-flet-with-fastapi/)
# [Flet for FastAPI | Flet](https://flet.dev/blog/flet-for-fastapi/)
# [flet/sdk/python/packages/flet-fastapi at main · flet-dev/flet](https://github.com/flet-dev/flet/tree/main/sdk/python/packages/flet-fastapi)
# [flet/sdk/python/pyproject.toml at main · flet-dev/flet](https://github.com/flet-dev/flet/blob/main/sdk/python/pyproject.toml)
# [flet-dev/flet-fastapi-example: Example of a Flet + FastAPI App published using Dockup](https://github.com/flet-dev/flet-fastapi-example)

import flet as ft
import flet_fastapi


async def main(page: ft.Page):
    await page.add_async(ft.Text("Hello, Flet!"))


app = flet_fastapi.app(main)
