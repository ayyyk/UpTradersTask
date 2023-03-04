from django import template

from showtree.models import Tree, Menu
from showtree.connection import query_debugger

register = template.Library()

@register.inclusion_tag('showtree/menu2.html', takes_context=True)
@query_debugger
def draw_menu2(context, menu_name):
    menu = Tree.objects.filter(
       menu__name=menu_name).order_by('parent_id', 'name').values()

    deepTree = []; dictId = dict(); badIds = set()

    menupath = context['menupath']
    menupath = menupath[1:] if menupath[0]=='/' else menupath
    tmp = menupath.split('/')
    pathElements = tmp[1:] if tmp[0]=='' else tmp

    isRight = False
    selectedElem = None
    def isOpenedChilds(selEl, item, pr):
        if selEl is None: return True

        selElVector = selEl['vector']
        try:
            itemVector = pr['vector'] + [len(pr['childs'])]
        except KeyError:
            itemVector = pr['vector'] + [0]

        if (itemVector[:len(selElVector)]==selElVector and 
                len(itemVector)>len(selElVector)+1):
            return False
        return True

    #print(f'\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    for item in menu:
        #print(f'\n+++++++++++++++++++++++++++++++++++++')
        #print(f'{item=}')
        try:
            pr = dictId[item['parent_id']]
        except KeyError:
            if item['parent_id'] in badIds:
                badIds.add(item['id'])
            else:
                #print('except KeyError:')
                deepTree.append({
                    'elem': item,
                    'path': item['name'],
                    'vector': [len(deepTree)],
                    'offset': 0,
                })
                dictId[item['id']] = deepTree[-1]

                if pathElements and item['name']==pathElements[0]:
                    isRight = True
                    if len(pathElements)==1:
                        selectedElem = deepTree[-1]
                        selectedElem['selected'] = True
                #print(f'{selectedElem=}')
                #print(dictId.keys())
        else:
            if not isRight: break
            #print(f'11{selectedElem=}')
            if isOpenedChilds(selectedElem, item, pr):
                try:
                    seat = pr['childs']
                except KeyError:
                    seat = pr['childs'] = []

                seat.append({
                    'elem': item,
                    'path': pr['path'] + '/' + item['name'] ,
                    'vector': pr['vector'] + [len(seat)],
                    'offset': pr['offset'] + 20, 
                })
                dictId[item['id']] = seat[-1]
                #print(menupath, seat[-1]['path'])
                if menupath==seat[-1]['path']:
                    selectedElem = seat[-1]
                    selectedElem['selected'] = True
            else:
                badIds.add(item['id'])

    if selectedElem is not None:
        childs = deepTree
        for elem in selectedElem['vector']:
            #print(f'{elem=}')
            for index in range(elem+1, len(childs)):
                try:
                    del childs[index]['childs']
                except KeyError:
                    pass
            try:        
                childs = childs[elem]['childs']
            except KeyError:
                pass
    else:
        for elem in deepTree:
            try:
                del elem['childs']
            except KeyError:
                pass

    return {'menu': deepTree}