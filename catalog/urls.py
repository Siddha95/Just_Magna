from django.urls import path
from catalog.views import CatalogView
from django.contrib import admin

urlpatterns = [
    path("", CatalogView.as_view(), name='catalog'),
]