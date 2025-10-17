from django import forms
from .models import Ingredient

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
            'name': forms.TextInput(attrs={'classes':'form-control'})
        }
    def clean(self):
        fields = self.cleaned_data