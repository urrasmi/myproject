from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Welcome to My project</h1>")