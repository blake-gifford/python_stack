import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import User, Message, Comment

def index(request):
    if "uuid" in request.session:
        return redirect('/homepage')

    return render(request, 'index.html')

def register(request):
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

        return redirect('/homepage')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])

        request.session['uuid'] = user.id

    return redirect('/homepage')



def logout(request):
    request.session.clear()

    return redirect('/')


def homepage(request):

    if "uuid" not in request.session:
        return redirect("/")

    context = {
        "logged_in_user": User.objects.get(id = request.session['uuid']),
        "all_messages": Message.objects.all()
    }
    return render(request, 'homepage.html', context)


def add_message(request):

    errors = Message.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
            return redirect('/homepage')

    Message.objects.create(
        message = request.POST['message'],
        user= User.objects.get(id = request.session['uuid'])
    )
    return redirect('/homepage')


def add_comment(request):

    errors = Comment.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
            return redirect('/homepage')

    Comment.objects.create(
        comment = request.POST['comment'],
        message = request.POST['message'],
        user = User.objects.get(id = request.session['uuid'])
    )
    return redirect('/homepage')
# Create your views here.


