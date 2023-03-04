from django import template
from django.template.defaultfilters import stringfilter

from showtree.models import Tree, Menu

register = template.Library()

@register.inclusion_tag('showtree/drawing.html') #, takes_context=True)
def drawing(elems):
    return {
        'elems': elems
    }