# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RunDoApp', '0003_auto_20171211_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddata',
            name='foodName',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
