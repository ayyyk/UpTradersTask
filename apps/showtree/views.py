from django.shortcuts import render

from .models import Tree

def showtree(request, *args, **kwargs): #, action):
    menu = Tree.objects.all().values()
    if 'path' in kwargs:
        print(kwargs['path'])
        mehupath = '/' + kwargs['path']
        tmp = kwargs['path'].split('/')
        top = len(tmp) - 1
        upmenu = ''.join(tmp[:-1])
        print(upmenu)
    else:
        mehupath = ''
        top = -1
        upmenu = ''
    return render(
        request, 
        'showtree/index.html', 
        {
            'menu': menu,
            'mehupath': mehupath,
            'level': top,
            'upmenu': upmenu
        }
    )