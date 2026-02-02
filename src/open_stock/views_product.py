# from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# from django.urls import path, include
# from django.contrib.auth.mixins import LoginRequiredMixin


# ==== Product CreateView ====
class ProductCreateView(CreateView):
    model = Product
    template_name = 'open_stock/product/product_create.html'
    fields = ['name', 'category', 'location',
              'price', 'count_mini_alarm', 'description', 'sku']

    def form_valid(self, form):
        form.instance.name = form.cleaned_data['name']
        form.instance.category = form.cleaned_data['category']
        form.instance.location = form.cleaned_data['location']
        form.instance.count_mini_alarm = form.cleaned_data['count_mini_alarm']
        form.instance.sku = form.cleaned_data['sku']
        slug = f"{form.cleaned_data['category']}-{form.cleaned_data['name']}"
        form.instance.slug = slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('open_stock:product_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Ajouter un nouveau produit"
        return context


# ==== Product ListView ====
class ProductListView(ListView):
    model = Product
    template_name = 'open_stock/product/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Liste des produits'
        return context


# ==== Product DetailView ====
class ProductDetailView(DetailView):
    model = Product
    template_name = 'open_stock/product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Détails produit sélectionné'
        return context


# ==== Product UpdateView ====
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'open_stock/product/product_update.html'
    fields = ['name', 'category', 'location',
              'price', 'count_mini_alarm', 'description', 'sku']

    def get_success_url(self):
        return reverse('open_stock:product_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Création d'un nouveau produit"
        return context


# ==== Product DeleteView ====
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'open_stock/product/product_delete.html'
    success_url = reverse_lazy('open_stock:product_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Confirmer la suppression du produit :"
        return context
