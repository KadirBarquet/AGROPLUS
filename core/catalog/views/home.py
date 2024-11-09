from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from core.catalog.models import Product, Category
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'components/home.html'
    #login_url = '/security/auth/login'

class MenuView(LoginRequiredMixin, TemplateView):
    template_name = 'components/menu.html'
    login_url = '/security/auth/login'

class ProductListView(ListView):
    model = Product
    template_name = 'core/catalog/catalogo.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        search_query = self.request.GET.get('search')

        if category_id:
            queryset = queryset.filter(category__id=category_id)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        context['search_query'] = self.request.GET.get('search', '')
        return context

class AboutView(TemplateView):
    template_name = 'components/about.html'

class ContactView(TemplateView):
    template_name = 'components/contact.html'