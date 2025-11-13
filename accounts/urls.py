from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUpView
from accounts import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
    path("users/", views.UserListAPIView.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)

