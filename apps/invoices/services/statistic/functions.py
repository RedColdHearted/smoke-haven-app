from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils.translation import gettext_lazy as _

from ...models import Invoice
from apps.products.models import Supplier

def get_years_list(current_year: int)-> list[int]:
   return list(range(current_year, current_year - 5, -1))


def get_invoice_stat_by_year(year) -> dict[str, str | float | int]:
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


def get_invoices_sum_by_year(year: int) -> int:
    return Invoice.objects.filter(deadline__year=year).aggregate(
            total=Sum("amount_to_pay"),
        )["total"] or 0


def get_suppliers_invoice_stat() -> dict[str, str | int]:
    supplier_invoices_count = (
            Supplier.objects
            .annotate(invoice_count=Count("invoices"))
            .values("id", "name", "invoice_count")
        )

    suppliers_statistic = []
    for entry in supplier_invoices_count:
        suppliers_statistic.append({
            "name": entry["name"],
            "invoice_count": entry["invoice_count"] or 0
        })
    return suppliers_statistic


def get_suppliers_count() -> int:
    return len(Supplier.objects.all())
