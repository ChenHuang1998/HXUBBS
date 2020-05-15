from django.contrib import admin
from comment.models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_text', 'comment_time', 'user']
    list_display_links = ['id', 'get_text', 'comment_time', 'user']
    search_fields = ['get_text','user']

admin.site.register(Comment, CommentAdmin)
