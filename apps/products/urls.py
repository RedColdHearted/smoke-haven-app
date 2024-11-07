from django.urls import path

from .views import CreateSupplierView, ListSupplierView

app_name = "products"

urlpatterns = [
    path(
        "suppliers/list/",
        ListSupplierView.as_view(),
        name="suppliers",
    ),
    path(
        "suppliers/create/",
        CreateSupplierView.as_view(),
        name="create_supplier",
    ),
]