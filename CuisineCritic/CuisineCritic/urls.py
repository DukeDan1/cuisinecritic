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
import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('login/register', views.register, name='login/register'),
    path('login/login', views.login, name='login'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('profile', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('chineseManorHouse', views.chineseManorHouse, name='chineseManorHouse'),
    path('shanghaiShuffle', views.shanghaiShuffle, name='shanghaiShuffle'),
    path('luckyStar', views.luckyStar, name='luckyStar'),
    path('alessi', views.alessi, name='alessi'),
    path('bombayBanquet', views.bombayBanquet, name='bombayBanquet'),
    path('easternPavilion', views.easternPavilion, name='easternPavilion'),
    path('topolobamba', views.topolobamba, name='topolobamba'),
    path('elPastor', views.elPastor, name='elPastor'),
    path('wahaca', views.wahaca, name='wahaca'),
    path('phucket', views.phucket, name='phucket'),
    path('kaoSarn', views.kaoSarn, name='kaoSarn'),
    path('theMangoTree', views.theMangoTree, name='theMangoTree'),
    path('forgottenPassword', views.forgottenPassword, name='forgottenPassword'),
    path('login/forgottenPassword.html', views.forgottenPassword, name='forgottenPassword'),
]
