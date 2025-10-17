from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Dish
from .forms import IngredientForm
# Create your views here.

class CatalogView(ListView):
    model = Dish

class CatalogDetailView(DetailView):
    model = Dish

class IngredientCreateView(CreateView):
    template_name = "catalog/ingredient_form.html"
    form_class = IngredientForm
    success_url = "/"

# view per amministrazione
class AmministrazioneView(ListView):
    pass 

# view per eliminare ingrediente
class DeleteIngredientView(DeleteView):
    pass

# view per fare l'upgrade di un ingrediente

class UpdateIngredientView(UpdateView):
    pass 



