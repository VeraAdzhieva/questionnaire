from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет привет")

def hello(request):
    return HttpResponse("Привет 12345")
