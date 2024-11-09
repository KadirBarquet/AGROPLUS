from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.catalog.models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'core/supplier/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'core/supplier/supplier_form.html'
    fields = ['name', 'contact_email', 'contact_phone']
    success_url = reverse_lazy('catalog:supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'core/supplier/supplier_form.html'
    fields = ['name', 'contact_email', 'contact_phone']
    success_url = reverse_lazy('catalog:supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'core/supplier/supplier_delete.html'
    success_url = reverse_lazy('catalog:supplier_list')
