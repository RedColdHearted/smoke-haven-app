from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "login/",
        CustomLoginView.as_view(
            template_name="users/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
]