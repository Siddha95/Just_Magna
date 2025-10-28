from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SuccessView(TemplateView):
    template_name = "crm/success.html"
class SuccessSurveyView(TemplateView):
    template_name = "crm/success_survey.html"

class ContactView(FormView):
    form_class = ContactForm
    template_name = "crm/contact.html"

    def get_success_url(self):
        return reverse("success")
    
    def form_valid(self, form):
        name = form.cleaned_data.get("Nome")
        surname = form.cleaned_data.get("cognome")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Ricevuto un messaggio da mail {email}
            Nome: {name} 
            Cognome: {surname}
            Telefono: {phone} 
            Soggetto: {subject}
            ___________________________

            {message}
            
            """

        send_mail(
            subject="Ricevuto il form di contatto",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)

class SurveyView(LoginRequiredMixin, CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'crm/survey_form.html'
    success_url = reverse_lazy('success-survey')

    def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
        if Survey.objects.filter(user=request.user).exists():
            return render(request, 'crm/survey_already_submitted.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # form.instance.user = self.request.user 
        user = self.request.user
        # if Survey.objects.filter(user=user).exists():
        #     return render(self.request, 'crm/unsuccess_form.html')
        form.instance.user = user 
        # questa salva il nuovo oggetto Survey nel database
        response =  super().form_valid(form)

        for course in Course.objects.all():
            #a questo punto devi usare form.cleaned_data e NON request.POST
            vote = form.cleaned_data.get(f'vote_{course.id}')
            dish = form.cleaned_data.get(f'dish_{course.id}')
            if vote:
                Rating.objects.create(
                    survey=self.object,
                    course=course,
                    vote=int(vote),
                    dish_id = dish.id if dish else None
                )

        return response
    