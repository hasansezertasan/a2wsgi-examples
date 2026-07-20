"""webapp2 sub-application mounted via WSGIMiddleware."""

import json
from collections.abc import Callable

try:
    import webapp2
except ImportError:  # pragma: no cover - optional dependency
    webapp2 = None  # ty: ignore[invalid-assignment]


if webapp2 is not None:

    class HelloHandler(webapp2.RequestHandler):  # type: ignore[misc]
        """Handle webapp2 request."""

        def get(self, *args: object, **kwargs: object) -> None:
            """Handle GET request."""
            self.response.headers["Content-Type"] = "application/json"  # pyright: ignore[reportOptionalMemberAccess]  # pyrefly: ignore  # ty: ignore[unresolved-attribute]
            self.response.write(json.dumps({"message": "Hello webapp2"}))  # pyright: ignore[reportOptionalMemberAccess]  # pyrefly: ignore  # ty: ignore[unresolved-attribute]

    # Match any path so mounting under a prefix still works.
    app = webapp2.WSGIApplication(routes=[(r"/.*", HelloHandler)], debug=False)  # pyright: ignore[reportAssignmentType]
else:

    def app(
        environ: dict[str, object],
        start_response: Callable[..., object],
    ) -> list[bytes]:
        """Fallback WSGI app returning the payload without webapp2 installed.

        Returns:
            list[bytes]: The response body.
        """
        payload = b'{"message": "Hello webapp2"}'
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(payload))),
            ],
        )
        return [payload]
