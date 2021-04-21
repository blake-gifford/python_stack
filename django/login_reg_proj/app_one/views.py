import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    return redirect('/dashboard')


def register(request):
    return render(request, 'index.html')


def login(request):
    pass


def logout(request):
    pass


def dashboard(request):
    pass

# Create your views here.
