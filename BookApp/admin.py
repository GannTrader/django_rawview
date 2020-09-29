from django.contrib import admin

from BookApp.models import BookModel


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created', 'slug']
    list_filter = ['created']

admin.site.register(BookModel, BlogAdmin)
