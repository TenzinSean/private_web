# Generated by Django 2.1 on 2018-12-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseblog', '0004_auto_20181204_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymodel',
            name='context',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storymodel',
            name='pic',
            field=models.ImageField(default='', upload_to='pic_folder/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storymodel',
            name='titre',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
