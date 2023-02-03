from django.contrib import admin
from main1 import views
from django.urls import path

from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    url('/contacts/', views.contacte, name='contacts'),
    url('/currency/', views.currency, name='currency'),
    url('/show_messages/', views.show_messages, name='show_messages'),
    url('/services/', views.services, name='services'),
    url('/currency_stat/', views.currency_stat, name='currency_stat'),
    
    
]