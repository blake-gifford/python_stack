from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('author', views.author),
    path('add_author', views.add_author),
    path('books/<int:id>', views.display_book),
    path('author/<int:id>', views.display_author),
]

