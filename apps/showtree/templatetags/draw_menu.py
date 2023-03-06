from functools import reduce
from urllib.parse import urlparse

from django import template

from showtree.models import Tree, Menu
from showtree.connection import query_debugger

register = template.Library()

@register.inclusion_tag('showtree/menu.html', takes_context=True)
@query_debugger
def draw_menu(context, menu_name):
    menu = Tree.objects.filter(
       menu__name=menu_name).order_by('parent_id', 'name').values()

    if not len(menu):
        return {'childs': []}

    deepTree = []; 
    allIds = dict();

    menupath = context['menupath']
    menupath = menupath[1:] if menupath[0]=='/' else menupath
    pathElements = menupath.split('/')
    while not len(pathElements):
        pathElements = pathElements[1:]
    
    isRight = False
    selectedElem = None

    allIds = {elem['id']:elem for elem in menu}

    index = 0
    while (item:=menu[index])['parent_id']==None:
        deepTree.append({
            'elem': item,
            'path': item['name'],
            'vector': [len(deepTree)],
        })
        del allIds[item['id']]
        if pathElements and item['name']==pathElements[0]:
            isRight = True
            if len(pathElements)==1:
                selectedElem = deepTree[-1]
                selectedElem['selected'] = True
        index += 1

    if isRight:
        currPath = [0]
        while len(allIds):
            try:
                treeElem = reduce(lambda mas, next: mas['childs'][next],
                    currPath, {'childs':deepTree})
            except IndexError:
                currPath.pop()
                currPath[-1] += 1
            else:
                childs = []
                for item in allIds:
                    if allIds[item]['parent_id']==treeElem['elem']['id']:
                        childs.append(allIds[item])
                if childs:
                    for elem in childs:
                        del allIds[elem['id']]
                    treeElem['childs'] = []
                    for i, child in enumerate(childs):
                        treeElem['childs'].append({
                            'elem': child,
                            'path': treeElem['path'] + '/' + child['name'],
                            'vector': currPath + [i],
                        })
                        if (not selectedElem 
                                and treeElem['childs'][-1]['path']==menupath):
                            selectedElem = treeElem['childs'][-1]
                            selectedElem['selected'] = True
                    currPath = currPath + [0]
                else:
                    currPath[-1] += 1

    if selectedElem is not None:
        try:
            childs = selectedElem['childs']
        except KeyError:
            pass
        else:
            for child in childs:
                try:
                    del child['childs']
                except KeyError:
                    pass

        childs = deepTree
        for elem in selectedElem['vector']:
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

    return {
        'childs': deepTree,
    }