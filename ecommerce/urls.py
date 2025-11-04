from django.urls import path
from .views import *

urlpatterns = [
    path('cart/add/<int:dish_id>/', CartAddView.as_view(), name='add_to_cart'),
    path('cart/<str:user_username>', CartTemplateView.as_view(), name='cart_template')
]
