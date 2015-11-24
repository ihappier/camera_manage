# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_auto_20151123_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='brand_camera',
            field=models.CharField(max_length=1, default='L', choices=[('H', '海康威视'), ('L', '南京吕诺')], verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='status_camera',
            field=models.CharField(max_length=1, default='T', choices=[('T', '正常'), ('F', '不通')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='server',
            name='ip_address_server',
            field=models.CharField(max_length=32, serialize=False, primary_key=True, verbose_name='服务器IP地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='status_server',
            field=models.CharField(max_length=1, default='T', choices=[('T', '正常'), ('F', '不通')], verbose_name='服务器是否正常'),
        ),
    ]
