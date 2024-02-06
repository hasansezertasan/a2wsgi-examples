# a2wsgi Examples

The goal of this project is to provide examples about integrating different Python Web Frameworks and how they can be used together with `a2wsgi`.

## Why

Who likes migration? But in some cases, it's necessary. `a2wsgi` helps us to convert our ASGI applications to WSGI or vice versa.

A Scenerio: You have a Flask application and you want to migrate it to FastAPI.

You have two options:

1. Rewrite the whole application from scratch and deploy it when it's ready.
2. Use `a2wsgi` to convert your Flask application to WSGI using `a2wsgi` and then integrate (mount) it to your FastAPI application and deploy it. By the time, you can rewrite your application step by step.

> This was the scenerio that I faced.

## Progress

### Frameworks

| Framework  | Mount                 | Protocol  |
| ---------- | --------------------- | --------- |
| Flask      | :white_check_mark:    | ASGI/WSGI |
| FastAPI    | :white_check_mark:    | ASGI/WSGI |
| Django     | :white_check_mark:    | WSGI      |
| Starlette  | :white_check_mark:    | ASGI/WSGI |
| Bottle     | :white_check_mark:    | WSGI      |
| Litestar   | :white_check_mark:    |           |
| BlackSheep | :x:                   |           |
| Quart      | :x:                   |           |
| Robyn      | :x:                   |           |
| Falcon     | :x:                   |           |
| HUG        | :x:                   |           |
| Tornado    | :x:                   |           |
| Sanic      | :white_square_button: |           |
| Pyramid    | :white_square_button: |           |
| webapp2    | :white_square_button: |           |
| aiohttp    | :warning:             |           |

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
3. Go to `http://localhost:8000/docs` to see the API documentation
4. Enjoy!

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Author

- [hasansezertasan](https://www.github.com/hasansezertasan), It's me :wave:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
