from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Dish
from .forms import IngredientForm
# Create your views here.

class CatalogView(ListView):
    model = Dish

class CatalogDetailView(DetailView):
    model = Dish

class IngredientCreateView(CreateView):
    template_name = "ingredient_create.html"
    form_class = IngredientForm
    success_url = "/"



