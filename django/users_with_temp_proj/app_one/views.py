from django.shortcuts import render, redirect

from app_one.models import Users

def index(request):
    context = {
        "all_users" : Users.objects.all()
    }
    return render(request, "index.html", context)


def create_user(request):
    print(request.POST)

    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = request.POST['age']
    )
    return redirect("/")



# Create your views here.
