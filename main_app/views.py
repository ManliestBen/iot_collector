from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    return render(request, 'projects/index.html')

def about(request):
    return render(request, 'about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', { 'projects': projects })
# Create your views here.
