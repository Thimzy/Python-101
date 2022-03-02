from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("""<h1>This is just a simple view</h1>
                        <br>
                        <h2>Testing this guy</h2>""")

def hello(request):
    return HttpResponse("""<h1>This is a new app</h1>
                        <br>
                        <h2>Testing this guy</h2>""")

def back(request):
    return HttpResponse("""<h1>This is my latest app</h1>
                        <br>
                        <h2>Testing this guy</h2>""")

def war(request):
    return HttpResponse("""<h1>Russia Ukraine we one united we stand</h1>
                        <br>
                        <h2>Testing this guy</h2>""")

def timzy(request):
    return HttpResponse("""<h1>God create heaven and earth</h1>
                        <br>
                        <h2>Testing this guy</h2>""")