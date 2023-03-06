from django.contrib import admin

from .models import Tree, Menu


class TreeAdmin(admin.ModelAdmin):
    # settings for common displaing
    empty_value_display = '-up level-'
    list_display = ('menu', 'parent', 'id', 'name', 'url', 'named_url', )
    list_display_links = ('id', 'menu', 'parent')
    list_filter = ('menu',)
    list_editable = ('name', 'url', 'named_url', )
    search_fields = ('name', 'url', 'named_url',)
    #list_per_page = 20

    # @admin.display(description='parent')
    # def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.first_name, obj.last_name)).upper()


admin.site.register(Tree, TreeAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)

admin.site.register(Menu, MenuAdmin)