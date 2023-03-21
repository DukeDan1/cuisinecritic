from django.db import models
from  django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    avatar_src = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Category(models.Model):
    category_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    image_src = models.ImageField(upload_to='media/categories')

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class RestaurantImage(models.Model):
    image_id = models.CharField(max_length=50, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image_src = models.ImageField(upload_to='media/restaurants')

class Review(models.Model):
    review_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=200)
    comment = models.CharField(max_length=2000)
    likes = models.IntegerField()
    image_src = models.ImageField(upload_to='media/reviews', null=True, blank=True)
