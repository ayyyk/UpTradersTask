from urllib.parse import urlparse

from django import template
from django.template.defaultfilters import stringfilter

from showtree.models import Tree, Menu

register = template.Library()


@register.filter
def isSelected(elem):
    try:
        elem['selected']
    except KeyError:
        return "#1C2841;"
    else:
        return "red;"


@register.filter
def isInnerPath(path):
    #print(path, '********************************')
    parsResult = urlparse(path)
    if parsResult.netloc:
        return False
    return True



@register.inclusion_tag('showtree/menu.html')
def drawing(childs):
    return {
        'childs': childs
    }