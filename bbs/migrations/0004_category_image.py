# Generated by Django 2.2.1 on 2020-03-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_category_post_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='categoryimg/beidouqixing.png', upload_to='categoryimg'),
        ),
    ]
