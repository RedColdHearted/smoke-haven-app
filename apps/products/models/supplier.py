from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .validators import (
    validate_inn,
    validate_bik,
    validate_russian_phone_number,
)

class Supplier(BaseModel):
    """Represent supplier in db."""

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120,
    )
    inn = models.CharField(
        validators=[validate_inn],
        verbose_name=_("INN"),
        max_length=12,
    )
    bik = models.CharField(
        validators=[validate_bik],
        verbose_name=(_("BIK")),
        max_length=9,
    )
    phone_number = models.CharField(
        validators=[validate_russian_phone_number],
        verbose_name=_("Phone number"),
        max_length=20,
    )

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self) -> str:
        return self.name