from django import forms

from ..models import Invoice
from apps.products.models import Supplier
from ..models.utils import generate_two_week_pass_date


class InvoiceForm(forms.ModelForm):
    """Invoice create from."""

    amount_to_pay = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": "введите сумму к оплате накладной",
            }
        ),
        label="Сумма к оплате в рублях",
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        label="Выберите поставщика продукции",
        widget=forms.Select(
            attrs={
                "class": "select2 w-50 form-select",
            },
        ),
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control w-25",
            },
        ),
        label="Введите срок оплаты накладной (2 недели по умолчанию)",
        initial=generate_two_week_pass_date,
    )
    class Meta:
        model = Invoice
        fields = ["amount_to_pay", "supplier", "deadline"]
