from django.urls import path
from .api import *

# DRF API
urlpatterns = [

    path("course/", CourseListAPIView.as_view()),
    path("dish/", DishListAPIView.as_view()),
    path("ingredient/", IngredientListAPIView.as_view()),
    path("dish/<int:pk>/", DishDetailAPIView.as_view()),
    
]
