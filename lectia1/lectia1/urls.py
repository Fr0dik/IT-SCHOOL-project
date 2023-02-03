from django.conf.urls import url
from django.contrib import admin
from main1 import views
from django.urls import path, include





urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('main1.urls')),   

]