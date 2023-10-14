
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import login, authenticate

def index(request):
    context = {"user": request.user}

    return render(request, "sistema/index.html", context)



def login_view(request):

    return render(request, 'sistema/login.html')
