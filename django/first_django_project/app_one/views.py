from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("this is the equivalent of @app.route!")


def root_method(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new_method(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create_method(request):
    return redirect("/")


def number_method(request, num):
    return HttpResponse(f"place holder to display blog number {num}")


def edit_method(request, num):
    return HttpResponse(f"placeholder to edit blog {num}!")


def delete_method(request, num):
    return redirect("/")

# Create your views here.
