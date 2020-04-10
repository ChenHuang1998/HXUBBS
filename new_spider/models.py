from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    time = models.CharField(max_length=256, verbose_name='时间')
    url = models.CharField(max_length=256, verbose_name='新闻地址')

    class Meta:
        verbose_name = "新闻"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

