# Generated by Django 2.2.1 on 2020-03-31 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unlikecount',
            old_name='liked_num',
            new_name='unliked_num',
        ),
        migrations.RenameField(
            model_name='unlikerecord',
            old_name='liked_time',
            new_name='unliked_time',
        ),
    ]