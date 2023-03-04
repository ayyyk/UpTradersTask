import pprint

from django import template
from django.template.defaultfilters import stringfilter

from showtree.models import Tree, Menu
from showtree.connection import query_debugger

register = template.Library()


@register.inclusion_tag('showtree/menu2.html', takes_context=True)
@query_debugger
def draw_menu2(context, menu_name):
    menu = Tree.objects.filter(
       menu__name=menu_name).order_by('parent_id', 'name').values()

    i = 0
    deepTree = []
    dictId = dict()
    for item in menu:
        try:
            pr = dictId[item['parent_id']]
        except KeyError:
            deepTree.append({
                'elem': item,
                'num': len(deepTree),
                'path': item['name'],
                'level': 0,
                'vector': [len(deepTree)],
                'offset': 0,
            })
            dictId[item['id']] = deepTree[-1]
        else:
            try:
                seat = pr['childs']
            except KeyError:
                seat = pr['childs'] = []
            seat.append({
                'elem': item,
                'num': len(seat),
                'path': pr['path'] + '/' + item['name'] ,
                'level': pr['level'] + 1,
                'vector': pr['vector'] + [len(seat)],
                'offset': (pr['level'] + 1) * 20,
            })
            dictId[item['id']] = seat[-1]

    return {
        'menu': deepTree,
        'menupath': context['menupath'],
        'level': context['level'],
        'upmenu': context['upmenu']
    }


    # while menu[i]['parent_id'] is None:
    #     deepTree.append({
    #         'elem': menu[i],
    #         'num': i,
    #         'path': menu[i]['name'],
    #         'level': 0,
    #         'vector': [i],
    #         'offset': 0,
    #     })
    #     dictId[menu[i]['id']] = deepTree[-1]
    #     i += 1

    # for k in range(i, len(menu)):
    #     pr = dictId[menu[k]['parent_id']]
    #     try:
    #         seat = pr['childs']
    #     except KeyError:
    #         seat = pr['childs'] = []
    #     seat.append({
    #         'elem': menu[k],
    #         'num': len(seat),
    #         'path': pr['path'] + '/' + menu[k]['name'] ,
    #         'level': pr['level'] + 1,
    #         'vector': pr['vector'] + [len(seat)],
    #         'offset': (pr['level'] + 1) * 20,
    #     })

    #     dictId[menu[k]['id']] = seat[-1]