from django.shortcuts import render
from .models import Project

# Create your views here.
projects = Project.objects.all()
def portfolio(request):
    return render(request, 'portfolio/portfolio.html', {'projects': projects})