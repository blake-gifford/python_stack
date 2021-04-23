from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('homepage', views.homepage),
    # display paths
    path('message/new', views.add_message),
    path('comment/new', views.add_comment),
    # action paths
    # path('message/display', views.show_messages)
]