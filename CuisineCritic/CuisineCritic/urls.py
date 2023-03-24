"""CuisineCritic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('restaurants', views.restaurant_list, name='restaurants'),
    path('restaurants/', views.restaurant_list, name='restaurants'),
    path('profile', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('logout', views.logout_page, name='logout'),
    path('delete', views.delete_account, name='delete'),



    # Render restaurant
    path('restaurants/<slug:restaurant_slug>', views.render_restaurant, name='show_restaurant'),
    # see all restaurants in category
    path('category', views.redirect_restaurant, name='category_list'),
    path('category/', views.redirect_restaurant, name='category_list'),
    path('category/<slug:category_slug>', views.render_category, name='show_category'),

    # Add restaurant form
    path('add-restaurant', views.add_restaurant, name='add_restaurant'),
    
    # API URL endpoints:
    path('api/login', views.api_login, name='api_login'),
    path('api/register', views.api_register, name='api_register'),
    path('api/search', views.api_search, name='api_search'),
    path('api/create_restaurant', views.api_create_restaurant, name='api_create_restaurant'),
    path('api/upload_restaurant_image', views.api_upload_restaurant_image, name='api_upload_restaurant_image'),
    path('api/review', views.api_submit_review, name='api_submit_review'),
    path('api/upload_avatar', views.api_upload_avatar, name='api_upload_avatar'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
