
from django.contrib import admin
from django.urls import path, include

from main import views
from django.contrib.auth.urls import urlpatterns as accounts_urlpatterns


accounts_urlpatterns.append(
    path("signup/", views.SignUpView.as_view(), name="signup")
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.root, name="root"),
    path('series_list/', views.series_list, name='series_list'),
    path("homepage/", views.homepage, name="home"),
    path("user_settings/", views.user_settings, name="user_settings"),
    path("accounts/", include(accounts_urlpatterns)),
    path('adauga_comentariu/<int:serial_id>/', views.adauga_comentariu, name='adauga_comentariu'),
    path('search/', views.search, name='search'),

]

