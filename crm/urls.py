from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r"surveys", SurveyViewSet, basename='api-survey')
router.register(r"ratings", RatingViewSet, basename='api-rating')

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),

    path("feedback/success/", FeedbackSuccessView.as_view(), name="feedback-success"),
    path('survey/success', SurveySuccessView.as_view(), name='survey-success'),

    path('survey/', SurveyView.as_view(), name='survey'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),

    path("api/", include(router.urls)),
]