# Generated by Django 2.1 on 2018-12-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseblog', '0005_auto_20181212_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymodel',
            name='sub_titre',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
