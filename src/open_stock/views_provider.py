# from django.shortcuts import render
from .models import Provider
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# from django.urls import path, include
# from django.contrib.auth.mixins import LoginRequiredMixin


# ==== Provider CreateView ====
class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'open_stock/provider/provider_create.html'
    fields = ['name', 'description', 'favorite']

    def form_valid(self, form):
        form.instance.name = form.cleaned_data['name']
        form.instance.category = form.cleaned_data['description']
        form.instance.location = form.cleaned_data['favorite']
        slug = f"_{form.cleaned_data['name']}"
        form.instance.slug = slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('open_stock:provider_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Ajouter un nouveau magasin"
        return context


# ==== Provider ListView ====
class ProviderListView(ListView):
    model = Provider
    template_name = 'open_stock/provider/provider_list.html'
    context_object_name = 'providers'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Liste des magasins'
        return context


# ==== Provider DetailView ====
class ProviderDetailView(DetailView):
    model = Provider
    template_name = 'open_stock/provider/provider_detail.html'
    context_object_name = 'provider'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = 'Détails du magasin sélectionné'
        return context


# ==== Provider UpdateView ====
class ProviderUpdateView(UpdateView):
    model = Provider
    template_name = 'open_stock/provider/provider_update.html'
    fields = ['name', 'description', 'favorite']

    def get_success_url(self):
        return reverse('open_stock:provider_detail', args=[self.object.pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Création d'un nouveau magasin"
        return context


# ==== Provider DeleteView ====
class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'open_stock/provider/provider_delete.html'
    success_url = reverse_lazy('open_stock:provider_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestion des stocks'
        context['subtitle'] = "Confirmer la suppression du magasin :"
        return context
