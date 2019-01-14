from django.shortcuts import render,redirect
from .models import *


def index (request):
    if 'items' not in request.session:
        request.session['items'] = 0

    if 'order_price' not in request.session:
        request.session['ordered_price'] = 0

    if 'price_total' not in request.session:
        request.session['price_total'] = 0

    storefront ={
        'items' : Item.objects.all()
    }
    return render(request, 'index.html', storefront)

def process(request):
    b = Item.objects.get(id=request.POST['id'])
    request.session['items'] += int(request.POST['quantity'])
    request.session['ordered_price'] = float(request.POST['quantity']) * float(b.price)
    request.session['price_total'] += float(request.POST['quantity']) * float (b.price)
    return redirect('/thank_you')

def thank_you(request):
    context={
        'order_price':request.session['ordered_price'],
        'price_total':request.session['price_total'],
        'items':request.session['items']
    }
    return render(request, 'thanks.html', context)



