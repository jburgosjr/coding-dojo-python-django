from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    ran_string = get_random_string(length=14) 
    random ={
       'rtext': ran_string
    }

    if 'count' not in request.session:
        request.session['count'] = 1

    return render(request,'index.html', random)

def random(request):
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
    


