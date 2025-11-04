from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Cart_dish
from django.shortcuts import get_object_or_404, redirect, render




class CartAddFormView(LoginRequiredMixin, FormView):
    form_class = CartForm
    

    def form_valid(self, form):
        dish_id = self.kwargs.get('dish_id')
        dish = get_object_or_404(Dish, id=dish_id)
        quantity = form.cleaned_data.get('quantity', 1)
        user = self.request.user
        cart, created= Cart.objects.get_or_create(user=user)
        cart_dish, dish_created = Cart_dish.objects.get_or_create(
            cart = cart,
            dish = dish,
            defaults={'quantity':quantity}
            )
        
        if not dish_created:
            cart_dish.quantity += quantity
            cart_dish.save()
         
    
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
    

class CartTemplateView(LoginRequiredMixin, TemplateView):
    pass