from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'act_log' not in request.session:
        request.session['act_log'] = []

    return render(request, 'ninja_gold.html')

def get_gold(request):

    if request.POST['button'] == 'farm':
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(1,9)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>Got yourself a good crop this season. you've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(1,9)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Got yourself a good crop this season. you've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'cave':
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(0,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'> Youve found some treasure! Found %s gold!  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(1,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you hear some noises that scare you. you run away like a pansy loosing %s gold (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'loot':
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(2,6)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>Earned %s gold from looting a random person! you might want to re-evaluate your life. (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(2,5)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> The person you tried to mug fights back! serves you right. you loose %s gold (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'casino':
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(10,101)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>Earned %s gold from the casino! lady luck has been kind to you! (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(10,101)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you've lost %s gold from the casino! lady luck, why have you forsaken me! (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    return redirect('/')

def restart_game(request):
    request.session.clear()
    return redirect('/')

    
            
