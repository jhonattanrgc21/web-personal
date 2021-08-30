# Vistas de la app Portfolio
from django.shortcuts import render
from .models import Project

def portfolio(request):
    ''' Obtiene una lista con todos los proyectos
        registrados en la BD y los renderiza a la
        vista portfolio.html '''
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})