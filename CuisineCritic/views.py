from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    return render(request, 'CuisineCritic/index.html', context={})

def login(request):
    return render(request, 'CuisineCritic/login.html')
