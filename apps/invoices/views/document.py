from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Document, Invoice


class DownloadDocumentView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        try:
            document = Document.objects.get(pk=pk)
            response = HttpResponse(document.file, content_type='application/octet-stream')
            response['Content-Disposition'] = f'inline; filename="{document.file.name}"'
            return response
        except Document.DoesNotExist:
            raise Http404("Document not found")


class DeleteDocumentView(LoginRequiredMixin, DeleteView):
    model = Document

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", self.success_url)


class UploadDocumentByInvoiceView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['file']  # Specify the fields to be used in the form
    template_name = 'invoices/document_upload_form.html'  # Optional: create a separate template if needed

    def form_valid(self, form):
        # Get the invoice ID from the URL
        invoice_id = self.kwargs['invoice_id']
        invoice = get_object_or_404(Invoice, id=invoice_id)

        # Create the Document instance
        document = form.save(commit=False)
        document.content_type = ContentType.objects.get_for_model(invoice)
        document.object_id = invoice.id
        document.save()

        # Redirect to the invoice detail page
        return redirect('invoices:detail_invoice', pk=invoice.id)

    def form_invalid(self, form):
        return HttpResponse("Ошибка загрузки файла", status=400)

