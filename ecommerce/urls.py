from django.urls import path
from .views import *

urlpatterns = [
    path('cart/add/', CartAddFormView.as_view(), name='add_to_cart'),
    path('cart_list/', CartTemplateView.as_view(), name='cart_list'),
    path('cart/<int:pk>/edit/', QuantityEditView.as_view(), name='quantity_edit'),
]
