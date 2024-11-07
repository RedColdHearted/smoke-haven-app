from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from ..models import InvoicePayment


@admin.register(InvoicePayment)
class InvoicePaymentAdmin(BaseAdmin):
    """UI for InvoicePayment model."""

    ordering = (
        "id",
    )
    autocomplete_fields = (
        "invoice",
    )
    list_display = (
        "id",
        "invoice",
        "paid_amount",
        "payment_type",
        "created",
    )
    list_display_links = (
        "id",
        "invoice",
    )
    search_fields = (
        "id",
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": (
                    "invoice",
                    "paid_amount",
                    "payment_type",
                ),
            },
        ),
    )
    fieldsets = (
        (
            _("Main Info"), {
                "fields": (
                    "invoice",
                    "paid_amount",
                    "payment_type",
                ),
            },
        ),
    )