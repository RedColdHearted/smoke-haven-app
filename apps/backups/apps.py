from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BackupsAppConfig(AppConfig):
    """Default configuration for Backups app."""

    name = "apps.backups"
    verbose_name = _("Backups")