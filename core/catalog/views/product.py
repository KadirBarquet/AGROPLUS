from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core.catalog.models import Product

# Vistas para Product
class ProductListView(ListView):
    model = Product
    template_name = 'core/product/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.all().order_by('name')
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'core/product/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'core/product/product_form.html'
    fields = ['name', 'category', 'supplier', 'description', 'price', 'stock_quantity', 'image']
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'core/product/product_form.html'
    fields = ['name', 'category', 'supplier', 'description', 'price', 'stock_quantity', 'image']
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'core/product/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')