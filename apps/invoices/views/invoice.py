from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import DetailView, DeleteView, UpdateView
from django.shortcuts import redirect
from ..forms import InvoiceForm, DocumentForm
from ..models import Document
from django.contrib.contenttypes.models import ContentType
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

from ..models import Invoice, InvoicePayment
from ..filters import InvoiceFilter


class DetailInvoiceView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = "invoices/detail_invoice.html"
    context_object_name = "invoice"
    queryset = Invoice.objects.with_total_paid_amount()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_percentage"] = int(
            (self.object.total_amount / self.object.amount_to_pay) * 100,
        ) if self.object.amount_to_pay > 0 else 0
        context["documents"] = Document.objects.filter(
            content_type=ContentType.objects.get_for_model(self.object),
            object_id=self.object.id,
        )
        context["invoice_payments"] = InvoicePayment.objects.filter(invoice=self.object)
        return context


class ListInvoiceView(LoginRequiredMixin, FilterView):
    model = Invoice
    template_name = "invoices/invoices.html"
    context_object_name = "invoices"
    filterset_class = InvoiceFilter
    paginate_by = 10
    queryset = Invoice.objects.with_total_paid_amount()


class CreateInvoiceView(LoginRequiredMixin, FormView):
    """Invoice create class-based view."""

    template_name = "invoices/create_invoice.html"
    form_class = InvoiceForm
    success_url = reverse_lazy("invoices:invoices")

    def get_context_data(self, **kwargs):
        """Return context data."""
        context = super().get_context_data(**kwargs)
        context["document_forms"] = [
            DocumentForm(prefix=str(i)) for i in range(3)
        ]
        return context

    def post(self, request, *args, **kwargs):
        """Perform logic of `post` method."""
        invoice_form = self.get_form()
        document_forms = [
            DocumentForm(
                request.POST,
                request.FILES,
                prefix=str(i),
            ) for i in range(3)
        ]

        if invoice_form.is_valid() and all(
            df.is_valid() for df in document_forms
        ):
            invoice = invoice_form.save()

            for document_form in document_forms:
                try:
                    file = document_form.cleaned_data.get("file")
                    if file:
                        Document.objects.create(
                            content_type=ContentType.objects.get_for_model(
                                invoice,
                            ),
                            object_id=invoice.id,
                            file=file,
                        )
                except MultiValueDictKeyError:
                    continue

            return redirect(self.success_url)
        return self.form_invalid(invoice_form)


class DeleteInvoiceView(LoginRequiredMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy("invoices:invoices")


class UpdateInvoiceView(LoginRequiredMixin, UpdateView):
    model = Invoice
    template_name = "invoices/update_invoice.html"
    context_object_name = "invoice"
    form_class = InvoiceForm

    def get_success_url(self):
        return reverse_lazy(
            "invoices:update_invoice",
            kwargs={
            "pk": self.object.pk,
            }
        )

