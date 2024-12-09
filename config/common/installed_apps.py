# Application definition
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

THIRD_PARTY = (
    "imagekit",
    "django_filters",
    "django_extensions",
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    "two_factor",
    "django_otp",
    'django_otp.plugins.otp_static',
    "django_otp.plugins.otp_totp",
)

LOCAL_APPS = (
    "apps.core",
    "apps.users",
    "apps.products",
    "apps.invoices",
    "apps.backups",
)

INSTALLED_APPS += THIRD_PARTY + LOCAL_APPS