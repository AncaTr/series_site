from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import Comentariu
from django.contrib.auth.models import User
from main.models import Serial
class SerialForm(forms.ModelForm):
    class Meta:
        model = Serial
        fields = ['field1', 'field2', 'field3']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ComentariuForm(forms.ModelForm):
    class Meta:
        model = Comentariu
        fields = ['text']
