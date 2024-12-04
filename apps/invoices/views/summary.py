
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.invoices.services.summary.functions import (
    years_list,
    monthly_stat,
    vital_stat,
    total_sum,
)

class SummaryView(LoginRequiredMixin, TemplateView):
    """Class-based view for index page."""

    template_name = "invoices/summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = timezone.now().year
        selected_year = self.request.GET.get('year', current_year)
        v_stat = vital_stat(selected_year)

        context["selected_year"] = selected_year
        context["current_year"] = current_year
        context["years_list"] = years_list(current_year)
        context["total_sum"] = total_sum(selected_year)
        context["monthly_stat"] = monthly_stat(selected_year)
        context["total_count"] = v_stat.count
        context["average_amount"] = v_stat.avg
        context["max_amount"] = v_stat.maximum
        context["min_amount"] = v_stat.minimum
        return context