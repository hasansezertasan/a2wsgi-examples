from quart.wrappers.response import Response


from quart import Quart, jsonify

app = Quart(import_name=__name__)


@app.get(rule="/")
async def index() -> Response:
    """Handle Quart request."""
    return jsonify({"message": "Hello quart"})
