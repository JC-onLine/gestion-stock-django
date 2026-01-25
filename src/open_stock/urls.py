from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


app_name = 'open_stock'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # path('<int:pk>/update/', ProductUpdateView, name='product_update'),
    # path('<int:pk>/delete/', ProductDeleteView, name='product_delete'),
    # path('detail/', ProductDetailView.as_view(), name='product_detail'),
]
