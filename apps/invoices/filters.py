from django import forms

from django_filters import filterset, widgets

from .models import Invoice
from apps.products.models import Supplier

class InvoiceFilter(filterset.FilterSet):
    """Represent filter of issues list."""

    id = filterset.NumberFilter(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "введите её номер",
            }
        ),
        lookup_expr="iexact",
        label="Поиск по номеру накладной"
    )

    def filter_similar_amount(queryset, name, value):
        """Filter and queryset with similar amount."""
        value = float(value)
        threshold = value * 0.15
        return queryset.filter(
            **{
                f"{name}__range": (
                    value - threshold,
                    value + threshold,
                ),
            }
        )

    amount_to_pay = filterset.NumberFilter(
        label="Поиск по сумме накладной",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите сумму накладной",
            },
        ),
        required=False,
        method=filter_similar_amount,
    )
    supplier = filterset.ModelChoiceFilter(
        queryset=Supplier.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "select2 form-select",
                "data-placeholder": "Выберете поставщика",
            },
        ),
        label="Поиск по постовщику",
        required=False,
    )
    deadline_after = filterset.DateFilter(
        field_name="deadline",
        lookup_expr="gte",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "From"
            },
       ),
        label="Дата от",
    )
    deadline_before = filterset.DateFilter(
        field_name="deadline",
        lookup_expr="lte",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "To"
            },
        ),
        label="Дата до",
    )
    is_fully_paid = filterset.BooleanFilter(
        widget=widgets.BooleanWidget(
            attrs={
                "class": "form-control",
                "data-placeholder": "выберете статус",
            },
        ),
        label="поиск по статусу оплаты",
    )

    class Meta:
        model = Invoice
        fields = (
            "id",
            "amount_to_pay",
            "supplier",
            "deadline",
            "is_fully_paid",
        )
