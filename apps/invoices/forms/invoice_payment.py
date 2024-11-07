from django import forms

from ..models import InvoicePayment


class InvoicePaymentCreateForm(forms.ModelForm):
    """Invoice payment create from."""

    paid_amount = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": "введите сумму оплаченную платежкой",
            }
        ),
        label="Сумма в рублях",
    )
    payment_type = forms.ChoiceField(
        choices=InvoicePayment.Payment.choices,
        label="Выберите тип оплаты",
        widget=forms.Select(
            attrs={
                "class": "select2 w-50 form-select",
            },
        ),
    )
    class Meta:
        model = InvoicePayment
        fields = ["paid_amount", "payment_type"]
