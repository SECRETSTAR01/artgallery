from django.contrib import admin
from django.urls import path, include
from anoop import views

urlpatterns = [
    path('home', views.menu, name='menu' ),
    path('pricing', views.pricing, name ='pricing'),
    path('contact', views.contact, name='contact'),
    path('artwork', views.artwork, name='artwork'),
]