from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Supplier


class SupplierForm(forms.ModelForm):
    """Supplier create from."""

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Input supplier's name"),
            }
        ),
        label=_("supplier's name"),
    )
    inn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Input supplier's inn"),
            }
        ),
        label=_("supplier's inn"),
        required=False,
    )
    bik = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Input supplier's bik"),
            }
        ),
        label=_("supplier's bik"),
        required=False,
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Input supplier's phone number"),
            }
        ),
        label=_("supplier's phone number"),
        required=False,
    )
    class Meta:
        model = Supplier
        fields = (
            "name",
            "inn",
            "bik",
            "phone_number",
        )
