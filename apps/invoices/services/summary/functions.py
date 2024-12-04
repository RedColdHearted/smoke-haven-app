from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils.translation import gettext_lazy as _

from ...models import Invoice
from .dataclasses import NumericStat

def years_list(current_year: int)-> list[int]:
   return list(range(current_year, current_year - 5, -1))


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
    return NumericStat(
        count=length,
        avg=sum(item.amount_to_pay for item in query) / length,
        maximum=max(item.amount_to_pay for item in query),
        minimum=min(item.amount_to_pay for item in query),
    )


def total_sum(year: int) -> int:
    return Invoice.objects.filter(deadline__year=year).aggregate(
            total=Sum("amount_to_pay"),
        )["total"] or 0
