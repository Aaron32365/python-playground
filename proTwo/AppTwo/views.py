from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def  help(request):
    info = {"template1": "Help Template"}
    return render(request,"proTwo/index.html",context=info)

def  index(request):
    info = {"template1": "this is the index page"}
    return render(request,"proTwo/index.html",context=info)
