from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<div ><h1>Chatbot apis</h1><p>use /chatbot/api for api and /admin for admin panel</p></div>")