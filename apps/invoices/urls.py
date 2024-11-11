from django.urls import path

from .views import (
    ListInvoiceView,
    CreateInvoiceView,
    DetailInvoiceView,
    DeleteInvoiceView,
    UpdateInvoiceView,
    DownloadDocumentView,
    DeleteDocumentView,
    UploadDocumentByInvoiceView,
    InvoicePaymentCreateView,
    DeleteInvoicePaymentView,
)

app_name = "invoices"

urlpatterns = [
    path(
        "<int:pk>/",
        DetailInvoiceView.as_view(),
        name="detail_invoice",
    ),
    path(
        "",
        ListInvoiceView.as_view(),
        name="invoices",
    ),
    path(
        "create/",
        CreateInvoiceView.as_view(),
        name="create_invoice",
    ),
    path(
        "delete/<int:pk>/",
        DeleteInvoiceView.as_view(),
        name="delete_invoice",
    ),
    path(
        "update/<int:pk>/",
        UpdateInvoiceView.as_view(),
        name="update_invoice",
    ),
    path(
        'documents/download/<int:pk>/',
        DownloadDocumentView.as_view(),
        name='document_download'
    ),
    path(
        'documents/delete/<int:pk>/',
        DeleteDocumentView.as_view(),
        name='document_delete'
    ),
    path(
        'documents/upload_by_invoice/<int:invoice_id>/',
        UploadDocumentByInvoiceView.as_view(),
        name='document_upload_by_invoice'
    ),
    path(
        'invoices/invoice_payment/create/<int:invoice_id>/',
        InvoicePaymentCreateView.as_view(),
        name='create_invoice_payment',
    ),
    path(
        "invoices/invoice_payment/delete/<int:pk>/",
        DeleteInvoicePaymentView.as_view(),
        name="delete_invoice_payment",
    ),
]
