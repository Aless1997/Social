from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Post, Tipologia

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nome', 'tipologia', 'target', 'descrizione']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['compania', 'oggetto']

class TipologiaForm(forms.ModelForm):
    class Meta:
        model = Tipologia
        fields = ['nominativo']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()