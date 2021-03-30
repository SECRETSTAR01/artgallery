from django.contrib import admin
from django.urls import path, include
from anoop import views

urlpatterns = [
    path('home', views.homepage, name='homepage' ),
    path('pricing', views.pricing, name ='pricing'),
    path('contact', views.contact, name='contact'),
    path('artwork', views.artwork, name='artwork'),
    path('portrait', views.portrait, name='portrait'),
    path('payment', views.payment, name="payment")
]