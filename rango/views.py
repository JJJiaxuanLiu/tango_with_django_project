from django.shortcuts import render

from django.http import HttpResponse

def index(requset):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a herf='/rango/'>Index</a>")
