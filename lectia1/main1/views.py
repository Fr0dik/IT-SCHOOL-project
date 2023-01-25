from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def testing(request):
  template = loader.get_template('home.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))  

def home(request):
    return render(request, 'main1/home.html', {'varsta': 28, 'nume': 'Madalin'})
