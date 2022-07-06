
from django.http import JsonResponse
from django.views import View
import requests
import json

from urllib3 import Retry
# from django.http import HttpResponse
from . forms import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Poll
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View
from django.http import JsonResponse


def signupform(request):
    reg = SignupForm()
    if request.method == 'POST':
        reg = SignupForm(request.POST)
        if reg.is_valid():
            new = reg.save()
            login(request, new)
            return redirect('index')
        else:
            return redirect('signupform')
        
    context = {
        'reg': reg
    }

    return render (request,'signup.html', context)

def password(request):
    update = PasswordChangeForm(request.user)
    if request.method == 'POST':
        update = PasswordChangeForm(request.user, request.POST)
        if update.is_valid():
            user=update.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful!')
            return redirect('index')
        else:
            messages.error(request, update.errors)
            return redirect('password')

    context = {
        'update': update
    }

    return render(request, 'password.html', context)


def logoutfunc(request):
    logout(request)
    return redirect('login')

def loginfunc(request):  
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
        
    return render (request, 'login.html')

@login_required(login_url='/login')
def index(request):
    poll = Poll.objects.all()
    
    context={
        'poll': poll
    }

    return render(request, 'index.html', context)

def poll(request):
    poll = Poll.objects.all()
    context={
        'poll': poll
    }

    return render(request, 'poll.html', context)

def profile(request):
    # profile = Poll.objects.all()
    polls = Poll.objects.all().filter(user__username= request.user.username)
    
    context={
        # 'profile': profile,
        'polls': polls
    }

    return render(request, 'profile.html', context)

def save(request):
    user = User.objects.get(username = request.user.username)
    total = 0
    count = Poll.objects.all().filter(user__username= request.user.username)
    for type in count:
        total = total + 1
    if total > 4:
        messages.success(request, 'Maximum number of polls created!')
        return redirect('index')
    else:
        user = User.objects.get(username = request.user.username)
        q = request.POST['question']
        o1 = request.POST['opt1']
        o2 = request.POST['opt2']
        o3 = request.POST['opt3']
        o4 = request.POST['opt4']
        new_poll = Poll()
        if request.method == 'POST':
            new_poll.user = user
            new_poll.question = q
            new_poll.answer1 = o1
            new_poll.answer2 = o2
            new_poll.answer3 = o3
            new_poll.answer4 = o4
            new_poll.save()
            return redirect('index')
        
# def deleteitem(request):
#     itemid=request.POST['itemid']
#     Reservation.objects.filter(pk=itemid).delete()
#     messages.success(request, 'room deleted')
#     return redirect('reservation')


class AxiosView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'axios.html',context)
    
    
class PollView(View):
    def get(self, request, *args, **kwargs):
        new = Poll.objects.all()
        
        context={
            'new':new
        }
        return render(request, 'newpoll.html', context)
    
    
class PollFormView(View):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username= request.user.username)
        content = request.POST.get('content')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        try:
            newpoll = Poll()
            newpoll.user = user
            newpoll.question = content
            newpoll.answer1 = option1
            newpoll.answer2 = option2 
            newpoll.answer3 = option3
            newpoll.answer4 = option4 
            newpoll.save()
            # Poll.objects.create(user=request.user.username, question=content, answer1=option1, answer2=option2, answer3=option3, answer4=option4)
            resp ={
                'status': 'success'
            }
        except Exception as e:
            print(e)
            resp ={
               'status': 'Failed' 
            }
        return JsonResponse(resp)
    
    
# class DelitemView(View):
#     def get(self, request, *args, **kwargs):
#         delitem = Poll.objects.get(pk= )   
#         resp = {
            
#         }
#         return JsonResponse(resp)