from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def counter(request):
    request.session['num'] = 1
    


def success(request):
    # del request.session['num']
    return redirect('/')

# Create your views here.

