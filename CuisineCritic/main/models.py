from django.db import models
from  django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    avatar_src = models.ImageField(upload_to='users', blank=True, null=True)

class Category(models.Model):
    category_id = models.AutoField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    # image_src = models.ImageField(upload_to='media', blank=True, null=True) Removed for now

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

class RestaurantImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image_src = models.ImageField(upload_to='restaurants')

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=200)
    comment = models.CharField(max_length=2000)
    # likes = models.IntegerField(default=0) Removed for now
    #image_src = models.ImageField(upload_to='reviews', null=True, blank=True) Goodbye for now
