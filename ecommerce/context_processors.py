from .models import Cart, Cart_dish
from django.db.models import Sum

def cart_item_count(request):
    cart_count = 0
    if request.user.is_authenticated:
       
        try:
            cart= Cart.objects.get(user=request.user)
            cart_user_dish = Cart_dish.objects.filter(cart=cart)
            cart_count = cart_user_dish.aggregate(Sum('quantity'))['quantity__sum']
            
        except Cart.DoesNotExist:
            pass
            
    return{'cart_item_count': cart_count}