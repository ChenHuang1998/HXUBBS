from django.urls import path
from userinfo.views import *
urlpatterns = [
    path('userinfo/', userinfo, name='userinfo'),
    path('modify_img/', modify_img, name='modify_img'),
    path('modify_info/', modify_info, name='modify_info'),
    path('del_post/', del_post, name='del_post')

]

