from django.shortcuts import redirect
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.conf import settings 
from .models import Rating, Survey
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, DetailView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from rest_framework import permissions, viewsets, mixins
from .serializers import SurveySerializer, RatingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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
    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)

    #     if request.method == 'GET' and request.user.is_authenticated:
    #         try: 
    #             survey = Survey.objects.get(user=request.user)             
    #             return redirect(reverse_lazy("survey-detail", kwargs={"pk": survey.pk}))
    #         except Survey.DoesNotExist:
    #             pass
        
    #     return response
    
    def get(self, request, *args, **kwargs):
        self.object = None
        try: 
            survey = Survey.objects.get(user=request.user)
            return redirect(reverse_lazy("survey-detail", kwargs={"pk": survey.pk}))
        except Survey.DoesNotExist:
            pass
        return super().get(request, *args, **kwargs)

    
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

    def get_object(self, queryset = None):
        
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object è oggetto mostrato
        context["ratings"] = Rating.objects.filter(survey = self.object)
        return context
    

#Viewsets
# provo con custom viewset
class RatingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #PERCHÈ NON SI VEDE NIENTE IN GET E MI TORNA ERRORE? 
    
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by("-id")
    serializer_class = SurveySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    