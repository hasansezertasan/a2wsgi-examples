# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
from tornado.escape import json_encode


def app(environ, start_response):  # type: ignore[override]
    """Minimal Tornado-powered WSGI app."""
    body = json_encode({"message": "Hello tornado"}).encode()
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]
