from django.contrib import admin

from .models import Tree

class TreeAdmin(admin.ModelAdmin):
    list_display = (
        'id','tree_name', 'name', 'full_name', 'up_elem', 'level','offset')
    list_display_links = ('tree_name',)
    #readonly_fields = ('tree', 'link',)
    list_editable = ('name', 'full_name', 'offset',)
    # search_fields = ('user',)

admin.site.register(Tree, TreeAdmin)
