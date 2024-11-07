from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from ..models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(BaseAdmin):
    """UI for Invoice model."""

    ordering = (
        "id",
    )
    autocomplete_fields = (
        "supplier",
    )
    list_display = (
        "id",
        "amount_to_pay",
        "supplier",
        "deadline",
        "is_expired",
    )
    list_display_links = (
        "id",
        "supplier",
    )
    search_fields = (
        "id",
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": (
                    "amount_to_pay",
                    "supplier",
                    "deadline",
                    "is_expired",
                ),
            },
        ),
    )
    fieldsets = (
        (
            _("Main Info"), {
                "fields": (
                    "amount_to_pay",
                    "supplier",
                    "deadline",
                    "is_expired",
                ),
            },
        ),
    )