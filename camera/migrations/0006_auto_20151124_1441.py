# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0005_auto_20151124_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='date_camera',
            field=models.DateField(verbose_name='投运时间', auto_now_add=True),
        ),
    ]
