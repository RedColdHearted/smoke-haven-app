from django.urls import path

from .views import BackupCreateView

app_name = "backups"

urlpatterns = [
    path(
        "create",
        BackupCreateView.as_view(),
        name="create_backup",
    ),
]
