from django.urls import path
from django.shortcuts import render

def foother(request):
    return render(request, 'base.html')