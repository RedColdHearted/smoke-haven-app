from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvoicesAppConfig(AppConfig):
    """Default configuration for Invoices app."""

    name = "apps.invoices"
    verbose_name = _("Invoices")