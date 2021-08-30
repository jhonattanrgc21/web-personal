# Vistas de la app Core
from django.shortcuts import render

def home(request):
    ''' Renderiza a la vista Home '''
    return render(request, 'core/home.html')

def about(request):
    ''' Renderiza a la vista About me '''
    return render(request, 'core/about.html')

def contact(request):
    ''' Renderiza a la vista Contact '''
    return render(request, 'core/contact.html')