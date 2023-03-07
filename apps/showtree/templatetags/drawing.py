from urllib.parse import urlparse

from django import template
from django.template.defaultfilters import stringfilter
from django.urls import reverse_lazy, NoReverseMatch

from showtree.models import Tree, Menu

register = template.Library()


@register.filter
def getUrl(xUrl):
    path = xUrl
    try:
        path = reverse_lazy(xUrl)
    except NoReverseMatch as Err:
        pass
    else:
        return path
    return xUrl


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
    parsResult = urlparse(path)
    if parsResult.netloc:
        return False
    return True


@register.inclusion_tag('showtree/menu.html')
def drawing(childs):
    return {
        'childs': childs
    }