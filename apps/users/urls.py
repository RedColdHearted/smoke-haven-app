from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProfileView, UserInitialsUpdateView, UserAvatarUpdateView

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
        "update-initials/",
        UserInitialsUpdateView.as_view(),
        name="update_initials",
    ),
    path(
        "update-avatar/",
        UserAvatarUpdateView.as_view(),
        name="update_avatar",
    )
]
