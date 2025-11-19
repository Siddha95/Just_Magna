from rest_framework import routers
from .viewsets import *
from django.urls import path, include

# DRF API
router = routers.DefaultRouter()
router.register(r"survey", SurveyViewSet, basename='api-survey')
router.register(r"rating", RatingViewSet, basename='api-rating')

urlpatterns = [
    path("api/", include(router.urls)),
]