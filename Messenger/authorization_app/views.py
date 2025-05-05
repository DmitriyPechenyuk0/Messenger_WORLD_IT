from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import AuthorizationForm
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login

# Create your views here.

class AuthorizationView(TemplateView, FormMixin):
    template_name = "authorization_app/authorization.html"
    form_class = AuthorizationForm

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['auth_form'] = AuthorizationForm()
        return context
    
    def post(self, request):
        form = self.get_form()
        email = request.POST.get("email")
        password = request.POST.get("password")
        if form.is_valid():
            user = authenticate(request=request, password=password)
            if user:
                login(request=request, user=user)
                print("qqqqqq")

        
            
    

