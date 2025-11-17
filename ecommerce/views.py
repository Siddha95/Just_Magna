from .forms import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Cart, Cart_dish
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import permissions, viewsets, status
from .serializers import CartSerializer, CartDishSerializer, VoucherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication





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
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try: 
            cart = Cart.objects.get(user=self.request.user)
            cart_items = Cart_dish.objects.filter(cart=cart)
        
            context["cart_items"] = cart_items
            context["cart"] = cart
        

        except Cart.DoesNotExist:
            pass
    
        return context
    


class QuantityEditView(SuccessMessageMixin, UpdateView):
    model = Cart_dish
    form_class = UpdateQuantityForm
    template_name = 'ecommerce/cart_list.html'
    success_url = reverse_lazy('cart_list')
    success_message = "La quantità è stata aggiornata correttamente!"
    

    def form_valid(self, form):
        
        cart_item = form.save(commit=False)
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
        return super().form_valid(form)
    





class VoucherListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 

    def get(self, request, format=None):
        voucher = Voucher.objects.all()
        serializer = VoucherSerializer(voucher, many=True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer = VoucherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CartDishAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        cart_dish = Cart_dish.objects.all()
        serializer = CartDishSerializer(cart_dish, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CartDishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        