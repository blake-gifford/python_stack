from django.shortcuts import render, redirect

from app_one.models import Author, Book


def index(request):
    context = [
        "all_books": Book.object.all(),
        "all_authors": Author.object.all()
    ]
    return render(request, "index.html", context)


def add_book(request):
    return redirect
# Create your views here.
