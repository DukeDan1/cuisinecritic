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
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Avg




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


# Render the restaurant view by querying the database and showing the correct restaurant
def render_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_id)

        # Get all reviews for the restaurant, if any
        reviews = Review.objects.filter(restaurant=restaurant)

        # Get the average rating for the restaurant
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        print(average_rating)

        # Get all of the images for this restaurant, if any
        images = RestaurantImage.objects.filter(restaurant=restaurant)

        context_dict = {"restaurant": restaurant, "reviews": reviews[:3], "average_rating": average_rating, 'success': True}
        
        context_dict["images"] = []

        for x in images:
            context_dict["images"].append(x.image_src.url)

        return render(request, 'CuisineCritic/base_restaurant.html', context=context_dict)
    except Restaurant.DoesNotExist:
        # request some cool restaurants to show in a list
        restaurants = Restaurant.objects.all()
        return render(request, 'CuisineCritic/base_restaurant.html', context={'success':False, "reason": "This restaurant was not found", "list_of_restaurants": restaurants[:5]})
    except Exception as e:
        print(e)
        return render(request, 'CuisineCritic/base_restaurant.html', context={'success':False, "reason": "An unknown error occurred"})




# API:

@csrf_protect 
def api_login(request):
    if request.method == 'POST':                                                                                                                                                                                                           
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        response_data = {'success':False, 'message': "Your email and password do not match."} 

        if user:                                                                   
            if user.is_active:       
                login(request, user)                                                                                                    
                response_data['success'] = True
                response_data['message'] = 'Successfully logged in.' 
            else:
                response_data['success'] = False
                response_data['message'] = 'You are not an active user.'
        

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")
    
@csrf_protect
def api_register(request):
    if request.method == "POST":
        pass
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")
    

@csrf_protect
def api_search(request):
    pass

@csrf_protect
def api_create_restaurant(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        category = request.POST.get('category')

        # get images


        try:
            r = Restaurant(name=name, address=address, category=category)
            r.save()
            return HttpResponse(json.dumps({"message": "Restaurant created successfully.", "success": True}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"message": "Unable to create restaurant. Please try again.", "success": False}), content_type="application/json")

        
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")

def api_submit_review(request):
    pass