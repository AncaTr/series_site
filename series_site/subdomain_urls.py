# your_project/subdomain_urls.py

from django.urls import path
from your_app.views import series_list

urlpatterns = [
    path('series_list/', series_list, name='series_list'),
]
