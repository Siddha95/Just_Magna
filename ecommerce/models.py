from django.conf import settings 
from django.db import models 
from django.utils import timezone 




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
    

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField((""), max_length=200)


    def __str__(self):
        return (self.name + ' ' + self.surname)

