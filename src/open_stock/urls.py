from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


app_name = 'open_stock'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    # path('delete/<int:pk>/', ProductDeleteView, name='product_delete'),
]
