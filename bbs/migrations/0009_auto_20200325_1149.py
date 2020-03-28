# Generated by Django 2.2.1 on 2020-03-25 11:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0008_auto_20200318_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '版块', 'verbose_name_plural': '版块'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '帖子', 'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': '主题', 'verbose_name_plural': '主题'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '自定义用户', 'verbose_name_plural': '自定义用户'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='帖子内容'),
        ),
    ]
