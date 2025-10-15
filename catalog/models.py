from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Dish(models.Model):
    name = models.CharField(max_length=200)
    gluten_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    price = models.FloatField(blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    gluten_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    



