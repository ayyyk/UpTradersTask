from django.shortcuts import render

from .models import Tree

def showtree(request, *args, **kwargs):
    print(kwargs['path'])
    try:
        menupath = '/' + kwargs['path']
    except KeyError:
        menupath = '/'
        top = -1
        upmenu = ''
    else:
        tmp = kwargs['path'].split('/')
        top = len(tmp) - 1
        upmenu = ''.join(tmp[:-1])

    return render(
        request, 
        'showtree/index.html', 
        {
            'menupath': menupath,
            'level': top,
            'upmenu': upmenu
        }
    )