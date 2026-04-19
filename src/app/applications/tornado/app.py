"""Tornado sub-application mounted via WSGIMiddleware.

Tornado runs its own IOLoop and does not expose a standard WSGI/ASGI adapter
for sub-app mounting. This provides a minimal WSGI app that uses Tornado's
json_encode for consistent serialization.
"""

from tornado.escape import json_encode


def app(environ, start_response):  # type: ignore[override]
    """Minimal WSGI app — Tornado has no WSGI adapter for sub-app mounting."""
    body = json_encode({"message": "Hello tornado"}).encode()
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]
