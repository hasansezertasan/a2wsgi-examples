"""Pyramid example application."""

from pyramid.config import Configurator  # type: ignore[import-untyped]
from pyramid.response import Response  # type: ignore[import-untyped]


def hello_pyramid(request: object) -> Response:
    """Handle Pyramid request.

    Returns:
        Response: The response to be sent back.
    """
    return Response(json_body={"message": "Hello pyramid"})


with Configurator() as config:
    config.add_route(name="home", pattern="/")
    config.add_view(view=hello_pyramid, route_name="home", renderer="json")
    app = config.make_wsgi_app()
