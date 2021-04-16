from django.shortcuts import render, redirect

from app_one.models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos" : Dojo.objects.all(),
        "all_ninjas" : Ninja.objects.all()
    }
    return render(request, "index.html")


def submit(request):
    print(request.POST)

    Dojo.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = request.POST['dojo']
    )
    return redirect('/')

# Create your views here.
