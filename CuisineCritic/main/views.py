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
from django.db.models import Avg, Q
from .forms import Registration, CreateRestaurant
from django.contrib.auth.forms import UserCreationForm
import random




def index(request):
    return render(request, 'CuisineCritic/index.html', context={})


def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("restaurants"))
    else: return render(request, 'CuisineCritic/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse("index"))
    else: return redirect(reverse("index"))

def register(request):
    if request.user.is_authenticated:
        return redirect("/account")
    return render (request, template_name="CuisineCritic/register.html", context={"profile_form":Registration(), "user_form":UserCreationForm()})

def restaurants(request):
    return render(request, 'CuisineCritic/restaurants.html')

def profile(request):
    return render(request, 'CuisineCritic/profile.html')



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
def render_restaurant(request, restaurant_slug):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_slug)

        # Get all reviews for the restaurant, if any, then select to show randomly
        reviews = Review.objects.filter(restaurant=restaurant)
        n = len(reviews)
        if n > 3: n = 3
        selected_reviews = set()
        while len(selected_reviews) < n:
            selected_reviews.add(random.choice(reviews))

        # Get the average rating for the restaurant
        try:
            average_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 1)
        except:
            average_rating = False
        

        # Get all of the images for this restaurant, if any
        images = RestaurantImage.objects.filter(restaurant=restaurant)

        context_dict = {"restaurant": restaurant, "reviews": selected_reviews, "average_rating": average_rating, 'success': True}
        
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


def restaurant_list(request):
    try:
        categories = Category.objects.all()
        for x in categories:
            x.restaurants = Restaurant.objects.filter(category=x)[:3]
            for y in x.restaurants:
                try:
                    y.image = RestaurantImage.objects.filter(restaurant=y)[0].image_src.url
                except:
                    y.image = "..."

        context_dict = {"categories": categories, 'success': True}
        return render(request, 'CuisineCritic/restaurants.html', context=context_dict)
    except Exception as e:
        print(e)
        return render(request, 'CuisineCritic/restaurants.html', context={'success':False, "reason": "An unknown error occurred"})
    
def render_category(request, category_slug):
    # view all restaurants in a category
    try:
        category = Category.objects.get(slug=category_slug)
        restaurants = Restaurant.objects.filter(category=category)
        
        if len(restaurants) > 0:
            context_dict = {"restaurants": [], "category_name": category.name, 'success': True}
            for x in restaurants:
                context_dict['restaurants'].append({
                    "name": x.name,
                    "slug": x.slug,
                    "image": RestaurantImage.objects.filter(restaurant=x)[0].image_src.url
                })
            
            # turn the array into a 2D array so that we can display 3 restaurants per row.
            # each element in the array will contain up to 3 elements.
            context_dict["restaurants"] = [context_dict["restaurants"][i:i+3] for i in range(0, len(context_dict["restaurants"]), 3)]
            return render(request, 'CuisineCritic/categories.html', context=context_dict)
        else:
            return render(request, 'CuisineCritic/categories.html', context={'success':False, "reason": "There are no restaurants in this category"})
    except Category.DoesNotExist:
        return render(request, 'CuisineCritic/categories.html', context={'success':False, "reason": "This category was not found"})
    except Exception as e:
        print(e)
        return render(request, 'CuisineCritic/categories.html', context={'success':False, "reason": "An unknown error occurred"})

def redirect_restaurant(request):
    return redirect("/restaurants")


def add_restaurant(request):
    if not request.user.is_authenticated:
        return redirect("/restaurants")
    else:
        context_dict = {"restaurant_form": CreateRestaurant()}
        return render(request, 'CuisineCritic/addRestaurant.html', context=context_dict)
        


