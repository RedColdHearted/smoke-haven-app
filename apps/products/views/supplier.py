from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import Supplier
from ..forms import SupplierForm


class CreateSupplierView(LoginRequiredMixin, CreateView):
    """Supplier create class-based view."""

    model = Supplier
    template_name = "products/create_supplier.html"
    form_class = SupplierForm
    success_url = reverse_lazy("products:suppliers")


class UpdateSupplierView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = "products/update_supplier.html"
    form_class = SupplierForm
    success_url = reverse_lazy("products:suppliers")



class ListSupplierView(LoginRequiredMixin, ListView):
    """Suppliers list class-based view."""

    model = Supplier
    template_name = "products/suppliers.html"
    context_object_name = "suppliers"
