# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-30 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_image_upload1_image_upload2_image_upload3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload1',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image_upload2',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image_upload3',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
