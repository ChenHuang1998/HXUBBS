from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from bbs.models import UserProfile
# Create your models here.

class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    liked_num = models.IntegerField(default=0, verbose_name='点赞数')


class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='点赞人')
    liked_time = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')


class UnLikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    unliked_num = models.IntegerField(default=0, verbose_name='不喜欢数')


class UnLikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='不喜欢用户')
    unliked_time = models.DateTimeField(auto_now_add=True, verbose_name='踩时间')
