# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 00:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RunDoApp', '0002_auto_20171221_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddata',
            old_name='time_to_runnnnn',
            new_name='time_to_run',
        ),
    ]
