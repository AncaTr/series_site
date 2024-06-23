from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comentariu

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ComentariuForm(forms.ModelForm):
    class Meta:
        model = Comentariu
        fields = ['text']