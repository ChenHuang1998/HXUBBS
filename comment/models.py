from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from bbs.models import UserProfile
from ckeditor.fields import RichTextField
from django.utils.html import format_html
# Create your models here.


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = RichTextField(verbose_name='回复内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='回复时间')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments', verbose_name='回复人')

    root = models.ForeignKey('self', null=True, related_name='root_comment', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='parent_comment', on_delete=models.CASCADE)
    reply_to = models.ForeignKey(UserProfile, null=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['comment_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text

    def get_text(self):
        return format_html(self.text)



