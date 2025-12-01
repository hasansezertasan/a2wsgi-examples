try:
    import connexion
except ImportError:  # pragma: no cover - optional dependency
    connexion = None


def hello() -> dict[str, str]:
    """Handle Connexion request."""
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
        resolver_error=Exception,
    )
    # Expose the ASGI-compatible Connexion app.
    app = connexion_app  # type: ignore[assignment]
else:
    async def app(scope, receive, send):  # type: ignore[override]
        """Fallback ASGI app returning the expected payload without Connexion installed."""
        if scope["type"] != "http":
            raise RuntimeError("Connexion demo only supports HTTP.")
        payload = b'{"message": "Hello connexion"}'
        headers = [
            (b"content-type", b"application/json"),
            (b"content-length", str(len(payload)).encode("latin-1")),
        ]
        await send({"type": "http.response.start", "status": 200, "headers": headers})
        await send({"type": "http.response.body", "body": payload, "more_body": False})
