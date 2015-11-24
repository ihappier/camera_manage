# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0006_auto_20151124_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='date_server',
            field=models.DateField(auto_now_add=True, verbose_name='投运时间'),
        ),
    ]
