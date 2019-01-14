from django.shortcuts import render
from time import strftime, localtime

def time(request):
    time_d={
        'time': strftime('%I:%M %p', localtime()),
        'date': strftime('%A %B %d'),
    }

    return render(request,'time.html', time_d)
