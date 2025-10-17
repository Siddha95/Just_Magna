from django.urls import path
from .views import CatalogView, CatalogDetailView, IngredientCreateView



urlpatterns = [
    path("", CatalogView.as_view(), name='home'),
    path("details/<int:pk>/", CatalogDetailView.as_view(), name="catalog-detail"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create")
]