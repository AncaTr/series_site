
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from main.models import Serial
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def root(request):
    return redirect("series_list")
def series_list(request):
    series = Serial.objects.all()
    return render(request, 'series_list.html', {'series': series})
def register(request):
    return HttpResponse("<h2>Register page</h2>")
def user_settings(request):
    return HttpResponse("<h2>User settings</h2>")

def adauga_comentariu(request, serial_id):
    # Your add comment logic here
    return render(request, 'adauga_comentariu.html', {'serial_id': serial_id})

def login(request):
    return HttpResponse("<h2>Login page</h2>")
def homepage(request):
    return HttpResponse("<h2>home page</h2>")
