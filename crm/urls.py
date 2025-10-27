from django.urls import path 
from .views import *

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('success-survey/', SuccessSurveyView.as_view(), name='success-survey'),
    path('unsuccess-survey/', SuccessSurveyView.as_view(), name='unsuccess-survey'),
]
