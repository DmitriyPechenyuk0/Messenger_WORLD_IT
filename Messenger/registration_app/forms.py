from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введи пароль'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повтори пароль'}))

class CodeForm(forms.Form):
    code = forms.CharField(max_length=6 ,widget=forms.TextInput())