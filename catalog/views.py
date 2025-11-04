from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish, Ingredient
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CatalogView(ListView):
    paginate_by = 4
    model = Dish
    context_object_name = "dishes"
    template_name = "catalog/catalog_list.html"

    

# se il template ha lo stesso nome del model non serve specificarlo con tempalte name


# dettagli piatto
class CatalogDetailView(LoginRequiredMixin, DetailView):
    
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.course:
            context['related_dishes'] = Dish.objects.filter(course=self.object.course).exclude(id=self.object.id)
       
        return context

# crea da admin views
class IngredientCreateView(CreateView):
    template_name = "catalog/ingredient_form.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingredient-list")

class DishCreateView(CreateView):
    template_name = "catalog/dish_form.html"
    form_class = DishForm
    success_url = reverse_lazy("dish-list")

# view per amministrazione 
class IngredientAdminView(LoginRequiredMixin, ListView):
    model = Ingredient

class DishAdminView(LoginRequiredMixin, ListView):
    model = Dish

# view per eliminare ingrediente
class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "catalog/confirm_delete.html"
    # Dentro funzioni o metodi di view - reverse()
    # Dentro attributi di classi,forms, mixins - reverse_lazy()
    success_url = reverse_lazy("ingredient-list")

class DeleteDishView(DeleteView):
    model = Dish 
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("dish-list")


# view per fare l'upgrade di un ingrediente
class UpdateIngredientView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    # template_name = "catalog/ingredient_update_form.html"
    success_url = reverse_lazy("ingredient-list")

class UpdateDishView(UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dish-list")


