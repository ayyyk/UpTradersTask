from django import template

from showtree.models import Tree

register = template.Library()

@register.simple_tag
def draw_menu(format_string):
    menu = Tree.objects.filter()
    return datetime.datetime.now().strftime(format_string)