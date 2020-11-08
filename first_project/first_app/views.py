# imports
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# every view must return an object
def index(request):
    my_dict = {'insert_me': 'Hello I am from templates/first_app/views.py'}
    return render(request,'first_app/index.html', context = my_dict)