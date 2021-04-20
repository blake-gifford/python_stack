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
    if request.method != 'POST':
        return redirect('/shows')
    # new_obj = show.object.create(
    # 
    # )
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
    context = {
        'show': Show.objects.get(id = show_id)
    }
    return render(request, 'edit.html', context)


def update_show(request, show_id):
    show = Show.objects.get(id = show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()

    return redirect('/shows')


def delete_show(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/shows')

# Create your views here.

