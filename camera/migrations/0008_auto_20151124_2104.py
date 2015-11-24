# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0007_auto_20151124_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camera',
            options={'verbose_name_plural': '摄像机'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name_plural': '服务器'},
        ),
    ]
