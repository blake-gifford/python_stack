from django.shortcuts import render


def index(request):
    random.randint(1,100)
    return render(request, "index.html")


def answer(request):
    return 

# Create your views here.
