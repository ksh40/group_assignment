from django import forms
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Donor
        fields = ['name', 'email', 'phone', 'age', 'password']

class DonorLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
