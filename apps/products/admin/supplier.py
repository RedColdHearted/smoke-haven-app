from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from ..models import Supplier


@admin.register(Supplier)
class SupplierAdmin(BaseAdmin):
    """UI for Supplier model."""

    ordering = (
        "name",
    )
    list_display = (
        "id",
        "name",
        "inn",
        "bik",
        "phone_number",
    )
    list_display_links = (
        "name",
        "inn",
        "bik",
        "phone_number",
    )
    search_fields = (
        "id",
        "name",
        "inn",
        "bik",
        "phone_number",
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "inn",
                    "bik",
                    "phone_number",
                ),
            },
        ),
    )
    fieldsets = (
        (
            _("Main Info"), {
                "fields": (
                    "name",
                    "inn",
                    "bik",
                    "phone_number",
                ),
            },
        ),
    )