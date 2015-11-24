# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('ip_address_camera', models.CharField(primary_key=True, max_length=255, verbose_name='IP地址', serialize=False)),
                ('address_camera', models.CharField(max_length=255, verbose_name='相机位置')),
                ('status_camera', models.IntegerField(null=True, verbose_name='状态', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('ip_address_server', models.CharField(primary_key=True, max_length=255, verbose_name='服务器IP地址', serialize=False)),
                ('status_server', models.IntegerField(null=True, verbose_name='服务器是否正常', blank=True)),
                ('comments_server', models.CharField(max_length=128, verbose_name='备注', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='server_camera',
            field=models.ForeignKey(to='camera.Server', verbose_name='相机所属服务器', blank=True),
        ),
    ]
