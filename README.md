# a2wsgi Examples

The purpose of this project is to provide examples of how we can use (integrate) different Python Web Frameworks together using [a2wsgi][a2wsgi].

## Why

Who likes migration? But in some cases, it's necessary. [a2wsgi] helps us to convert our ASGI applications to WSGI or vice versa.

A Scenario (that I have faced): You have a Flask application and you want to migrate it to FastAPI. You have two options:

1. Rewrite the whole application from scratch and deploy it when it's ready.
2. Use [a2wsgi] to convert your Flask application to WSGI using [a2wsgi] and then integrate (mount) it to your FastAPI application and deploy it. By the time, you can rewrite your application step by step.

## Progress

### Frameworks

| Framework  | Mount              | Protocol | Notes                                                 |
| ---------- | ------------------ | -------- | ----------------------------------------------------- |
| Flask      | :white_check_mark: | WSGI     | Full app with cookie endpoints                        |
| FastAPI    | :white_check_mark: | ASGI     | Full app with cookie endpoints                        |
| Django     | :white_check_mark: | WSGI     |                                                       |
| Starlette  | :white_check_mark: | ASGI     |                                                       |
| Litestar   | :white_check_mark: | ASGI     |                                                       |
| BlackSheep | :white_check_mark: | ASGI     | ASGI shim — requires own lifecycle for full app mount |
| Quart      | :white_check_mark: | ASGI     |                                                       |
| Falcon     | :white_check_mark: | WSGI     |                                                       |
| Sanic      | :white_check_mark: | ASGI     | ASGI shim — manages own event loop                    |
| Connexion  | :white_check_mark: | ASGI     | Fallback shim when not installed                      |
| Bottle     | :white_check_mark: | WSGI     |                                                       |
| Robyn      | :white_check_mark: | WSGI     | WSGI shim — no WSGI/ASGI adapter available            |
| HUG        | :white_check_mark: | WSGI     |                                                       |
| Tornado    | :white_check_mark: | WSGI     | WSGI shim — runs own IOLoop, no adapter               |
| Pyramid    | :white_check_mark: | WSGI     |                                                       |
| webapp2    | :white_check_mark: | WSGI     | Fallback shim when not installed                      |
| aiohttp    | :white_check_mark: | ASGI     | ASGI shim — no native ASGI sub-app mounting           |

### Other tools

| Framework   | Mount                 |
| ----------- | --------------------- |
| Gradio      | :white_check_mark:    |
| PyWebIO     | :white_check_mark:    |
| Flet        | :white_check_mark:    |
| NiceGUI     | :construction:        |
| Reflex      | :construction:        |
| Streamlit   | :white_square_button: |
| Plotly Dash | :white_square_button: |

Emoji key:

- :white_check_mark:: Accomplished
- :white_square_button:: Not tried yet
- :x:: Tried and failed
- :construction:: In progress
- :warning:: Not sure if possible

## How to run

### Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- Docker & Docker Compose (optional)

### Local development

```bash
uv sync
uv run uvicorn app.main:app --reload
```

### Docker

```bash
docker compose up --build
```

Go to `http://localhost:8000/docs` to see the API documentation.

### Running tests

```bash
uv run pytest tests/ -v
```

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

### Further Reading

- [Frameworks that run on WSGI — WSGI.org](https://wsgi.readthedocs.io/en/latest/frameworks.html)
- [Implementations — ASGI 3.0 documentation](https://asgi.readthedocs.io/en/latest/implementations.html)
- [Application Dispatching — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/patterns/appdispatch/)
- [Sub Applications - Mounts - FastAPI](https://fastapi.tiangolo.com/advanced/sub-applications/)

## Author

- [hasansezertasan](https://www.github.com/hasansezertasan), It's me :wave:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- Links -->

[a2wsgi]: https://github.com/abersheeran/a2wsgi
