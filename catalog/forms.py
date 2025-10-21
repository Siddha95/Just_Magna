from django import forms
from .models import *

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'gluten_free', 'vegan', 'vegetarian']
        labels = {'name' : 'Nome',
                  'gluten_free' : 'Gluten Free',
                  'vegan' : 'Vegano',
                  'vegetarian' : 'Vegetariano'
        }
        widgets = {
            # 'name': forms.TextInput(attrs={'class':'form-control'})
        }

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish 
        fields = ['name', 'gluten_free', 'vegetarian', 'vegan', 'price', 'descrizione', 'image']
        labels = { 'name' : 'Nome',
                  'gluten_free' : 'Gluten Free',
                  'vegan' : 'Vegano',
                  'vegetarian' : 'Vegetariano',
                  'price' : 'Prezzo',
                  'descrizione' : 'Descrizione',
                  'image' : 'Immagine',
        }
        widgets = {
            # 'name' : forms.TextInput(attrs={'class':'form-control'}),
            # 'descrizione' : forms.TextInput(attrs={'rows':3, 'class': 'form-control'}),
            # 'image' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
        }