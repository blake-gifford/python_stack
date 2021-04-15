from django.shortcuts import render, HttpResponse, redirect


def index(request):
    # check if key 'num' is already in session
    # start 'num' at 0
    # else increment by 1
    if 'num' not in request.session:
        request.session['num'] = 0
    
    request.session['num'] += 1

    return render(request, "index.html")


# def counter(request):
#     request.session['num'] = 0
    


def success(request):
    del request.session['num']
    return redirect('/')

# Create your views here.

