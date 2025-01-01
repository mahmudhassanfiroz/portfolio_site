from django.shortcuts import render, redirect
from portfolio.forms import ContactForm
from portfolio.models import  Project, Service
import json

def home_view(request):
  services = Service.objects.all()
  projects = Project.objects.all()
  context = {
    'services': services,
    'projects': projects
  }
  return render(request, 'index.html', context)


