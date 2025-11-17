from django.urls import path
from .views import *
from ecommerce import views

urlpatterns = [
    path('cart/add/', CartAddFormView.as_view(), name='add_to_cart'),
    path('cart_list/', CartTemplateView.as_view(), name='cart_list'),
    path('cart/<int:pk>/edit/', QuantityEditView.as_view(), name='quantity_edit'),

    #API Routes for APiViews
    path("api/vouchers/", views.VoucherListAPIView.as_view()),
    path("api/carts/", views.CartListAPIView.as_view()),
    path("api/cart_dishes/", views.CartDishAPIView.as_view()),
]
