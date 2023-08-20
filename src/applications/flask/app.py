from flask import Flask, jsonify, make_response, request, session

app = Flask(__name__)


@app.before_request
def before_request():
    print("I am a flask middleware before request.")


@app.after_request
def after_request(response):
    print(f"Flask Cookies: {request.cookies}")
    print(f"Flask Session: {session.items()}")
    print("I am a flask middleware after request.")
    return response


@app.get("/")
def index():
    return jsonify(
        {
            "message": "Hello World",
        },
    )


@app.post("/cookie")
def set_cookie():
    res = make_response(jsonify({"message": "Cookie set"}))
    res.set_cookie(key="application", value="flask")
    return res


@app.get("/cookie")
def get_cookie():
    return jsonify({"message": request.cookies.get("application")})


@app.get("/delete-cookie")
def delete_cookie():
    res = make_response(jsonify({"message": "Cookie deleted"}))
    res.delete_cookie(key="application")
    return res


@app.get("/cookies")
def get_cookies():
    print(request.cookies)
    return jsonify({"message": "cookies", "cookies": request.cookies})
