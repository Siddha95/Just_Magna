from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"dishes", DishViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"ingredients", IngredientViewSet)


urlpatterns = [
    # Catalog app
    path("", CatalogView.as_view(), name='home'),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/delete/<str:pk>", DeleteDishView.as_view(), name="dish-delete"),
    path("dish/update/<str:pk>", UpdateDishView.as_view(), name="dish-update"),
    path("dish/list", DishAdminView.as_view(), name="dish-list"),

    path("ingredient/delete/<str:pk>", DeleteIngredientView.as_view(), name="ingredient-delete"),
    path("ingredient/create", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/update/<str:pk>", UpdateIngredientView.as_view(), name="ingredient-update"),
    path("ingredient/list", IngredientAdminView.as_view(), name="ingredient-list"),

    # DRF API routes
    path("api/", include(router.urls)),    
]