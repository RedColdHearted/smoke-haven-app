from django.contrib import admin
from django.urls import path, include,re_path 
from django.contrib.auth import views as auth_views

from two_factor.urls import urlpatterns as tf_urls
from debug_toolbar.toolbar import debug_toolbar_urls

from apps.core.views import IndexView, protected_serve


urlpatterns = [
    path("two_factor/", include(tf_urls)),
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "users/",
        include("apps.users.urls"),
    ),
    path(
        "products/",
        include("apps.products.urls"),
    ),
    path(
        "invoices/",
        include("apps.invoices.urls"),
    ),
]

urlpatterns += debug_toolbar_urls()
urlpatterns += re_path(
    r'^media/(?P<path>.*)$',
    protected_serve,
    name='protected_media',
),

urlpatterns += (
        path(
            "admin/",
            admin.site.urls,
        ),
    )

urlpatterns += [
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]