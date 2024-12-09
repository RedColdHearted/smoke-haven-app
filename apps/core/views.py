import os

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from apps.backups.models import Backup

class IndexView(LoginRequiredMixin, TemplateView):
    """Class-based view for index page."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_backup_date"] = Backup.objects.all().order_by(
            "-created",
        ).first().created.date
        return context


@login_required
def protected_serve(request, path):
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        raise Http404(_("File does not exist"))

    return serve(request, path, document_root=settings.MEDIA_ROOT)