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
        # 'all_books': Book.objects.get(id = book_id),
    }
    return render(request, "author.html", context) 


def display_author(request, id):
    # return render(request, "display_author.html")
    context = {
    'all_authors': Author.objects.get(id = id),
    }
    return render(request, "display_author.html", context)


def add_author(request):

    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
        books = Book.objects.get(id = request.POST['books'])
        # books = request.POST['books']
    )
    return redirect('/author')


def display_book(request, id):
    context = {
        'all_books': Book.objects.get(id = id),
        'all_authors': Author.objects.all()
    }
    return render(request, "display_book.html", context)



