from django import forms
from django.core.exceptions import ValidationError
from .models import *


class ContactForm(forms.Form):
    nome = forms.CharField(
        required=True,
        max_length=200, 
        widget= forms.TextInput(attrs={"placeholder": "Il tuo nome"})
    )
    cognome = forms.CharField(
        required=True,
        max_length=200, 
        widget=forms.TextInput(attrs={"placeholder": "Il tuo cognome"})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "La tua mail"})
    )
    telefono = forms.CharField(
        required=False, 
        max_length=15, 
        widget=forms.TextInput(attrs={"placeholder": "Il tuo numero"})
    )
    soggetto = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={"placeholder": "Soggetto"})
    )
    messaggio = forms.CharField(max_length=254,
        widget=forms.Textarea(attrs={"placeholder": "Il tuo messaggio"})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if not email and not phone:
            raise ValidationError(
                "Devi fornire almeno un'email o un numero di telefono"
            )
        return cleaned_data
        