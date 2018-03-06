# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_zan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('art_id', models.IntegerField()),
                ('discuss', models.CharField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
            ],
        ),
    ]
