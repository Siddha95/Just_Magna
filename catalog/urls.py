from django.urls import path, include

from .views import *
from catalog import views

urlpatterns = [
    # Catalog app
    path("", CatalogView.as_view(), name='home'),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/delete/<str:pk>", DeleteDishView.as_view(), name="dish-delete"),
    path("dish/update/<str:pk>", UpdateDishView.as_view(), name="dish-update"),
    path("dish/", DishAdminView.as_view(), name="dish-list"),
    # path("dish/search", DishSearchView.as_view(), name='dish-search'),

    path("ingredient/delete/<str:pk>", DeleteIngredientView.as_view(), name="ingredient-delete"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/update/<str:pk>", UpdateIngredientView.as_view(), name="ingredient-update"),
    path("ingredient/", IngredientAdminView.as_view(), name="ingredient-list"),

    
]
