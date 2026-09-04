from django.urls import path

from .views import (
    register_user,
    login_user,
    projects,
    tasks,
    comments,
    notifications,
    websocket_test,
)


urlpatterns = [

    path(
        "register/",
        register_user,
        name="register"
    ),

    path(
        "login/",
        login_user,
        name="login"
    ),

    path(
        "projects/",
        projects,
        name="projects"
    ),

    path(
        "tasks/",
        tasks,
        name="tasks"
    ),

    path(
        "comments/",
        comments,
        name="comments"
    ),

    path(
        "notifications/",
        notifications,
        name="notifications"
    ),

    path(
        "websocket-test/",
        websocket_test,
        name="websocket-test"
    ),
]