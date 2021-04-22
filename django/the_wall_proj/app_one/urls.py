from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('logout', views.logout),
    path('homepage', views.homepage),
]