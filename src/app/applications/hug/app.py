"""HUG example endpoint."""

import sys

import hug  # type: ignore[import]


@hug.get("/")  # type: ignore[attr-defined]
def index() -> dict:
    """Handle HUG request."""
    return {"message": "Hello hug"}


# hug exposes a WSGI-compatible app via the CLI; replicate that here.
__hug_wsgi__ = hug.run.server(sys.modules[__name__])  # type: ignore[attr-defined]
app = __hug_wsgi__
