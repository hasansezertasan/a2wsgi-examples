"""Robyn sub-application mounted via WSGIMiddleware.

Robyn does not expose a WSGI/ASGI adapter, so this provides a minimal
WSGI app that returns the expected JSON payload.
"""


def app(environ, start_response):  # type: ignore[override]
    """Minimal WSGI app — Robyn has no WSGI/ASGI adapter."""
    payload = b'{"message": "Hello robyn"}'
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(payload))),
        ],
    )
    return [payload]
