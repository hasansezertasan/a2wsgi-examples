from bottle import Bottle

app = Bottle()


@app.route("/")
def hello():
    return {
        "message": "Hello World",
    }
