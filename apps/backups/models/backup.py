from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Backup(BaseModel):
    """Represent backup in db."""

    class CreationType(models.TextChoices):
        """String based enum for creation type choice."""

        MANUAL = "Manual", _("Manual")
        ASYNC_TASK = "Async task", _("Async task")

    creating_type = models.CharField(
        choices=CreationType.choices,
        verbose_name=_("Creating type"),
        max_length=20,
    )
    drive_url = models.CharField(
        verbose_name=_("Drive url"),
        help_text=_("A url with backup's folder on Google drive"),
        max_length=120,
    )
    folder_id = models.CharField(
        verbose_name=_("Folder id"),
        help_text=_("An id of backup's folder on Google drive"),
        max_length=120,
    )
    class BackupStatus(models.TextChoices):
        """String based enum for creation type choice."""

        PENDING = "Pending", _("Pending")
        IN_PROGRESS = "In progress", _("In progress")
        DONE = "Done", _("Done")

    status = models.CharField(
        choices=BackupStatus.choices,
        verbose_name=_("Status"),
        default=BackupStatus.PENDING.value,
        max_length=20,
    )

    class Meta:
        verbose_name = _("Backup")
        verbose_name_plural = _("Backups")

    def __str__(self) -> str:
        return f"{self.id}"