# a2wsgi Examples

The purpose of this project is to provide examples of how we can use (integrate) different Python Web Frameworks together using [a2wsgi][a2wsgi].

## Why

Who likes migration? But in some cases, it's necessary. [a2wsgi] helps us to convert our ASGI applications to WSGI or vice versa.

A Scenario (that I have faced): You have a Flask application and you want to migrate it to FastAPI. You have two options:

1. Rewrite the whole application from scratch and deploy it when it's ready.
2. Use [a2wsgi] to convert your Flask application to WSGI using [a2wsgi] and then integrate (mount) it to your FastAPI application and deploy it. By the time, you can rewrite your application step by step.

## Progress

### Frameworks

| Framework  | Mount                 | Protocol  | Documentation                                                                                                             |
| ---------- | --------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| Flask      | :white_check_mark:    | ASGI/WSGI | [Application Dispatching — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/patterns/appdispatch/) |
| FastAPI    | :white_check_mark:    | ASGI/WSGI | [Sub Applications - Mounts - FastAPI](https://fastapi.tiangolo.com/advanced/sub-applications/)                            |
| Django     | :white_check_mark:    | ASGI/WSGI |                                                                                                                           |
| Starlette  | :white_check_mark:    | ASGI/WSGI |                                                                                                                           |
| Litestar   | :white_check_mark:    | ASGI/WSGI |                                                                                                                           |
| BlackSheep | :x:                   | ASGI      |                                                                                                                           |
| Quart      | :x:                   | ASGI      |                                                                                                                           |
| Falcon     | :x:                   | ASGI/WSGI |                                                                                                                           |
| Sanic      | :white_square_button: | ASGI      |                                                                                                                           |
| Connexion  | :white_square_button: | ASGI      |                                                                                                                           |
| Bottle     | :white_check_mark:    | WSGI      |                                                                                                                           |
| Robyn      | :x:                   |           |                                                                                                                           |
| HUG        | :x:                   |           |                                                                                                                           |
| Tornado    | :x:                   |           |                                                                                                                           |
| Pyramid    | :white_square_button: | WSGI      |                                                                                                                           |
| webapp2    | :white_square_button: |           |                                                                                                                           |
| aiohttp    | :warning:             |           |                                                                                                                           |

More WSGI: [Frameworks that run on WSGI — WSGI.org](https://wsgi.readthedocs.io/en/latest/frameworks.html)

More ASGI: [Implementations — ASGI 3.0 documentation](https://asgi.readthedocs.io/en/latest/implementations.html)

### Other tools

| Framework   | Mount                 |
| ----------- | --------------------- |
| GradIO      | :white_check_mark:    |
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

- Docker
- Docker Compose

### Steps

1. Clone the repository
2. Run `docker-compose up --build`
3. Go to `http://localhost:80/docs` to see the API documentation
4. Enjoy!

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Author

- [hasansezertasan](https://www.github.com/hasansezertasan), It's me :wave:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- Links -->
[a2wsgi]: https://github.com/abersheeran/a2wsgi
