from urllib.parse import urlparse

from django.shortcuts import render

#from .models import Tree

def showtree(request, path='/', *args, **kwargs):


    return render(request, 'showtree/index.html', {'menupath': path})