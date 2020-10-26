"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from blog import views

urlpatterns = [
    path('', views.first,name="first"),
    path('academyfirst/', views.academyfirst,name="academyfirst"),
    path('exhibition/', views.exhibition,name="exhibition"),
    path('login/', views.login,name="login"),
    path('studentforth/', views.studentforth,name="studentforth"),
    path('studentsecond/', views.studentsecond,name="studentsecond"),
    path('studentthird/', views.studentthird,name="studentthird"),
    path('video/', views.video,name="video"),
    path('logintest$', views.logintest,name="logintest"),
]
