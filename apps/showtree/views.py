from urllib.parse import urlparse

from django.shortcuts import render

#from .models import Tree

def showtree(request, path='/', *args, **kwargs):
    # parsResult = urlparse(path)
    # print('*********************************')
    # print(path)
    # print(parsResult)

    # try:
    #     menupath = path[1:] if path.startswith('//') else path
    # except KeyError:
    #     menupath = '/'
    # else:
    #     tmp = path.split('/')

    # menupath = path[1:] if path.startswith('//') else path
    # menupath = path[1:] if path.startswith('/') else path


    return render(request, 'showtree/index.html', {'menupath': path})