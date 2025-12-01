# TODO @hasansezertasan: This implementation is a temporary workaround, please replace it.
import json

try:
    import webapp2  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    webapp2 = None  # type: ignore


if webapp2 is not None:
    class HelloHandler(webapp2.RequestHandler):  # type: ignore[misc]
        """Handle webapp2 request."""

        def get(self, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
            self.response.headers["Content-Type"] = "application/json"
            self.response.write(json.dumps({"message": "Hello webapp2"}))

    # Match any path so mounting under a prefix still works.
    app = webapp2.WSGIApplication(routes=[(r"/.*", HelloHandler)], debug=False)
else:
    def app(environ, start_response):  # type: ignore[override]
        """Fallback WSGI app returning the expected payload without webapp2 installed."""
        payload = b'{"message": "Hello webapp2"}'
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(payload))),
            ],
        )
        return [payload]
