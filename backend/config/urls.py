from django.contrib import admin
from django.urls import path, include

from core.views import home, websocket_test


urlpatterns = [

    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path(
        "api/",
        include("core.urls")
    ),


    path(
        "websocket-test/",
        websocket_test,
        name="websocket-test"
    ),
]