from django.conf import settings 
from django.db import models 
from django.utils import timezone 
from django.contrib.auth.models import User
from catalog.models import Dish




class Voucher(models.Model):
    title = models.CharField(max_length=200)
    discount_percentage = models.IntegerField()
    creation_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    valid = models.BooleanField(default=True)
    
    def is_valid(self):
        return self.expiry_date >= self.creation_date

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utente")

    def cart_total(self):
        total = 0
        for item in self.dishes.select_related("dish"):
            total += item.dish.price * item.quantity
        return total

    

    def __str__(self):
        return f"Carrello di Utente - {self.user.username}"

class Cart_dish(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Carrello", related_name="dishes")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Piatti")
    quantity = models.IntegerField(verbose_name="Quantità")
    
    def get_update_quantity_form(self):
        from ecommerce.forms import UpdateQuantityForm
        return UpdateQuantityForm(instance=self)

    def __str__(self):
        return f"Id del carrello - {self.cart.id}"
    



class Order(models.Model):
    pass
     
class Address(models.Model):
    pass 

class Invoice(models.Model):
    pass 

