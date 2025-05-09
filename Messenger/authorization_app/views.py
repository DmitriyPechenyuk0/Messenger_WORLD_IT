from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from .forms import AuthorizationForm
# Create your views here.

class AuthorizationView(LoginView):
    template_name = "authorization_app/authorization.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'reg'
        return context
    

class LogOutView(LogoutView):
    next_page = '/'
