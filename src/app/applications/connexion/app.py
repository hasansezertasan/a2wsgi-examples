"""Connexion example application."""

from collections.abc import Awaitable, Callable

try:
    import connexion
except ImportError:  # pragma: no cover - optional dependency
    connexion = None  # ty: ignore[invalid-assignment]


def hello() -> dict[str, str]:
    """Handle Connexion request.

    Returns:
        dict[str, str]: The response to be sent back.
    """
    return {"message": "Hello connexion"}


if connexion is not None:
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "Connexion Demo", "version": "1.0.0"},
        "paths": {
            "/": {
                "get": {
                    "operationId": f"{__name__}.hello",
                    "responses": {
                        "200": {
                            "description": "ok",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {"type": "string"},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    connexion_app = connexion.App(__name__, specification_dir=".")
    connexion_app.add_api(
        spec,
        validate_responses=False,
        strict_validation=False,
    )
    # Expose the ASGI-compatible Connexion app.
    app = connexion_app  # pyright: ignore[reportAssignmentType]
else:

    async def app(
        scope: dict[str, object],
        receive: object,
        send: Callable[..., Awaitable[None]],
    ) -> None:
        """Fallback ASGI app when Connexion is not installed.

        Raises:
            RuntimeError: If the ASGI scope type is not ``http``.
        """
        if scope["type"] != "http":
            msg = "Connexion demo only supports HTTP."
            raise RuntimeError(msg)
        payload = b'{"message": "Hello connexion"}'
        headers = [
            (b"content-type", b"application/json"),
            (b"content-length", str(len(payload)).encode("latin-1")),
        ]
        await send({"type": "http.response.start", "status": 200, "headers": headers})
        await send({"type": "http.response.body", "body": payload, "more_body": False})
