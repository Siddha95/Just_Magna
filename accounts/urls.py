from django.urls import path, include
from .views import SignUpView
from accounts import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),

    # DRF API
    path("api/users/", views.UserListAPIView.as_view()),    
]


