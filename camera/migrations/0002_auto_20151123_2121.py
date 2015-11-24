# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='status_camera',
            field=models.IntegerField(default=True, blank=True, verbose_name='状态'),
        ),
    ]
