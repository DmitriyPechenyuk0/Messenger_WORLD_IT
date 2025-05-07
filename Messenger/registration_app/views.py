from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin 
from django.contrib.auth.models import User
from .forms import RegistrationForm
import secrets, string
from django.core.mail import send_mail
# Create your views here.

class RegistrationView(FormMixin ,TemplateView):
    template_name='registration_app/registration.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['reg_form'] = RegistrationForm()
        return context
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            
            email=request.POST.get('email')
            code = ''
            for number in range(6):
                code += secrets.choice(string.digits)

            send_mail(
                'Код підтвердження реєстрації',
                f'Ваш код: {code}',
                None,
                [email],
            )
        return render(request, self.template_name, {'reg_form': RegistrationForm()})