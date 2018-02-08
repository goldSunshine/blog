# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\xa0\x87\xe9\xa2\x98')),
                ('category', models.CharField(max_length=50, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\xa0\x87\xe7\xad\xbe', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe8\xb7\x9f\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
