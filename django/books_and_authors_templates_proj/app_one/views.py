from django.shortcuts import render, redirect

# from app_one.models import 


def index(request):
    return render(request, "index.html")
# Create your views here.
