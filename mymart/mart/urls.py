from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Mart'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('checkout/', views.checkout, name='Checkout'),
    path('tracking/', views.tracking, name='Tracking'),
    path('search/', views.search, name='Search'),
    path('product/', views.product, name='Product'),
]