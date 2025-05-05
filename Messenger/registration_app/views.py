from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin 
from django.contrib.auth.models import User
from .forms import RegistrationForm
# Create your views here.

class RegistrationView(FormMixin, TemplateView):
    template_name='registration_app/registration.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['reg_form'] = RegistrationForm()
        return context
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            user = User.objects.create_user(
                email=request.POST.get('email'),
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
        return render(request, self.template_name, {'reg_form': RegistrationForm()})