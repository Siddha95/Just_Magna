from django import forms 
from .models import *


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        label="Quantità",
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control text-center',
            'style': 'width: 80px;',

        })
    )

    dish_id = forms.IntegerField(widget=forms.HiddenInput())

    
    



    

    