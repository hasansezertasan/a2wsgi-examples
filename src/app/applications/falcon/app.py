"""Falcon example application."""

import falcon


class HelloResource:
    """Resource for Falcon application."""

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:  # ruff:ignore[no-self-use]
        """Handle GET request."""
        resp.media = {"message": "Hello falcon"}


app = falcon.App()
app.add_route(uri_template="/", resource=HelloResource())
