from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from django.urls import path

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)


def index(request):
    return JsonResponse(
        data={
            "message": "Hello django",
        },
    )


urlpatterns = [
    path("", index),
]

application = get_wsgi_application()
