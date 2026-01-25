from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'open_stock/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Liste des produits'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'open_stock/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Détails produit sélectionné'
        return context


class ProductCreateView(CreateView):
    pass


class ProductUpdateView(UpdateView):
    pass


class ProductDeleteView(DeleteView):
    pass

# <a href="{% url 'open_stock:product_detail' product.pk %}">{{ product.name }}</a>

