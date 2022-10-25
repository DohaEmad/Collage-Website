from contextlib import _RedirectStream, redirect_stderr
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from . models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.template import RequestContext
from django.contrib import messages

# Create your views here.

def login (request):
    if request.method=='POST':
        username=request.POST.get('user')
        print(username)
        password=request.POST.get('passwordd')
        print(password)
        for x in Users.objects.iterator():
            print(x.username)
            print(x.passwordd)
            if x.username == username and x.passwordd == password:
                return render(request, 'pages/home_page.html')

    return render(request,'pages/login_page.html')

    





        

