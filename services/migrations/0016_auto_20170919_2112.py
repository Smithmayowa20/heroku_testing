# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20170919_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_users',
            field=models.CharField(blank=True, help_text='tag single or several users with @username followed by space \n\t\t\t\n e.g @tanya340 @mark for several users\n and @tanya for single user', max_length=250, null=True),
        ),
    ]
