"""Flask example application."""

from flask import Flask, jsonify, make_response, request
from flask.wrappers import Response

app = Flask(__name__)


@app.after_request
def after_request(response: Response) -> Response:
    """Return the response unchanged after each request.

    Returns:
        Response: The unchanged response.
    """
    return response


@app.get(rule="/")
def index() -> Response:
    """Handle Flask request.

    Returns:
        Response: The response to be sent back.
    """
    return jsonify(
        {
            "message": "Hello flask",
        },
    )


@app.post(rule="/cookie")
def set_cookie() -> Response:
    """Set a cookie and return a confirmation message.

    Returns:
        Response: The response to be sent back.
    """
    res = make_response(jsonify({"message": "Cookie set"}))
    res.set_cookie(key="application", value="flask")
    return res


@app.get(rule="/cookie")
def get_cookie() -> Response:
    """Return the value of the ``application`` cookie.

    Returns:
        Response: The response to be sent back.
    """
    return jsonify({"message": request.cookies.get("application")})


@app.get(rule="/delete-cookie")
def delete_cookie() -> Response:
    """Delete the cookie and return a confirmation message.

    Returns:
        Response: The response to be sent back.
    """
    res = make_response(jsonify({"message": "Cookie deleted"}))
    res.delete_cookie(key="application")
    return res


@app.get(rule="/cookies")
def get_cookies() -> Response:
    """Return all cookies sent with the request.

    Returns:
        Response: The response to be sent back.
    """
    return jsonify({"message": "cookies", "cookies": request.cookies})
