from django.urls import path

from .views import BackupCreateView, BackupListView

app_name = "backups"

urlpatterns = [
    path(
        "",
        BackupListView.as_view(),
        name="list_backups",
    ),
    path(
        "create/",
        BackupCreateView.as_view(),
        name="create_backup",
    ),
]
