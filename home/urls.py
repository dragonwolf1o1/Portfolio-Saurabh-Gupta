from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name="home" ),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contactus',views.contactus,name='contactus')
]
