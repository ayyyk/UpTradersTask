from django.contrib import admin

from .models import Tree

class TreeAdmin(admin.ModelAdmin):
    list_display = ('id','tree_name', 'name', 'full_name', 'up_elem')
    #readonly_fields = ('tree', 'link',)
    # list_editable = ('update',)
    # search_fields = ('user',)

admin.site.register(Tree, TreeAdmin)
