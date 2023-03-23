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
    path('login/', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('login/register', views.register, name='login/register'),
    path('login/login', views.login, name='login'),
    path('restaurants', views.restaurant_list, name='restaurants'),
    path('restaurants/', views.restaurant_list, name='restaurants'),
    path('profile', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('forgottenPassword', views.forgottenPassword, name='forgottenPassword'),
     path('login/forgottenPassword.html', views.forgottenPassword, name='forgottenPassword'),
    path('logout', views.logout_page, name='logout'),
    path('delete', views.delete_account, name='delete'),


    # Replaced by automated restaurant pages:
    # path('chineseManorHouse', views.chineseManorHouse, name='chineseManorHouse'),
    # path('shanghaiShuffle', views.shanghaiShuffle, name='shanghaiShuffle'),
    # path('luckyStar', views.luckyStar, name='luckyStar'),
    # path('alessi', views.alessi, name='alessi'),
    # path('bombayBanquet', views.bombayBanquet, name='bombayBanquet'),
    # path('easternPavilion', views.easternPavilion, name='easternPavilion'),
    # path('topolobamba', views.topolobamba, name='topolobamba'),
    # path('elPastor', views.elPastor, name='elPastor'),
    # path('wahaca', views.wahaca, name='wahaca'),
    # path('phucket', views.phucket, name='phucket'),
    # path('kaoSarn', views.kaoSarn, name='kaoSarn'),
    # path('theMangoTree', views.theMangoTree, name='theMangoTree'),


    # Render restaurant
    path('restaurants/<slug:restaurant_slug>', views.render_restaurant, name='show_restaurant'),
    # see all restaurants in category
    path('category', views.redirect_restaurant, name='category_list'),
    path('category/', views.redirect_restaurant, name='category_list'),
    path('category/<slug:category_slug>', views.render_category, name='show_category'),
    
    # API URL endpoints:
    path('api/login', views.api_login, name='api_login'),
    path('api/register', views.api_register, name='api_register'),
    path('api/search', views.api_search, name='api_search'),
    path('api/createRestaurant', views.api_create_restaurant, name='api_create_restaurant'),
    path('api/review', views.api_submit_review, name='api_submit_review'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
