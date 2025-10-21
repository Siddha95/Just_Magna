from django.urls import path
from .views import *


urlpatterns = [
    # Catalog app
    path("", CatalogView.as_view(), name='home'),
    path("details/<int:pk>/", CatalogDetailView.as_view(), name="catalog-detail"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("ingredient/del/<str:pk>", DeleteIngredientView.as_view(), name="ingredient-delete"),
    path("dish/del/<str:pk>", DeleteDishView.as_view(), name="dish-delete"),
    path("dish/update/<str:pk>", UpdateDishView.as_view(), name="dish-update"),
    path("ingredient/update/<str:pk>", UpdateIngredientView.as_view(), name="ingredient-update"),
    path("ingredient/list", IngredientAdminView.as_view(), name="ingredient-list"),
    path("dish/list", DishAdminView.as_view(), name="dish-list"),
]

