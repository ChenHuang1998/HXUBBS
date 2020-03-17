from django.contrib import admin
from bbs.models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(UserProfile)

