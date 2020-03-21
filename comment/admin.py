from django.contrib import admin
from comment.models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'comment_time', 'user']


admin.site.register(Comment, CommentAdmin)
