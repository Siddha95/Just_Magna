from django.urls import path
from .views import AddCartView

urlpatterns = [
    path('cart/add/<int:dish_id>/', AddCartView.as_view(), name='add_to_cart'),
]
