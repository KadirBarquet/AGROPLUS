from django.urls import path
from core.catalog.views import home, category, product, supplier

app_name = "catalog"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('menu/', home.MenuView.as_view(), name='menu'),
    path('catalogo/', home.ProductListView.as_view(), name='catalogo'),
    path('about/', home.AboutView.as_view(), name='about'),
    path('contact/', home.ContactView.as_view(), name='contact'),

    #CATEGORIA
    path('categories/', category.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', category.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', category.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', category.CategoryDeleteView.as_view(), name='category_delete'),

    #PROVEEDORES 
    path('suppliers/', supplier.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', supplier.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', supplier.SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', supplier.SupplierDeleteView.as_view(), name='supplier_delete'),

    #PRODUCTOS
    path('products/', product.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', product.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', product.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', product.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', product.ProductDeleteView.as_view(), name='product_delete'),
]