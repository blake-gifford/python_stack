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
    return render(request, "author.html", context) 


def add_author(request):
    print(request.POST)
    
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
        books = request.POST['books'],
    )
    return redirect('/author')


# def display_book(request):
#     # return render(request, "display_book.html")
#     context = {
#         "book": Book.objects.get(id = 'book_id'),
#         "author": Author.objects.all()
#     }
#     return render(request, "display_book.html", context)
# context = {
#         "jedi": Jedi.objects.get(id = jedi_id),
#         "force_powers": ForcePower.objects.all()
#     }


# def display_author(request):
#     # return render(request, "display_author.html")
#     pass
