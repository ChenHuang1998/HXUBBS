"""HXUBBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

favicon_view = RedirectView.as_view(url='/static/imgs/favicon.ico', permanent=True)

# 定制站点头部和标题
admin.site.site_title = '论坛后台管理'  # 站点标题
admin.site.site_header = '论坛后台管理'  # 站点头部

urlpatterns = [
    re_path(r'favicon\.ico$', favicon_view),
    re_path(r'favicon\.png$', favicon_view),
    path('admin/', admin.site.urls),
    path('', include('bbs.urls')),
    path('comment/', include('comment.urls')),
]
