from django.shortcuts import render, redirect

from app_one.models import Author, Book


def index(request):
    return render(request, "index.html")


def add_book(request):
    return redirect
# Create your views here.
