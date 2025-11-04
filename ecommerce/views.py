from .forms import *
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Cart, Cart_dish
from django.shortcuts import get_object_or_404, redirect, render




class CartAddView(LoginRequiredMixin, View):
    

    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        quantity = int(request.POST.get('quantity', 1))
        #created diventa vera se viene creato il cart
        cart= Cart.objects.get_or_create(user=request.user)
        cart_dish, dish_created = Cart_dish.objects.get_or_create(
            cart = cart,
            dish = dish,
            defaults={'quantity':quantity}
            )
        #devo inserire nel template un modo per gestire i messaggi
        
        if not dish_created:
            cart_dish.quantity += 1
            cart_dish.save()
            messages.success(
                request,
                f'Quantità di "{dish.name}" aggiornata a {cart_dish.quantity}'
            )
        else:
            messages.success(
                request,
                f'"{dish.name}" aggiunto al carrello!'
            )
        return redirect(request.META.get('HTTP_REFERER', '/'))

        

class CartTemplateView(LoginRequiredMixin, TemplateView):
    pass
