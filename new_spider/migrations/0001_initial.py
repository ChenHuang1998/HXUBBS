# Generated by Django 2.2.1 on 2020-04-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('time', models.CharField(max_length=256, verbose_name='时间')),
                ('url', models.CharField(max_length=256, verbose_name='新闻地址')),
            ],
        ),
    ]
