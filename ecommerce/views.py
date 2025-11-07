from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Cart_dish
from django.shortcuts import get_object_or_404, redirect, render




class CartAddFormView(LoginRequiredMixin, FormView):
    form_class = AddToCartForm
    http_method_names = ['post']
    template_name = 'catalog/catalog_list.html'

    def form_invalid(self, form):
        print("form_invalid:", form.errors)
    
        return redirect('/')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        dish_id = form.cleaned_data['dish_id']
        
        quantity = form.cleaned_data['quantity']
        user = self.request.user
        dish = get_object_or_404(Dish, id=dish_id)
        cart, _ = Cart.objects.get_or_create(user=user)

        cart_dish, created = Cart_dish.objects.get_or_create(
            cart = cart,
            dish = dish,
            defaults={'quantity':quantity}
            )
        
        if not created:
            cart_dish.quantity += quantity
            cart_dish.save()
         
    
        return redirect(self.request.META.get('HTTP_REFERER', '/'))


class CartTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "ecommerce/cart_list.html"	
    model = Cart_dish



    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        # cart è elementi di cart dove user è uguale all'user che ha fatto la richiesta
        try: 
            cart = Cart.objects.get(user=self.request.user)
        #cart_items sono gli oggetti di cart dish dove ii cart sono uguali a user id 
            cart_items = Cart_dish.objects.filter(cart=cart).select_related("dish")
            context["cart_items"] = cart_items
        except Cart.DoesNotExist:
            pass
    
        return context
    


