from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import DetailView, DeleteView
from django.shortcuts import redirect
from ..forms import InvoiceCreateForm, DocumentForm
from ..models import Document
from django.contrib.contenttypes.models import ContentType
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import InvoicePayment


from django.urls import reverse_lazy
from ..forms import InvoicePaymentCreateForm, DocumentForm


class InvoicePaymentCreateView(LoginRequiredMixin, CreateView):
    model = InvoicePayment
    form_class = InvoicePaymentCreateForm
    template_name = 'invoices/create_invoice_payment.html'  # Шаблон для формы

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["document_form"] = DocumentForm()
        return context
    
    def get_success_url(self):
        return reverse_lazy('invoices:detail_invoice', args=(
                self.kwargs['invoice_id'],
            ),
        )
    
    def post(self, request, *args, **kwargs):
        """Perform logic of `post` method."""
        invoice_payment_form = self.get_form()
        document_form = DocumentForm(
                request.POST,
                request.FILES,
            )

        if invoice_payment_form.is_valid() and document_form.is_valid():
            invoice_payment_form.instance.invoice_id = self.kwargs["invoice_id"]
            invoice_payment = invoice_payment_form.save()

            file = document_form.cleaned_data.get("file")
            if file:
                Document.objects.create(
                    content_type=ContentType.objects.get_for_model(
                        invoice_payment,
                    ),
                    object_id=invoice_payment.id,
                    file=file,
                )

            return redirect(self.get_success_url())
        return self.form_invalid(invoice_payment_form)



class DeleteInvoicePaymentView(LoginRequiredMixin, DeleteView):
    model = InvoicePayment

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", self.success_url)