def account(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        try:
            user = UserProfile.objects.get(user=request.user)
            context_dict = {"user_details": user, 'success': True}
            return render(request, 'CuisineCritic/account.html', context=context_dict)
        except UserProfile.DoesNotExist:
            return render(request, 'CuisineCritic/account.html', context={'success':False, "error": "We were unable to fetch your account. Please try again."})
        except Exception as e:
            print(e)
            return render(request, 'CuisineCritic/account.html', context={'success':False, "error": "An unexpected error has occurred. Please try again."})

def delete_account(request):
    if request.method != "POST":
        return redirect("/account")
    else:
        try:
            if request.POST.get("confirmation") != "true":
                return redirect("/account")
            
            
            profile = UserProfile.objects.get(user=request.user)

            Review.objects.delete(user=profile)

            profile.delete()

            user = User.objects.get(username=request.user.username)
            user.delete()

            return redirect("/logout")
        except UserProfile.DoesNotExist:
            return redirect("/account")
        except Exception as e:
            print(e)
            return redirect("/account")

# API:

@csrf_protect 
def api_login(request):
    if request.method == 'POST':                                                                                                                                                                                                  
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        try:
            # get username from email
            userProfile = UserProfile.objects.get(email=email)
            user = authenticate(username=userProfile.user.username, password=password)
            response_data = {'success':False, 'message': "Your email and password do not match."} 

            if user:                                                             
                if user.is_active:       
                    login(request, user)                                                                                                    
                    response_data['success'] = True
                    response_data['message'] = 'Successfully logged in.' 
                else:
                    response_data['message'] = 'You are not an active user.'
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        except UserProfile.DoesNotExist:
            return HttpResponse(json.dumps({"message": "This email is not registered.", "success":False}), content_type="application/json")
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"message": "An unknown error occurred.", "success":False}), content_type="application/json")



        
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")
    
@csrf_protect
def api_register(request):
    if request.method == "POST":
        try:
            user_form = UserCreationForm(request.POST)
            reg_form = Registration(request.POST)
            response_data = {'success':False, 'message': "The provided information is invalid."} 
            
            if user_form.is_valid() and reg_form.is_valid():
                
                user = user_form.save()
                reg_user = reg_form.save(commit=False)
                reg_user.user = user
                reg_user.save()
                login(request, user)

                response_data['success'] = True
                response_data['message'] = 'You have successfully registered.'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else: 
                if not user_form.is_valid() and user_form.errors:
                    response_data['message'] += " \n\n " + user_form.errors.as_ul()
                if not reg_form.is_valid() and reg_form.errors:
                    response_data['message'] += " \n\n " + reg_form.errors.as_ul()
                
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"message": "An unknown error occurred.", "success":False}), content_type="application/json")
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")

