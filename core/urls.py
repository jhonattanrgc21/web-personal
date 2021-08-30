# URLs de la app Core
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about-me'),
    path('contact/', views.contact, name='contact'),
]