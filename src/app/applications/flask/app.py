from flask import Flask, jsonify, make_response, request
from flask.wrappers import Response

app = Flask(__name__)


@app.after_request
def after_request(response):
    return response


@app.get(rule="/")
def index() -> Response:
    return jsonify(
        {
            "message": "Hello flask",
        },
    )


@app.post(rule="/cookie")
def set_cookie() -> Response:
    res = make_response(jsonify({"message": "Cookie set"}))
    res.set_cookie(key="application", value="flask")
    return res


@app.get(rule="/cookie")
def get_cookie() -> Response:
    return jsonify({"message": request.cookies.get("application")})


@app.get(rule="/delete-cookie")
def delete_cookie() -> Response:
    res = make_response(jsonify({"message": "Cookie deleted"}))
    res.delete_cookie(key="application")
    return res


@app.get(rule="/cookies")
def get_cookies() -> Response:
    return jsonify({"message": "cookies", "cookies": request.cookies})
