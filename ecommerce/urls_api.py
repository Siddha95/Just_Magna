from django.urls import path
from .views import *
from .api import *


urlpatterns = [
    #API Routes for APiViews
    path("api/voucher/", VoucherListAPIView.as_view()),
    path("api/cart/", CartListAPIView.as_view()),
    path("api/cart_dish/", CartDishAPIView.as_view()),
]