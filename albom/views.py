from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def homeView(request):
    return render(request, 'index.html')

from .models import Albom

def showAlbomView(request, name, *args, **wargs):
    context = Albom.objects.filter(name=name)
    
    print(context.first())

    return render(request, 'index.html', {'context': context.first(),})