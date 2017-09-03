# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-26 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20170813_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ManyToManyField(blank=True, related_name='file_upload', to='services.File_upload'),
        ),
    ]