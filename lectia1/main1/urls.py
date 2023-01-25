from django.urls import path

from main1 import views

urlpatterns = [
    path('', views.home, name='home')
]