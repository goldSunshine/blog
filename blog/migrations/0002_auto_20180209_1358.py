# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xad\xa3\xe6\x96\x87', blank=True),
        ),
    ]
