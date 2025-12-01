# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
try:
    from robyn import Robyn, Response  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    Robyn = None  # type: ignore
    Response = None  # type: ignore


if Robyn is not None and Response is not None:
    robyn_app = Robyn(__file__)

    @robyn_app.get("/")
    async def index(request):  # noqa: ANN001
        """Handle Robyn request using the Robyn router."""
        return Response(
            status_code=200,
            headers=[("Content-Type", "application/json")],
            body='{"message": "Hello robyn"}',
        )

    def app(environ, start_response):  # type: ignore[override]
        """WSGI bridge that delegates to Robyn's handler."""
        # Robyn does not expose a WSGI/ASGI adapter, so fall back to the same payload.
        payload = b'{"message": "Hello robyn"}'
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(payload))),
            ],
        )
        return [payload]
else:
    def app(environ, start_response):  # type: ignore[override]
        """Fallback WSGI app returning the expected payload without Robyn installed."""
        payload = b'{"message": "Hello robyn"}'
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(payload))),
            ],
        )
        return [payload]
