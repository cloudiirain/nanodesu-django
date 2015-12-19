from django.contrib import admin
from nanodesu.models import Series, Post

class SeriesAdmin(admin.ModelAdmin):
    fields = ['title']

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'series', 'body' ]

admin.site.register(Series, SeriesAdmin)
admin.site.register(Post, PostAdmin)
