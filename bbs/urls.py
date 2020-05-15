from django.urls import path
from bbs.views import *


urlpatterns = [
    path('', index, name='index'),
    path('PostApi', PostList.as_view(), name='PostApi'),
    path('addpost/', addpost),
    path('login/', acc_login, name='login'),
    path('logout/', acc_logout, name='logout'),
    path('register/', register, name='register'),
    path('category/', category, name='category'),
    path('publish/', publish, name='publish'),
    path('categorydetail/', caregorydetail, name='categorydetail'),
    path('postdetail/<int:post_id>', postdetail, name='postdetail'),
    path('linked/', linked, name='linked'),
    path('search/', search, name='search'),
]
