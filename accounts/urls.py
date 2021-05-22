from django.contrib import admin
from django.contrib.auth import login
from django.urls import path,include
from accounts import views

urlpatterns = [
    path("login/",views.login),
    path("result/",views.result),
    path("home",views.index,name='home'),
    path("",views.login,name='login'),
    path("rooms",views.rooms,name='rooms'),
    path("services",views.services,name='services'),
    path("contact/",views.contact,name='contact'),
    path("preferences/",views.preferences),
]