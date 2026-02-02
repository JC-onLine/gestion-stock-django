# from django.shortcuts import render
from .models import Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# from django.urls import path, include
# from django.contrib.auth.mixins import LoginRequiredMixin


# ==== Category CreateView ====
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'open_stock/category/category_create.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.name = form.cleaned_data['name']
        slug = f"{form.cleaned_data['name']}"
        form.instance.slug = slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('open_stock:category_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des categories'
        context['subtitle'] = "Ajouter une nouvelle catégorie"
        return context


# ==== Category ListView ====
class CategoryListView(ListView):
    model = Category
    template_name = 'open_stock/category/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Liste des categories'
        return context


# ==== Category DetailView ====
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'open_stock/category/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Détails produit sélectionné'
        return context


# ==== Category UpdateView ====
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'open_stock/category/category_update.html'
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('open_stock:category_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des catégory de produit'
        context['subtitle'] = "Création d'une nouvelle catégorie"
        return context


# ==== Category DeleteView ====
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'open_stock/category/category_delete.html'
    success_url = reverse_lazy('open_stock:category_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des categories'
        context['subtitle'] = "Confirmer la suppression de la catégorie :"
        return context
