from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Document(BaseModel):
    """Represent document in db."""

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField(
        verbose_name=_("Object ID"),
    )
    content_object = GenericForeignKey(
        "content_type",
        "object_id",
    )
    file = models.FileField(
        upload_to=settings.DEFAULT_MEDIA_PATH
    )

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    def __str__(self) -> str:
        return f"{self.id}"