# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0004_auto_20151124_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camera',
            options={'verbose_name': '摄像机'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name': '服务器'},
        ),
        migrations.AlterModelTable(
            name='camera',
            table='list_camera',
        ),
        migrations.AlterModelTable(
            name='server',
            table='list_server',
        ),
    ]
