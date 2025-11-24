from bottle import Bottle

app = Bottle()


@app.route(path="/")
def hello() -> dict[str, str]:
    """Handle bottle request.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    return {
        "message": "Hello bottle",
    }
