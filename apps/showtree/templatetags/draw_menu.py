from django import template
from django.template.defaultfilters import stringfilter

from showtree.models import Tree, Menu
from showtree.connection import query_debugger

register = template.Library()


@register.filter
def offset(full_name):
    return (len(full_name.split('/'))-1) * 20

@register.filter
def level(full_name):
    return len(full_name.split('/')) - 2


@register.inclusion_tag('showtree/menu.html', takes_context=True)
@query_debugger
def draw_menu(context, menu_name):
    menu = Tree.objects.filter(
       menu__name=menu_name).order_by('full_name').values()
    if any(elem['full_name']==context['menupath'] for elem in menu):
        menupath = context['menupath']
    else:
        menupath = '/'
    return {
        'menu': menu,
        'menupath': menupath,
        'level': context['level'],
        'upmenu': context['upmenu']
    }