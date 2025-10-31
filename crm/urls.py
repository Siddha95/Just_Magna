from django.urls import path 
from .views import *

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),

    path("success/", SuccessView.as_view(), name="success"),
    path('success-survey/', SuccessSurveyView.as_view(), name='success-survey'),

    path('survey/', SurveyView.as_view(), name='survey'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
]