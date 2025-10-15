from django.shortcuts import render
from django.views.generic import ListView
from .models import Dish
# Create your views here.

class CatalogView(ListView):
    model = Dish
    
    # template_name = "dish_list.html"
    # context_object_name = 'dishes'  # opzionale, nome nel template




    # def get_context_data(self, **kwargs):
    #     context = super(HomePage, self).get_context_data(**kwargs)
    #     context['categories'] = Category.objects.filter(active=True)
    #     context['products'] = Product.objects.filter(active=True).order_by('-created')
    #     context['featured_products'] = Product.objects.filter(featured=True)
    #     return context