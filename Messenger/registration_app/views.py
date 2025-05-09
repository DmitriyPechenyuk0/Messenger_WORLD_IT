from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.models import User
from .forms import RegistrationForm, CodeForm
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from .models import RegistrationCodes
from django.http import HttpRequest
import secrets, string

# Create your views here.

class RegistrationView(View):
    def get(self, request: HttpRequest):
        return render(request, 'registration_app/registration.html', {
            'form': RegistrationForm()
        })
    def post(self, request: HttpRequest):
        button = request.POST.get('submitform')
        if button == 'mainform':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                    email=form.cleaned_data['email']
                    code = ''
                    for number in range(6):
                        code += secrets.choice(string.digits)

                    RegistrationCodes.objects.create(
                        email=email,
                        code=code
                    )
                    send_mail(
                        'Підтвердіть Електронну Адресу',
                        f'Дякуємо що користуєтесь World IT Messenger!\nКод підтвердження реєстрації: {code}',
                        None,
                        [email],
                    )
                    response = render(request, 'registration_app/registration.html', {
                            'form': RegistrationForm(),
                            'codeform': CodeForm})
                    
                    response.set_cookie('email', form.cleaned_data['email'])
                    response.set_cookie('password', form.cleaned_data['password'])

                    return response
                else:
                    form.add_error('confirm_password', 'Паролі не співпадають')
                    return render(request, 'registration_app/registration.html', {'form': RegistrationForm()})
            else:
                return render(request, 'registration_app/registration.html', {'form': RegistrationForm()})
        elif button == 'codeform':
            form = CodeForm(request.POST)
            print('add')
            if form.is_valid():
                email = request.COOKIES.get('email')
                print(email, RegistrationCodes.objects.filter(email=email).exists())
                if email != None and RegistrationCodes.objects.filter(email=email).exists() == True:
                    auth_code = request.COOKIES.get('password')
                    entered_code = form.cleaned_data['code']
                    print('True True True')
                    if entered_code == auth_code:
                        password = request.COOKIES.get('password')
                        print('User Created')
                        User.objects.create_user(username=email, email=email, password=password)

                        response = render(request, 'registration_app/registration.html', {
                                'form': RegistrationForm(),
                                'codeform': CodeForm,
                                'success': 'successed'})

                        response.delete_cookie('email')
                        response.delete_cookie('password')
                        return response
                    else:
                        return render(request, 'registration_app/registration.html', {
                            'form': RegistrationForm(),
                            'codeform': CodeForm()})
                else:
                    return render(request, 'registration_app/registration.html', {
                        'form': RegistrationForm(),
                        'codeform': CodeForm()})
            else:
                form.add_error('confirm_password', 'Паролі не співпадають')
                return render(request, 'registration_app/registration.html', {
                    'form': RegistrationForm(),
                    'codeform': CodeForm()})
