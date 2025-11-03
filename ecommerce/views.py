from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import FormView 
from django.contrib.auth.mixins import LoginRequiredMixin



class CartAddView(LoginRequiredMixin, FormView):
    form_class = CartForm
    
    

    def form_valid(self, form):
        #qui scrivo l'user su Cart
        form.instance.user = self.request.user
        return super().form_valid(form)
    


    def get_context_data(self, **kwargs):

        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
            return super().get_context_data(**kwargs)