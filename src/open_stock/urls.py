from django.urls import path
from .views_product import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views_category import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from .views_provider import ProviderListView, ProviderDetailView, ProviderCreateView, ProviderUpdateView, ProviderDeleteView


app_name = 'open_stock'
urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('provider/create/', ProviderCreateView.as_view(), name='provider_create'),
    path('provider/list/', ProviderListView.as_view(), name='provider_list'),
    path('provider/detail/<int:pk>/', ProviderDetailView.as_view(), name='provider_detail'),
    path('provider/update/<int:pk>/', ProviderUpdateView.as_view(), name='provider_update'),
    path('provider/delete/<int:pk>/', ProviderDeleteView.as_view(), name='provider_delete'),
]
