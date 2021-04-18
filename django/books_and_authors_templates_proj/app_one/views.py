from django.shortcuts import render, redirect

from app_one.models import Author, Book


def index(request):
    print(request.POST)

    context = {
        "all_books" : Book.objects.all(),
        "all_authors" : Author.objects.all()
    }
    return render(request, "index.html", context)


# def authors(request):
#     return render(request, "author.html")


# def add_author(request):
#     pass
# Create your views here.
