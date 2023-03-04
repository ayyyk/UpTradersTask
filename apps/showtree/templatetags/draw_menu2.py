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

    menupath = context['menupath']
    print(menupath)
    menupath = menupath[1:] if menupath[0]=='/' else menupath
    tmp = menupath.split('/')
    pathElements = tmp[1:] if tmp[0]=='' else tmp

    isRight = False
    selectedElem = None
    def isOpenedChilds(selEl, item, pr):
        if selEl is not None:
            print('selEl is not None')
            print(len(pr['vector']), len(selEl['vector']))
            if len(pr['vector'])+1 > len(selEl['vector']):
                prVector = pr['vector']
                selElVector = selEl['vector']
                print(f'{len(prVector)+1} > {len(selElVector)}')
                if all(selEl['vector'][i]==pr['vector'][i] 
                        for i in range(len(selEl['vector']))):
                    return False
        return True

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
            if item['name']==pathElements[0]: 
                isRight = True
                if len(pathElements)==1:
                    selectedElem = deepTree[-1]
        else:
            if not isRight: break
            if isOpenedChilds(selectedElem, item, pr):
                try:
                    seat = pr['childs']
                except KeyError:
                    seat = pr['childs'] = []

                lenSeat = len(seat)
                level = pr['level'] + 1
                seat.append({
                    'elem': item,
                    'num': lenSeat, #len(seat),
                    'path': pr['path'] + '/' + item['name'] ,
                    'level': level, #pr['level'] + 1,
                    'vector': pr['vector'] + [lenSeat], #[len(seat)],
                    'offset': level * 20, #(pr['level'] + 1) * 20,
                })
                dictId[item['id']] = seat[-1]
                print(menupath, seat[-1]['path'])
                if menupath==seat[-1]['path']:
                    selectedElem = seat[-1]

    
    return {
        'menu': deepTree,
        'menupath': menupath,
        'level': context['level'],
        'upmenu': context['upmenu']
    }