from .paths import BASE_DIR

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [BASE_DIR / "ui"]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

GOOGLE_CREDENTIALS_PATH = "client_secrets.json"

