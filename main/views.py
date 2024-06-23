
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, ComentariuForm
from .models import Serial
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Contul a fost creat pentru {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'seriale/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Utilizator sau parolă invalidă.')
        else:
            messages.error(request, 'Utilizator sau parolă invalidă.')
    form = AuthenticationForm()
    return render(request, 'seriale/login.html', {'form': form})

def home(request):
    seriale = Serial.objects.all()
    return render(request, 'seriale/home.html', {'seriale': seriale})

def adauga_comentariu(request, serial_id):
    serial = Serial.objects.get(id=serial_id)
    if request.method == 'POST':
        form = ComentariuForm(request.POST)
        if form.is_valid():
            comentariu = form.save(commit=False)
            comentariu.utilizator = request.user
            comentariu.serial = serial
            comentariu.save()
            return redirect('home')
    else:
        form = ComentariuForm()
    return render(request, 'seriale/adauga_comentariu.html', {'form': form})


# Create your views here.
