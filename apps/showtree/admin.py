from django.contrib import admin

from .models import Tree, Menu

class BottomItem(admin.TabularInline):
    model = Tree

    class Meta:
        verbose_name = 'Down Items'

class TreeAdmin(admin.ModelAdmin):
    # settings for common displaing
    #empty_value_display = '-empty-'
    list_display = ('id', 'name', 'link', 'menu', 'parent')
    list_display_links = ('id', 'name', 'link')
    
    #list_editable = ('name', 'link', 'menu', 'parent' )
    #search_fields = ('menu',)
    list_per_page = 20
    list_filter = ('menu', )
    inlines = [BottomItem]
    save_on_top = True
    #fields = list_display

    # @admin.display(description='parent')
    # def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.first_name, obj.last_name)).upper()


    # settings for individual displaing
    #exclude = ('parent',)
    #readonly_fields = ('tree', 'link',)




admin.site.register(Tree, TreeAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)

admin.site.register(Menu, MenuAdmin)