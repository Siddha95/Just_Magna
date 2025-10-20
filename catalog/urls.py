from django.urls import path
from .views import CatalogView, CatalogDetailView, IngredientCreateView, DeleteIngredientView, UpdateIngredientView, AmministrazioneView


urlpatterns = [
    # Catalog app
    path("", CatalogView.as_view(), name='home'),
    path("details/<int:pk>/", CatalogDetailView.as_view(), name="catalog-detail"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/del/<str:pk>", DeleteIngredientView.as_view(), name="ingredient-delete"),
    path("ingredient/update/<str:pk>", UpdateIngredientView.as_view(), name="ingredient-update"),
    path("ingredient/list", AmministrazioneView.as_view(), name="ingredient-list"),
]

