from django.contrib import admin
from bbs.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'theme', 'short_content', 'author', 'created_time']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(UserProfile)


