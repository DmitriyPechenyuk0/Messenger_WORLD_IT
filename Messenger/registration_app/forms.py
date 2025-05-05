from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())