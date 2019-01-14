from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    

    return render(request, 'survey.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favlanguage'] = request.POST['favlanguage']
    request.session['comment'] = request.POST['comment']
    request.session.modified = True 
    
    return redirect('/result')

def result(request):

    return render(request, 'result.html')

def back(request):
   
    
    
    return redirect('/')

    
