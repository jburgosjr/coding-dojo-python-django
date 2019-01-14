from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    
    if 'u_id' not in request.session:
        request.session['u_id'] = 0

    return render(request, 'login.html')

def reg_validate(request):
    check = User.objects.filter(email = request.POST['email'])
    error = False

    if len(request.POST['first_name'])< 2:
        messages.error(request,'First Name must be longer than 1 character', extra_tags = 'fn_error' )
        error = True

    if not NAME_REGEX.match(request.POST['first_name']):
        messages.error(request,'Name Field must ONLY contain Alpha characters', extra_tags = 'fn_error')
        error = True

    if not NAME_REGEX.match(request.POST['last_name']):
        messages.error(request,'Name Field must ONLY contain Alpha characters', extra_tags = 'ln_error')
        error = True

    if len(request.POST['last_name'])< 2:
        messages.error(request,'Last Name must be longer than 1 character', extra_tags = 'ln_error')
        error = True

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Email is in an invalid format', extra_tags = 'email_error')
        error = True

    if check:
        messages.error(request,'Email has already been registered', extra_tags = 'email_error')
        error = True

    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request,'Passwords do not match', extra_tags = 'pw_error')
        error = True

    if len(request.POST['password']) < 8 :
        messages.error(request,'Password must be 8 or more characters long', extra_tags = 'pw_error')

    if error == True:
        return redirect('/')

    elif error == False:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        decoded_hash = hashed.decode('utf-8')

        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = decoded_hash)

        messages.success(request, 'You have registered succesfully. You may now login', extra_tags = 'registered')
        
        return redirect('/')

def login_validate(request):
    error = False
    echeck = User.objects.filter(email=request.POST['email'])

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
        error = True
    
    else:
        if echeck:
            if echeck[0].email == request.POST['email']:
                if bcrypt.checkpw(request.POST['password'].encode(),echeck[0].password.encode()):
                    request.session['login'] = True
                    request.session['u_id'] = echeck[0].id
                    
                else:
                    messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
                    error = True
            else:
                messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
                error = True
        else:
            messages.error(request,'Invalid Credentials', extra_tags = 'log_error')
            error = True

    

    if error == True:
        return redirect('/')
    elif error == False:
        return redirect('/home')

def home(request):
    if request.session['u_id'] == True:
        home = {
            'user':User.objects.get(id=request.session['u_id']),
            'reviews':Review.objects.all().reverse()
        }

        return render(request, 'home.html', home)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    if request.session['u_id'] == True:
        author_info={
            'authors':Author.objects.all()
        }
        return render(request, 'add_book.html', author_info)
    else:
        return redirect('/')

def add_process(request):
    if request.POST['author'] == 'False':
        u = User.objects.get(id=request.session['u_id'])
        a=Author.objects.create(first_name = request.POST['na_fn'], last_name = request.POST['na_ln'])
        b=Book.objects.create(title = request.POST['title'], author = a, uploader = u)
        Review.objects.create(comment = request.POST['review'], rating = request.POST['rating'], reviewer = u, book = b)
        return redirect('/book/%s' %(b.id))
    else:
        u = User.objects.get(id=request.session['u_id'])
        a = Author.objects.get(id=request.POST['author'])
        b = Book.objects.create(title = request.POST['title'], author = a, uploader = u)
        Review.objects.create(comment = request.POST['review'], rating = request.POST['rating'], reviewer = u, book = b)
        return redirect('/book/%s' %(b.id))

def book_info(request,id):
    if request.session['u_id'] ==True:
        book_info={
            'books':Book.objects.get(id=id)
        }
        return render(request, 'book.html', book_info)

    else:
        return redirect('/')


        
