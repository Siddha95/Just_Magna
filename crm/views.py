from django.shortcuts import redirect
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.conf import settings 
from .models import Rating, Survey
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, DetailView
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

    #check se utente ha fatto un survey
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        if request.user.is_authenticated:
            try: 
                survey = Survey.objects.get(user=request.user)
                #REDIRECT SU DETAIL VIEW 
                return redirect(reverse("survey-detail", kwargs={"pk": survey.pk}))
                #redirect(SurveyDetailView pk = survey.id) )scritto a cazzo vedi comem si fa
            except Survey.DoesNotExist:
                pass
        
        return response

        #if Survey.objects.filter(user=request.user).exists():
        #    return render(request, 'crm/survey_detail.html')
        

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user 
        response =  super().form_valid(form)

        for course in Course.objects.all():
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

class SurveyDetailView(DetailView):
    
    model = Survey
    #manca il controllo: se il survey non ha user = request.user -> morte
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object è oggetto mostrato
        context["ratings"] = Rating.objects.filter(survey = self.object)
        return context
    