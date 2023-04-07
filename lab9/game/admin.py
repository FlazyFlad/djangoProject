from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


def mark_sale(param):
    pass


class GameAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'title', 'get_html_photo')
    list_display_links = ('news_id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title", )}
    fields = ('title', 'slug', 'category_id', 'content', 'image', 'get_html_photo', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50px>")

    get_html_photo.short_description = "Картина/Фото"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'desciption')
    list_display_links = ('category_id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(News, GameAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Game News'
admin.site.site_header = 'Game News'