from django.contrib import admin

from apps.core.admin import BaseAdmin

from ..models import Document


@admin.register(Document)
class DocumentAdmin(BaseAdmin):
    """UI for document model."""

    ordering = ("id",)
    readonly_fields = (
        "content_object",
    )
    list_display = (
        "id",
        "object_id",
        "content_type",
    )
    list_display_links = (
        "id",
        "object_id",
        "content_type",
    )
    search_fields = (
        "id",
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": (
                    "content_object",
                ),
            },
        ),
    )