from django.urls import path 
from .views import *

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path('survey/', AddSurveyView.as_view(), name='add-survey'),
    path('rating/', AddRatingView.as_view(), name='add-rating'),
    path('success-survey', SuccessSurveyView.as_view(), name='success-survey'),
]
