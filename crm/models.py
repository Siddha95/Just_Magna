from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from catalog.models import Course, Dish
from django.core.validators import MinValueValidator, MaxValueValidator



class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utente")
    feedback = models.CharField(max_length=200, blank=True, null=True, verbose_name="Feedback")
    
    def __str__(self):
        return f"Survey di utente - {self.user.username}"
    

class Rating(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="Survey", related_name='ratings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Portata")
    vote = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(49)], 
        verbose_name="Punteggio"
    )
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Piatto preferito" )


    def __str__(self):
        return f"Punteggio del Survey di - {self.survey.user.username}"