from django.conf import settings 
from django.db import models 
from django.utils import timezone 



class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True,blank=True, verbose_name="Portata")
    gluten_free = models.BooleanField(default=False, verbose_name="Senza glutine")
    vegetarian = models.BooleanField(default=False, verbose_name="Vegetariano")
    vegan = models.BooleanField(default=False, verbose_name="Vegano")
    price = models.FloatField(blank=True, null=True, verbose_name="Prezzo")
    descrizione = models.TextField(blank=True, null=True, verbose_name="Descrizione")
    image = models.ImageField(upload_to='images/', verbose_name="Immagine")

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    gluten_free = models.BooleanField(default=False,verbose_name="Senza glutine")
    vegetarian = models.BooleanField(default=False, verbose_name="Vegetariano")
    vegan = models.BooleanField(default=False, verbose_name="Vegano")

    def __str__(self):
        return self.name

