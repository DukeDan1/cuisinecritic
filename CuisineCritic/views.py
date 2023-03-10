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

def register(request):
    return render(request, 'CuisineCritic/register.html')

def restaurants(request):
    return render(request, 'CuisineCritic/restaurants.html')

def profile(request):
    return render(request, 'CuisineCritic/profile.html')

def account(request):
    return render(request, 'CuisineCritic/account.html')
