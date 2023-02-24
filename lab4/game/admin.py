from django.contrib import admin

from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'title', 'image')
    list_display_links = ('news_id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name')
    list_display_links = ('category_id', 'name')
    search_fields = ('name',)

admin.site.register(News, GameAdmin)
admin.site.register(Category, CategoryAdmin)