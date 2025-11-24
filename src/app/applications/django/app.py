from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http.response import JsonResponse
from django.urls import path

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)


def index(request) -> JsonResponse:
    """Handle django request.

    Args:
        request: The incoming request.
    Returns:
        JsonResponse: The response to be sent back.
    """
    return JsonResponse(
        data={
            "message": "Hello django",
        },
    )


urlpatterns = [
    path(route="", view=index),
]

application = get_wsgi_application()
