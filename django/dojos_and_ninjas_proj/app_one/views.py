from django.shortcuts import render, redirect

# from app_one.models import Dojo

def index(request):
    # context = {
    #     "all_users" : Users.objects.all()
    # }
    return render(request, "index.html")

# Create your views here.
