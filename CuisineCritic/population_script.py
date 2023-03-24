import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','CuisineCritic.settings')

import django
django.setup()
from django.contrib.auth.forms import UserCreationForm
from main.forms import Registration
import random

from main.models import *

restaurants = [
    {
        "Name": "Topolobamba",
        "Image name": "mexican-photo-1.jpg",
        "Slug": "topolobamba",
        "Category": "Mexican",
        "Address": "60 Mariia Drive, Glasgow, G10 8KM"
    },
    {
        "Name": "El Pastor",
        "Image name": "mexican-photo-2.jpg",
        "Slug": "elPastor",
        "Category": "Mexican",
        "Address": "2 Havana Street, Glasgow, G4 9JH"
    },
    {
        "Name": "Wahaca",
        "Image name": "mexican-photo-3.jpg",
        "Slug": "wahaca",
        "Category": "Mexican",
        "Address": "3 University Avenue, Glasgow, G12 8AA"
    },
    {
        "Name": "Mexican Manor House",
        "Image name": "mexican-photo-4.jpg",
        "Slug": "mexicanManorHouse",
        "Category": "Mexican",
        "Address": "5 Woodburn Road, Glasgow, G13 9JD"
    },
    {
        "Name": "Chinese Manor House",
        "Image name": "chinese-photo-1.jpg",
        "Slug": "chineseManorHouse",
        "Category": "Chinese",
        "Address": "5 Woodburn Road, Glasgow, G13 9JD"
    },
    {
        "Name": "Lucky Star",
        "Image name": "chinese-photo-2.jpg",
        "Slug": "luckyStar",
        "Category": "Chinese",
        "Address": "16A Hyndland Crescent, Glasgow, G11 6ND"
    },
    {
        "Name": "Shanghai Shuffle",
        "Image name": "chinese-photo-3.jpg",
        "Slug": "shanghaiShuffle",
        "Category": "Chinese",
        "Address": "8 Patrick Street, Glasgow, G14 8BS"
    },
    {
        "Name": "Alessi",
        "Image name": "indian-photo-1.jpg",
        "Slug": "alessi",
        "Category": "Indian",
        "Address": "20 Brickway Lane, Glasgow, G11 027"
    },
    {
        "Name": "Bombay Banquet",
        "Image name": "indian-photo-2.jpg",
        "Slug": "bombayBanquet",
        "Category": "Indian",
        "Address": "4 Elaine Avenue, Glasgow, G90 8HA"
    },
    {
        "Name": "Eastern Pavilion",
        "Image name": "indian-photo-3.jpg",
        "Slug": "easternPavilion",
        "Category": "Indian",
        "Address": "31 Cumbernauld Road, Glasgow, G06 8PS"
    },
    {
        "Name": "Phucket",
        "Image name": "thai-photo-1.jpg",
        "Slug": "phucket",
        "Category": "Thai",
        "Address": "16 Craigs Road, Glasgow, G12 7JD"
    },
    {
        "Name": "Kao Sarn",
        "Image name": "thai-photo-2.jpg",
        "Slug": "kaoSarn",
        "Category": "Thai",
        "Address": "15 Molema Circus, Glasgow, G9 3DC"
    },
    {
        "Name": "The Mango Tree",
        "Image name": "thai-photo-3.jpg",
        "Slug": "theMangoTree",
        "Category": "Thai",
        "Address": "56 Balmoral Drive, Glasgow, G12 8JH"
    },    {
        "Name": "Chinese Manor House",
        "Image name": "chinese-photo-1.jpg",
        "Slug": "chineseManorHouse",
        "Category": "Chinese",
        "Address": "5 Woodburn Road, Glasgow, G13 9JD"
    },
    {
        "Name": "Shanghai Shuffle",
        "Image name": "chinese-photo-2.jpg",
        "Slug": "shanghaiShuffle",
        "Category": "Chinese",
        "Address": "8 Patrick Street, Glasgow, G14 8BS"
    },
    {
        "Name": "Lucky Star",
        "Image name": "chinese-photo-3.jpg",
        "Slug": "luckyStar",
        "Category": "Chinese",
        "Address": "16A Hyndland Crescent, Glasgow, G11 6ND"
    }
]

