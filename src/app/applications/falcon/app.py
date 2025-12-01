import falcon


class HelloResource:
    """Resource for Falcon application."""

    def on_get(self, req, resp) -> None:  # noqa: ARG002
        """Handle GET request."""
        resp.media = {"message": "Hello falcon"}


app = falcon.App()
app.add_route(uri_template="/", resource=HelloResource())
