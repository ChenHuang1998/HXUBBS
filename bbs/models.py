from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='版块')
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, default=1)
    content = RichTextField(verbose_name='帖子内容')
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    priority = models.IntegerField(verbose_name='是否置顶',default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='版块名')
    image = models.ImageField(upload_to='categoryimg', default='categoryimg/beidouqixing.png')
    brief = models.CharField(max_length=128, default='欢迎查看本版块帖子',  verbose_name='版块简介')
    post_num = models.IntegerField(default=0, verbose_name='帖子数')

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128, verbose_name='主题')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='用户名')
    signature = models.CharField(max_length=128, blank=True, null=True, verbose_name='个性签名')
    image = models.ImageField(verbose_name='头像', default='imgs/default.png')

    def __str__(self):
        return self.name



