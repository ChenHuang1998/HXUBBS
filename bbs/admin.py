from django.contrib import admin
from bbs.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','category', 'theme', 'short_content', 'author', 'created_time']
    search_fields = ['content']
    list_display_links = ['id','category', 'theme', 'short_content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brief', 'post_num', 'image']
    list_display_links = ['id', 'name', 'brief']
    search_fields = ['name']


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['id', 'name', 'category']
    search_fields = ['name']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'signature']
    list_display_links = ['id', 'name', 'signature']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_display_links = ['id', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Notice,NoticeAdmin)

