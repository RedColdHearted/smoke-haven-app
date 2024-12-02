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
from apps.invoices.services.statistic.functions import (
    get_years_list,
    get_invoice_stat_by_year,
    get_invoices_sum_by_year,
    get_suppliers_invoice_stat,
    get_suppliers_count,
)

class IndexView(LoginRequiredMixin, TemplateView):
    """Class-based view for index page."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        current_year = timezone.now().year
        selected_year = self.request.GET.get('year', current_year)

        context = super().get_context_data(**kwargs)
        context["selected_year"] = selected_year
        context["current_year"] = current_year
        context["years_list"] = get_years_list(current_year)
        context["total_invoices_sum"] = get_invoices_sum_by_year(selected_year)
        context["invoice_statistic"] = get_invoice_stat_by_year(selected_year)
        context["suppliers_statistic"] = get_suppliers_invoice_stat()
        context["suppliers_count"] = get_suppliers_count()
        return context


@login_required
def protected_serve(request, path):
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        raise Http404(_("File does not exist"))

    return serve(request, path, document_root=settings.MEDIA_ROOT)