from django.contrib import admin
from new_spider.models import *
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time']
    list_display_links = ['id', 'title']

admin.site.register(News, NewsAdmin)
