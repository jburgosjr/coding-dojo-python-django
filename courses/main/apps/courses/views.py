from django.shortcuts import render, redirect
from .models import *

def index(request):
    all_courses={
        'courses':Course.objects.all(),
        'descriptions': Description.objects.all()
        
    }
    return render(request,'home.html',all_courses)

def add(request):
   b = Course.objects.create(name = request.POST['course_name'])
   Description.objects.create(desc = request.POST['course_description'], courses = b)
   return redirect('/')

def delete(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
    
