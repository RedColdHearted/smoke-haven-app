from django.contrib import admin
from django.urls import path, include,re_path 
from django.conf import settings


from debug_toolbar.toolbar import debug_toolbar_urls

from apps.core.views import IndexView, protected_serve

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
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