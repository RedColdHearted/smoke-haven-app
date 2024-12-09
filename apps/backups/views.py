from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Backup
from apps.backups.services.google_backup.functions import backup

class BackupListView(LoginRequiredMixin, ListView):
    model = Backup
    paginate_by = 10
    template_name = "backups/backup_list.html"
    context_object_name = "backups"


class BackupCreateView(LoginRequiredMixin, CreateView):
    model = Backup

    def get_success_url(self):
        return reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        backup_folder = backup()
        instance = Backup(
            creating_type=Backup.CreationType.MANUAL.value,
            drive_url=backup_folder["embedLink"],
            folder_id=backup_folder["id"],
            status=Backup.BackupStatus.DONE.value,
        )
        instance.save()
        return HttpResponseRedirect(self.get_success_url())