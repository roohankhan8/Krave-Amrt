import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# from math import ceil

# Create your views here.
def index(request):
    my_products = Product.objects.all()
    params = {'product': my_products}
    return render(request, 'index.html', params)
def about(request):
    return render(request, 'about.html')
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
