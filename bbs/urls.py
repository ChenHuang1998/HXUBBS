from django.urls import path
from bbs.views import *


urlpatterns = [
    path('', index, name='index'),
    # path('addpost/', addpost),
    path('login/', acc_login, name='login'),
    path('logout/', acc_logout, name='logout'),
    path('category/', category, name='category'),
    path('categorydetail/', caregorydetail)
]
