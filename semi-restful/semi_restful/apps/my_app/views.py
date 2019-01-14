from django.shortcuts import render,redirect
from .models import *
import datetime

def index(request):
    return redirect('/users')

def users(request):
    user_query={
        'users' : User.objects.all()
    }
    return render(request, 'users.html', user_query)

def show(request,id):
    
    show_query={
        'shows':User.objects.get(id = id)
    }

    return render(request, 'show.html', show_query)

def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect('/')

def edit(request,id):
    edit_query={
        'users': User.objects.get(id=id)
    }

    return render(request, 'edit.html', edit_query)

def update(request,id):
    update = User.objects.get(id=id)
    update.first_name = request.POST['first_name']
    update.last_name = request.POST['last_name']
    update.email = request.POST['email']
    update.save()
    return redirect('/')

def add(request):
   
    return render(request,'new.html')

def process(request):

    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/')




    






