from django import forms 
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,HTML
from django.core.exceptions import ValidationError

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        label="Quantità",
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control text-center',

        })
    )

    dish_id = forms.IntegerField(widget=forms.HiddenInput())


class UpdateQuantityForm(forms.ModelForm):
    class Meta: 
        model = Cart_dish
       
        fields = ['quantity',]
        widgets = {
            'quantity': forms.NumberInput(attrs={
            'class': 'form-control text-center',

            })
        }


class ShippingForm(forms.Form):

    PAYMENT_CHOICES = [
        [1, "Paypal"],
        [2, "Carta di credito"],
        [3, "Carta di debito"],
    ]

    address = forms.CharField(
        label="Indirizzo",
        required=True,
        max_length=200, 
        widget= forms.TextInput(attrs={"placeholder": "Il tuo indirizzo"})
    )

    payment = forms.ChoiceField(
        label="Metodi di pagamento",
        choices=PAYMENT_CHOICES, 
        required=True
        
        )
    
    comment = forms.CharField(
        label="Commento aggiuntivo",
        required=False,
        initial=None,
        max_length=200, 
        widget= forms.Textarea(attrs={"placeholder": "Dacci ulteriori indicazioni o lascia un commento"})
    )

    def clean(self):
        cleaned_data = super().clean()
        address = cleaned_data.get('address')
        payment= cleaned_data.get('payment')
        comment = cleaned_data.get('comment')

        # if not address or not payment:
        #     raise ValidationError(
        #         "Devi fornire almeno un indirizzo e metodo di pagamento!"
        #     )
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.add_input(Submit('submit', 'Conferma'))


    

    