from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.errors import AuthenticationError

from authentication.views import router as authentication_router
from orders.views import router as orders_router

api_v1 = NinjaAPI(version="1.0.0")

api_v1.add_router("/orders/", orders_router)
api_v1.add_router("/authentication/", authentication_router)


def auth_error_exception_handler(request, exc):
    data = {
        "message": "AuthenticationError",
        "success": False,
        "data": None,
    }
    response = api_v1.create_response(request, data, status=401)
    return response


api_v1.exception_handler(AuthenticationError)(auth_error_exception_handler)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api_v1.urls),
]
