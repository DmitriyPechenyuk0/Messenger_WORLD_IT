from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.core.mail import send_mail
import secrets, string
# Create your views here.

class RegistrationView(FormView):
    template_name='registration_app/registration.html'
    form_class = RegistrationForm
    success_url='/'    
    def form_valid(self, form):
        email=form.cleaned_data['email']
        code = ''
        for number in range(6):
            code += secrets.choice(string.digits)

        send_mail(
            'Підтвердіть Електронну Адресу',
            f'Дякуємо що користуєтесь World IT Messenger!\nКод підтвердження реєстрації: {code}',
            None,
            [email],
        )
        return super().form_valid(form)
    