from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import AuthorizationForm
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
        print(email, password)
        if form.is_valid():
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    
                    login(request, user)

                else:
                    user = None
            except User.DoesNotExist:
                user = None
        return render(request, self.template_name, {'auth_form': AuthorizationForm()})

        
            
    

