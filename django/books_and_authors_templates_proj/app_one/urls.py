from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('author', views.author),
    path('add_aurthor', views.add_author),
    # path('books/<int:book_id>', views.display_book),
    # path('authors/<int:author_id>', views.display_author),
]