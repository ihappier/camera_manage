# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0003_auto_20151124_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='date_camera',
            field=models.DateField(default=datetime.datetime(2015, 11, 24, 3, 6, 58, 673511, tzinfo=utc), verbose_name='投运时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='date_server',
            field=models.DateField(default=datetime.datetime(2015, 11, 24, 3, 7, 14, 446593, tzinfo=utc), verbose_name='投运时间'),
            preserve_default=False,
        ),
    ]
