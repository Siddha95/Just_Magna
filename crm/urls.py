from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r"surveys", SurveyViewSet, basename='survey')
router.register(r"ratings", RatingViewSet, basename='rating')

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),

    path("success/", SuccessView.as_view(), name="success"),
    path('success-survey/', SuccessSurveyView.as_view(), name='success-survey'),

    path('survey/', SurveyView.as_view(), name='survey'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),

    path("api/", include(router.urls)),
]