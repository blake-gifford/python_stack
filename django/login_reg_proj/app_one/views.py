import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    # return redirect('/dashboard')
    return render(request, 'index.html')


def register(request):
    return redirect('/dashboard')


def login(request):
    return redirect('/dashboard')


def logout(request):
    return redirect('/')


def dashboard(request):
    return render(request, 'dashboard.html')

# Create your views here.
