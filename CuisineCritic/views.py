from multiprocessing import AuthenticationError
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
#from rest_framework.decorators import api_view
import json
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_protect 




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

def chineseManorHouse(request):
    return render(request, 'CuisineCritic/chineseManorHouse.html')

def shanghaiShuffle(request):
    return render(request, 'CuisineCritic/shanghaiShuffle.html')

def luckyStar(request):
    return render(request, 'CuisineCritic/luckyStar.html')

def alessi(request):
    return render(request, 'CuisineCritic/alessi.html')

def bombayBanquet(request):
    return render(request, 'CuisineCritic/bombayBanquet.html')

def easternPavilion(request):
    return render(request, 'CuisineCritic/easternPavilion.html')

def topolobamba(request):
    return render(request, 'CuisineCritic/topolobamba.html')

def elPastor(request):
    return render(request, 'CuisineCritic/elPastor.html')

def wahaca(request):
    return render(request, 'CuisineCritic/wahaca.html')

def phucket(request):
    return render(request, 'CuisineCritic/phucket.html')

def kaoSarn(request):
    return render(request, 'CuisineCritic/kaoSarn.html')

def theMangoTree(request):
    return render(request, 'CuisineCritic/theMangoTree.html')

def forgottenPassword(request):
    return render(request, 'CuisineCritic/forgottenPassword.html')


# API:

@csrf_protect 
def api_login(request):
    if request.method == 'POST':                                                                                                                                                                                                           
        login_form = LoginForm(request, request.POST)
        response_data = {}                                                                              
        if login_form.is_valid():                                                                                                           
            response_data['success'] = True
            response_data['message'] = 'Successfully logged in.' 
        else:
            response_data['success'] = False
            response_data['message'] = 'Your username or password is incorrect.'

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
