from django.urls import path

from .views import CreateSupplierView, ListSupplierView, UpdateSupplierView

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
    path(
        "suppliers/update/<int:pk>/",
        UpdateSupplierView.as_view(),
        name="update_supplier",
    ),
]