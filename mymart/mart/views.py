import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse('Hello about')
def contact(request):
    return HttpResponse('Hello contact')
def product(request):
    return HttpResponse('Hello product')
def checkout(request):
    return HttpResponse('Hello checkout')
def tracking(request):
    return HttpResponse('Hello tracking')
def search(request):
    return HttpResponse('Hello search')
