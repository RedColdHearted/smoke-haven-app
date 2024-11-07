from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class InvoicePayment(BaseModel):
    """Represent invoice payment in db."""

    invoice = models.ForeignKey(
        to="invoices.Invoice",
        verbose_name=_("Invoice id"),
        on_delete=models.CASCADE,
        related_name="invoice_payments",
    )
    paid_amount = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        verbose_name=_("Paid amount"),
        validators=[
            MinValueValidator(5000),
            MaxValueValidator(10000000),
        ],
        blank=False,
    )
    class Payment(models.TextChoices):
        """String based enum for payment type choice."""

        CASH = "Cash", _("Cash")
        NON_CACHE = "Non cash", _("Non cash")

    payment_type = models.CharField(
        choices=Payment.choices,
        verbose_name=_("Payment type"),
        max_length=10,
    )

    class Meta:
        verbose_name = _("Invoice payment")
        verbose_name_plural = _("Invoice payments")

    def __str__(self) -> str:
        return f"{self.id}"