from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(requests):
    return HttpResponse("welcome to my app")
