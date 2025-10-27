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
    

# class AddRatingView(LoginRequiredMixin, CreateView):
#     form_class = RatingForm
#     template_name = 'crm/rating_form.html'
#     success_url = reverse_lazy('add-survey')


# class AddSurveyView(LoginRequiredMixin, CreateView):
#     form_class = SurveyForm
#     template_name = 'crm/survey_form.html'

#     def get_success_url(self):
#         return reverse_lazy("success-survey")


class SurveyView(LoginRequiredMixin, CreateView):
    model = Survey
    fields = ["feedback"]
    template_name = 'crm/survey_form.html'
    success_url = reverse_lazy('success-survey')

    def form_valid(self, form):
        # form.instance.user = self.request.user 
        user = self.request.user
        if Survey.objects.filter(user=user).exists():
            return render(self.request, 'crm/unsuccess_form.html')
        form.instance.user = user 
        return super().form_valid(form)