from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .utils import generate_two_week_pass_date
from ..querysets import InvoiceQueryset


class Invoice(BaseModel):
    """Represent invoice in db."""

    amount_to_pay = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        verbose_name=_("Amount"),
        validators=[
            MinValueValidator(5000),
            MaxValueValidator(10000000),
        ],
        blank=False,
    )
    supplier = models.ForeignKey(
        to="products.Supplier",
        verbose_name=_("Supplier id"),
        on_delete=models.SET_NULL,
        related_name="invoices",
        null=True,
    )
    deadline = models.DateField(
        default=generate_two_week_pass_date,
        verbose_name=_("Deadline"),
    )
    is_expired = models.BooleanField(
        choices=(
            (True, _("Yes"),),
            (False, _("No"),),
        ),
        verbose_name=_("Is expired"),
        default=False,
    )

    objects = InvoiceQueryset.as_manager()

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self) -> str:
        return f"{self.id}"