# (generated by AI, except last row)
users = [
    {"username": "user1", "email": "user1@example.com", "password": "P@ssw0rd1234", "name": "Alice Smith"},
    {"username": "user2", "email": "user2@example.com", "password": "Str0ngP@ssword", "name": "Bob Johnson"},
    {"username": "user3", "email": "user3@example.com", "password": "P@ssw0rd5678", "name": "Charlie Brown"},
    {"username": "user4", "email": "user4@example.com", "password": "MyPa$$word1234", "name": "Dave Jones"},
    {"username": "user5", "email": "user5@example.com", "password": "P@ssw0rd9012", "name": "Eve Johnson"},
    {"username": "user6", "email": "user6@example.com", "password": "S3cur3P@ssword", "name": "Frank Smith"},
    {"username": "user7", "email": "user7@example.com", "password": "P@ssw0rd3456", "name": "Grace Lee"},
    {"username": "user8", "email": "user8@example.com", "password": "C0mpl3xP@ssword", "name": "Henry Chen"},
    {"username": "user9", "email": "user9@example.com", "password": "P@ssw0rd7890", "name": "Isabel Kim"},
    {"username": "user10", "email": "user10@example.com", "password": "MyS3cur3P@ss", "name": "John Smith"},
    {"username": "DukeDan1", "email": "daniel.shields@hotmail.co.uk", "password": "12345678WW", "name": "Daniel Shields"}
]

# (generated by AI:)
reviews = [
    {"rating": 4.5, "title": "Great food and service!", "comment": "I had a wonderful dining experience at this restaurant. The food was delicious and the service was excellent."},
    {"rating": 3.0, "title": "Average food, slow service", "comment": "The food was okay, but it took a long time to receive our order. The service could definitely be improved."},
    {"rating": 5.0, "title": "Amazing ambiance and food", "comment": "This restaurant has a great atmosphere and the food was absolutely delicious. I highly recommend it!"},
    {"rating": 2.5, "title": "Disappointing experience", "comment": "I had high hopes for this restaurant, but the food was mediocre and the service was lacking."},
    {"rating": 4.0, "title": "Good food and friendly staff", "comment": "The food was good and the staff were very friendly. I would definitely come back again."},
    {"rating": 1.5, "title": "Terrible experience", "comment": "I had a terrible dining experience at this restaurant. The food was cold and the service was rude."},
    {"rating": 3.5, "title": "Decent food, but noisy atmosphere", "comment": "The food was decent, but the atmosphere was very noisy and it was difficult to have a conversation."},
    {"rating": 4.5, "title": "Great place for brunch", "comment": "This restaurant is a great spot for brunch. The food was delicious and the atmosphere was lively."},
    {"rating": 3.0, "title": "Okay food, but overpriced", "comment": "The food was okay, but I felt that it was overpriced for what we received."},
    {"rating": 4.0, "title": "Excellent service and drinks", "comment": "The service was excellent and the drinks were delicious. I would definitely recommend this restaurant for a night out."},
    {"rating": 4.0, "title": "Great dinner spot", "comment": "This restaurant is a great spot for a nice dinner. The food was delicious and the service was attentive."},
    {"rating": 3.5, "title": "Decent food, slow service", "comment": "The food was okay, but it took a while for our order to come out. The server was friendly, but not very attentive."},
    {"rating": 5.0, "title": "Absolutely incredible!", "comment": "This restaurant was an amazing experience from start to finish. The food was exceptional and the service was top-notch."},
    {"rating": 2.0, "title": "Disappointing meal", "comment": "Unfortunately, the food at this restaurant did not meet our expectations. The flavors were off and the portions were small."},
    {"rating": 4.5, "title": "Great brunch with friends", "comment": "I had a fantastic time brunching with friends at this restaurant. The food and drinks were delicious and the atmosphere was lively."}
]




def add_restaurants():
    for x in restaurants:
        try:
            c = Category.objects.get_or_create(name=x['Category'])[0]
            c.save()
            
            r = Restaurant.objects.get_or_create(name=x['Name'], address=x['Address'], category=c)[0]
            r.save()

            i = RestaurantImage.objects.get_or_create(image_src=x['Image name'], restaurant=r)[0]
            i.save()
        except Exception as e:
            print("Receiving error: ", e)
            # raise e

    # test multiple images per restaurant
    r = Restaurant.objects.get(slug__icontains="phucket")
    i = RestaurantImage.objects.get_or_create(image_src="phucket2.jpg", restaurant=r)[0]
    i.save()
    i = RestaurantImage.objects.get_or_create(image_src="phucket3.jpg", restaurant=r)[0]
    i.save()


def add_users():
    for x in users:
        
        x["password1"] = x["password"]
        x["password2"] = x["password"]

        try:
            user_form = UserCreationForm(data=x)
            reg_form = Registration(data=x)

            user_form.save()
            reg_form.save()
        except Exception as e:
            print("Receiving error: ", e)
            print("If you have already created the test users, this is expected.")
            print("Otherwise, please add 'raise e' after line 203 in CuisineCritic/populate.py to see the full error message.", end="\n\n")
            # raise e



def add_reviews():
    for x in restaurants:
        random_reviews = [random.choice(reviews) for x in range(3)]
        for y in random_reviews:
            user = UserProfile.objects.get(email=random.choice(users)["email"])
            r = Review.objects.get_or_create(rating=y["rating"], title=y["title"], comment=y["comment"], restaurant=Restaurant.objects.get(name=x["Name"]), user=user)[0]
            r.save()


        
add_restaurants()
add_users()
add_reviews()   