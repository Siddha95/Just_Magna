from django.urls import path
from .views import CatalogView, CatalogDetailView, IngredientCreateView, DeleteIngredientView, UpdateIngredientView, AmministrazioneView



urlpatterns = [
    path("", CatalogView.as_view(), name='home'),
    path("details/<int:pk>/", CatalogDetailView.as_view(), name="catalog-detail"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/del/<str:id>", DeleteIngredientView.as_view(), name="ingredient-delete"),
    path("ingredient/update", UpdateIngredientView.as_view(), name="ingredient-update"),
    path("ingredient/list", AmministrazioneView.as_view(), name="ingredient-list"),

]