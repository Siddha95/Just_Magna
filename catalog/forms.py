from django import forms
from .models import Ingredient, Dish
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,HTML

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.add_input(Submit('submit', 'Salva piatto'))

        self.helper.layout = Layout(
            HTML('<h1>Inserisci un Piatto</h1>'),
            HTML('<h2>Movite Pure</h2>')
        )

        