from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish, Ingredient
from .forms import IngredientForm
from django.http import Http404
from django.urls import reverse_lazy
# Create your views here.

class CatalogView(ListView):
    model = Dish

class CatalogDetailView(DetailView):
    model = Dish

class IngredientCreateView(CreateView):
    template_name = "catalog/ingredient_form.html"
    form_class = IngredientForm
    success_url = "/ingredient/list"

# view per amministrazione
class AmministrazioneView(ListView):
    model = Ingredient

# view per eliminare ingrediente
class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("ingredient-list")

# view per fare l'upgrade di un ingrediente

class UpdateIngredientView(UpdateView):
    pass 



