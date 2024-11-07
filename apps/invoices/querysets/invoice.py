from typing import Self
from django.db.models import (
    QuerySet,
    Case,
    When,
    BooleanField,
    DecimalField,
    OuterRef,
    Subquery,
    Sum,
    F,
)
from django.db.models.functions import Coalesce

from .. import models

class InvoiceQueryset(QuerySet):
    """Queryset class for `Invoice` model."""

    def with_total_paid_amount(self) -> Self:
        """Annotate `InvoiceQueryset` with total amount of related payments."""

        total_amount_subquery = models.InvoicePayment.objects.filter(
            invoice=OuterRef("pk"),
        ).values("invoice").annotate(
            total=Sum("paid_amount")
        ).values("total")[:1]

        return self.annotate(
            total_amount=Coalesce(
                Subquery(total_amount_subquery),
                0.00,
                output_field=DecimalField(decimal_places=2, max_digits=8),
            ),
            is_fully_paid=Case(
                When(total_amount__gte=F("amount_to_pay"), then=True),
                default=False,
                output_field=BooleanField(),
            )
        ).select_related("supplier")