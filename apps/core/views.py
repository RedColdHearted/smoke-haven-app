from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    """Class-based view for index page."""

    template_name = "index.html"
