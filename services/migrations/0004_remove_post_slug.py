# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170811_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
