from django.shortcuts import render, redirect

from app_one.models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)


def create_dojo(request):
    print(request.POST)

    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    # Ninja.objects.create(
    #     first_name = request.POST['first_name'],
    #     last_name = request.POST['last_name'],
    #     dojo = request.POST['dojo']
    # )
    return redirect('/')


def create_ninja(request):
    print(request.POST)

    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = Dojo.objects.get(id = request.POST['dojo'])
    )
    return redirect("/")

# Create your views here.
