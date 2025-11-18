from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Fieldset, Field


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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Invia messaggio'))
        
class SurveyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        courses = Course.objects.all()
        #Crispy
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'survey-form'
        self.helper.add_input(Submit('submit', 'Invia il sondaggio'))

        self.helper.layout = Layout()
        
        for course in courses:
            course_id = course.id

            vote_field = f'vote_{course_id}'
            self.fields[vote_field] = forms.IntegerField(
                required=True,
                label=mark_safe(f'<h3>Valutazione</h3>'),
                initial=3,
                widget= forms.NumberInput(attrs= {
                    'type':'range',
                    'min':'1',
                    'max':'5',
                    'step':'1',
                    'class': 'form-range col-sm-2',
                }),
                help_text="Trascina lo slider in base a quanto sei soddisfatto"
            )

            dish_field = f'dish_{course_id}'
            self.fields[dish_field] = forms.ModelChoiceField(
                queryset=course.dish_set.all(),
                required=False,
                label=f"Scegli un piatto preferito(se vuoi)",
                empty_label="Seleziona un piatto",
                widget=forms.Select(attrs={
                    'class': 'col-sm-6',
                })
            )

            self.helper.layout.append(
            Fieldset(
                mark_safe(f'<h1>{course.name}</h1>'),
                vote_field,
                HTML('<br></br>'),
                dish_field,
                HTML('<br></br>')

                )
            )


        self.helper.layout.append(
            Fieldset(
                mark_safe('<h1 style="text-align:center;">Feedback Generale</h1>'),
                Field('feedback', show_label=False)
            )
        )
        #Crispy form
    class Meta:
        model = Survey
        fields = ("feedback", )
        widgets = {
            'feedback' : forms.Textarea(attrs={
                'placeholder':'Lasciaci il tuo feedback',
            })
        }
         
    
