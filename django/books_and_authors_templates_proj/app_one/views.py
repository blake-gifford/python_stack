from django.shortcuts import render, redirect

from app_one.models import Author, Book


def index(request):
    print(request.POST)

    context = {
        "all_books" : Book.objects.all(),
        "all_authors" : Author.objects.all()
    }
    return render(request, "index.html", context)



def add_book(request):
    
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description']
    )
    return redirect('/')


def author(request):
    print(request.POST)

    context = {
        "all_books" : Book.objects.all(),
        "all_authors" : Author.objects.all()
    }
    return(request, "author.html", context) 


def add_author(request):
    
    Author.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        books = request.POST['books'],
    )
    return redirect('/')


def display_book(request):
    # return render(request, "display_book.html")
    pass


def display_author(request):
    # return render(request, "display_author.html")
    pass
