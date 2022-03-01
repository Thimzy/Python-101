from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def welcome(request):
    return HttpResponse("<h1>This is just a simple views</h1>")