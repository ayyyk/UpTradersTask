from django.contrib import admin

from .models import Tree, Menu

class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'parent', 'name', 'full_name', 'up_elem')
    list_display_links = ('id',)
    #readonly_fields = ('tree', 'link',)
    list_editable = ('name', 'full_name', 'menu', 'parent' )
    # search_fields = ('user',)

admin.site.register(Tree, TreeAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
        
    list_display_links = ('id',)
    list_editable = ('name',)

admin.site.register(Menu, MenuAdmin)