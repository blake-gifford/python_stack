from django.shortcuts import render, redirect

from app_one.models import Show

def index(request):
    return redirect('/shows')


def all_shows(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, 'all_shows.html', context)


def new_show(request):
    return render(request, "new_show.html")


def create_show(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows')


def display_show(request, show_id):
    context = {
        'show': Show.objects.get(id = show_id)
    }
    return render(request, 'display.html', context)


def edit_show(request, show_id):
    pass


def update_show(request, show_id):
    pass


def delete_show(request, show_id):
    pass

# Create your views here.

