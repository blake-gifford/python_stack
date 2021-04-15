from django.shortcuts import render, redirect

import random


def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0 
        request.session['activities'] = []
        
    return render(request, 'index.html')


def process_money(request):
    gold = 0
    if request.POST['location'] == 'farm':
        gold = random.randint(10,20)
        request.session['gold'] += gold
        # request.session['activities'].append(f"You have earned, {gold}.")
        # request.session.save()
    if request.POST['location'] == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        # request.session['activities'].append(f"You have earned, {gold}.")
        # request.session.save()
    if request.POST['location'] == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        # request.session['activities'].append(f"You have earned, {gold}.")
        # request.session.save()
    if request.POST['location'] == 'casino':
        gold = random.randint(-50,50)
        request.session['gold'] += gold
    request.session['activities'].append(f"You have walked out with {gold}.")
    request.session.save()
        # request.session['activities'] = f"You have walked out of the casino with, {request.session['gold']}. "
    
    return redirect("/")



# Create your views here.

