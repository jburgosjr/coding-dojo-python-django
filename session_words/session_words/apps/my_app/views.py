from django.shortcuts import render, redirect
from time import strftime, localtime

def index(request):
    if 'word_log' not in request.session:
        request.session['word_log'] = []
  

    
    
    return render(request, 'index.html')

def process(request):
    
    if "bold" in request.POST:
        session_word = {
            'word':request.POST['word'],
            'color':request.POST['color'],
            'bold':request.POST['bold'],
            'time':strftime('%m/%d/%Y %I:%M %p', localtime())
            
        }
        temp = request.session['word_log']
        temp.insert(0,session_word)
        request.session['word_log'] = temp
    else:
        session_word = {
            'word':request.POST['word'],
            'color':request.POST['color'],
            'bold':'normal',
            'time':strftime('%m/%d/%Y %I:%M %p', localtime())
        }
        temp = request.session['word_log']
        temp.insert(0,session_word)
        request.session['word_log'] = temp
    print(request.session['word_log'])
    return redirect('/')


