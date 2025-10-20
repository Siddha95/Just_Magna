from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish, Ingredient
from .forms import IngredientForm 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CatalogView(ListView):
    model = Dish

class CatalogDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = Dish

class IngredientCreateView(CreateView):
    template_name = "catalog/ingredient_form.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingredient-list")

# view per amministrazione
class AmministrazioneView(ListView):
    model = Ingredient


# view per eliminare ingrediente
class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "catalog/confirm_delete.html"
    # Dentro funzioni o metodi di view - reverse()
    # Dentro attributi di classi,forms, mixins - reverse_lazy()
    success_url = reverse_lazy("ingredient-list")


# view per fare l'upgrade di un ingrediente
class UpdateIngredientView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    # template_name = "catalog/ingredient_update_form.html"
    success_url = reverse_lazy("ingredient-list")


