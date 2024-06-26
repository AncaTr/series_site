from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.template import loader
from main.models import Review

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def root(request):
    return redirect("series_list")
def series_list(request):
    series = Serial.objects.all()
    template = loader.get_template('series_list.html')
    context = {'series_list': series}
    return HttpResponse(template.render(context, request))
def register(request):
    return HttpResponse("<h2>Register page</h2>")
def user_settings(request):
    return HttpResponse("<h2>User settings</h2>")

def adauga_comentariu(request, serial_id):
    # Your add comment logic here
    return render(request, 'series/static/templates/registration/adauga_comentariu.html',
                  {'serial_id': serial_id})

def login(request):
    return HttpResponse("<h2>Login page</h2>")
def homepage(request):
    return HttpResponse("<h2>home page</h2>")
def serial_page(request):
    return HttpResponse("<h2>home page</h2>")
from django.shortcuts import render
from .models import Serial

def search(request):
    query = request.GET.get('q')
    if query:
        results = Serial.objects.filter(titlu__icontains=query)
    else:
        results = []
    return render(request, 'search_result.html', {'results': results, 'query': query})


def submit_review(request, serial_id):
    assert request.method == 'POST'
    name = request.POST.get('name')
    comment = request.POST.get('comment')
    rating = request.POST.get('rating')
    # Procesează datele aici (de ex. salvează în baza de date sau altă acțiune)

    serial = Serial.objects.get(pk=serial_id)
    user = request.user

    review = Review(
        name=name,
        comment=comment,
        rating=rating,
        reviewer=user,
        serial=serial,
    )

    review.save()

    # Exemplu de redirectionare către pagina principală după submit
    return redirect('series_list')
    # Înlocuiește 'series_list' cu numele corect al view-ului tău pentru listarea serialelor
def reviews(request, serial_id):
    reviews = Review.objects.filter(serial_id=serial_id)
    template = loader.get_template('reviews_list.html')
    context = {'reviews_list': reviews}
    return HttpResponse(template.render(context, request))


def my_view(request):
    series_list = Serial.objects.all()  # Obținem lista de serii din baza de date
    reviews_list = Review.objects.all()  # Obținem lista de recenzii din baza de date

    concatenated_titles = ' - '.join([series.title for series in series_list])

    return render(request, 'my_template.html', {
        'reviews_list': reviews_list,
        'concatenated_titles': concatenated_titles
    })
