from http import HTTPStatus

from django.utils.translation import gettext_lazy as _
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Document, Invoice

REFER_HTTP_HEADER = "HTTP_REFERER"
CONTENT_DOWNLOAD_HEADER = "Content-Disposition"
ANY_FILE_TYPE_HEADER = "application/octet-stream"

class DownloadDocumentView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        try:
            document = Document.objects.get(pk=pk)
            response = HttpResponse(
                document.file,
                content_type=ANY_FILE_TYPE_HEADER,
            )
            response[CONTENT_DOWNLOAD_HEADER] = (
                f"inline; filename='{document.file.name}'"
            )
            return response
        except Document.DoesNotExist:
            raise Http404(_("Document not found"))


class DeleteDocumentView(LoginRequiredMixin, DeleteView):
    model = Document

    def get_success_url(self):
        return self.request.META.get(REFER_HTTP_HEADER, self.success_url)


class UploadDocumentByInvoiceView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ("file",)
    template_name = "invoices/document_upload_form.html"

    def form_valid(self, form):
        invoice_id = self.kwargs["invoice_id"]
        invoice = get_object_or_404(Invoice, id=invoice_id)

        document = form.save(commit=False)
        document.content_type = ContentType.objects.get_for_model(invoice)
        document.object_id = invoice.id
        document.save()

        return redirect("invoices:detail_invoice", pk=invoice.id)

    def form_invalid(self, form):
        return HttpResponse(
            _("File download error"),
            status=HTTPStatus.BAD_REQUEST,
        )

