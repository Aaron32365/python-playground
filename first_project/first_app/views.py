# imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# every view must return an object
def index(request):
    return HttpResponse("Hello world!")