# FastAPI Mount Examples

The goal of this project is to provide examples to integrate / use as sub application written in different frameworks with FastAPI.

## Progress

| Framework   | Mount |  Support  |
| :---------- | :---: | :-------: |
| Flask       |   ✅   | ASGI/WSGI |
| FastAPI     |   ✅   | ASGI/WSGI |
| Django      |   ✅   | WSGI      |
| Starlette   |   ✅   | ASGI/WSGI |
| Bottle      |   ✅   | WSGI      |
| Litestar    |   ✅   |           |
| BlackSheep  |   ❌   |           |
| Quart       |   ❌   |           |
| Robyn       |   ❌   |           |
| Falcon      |   ❌   |           |
| HUG         |   ❌   |           |
| Tornado     |   ❌   |           |
| Sanic       |   🔳   |           |
| Pyramid     |   🔳   |           |
| webapp2     |   🔳   |           |
| aiohttp     |   ⚠️   |           |
| GradIO      |   ✅   |           |
| PyWebIO     |   ✅   |           |
| Flet        |   ✅   |           |
| NiceGUI     |   🚧   |           |
| Reflex      |   🚧   |           |
| Streamlit   |   🔳   |           |
| Plotly Dash |   🔳   |           |

Emoji key:

- ✅: Accomplished
- 🔳: Not tried yet
- ❌: Tried and failed
- 🚧: In progress
- ⚠️: Not sure if possible

## Why

Migration process is not likable but in some cases, necessary. `a2wsgi` offers us to migrate our web applications with ease.

## How to run

### Requirements

- Docker
- Docker Compose

### Steps

1. Clone the repository
2. Run `docker-compose up --build`
3. Go to `http://localhost:8000/docs` to see the API documentation
4. Enjoy!

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Author

- [hasansezertasan](https://www.github.com/hasansezertasan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

It's an open source project mainly for educational purposes. Feel free to use it however you want.
