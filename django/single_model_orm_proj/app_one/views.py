from django.shortcuts import render, redirect

from .models import *


def index(request):
    return render(request, "index.html")


def create_user(request):
    print(request.POST)

    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = request.POST['age']
    )
    return redirect('/')

# Create your views here.
