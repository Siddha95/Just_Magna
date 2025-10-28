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
    

# class RatingForm(forms.ModelForm):

#     class Meta:
#         model = Rating
#         fields = ['survey', 'course', 'vote', 'dish']
#     widgets = {
#         # vuote per ora
#     }   

# class SurveyForm(forms.ModelForm):

#     class Meta:
#         model = Survey
#         fields = ['user', 'feedback'] 

#     widgets = {
#         # vuote per ora
#     }     


class SurveyForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        courses = Course.objects.all()

        for course in courses:
            course_id = course.id
            course_title = course.title


            vote_field_name = f'vote_{course_id}'
            self.fields[vote_field_name] = forms.IntegerField(
                required = True,
                label=f'{course_title} valutazione',
                initial= 3,
                validators = [MinValueValidator(1), MaxValueValidator(5)],
                widget= forms.NumberInput(attrs= {
                    'type': 'range',
                    'min': '1',
                    'max': '5',
                    'step': '1',
                    'class': 'form-range'
                }),
                # help_text="Trascina lo slider da 1 a 5"
            )

            
            dish_field_name = f'dish_{course_id}'
            self.fields[dish_field_name] = forms.ModelChoiceField(
                queryset=course.dish_set.all(),
                required=False,
                label=f'Scegli un piatto preferito (se vuoi)',
                empty_label='Seleziona un piatto',
                widget=forms.Select(attrs={
                    'class' : 'form-select'
                })
            )

            
        

    class Meta:
         model = Survey
         fields = ('feedback',)
         widgets = {
             'feedback' : forms.Textarea(attrs={
                 'rows': 5,
                 'placeholder': 'Lasciaci il tuo feedback'
             })
         }


    

    
