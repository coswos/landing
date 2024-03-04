from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "generator/home.html")

def error(request):
    return render(request, 'generator/error.html')


from django.urls import path, re_path

def handler_404(request, exception):
    HttpResponse