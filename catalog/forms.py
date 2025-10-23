from django import forms
from .models import *

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'gluten_free', 'vegan', 'vegetarian']
        widgets = {
            # 'name': forms.TextInput(attrs={'class':'form-control'})
        }

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish 
        fields = ['name', 'gluten_free', 'vegetarian', 'vegan', 'price', 'course', 'descrizione', 'image']
        widgets = {
            # 'name' : forms.TextInput(attrs={'class':'form-control'}),
            # 'descrizione' : forms.TextInput(attrs={'rows':3, 'class': 'form-control'}),
            # 'image' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
        }