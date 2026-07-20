"""HUG example endpoint."""

import sys

import hug  # type: ignore[import-untyped]


@hug.get("/")  # type: ignore[untyped-decorator]
def index() -> dict:  # type: ignore[type-arg]  # hug reads this annotation at runtime; a parametrized generic changes behavior
    """Handle HUG request.

    Returns:
        dict: The response to be sent back.
    """
    return {"message": "Hello hug"}


# hug exposes a WSGI-compatible app via the CLI; replicate that here.
__hug_wsgi__ = hug.run.server(sys.modules[__name__])
app = __hug_wsgi__
