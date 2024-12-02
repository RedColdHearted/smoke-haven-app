import os

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils import timezone

from apps.invoices.models import Invoice
from apps.products.models import Supplier

class IndexView(LoginRequiredMixin, TemplateView):
    """Class-based view for index page."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Получаем текущий год или год из GET-параметра
        current_year = timezone.now().year
        year = self.request.GET.get('year', current_year)

        # Создаем список годов для выбора
        years = list(range(current_year, current_year - 5, -1))

        # invoices
        monthly_invoices = (
            Invoice.objects
            .filter(deadline__year=year)  # Фильтр по году
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

        total_invoices_sum = Invoice.objects.filter(deadline__year=year).aggregate(
            total=Sum("amount_to_pay"),
        )["total"] or 0
        print(total_invoices_sum)
        # suppliers
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
        total_suppliers = len(Supplier.objects.all())

        context = super().get_context_data(**kwargs)
        context["invoice_statistic"] = invoice_statistic
        context["suppliers_statistic"] = suppliers_statistic
        context["total_invoices_sum"] = total_invoices_sum
        context["total_suppliers"] = total_suppliers
        context["selected_year"] = year
        context["current_year"] = current_year
        context["years"] = years
        return context


@login_required
def protected_serve(request, path):
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        raise Http404(_("File does not exist"))

    return serve(request, path, document_root=settings.MEDIA_ROOT)