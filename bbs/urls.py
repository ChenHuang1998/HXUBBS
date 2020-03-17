from django.urls import path
from bbs.views import *


urlpatterns = [
    path('', index, name='index'),
    # path('addpost/', addpost),
    path('login/', acc_login, name='login'),
    path('logout/', acc_logout, name='logout'),
    path('register/', register, name='register'),
    path('category/', category, name='category'),
    path('publish/', publish, name='publish'),
    path('categorydetail/', caregorydetail),
    path('postdetail/<int:post_id>', postdetail, name='postdetail'),
    path('linked/', linked, name='linked'),
]
