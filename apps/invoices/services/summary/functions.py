from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils.translation import gettext_lazy as _

from ...models import Invoice, InvoicePayment
from .dataclasses import NumericStat

def years_list(current_year: int)-> list[int]:
   return list(range(current_year, current_year - 2, -1))


def monthly_stat(year: int) -> dict[str, str | float | int]:
    monthly_invoices = (
        Invoice.objects
        .filter(deadline__year=year)
        .annotate(month=TruncMonth("deadline"))
        .values("month")
        .annotate(total_amount=Sum("amount_to_pay"))
        .order_by("month")
    )
    invoice_statistic = []
    for entry in monthly_invoices:
        invoice_statistic.append({
            "month": _(entry["month"].strftime("%B")),
            "total_amount": float(entry["total_amount"]) or 0
        })
    return invoice_statistic


def vital_stat(year: int) -> NumericStat:
    query = Invoice.objects.filter(deadline__year=year)
    length = len(query)
    if length:
        return NumericStat(
            count=length,
            avg=sum(item.amount_to_pay for item in query) / length,
            maximum=max(item.amount_to_pay for item in query),
            minimum=min(item.amount_to_pay for item in query),
        )
    return NumericStat(
        count=0,
        avg=0.00,
        maximum=0.00,
        minimum=0.00,
    )

def most_frequent_payment_type(year: int):
    return _(
        InvoicePayment.objects.filter(
                invoice__deadline__year=year
            ).values(
                "payment_type",
            ).annotate(
                count=Count("payment_type"),
            ).order_by(
                "-count",
            ).first()["payment_type"]
        )


def total_sum(year: int) -> int:
    return Invoice.objects.filter(deadline__year=year).aggregate(
            total=Sum("amount_to_pay"),
        )["total"] or 0


