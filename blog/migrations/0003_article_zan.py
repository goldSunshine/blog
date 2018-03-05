# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180209_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='zan',
            field=models.IntegerField(default=0),
        ),
    ]
