from django.contrib.auth.views import (
    LoginView,
)

from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    """Custom login class-based view with custom login form."""

    form_class = CustomLoginForm