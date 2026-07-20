"""Robyn sub-application mounted via WSGIMiddleware.

Robyn does not expose a WSGI/ASGI adapter, so this provides a minimal
WSGI app that returns the expected JSON payload.
"""

from collections.abc import Callable


def app(
    environ: dict[str, object],
    start_response: Callable[..., object],
) -> list[bytes]:
    """Minimal WSGI app — Robyn has no WSGI/ASGI adapter.

    Returns:
        list[bytes]: The response body.
    """
    payload = b'{"message": "Hello robyn"}'
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(payload))),
        ],
    )
    return [payload]
