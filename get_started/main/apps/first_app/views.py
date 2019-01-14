from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "hello world"
    return HttpResponse(response)
