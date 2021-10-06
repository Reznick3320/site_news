from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import NewCategory, New, Author


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'image', 'is_published')
    list_display_links = ('id', 'first_name', 'last_name')
    list_editable = ('is_published', )
    list_filter = ('is_published', )


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'category', 'is_published')
    list_display_links = ('id', 'header', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


admin.site.register(NewCategory)
admin.site.register(New, NewAdmin)
admin.site.register(Author, AuthorAdmin)
