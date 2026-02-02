from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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
    model = Product
    template_name = 'open_stock/product_create.html'
    fields = ['name', 'category', 'location', 'description', 'price']

    def form_valid(self, form):
        # name = form.cleaned_data['name']
        # category = form.cleaned_data['category']
        form.instance.name = form.cleaned_data['name']
        form.instance.category = form.cleaned_data['category']
        form.instance.location = form.cleaned_data['location']
        # form.instance.name = title
        # form.instance.name = title
        # form.instance.name = title
        slug = f"{form.cleaned_data['category']}-{form.cleaned_data['name']}"
        form.instance.slug = slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('open_stock:product_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Création d'un nouveau produit"
        return context


class ProductUpdateView(UpdateView):
    pass


class ProductDeleteView(DeleteView):
    pass