@csrf_protect
def api_search(request):
    if request.method == "POST":
        query = request.POST.get('query')
        if query:
            try:
                category = Category.objects.filter(name__iexact=query)
                
                if len(category) > 0:
                    category = category[0]
                    restaurants = Restaurant.objects.filter(Q(name__icontains=query) | Q(category=category))
                else: restaurants = Restaurant.objects.filter(name__icontains=query)
                

                if restaurants and len(restaurants) > 0:
                    restaurants_array = [{"slug": x.slug, "name":x.name} for x in restaurants[:10]]
                    return HttpResponse(json.dumps({"message": "Search results found.", "success":True, "restaurants": restaurants_array}), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"message": "No search results found.", "success":False}), content_type="application/json")
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps({"message": "An unknown error occurred.", "success":False}), content_type="application/json")
            
        else:
            return HttpResponse(json.dumps({"message": "Please provide a search query.", "success":False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")

@csrf_protect
def api_create_restaurant(request):
    if request.method == "POST":
        try:
            restaurant_form = CreateRestaurant(request.POST)
            response_data = {'success':False, 'message': "The provided information is invalid."}

            if restaurant_form.is_valid():

                restaurant = restaurant_form.save()
                restaurant.save()

                response_data['success'] = True
                response_data['message'] = 'You have successfully created a restaurant.'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                if not restaurant_form.is_valid() and restaurant_form.errors:
                    response_data['message'] += " \n\n " + restaurant_form.errors.as_ul()

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except Exception as e:
            print(e)

            return HttpResponse(json.dumps({"message": "Unable to create restaurant. Please try again.", "success": False}), content_type="application/json")

    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")


@csrf_protect
def api_upload_avatar(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                avatar = request.FILES.get('avatar_src')
                if avatar:
                    user.avatar_src = avatar
                    user.save()
                    return HttpResponse(json.dumps({"message": "Avatar uploaded successfully.", "success": True}), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"message": "Please select an image.", "success": False}), content_type="application/json")
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps({"message": "An unknown error occurred.", "success": False}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "You must be logged in to upload an avatar.", "success": False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")

@csrf_protect
def api_submit_review(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                restaurant = Restaurant.objects.get(restaurant_id=request.POST.get('restaurant'))
                user = UserProfile.objects.get(user=request.user)
                rating = request.POST.get('review-rating')
                title = request.POST.get('review-title')
                comment = request.POST.get('review-comment')

                print(user, rating, title, comment)

                if restaurant and user and rating and title and comment:
                    r = Review(restaurant=restaurant, user=user, rating=rating, title=title, comment=comment)
                    r.save()
                else:
                    return HttpResponse(json.dumps({"message": "Please fill out all fields.", "success": False}), content_type="application/json")
                
                return HttpResponse(json.dumps({"message": "Review submitted successfully.", "success": True}), content_type="application/json")
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps({"message": "Unable to submit review. Please try again.", "success": False}), content_type="application/json")
        else: return HttpResponse(json.dumps({"message": "You must be logged in in order to submit a review.", "success":False}), content_type="application/json")
    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")
       

@csrf_protect
def api_create_restaurant(request):
    if request.method == "POST":
        try:

            restaurant_form = CreateRestaurant(request.POST)

            response_data = {'success':False, 'message': "The provided information is invalid."}

            if restaurant_form.is_valid():
                restaurant_form.save()

                response_data['success'] = True
                response_data['message'] = 'You have successfully created a restaurant.'
                response_data['restaurant_id'] = restaurant_form.instance.restaurant_id
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                if not restaurant_form.is_valid() and restaurant_form.errors:
                    response_data['message'] += " \n\n " + restaurant_form.errors.as_ul()

            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        except Exception as e:
            print(e)

            return HttpResponse(json.dumps({"message": "Unable to create restaurant. Please try again with a different restaurant name.", "success": False}), content_type="application/json")

    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")

@csrf_protect
def api_upload_restaurant_image(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                restaurant = Restaurant.objects.get(restaurant_id=request.POST.get('restaurant_id'))
                image = request.FILES.get('restaurant-image0')
                increment = 0

                if image:
                    while image and increment < 10:
                        r = RestaurantImage(restaurant=restaurant, image_src=image)
                        r.save()
                        increment += 1
                        image = request.FILES.get('restaurant-image'+str(increment))
                    return HttpResponse(json.dumps({"message": "Image(s) uploaded successfully.", "success": True}), content_type="application/json")
                else:
                    restaurant.delete()
                    return HttpResponse(json.dumps({"message": "Please select an image.", "success": False}), content_type="application/json")
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps({"message": "An unknown error occurred.", "success": False}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "You must be logged in to upload an image.", "success": False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")


@csrf_protect
def api_change_password(request):
    if request.method == "POST":
        # get data
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('password2')

        # check if user is logged in
        if request.user.is_authenticated:
            # check if passwords match
            if new_password == confirm_password:
                # check if old password is correct
                if request.user.check_password(old_password):
                    # change password
                    request.user.set_password(new_password)
                    request.user.save()
                    return HttpResponse(json.dumps({"message": "Password changed successfully.", "success":True}), content_type="application/json")
                else: return HttpResponse(json.dumps({"message": "The old password you provided is incorrect.", "success":False}), content_type="application/json")
            else: return HttpResponse(json.dumps({"message": "The new passwords you provided do not match.", "success":False}), content_type="application/json")
        else: return HttpResponse(json.dumps({"message": "You must be logged in in order to change your password.", "success":False}), content_type="application/json")

    else: return HttpResponse(json.dumps({"message": "This endpoint only accepts POST requests.", "success":False}), content_type="application/json")
