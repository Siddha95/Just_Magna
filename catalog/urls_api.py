from django.urls import path, include

from .views import *
from catalog import views

urlpatterns = [
    # Catalog app

    # DRF API routes
    path("courses/", views.CourseListAPIView.as_view()),
    path("dishes/", views.DishListAPIView.as_view()),
    path("ingredients/", views.IngredientListAPIView.as_view()),
    path("dishes/<int:pk>/", views.DishDetailAPIView.as_view()),
    
]
