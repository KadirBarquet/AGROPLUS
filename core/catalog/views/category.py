from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.catalog.models import Category

# Vistas para Category
class CategoryListView(ListView):
    model = Category
    template_name = 'core/category/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'core/category/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('catalog:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'core/category/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('catalog:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'core/category/category_delete.html'
    success_url = reverse_lazy('catalog:category_list')