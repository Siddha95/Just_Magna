from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Dish, Ingredient
from .forms import IngredientForm
from django.http import Http404
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
    def get_object(self, queryset = None):
        return super().get_object(queryset)

# view per fare l'upgrade di un ingrediente

class UpdateIngredientView(UpdateView):
    pass 



