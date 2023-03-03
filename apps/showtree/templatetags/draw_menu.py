from django import template

from showtree.models import Tree

register = template.Library()

@register.inclusion_tag('showtree/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Tree.objects.filter(
        menu__name=menu_name).order_by('full_name').values()
    return {
        'menu': menu,
        'menupath': context['menupath'],
        'level': context['level'],
        'upmenu': context['upmenu']
    }