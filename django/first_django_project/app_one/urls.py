from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.root_method),
    path('blogs/new', views.new_method),
    path('blogs/create', views.create_method),
    path('blogs/<int:num>', views.number_method),
    path('blogs/<int:num>/edit', views.edit_method),
    path('blogs/<int:num>/delete', views.delete_method),
]