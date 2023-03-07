from django.contrib import admin

from .models import Tree, Menu


class TreeAdmin(admin.ModelAdmin):
    empty_value_display = '-top level-'
    list_display = ('menu', 'parent', 'id', 'name', 'url', 'named_url', )
    list_display_links = ('id', 'menu', 'parent')
    list_filter = ('menu',)
    list_editable = ('name', 'url', 'named_url', )
    search_fields = ('name', 'url', 'named_url',)
    #list_per_page = 20

admin.site.register(Tree, TreeAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)

admin.site.register(Menu, MenuAdmin)