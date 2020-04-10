from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='版块')
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, default=1)
    content = RichTextUploadingField(verbose_name='帖子内容')
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    read_num = models.IntegerField(verbose_name='点击量', default=0)
    priority = models.IntegerField(verbose_name='是否置顶',default=0)

    class Meta:
        ordering = ['-created_time']
        verbose_name = "帖子"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def short_content(self):
        if len(str(self.content)) > 30:
            return '{}...'.format(str(self.content)[0:29])
        else:
            return str(self.content)

    short_content.allow_tags = True
    short_content.short_description = 'content'


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='版块名')
    image = models.ImageField(upload_to='categoryimg', default='beidouqixing.png')
    brief = models.CharField(max_length=128, default='欢迎查看本版块帖子',  verbose_name='版块简介')
    post_num = models.IntegerField(default=0, verbose_name='帖子数')

    class Meta:

        verbose_name = "版块"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128, verbose_name='主题')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "主题"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='用户名')
    signature = models.CharField(max_length=128, blank=True, null=True, verbose_name='个性签名')
    gender = models.IntegerField(null=True, blank=True, verbose_name='性别')
    college = models.CharField(max_length=16, blank=True, null=True, verbose_name='学院')
    grade = models.CharField(max_length=16, blank=True, null=True, verbose_name='班级')
    image = models.ImageField(verbose_name='头像', upload_to='head_img', default='default.png')

    class Meta:
        verbose_name = "自定义用户"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



