from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProfileView, UserUpdateView

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "update-info/",
        UserUpdateView.as_view(),
        name="update_info",
    )
]
