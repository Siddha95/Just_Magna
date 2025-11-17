from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish, Ingredient, Course
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ecommerce.forms import AddToCartForm

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import CourseSerializer, DishSerializer, IngredientSerializer
from rest_framework import status
# Create your views here.

class CatalogView(ListView):
    paginate_by = 4
    model = Dish
    context_object_name = "dishes"
    template_name = "catalog/catalog_list.html"


# se il template ha lo stesso nome del model non serve specificarlo con tempalte name
# dettagli piatto
class DishDetailView(LoginRequiredMixin, DetailView):
    
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


#VIEWSETS

class CourseListAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class DishListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    
    def get(self, request, format=None):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):

        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class DishDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 

       # Retrieve, update or delete a dish instance.
    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        dish = self.get_object(pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        dish = self.get_object(pk)
        serializer = DishSerializer(dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        dish = self.get_object(pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class IngredientListAPIView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredient, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


