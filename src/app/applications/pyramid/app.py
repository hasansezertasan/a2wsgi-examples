from pyramid.config import Configurator
from pyramid.response import Response


def hello_pyramid(request):  # noqa: ANN001
    """Handle Pyramid request."""
    return Response(json_body={"message": "Hello pyramid"})


with Configurator() as config:
    config.add_route(name="home", pattern="/")
    config.add_view(view=hello_pyramid, route_name="home", renderer="json")
    app = config.make_wsgi_app()
