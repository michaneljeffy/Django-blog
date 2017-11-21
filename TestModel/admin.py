"""用户管理工具"""
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.

class TagInline(admin.TabularInline):
    """Tag内联"""
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    """新建类"""
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
admin.site.register(Contact,ContactAdmin);
admin.site.register(Test)
