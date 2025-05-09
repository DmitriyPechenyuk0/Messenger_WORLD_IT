from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class CodeForm(forms.Form):
    code = forms.CharField(max_length=6 ,widget=forms.TextInput())