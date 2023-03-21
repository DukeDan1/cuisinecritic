import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','CuisineCritic.settings')

import django
django.setup()

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
        "Address": "Unknown"
    },
    {
        "Name": "Wahaca",
        "Image name": "mexican-photo-3.jpg",
        "Slug": "wahaca",
        "Category": "Mexican",
        "Address": "Unknown"
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
        "Address": "Unknown"
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



def add_restaurants():
    for x in restaurants:
        c = Category.objects.get_or_create(name=x['Category'])[0]
        c.save()
        
        r = Restaurant.objects.get_or_create(name=x['Name'], address=x['Address'], category=c)[0]
        r.save()

        i = RestaurantImage.objects.get_or_create(image_src=x['Image name'], restaurant=r)[0]
        i.save()

        
add_restaurants()