from .api import *
from django.urls import path

# DRF API
urlpatterns = [
   
    path("api/user/", UserListAPIView.as_view()), 
    path("api/user/create", UserCreateAPIView.as_view()),      
]