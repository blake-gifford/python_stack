import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import User


def index(request):
    if "uuid" in request.session:
        return redirect('/dashboard')

    return render(request, 'index.html')


def register(request):
    print(request.POST['first_name'])
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")
    else:
        account = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = account
        )
        request.session['uuid'] = new_user.id

        return redirect('/dashboard')


def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")
    else:
        user = User.objects.get(email = request.POST['email'])

        request.session['uuid'] = user.id

    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    
    return redirect('/')


def dashboard(request):
    if "uuid" not in request.session:
        return redirect("/")
    context = {
        "logged_in_user": User.objects.get(id = request.session['uuid']),
        "all_users": User.objects.all()
    }

    return render(request, "dashboard.html", context)

# Create your views here.
