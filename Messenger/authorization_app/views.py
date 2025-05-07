from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import AuthorizationForm
# Create your views here.

class AuthorizationView():
    template_name = "authorization_app/authorization.html"
    form_class = AuthorizationForm
